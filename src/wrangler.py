from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/register")
def register(username: str,request: Request):
    client_host = request.client.host
    return {"client_host": client_host, "username": username}