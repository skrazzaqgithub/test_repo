import requests

class LoginError(Exception):
    """Custom exception for login failure."""
    pass

def login_to_website(username, password):
    login_url = "https://reqres.in/api/login"
    payload = {
        'username': username,
        'password': password
    }

    try:
        response = requests.post(login_url, data=payload, timeout=5)

        # Raise HTTP error for bad responses (4xx, 5xx)
        response.raise_for_status()

        # Simulating login success/failure check (you'd adjust this for your real use case)
        if "Login failed" in response.text or response.status_code == 401:
            raise LoginError("Invalid username or password.")

        print("✅ Login successful!")
        return response.text

    except LoginError as le:
        print(f"❌ Login failed: {le}")
    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("❌ Connection error. Check your internet or URL.")
    except requests.exceptions.Timeout:
        print("❌ Timeout occurred.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Example usage
username = input("Enter username: ")
password = input("Enter password: ")

login_to_website(username, password)
