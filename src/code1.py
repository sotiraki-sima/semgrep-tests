import flask
from flask import response as r

app = flask.Flask()

@app.route("/index")
def index():
    resp = r.set_cookie("sessionid", "RANDOM-UUID")
    return resp

@app.route("/snafu")
def snafu():
    resp = r.set_cookie("sessionid",
        generate_cookie_value("RANDOM-UUID"),
        secure=True)
    return resp

@app.route("/foo")
def foo():
    from flask.response import set_cookie as sc
    sc("sessionid", "RANDOM-UUID")

@app.route("/admin")
def admin():
    # this cookie is secure
    resp = r.set_cookie("sessionid", "RANDOM-UUID", secure=True, httponly=True, samesite="Lax")
    return resp