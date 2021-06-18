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
    return render_template("search.html")


@app.route("/search_result", methods=["GET", "POST"])
def search_result():
    query = request.form.get("query")
    results = list(mongo.db.terms.find({"$text": {"$search": query}}))
    return render_template("search_results.html", results=results)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username exists in the DB
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
            if check_password_hash(existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
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
    searchs = list(mongo.db.terms.find())
    # grab session user's username from DB
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("user_profile.html", username=username, searchs=searchs)

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


@app.route("/edit_profile", methods=["GET", "POST"])
@app.route("/edit_profile/<username>", methods=["GET", "POST"])
def edit_profile(username=None):
    if request.method == "POST":
        user_id = mongo.db.users.find( { username: username }, { username: 0, email: 0, password: 0})
        query = {"_id": ObjectId(user_id)}
        newvalue = {"$set": {"email": request.form.get("email"), "password": request.form.get("password")}}
        mongo.db.users.update_one(user_id._id, newvalue)
        flash("Profile updated")
        return redirect(url_for("edit_profile"))

    else:
        return render_template("edit_user.html", username=username)


@app.route("/edit_entry", methods=["GET", "POST"])
@app.route("/edit_entry/<entry_id>", methods=["GET", "POST"])
def edit_entry(entry_id=None):
    if request.method == "POST":
        query = {"_id": ObjectId(entry_id)}
        newvalue = {"$set": {"term": request.form.get("term"), "definition": request.form.get("definition")}}
        mongo.db.terms.update_one(query, newvalue)
        flash("Entry updated")
        return redirect(url_for("edit_entry"))

    else:
        entry = mongo.db.terms.find_one({"_id": ObjectId(entry_id)})
        return render_template("edit_entry.html", entry_id=entry)


@app.route("/delete_entry/<term>")
def delete_entry(term):
    mongo.db.terms.remove({"_id": ObjectId(term)})
    flash("Entry Successfully deleted")
    return redirect(url_for("profile", username=session["user"]))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
