import requests

URL = "http://127.0.0.1:5000/vehicles"


def create_vehicle(brand, model, color, year, userid):
    vehicle = {
        "brand": brand,
        "model": model,
        "color": color,
        "year": year,
        "userid": userid
    }
    response = requests.post(URL, json=vehicle)
    if response.status_code == 201:
        print("Successfully created new record; Got: %s" %
              response.json().get("message"))
    else:
        print("Something went wrong while trying to create a new vehicle.")


if __name__ == "__main__":
    brand = input("Type in the vehicle's brand: ")
    model = input("Type in the vehicle's model: ")
    color = input("Type in the vehicle's color: ")
    year = input("Type in the vehicle's year: ")
    userid = input("Type in the vehicle's owner id: ")
    create_vehicle(brand, model, color, year, userid)
