from fastapi import FastAPI
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
import ssl

app = FastAPI()
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain("cert.pem", keyfile="key.pem")


@app.get("/.well-known/singlestore-verify/token")
def read_root():
    return "f5e220b6-7779-4de9-acf5-d79dc0981236"
