from fastapi import FastAPI

app : FastAPI = FastAPI()

@app.get("/hi")
def greet(who):
    return f"Hello? {who}?"

