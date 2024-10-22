from flask import Flask
from models.database import  init_db


app = Flask(__name__)

@app.route("/")
def home():
    return "Hello"




if __name__ == "__main__":
    init_db()
    app.run()