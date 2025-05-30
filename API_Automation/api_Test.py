import requests
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
else:
    print("Fetching is unsuccessful")