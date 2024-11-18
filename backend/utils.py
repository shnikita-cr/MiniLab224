from datetime import datetime, timedelta

import requests


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


def get_user_activity(username, headers):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        rj = response.json()
        one_week_ago = datetime.now() - timedelta(days=7)
        events_last_week = [event for event in rj if
                            datetime.strptime(event['created_at'], "%Y-%m-%dT%H:%M:%SZ") > one_week_ago]
        activity_count = len(events_last_week)
        event_types = {}
        for event in events_last_week:
            event_types[event["type"]] = event_types.get(event["type"], 0) + 1

        return activity_count, event_types
    else:
        return []
