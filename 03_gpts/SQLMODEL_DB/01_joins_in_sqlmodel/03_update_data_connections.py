from typing import Optional
from sqlmodel import Field, SQLModel, create_engine, Session, select, delete
from dotenv import load_dotenv, find_dotenv
from os import getenv

_:bool = load_dotenv(find_dotenv())


#02 create a team table with columns: id, name, and headquarters.
class Team(SQLModel, table=True):
    """
    create a Team table with columns: id, name, and headquarters.
    """
    id: Optional[int] = Field(primary_key=True)
    name: str
    headquarters : str




class Hero(SQLModel, table=True):
    """
    Create a hero table with 
    Columns: id, name, secret_name, age, team_id.
    foreign key: team_id refrences id in Team table.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str 
    age: Optional[int] = Field(default=None, index=True)
    #03 add team_id as a foreign key in Hero table
    team_id: Optional[int] = Field(default=None, foreign_key="team.id")


#04 create a database engine using create_engine
postgres_sql = getenv("POSTGRES_SQL")
engine = create_engine(postgres_sql, echo=True)

#05 create a function create_db_and_tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def create_heroes():
    #01 create session
    with Session(engine) as session:
        hero_spider_man = Hero(name="Peter Paker", secret_name="Spiderman")
        session.add(hero_spider_man)
        session.commit()

def select_heroes_by_where():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.team_id == 2)
        results = session.exec(statement)
        heroes = results.all()
        print("Heroes:",heroes)
    # 01 create a session
    # 02 create a statement to select all heroes using where
        
def select_heroes_by_join():
    with Session(engine) as session:
        statement = select(Hero).join(Team)
        results = session.exec(statement)
        heroes = results.all()
        print("Heroes:",heroes)

def select_heroes_by_left():
    with Session(engine) as session:
        statement = select(Hero).join(Team, isouter=True)
        results = session.exec(statement)
        heroes = results.all()
        print("Heroes",heroes)

def select_heroes_by_full():
    with Session(engine) as session:
        statement = select(Hero).join(Team, full=True)
        results = session.exec(statement)
        heroes = results.all()
        print("Heroes",heroes)
    
def update_heroes():
    with Session(engine) as session:
        stmt = select(Hero).where(Hero.secret_name == "Spiderman")
        hero = session.exec(stmt).one()
        hero.team_id = 1
        session.add(hero)
        session.commit()
    

        

def main():
    # create_db_and_tables()
    # create_heroes()
    # select_heroes_by_where()
    # select_heroes_by_join()
    # select_heroes_by_left()
    # select_heroes_by_full()
    update_heroes()


if __name__=="__main__":
    main()

