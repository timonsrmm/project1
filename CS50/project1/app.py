import os

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not ("postgres://bolnfooahgbqsw:7d78f8b5bd6c9dd2408249a8a1e65cc47d8f24a15fff0a72be296f7eb033ef01@ec2-54-235-114-242.compute-1.amazonaws.com:5432/dblvltk9k6coln"):
    raise RuntimeError("postgres://bolnfooahgbqsw:7d78f8b5bd6c9dd2408249a8a1e65cc47d8f24a15fff0a72be296f7eb033ef01@ec2-54-235-114-242.compute-1.amazonaws.com:5432/dblvltk9k6coln is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine("postgres://bolnfooahgbqsw:7d78f8b5bd6c9dd2408249a8a1e65cc47d8f24a15fff0a72be296f7eb033ef01@ec2-54-235-114-242.compute-1.amazonaws.com:5432/dblvltk9k6coln")
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == "GET":
        return "Please go back to the Sign up page"
    else:
        name = request.form.get("name")
        return render_template("signup.html", name=name)
