# -*- coding:utf8 -*-
import flask
app = flask.Flask(__name__)

@app.route("/")
def Home():
    return "وهنا كود اكتب ثلاث علمات"


@app.route("/hello")
def hello():
    return u"""
    هنا كود HTML
    اذا بتكتب عربي اكتب حرف U قبل علامات التنصيص
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1412)
