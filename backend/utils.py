import requests


def get_recursive_followers(response_given, headers, depth=5):
    lst = []
    for i in response_given.json():
        follower = i["login"]
        followers_url = f"https://api.github.com/users/{follower}/followers"
        response = requests.get(followers_url, headers=headers)
        if response.status_code == 200:  # Проверка кода ответа
            lst.append(response)
    return lst


def get_followers(username, headers):
    url = f"https://api.github.com/users/{username}/followers"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return []


def get_repositories(username, headers):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return []


def add_users_data(response_json, headers, depth=0):
    if depth < 0:
        return
    for user in response_json:
        followers = get_followers(user["login"], headers)
        if followers:
            if depth > 1:
                add_users_data(followers, headers, depth - 1)
                user["followers"] = followers
            repos = get_repositories(user["login"], headers)
            user["size"] = len(repos)
