import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "hhkjggkjhjkkhaeaa232342aa"
USERNAME = "uditmishra"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Outdoor Walk",
    "unit": "km",
    "type": "float",
    "color": "momiji",
    "timezone": "Asia/New Delhi"
}

header = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url= graph_endpoint, json=graph_config, headers=header)
# print(response.text)
# o/p at https://pixe.la/v1/users/uditmishra/graphs/graph1.html

today = datetime(year=2022, month=3, day=12)
print(today.strftime("%Y%m%d"))

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_creation_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "8.2",
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_creation_config, headers=header)
# print(response.text)

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
pixel_update_config = {
    "quantity": "8.5"
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_update_config, headers=header)
# print(response.text)

pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response = requests.delete(url=pixel_update_endpoint, headers=header)
print(response.text)


