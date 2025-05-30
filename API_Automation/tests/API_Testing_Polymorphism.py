import requests

class APIRequest:
    """Base class for API requests"""
    def __init__(self, base_url):
        self.base_url = base_url

    def send_request(self, endpoint, **kwargs):
        """Method to be overridden by subclasses"""
        raise NotImplementedError("Subclasses must implement this method.")

class GetRequest(APIRequest):
    def send_request(self, endpoint, **kwargs):
        response = requests.get(f"{self.base_url}/{endpoint}", params=kwargs.get("params"))
        return response

# class PostRequest(APIRequest):
#     def send_request(self, endpoint, **kwargs):
#         response = requests.post(f"{self.base_url}/{endpoint}", json=kwargs.get("data"))
#         return response
#
# class PutRequest(APIRequest):
#     def send_request(self, endpoint, **kwargs):
#         response = requests.put(f"{self.base_url}/{endpoint}", json=kwargs.get("data"))
#         return response
#
# class DeleteRequest(APIRequest):
#     def send_request(self, endpoint, **kwargs):
#         response = requests.delete(f"{self.base_url}/{endpoint}")
#         return response

# Example Usage:
# BASE_URL = "https://jsonplaceholder.typicode.com"
BASE_URL = "https://api.weather.gov"

# Testing GET request
get_api = GetRequest(BASE_URL)
response = get_api.send_request("/stations")
print(response.status_code, response.json())

# Testing POST request
# post_api = PostRequest(BASE_URL)
# new_post = {"title": "Test Title", "body": "Test Body", "userId": 1}
# response = post_api.send_request("posts", data=new_post)
# print(response.status_code, response.json())