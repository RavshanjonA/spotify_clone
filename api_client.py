import requests
import json
import threading


def user_login(username, password):
    url = "http://127.0.0.1:8000/user/api/token/"
    body = {"username": username, "password": password}
    repsonse = requests.post(data=body, url=url)
    return json.loads(repsonse.content)["access"]


def follow_artist(token):
    url = "http://127.0.0.1:8000/user/artist-follow/"
    headers = {"Authorization": f"Bearer {token}"}
    body = {"artistId": "57ec8ee4-a4a2-4439-8fb2-d6da37724b2b"}
    response = requests.request("POST", data=body, url=url, headers=headers)
    print(response.status_code, token)


def unfollow_artist(token):
    url = "http://127.0.0.1:8000/user/artist-unfollow/"
    headers = {"Authorization": f"Bearer {token}"}
    body = {"artistId": "57ec8ee4-a4a2-4439-8fb2-d6da37724b2b"}
    response = requests.request("POST", data=body, url=url, headers=headers)

    print(response.status_code, response.content)


if __name__ == "__main__":
    threads = []
    data = [
        {"username": "test1", "password": "test1"},
        {"username": "ravshanjon", "password": "12055"},
    ]
    tokens = [user_login(**user) for user in data]

    for token in tokens:
        t1 = threading.Thread(target=unfollow_artist, kwargs={"token": token})
        t1.start()
        threads.append(t1)
    for t in threads:
        t.join()
