from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template ("index.html")

@app.oute("/analysis.html?")
def analysis():
    return render_template ("analysis.html")
