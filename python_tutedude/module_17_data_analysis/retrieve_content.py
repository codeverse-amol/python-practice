import requests

url = "https://en.wikipedia.org/wiki/Narendra_Modi"
response = requests.get(url)

print(response.status_code)
print(response.text)