from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_ghw():
    return "<p>Thansk, 404, for all the help!!!</p>"