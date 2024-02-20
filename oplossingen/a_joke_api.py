# Print de response van deze joke api:https://official-joke-api.appspot.com/random_joke
# Kijk naar het http_request voorbeeld om te zien hoe het moet.

import requests

response = requests.get("https://official-joke-api.appspot.com/random_joke")
print(response.text)

# Pas je code aan zodat:
# - Als de code gelijk is aan 200, de response geprint wordt.
# - Bij andere codes een foutmelding geprint wordt. (Wees creatief met je foutcodes).

if response.status_code == 200:
    print(response.text)
else:
    print("418 I'm a teapot")