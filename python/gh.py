#!/usr/bin/env python3
import requests, sys

def follow():
    def get_followers():
        url = f"https://api.github.com/users/{username}/followers?per_page=100"
        users = requests.get(url).json()
        return set(user['login'] for user in users)

    def get_following():
        url = f"https://api.github.com/users/{username}/following?per_page=100"
        users = requests.get(url).json()
        return set(user['login'] for user in users)

    followers = get_followers()
    following = get_following()
    dont_follow_you = "\n".join(following - followers)
    you_dont_follow = "\n".join(followers - following)

    print(f"""
===============
You Dont Follow:
===============
{you_dont_follow}

===============
Dont Follow You:
===============
{dont_follow_you}
""")

def issues():
    repos = requests.get(f"https://api.github.com/users/{username}/repos").json()

    issues = []

    for repo in repos:
        name = repo["name"]
        open_issues = repo["open_issues"] # open_issues_count
        if open_issues > 0:
            issues.append(f" ({open_issues}) {name}")

    print("-  Issues/PRs  -")
    print("\n".join(issues))

def stars():
    repos = requests.get("https://api.github.com/users/tamton-aquib/repos").json()
    print(sum([repo['stargazers_count'] for repo in repos]))

_, command, *username = sys.argv
if not command: print("Enter a command. (issues/follow)"); sys.exit(1)
username = username[0] if len(username)>0 else input("Enter username: ").strip()

{'issues': issues, 'follow': follow, 'pr': issues, 'stars': stars}[command]()
