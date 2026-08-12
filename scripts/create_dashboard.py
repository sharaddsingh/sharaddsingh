from pathlib import Path
import json
from datetime import datetime


# -----------------------------
# Configuration
# -----------------------------

WIDTH = 900
HEIGHT = 650

OUTPUT_FILE = Path("assets/github-dashboard.svg")
INPUT_FILE = Path("data/contributions.json")


# -----------------------------
# Load contribution data
# -----------------------------

with open(INPUT_FILE, "r", encoding="utf-8") as file:
    contribution_data = json.load(file)

days = contribution_data["days"]


# -----------------------------
# Heatmap configuration
# -----------------------------

CELL_SIZE = 10
GAP = 3

HEATMAP_X = 60
HEATMAP_Y = 350

LEVEL_COLORS = {
    "NONE": "#161b22",
    "FIRST_QUARTILE": "#0e4429",
    "SECOND_QUARTILE": "#006d32",
    "THIRD_QUARTILE": "#26a641",
    "FOURTH_QUARTILE": "#39d353",
}


# -----------------------------
# Generate contribution cells
# -----------------------------

heatmap_cells = []

for index, day in enumerate(days):

    date = datetime.strptime(
        day["date"],
        "%Y-%m-%d"
    )

    # Sunday = 0
    weekday = (date.weekday() + 1) % 7

    # Each 7 days = one column
    week = index // 7

    x = HEATMAP_X + week * (CELL_SIZE + GAP)
    y = HEATMAP_Y + weekday * (CELL_SIZE + GAP)

    color = LEVEL_COLORS.get(
        day["level"],
        LEVEL_COLORS["NONE"]
    )

    # Animation delay
    delay = index * 0.015

    heatmap_cells.append(
        f"""
        <rect
            x="{x}"
            y="{y}"
            width="{CELL_SIZE}"
            height="{CELL_SIZE}"
            rx="2"
            fill="{color}"
            opacity="0"
        >
            <title>
                {day["date"]}: {day["count"]} contributions
            </title>

            <animate
                attributeName="opacity"
                from="0"
                to="1"
                begin="{delay:.3f}s"
                dur="0.25s"
                fill="freeze"
            />
        </rect>
        """
    )


heatmap_svg = "\n".join(heatmap_cells)


# -----------------------------
# Create SVG
# -----------------------------

svg = f"""
<svg
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


    <!-- Terminal header -->

    <text
        x="40"
        y="55"
        fill="#58a6ff"
        font-family="monospace"
        font-size="22"
    >
        $ neofetch
    </text>


    <!-- Profile -->

    <text
        x="40"
        y="105"
        fill="#ffffff"
        font-family="monospace"
        font-size="20"
    >
        Sharad Pratap Singh
    </text>

    <text
        x="40"
        y="135"
        fill="#8b949e"
        font-family="monospace"
        font-size="15"
    >
        -----------------------------
    </text>


    <!-- Information -->

    <text
        x="40"
        y="175"
        fill="#58a6ff"
        font-family="monospace"
        font-size="15"
    >
        Role
    </text>

    <text
        x="180"
        y="175"
        fill="#ffffff"
        font-family="monospace"
        font-size="15"
    >
        AI / Product Analyst
    </text>


    <text
        x="40"
        y="205"
        fill="#58a6ff"
        font-family="monospace"
        font-size="15"
    >
        Education
    </text>

    <text
        x="180"
        y="205"
        fill="#ffffff"
        font-family="monospace"
        font-size="15"
    >
        BITS Pilani
    </text>


    <text
        x="40"
        y="235"
        fill="#58a6ff"
        font-family="monospace"
        font-size="15"
    >
        Stack
    </text>

    <text
        x="180"
        y="235"
        fill="#ffffff"
        font-family="monospace"
        font-size="15"
    >
        Python | FastAPI | AI
    </text>


    <!-- Contribution section -->

    <text
        x="40"
        y="310"
        fill="#58a6ff"
        font-family="monospace"
        font-size="18"
    >
        Contributions
    </text>


    <!-- Heatmap -->

    {heatmap_svg}


    <!-- Legend -->

    <text
        x="60"
        y="455"
        fill="#8b949e"
        font-family="monospace"
        font-size="11"
    >
        Less
    </text>

    <rect
        x="100"
        y="445"
        width="10"
        height="10"
        rx="2"
        fill="#161b22"
    />

    <rect
        x="116"
        y="445"
        width="10"
        height="10"
        rx="2"
        fill="#0e4429"
    />

    <rect
        x="132"
        y="445"
        width="10"
        height="10"
        rx="2"
        fill="#006d32"
    />

    <rect
        x="148"
        y="445"
        width="10"
        height="10"
        rx="2"
        fill="#26a641"
    />

    <rect
        x="164"
        y="445"
        width="10"
        height="10"
        rx="2"
        fill="#39d353"
    />

    <text
        x="182"
        y="455"
        fill="#8b949e"
        font-family="monospace"
        font-size="11"
    >
        More
    </text>


    <!-- Footer -->

    <text
        x="40"
        y="610"
        fill="#8b949e"
        font-family="monospace"
        font-size="13"
    >
        github.com/sharaddsingh
    </text>

</svg>
"""


# -----------------------------
# Save SVG
# -----------------------------

OUTPUT_FILE.write_text(
    svg,
    encoding="utf-8"
)


print("Dashboard SVG created!")
print(f"Total contributions: {contribution_data['total']}")
print(f"Days processed: {len(days)}")
print(f"Output: {OUTPUT_FILE}")