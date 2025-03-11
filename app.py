from flask.logging import default_handler
import time
from flask import Flask
from flask import request
import json
import sys
import traceback
import logging


log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)


app = Flask(__name__)


REQUEST_ID_HEADER = "x-fc-request-id"


@app.route("/status", methods=["GET"])
def init_invoke():
   
    return "OK 8000"


@app.route("/invoke", methods=["POST"])
def event_invoke():
  

    return "hello world!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, threaded=True)
