from pydantic import BaseModel

class UserAddSchema(BaseModel):
    username: str 
    password: str 
    role: str

class UserSchema(UserAddSchema):
    id: int