from database import User, engine
import random, string
from sqlalchemy.orm import Session


def check_user_exist(tg_login: str, password: str) -> bool:
    with Session(autoflush=False, bind=engine) as session:
        b = session.query(User).where(User.tg_login == tg_login and User.password == password)
    return len(b.all()) != 0


def add_user(tg_login: str, password: str):
    with Session(autoflush=False, bind=engine) as session:
        b = session.query(User).where(User.tg_login == tg_login).count()
        session.commit()
    if b != 0:
        return
    user = User(tg_login=tg_login, password=password)
    with Session(autoflush=False, bind=engine) as session:
        b = session.add(user)
        session.commit()


def generate_password():
    letters = 'qwertyuiopasdfghjklzxcvbnm'
    return ''.join(letters[random.randint(0, len(letters) - 1)] for i in range(7))