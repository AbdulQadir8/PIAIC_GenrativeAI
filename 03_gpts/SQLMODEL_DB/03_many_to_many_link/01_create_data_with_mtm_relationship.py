from typing import Optional, List
from sqlmodel import Field, SQLModel, create_engine, Session, select, delete, Relationship
from dotenv import load_dotenv, find_dotenv
from os import getenv

_:bool = load_dotenv(find_dotenv())


#01 - Create a link model to represent the many-to-many relationship between the two models
# The link model will have two fields, one for each model's primary key
class HeroTeamLink(SQLModel, table=True):
    hero_id: Optional[int] = Field(default=None, foreign_key="hero.id",primary_key=True)
    team_id: Optional[int] = Field(default=None, foreign_key="team.id",primary_key=True)




#02 create a team table with columns: id, name, and headquarters.
class Team(SQLModel, table=True):
    """
    create a Team table with columns: id, name, and headquarters.
    """
    id: Optional[int] = Field(primary_key=True)
    name: str
    headquarters : str
    #02 The relationship attribute is used to define the relationship between the two models
    # The link_model argument is used to specify the link model that will be used to 
    heros: List["Hero"] = Relationship(back_populates="team", link_model=HeroTeamLink)



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

    team: Optional[Team] = Relationship(back_populates="heros",link_model=HeroTeamLink)


#04 create a database engine using create_engine
postgres_sql = getenv("POSTGRES_SQL")
engine = create_engine(postgres_sql, echo=True)

#05 create a function create_db_and_tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def create_heroes():
    with Session(engine) as session:
        team_preventers = Team(name="Preventers", headquarters="Sharp Tower")
        team_z_force = Team(name="Z-Force", headquarters="Sister Margaret's Bar")

        hero_deadpond = Hero(
            name="Deadpond",
            secret_name="Dive Wilson",
            teams=[team_z_force, team_preventers],
        )
        hero_rusty_man = Hero(
            name="Rusty-Man",
            secret_name="Tommy Sharp",
            age=48,
            teams=[team_preventers],
        )
        hero_spider_boy = Hero(
            name="Spider-Boy", secret_name="Pedro Parqueador", teams=[team_preventers]
        )

        session.add(hero_deadpond)
        session.add(hero_rusty_man)
        session.add(hero_spider_boy)
        session.commit()

def main():
    # create_db_and_tables()
    create_heroes()


if __name__=="__main__":
    main()