import joblib
import pandas as pd
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import load_img, img_to_array
import numpy as np
from PIL import Image

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
    
    print(classes)
    if classes[0] > 0.5:
        return "it is a human"
    return "it is a horse"

