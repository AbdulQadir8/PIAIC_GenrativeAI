from fastapi import FastAPI

app: FastAPI = FastAPI()


@app.get("/in/{pname}")
def student_profile(pname:str):
    return {"Student name": pname}

@app.get("/{org}/student/{student_name}")
def student_profile_org(org:str, student_name:str):
    return {"Student Name": student_name, "Organization": org}