
from database import local_session
import api.models.user as user_model
import api.models.score as score_model


db=local_session()

def seed():
    name_list=['田中ちゃん','村井','Test1','Test2','Test3','Test4','Test5','Test6','Test7','Test8']

    #一人目
    for i in range(10):
        user = user_model.User(name=name_list[i])
        db.add(user)
        db.commit()
        for j in range(2):
            user_id=db.query(user_model.User.id).filter(user_model.User.name==name_list[i])
            score = score_model.Score(user_id = user_id,rate=(j+1)*(i+1))
            db.add(score)
            db.commit()
        db.refresh(user)
        db.refresh(score)
if __name__ == '__main__':
    BOS = '\033[92m'  # 緑色表示用
    EOS = '\033[0m'

    print(f'{BOS}Seeding data...{EOS}')
    seed()