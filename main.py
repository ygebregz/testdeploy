import numpy as np
from flask import Flask, request, render_template, url_for, jsonify
from flask_cors import CORS, cross_origin
import logging
from predict import make_prediction

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    """Basic HTML response."""
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    logging.debug("got into predict api endpoint")
    print("files", request.files)
    if 'image' not in request.files:
        logging.debug("image not in request file")
        return 'No file part in the request', 400
    
    file = request.files['image']
    logging.debug("got into file")
    if file.filename == '':
        return 'No selected file.', 400
    
    pred = make_prediction(file)
    logging.debug("returning result from endpoint")
    
  
    return render_template("results.html", prediction = pred, comment="asd")

if __name__ == '__main__':
    app.run()