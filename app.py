import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/main_search")
def main_search():
    searchs = list(mongo.db.terms.find())
    return render_template("search.html", searchs=searchs)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        #check if username exists in the DB
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username in use, please choose a different one")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password")),
        }
        mongo.db.users.insert_one(register)

        # put new user into session
        session["user"] = request.form.get("username").lower()
        flash("User successfully register")
        return redirect(url_for("profile", username=session["user"]))
        
    return render_template("register_user.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check the if password is the same
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # password doesn't match
                flash("Incorrect User and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exists
            flash("Incorrect User and/or Password")
            return redirect(url_for("login"))
    return render_template("login_user.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab session user's username from DB
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("user_profile.html", username=username)

    return redirect(url_for("main_search"))


@app.route("/logout")
def logout():
    # close the session
    flash("Your session has been closed")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_entry", methods=["GET", "POST"])
def add_entry():
    if request.method == "POST":
        term = {
            "term": request.form.get("term"),
            "user": session["user"],
            "definition": request.form.get("definition")
        }
        mongo.db.terms.insert_one(term)
        flash("New entry added to the dicitonary")
        return redirect(url_for("add_entry"))
        
    return render_template("add_entry.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
