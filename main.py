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
    body = (
        "<html>"
        "<body style='padding: 10px;'>"
        "<h1>Welcome to my Flask API</h1>"
        "</body>"
        "</html>"
    )
    return body

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
    
  
    return pred, 200

if __name__ == '__main__':
    app.run()