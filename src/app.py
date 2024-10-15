from flask import Flask, request, render_template
from pickle import load

app = Flask(__name__)
model = load(open("../models/random_forest_42.sav", "rb"))


@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        
        # Obtain values from form
        val1 = float(request.form["val1"])
        val2 = float(request.form["val2"])
        val3 = float(request.form["val3"])
        
        data = [[val1, val2, val3]]
        print(data)
        prediction = str(model.predict(data)[0])
    else:
        prediction = None
    
    return render_template("index.html", prediction = prediction)
