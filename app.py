
from flask import Flask

app = Flask(__name__)

@app.route("/")
def accueil():
    return "Application publiée sur Docker Hub, version 1.1\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

