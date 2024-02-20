# Bekijk de documentatie voor de free games API: https://www.freetogame.com/api-doc
# Hoe zou je een lijst met games kunnen binnenhalen met de volgende voorwaarden?
# - PC-games
# - Gesorteerd volgens relevantie

# Bijkomende opdracht:
# Print voor alle pc-games die het woord “world” bevatten, de titel en de game_url.
# Zorg dat het niet gevoelig is aan hoofdletters.

import requests

response = requests.get(
    url="https://www.freetogame.com/api/games",
    params={
        'platform': 'pc',
        'sort-by': 'relevance'
    }
)

if response.status_code == 200:
    game_data = response.json()
    for game in game_data:
        if "world" in game['title'].lower():
            print(f"{game['title']}: {game['game_url']}")
else:
    print(f"Fout: {response.status_code} - {response.text}")