from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def sample():
    return f'This is {os.getenv("APP")} server'


if __name__ == '__main__':
    print("Starting the server")
    app.run(host='0.0.0.0')
