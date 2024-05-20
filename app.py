from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/.well-known/singlestore-verify/token")
def read_root():
    return "0394c6e0-d4cb-4432-9daa-b9915f32b6d7"
