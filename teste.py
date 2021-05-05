import io
from PIL import Image
im = Image.new("RGB", (100, 100))
b = io.BytesIO()
im.save(b, "JPEG")

b.seek(0)
fb = io.BufferedReader(b)

print(type(fb))