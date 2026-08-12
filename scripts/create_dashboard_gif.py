from pathlib import Path
import json
from datetime import datetime

from PIL import Image, ImageDraw, ImageFont


# ============================================================
# Configuration
# ============================================================

WIDTH = 900
HEIGHT = 650

GITHUB_FILE = Path("data/github.json")
CONTRIBUTIONS_FILE = Path("data/contributions.json")

OUTPUT_FILE = Path("assets/github-dashboard.gif")

# Number of cells revealed per frame
CELLS_PER_FRAME = 12

# Speed of animation
FRAME_DURATION = 120

# How long the completed dashboard stays visible
FINAL_FRAME_DURATION = 3000


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
# Fonts
# ============================================================

FONT_PATH = "C:/Windows/Fonts/consola.ttf"

FONT_TITLE = ImageFont.truetype(
    FONT_PATH,
    22
)

FONT_NAME = ImageFont.truetype(
    FONT_PATH,
    20
)

FONT_NORMAL = ImageFont.truetype(
    FONT_PATH,
    15
)

FONT_SMALL = ImageFont.truetype(
    FONT_PATH,
    14
)

FONT_FOOTER = ImageFont.truetype(
    FONT_PATH,
    13
)


# ============================================================
# Heatmap configuration
# ============================================================

CELL_SIZE = 10
GAP = 3

HEATMAP_X = 40
HEATMAP_Y = 430


# ============================================================
# Prepare heatmap cells
# ============================================================

cells = []

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

    cells.append({
        "x": x,
        "y": y,
        "color": color,
        "date": day["date"],
        "count": day["count"],
    })


# ============================================================
# Create one dashboard frame
# ============================================================

def create_dashboard(revealed_cells):

    image = Image.new(
        "RGB",
        (WIDTH, HEIGHT),
        BACKGROUND
    )

    draw = ImageDraw.Draw(image)


    # --------------------------------------------------------
    # Border
    # --------------------------------------------------------

    draw.rounded_rectangle(
        (0, 0, WIDTH - 1, HEIGHT - 1),
        radius=16,
        outline=BORDER,
        width=1
    )


    # --------------------------------------------------------
    # Terminal
    # --------------------------------------------------------

    draw.text(
        (40, 30),
        "$ neofetch",
        fill=BLUE,
        font=FONT_TITLE
    )


    # --------------------------------------------------------
    # Name
    # --------------------------------------------------------

    draw.text(
        (40, 75),
        name,
        fill=WHITE,
        font=FONT_NAME
    )


    # --------------------------------------------------------
    # Separator
    # --------------------------------------------------------

    draw.text(
        (40, 105),
        "-----------------------------",
        fill=MUTED,
        font=FONT_NORMAL
    )


    # --------------------------------------------------------
    # Role
    # --------------------------------------------------------

    draw.text(
        (40, 140),
        "Role",
        fill=BLUE,
        font=FONT_NORMAL
    )

    draw.text(
        (180, 140),
        "AI / Product Analyst",
        fill=WHITE,
        font=FONT_NORMAL
    )


    # --------------------------------------------------------
    # Education
    # --------------------------------------------------------

    draw.text(
        (40, 170),
        "Education",
        fill=BLUE,
        font=FONT_NORMAL
    )

    draw.text(
        (180, 170),
        "BITS Pilani",
        fill=WHITE,
        font=FONT_NORMAL
    )


    # --------------------------------------------------------
    # Stack
    # --------------------------------------------------------

    draw.text(
        (40, 200),
        "Stack",
        fill=BLUE,
        font=FONT_NORMAL
    )

    draw.text(
        (180, 200),
        "Python | FastAPI | AI",
        fill=WHITE,
        font=FONT_NORMAL
    )


    # --------------------------------------------------------
    # Separator
    # --------------------------------------------------------

    draw.line(
        (40, 235, 860, 235),
        fill=BORDER,
        width=1
    )


    # --------------------------------------------------------
    # GitHub
    # --------------------------------------------------------

    draw.text(
        (40, 270),
        "GitHub",
        fill=BLUE,
        font=FONT_NORMAL
    )


    # --------------------------------------------------------
    # Repositories
    # --------------------------------------------------------

    draw.text(
        (40, 305),
        "Repositories",
        fill=BLUE,
        font=FONT_SMALL
    )

    draw.text(
        (190, 305),
        str(repositories),
        fill=WHITE,
        font=FONT_SMALL
    )


    # --------------------------------------------------------
    # Followers
    # --------------------------------------------------------

    draw.text(
        (40, 330),
        "Followers",
        fill=BLUE,
        font=FONT_SMALL
    )

    draw.text(
        (190, 330),
        str(followers),
        fill=WHITE,
        font=FONT_SMALL
    )


    # --------------------------------------------------------
    # Following
    # --------------------------------------------------------

    draw.text(
        (40, 355),
        "Following",
        fill=BLUE,
        font=FONT_SMALL
    )

    draw.text(
        (190, 355),
        str(following),
        fill=WHITE,
        font=FONT_SMALL
    )


    # --------------------------------------------------------
    # Contributions
    # --------------------------------------------------------

    draw.text(
        (400, 270),
        "Contributions",
        fill=BLUE,
        font=FONT_NORMAL
    )

    draw.text(
        (400, 305),
        f"{total_contributions} contributions",
        fill=WHITE,
        font=FONT_SMALL
    )


    # --------------------------------------------------------
    # Animated heatmap
    # --------------------------------------------------------

    for cell in cells[:revealed_cells]:

        draw.rounded_rectangle(
            (
                cell["x"],
                cell["y"],
                cell["x"] + CELL_SIZE,
                cell["y"] + CELL_SIZE
            ),
            radius=2,
            fill=cell["color"]
        )


    # --------------------------------------------------------
    # Footer
    # --------------------------------------------------------

    draw.text(
        (40, 610),
        f"github.com/{username}",
        fill=MUTED,
        font=FONT_FOOTER
    )


    # --------------------------------------------------------
    # Online
    # --------------------------------------------------------

    draw.ellipse(
        (685, 606, 693, 614),
        fill=BLUE
    )

    draw.text(
        (705, 605),
        "online",
        fill=BLUE,
        font=FONT_FOOTER
    )


    return image


# ============================================================
# Create frames
# ============================================================

frames = []

total_cells = len(cells)

print(
    f"Total heatmap cells: {total_cells}"
)


# ------------------------------------------------------------
# Empty starting frame
# ------------------------------------------------------------

frames.append(
    create_dashboard(0)
)


# ------------------------------------------------------------
# Reveal cells gradually
# ------------------------------------------------------------

for revealed in range(
    CELLS_PER_FRAME,
    total_cells + CELLS_PER_FRAME,
    CELLS_PER_FRAME
):

    revealed = min(
        revealed,
        total_cells
    )

    frame = create_dashboard(
        revealed
    )

    frames.append(frame)

    print(
        f"Generated frame "
        f"{len(frames)}: "
        f"{revealed}/{total_cells} cells"
    )


# ============================================================
# Save GIF
# ============================================================

OUTPUT_FILE.parent.mkdir(
    parents=True,
    exist_ok=True
)


# Make final frame stay longer
durations = [
    FRAME_DURATION
] * len(frames)

durations[-1] = FINAL_FRAME_DURATION


frames[0].save(
    OUTPUT_FILE,
    save_all=True,
    append_images=frames[1:],
    duration=durations,
    loop=0,
    disposal=2
)


# ============================================================
# Done
# ============================================================

print()
print("Dashboard GIF created!")
print(f"Frames: {len(frames)}")
print(f"Cells: {total_cells}")
print(f"Output: {OUTPUT_FILE}")