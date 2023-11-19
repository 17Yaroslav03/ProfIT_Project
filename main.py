from fastapi import FastAPI, Path, Header, Body
from pydantic import BaseModel
from typing import Any, List
from fastapi import FastAPI, Response, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from typing_extensions import Annotated
from cruds import db_get_all_hobby, db_add_user_discription, check_user_exist, db_get_user_me, db_add_user_hobby, db_get_hobby, db_get_people_in_group
from typing import Union
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing_extensions import Annotated
from fastapi_login import LoginManager
from fastapi.responses import FileResponse
from typing import Union
import os


app = FastAPI()


def parse_cookie_for_bearer_token(t: str):
    pos = t.find("Bearer")
    if pos == -1:
        return ""
    pos2 = t.find("\"", pos+1)
    if pos2 == -1:
        return ""
    token = t[pos+7:pos2]
    return token


def check_directory(path, file_name):
    t = '.jpg'
    files_list = os.listdir(path)
    for i in files_list:
        if i == file_name + t:
            return True
    return False    


origins = [
    "http://localhost",
    "http://localhost:80",
    "http://194.87.147.11",
    "http://194.87.147.11:80",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class UserDiscription(BaseModel):
    tg_login: str
    discription: str


class UserHobby(BaseModel):
    tg_login: str
    hobby_id: str


class Hobby(BaseModel):
    id: int
    name: str
    discription: str
    avatar_link: str
    chat_id: str


class AboutMe(BaseModel):
    discription: str
    hobby: List[int] 


class LoginModel(BaseModel):
    tg_login: str
    password: str


#Получить список всех хобби
@app.get("/hobby", response_model=List[Hobby])
def get_all_hobby():
    return db_get_all_hobby()


@app.get("/hobby/{id}")
def get_one_hobby(id: int)-> Hobby:
    return db_get_hobby(id)


@app.post("/login")
async def login(response: Response, data: LoginModel):
    if not check_user_exist(data.tg_login, data.password):
        raise HTTPException(status_code=400, detail="Incorrect username or password or no activate telegramm bot")
    access_token = data.tg_login
    response.set_cookie(key="access_token",value=f"Bearer {access_token}", httponly=True)


@app.post("/logout")
def logout(response: Response):
    response.delete_cookie(key="access_token")


@app.get("/me",  response_model=Union[AboutMe, str])
def info_about_me(request: Request):
    t = request.headers.get("cookie")
    if not isinstance(t, str):
        print("No token")
        #ошибка доступа
        return "not auth"
    tg_login = parse_cookie_for_bearer_token(t)
    return db_get_user_me(tg_login)

    
@app.post("/aboutme")
def add_my_discription(dis: str, request: Request):
    t = request.headers.get("cookie")
    if not isinstance(t, str):
        print("No token")
        #ошибка доступа
        return "not auth"
    tg_login = parse_cookie_for_bearer_token(t)
    db_add_user_discription(tg_login, dis)


@app.post("/addhobby")
def add_me_hobby(id_hob: int, request: Request):
    t = request.headers.get("cookie")
    if not isinstance(t, str):
        print("No token")
        #ошибка доступа
        return "not auth"
    tg_login = parse_cookie_for_bearer_token(t)
    db_add_user_hobby(tg_login, id_hob)


@app.get("/photo/{tg_login}")
def download_file(tg_login: str):
    if check_directory("./photo", tg_login):
        return FileResponse(path=f'./photo/{tg_login}.jpg', filename=f'{tg_login}.jpg', media_type='multipart/form-data')
    else:
        return FileResponse(path=f'./ava.jpg', filename='ava.jpg', media_type='multipart/form-data')


@app.get("/group/{id}")
def get_people(id: int) -> List[str]:
    return db_get_people_in_group(id)