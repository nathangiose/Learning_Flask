from application import app, db
from flask import render_template, request, json, Response, redirect, flash, url_for
from application.models import User, Enrollment, Course
from application.forms import LoginForm, RegisterForm

courseData = [{"courseID": "1", "title": "PHP 101", "description": "Intro to PHP", "credits": 3, "term": "Fall, Spring"}, {"courseID": "2", "title": "Java 1", "description": "Intro to Java Programming", "credits": 4, "term": "Spring"}, {"courseID": "3", "title": "Adv PHP 201",
                                                                                                                                                                                                                                             "description": "Advanced PHP Programming", "credits": 3, "term": "Fall"}, {"courseID": "4", "title": "Angular 1", "description": "Intro to Angular", "credits": 3, "term": "Fall, Spring"}, {"courseID": "5", "title": "Java 2", "description": "Advanced Java Programming", "credits": 4, "term": "Fall"}]


@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", index=True)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.objects(email=email).first()
        if user and user.get_password(password):
            flash(f"{user.first_name}, you successfully logged in!", "success")
            return redirect("/index")
        else:
            flash("Invalid, something went wrong.", "danger")
    return render_template("login.html", title="Login", form=form, login=True)


@app.route("/courses/")
@app.route("/courses/<term>")
def courses(term="Winter 2021"):

    return render_template("courses.html", courseData=courseData, login=True, term=term)


@app.route("/enrollment", methods=["GET", "POST"])
def enrollment():
    id = request.form.get("courseID")
    title = request.form.get("title")
    term = request.form.get("term")
    return render_template("enrollment.html", enrollment=True, data={"id": id, "title": title, "term": term})


@app.route("/register", methods=["POST", "GET"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_id = User.objects.count()
        user_id += 1

        email = form.email.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        user = User(user_id=user_id, email=email,
                    first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        flash("You have been succcessfully registered!", "success")
        return redirect(url_for("index"))

    return render_template("register.html", form=form, register=True, title="Register")


@app.route("/api/")
@app.route("/api/<idx>")
def api(idx=None):
    if(idx == None):
        jdata = courseData
    else:
        jdata = courseData[int(idx)]

    return Response(json.dumps(jdata), mimetype="application/json")


@app.route("/user")
def user():
    # User(user_id=1, first_name="Nathan", last_name="Giose",
    #      email="nathangiose@gmail.com", password="lifechoices2021").save()

    # User(user_id=2, first_name="Tashwill", last_name="Andries",
    #      email="tashwilla56@gmail.com", password="password123").save()

    # User(user_id=3, first_name="Tashwilla", last_name="Andries",
    #      email="tashwilla53@gmail.com", password="lifechoices2020").save()

    users = User.objects.all()
    return render_template("user.html", users=users)
