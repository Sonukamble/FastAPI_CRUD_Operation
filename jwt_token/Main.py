from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from database import get_db
from entity.schemas import CreateMovie, CreateUser
from operation.CRUD import create_movie, create_user

app = FastAPI()


@app.post("/create/movie")
async def create_movies(movies: CreateMovie, db: Session = Depends(get_db)):
    try:
        print("data-", f"{movies}")
        response = await create_movie(movies, db)
        if response:
            return JSONResponse(content={"message": "successful"})
    except Exception as ex:
        return JSONResponse(content={"error": str(ex)}, status_code=500)


@app.post("/creating/user")
async def create_users(users: CreateUser, db: Session = Depends(get_db)):
    try:
        response = await create_user(users, db)
        if response:
            return JSONResponse(content={"message": "successful"})
    except Exception as ex:
        return JSONResponse(content={"error": str(ex)}, status_code=500)
