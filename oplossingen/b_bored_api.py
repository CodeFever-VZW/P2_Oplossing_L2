# Gebruik de bored api om een JSON-bestand in te lezen: https://www.boredapi.com/api/activity
# De response als json interpreteren kan zo: data = response.json()

import requests

response = requests.get("https://www.boredapi.com/api/activity")

if response.status_code == 200:
    activity_data = response.json()
    activity = activity_data['activity']

    print("Activiteit: ", activity)
else:
    print(f"Fout: {response.status_code} - {response.text}")