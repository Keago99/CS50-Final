import os
import datetime

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps

app = Flask(__name__)

app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'

PYTHONDONTWRITEBYTECODE= "abc"

db = SQL("sqlite:///Exercise.db")



app.config["TEMPLATES_AUTO_RELOAD"] = True

"Method to ensure logins are required" 
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


"The main page/home page"
@app.route("/")
@login_required
def index():
    return render_template("index.html")

"Where users register for new accounts"
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        
        password = request.form.get("password")

        if not request.form.get("username"):
            return render_template("error.html", error="No username")

        if not request.form.get("password"):
            return render_template("error.html", error="No password")

        if not request.form.get("confirmation"):
            return render_template("error.html", error="Re-type password")

        if request.form.get("password") != request.form.get("confirmation"):
            return render_template("error.html", error = "passwords do not match")

            

        rows = db.execute("SELECT * FROM users WHERE userName = ?", request.form.get("username"))

        if len(rows) != 0:
            return render_template("error.html", error = "Username already exists")
        
        else:
            username = request.form.get("username")
            hash = generate_password_hash(request.form.get("password"))
            db.execute("INSERT INTO users (userName, hash) VALUES(?, ?)", username, hash)
            rows = db.execute("SELECT * FROM users WHERE userName = ?", request.form.get("username"))
            session["user_id"] = rows[0]["id"]
            return redirect("/welcome")
            

    

    else:
        return render_template("register.html")

"The login page, users will be redirected here if they hit a page that requires them to be logged in"
@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "POST":

        
        # Ensure username was submitted
        if not request.form.get("username"):
            return render_template("error.html", error="No username")

        # Ensure password was submitted
        if not request.form.get("password"):
            return render_template("error.html", error="No password")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE userName = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return render_template("error.html", error="Invalid username/password")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    else:
        return render_template("login.html")

@app.route("/error")
def error():
    return render_template("error.html")

@app.route("/welcome")
@login_required
def welcome():
    return render_template("welcome.html") 

@app.route("/howTo")
@login_required
def howTo():
    return render_template("howTo.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/calibrate", methods=["GET", "POST"])
@login_required
def calibrate():
    if request.method == "POST":

        Squat = request.form.get("Squat")
        Deadlift = request.form.get("Deadlift")
        Bench = request.form.get("Bench")
        BBRow = request.form.get("BBRow")
        OverheadPress = request.form.get("OverheadPress")
        BBCurl = request.form.get("BBCurl")
        Pullups = request.form.get("Pullups")


        if not request.form.get("Squat"):
            return render_template("error.html", error="Please enter a number greater than 0")

        if not request.form.get("Deadlift"):
            return render_template("error.html", error="Please enter a number greater than 0")

        if not request.form.get("Bench"):
            return render_template("error.html", error="Please enter a number greater than 0")

        if not request.form.get("BBRow"):
            return render_template("error.html", error="Please enter a number greater than 0")

        if not request.form.get("OverheadPress"):
            return render_template("error.html", error="Please enter a number greater than 0")

        if not request.form.get("BBCurl"):
            return render_template("error.html", error="Please enter a number greater than 0")

        if not request.form.get("Pullups"):
            return render_template("error.html", error="Please enter a number greater than 0")

        userExists = db.execute("SELECT * FROM Exercises WHERE userID = ?", session["user_id"])

        if len(userExists) != 0:
            db.execute("UPDATE Exercises SET Squat = ?, Deadlift = ?, Bench = ?, BBRow = ?, OverheadPress = ?, BBCurl = ?, Pullups = ? WHERE userID = ? ",
            Squat, Deadlift, Bench, BBRow, OverheadPress, BBCurl, Pullups, session["user_id"])

            flash("Your lifts have been updated!")
            return redirect("/")

        else:
            db.execute("INSERT INTO Exercises (UserID, Squat, Deadlift, Bench, BBRow, OverheadPress, BBCurl, Pullups) VALUES(?,?,?,?,?,?,?,?)",
            session["user_id"], Squat, Deadlift, Bench, OverheadPress, BBRow, BBCurl, Pullups)

            flash("Your lifts have been set for the first time ")
            return redirect("/")

    else:
        return render_template("calibrate.html")

@app.route("/week1")
@login_required
def week1():

    ExerInfo = db.execute("SELECT * FROM Exercises WHERE userID = ?", session["user_id"])

    if len(ExerInfo) != 0:
        return render_template("week1.html", Info = ExerInfo)
    
    else:
        flash("Please enter your lifts before viewing your weekly training")
        return redirect("/calibrate")

@app.route("/week2")
@login_required
def week2():

    ExerInfo = db.execute("SELECT * FROM Exercises WHERE userID = ?", session["user_id"])

    if len(ExerInfo) != 0:
        return render_template("week2.html", Info = ExerInfo)

    else:
        flash("Please enter your lifts before viewing your weekly training")
        return redirect("/calibrate")

@app.route("/week3")
@login_required
def week3():
    
    ExerInfo = db.execute("SELECT * FROM Exercises WHERE userID = ?", session["user_id"])

    if len(ExerInfo) != 0:
        return render_template("week3.html", Info = ExerInfo)
        
    else:
        flash("Please enter your lifts before viewing your weekly training")
        return redirect("/calibrate")

@app.route("/week4")
@login_required
def week4():

    ExerInfo = db.execute("SELECT * FROM Exercises WHERE userID = ?", session["user_id"])

    if len(ExerInfo) != 0:
        return render_template("week4.html", Info = ExerInfo)
        
    else:
        flash("Please enter your lifts before viewing your weekly training")
        return redirect("/calibrate")

@app.route("/FAQ")
@login_required
def FAQ():

    return render_template("FAQ.html")

