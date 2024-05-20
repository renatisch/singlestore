from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/.well-known/singlestore-verify/token")
def read_root():
    return "f3e80765-f223-429f-b3a5-d33ac8c039bd"
