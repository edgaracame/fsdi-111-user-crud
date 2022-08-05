import requests

URL = "http://127.0.0.1:5000/vehicles"


def deactivate_vehicle(id):
    url = URL + "/" + id
    response = requests.delete(url, json=id)
    if response.status_code == 204:
        print("Vehicle successfully removed")
    else:
        print("Something went wrong while trying to remove the vehicle.")


if __name__ == "__main__":
    id = input("Type in the vehicle's id: ")
    deactivate_vehicle(id)
