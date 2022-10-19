
from fastapi import Depends
from database import local_session
import api.models.user as user_model
import api.models.score as score_model


db=local_session()

def seed():
    
    #一人目
    user = user_model.User(name='田中ちゃん')
    db.add(user)
    db.commit()
    for i in range(2):
        user_id=db.query(user_model.User.id).filter(user_model.User.name=='田中ちゃん')
        score = score_model.Score(user_id = user_id,rate=i*1)
        db.add(score)
        db.commit()
    db.refresh(user)
    db.refresh(score)
    #二人目
    user = user_model.User(name='村井源太')
    db.add(user)
    db.commit()
    for i in range(2):
        user_id=db.query(user_model.User.id).filter(user_model.User.name=='村井源太')
        score = score_model.Score(user_id = user_id,rate=i*5)
        db.add(score)
        db.commit()
    db.refresh(user)
    db.refresh(score)
    #三人目
    user = user_model.User(name='伊藤大輝')
    db.add(user)
    db.commit()
    for i in range(2):
        user_id=db.query(user_model.User.id).filter(user_model.User.name=='伊藤大輝')
        score = score_model.Score(user_id = user_id,rate=i*10)
        db.add(score)
        db.commit()
    db.refresh(user)
    db.refresh(score)
    #4人目
    user = user_model.User(name='plmwa')
    db.add(user)
    db.commit()
    for i in range(2):
        #id3とあえて同じrate
        user_id=db.query(user_model.User.id).filter(user_model.User.name=='plmwa')
        score = score_model.Score(user_id = user_id,rate=i*10)
        db.add(score)
        db.commit()
    db.refresh(user)
    db.refresh(score)
    #5人目
    user = user_model.User(name='cha')
    db.add(user)
    db.commit()
    for i in range(2):
        user_id=db.query(user_model.User.id).filter(user_model.User.name=='cha')
        score = score_model.Score(user_id = user_id,rate=i*20)
        db.add(score)
        db.commit()
    db.refresh(user)
    db.refresh(score)
    #6人目
    user = user_model.User(name='Test1')
    db.add(user)
    db.commit()
    for i in range(2):
        user_id=db.query(user_model.User.id).filter(user_model.User.name=='Test1')
        score = score_model.Score(user_id = user_id,rate=i*30)
        db.add(score)
        db.commit()
    db.refresh(user)
    db.refresh(score)
    #7人目
    user = user_model.User(name='Test2')
    db.add(user)
    db.commit()
    for i in range(2):
        user_id=db.query(user_model.User.id).filter(user_model.User.name=='Test2')
        score = score_model.Score(user_id = user_id,rate=i*40)
        db.add(score)
        db.commit()
    db.refresh(user)
    db.refresh(score)
    #8人目
    user = user_model.User(name='Test4')
    db.add(user)
    db.commit()
    for i in range(2):
        user_id=db.query(user_model.User.id).filter(user_model.User.name=='Test4')
        score = score_model.Score(user_id = user_id,rate=i*60)
        db.add(score)
        db.commit()
    db.refresh(user)
    db.refresh(score)
    #9人目
    user = user_model.User(name='Test5')
    db.add(user)
    db.commit()
    for i in range(2):
        user_id=db.query(user_model.User.id).filter(user_model.User.name=='Test5')
        score = score_model.Score(user_id = user_id,rate=i*30)
        db.add(score)
        db.commit()
    db.refresh(user)
    db.refresh(score)
    #10人目
    user = user_model.User(name='Test6')
    db.add(user)
    db.commit()
    for i in range(2):
        user_id=db.query(user_model.User.id).filter(user_model.User.name=='Test6')
        score = score_model.Score(user_id = user_id,rate=i*70)
        db.add(score)
        db.commit()
    db.refresh(user)
    db.refresh(score)
   
    



if __name__ == '__main__':
    BOS = '\033[92m'  # 緑色表示用
    EOS = '\033[0m'

    print(f'{BOS}Seeding data...{EOS}')
    seed()