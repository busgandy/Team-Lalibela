from flask import Flask, redirect, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open("linear_regression.pkl", "rb"))


@app.route("/")
def index():
    return render_template ("index.html")

@app.route("/analysis")
def analysis():
    return render_template ("analysis.html")
@app.route("/prediction")
def prediction():    
    return render_template ("Start Predictions.html")
    
@app.route("/predict", methods=["POST"])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    
    output = round(prrediction[0], 2)
    return render_template ( "Start Predictions.html" , prediction_text = "Employee Salary is: ${}".format(output))



def contact():
    if request.method == 'POST':
        if request.form['submit_button'] == 'START YOUR PREDICTION':
            return render_template ("analysis.html")
        elif request.form['submit_button'] == 'CHECK FOR ANALYSIS':
            return render_template ("Start Predictions.html")


        

        
@app.route("/start", methods = ["GET", "POST"])
def start_prediction():
    return render_template ("Start Predictions.html")
