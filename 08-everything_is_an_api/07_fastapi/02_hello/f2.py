from fastapi import FastAPI

app : FastAPI = FastAPI()

@app.get("/notifications")
def notifications(filter:str,id:int,country):
    # return {"data": "filter"+ filter}
    return {"Name": filter,"Id":id,"Country":country}
