from os import name
from flask import Flask, json,jsonify,request
from pdata import data
from flask.helpers import flash

app = Flask(__name__)
@app.route("/")
def home():
    return "HOME PAGE"

@app.route("/page2")
def pagetwo():
    return "THIS IS THE SECOND PAGE"

@app.route("/datapage")
def datapage():
    return jsonify({
        "data":data,
        "message":"success"
    }),200

@app.route("/planetdata")
def planetdata():
    name = request.args.get("name")
    planetdata = next(i for i in data if i["name"] == name)
    return jsonify({
        "data":planetdata,
        "message":"success"
    }),200


if __name__ == "__main__":
    app.run()
