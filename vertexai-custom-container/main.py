import base64
import numpy as np
import tensorflow as tf

from io import BytesIO
from PIL import Image as PILImage
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load your SavedModel
model = tf.saved_model.load("local_model/fine_tuned_model_tf")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    # Access the instances
    instances = data.get("instances") 
    if not instances or len(instances) != 1:
        return jsonify({"error": "Invalid input format. 'instances' should be an array with one element."}), 400
    image_data = instances[0]  # Assuming a single image in instances

    # Optional: Access parameters if needed
    parameters = data.get("parameters")

    # Preprocess the data as needed
    input_data = preprocess_fn(image_data)  

    # Make predictions
    predictions = model.serve(input_data)

    # Postprocess predictions 
    output = postprocess_fn(predictions) 

    return jsonify(output) 

def preprocess_fn(image_data):
    # Decode the base64 string
    decoded_image = base64.b64decode(image_data)

    # Open the image, crop it, convert it to RGB format, and display it.
    img = PILImage.open(BytesIO(decoded_image)).crop((0, 0, 224, 224)).convert('RGB')

    # Convert the image to a Tensor and scale to [0, 1]
    tensor = tf.cast(tf.expand_dims(np.array(img), axis=0), tf.float32) / 255.0
    
    return tensor

def postprocess_fn(predictions):
    # Format friendly prediction response
    prediction_percentage = "{:.0%}".format(max(predictions.numpy()[0]))
    if np.argmax(predictions.numpy()[0]) == 0:
        prediction_label = "Benigna"
    else:
        prediction_label = "Câncer"

    return {"predictions": [{"prediction_label": prediction_label, "prediction_percentage": prediction_percentage}]} 

@app.route('/health_check')
def health_check():
    return "Healthy"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True) 