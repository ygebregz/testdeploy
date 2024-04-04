import numpy as np
from flask import Flask, request
from predict import make_prediction
import logging 

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
    print("files", request.files)
    if 'image' not in request.files:
        return 'No file part in the request', 400
    
    file = request.files['image']
    logging.info(f'File is {str(file)}')
    
    if file.filename == '':
        return 'No selected file.', 400
    
    pred = make_prediction(file)
    
  
    return pred, 200

if __name__ == "__main__":
    app.run()
