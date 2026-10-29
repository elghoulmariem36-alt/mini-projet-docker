
import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def accueil():
    message = os.getenv(
        "APP_MESSAGE",
        "Bienvenue dans mon application Docker !"
    )
    return message + "\nVersion 1.0.1 - Mise a jour de l'application\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

