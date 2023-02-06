import requests
from datetime import datetime

USER_NAME = 'pokavv'
TOKEN = 'thisistokenkey'
GRAPH_ID = 'graph1'

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USER_NAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USER_NAME}/graphs'

graph_config = {
    'id': GRAPH_ID,
    'name': 'My Graph',
    'unit': 'Course',
    'type': 'float',
    'color': 'ajisai'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# response_graph = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response_graph.text)

today = datetime.now()
print(today)

pixel_creation = f'{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}'
pixel_data = {
    'date': today.strftime('%Y%m%d'),
    'quantity': input('How many course did you learn today? '),
}

response = requests.post(url=pixel_creation, json=pixel_data, headers=headers)
print(response.text)


#################### modify #####################

update_endpoint =f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

update_data = {
    'quantity': '5',
}

# response = requests.put(url=update_endpoint, json=update_data, headers=headers)
# print(response.text)

#################################################


#################### delete #####################

delete_endpoint =f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)

#################################################