from flask import Flask, request
from requests import get

app = Flask(__name__)


@app.route('/')
def index():
    return "hello world"

@app.route("/<path:subpath>")
def query(subpath):
    default_api = "https://newsapi.org"
    if not request.args:
        return get(f"{default_api}/{subpath}").content
    elif "api" not in request.args.keys():
        query = '&'.join([f"{key}={request.args[key]}" for key in request.args.keys()])
        response = get(f"{default_api}/{subpath}?{query}")
        return response.json()
    else:
        request_keys = list(request.args.keys())
        request_keys.remove("api")
        query = "&".join([f"{key}={request.args[key]}" for key in request_keys])
        response = get(f"{request.args['api']}/{subpath}?{query}")
        return response.json()
