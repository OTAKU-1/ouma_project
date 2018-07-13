# -*- coding:utf8 -*-
import flask
app = flask.Flask(__name__)

@app.route("/")
def Home():
    return "<h1>Hey!, I Love PYTHON </h1> <a href='hello'>Hello</a> احبك يا بايثون"


@app.route("/hello")
def hello():
    return u"""
    <h1 style="direction:rtl">
    مرحبا بالعالم! 
    </h1>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1412)
