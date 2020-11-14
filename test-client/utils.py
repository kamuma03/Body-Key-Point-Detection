import base64
from io import BytesIO
from PIL import Image

def decode_img(img):
    img = base64.b64decode(img)
    img = BytesIO(img)
    img = Image.open(img)
    return img

def encode_img(pil_img):
    buffered = BytesIO()
    pil_img.save(buffered, format="JPEG")
    pil_img_bytes = base64.b64encode(buffered.getvalue())
    pil_img_str = pil_img_bytes.decode('utf-8')
    return pil_img_str