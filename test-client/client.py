import requests
from PIL import Image
import json
from io import BytesIO 
import base64
from utils import encode_img, decode_img

host = '18.133.254.35'
# host = 'localhost'

img = Image.open('Images/walking.jpg')
img = encode_img(img)

s = {
    'input': img
}
r = requests.post(f'http://{host}:5000/', data=json.dumps(s), headers={'content-type': 'application/json'})

print(r)
print(r.json())
r = r.json()
img = decode_img(r['response'])
img.show()