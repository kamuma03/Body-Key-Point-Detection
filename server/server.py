from flask import Flask, request
from utils import decode_img, encode_img
from model import KeypointRCNN, visualise_keypoints
import json

app = Flask(__name__)

model = KeypointRCNN()


@app.route('/', methods=['POST'])
def root():

    print(request)
    x = request.get_json()
    img = x['input']
    img = decode_img(img) 

    predictions = model(img)
    print(len(predictions[0]))

    img = visualise_keypoints(img, predictions)

    img = encode_img(img)

    response = flask.resonse
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

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
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  response.headers.add('Access-Control-Allow-Credentials', 'true')
  return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)