# import coordinates
import requests
import pytest
# # import json
# @pytest.fixture()
# def fixture_code():
#     print("This is our fixture code and it will execute before testcase")
#     print("------------------------------------------------------------")
url = "https://api.weather.gov/stations"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    station_ids = data['features']
    for station in station_ids:
            # coordinates = station['coordinates']
        properties = station['properties']
        features = station['geometry']
        if properties.get('timeZone') == "America/New_York":
            print(station['id'])
            coordinates = features['coordinates']
            print(properties['timeZone'])
            print(len(station['id']))
            print(f"Coordinates for the weather station related to timeZone : {coordinates}")
                # print(station['coordinates'])
                # if 'timeZone' == 'America/New_York':
                #     print(station['coordinates'])
    else:
        print("Fetching is unsuccessful")
# import requests
# header = {
#     'Accept': 'text/plain',
#     'Content-Type': 'application/json'
# }
#
# requests_payload = {
#     "id": 123,
#     "org": "cg",
#     "name": "abdul"
# }
#
# response = requests.post("https://sampleapis.com/futurama/api/characters", headers=header, json=requests_payload)
# print(response.status_code)
# print(response.json())
# data = response.json()
# assert response.status_code == 200
# assert data['id'] == 123