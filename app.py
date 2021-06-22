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
    '''Renders the main search page'''
    return render_template("search.html")


@app.route("/search_result", methods=["GET", "POST"])
def search_result():
    '''Searchs for a term in the database.
        Returns:
        A list with the results of the query
    '''
    query = request.form.get("query")
    results = list(mongo.db.terms.find({"$text": {"$search": query}}))
    return render_template("search_results.html", results=results)


@app.route("/register", methods=["GET", "POST"])
def register():
    ''' Register a user.
        if the user is created:
        Returns:
        Add user to the database
        Once the user is created login it in the application
        Returns to the User profile page

        If the user is not created:
        Returns to the register user page
    '''
    if request.method == "POST":
        # check if username exists in the DB
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username in use, please choose a different one")
            return redirect(url_for("register"))

        register_user = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password")),
        }
        mongo.db.users.insert_one(register_user)

        # put new user into session
        session["user"] = request.form.get("username").lower()
        flash("User successfully register")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register_user.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    ''' Log In an user in the application.
        if the user exists:
        The login details used are correct:
        Login it in the application
        Returns to the User profile page

        The login details aren't correct:
        Displays a error message
        Return to Login page

    '''
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
    ''' Shows profile for the user.
        Args:
        username: username for the user
        Returns:
        User's profile page
        A list with the terms inside the terms collection (searchs)
        The username of the user (username)
    '''
    searchs = list(mongo.db.terms.find())
    # grab session user's username from DB
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("user_profile.html", username=username, searchs=searchs)

    return redirect(url_for("main_search"))


# The extra app.route part of he code was researched with the following
# (https://stackoverflow.com/questions/17873820/flask-url-for-with-multiple-parameters)
@app.route("/edit_profile", methods=["GET", "POST"])
@app.route("/edit_profile/<username>", methods=["GET", "POST"])
def edit_profile(username=None):
    ''' Edit profile details for the user.
        Args:
        username: username for the user
        Returns:
        Using the username find the "_id" for the user
        Get new values from the edit_profile page
        Using the "_id", update the values in the database
        Shows a message
        Returns to the edit_profile page
        If the update is cancel:
        Returns to user's edit_user page
    '''
    user_info = mongo.db.users.find_one({'username': username})
    if not session or not user_info or user_info['username'] != session['user']:
        flash("You are not authoriced to do that operation")
        return render_template('search.html')
    else:
        if request.method == "POST":
            # find the _id for the user
            user_id = user_info["_id"]
            query = {"_id": ObjectId(user_id)}
            newvalue = {"$set": {"email": request.form.get("email"),
                        "password": generate_password_hash(request.form.get("password"))}}
            mongo.db.users.update_one(query, newvalue)
            flash("Profile updated")
            return redirect(url_for("edit_profile"))

        else:
            user_email = user_info["email"]
            return render_template("edit_user.html", username=username, user_email=user_email)


@app.route("/logout")
def logout():
    ''' Close the session for the user.
        Log out the user
        Shows a message about the action
        Returns to the login page
    '''
    # close the session
    flash("Your session has been closed")
    session.pop("user")
    return redirect(url_for("login"))


# The extra app.route part of he code was researched with the following
# (https://stackoverflow.com/questions/17873820/flask-url-for-with-multiple-parameters)
@app.route("/edit_entry", methods=["GET", "POST"])
@app.route("/edit_entry/<entry_id>", methods=["GET", "POST"])
def edit_entry(entry_id=None):
    ''' Edit entry data in the dictionary.
        Args:
        entry_id: the "_id" field for the entry
        Returns:
        Convert the entry_id value to ObjectId type (query)
        Get new values from the edit_entry page (newvalue)
        Using query and newvalues, update the data in the database
        Shows a message
        Returns to the edit_entry page
        If the update is cancel:
        Returns to edit_entry page
    '''
    entry = mongo.db.terms.find_one({"_id": ObjectId(entry_id)})
    if not entry or not session or entry['user'] != session["user"]:
        flash("You are not authoriced to do that operation")
        return render_template('login_user.html')
    else:
        if request.method == "POST":
            query = {"_id": ObjectId(entry_id)}
            newvalue = {"$set": {"term": request.form.get("term"),
                        "definition": request.form.get("definition")}}
            mongo.db.terms.update_one(query, newvalue)
            flash("Entry updated")
            return redirect(url_for("edit_entry", entry_id=entry_id))

        else:
            entry = mongo.db.terms.find_one({"_id": ObjectId(entry_id)})
            return render_template("edit_entry.html", entry_id=entry)


@app.route("/add_entry", methods=["GET", "POST"])
def add_entry():
    ''' Add an entry to the dictionary.
        Create a dictionary with the new data from the add_entry.html
        and session user (term)
        Insert the dictionary data in the database
        Returns to the add_entry page
    '''
    if not session:
        flash("You are not authoriced to do that operation")
        return render_template('login_user.html')
    else:
        if request.method == "POST":
            term = {
                    "term": request.form.get("term"),
                    "user": session["user"],
                    "definition": request.form.get("definition")
                }
            mongo.db.terms.insert_one(term)
            flash("New entry added to the dicitonary")
            return redirect(url_for("profile", username=session['user']))

        return render_template("add_entry.html")


@app.route("/delete_entry/<term>")
def delete_entry(term):
    ''' Edit profile details for the user.
        Args:
        term: entry from the database
        Returns:
        Delete the term entry in the database
        Shows a message
        Returns to the users'profile page
    '''
    entry = mongo.db.terms.find_one({"_id": ObjectId(term)})
    if not entry or entry['user'] != session["user"]:
        flash("You are not authoriced to do that operation")
        return render_template('search.html')
    else:
        mongo.db.terms.remove({"_id": ObjectId(term)})
        flash("Entry Successfully deleted")
        return redirect(url_for("profile", username=session["user"]))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
