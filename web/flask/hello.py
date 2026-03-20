from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    # CRITICAL FOR IDLE: 
    # 1. use_reloader=False prevents IDLE from crashing/hanging.
    # 2. debug=True still allows you to see errors in the browser.
    app.run(debug=True, use_reloader=False, port=5000)
