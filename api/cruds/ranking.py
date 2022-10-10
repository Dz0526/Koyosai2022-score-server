from sqlalchemy.ext.asyncio import AsyncSession

import api.models.score as score_model
import api.models.user as user_model

from typing import List, Tuple, Optional
from sqlalchemy import desc, select,func
from sqlalchemy.engine import Result
import logging






    

async def get_rank_list(db:AsyncSession, user_id: int) -> Tuple[int, str,int]:

    
    
    
    logger = logging.getLogger('uvicorn')    
    #一番高いレートを出す
    #ユーザー1人1人の最高値レートを一度出す
    return_rate_list=db.query(
        score_model.Score.user_id,
        func.max(score_model.Score.rate),
        ).group_by(score_model.Score.user_id).all()

    #一旦編集可能なlistに
    rate_list=[]
    for user_rate in return_rate_list:
        rate_list.append(list(user_rate))

    #name追加
    user_name=""
    for i in range(len(rate_list)):
        user_name=db.query(user_model.User.name).filter(user_model.User.id == rate_list[i][0]).all()[0][0]
        rate_list[i].append(user_name)

    #selfのmax_rateを取得
    for i in range(len(rate_list)):
        if user_id==rate_list[i][0]:
            self_rate=rate_list[i][2]
    
    rate_list_sorted=sorted(rate_list,reverse=True,key=lambda x: x[1])
    

    #ランク算出
    rate_list_sorted[0].append(1)
    rank=0
    for i in range(len(rate_list_sorted)):
        rank=i+1
        if i==0:
            pass
        elif rate_list_sorted[i][1]==rate_list_sorted[i-1][1]:
            rank-=1
            rate_list_sorted[i].append(rank)
        else:
            rate_list_sorted[i].append(rank)

    #first
    first_list=[]
    first_list.append(rate_list_sorted[0][0])
    first_list.append(rate_list_sorted[0][1])
    first_list.append(rate_list_sorted[0][2])
    first_list.append(rate_list_sorted[0][3])

    #self
    self_list=[]
    self_index=0
    for i in range(len(rate_list_sorted)):
        if rate_list_sorted[i][0]==user_id:
            self_list.append(rate_list_sorted[i][0])
            self_list.append(rate_list_sorted[i][1])
            self_list.append(rate_list_sorted[i][2])
            self_list.append(rate_list_sorted[i][3])
            self_index=i
            break
    
    #higher_around_rank_users
    #selfより上5件取得
    higher_around_rank_list=[]
    if len(rate_list_sorted)<8:
        higher_around_rank_list=rate_list_sorted[1:self_index]
    else:
        higher_around_rank_list=rate_list_sorted[self_index-4:self_index]

    #lower_around_rank_users
    #selfより下5件取得
    lower_around_rank_list=[]

    if len(rate_list_sorted)-self_index==1:
        pass
    elif len(rate_list_sorted)-self_index<6:
        lower_around_rank_list=rate_list_sorted[self_index+1:self_index+(len(rate_list_sorted)-self_index)]
    else:
        lower_around_rank_list=rate_list_sorted[self_index+1:self_index+6]

    dic_higher_around_rank=[]
    dic_lower_around_rank=[]
    for i in higher_around_rank_list:
        dic_higher_around_rank.append({*i})
    for i in lower_around_rank_list:
        dic_lower_around_rank.append({*i})
        

    result={"first":{*first_list},"self":{*self_list},"higher_around_rank_users":dic_higher_around_rank,"lower_around_rank_users":dic_lower_around_rank}
    logger.info(first_list)
    logger.info(self_list)
    logger.info(higher_around_rank_list)
    logger.info(lower_around_rank_list)
    logger.info(rate_list_sorted)

    #logger.info(result)

    

    return result
