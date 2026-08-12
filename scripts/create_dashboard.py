from pathlib import Path
import json
from datetime import datetime


# ============================================================
# Configuration
# ============================================================

WIDTH = 900
HEIGHT = 650

GITHUB_FILE = Path("data/github.json")
CONTRIBUTIONS_FILE = Path("data/contributions.json")
OUTPUT_FILE = Path("assets/github-dashboard.svg")


# ============================================================
# Load GitHub data
# ============================================================

with open(GITHUB_FILE, "r", encoding="utf-8") as file:
    github_data = json.load(file)


# ============================================================
# Load contribution data
# ============================================================

with open(CONTRIBUTIONS_FILE, "r", encoding="utf-8") as file:
    contribution_data = json.load(file)


days = contribution_data["days"]

name = github_data["name"]
username = github_data["username"]

repositories = github_data["repositories"]
followers = github_data["followers"]
following = github_data["following"]

total_contributions = contribution_data["total"]


# ============================================================
# Heatmap configuration
# ============================================================

CELL_SIZE = 10
GAP = 3

HEATMAP_X = 40
HEATMAP_Y = 420

LEVEL_COLORS = {
    "NONE": "#161b22",
    "FIRST_QUARTILE": "#0e4429",
    "SECOND_QUARTILE": "#006d32",
    "THIRD_QUARTILE": "#26a641",
    "FOURTH_QUARTILE": "#39d353",
}


# ============================================================
# Generate heatmap cells
# ============================================================

heatmap_cells = []

for index, day in enumerate(days):

    date = datetime.strptime(
        day["date"],
        "%Y-%m-%d"
    )

    # Sunday = 0
    weekday = (date.weekday() + 1) % 7

    # Every 7 days = next column
    week = index // 7

    x = HEATMAP_X + week * (CELL_SIZE + GAP)
    y = HEATMAP_Y + weekday * (CELL_SIZE + GAP)

    color = LEVEL_COLORS.get(
        day["level"],
        LEVEL_COLORS["NONE"]
    )

    heatmap_cells.append(
        f"""
        <rect
            x="{x}"
            y="{y}"
            width="{CELL_SIZE}"
            height="{CELL_SIZE}"
            rx="2"
            fill="{color}"
        >
            <title>
                {day["date"]}: {day["count"]} contributions
            </title>
        </rect>
        """
    )


heatmap_svg = "\n".join(heatmap_cells)


# ============================================================
# Create dashboard SVG
# ============================================================

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


    <!-- Terminal -->

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


    <!-- GitHub -->

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


    <!-- Heatmap -->

    {heatmap_svg}


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


    <!-- Online indicator -->

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


# ============================================================
# Save
# ============================================================

OUTPUT_FILE.parent.mkdir(
    parents=True,
    exist_ok=True
)

OUTPUT_FILE.write_text(
    svg,
    encoding="utf-8"
)


print("GitHub dashboard created!")
print(f"Repositories: {repositories}")
print(f"Followers: {followers}")
print(f"Following: {following}")
print(f"Contributions: {total_contributions}")
print(f"Heatmap cells: {len(days)}")
print(f"Output: {OUTPUT_FILE}")