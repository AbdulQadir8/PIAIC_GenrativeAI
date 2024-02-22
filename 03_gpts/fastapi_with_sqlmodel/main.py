from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException,Query
from sqlmodel import SQLModel, Field, create_engine, Session,select
from model import Hero,HeroResponse, HeroCreate, HeroUpdate,Team,TeamResponse, TeamCreate,TeamUpdate, HeroResponsewithTeam



DB_URL = "postgresql://aq98123:XQWNJ40patHx@ep-shy-breeze-a57yskaw.us-east-2.aws.neon.tech/fastapi_testing2?sslmode=require"
engine = create_engine(DB_URL)

def create_tables():
    SQLModel.metadata.create_all(engine)

app = FastAPI()


#DB Dependency Injection
def get_dep():
    with Session(engine)  as session:
        yield session


@app.on_event("startup")
def on_startup():
    create_tables()

@app.get("/")
def get_heros():
    return {"Hellow":"World"}

# Get all heros
@app.get("/heroes", response_model=list[Hero])
def get_heroes(session: Annotated[Session, Depends(get_dep)],offset:int= Query(default=0, le=4),limit:int=Query(default=2,le=4)):
    heroes = session.exec(select(Hero).offset(offset).limit(limit)).all()
    print(heroes.team)
    return heroes
    

@app.post("/heroes",response_model=HeroResponse)
def create_heroes(hero: HeroCreate,db: Annotated[Session, Depends(get_dep)]):
    hero_to_insert = Hero.model_validate(hero)
    db.add(hero_to_insert)
    db.commit()
    db.refresh(hero_to_insert)
    return hero_to_insert

#Single Hero
@app.get("/heroes/{hero_id}",response_model=HeroResponsewithTeam)
def get_gero_by_id(hero_id: int, session: Annotated[Session, Depends(get_dep)]):
    hero = session.get(Hero,hero_id)
    if not hero:
        raise HTTPException(status_code=404,detail="Hero Not Found")
    return hero
#Hero Update
@app.patch("/heroes/{hero_id}")
def update_hero(hero_id: int, hero_data: HeroUpdate, session: Annotated[Session, Depends(get_dep)]):
    #Get Hero
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404,detail="Hero Not Found")
    print("HERO IN DB",hero)
    print("Data From Client",hero_data)

    hero_dict_data = hero_data.model_dump(exclude_unset=True)
    print("hero_dict_data",hero_dict_data)


    for key,value in hero_dict_data.items():
        setattr(hero,key,value)

    print("After",hero)

    session.add(hero)
    session.commit()
    session.refresh(hero)

    return hero
# Hero delete
@app.delete("/heroes/{hero_id}")
def delete_hero(hero_id,session: Annotated[Session,Depends(get_dep)]):
    hero = session.get(Hero,hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    session.delete(hero)
    session.commit()
    return {"message":"Hero deleted successfully"}


# Get all Teams
@app.get("/teams",response_model=list[Team])
def get_teams(session: Annotated[Session, Depends(get_dep)], offset: int = Query(default=0, le=4), limit: int = Query(default=2, le=4)):
    teams = session.exec(select(Team).offset(offset).limit(limit)).all()
    return teams


#Create Teams
@app.post("/teams",response_model=TeamResponse)
def create_team(team: TeamCreate, db: Annotated[Session, Depends(get_dep)]):
    print("Data from client",team)

    team_to_insert = Team.model_validate(team)
    print("DATA AFTER VALIDATION", team_to_insert)
    db.add(team_to_insert)
    db.commit()
    db.refresh(team_to_insert)
    return team_to_insert

#Single Team
@app.get("/teams/{team_id}",response_model=TeamResponse)
def get_team_by_id(team_id: int, session: Annotated[Session, Depends(get_dep)]):
    team = session.get(Team, team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team

# Team Update
@app.patch("/teams/{team_id}")
def update_team(team_id: int, team_data: TeamUpdate, session: Annotated[Session, Depends(get_dep)]):
    team = session.get(Team, team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team Not Found")
    print("Team In DB",team)
    print("Data From Client", team_data)

    team_dict_data = team_data.model_dump(exclude_unset=True)
    print("team_dict_data", team_dict_data)

    for key,value in team_dict_data.items():
        setattr(team,key,value)

    print("AFTER",team)

    session.add(team)
    session.commit()
    session.refresh(team)

    return team

# Team Delete
@app.delete("/teams/{team_id}")
def delete_team(team_id: int, session: Annotated[Session, Depends(get_dep)]):
    team = session.get(Team, team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team Not Found")
    session.delete(team)
    session.commit()
    return {"message":"Team Deleted Successfully"}