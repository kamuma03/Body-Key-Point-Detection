import requests
from PIL import Image
import json
from io import BytesIO 
import base64

# img = Image.open('beijing.jpeg')
# buffer = BytesIO() # create buffer to read to
# img.save(buffer, format='JPEG') # store image in buffer
# img = base64.b64encode(buffer.getvalue()) # get value of buffer and encode as base64
# img = img.decode('utf-8') # decode as utf-8

# img = base64.b64decode(img)
# img = BytesIO(img)
# img = Image.open(img)
# img.show()

s = {
    'input': 'img'
}
# r = requests.post('http://:5000/predict', data=json.dumps(s), headers={'content-type': 'application/json'})
r = requests.get('http://35.178.210.245:5000/')

print(r)