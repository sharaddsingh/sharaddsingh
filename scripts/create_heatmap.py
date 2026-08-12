import json
from datetime import datetime


INPUT_FILE = "data/contributions.json"
OUTPUT_FILE = "assets/contribution-heatmap.svg"

CELL_SIZE = 12
GAP = 4

LEFT_MARGIN = 35
TOP_MARGIN = 25

ROWS = 7

LEVEL_COLORS = {
    "NONE": "#161b22",
    "FIRST_QUARTILE": "#0e4429",
    "SECOND_QUARTILE": "#006d32",
    "THIRD_QUARTILE": "#26a641",
    "FOURTH_QUARTILE": "#39d353",
}


# -----------------------------
# Load contribution data
# -----------------------------

with open(INPUT_FILE, "r", encoding="utf-8") as file:
    data = json.load(file)

days = data["days"]


# -----------------------------
# Calculate dimensions
# -----------------------------

total_days = len(days)

weeks = (total_days + 6) // 7

width = (
    LEFT_MARGIN
    + weeks * (CELL_SIZE + GAP)
    + 20
)

height = (
    TOP_MARGIN
    + ROWS * (CELL_SIZE + GAP)
    + 25
)


# -----------------------------
# Start SVG
# -----------------------------

svg = []

svg.append(
    f'<svg width="{width}" height="{height}" '
    f'viewBox="0 0 {width} {height}" '
    f'xmlns="http://www.w3.org/2000/svg">'
)

svg.append(
    '<rect width="100%" height="100%" fill="#0d1117" rx="8"/>'
)


# -----------------------------
# Draw cells
# -----------------------------

for index, day in enumerate(days):

    date = datetime.strptime(
        day["date"],
        "%Y-%m-%d"
    )

    weekday = (date.weekday() + 1) % 7

    week = index // 7

    x = (
        LEFT_MARGIN
        + week * (CELL_SIZE + GAP)
    )

    y = (
        TOP_MARGIN
        + weekday * (CELL_SIZE + GAP)
    )

    level = day["level"]

    color = LEVEL_COLORS.get(
        level,
        LEVEL_COLORS["NONE"]
    )

    count = day["count"]

    # Each cell starts invisible
    # and fades in at a different time.

    delay = index * 0.015

    svg.append(
        f'''
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
                {day["date"]}: {count} contributions
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
        '''
    )


# -----------------------------
# Legend
# -----------------------------

legend_y = height - 17
legend_x = LEFT_MARGIN

svg.append(
    f'''
    <text
        x="{legend_x - 30}"
        y="{legend_y + 4}"
        fill="#8b949e"
        font-family="monospace"
        font-size="10"
    >
        Less
    </text>
    '''
)


legend_levels = [
    "NONE",
    "FIRST_QUARTILE",
    "SECOND_QUARTILE",
    "THIRD_QUARTILE",
    "FOURTH_QUARTILE",
]


for i, level in enumerate(legend_levels):

    x = (
        legend_x
        + i * (CELL_SIZE + GAP + 3)
    )

    svg.append(
        f'''
        <rect
            x="{x}"
            y="{legend_y - 8}"
            width="{CELL_SIZE}"
            height="{CELL_SIZE}"
            rx="2"
            fill="{LEVEL_COLORS[level]}"
        />
        '''
    )


svg.append(
    f'''
    <text
        x="{legend_x + 5 * (CELL_SIZE + GAP + 3) + 5}"
        y="{legend_y + 4}"
        fill="#8b949e"
        font-family="monospace"
        font-size="10"
    >
        More
    </text>
    '''
)


# -----------------------------
# Close SVG
# -----------------------------

svg.append("</svg>")


# -----------------------------
# Save
# -----------------------------

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as file:

    file.write("\n".join(svg))


print("Animated contribution heatmap created!")

print(
    f"Total contributions: {data['total']}"
)

print(
    f"Days processed: {len(days)}"
)

print(
    f"Output: {OUTPUT_FILE}"
)