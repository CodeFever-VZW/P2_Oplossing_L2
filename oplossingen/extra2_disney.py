# Bekijk de documentatie voor de Disney API: https://disneyapi.dev/docs/
# Vraag aan de API alle personages.
#
# Print alle personages als volgt:
# Naam: Abu - Oorspronkelijke film: Aladdin (film)
# Naam: Abuelita - Oorspronkelijke film: Onbekend

import requests

# api_url = "http://api.disneyapi.dev/character"
# Zorg er voor dat je alle personages kan tonen.
api_url = "http://api.disneyapi.dev/character?page=&pageSize=7438"
response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()

    print("Lijst met Disney-personages:")
    for personage in data['data']:
        naam = personage['name']
        films = personage['films']
        if films:
            oorspronkelijke_film = films[0]
        else:
            oorspronkelijke_film = "Onbekend"
        print(f"Naam: {naam} - Oorspronkelijke film: {oorspronkelijke_film}")

else:
    print(f"Fout: {response.status_code} - {response.text}")