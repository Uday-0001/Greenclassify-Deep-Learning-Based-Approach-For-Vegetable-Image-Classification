import numpy as np
import os
import tensorflow as tf
from flask import Flask, request, render_template
from tensorflow.keras.models import load_model    
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

# --- CONFIGURATION ---
MODEL_PATH = 'vegetable_classification.h5'
UPLOAD_FOLDER = 'uploads'

# --- LOAD MODEL ---
print("Loading model...")
try:
    # compile=False is generally safer for inference if custom metrics/losses might be missing
    model = load_model(MODEL_PATH, compile=False)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    print("Please ensure 'vegetable_classification.h5' is in the current directory.")
    model = None

# --- ROUTES ---

@app.route('/')
def index():
    """Default home page route"""
    return render_template('index.html')

@app.route('/index.html')
def home():
    """Home page alias"""
    return render_template("index.html")

@app.route('/logout.html')
def logout():
    """Logout page route"""
    return render_template('logout.html')

@app.route('/result', methods=["GET", "POST"])
def res():
    """
    Handle image upload and prediction.
    GET: Render the prediction page.
    POST: Process the uploaded image and display the result.
    """
    if request.method == "POST":
        # Check if the model is loaded
        if model is None:
            return render_template('prediction.html', pred="Error: Model not loaded")

        # Get the file from post request
        f = request.files['image']
        
        # Define upload path
        basepath = os.path.dirname(__file__) 
        folder_path = os.path.join(basepath, UPLOAD_FOLDER)
        
        # Create uploads folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            
        filepath = os.path.join(folder_path, f.filename)
        f.save(filepath)
        
        # Preprocessing the image
        # Target size must match the input shape of the trained model (150x150)
        img = tf.keras.utils.load_img(filepath, target_size=(150, 150)) 
        img_arr = tf.keras.utils.img_to_array(img)
        img_arr = img_arr / 255.0  # Normalize pixel values if training used rescaling (1./255)
        
        img_input = np.expand_dims(img_arr, axis=0) # Add batch dimension

        # Make prediction
        preds = model.predict(img_input)
        pred_index = np.argmax(preds) # Get highest probability index
        
        # Class mapping dictionary
        op = {
            0: 'Bean', 1: 'Bitter_Gourd', 2: 'Bottle_Gourd', 3: 'Brinjal', 
            4: 'Broccoli', 5: 'Cabbage', 6: 'Capsicum', 7: 'Carrot', 
            8: 'Cauliflower', 9: 'Cucumber', 10: 'Papaya', 11: 'Potato', 
            12: 'Pumpkin', 13: 'Radish', 14: 'Tomato'
        }
              
        result = op.get(pred_index, "Unknown Vegetable")
        
        return render_template('prediction.html', pred=result, image_name=f.filename)

    # For GET requests, just render the page
    return render_template('prediction.html')

if __name__ == "__main__":
    app.run(debug=True)
