from flask import Flask, request, render_template

from tensorflow.keras.models import load_model
from tensorflow.keras.utils import img_to_array
import numpy as np
from PIL import Image


#TODO : get from bucket / drive /
model = load_model('my_model.h5')

def make_prediction(image):
    """
    Make a prediction using the trained model
    """
    img = Image.open(image).convert('RGB').resize((300,300))
    x = img_to_array(img)
    x /= 255 #normalize
    x = np.expand_dims(x, axis=0)
    
    images = np.vstack([x])
    
    classes = model.predict(images, batch_size =10)
    if classes[0] > 0.5:
        return "Human"
    return "Horse"


app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    """Basic HTML response."""
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    print("files", request.files)
    if 'image' not in request.files:
        return 'No file part in the request', 400
    
    file = request.files['image']
    if file.filename == '':
        return 'No selected file.', 400
    
    pred = make_prediction(file)  
    return render_template("results.html", prediction = pred, comment="asd")

if __name__ == '__main__':
    app.run()