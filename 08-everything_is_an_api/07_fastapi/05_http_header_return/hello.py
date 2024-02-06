from fastapi import FastAPI, Header

app : FastAPI = FastAPI()

@app.post("/agent")
def get_agent(user_agent:str = Header()):
    print(user_agent)
    return user_agent
