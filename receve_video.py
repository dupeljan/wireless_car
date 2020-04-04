

# Replace the URL with your own IPwebcam shot.jpg IP:port
url='http://192.168.1.39:8080/stream'
from PIL import Image
import requests
from io import BytesIO

response = requests.get(url)
img = Image.open(BytesIO(response.content))
img.show()