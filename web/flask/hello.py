from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! <a href='/games'>View the games.</a></p>"

@app.route("/games")
def games():
    return "<p>Here's where the games will be listed...</p>"
