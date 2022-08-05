import requests

URL = "http://127.0.0.1:5000/vehicles"


def update_vehicle(brand, model, color, year, userid, id):
    vehicle = {
        "brand": brand,
        "model": model,
        "color": color,
        "year": year,
        "userid": userid
    }
    url = URL + "/" + id
    response = requests.put(url, json=vehicle)
    if response.status_code == 204:
        print("Vehicle successfully updated")
    else:
        print("Something went wrong while trying to update the vehicle.")


if __name__ == "__main__":
    id = input("Type in the vehicle's id: ")
    brand = input("Type in the vehicle's brand: ")
    model = input("Type in the vehicle's model: ")
    color = input("Type in the vehicle's color: ")
    year = input("Type in the vehicle's year: ")
    userid = input("Type in the vehicle's owner id: ")
    update_vehicle(brand, model, color, year, userid, id)
