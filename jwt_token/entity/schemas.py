from pydantic import BaseModel

class CreateMovie(BaseModel):
    name: str

    class Config:
        from_attributes = True

class CreateUser(BaseModel):
    email:str
    password:str