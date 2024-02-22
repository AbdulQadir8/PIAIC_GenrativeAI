from typing import Optional
from sqlmodel import SQLModel, Field, create_engine, Session, select


class Hero(SQLModel,table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None

database_conn_str = "postgresql://aq98123:Uvl4GXM6fHbB@ep-muddy-leaf-a5jvs6z0.us-east-2.aws.neon.tech/fastapi_dev?sslmode=require"
engine = create_engine(database_conn_str, echo=True)

def create_hero():
    hero1 = Hero(name="Ameen Alam",secret_name="AM")
    hero2 = Hero(name="Junaid",secret_name="JU")
    hero3 = Hero(name="Zeeshan",secret_name="ZE")

    session = Session(engine)
    session.add(hero1)
    session.add(hero2)
    session.add(hero3)
    session.commit()
    session.close()

def get_hero():
    session = Session(engine)
    # statement = select(Hero).where(Hero.name=="Junaid")
    # statement = select(Hero).where(Hero.name!="Junaid")
    # statement = select(Hero).where(Hero.id == 3)
    # statement = select(Hero).limit(2)
    # statement = select(Hero).offset(4).limit(2)
    # statement = select(Hero.id)
    statement = select(Hero.id, Hero.name)

    result = session.exec(statement)
    # print(result)
    # print(result.first())
    print(result.all())
    # for hero in result:
    #     print("Individual")
    #     print(hero.secret_name)

def update_hero():
    session = Session(engine)
    statement = select(Hero).where(Hero.name == "Ameen Alam")
    result = session.exec(statement).first()
    print(result)
    result.age = 25
    session.add(result)
    session.commit()
    print("Updated Data")
    print(result)
    session.close()

def delete_hero():
    session = Session(engine)
    statement = select(Hero).where(Hero.id==3)
    result = session.exec(statement).first()
    print(result)
    session.delete(result)
    session.commit()
    session.close()

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


if __name__=="__main__":
    # create_db_and_tables()
    # create_hero()
    # get_hero()
    # update_hero()
    delete_hero()