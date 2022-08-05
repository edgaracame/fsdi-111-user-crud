import requests

URL = "http://127.0.0.1:5000/users"


def update_user(first_name, last_name, hobbies, id):
    user = {
        "first_name": first_name,
        "last_name": last_name,
        "hobbies": hobbies
    }
    url = URL + "/" + id
    response = requests.put(url, json=user)
    if response.status_code == 204:
        print("User successfully updated")
    else:
        print("Something went wrong while trying to update the user.")


if __name__ == "__main__":
    id = input("Type in the user's id: ")
    fname = input("Type in the user's first name: ")
    lname = input("Type in the user's last name: ")
    hobbies = input("Type in the user's hobbies: ")
    update_user(fname, lname, hobbies, id)
