from sqlalchemy.orm import Session
from entity.models import Movie,User

import json

async def create_movie(movie_data, db: Session):
    try:
        print("data2-",f"{movie_data.dict()}")

        new_movie = Movie(**movie_data.dict())

        db.add(new_movie)
        db.commit()
        db.refresh(new_movie)
        return new_movie
    except Exception as ex:
        db.rollback()
        raise ex
    
async def create_user(user_data,db):
    try:
        user_data_json=json.load(user_data)
        data={
            "email":user_data_json.email,
            "hashed_password":user_data_json.password,
            "is_active":1
        }
        new_user=User(data)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except Exception as ex:
        raise ex
