import requests
import io
from PIL import Image

API_TOKEN = "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"
headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

prompt = input("Enter a description for the image you'd like to generate: ")

# Using Stable Diffusion XL model which is known to work with the API
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"

# Make the request
response = requests.post(
    API_URL,
    headers=headers,
    json={"inputs": prompt}
)

# Check if the request was successful
if response.status_code == 200:
    # Convert the response content to an image
    image = Image.open(io.BytesIO(response.content))
    # Save the image
    image.save("generated_image.png")
    print("Image successfully generated and saved as 'generated_image.png'")
else:
    print(f"Error: {response.status_code}")
    print(response.text)