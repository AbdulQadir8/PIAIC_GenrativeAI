from sqlmodel import SQLModel,Field, Relationship

class TeamBase(SQLModel):
    name: str
    headquarters: str

class Team(TeamBase, table=True):
    id: int = Field(default=None, primary_key=True)

    heroes: list["Hero"] = Relationship(back_populates="team")

class TeamCreate(TeamBase):
    pass

class TeamResponse(TeamBase):
    id: int

class TeamUpdate(SQLModel):
    name: str | None = None
    headquarters: str | None = None
    

class HeroBase(SQLModel):
    name: str = Field(index=True)
    secret_name: str


    team_id: int | None = Field(default=None, foreign_key="team.id")

    

class Hero(HeroBase,table=True):
    id: int | None = Field(default=None,primary_key=True)
    age: int | None = None

    team: Team = Relationship(back_populates="heroes")

    
class HeroCreate(HeroBase):
    age: int | None =None


class HeroResponse(HeroBase):
    id: int
    age: int | None = None

class HeroUpdate(SQLModel):
    name: str | None = None
    secret_name: str | None = None
    age: int | None = None

class HeroResponsewithTeam(HeroResponse):
    team: TeamResponse