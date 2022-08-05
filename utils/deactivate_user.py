import requests

URL = "http://127.0.0.1:5000/users"


def deactivate_user(id):
    url = URL + "/" + id
    response = requests.delete(url, json=id)
    if response.status_code == 204:
        print("User successfully removed")
    else:
        print("Something went wrong while trying to remove the user.")


if __name__ == "__main__":
    id = input("Type in the user's id: ")
    deactivate_user(id)
