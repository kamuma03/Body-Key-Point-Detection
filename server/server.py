from flask import Flask, request
import flask
from utils import decode_img, encode_img
from model import KeypointRCNN, visualise_keypoints
import json
from time import time

app = Flask(__name__)

model = KeypointRCNN()


@app.route('/', methods=['POST'])
def root():

    print('the request:', request)
    x = request.get_json()
    img = x['input']
    
    img = decode_img(img) 

    predictions = model(img)

    img = visualise_keypoints(img, predictions)

    img = encode_img(img)

    return json.dumps({
        'statusCode': 200,
        'response': img
    })

@app.route('/predict', methods=['POST'])
def predict():
    print(request)
    x = request.get_json()
    img = x['input']
    img = decode_img(img)
    return 'hello'

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,access-control-allow-origin')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  response.headers.add('Access-Control-Allow-Credentials', 'true')
  return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)