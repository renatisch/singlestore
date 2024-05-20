from fastapi import FastAPI
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
import ssl

app = FastAPI()
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain("cert.pem", keyfile="key.pem")


@app.get("/")
def read_root():
    return "hello world"


@app.get("/.well-known/singlestore-verify/token")
def read_root():
    return "d791cb4a-155b-478f-a733-58b036306030"
