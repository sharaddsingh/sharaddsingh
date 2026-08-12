from pathlib import Path
import json
from datetime import datetime


# ============================================================
# Configuration
# ============================================================

WIDTH = 900
HEIGHT = 750

INPUT_FILE = Path("data/contributions.json")
OUTPUT_FILE = Path("assets/github-dashboard.svg")

FONT = "monospace"


# ============================================================
# Load contribution data
# ============================================================

with open(INPUT_FILE, "r", encoding="utf-8") as file:
    contribution_data = json.load(file)

days = contribution_data["days"]

total_contributions = contribution_data["total"]


# ============================================================
# Heatmap configuration
# ============================================================

CELL_SIZE = 12
GAP = 3

HEATMAP_X = 45
HEATMAP_Y = 370

LEVEL_COLORS = {
    "NONE": "#161b22",
    "FIRST_QUARTILE": "#0e4429",
    "SECOND_QUARTILE": "#006d32",
    "THIRD_QUARTILE": "#26a641",
    "FOURTH_QUARTILE": "#39d353",
}


# ============================================================
# Generate heatmap
# ============================================================

heatmap_cells = []

for index, day in enumerate(days):

    date = datetime.strptime(
        day["date"],
        "%Y-%m-%d"
    )

    weekday = (date.weekday() + 1) % 7

    week = index // 7

    x = HEATMAP_X + week * (CELL_SIZE + GAP)
    y = HEATMAP_Y + weekday * (CELL_SIZE + GAP)

    color = LEVEL_COLORS.get(
        day["level"],
        LEVEL_COLORS["NONE"]
    )

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
                dur="0.2s"
                fill="freeze"
            />

        </rect>
        """
    )


heatmap_svg = "\n".join(heatmap_cells)


# ============================================================
# Dashboard SVG
# ============================================================

svg = f"""
<svg
    width="{WIDTH}"
    height="{HEIGHT}"
    viewBox="0 0 {WIDTH} {HEIGHT}"
    xmlns="http://www.w3.org/2000/svg"
>

    <!-- ================================================= -->
    <!-- Background -->
    <!-- ================================================= -->

    <rect
        width="100%"
        height="100%"
        rx="16"
        fill="#0d1117"
        stroke="#30363d"
    />


    <!-- ================================================= -->
    <!-- Terminal command -->
    <!-- ================================================= -->

    <text
        x="45"
        y="55"
        fill="#58a6ff"
        font-family="{FONT}"
        font-size="22"
    >
        $ neofetch
    </text>


    <!-- ================================================= -->
    <!-- Name -->
    <!-- ================================================= -->

    <text
        x="45"
        y="105"
        fill="#ffffff"
        font-family="{FONT}"
        font-size="20"
    >
        Sharad Pratap Singh
    </text>


    <text
        x="45"
        y="135"
        fill="#8b949e"
        font-family="{FONT}"
        font-size="15"
    >
        -----------------------------
    </text>


    <!-- ================================================= -->
    <!-- Role -->
    <!-- ================================================= -->

    <text
        x="45"
        y="175"
        fill="#58a6ff"
        font-family="{FONT}"
        font-size="15"
    >
        Role
    </text>

    <text
        x="180"
        y="175"
        fill="#ffffff"
        font-family="{FONT}"
        font-size="15"
    >
        AI / Product Analyst
    </text>


    <!-- ================================================= -->
    <!-- Education -->
    <!-- ================================================= -->

    <text
        x="45"
        y="205"
        fill="#58a6ff"
        font-family="{FONT}"
        font-size="15"
    >
        Education
    </text>

    <text
        x="180"
        y="205"
        fill="#ffffff"
        font-family="{FONT}"
        font-size="15"
    >
        BITS Pilani
    </text>


    <!-- ================================================= -->
    <!-- Stack -->
    <!-- ================================================= -->

    <text
        x="45"
        y="235"
        fill="#58a6ff"
        font-family="{FONT}"
        font-size="15"
    >
        Stack
    </text>

    <text
        x="180"
        y="235"
        fill="#ffffff"
        font-family="{FONT}"
        font-size="15"
    >
        Python | FastAPI | AI
    </text>


    <!-- ================================================= -->
    <!-- Divider -->
    <!-- ================================================= -->

    <line
        x1="45"
        y1="280"
        x2="855"
        y2="280"
        stroke="#30363d"
    />


    <!-- ================================================= -->
    <!-- Contributions header -->
    <!-- ================================================= -->

    <text
        x="45"
        y="320"
        fill="#58a6ff"
        font-family="{FONT}"
        font-size="18"
    >
        Contributions
    </text>


    <text
        x="230"
        y="320"
        fill="#8b949e"
        font-family="{FONT}"
        font-size="14"
    >
        {total_contributions} contributions
    </text>


    <!-- ================================================= -->
    <!-- Heatmap -->
    <!-- ================================================= -->

    {heatmap_svg}


</svg>
"""


# ============================================================
# Save dashboard
# ============================================================

OUTPUT_FILE.write_text(
    svg,
    encoding="utf-8"
)

print("GitHub dashboard created!")
print(f"Total contributions: {total_contributions}")
print(f"Days processed: {len(days)}")
print(f"Output: {OUTPUT_FILE}")