from sqlalchemy.ext.asyncio import AsyncSession

import api.models.score as score_model
import api.models.user as user_model

from typing import List, Tuple, Optional
from sqlalchemy import desc, select,func
from sqlalchemy.engine import Result
#import logging



async def get_rank_list(db:AsyncSession) -> List[Tuple[int,str,int]]:
  
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
    
    result=[]
    for i in range(len(rate_list_sorted)):
        dic_append={
            "id":rate_list_sorted[i][0],
            "name":rate_list_sorted[i][2],
            "rate":rate_list_sorted[i][1],
            "rank":rate_list_sorted[i][3],
        }
        result.append(dic_append)
    return result

async def get_user_rank_list(db:AsyncSession, user_id: int) -> Tuple[int, str,int,int]:

    #logger = logging.getLogger('uvicorn')
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
    

    result={
        "top_three": [],
        "self": {
            "id": 0,
            "name": "伊藤大輝",
            "rate": 0,
            "rank": 0
        },
        "higher_around_rank_users": [],
        "lower_around_rank_users": []
    }

    

    #top_three
    top_three_list=[]
    top_three_list=rate_list_sorted[0:3]
    for i in range(len(top_three_list)):
        dic_append={
            "id":top_three_list[i][0],
            "name":top_three_list[i][2], 
            "rate":top_three_list[i][1],
            "rank":top_three_list[i][3]
        }
        result["top_three"].append(dic_append)
        


    #self
    self_index=0
    for i in range(len(rate_list_sorted)):
        if rate_list_sorted[i][0]==user_id:
            result["self"]["id"]=rate_list_sorted[i][0]
            result["self"]["name"]=rate_list_sorted[i][2]
            result["self"]["rate"]=rate_list_sorted[i][1]
            result["self"]["rank"]=rate_list_sorted[i][3]

            self_index=i
            break
    
    #higher_around_rank_users
    #selfより上5件取得
    higher_around_rank_list=[]
    if self_index < 5:
        higher_around_rank_list=rate_list_sorted[0:self_index]
    else:
        higher_around_rank_list=rate_list_sorted[self_index-5:self_index]
    

    #resultに代入
    for i in range(len(higher_around_rank_list)):
        dic_append={
            "id":higher_around_rank_list[i][0],
            "name":higher_around_rank_list[i][2],                "rate":higher_around_rank_list[i][1],
            "rank":higher_around_rank_list[i][3],
        }
        result["higher_around_rank_users"].append(dic_append)
        
    

    #lower_around_rank_users
    #selfより下5件取得
    lower_around_rank_list=[]

    if len(rate_list_sorted)-self_index==1:
        pass
    elif len(rate_list_sorted)-self_index<6:
        lower_around_rank_list=rate_list_sorted[self_index+1:self_index+(len(rate_list_sorted)-self_index)]
    else:
        lower_around_rank_list=rate_list_sorted[self_index+1:self_index+6]

    
    #lower result代入
    for i in range(len(lower_around_rank_list)):
        dic_append={
            "id":lower_around_rank_list[i][0],
            "name":lower_around_rank_list[i][2],
            "rate":lower_around_rank_list[i][1],
            "rank":lower_around_rank_list[i][3],
        }
        result["lower_around_rank_users"].append(dic_append)

    return result
