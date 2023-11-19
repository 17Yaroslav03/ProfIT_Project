from database import engine, User, Groups, Hobby
from sqlalchemy.orm import Session
import json
from utils import add_user


def db_get_hobby(id):
    with Session(autoflush=False, bind=engine) as session:
        b = session.query(Hobby).where(Hobby.id == id).one().as_dict()
    return b


def db_get_all_hobby():
    with Session(autoflush=False, bind=engine) as session:
        b = session.query(Hobby).all()

    return list(map(lambda x: x.as_dict(), b))


def check_user_exist(tg_login: str, password: str) -> bool:
    with Session(autoflush=False, bind=engine) as session:
        b = session.query(User).where(User.tg_login == tg_login and User.password == password)
    return len(b.all()) != 0


def db_add_user_discription(tg_login: str, discription: str):
    with Session(autoflush=False, bind=engine) as session:
        user = User(tg_login=tg_login, discription=discription)
        session.query(User).where(User.tg_login == tg_login).update({User.discription : discription})
        session.commit()


def db_add_user_hobby(tg_login: str, hobby_id: int):
    with Session(autoflush=False, bind=engine) as session:
        t = session.query(Groups).where(Groups.id == hobby_id and Groups.tg_login == tg.login).all()
    if len(t) > 0:
        return
    with Session(autoflush=False, bind=engine) as session:
        group = Groups(tg_login=tg_login, id_hobby=hobby_id)
        session.add(group)
        session.commit()


def db_get_user_me(user_tg_login):
    with Session(autoflush=False, bind=engine) as session:
        b = session.query(User).where(User.tg_login == user_tg_login).one()   
    if b is None:
        return
    user = b.as_dict()
    with Session(autoflush=False, bind=engine) as session:
        h = session.query(Groups).where(Groups.tg_login == user_tg_login).all()
    hs = list(map(lambda x: x.id_hobby, h))
    ans = {"discription": user['discription'],
    "hobby": hs}
    return ans


def db_utils_add_hobby(id, name, discription, chat_id, avatar_link):
    h = Hobby(id=id, name=name, discription=discription, chat_id=chat_id, avatar_link=avatar_link)
    with Session(autoflush=False, bind=engine) as session:
        session.add(h)
        session.commit()


def add_fake_people_hobby_groups():
    db_utils_add_hobby(1, "Чтение книг", "В этой группе собраны любители погрузиться в уникальные миры и пережить незабываемые приключения сидя на диване. Обсуждайте свои любимые произведения, делитесь интересными книгами и узнавайте смешные факты из жизни писателей с такими же книгоманами как и вы!", "https://t.me/+174U5OUsbP8yOTcy", "photo1")
    db_utils_add_hobby(2, "Кино", "В этой группе вы найдете людей, которые, как и вы, находят удовольствие в исследовании различных историй, открывают для себя новых режиссеров и актеров. Они не отталкиваются от жанров, эти ребята могут выбрать любой сюжет, чтобы полностью погрузиться в мир киноискусства", "https://t.me/+0ZLgtWW6dQ9lYmM6", "photo2")
    db_utils_add_hobby(3, "Музыка", "Хотите познакомиться с настоящими волшебниками? Тогда тебе точно сюда! Ведь умение превращать звуки в настоящие чарующие мелодии, которые сразу отправляют слушателя в небольшое путешествие - это настоящая магия! Вступайте в группу, делитесь своим творчеством и просто находите ребят с похожими музыкальными вкусами", "https://t.me/+bGoUllvXag0yZTUy", "photo3")
    db_utils_add_hobby(4, "Бильярд", "Любите погружаться в мир бесконечной стратегии, азарта и точности? Вступай в группу любителей бильярда. Каждая игра - это целая история, в которой сердце бьется в ритме каждого удара и каждое попадание добавляет тебе уверенности", "https://t.me/+fYEWs79HiptjYjhi", "photo4")
    db_utils_add_hobby(5, "Футбол", "Здесь Вы найдете энтузиастов, объединенных общей страстью к футболу. В группе люди собираются для игры в футбол, обсуждения последних новостей и матчей, обмена опытом и просто веселого времяпрепровождения. Здесь каждый имеет возможность проявить свои футбольные навыки и научиться чему-то новому", "https://t.me/+OZWKMzHdNngyZjFi", "photo5")
    add_user("@vova_minle1", "qwerty")
    add_user("@vova_minle2", "qwerty")
    add_user("@vova_minle3", "qwerty")
    add_user("@vova_minle4", "qwerty")
    add_user("@vova_minle5", "qwerty")
    add_user("@vova_minle6", "qwerty")
    add_user("@vova_minle7", "qwerty")
    add_user("@vova_minle8", "qwerty")
    add_user("@vova_minle9", "qwerty")
    add_user("@vova_minle10", "qwerty")
    add_user("@vova_minle11", "qwerty")
    add_user("@vova_minle12", "qwerty")
    db_add_user_discription("@vova_minle1", "Интересный человек")
    db_add_user_discription("@vova_minle2", "Умный человек")
    db_add_user_discription("@vova_minle3", "Добрый человек")
    db_add_user_discription("@vova_minle4", "Веселый человек")
    db_add_user_discription("@vova_minle5", "Прямой человек")
    db_add_user_discription("@vova_minle6", "Честный человек")
    db_add_user_discription("@vova_minle7", "Загадочный человек")
    db_add_user_discription("@vova_minle8", "Игривый человек")
    db_add_user_discription("@vova_minle9", "Занятой человек")
    db_add_user_discription("@vova_minle10", "Дружелюбный человек")
    db_add_user_discription("@vova_minle11", "Целеустремеленный человек")
    db_add_user_discription("@vova_minle12", "Внимательный человек")
    db_add_user_hobby("vova_minle1", 1)
    db_add_user_hobby("vova_minle2", 1)
    db_add_user_hobby("vova_minle3", 1)
    db_add_user_hobby("vova_minle4", 1)
    db_add_user_hobby("vova_minle5", 1)
    db_add_user_hobby("vova_minle6", 1)
    db_add_user_hobby("vova_minle7", 1)
    db_add_user_hobby("vova_minle8", 1)
    db_add_user_hobby("vova_minle9", 2)
    db_add_user_hobby("vova_minle10", 2)
    db_add_user_hobby("vova_minle11", 2)
    db_add_user_hobby("vova_minle12", 2)
    db_add_user_hobby("vova_minle1", 2)
    db_add_user_hobby("vova_minle2", 2)
    db_add_user_hobby("vova_minle3", 2)
    db_add_user_hobby("vova_minle4", 2)
    db_add_user_hobby("vova_minle5", 3)
    db_add_user_hobby("vova_minle6", 3)
    db_add_user_hobby("vova_minle7", 3)
    db_add_user_hobby("vova_minle8", 3)
    db_add_user_hobby("vova_minle9", 3)
    db_add_user_hobby("vova_minle10", 3)
    db_add_user_hobby("vova_minle11", 3)
    db_add_user_hobby("vova_minle12", 3)
    db_add_user_hobby("vova_minle12", 4)
    db_add_user_hobby("vova_minle11", 4)
    db_add_user_hobby("vova_minle10", 4)
    db_add_user_hobby("vova_minle1", 5)
    db_add_user_hobby("vova_minle2", 5)
    db_add_user_hobby("vova_minle3", 5)
    db_add_user_hobby("vova_minle4", 5)
    db_add_user_hobby("vova_minle7", 5)


def clean_database():
    with Session(autoflush=False, bind=engine) as session:
        b = session.query(Groups).delete()
        session.commit()
    
    with Session(autoflush=False, bind=engine) as session:
        b = session.query(User).delete()
        session.commit()

    with Session(autoflush=False, bind=engine) as session:
        b = session.query(Hobby).delete()
        session.commit()


def db_get_people_in_group(id):
    with Session(autoflush=False, bind=engine) as session:
        b = session.query(Groups).where(Groups.id_hobby == id).all()
    
    t = list(map(lambda x: x.tg_login, b))
    return t
