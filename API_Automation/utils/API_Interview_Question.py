# import the requests library
import requests

@pytest.fixture()
def fixture_code():
    print("This is our fixture code and it will execute before testcase")
    print("------------------------------------------------------------")

def code1_API_Testing(fixture_code):
    url = "https://api.weather.gov/stations"
    # Python break line can use \ , use variable to save url, make easier for copy paste
    response = requests.get(url)
    # Send the request and assign the response result to the variable res

    if response.status_code == 200:
        data = response.json()
        station_ids = data['features']
        print("List of stations :", len(station_ids))

        for station in station_ids:
            # station_response = requests.get(station_ids)
            # if station_response.status_code == 200:
            #   station_data = station_response.json()
            properties = station['properties']
            if properties.get('timeZone') == "America/Chicago":
                print(station['id'])
        else:
            print(f"Fetching is unsuccessful")