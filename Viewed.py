import sqlalchemy as sq
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session
from token import database

metadata = MetaData()
Base = declarative_base()

class Viewed(Base):
    __tablename__ = 'viewed'
    profile_id = sq.Column(sq.Integer, primary_key=True)
    worksheet_id = sq.Column(sq.Integer, primary_key=True)
# добавление записи в бд

def add_user():
    engine = create_engine(database)
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        to_bd = Viewed(profile_id = user_id, worksheet_id = user['id'])
        session.add(to_bd)
        session.commit()

# извлечение записей из БД
def check_user():
    engine = create_engine(database)
    with Session(engine) as session:
        from_bd = session.query(Viewed).filter(Viewed.profile_id == user_id, Viewed.worksheet_id == user['id']).first()
        return True if from_bd else Fals






