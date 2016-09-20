from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Home page";

@app.route("/Class")
def classroom():
    return "Class page"

@app.rout("/Internet")
def interweb():
    return "Internet of Things"

if(__name__ == '__main__'):
    app.run()
