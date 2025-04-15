from fastapi import APIRouter

from database import SessionDep
from user_service.schemas import UserAddSchema
from user_service.models import UserModel

router = APIRouter()

@router.get('/')
async def greet():
    return {'status': 'success', 'service': 'user_service'}

@router.post('/registration/')
async def user_reg(user_data: UserAddSchema, session: SessionDep):
    new_user = UserModel(
        username = user_data.username,
        hashed_password = user_data.password,
        role = user_data.role
    )
    print(type(session))
    session.add(new_user)
    await session.commit()
    return {'status': 'sucess'}

@router.post('/login/')
async def user_login():
    pass

@router.get('/me/')
async def get_user():
    pass

@router.get('/users/{user_id}')
async def identity_verification():
    pass