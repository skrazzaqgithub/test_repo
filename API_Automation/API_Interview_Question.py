# import the requests library
import requests
import pytest

@pytest.fixture()
def fixture_code():
    print("This is our fixture code and it will execute before testcase")
    print("------------------------------------------------------------")

def test_code1_API_Testing(fixture_code):
    url = "https://api.weather.gov/stations"
    # Python break line can use \ , use variable to save url, make easier for copy paste
    response = requests.get(url)
    assert response.status_code == 200, "Response status code is not 200"
    # Send the request and assign the response result to the variable res

    if response.status_code == 200:
        data = response.json()
        station_ids = data['features']
        print("List of stations :", len(station_ids))

        chicago_found = False
        for station in station_ids:
            # station_response = requests.get(station_ids)
            # if station_response.status_code == 200:
            #   station_data = station_response.json()
            properties = station['properties']
            if properties.get('timeZone') == "America/Chicago":
                print(station['id'])
                chicago_found = True
        if chicago_found:
            print("Fetching is successful for America/Chicago timezone")
        else:
            print("No station found with America/Chicago timezone")