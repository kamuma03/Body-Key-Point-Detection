import base64
from io import BytesIO
from PIL import Image
from time import time

def decode_img(img):
    img = base64.b64decode(img)
    img = BytesIO(img)
    img = Image.open(img)
    return img

def encode_img(pil_img):
    buffered = BytesIO()
    pil_img.save(buffered, format="JPEG")
    pil_img_bytes = base64.b64encode(buffered.getvalue())
    print('b64:')
    # save file to compare what's sent by python and js
    with open(f'test-client/encoded_imgs/py{time()}.txt', 'bw+') as f:
        f.write(pil_img_bytes)
    print(str(pil_img_bytes))
    pil_img_str = str(pil_img_bytes)
    # pil_img_str = pil_img_str[:2]
    pil_img_str = pil_img_bytes.decode('utf-8')
    return pil_img_str