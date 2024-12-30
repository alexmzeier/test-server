from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Depends, Response, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = ["http://localhost:3000", "*", "http://127.0.0.1"] #"*" für production entfernen
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/test")
async def main_route():
    return "successfull"