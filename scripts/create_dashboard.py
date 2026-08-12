from pathlib import Path
import json


# --------------------------------
# Configuration
# --------------------------------

WIDTH = 900
HEIGHT = 650

GITHUB_FILE = Path("data/github.json")
CONTRIBUTIONS_FILE = Path("data/contributions.json")

OUTPUT_FILE = Path("assets/github-dashboard.svg")


# --------------------------------
# Load GitHub data
# --------------------------------

with open(GITHUB_FILE, "r", encoding="utf-8") as file:
    github_data = json.load(file)


# --------------------------------
# Load contribution data
# --------------------------------

with open(
    CONTRIBUTIONS_FILE,
    "r",
    encoding="utf-8"
) as file:

    contribution_data = json.load(file)


# --------------------------------
# Extract dynamic values
# --------------------------------

name = github_data["name"]
username = github_data["username"]

repositories = github_data["repositories"]
followers = github_data["followers"]
following = github_data["following"]

total_contributions = contribution_data["total"]


# --------------------------------
# Create dashboard
# --------------------------------

svg = f"""<svg
    width="{WIDTH}"
    height="{HEIGHT}"
    viewBox="0 0 {WIDTH} {HEIGHT}"
    xmlns="http://www.w3.org/2000/svg"
>

    <!-- Background -->

    <rect
        width="100%"
        height="100%"
        rx="16"
        fill="#0d1117"
        stroke="#30363d"
    />


    <!-- Terminal command -->

    <text
        x="40"
        y="55"
        fill="#58a6ff"
        font-family="monospace"
        font-size="22"
    >
        $ neofetch
    </text>


    <!-- Name -->

    <text
        x="40"
        y="100"
        fill="#ffffff"
        font-family="monospace"
        font-size="20"
    >
        {name}
    </text>


    <!-- Separator -->

    <text
        x="40"
        y="130"
        fill="#8b949e"
        font-family="monospace"
        font-size="15"
    >
        -----------------------------
    </text>


    <!-- Role -->

    <text
        x="40"
        y="165"
        fill="#58a6ff"
        font-family="monospace"
        font-size="15"
    >
        Role
    </text>

    <text
        x="180"
        y="165"
        fill="#ffffff"
        font-family="monospace"
        font-size="15"
    >
        AI / Product Analyst
    </text>


    <!-- Education -->

    <text
        x="40"
        y="195"
        fill="#58a6ff"
        font-family="monospace"
        font-size="15"
    >
        Education
    </text>

    <text
        x="180"
        y="195"
        fill="#ffffff"
        font-family="monospace"
        font-size="15"
    >
        BITS Pilani
    </text>


    <!-- Stack -->

    <text
        x="40"
        y="225"
        fill="#58a6ff"
        font-family="monospace"
        font-size="15"
    >
        Stack
    </text>

    <text
        x="180"
        y="225"
        fill="#ffffff"
        font-family="monospace"
        font-size="15"
    >
        Python | FastAPI | AI
    </text>


    <!-- Separator -->

    <line
        x1="40"
        y1="260"
        x2="860"
        y2="260"
        stroke="#30363d"
    />


    <!-- GitHub section -->

    <text
        x="40"
        y="300"
        fill="#58a6ff"
        font-family="monospace"
        font-size="17"
    >
        GitHub
    </text>


    <!-- Repositories -->

    <text
        x="40"
        y="335"
        fill="#58a6ff"
        font-family="monospace"
        font-size="14"
    >
        Repositories
    </text>

    <text
        x="190"
        y="335"
        fill="#ffffff"
        font-family="monospace"
        font-size="14"
    >
        {repositories}
    </text>


    <!-- Followers -->

    <text
        x="40"
        y="360"
        fill="#58a6ff"
        font-family="monospace"
        font-size="14"
    >
        Followers
    </text>

    <text
        x="190"
        y="360"
        fill="#ffffff"
        font-family="monospace"
        font-size="14"
    >
        {followers}
    </text>


    <!-- Following -->

    <text
        x="40"
        y="385"
        fill="#58a6ff"
        font-family="monospace"
        font-size="14"
    >
        Following
    </text>

    <text
        x="190"
        y="385"
        fill="#ffffff"
        font-family="monospace"
        font-size="14"
    >
        {following}
    </text>


    <!-- Contributions -->

    <text
        x="400"
        y="300"
        fill="#58a6ff"
        font-family="monospace"
        font-size="17"
    >
        Contributions
    </text>

    <text
        x="400"
        y="335"
        fill="#ffffff"
        font-family="monospace"
        font-size="14"
    >
        {total_contributions} contributions
    </text>


    <!-- Contribution heatmap -->

    <image
        href="contribution-heatmap.svg"
        x="40"
        y="410"
        width="820"
        height="150"
        preserveAspectRatio="xMidYMid meet"
    />


    <!-- Footer -->

    <text
        x="40"
        y="610"
        fill="#8b949e"
        font-family="monospace"
        font-size="13"
    >
        github.com/{username}
    </text>


    <!-- Status -->

    <circle
        cx="690"
        cy="606"
        r="4"
        fill="#58a6ff"
    />

    <text
        x="705"
        y="610"
        fill="#58a6ff"
        font-family="monospace"
        font-size="13"
    >
        online
    </text>

</svg>
"""


# --------------------------------
# Save dashboard
# --------------------------------

OUTPUT_FILE.parent.mkdir(
    parents=True,
    exist_ok=True
)

OUTPUT_FILE.write_text(
    svg,
    encoding="utf-8"
)


# --------------------------------
# Output
# --------------------------------

print("GitHub dashboard created!")

print(f"Repositories: {repositories}")
print(f"Followers: {followers}")
print(f"Following: {following}")
print(f"Contributions: {total_contributions}")

print(f"Output: {OUTPUT_FILE}")