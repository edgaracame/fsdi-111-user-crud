from flask import Flask, request
from datetime import datetime

VERSION = "1.0.0"

app = Flask(__name__)


@app.get("/ping")
def get_ping():
    response = {
        "status": "ok",
        "message": "pong"
    }
    return response


@app.get("/version")
def get_version():
    response = {
        "status": "ok",
        "message": VERSION,
        "server_time": datetime.now().strftime("%F %H:%M:%S")
    }
    return response
