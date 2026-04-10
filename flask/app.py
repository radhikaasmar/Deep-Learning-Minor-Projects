from flask import Flask
from flask import render_template # for rendering templates (html) and static (js & css) folder
from flask import url_for # dynamic url for static files
from flask import request # to store data in form
from flask import jsonify # to return data in json format
from flask import flash # message flashing
from flask import redirect # this redirects to login page before main page

# static_folder: if you want to change default format  
# static_url_path: to keep different url other than folder name 
# app = Flask(__name__, static_folder="assets", static_url_path="/assets")
app = Flask(__name__)

# URL =? endpoint /
@app.route("/")
def hello_world():

    # to dynamically generate url for static files
    # print(url_for("static", filename="style2.css"))
    
    # when you send some string after url:
    name = request.args.get("name", default="anonymous")
    subject = request.args.get("subject")
    print(name)

    # render html template (should be in templates folder only)
    # static => css, js, images
    return render_template("index.html", name=name, sub=subject)

@app.route("/json")
def json():
    data={
        "message": "welcome to the platform"
    }
    return jsonify(data), 200 # 200 is status code: inspect-> network


# @app.route("/login")
# def login():
#     return render_template("login.html")

# @app.route("/handle-login", methods=["GET", "POST"])
# def handle_login():

#     # if request.method == "POST":  # when u submit the form
#     #     return "<p> POST request </p>"
#     # if request.method == "GET":   # when you directly open it 
#     #     return "<p> GET request </p>"
#     if request.method == "POST":  # when u submit the form
#         print(request.form)
#         name = request.form["username"]
#         password = request.form["password"]

#         return f"<p>Welcome {name} !<p>"

#     return "<p> This route is to handle login </p>"


# combining above 2 endpoints
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        name = request.form["username"]
        password = request.form["password"]

        friends = ["adam", "bob", "charlie", "dan"]
        header = '<header> ABC website </header>'

        return render_template("welcome.html", name=name, password=password, friends=friends, header=header)
    
    else:
        return render_template("login.html")

# for message flash    
app.secret_key = "some secret message or key"

# for templating inheritance
@app.route("/index2")
def index2():
    return render_template("index2.html")

@app.route("/index3")
def index3():

    # message flashing
    flash("support timings are from 9-5.")


    return render_template("index3.html")

@app.route("/homepage")
def redirecthomepage():

    return redirect(url_for("login"))

# to avoid errors when u export file to another file
if __name__ == "__app__":
    app.run(debug = True)


