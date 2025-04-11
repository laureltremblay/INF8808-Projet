# Load rink image
import base64
import os


image_path = "assets/images/rink.jpg"
image_uri = None
if image_path and os.path.exists(image_path):
    with open(image_path, "rb") as f:
        encoded_image = base64.b64encode(f.read()).decode()
        image_uri = f"data:image/jpg;base64,{encoded_image}"
