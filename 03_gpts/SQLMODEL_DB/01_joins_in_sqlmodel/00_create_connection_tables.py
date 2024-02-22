from typing import Optional
from sqlmodel import Field, SQLModel, create_engine
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
    id: Optional[int] = Field(default=True, primary_key=True)
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


def main():
    create_db_and_tables()

if __name__=="__main__":
    main()

