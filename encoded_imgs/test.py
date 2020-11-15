import base64
from PIL import Image
import io

fn = '1605461846.368733.txt'
# fn = 'b64_raw.txt'
with open(fn, 'r') as f:
    b64 = f.read()


# b64.replace("b'", "")
# b64.replace("'", "")

print(type(b64))
print(b64[:10])
print()
b64 = base64.b64decode(b64)
print(type(b64))
print(b64[:10])
image = Image.open(io.BytesIO(b64))
image.show()

