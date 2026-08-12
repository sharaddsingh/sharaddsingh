import json
import os
from pathlib import Path

import requests
from dotenv import load_dotenv


# --------------------------------
# Configuration
# --------------------------------

load_dotenv()

USERNAME = "sharaddsingh"

OUTPUT_FILE = Path("data/github.json")

TOKEN = os.getenv("GITHUB_TOKEN")


# --------------------------------
# GitHub API request
# --------------------------------

url = f"https://api.github.com/users/{USERNAME}"

headers = {
    "Accept": "application/vnd.github+json"
}

if TOKEN:
    headers["Authorization"] = f"Bearer {TOKEN}"


response = requests.get(
    url,
    headers=headers,
    timeout=10
)

response.raise_for_status()

data = response.json()


# --------------------------------
# Extract useful public data
# --------------------------------

github_data = {
    "username": data["login"],
    "name": data["name"],
    "repositories": data["public_repos"],
    "followers": data["followers"],
    "following": data["following"]
}


# --------------------------------
# Save data
# --------------------------------

OUTPUT_FILE.parent.mkdir(
    parents=True,
    exist_ok=True
)

OUTPUT_FILE.write_text(
    json.dumps(
        github_data,
        indent=4
    ),
    encoding="utf-8"
)


# --------------------------------
# Output
# --------------------------------

print("GitHub data fetched successfully!")

print(f"Username: {github_data['username']}")
print(f"Name: {github_data['name']}")
print(f"Repositories: {github_data['repositories']}")
print(f"Followers: {github_data['followers']}")
print(f"Following: {github_data['following']}")

print(f"Output: {OUTPUT_FILE}")