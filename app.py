from flask import Flask, request, jsonify , render_template
from PIL import Image
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
from matplotlib import pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os
#import configparser
#%matplotlib inline

#config = configparser.ConfigParser()
#config.read('config.ini')

project_id = 'cdfc6942-53a7-4327-919b-cc6a411df9ff' # Replace with your project ID
cv_key = '5c29517299694c29b87f0e237e011fba' # Replace with your prediction resource primary key
cv_endpoint = 'https://altarvisionservice-prediction.cognitiveservices.azure.com/' # Replace with your prediction resource endpoint
model_name = 'Iteration2' # this must match the model name you set when publishing your model iteration exactly (including case)!

app = Flask(__name__)

@app.route('/')
def index():    
    return render_template("abrilindex.html")
    
@app.route('/acercade')  
def acercade(): 
    return render_template("acercade.html")
@app.route('/boobot')  
def boobot(): 
    return render_template("PreliminarBot.html")
@app.route('/ofrenda')  
def ofrenda(): 
    return render_template("form1.html")

@app.route('/politicas')  
def politicas(): 
    return render_template("politica.html")

@app.route("/predict_image", methods=["POST"])
def process_image():
    file = request.files['file']
    file.save("predict")
    # Read the image via file.stream
    #img = Image.open(file.stream)
    #test_img_file = os.path.join('data', 'object-detection', 'ofr.jpg')
    test_img_file = 'predict'
    test_img = Image.open(test_img_file)
    imgbin = open(test_img_file,mode="rb")
    test_img_h, test_img_w, test_img_ch = np.array(test_img).shape
    print('Ready to predict using model {} in project {}'.format(model_name, project_id))

    # Get a prediction client for the object detection model
    credentials = ApiKeyCredentials(in_headers={"Prediction-key": cv_key})
    predictor = CustomVisionPredictionClient(endpoint=cv_endpoint, credentials=credentials)

    
    print('Detecting objects in {} using model {} in project {}...'.format(test_img_file, model_name, project_id))
    # Detect objects in the test image
    with open(test_img_file, mode="rb") as test_data:
        results = predictor.detect_image(project_id, model_name, test_data)
    # Create a figure to display the results
    fig = plt.figure(figsize=(10, 12))
    #fig = plt.figure(figsize=(test_img_h,test_img_w))
    plt.axis('off')

    # Display the image with boxes around each detected object
    draw = ImageDraw.Draw(test_img)
    lineWidth = int(np.array(test_img).shape[1]/100)
    object_colors = {
        "bebida": "lightgreen",
        "calavera_completa": "yellow",
        "calavera_de_dulce": "yellow",
        "cempasuchil": "orange",
        "comida": "blue",
        "cruz": "gold",
        "fruta": "magenta",
        "pan_de_muerto": "darkcyan",
        "papel_picado": "red",
        "retrato": "cyan"
    }
    found = []
    for prediction in results.predictions:
        color = 'white' # default for 'other' object tags
        if (prediction.probability*100) > 50:
            if prediction.tag_name in object_colors:
                color = object_colors[prediction.tag_name]
                found.append(prediction.tag_name)
            left = prediction.bounding_box.left * test_img_w 
            top = prediction.bounding_box.top * test_img_h 
            height = prediction.bounding_box.height * test_img_h
            width =  prediction.bounding_box.width * test_img_w
            points = ((left,top), (left+width,top), (left+width,top+height), (left,top+height),(left,top))
            draw.line(points, fill=color, width=lineWidth)
            #plt.annotate(prediction.tag_name + ": {0:.2f}%".format(prediction.probability * 100),(left,top), backgroundcolor=color)
            plt.annotate(prediction.tag_name,(left,top), backgroundcolor=color)
    test_img.save("./static/Imagenes/out.jpg")
    return jsonify(found)
 
if __name__ == "__main__":
    app.run()