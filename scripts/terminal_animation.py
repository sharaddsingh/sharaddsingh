from PIL import Image, ImageDraw, ImageFont

# =========================
# Canvas
# =========================

WIDTH = 700
HEIGHT = 300

BACKGROUND = "#0d1117"
BORDER = "#30363d"
BLUE = "#58a6ff"
WHITE = "#ffffff"
GRAY = "#8b949e"

# =========================
# Fonts
# =========================

font_large = ImageFont.truetype(
    "C:/Windows/Fonts/consola.ttf",
    20
)

font_name = ImageFont.truetype(
    "C:/Windows/Fonts/consola.ttf",
    18
)

font_small = ImageFont.truetype(
    "C:/Windows/Fonts/consola.ttf",
    15
)


# =========================
# Helper function
# =========================

def create_canvas():
    image = Image.new(
        "RGB",
        (WIDTH, HEIGHT),
        BACKGROUND
    )

    draw = ImageDraw.Draw(image)

    # Terminal border
    draw.rounded_rectangle(
        (0, 0, WIDTH - 1, HEIGHT - 1),
        radius=12,
        outline=BORDER
    )

    return image, draw


# =========================
# FRAME 1
# =========================

image, draw = create_canvas()

draw.text(
    (30, 25),
    "$ neofetch",
    fill=BLUE,
    font=font_large
)

image.save("assets/frame1.png")

print("Frame 1 created!")


# =========================
# FRAME 2
# =========================

draw.text(
    (30, 75),
    "Sharad Pratap Singh",
    fill=WHITE,
    font=font_name
)

image.save("assets/frame2.png")

print("Frame 2 created!")


# =========================
# FRAME 3
# =========================

draw.text(
    (30, 110),
    "-----------------------------",
    fill=GRAY,
    font=font_small
)

image.save("assets/frame3.png")

print("Frame 3 created!")


# =========================
# FRAME 4
# =========================

draw.text(
    (30, 145),
    "Role",
    fill=BLUE,
    font=font_small
)

draw.text(
    (150, 145),
    "AI / Product Analyst",
    fill=WHITE,
    font=font_small
)

image.save("assets/frame4.png")

print("Frame 4 created!")


# =========================
# FRAME 5
# =========================

draw.text(
    (30, 175),
    "Education",
    fill=BLUE,
    font=font_small
)

draw.text(
    (150, 175),
    "BITS Pilani",
    fill=WHITE,
    font=font_small
)

image.save("assets/frame5.png")

print("Frame 5 created!")


# =========================
# FRAME 6
# =========================

draw.text(
    (30, 205),
    "Stack",
    fill=BLUE,
    font=font_small
)

draw.text(
    (150, 205),
    "Python | FastAPI | AI",
    fill=WHITE,
    font=font_small
)

image.save("assets/frame6.png")

print("Frame 6 created!")


# =========================
# FRAME 7
# =========================

draw.text(
    (30, 235),
    "Status",
    fill=BLUE,
    font=font_small
)

draw.text(
    (150, 235),
    "Building cool things...",
    fill=WHITE,
    font=font_small
)

image.save("assets/frame7.png")

print("Frame 7 created!")

print("\nAll 7 frames created successfully!")