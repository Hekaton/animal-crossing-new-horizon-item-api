import json
from flask import Flask, jsonify
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app, config={"CACHE_TYPE": "simple"})

version = {
    "api_version": "0.0.1"
}

with open('data/fish.json') as fish_json:
    fish_data = json.load(fish_json)

with open('data/bug.json') as bug_json:
    bug_data = json.load(bug_json)

with open('data/fossil.json') as fossil_json:
    fossil_data = json.load(fossil_json)


@app.route('/')
def show_version():
    return jsonify(version)


@app.route('/fishs')
@cache.cached(timeout=600)
def get_fish():
    return jsonify(fish_data)


@app.route('/bugs')
@cache.cached(timeout=600)
def get_bugs():
    return jsonify(bug_data)


@app.route('/fossils')
@cache.cached(timeout=600)
def get_fossils():
    return jsonify(fossil_data)
