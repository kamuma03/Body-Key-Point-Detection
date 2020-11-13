def decode_img():
    img = base64.b64decode(img)
    img = BytesIO(img)
    img = Image.open(img)
    return img