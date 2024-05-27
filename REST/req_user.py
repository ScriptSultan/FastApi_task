from typing import Annotated

from fastapi import APIRouter, Depends, Request
from starlette.responses import Response

from REST.users import SUserSignUp, SOkResponse, Simple, SUserLogin, SUserEdit
from models.models import Users, Session
from other_foo.private import encode_jwt, get_user_id_by_token
from sqlalchemy import select, update

users = APIRouter(
    prefix="/api/v1/user",
    tags=['Authentication and Authorization'],
)


@users.post('/register', status_code=201)
def registration(param: Annotated[SUserSignUp, Depends()]):
    lala = param.model_dump()
    print(lala)
    with Session() as session:
        user = Users(**lala)
        print(user)
        session.add(user)
        session.flush()
        session.commit()
    return SOkResponse()


@users.post('/login')
def login(param: Annotated[SUserLogin, Depends()], response: Response):
    data = param.model_dump()
    email = data['email']
    password = data['password']
    with Session() as session:
        user = session.execute(select(Users.id, Users.password).filter_by(email=email))
        user_info = user.first()
    if user_info[1] != password:
        return {'Status': False, 'description': 'Неверный пароль'}
    payload = {'sub': user_info[0]}

    new_token = encode_jwt(payload)
    response.set_cookie(key='token', value=new_token, expires=600)

    return {'Status': True, 'description': 'Можете пользоваться сайтом'}


@users.get('/profile', status_code=200)
def get_profile(request: Request):
    user_id = get_user_id_by_token(request=request)
    with Session() as session:
        response = session.execute(select(Users).filter_by(id=user_id))
        resp = response.first()
        if not resp:
            return False
        user = [Simple.model_validate(result, from_attributes=True) for result in resp]
        return user[0]


@users.patch('/profile')
def edit_profile(param: Annotated[SUserEdit, Depends()], request: Request):
    user_id = get_user_id_by_token(request=request)
    data = param.model_dump()
    with Session() as session:
        response = session.execute(update(Users).filter_by(id=user_id).values(**data).returning(Users))
        resp = response.first()
        session.commit()
    user = [SUserEdit.model_validate(result, from_attributes=True) for result in resp]
    return user[0]








