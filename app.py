from email import message
from urllib import response
from webbrowser import get
from flask import Flask, render_template, request, jsonify

from chat import get_response

app = Flask(__name__)

@app.get("/")
def index_get():
    return render_template("index.html")


@app.get("/courses")
def courses():
    return render_template("courses.html")


@app.get("/colleges")
def colleges():
    return render_template("colleges.html")

@app.get("/about")
def about():
    return render_template("about.html")

@app.get("/contact")
def contact():
    return render_template("contact.html")

@app.get("/privacypolicy")
def privacypolicy():
    return render_template("privacypolicy.html")

@app.get("/dashboard")
def dashboard():
    return render_template("login.html")



@app.post("/predict")
def predict():
    text = request.get_json().get("message")

    response = get_response(text)
    message = {"answer":response}
    return jsonify(message)


if __name__== "__main__":
    app.run(debug=True)

    

