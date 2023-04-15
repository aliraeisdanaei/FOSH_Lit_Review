import requests

url = "https://certificationapi.oshwa.org/api/projects"

payload = {
}

paramaters = {
    "limit": 62,
    "offset": 2000
}

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYwMWRiYzE0ZTNkNjJjMDAxNzMyZWY2YyIsImlhdCI6MTY4MDcwNjUyMywiZXhwIjoxNjg5MzQ2NTIzfQ.yD2AUmqwnZtzWqhNr6Ur8HQqn08hAJUG8fVmoRQosHY', 
}

response = requests.request("GET", url, headers=headers, data=payload, params=paramaters)


fname_out = "certifications.json"
with open(fname_out, "w") as f:
    f.write(response.text)