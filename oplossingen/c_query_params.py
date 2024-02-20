# Maak een programma dat:
# - De naam van de gebruiker vraagt.
# - De naam van de gebruiker doorstuurt naar de API.
# - Een tekstje print met de naam en de voorspelde leeftijd.

import requests

naam = input("Geef jouw naam: ")

response = requests.get(
    url=f"https://api.agify.io/",
    params={"name": naam}
)

if response.status_code == 200:
    data = response.json()
    leeftijd = data['age']

    print(f"{naam} is vermoedelijk  {leeftijd} jaar oud.")
else:
    print("Ooops! Probeer het later opnieuw.")