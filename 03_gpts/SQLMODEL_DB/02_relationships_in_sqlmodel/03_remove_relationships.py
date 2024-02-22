from typing import Optional, List
from sqlmodel import Field, SQLModel, create_engine, Session, select, delete, Relationship
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
    heros: List["Hero"] = Relationship(back_populates="team")



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
    #02 The Relationship attribute is used to define the relationship
    #between the two models.

    team: Optional[Team] = Relationship(back_populates="heros")


#04 create a database engine using create_engine
postgres_sql = getenv("POSTGRES_SQL")
engine = create_engine(postgres_sql, echo=True)

#05 create a function create_db_and_tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def select_teams():
    with Session(engine) as session:
        stmt = select(Team).where(Team.name == "Avengers")
        team = session.exec(stmt).first()
        print("Selected team:", team)
        print("Selected team heroes", team.heros)


def update_heroes():
    with Session(engine) as session:
        stmt1 = select(Team).where(Hero.secret_name == "Spiderman")
        team = session.exec(stmt1).first()
        stmt = select(Hero).where(Hero.secret_name == "Spiderman")
        hero = session.exec(stmt).first()
        hero.team = None
        session.add(hero)
        session.commit()



def main():
    # create_db_and_tables()
    # create_heroes()
    # create_team()
    # select_teams()
    update_heroes()


if __name__ == "__main__":
    main()