from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template ("index.html")

@app.route("/analysis")
def analysis():
    return render_template ("analysis.html")
@app.route("/prediction")
def prediction():
    return render_template ("Start Predictions.html")
def contact():
    if request.method == 'POST':
        if request.form['submit_button'] == 'START YOUR PREDICTION':
            return render_template ("analysis.html")
        elif request.form['submit_button'] == 'CHECK FOR ANALYSIS':
            return render_template ("Start Predictions.html")

@app.route("/start", methods = ["GET", "POST"])
def start_prediction():
    return render_template ("Start Predictions.html")
