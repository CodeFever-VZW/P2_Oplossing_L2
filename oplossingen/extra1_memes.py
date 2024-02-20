# Bekijk de documentatie van de meme API: https://apimeme.com/
# Roep de API aan en geef de afbeelding weer.
#
# Tip: Je kan de volgende import gebruiken.
# from PIL import Image
# from io import BytesIO

# !!! Hoewel je in de code van de module PIL importeert, installeer je daarvoor de module Pillow

# Tip: je kan van een response naar foto gaan met de volgende regels:
# image_data = BytesIO(response.content)
# image = Image.open(image_data)

import requests
from PIL import Image
from io import BytesIO

image_url = "https://apimeme.com/meme"

response = requests.get(url=image_url,
params={
    'meme': 'Back-In-My-Day',
    'top': 'Back in my day',
    'bottom': 'we had to draw memes'
})

if response.status_code == 200:
    image_data = BytesIO(response.content)
    image = Image.open(image_data)
    image.show()
else:
    print(f"Fout: {response.status_code} - {response.text}")