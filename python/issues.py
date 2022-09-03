#!/usr/bin/env python3
import requests

repos = requests.get("https://api.github.com/users/tamton-aquib/repos").json()

for repo in repos:
    name = repo["name"]
    open_issues = repo["open_issues"] # open_issues_count
    if open_issues > 0:
        print(f" ({open_issues}) {name}")


# TODO: pagination: "https://api.github.com/repos/tamton-aquib/veldora/issues{/number}"
