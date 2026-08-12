import os
import json
import requests
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")
USERNAME = "sharaddsingh"


if not TOKEN:
    raise ValueError("GITHUB_TOKEN not found in .env")


# GitHub GraphQL API
URL = "https://api.github.com/graphql"


QUERY = """
query($username: String!) {
    user(login: $username) {
        contributionsCollection {
            contributionCalendar {
                totalContributions
                weeks {
                    contributionDays {
                        date
                        contributionCount
                        contributionLevel
                    }
                }
            }
        }
    }
}
"""


headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}


variables = {
    "username": USERNAME
}


response = requests.post(
    URL,
    json={
        "query": QUERY,
        "variables": variables
    },
    headers=headers
)


if response.status_code != 200:
    raise RuntimeError(
        f"GitHub API request failed: {response.status_code}\n"
        f"{response.text}"
    )


data = response.json()


if "errors" in data:
    raise RuntimeError(
        f"GitHub GraphQL error:\n{json.dumps(data['errors'], indent=2)}"
    )


calendar = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]


print("Total contributions:", calendar["totalContributions"])


days = []

for week in calendar["weeks"]:
    for day in week["contributionDays"]:
        days.append({
            "date": day["date"],
            "count": day["contributionCount"],
            "level": day["contributionLevel"]
        })


print("Total days:", len(days))

print("\nFirst 10 days:")

for day in days[:10]:
    print(day)


# Save structured data
os.makedirs("data", exist_ok=True)

output = {
    "username": USERNAME,
    "total": calendar["totalContributions"],
    "days": days
}


with open("data/contributions.json", "w", encoding="utf-8") as file:
    json.dump(output, file, indent=2)


print("\nContribution data saved to data/contributions.json")