from pathlib import Path
import json
from datetime import datetime


# ============================================================
# Configuration
# ============================================================

WIDTH = 900
HEIGHT = 720

GITHUB_FILE = Path("data/github.json")
CONTRIBUTIONS_FILE = Path("data/contributions.json")

OUTPUT_FILE = Path("assets/github-dashboard.svg")


# ============================================================
# Load data
# ============================================================

with open(GITHUB_FILE, "r", encoding="utf-8") as file:
    github_data = json.load(file)

with open(CONTRIBUTIONS_FILE, "r", encoding="utf-8") as file:
    contribution_data = json.load(file)


# ============================================================
# GitHub data
# ============================================================

name = github_data["name"]
username = github_data["username"]

repositories = github_data["repositories"]
followers = github_data["followers"]
following = github_data["following"]

total_contributions = contribution_data["total"]
days = contribution_data["days"]


# ============================================================
# Colors
# ============================================================

BACKGROUND = "#0d1117"
BORDER = "#30363d"

WHITE = "#ffffff"
MUTED = "#8b949e"
BLUE = "#58a6ff"

LEVEL_COLORS = {
    "NONE": "#161b22",
    "FIRST_QUARTILE": "#0e4429",
    "SECOND_QUARTILE": "#006d32",
    "THIRD_QUARTILE": "#26a641",
    "FOURTH_QUARTILE": "#39d353",
}


# ============================================================
# Heatmap configuration
# ============================================================

CELL_SIZE = 10
GAP = 3

HEATMAP_X = 40
HEATMAP_Y = 490


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

    # One column per week
    week = index // 7

    x = HEATMAP_X + week * (
        CELL_SIZE + GAP
    )

    y = HEATMAP_Y + weekday * (
        CELL_SIZE + GAP
    )

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
# SVG
# ============================================================

svg = f"""<svg
    width="{WIDTH}"
    height="{HEIGHT}"
    viewBox="0 0 {WIDTH} {HEIGHT}"
    xmlns="http://www.w3.org/2000/svg"
>

    <!-- ================================================== -->
    <!-- Background -->
    <!-- ================================================== -->

    <rect
        x="0"
        y="0"
        width="{WIDTH}"
        height="{HEIGHT}"
        rx="16"
        fill="{BACKGROUND}"
        stroke="{BORDER}"
    />


    <!-- ================================================== -->
    <!-- Terminal -->
    <!-- ================================================== -->

    <text
        x="40"
        y="55"
        fill="{BLUE}"
        font-family="monospace"
        font-size="22"
    >
        $ neofetch
    </text>


    <!-- ================================================== -->
    <!-- Name -->
    <!-- ================================================== -->

    <text
        x="40"
        y="105"
        fill="{WHITE}"
        font-family="monospace"
        font-size="20"
    >
        {name}
    </text>


    <!-- ================================================== -->
    <!-- Divider -->
    <!-- ================================================== -->

    <text
        x="40"
        y="135"
        fill="{MUTED}"
        font-family="monospace"
        font-size="15"
    >
        -----------------------------
    </text>


    <!-- ================================================== -->
    <!-- Role -->
    <!-- ================================================== -->

    <text
        x="40"
        y="175"
        fill="{BLUE}"
        font-family="monospace"
        font-size="15"
    >
        Role
    </text>

    <text
        x="180"
        y="175"
        fill="{WHITE}"
        font-family="monospace"
        font-size="15"
    >
        AI Engineer
    </text>


    <!-- ================================================== -->
    <!-- Education -->
    <!-- ================================================== -->

    <text
        x="40"
        y="205"
        fill="{BLUE}"
        font-family="monospace"
        font-size="15"
    >
        Education
    </text>

    <text
        x="180"
        y="205"
        fill="{WHITE}"
        font-family="monospace"
        font-size="15"
    >
        BITS Pilani
    </text>


    <!-- ================================================== -->
    <!-- Skills -->
    <!-- ================================================== -->

    <text
        x="40"
        y="235"
        fill="{BLUE}"
        font-family="monospace"
        font-size="15"
    >
        Skills
    </text>

    <text
        x="180"
        y="235"
        fill="{WHITE}"
        font-family="monospace"
        font-size="15"
    >
        Python | FastAPI | Machine Learning | NLP | GenAI
    </text>


    <!-- ================================================== -->
    <!-- AI Stack -->
    <!-- ================================================== -->

    <text
        x="40"
        y="265"
        fill="{BLUE}"
        font-family="monospace"
        font-size="15"
    >
        AI Stack
    </text>

    <text
        x="180"
        y="265"
        fill="{WHITE}"
        font-family="monospace"
        font-size="15"
    >
        LangChain | RAG | LLMs | AI Agents
    </text>


    <!-- ================================================== -->
    <!-- Tools -->
    <!-- ================================================== -->

    <text
        x="40"
        y="295"
        fill="{BLUE}"
        font-family="monospace"
        font-size="15"
    >
        Tools
    </text>

    <text
        x="180"
        y="295"
        fill="{WHITE}"
        font-family="monospace"
        font-size="15"
    >
        Git | Docker | Streamlit | Jupyter | Firebase
    </text>


    <!-- ================================================== -->
    <!-- Divider -->
    <!-- ================================================== -->

    <line
        x1="40"
        y1="330"
        x2="860"
        y2="330"
        stroke="{BORDER}"
        stroke-width="1"
    />


    <!-- ================================================== -->
    <!-- GitHub Section -->
    <!-- ================================================== -->

    <text
        x="40"
        y="365"
        fill="{BLUE}"
        font-family="monospace"
        font-size="18"
    >
        GitHub
    </text>


    <!-- Repositories -->

    <text
        x="40"
        y="400"
        fill="{BLUE}"
        font-family="monospace"
        font-size="14"
    >
        Repositories
    </text>

    <text
        x="190"
        y="400"
        fill="{WHITE}"
        font-family="monospace"
        font-size="14"
    >
        {repositories}
    </text>


    <!-- Followers -->

    <text
        x="40"
        y="425"
        fill="{BLUE}"
        font-family="monospace"
        font-size="14"
    >
        Followers
    </text>

    <text
        x="190"
        y="425"
        fill="{WHITE}"
        font-family="monospace"
        font-size="14"
    >
        {followers}
    </text>


    <!-- Following -->

    <text
        x="40"
        y="450"
        fill="{BLUE}"
        font-family="monospace"
        font-size="14"
    >
        Following
    </text>

    <text
        x="190"
        y="450"
        fill="{WHITE}"
        font-family="monospace"
        font-size="14"
    >
        {following}
    </text>


    <!-- ================================================== -->
    <!-- Contributions -->
    <!-- ================================================== -->

    <text
        x="400"
        y="365"
        fill="{BLUE}"
        font-family="monospace"
        font-size="18"
    >
        Contributions
    </text>

    <text
        x="400"
        y="400"
        fill="{WHITE}"
        font-family="monospace"
        font-size="14"
    >
        {total_contributions} contributions
    </text>


    <!-- ================================================== -->
    <!-- Heatmap -->
    <!-- ================================================== -->

    {heatmap_svg}


    <!-- ================================================== -->
    <!-- Heatmap Legend -->
    <!-- ================================================== -->

    <text
        x="40"
        y="595"
        fill="{MUTED}"
        font-family="monospace"
        font-size="12"
    >
        Less
    </text>


    <rect
        x="80"
        y="587"
        width="10"
        height="10"
        rx="2"
        fill="{LEVEL_COLORS["NONE"]}"
    />

    <rect
        x="96"
        y="587"
        width="10"
        height="10"
        rx="2"
        fill="{LEVEL_COLORS["FIRST_QUARTILE"]}"
    />

    <rect
        x="112"
        y="587"
        width="10"
        height="10"
        rx="2"
        fill="{LEVEL_COLORS["SECOND_QUARTILE"]}"
    />

    <rect
        x="128"
        y="587"
        width="10"
        height="10"
        rx="2"
        fill="{LEVEL_COLORS["THIRD_QUARTILE"]}"
    />

    <rect
        x="144"
        y="587"
        width="10"
        height="10"
        rx="2"
        fill="{LEVEL_COLORS["FOURTH_QUARTILE"]}"
    />

    <text
        x="165"
        y="595"
        fill="{MUTED}"
        font-family="monospace"
        font-size="12"
    >
        More
    </text>


    <!-- ================================================== -->
    <!-- Footer -->
    <!-- ================================================== -->

    <text
        x="40"
        y="675"
        fill="{MUTED}"
        font-family="monospace"
        font-size="13"
    >
        github.com/{username}
    </text>


    <!-- Online indicator -->

    <circle
        cx="685"
        cy="675"
        r="4"
        fill="{BLUE}"
    />

    <text
        x="700"
        y="679"
        fill="{BLUE}"
        font-family="monospace"
        font-size="13"
    >
        online
    </text>


</svg>
"""


# ============================================================
# Save SVG
# ============================================================

OUTPUT_FILE.parent.mkdir(
    parents=True,
    exist_ok=True
)

OUTPUT_FILE.write_text(
    svg,
    encoding="utf-8"
)


# ============================================================
# Done
# ============================================================

print("GitHub dashboard SVG created!")
print(f"Repositories: {repositories}")
print(f"Followers: {followers}")
print(f"Following: {following}")
print(f"Contributions: {total_contributions}")
print(f"Heatmap cells: {len(days)}")
print(f"Output: {OUTPUT_FILE}")
