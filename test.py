# This file is used to verify your http server acts as expected
# Run it with `python3 test.py``

import base64
import requests
from io import BytesIO
from PIL import Image

model_inputs = {
    'prompt': 'retro serie of different cars with different colors and shapes, mdjrny-v4 style',
    'negative': '',
    'num_inference_steps': 50,
    'guidance_scale': 7.5
}

res = requests.post('http://localhost:8000/', json = model_inputs)

image_byte_string = res.json()["image_base64"]

image_encoded = image_byte_string.encode('utf-8')
image_bytes = BytesIO(base64.b64decode(image_encoded))
image = Image.open(image_bytes)
image.save("output.jpg")