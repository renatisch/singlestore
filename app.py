from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/.well-known/singlestore-verify/token")
def read_root():
    return "d791cb4a-155b-478f-a733-58b036306030"
