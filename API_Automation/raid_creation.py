import requests

# Replace with actual base URL of your storage system
BASE_URL = "http://storage-array.example.com/api"

# Sample headers (could also require Authorization token in real scenarios)
HEADERS = {
    "Content-Type": "application/json"
}

# === POST request to create RAID configuration ===
def create_raid(raid_level, disks, data_blocks):
    url = f"{BASE_URL}/raid/create"
    payload = {
        "raid_level": raid_level,  # "RAID0" or "RAID5"
        "disks": disks,
        "data_blocks": data_blocks
    }

    response = requests.post(url, json=payload, headers=HEADERS)
    print("\n[POST] Create RAID Response:")
    print(response.status_code, response.json())

# === GET request to verify RAID status ===
def get_raid_status():
    url = f"{BASE_URL}/raid/status"
    response = requests.get(url, headers=HEADERS)
    print("\n[GET] RAID Status Response:")
    print(response.status_code, response.json())


# === Sample Test Case ===
if __name__ == "__main__":
    # Simulate 3 disks
    disks = ["Disk0", "Disk1", "Disk2"]
    data_blocks = ["A", "B", "C", "D", "E", "F"]

    # Test RAID 0 creation
    create_raid("RAID0", disks, data_blocks)

    # Test RAID 5 creation
    create_raid("RAID5", disks, data_blocks)

    # Check RAID status
    get_raid_status()
