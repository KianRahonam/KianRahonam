import requests.models

BASE_URL = "https://neo.labournet.in"
response = requests.get(f"{BASE_URL}",)
print(response.json())