import requests

url = "https://certificationapi.oshwa.org/api/projects"

payload = {}
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYwMWRiYzE0ZTNkNjJjMDAxNzMyZWY2YyIsImlhdCI6MTY4MDcwNjUyMywiZXhwIjoxNjg5MzQ2NTIzfQ.yD2AUmqwnZtzWqhNr6Ur8HQqn08hAJUG8fVmoRQosHY'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
