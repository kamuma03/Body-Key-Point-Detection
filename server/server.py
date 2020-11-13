from flask import Flask, request
from utils import decode_img

app = Flask(__name__)

@app.route('/')
def root():
    name = 'Harry'
    return json.dumps({
        'statusCode': 200,
        'response': 'hello world'
    })

@app.route('/predict', methods=['POST'])
def predict():
    print(request)
    x = request.get_json()
    img = x['input']
    img = decode_img()
    return 'hello'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)