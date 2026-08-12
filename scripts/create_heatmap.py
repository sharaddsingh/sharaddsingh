from pathlib import Path
import json
from datetime import datetime

# --------------------------------
# Configuration
# --------------------------------

WIDTH = 790
HEIGHT = 180

INPUT_FILE = Path("data/contributions.json")
OUTPUT_FILE = Path("assets/contribution-heatmap.svg")

CELL_SIZE = 10
GAP = 3

HEATMAP_X = 40
HEATMAP_Y = 15

LEVEL_COLORS = {
    "NONE": "#161b22",
    "FIRST_QUARTILE": "#0e4429",
    "SECOND_QUARTILE": "#006d32",
    "THIRD_QUARTILE": "#26a641",
    "FOURTH_QUARTILE": "#39d353",
}

# --------------------------------
# Load contribution data
# --------------------------------

with open(INPUT_FILE, "r", encoding="utf-8") as file:
    contribution_data = json.load(file)

days = contribution_data["days"]

# --------------------------------
# Generate heatmap cells
# --------------------------------

heatmap_cells = []

for index, day in enumerate(days):

    date = datetime.strptime(
        day["date"],
        "%Y-%m-%d"
    )

    # Sunday = 0
    weekday = (date.weekday() + 1) % 7

    # Every 7 days = one column
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

# --------------------------------
# Create SVG
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
        rx="10"
        fill="#0d1117"
    />

    <!-- Contribution heatmap -->

    {heatmap_svg}

</svg>
"""

# --------------------------------
# Save SVG
# --------------------------------

OUTPUT_FILE.write_text(
    svg,
    encoding="utf-8"
)

print("Contribution heatmap created!")
print(f"Weeks: {(len(days) + 6) // 7}")
print(f"Days: {len(days)}")
print(f"Output: {OUTPUT_FILE}")