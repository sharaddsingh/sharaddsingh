from PIL import Image, ImageDraw, ImageFont

# Canvas
WIDTH = 700
HEIGHT = 300

# GitHub dark background
image = Image.new("RGB", (WIDTH, HEIGHT), "#0d1117")

# Drawing tool
draw = ImageDraw.Draw(image)

# Terminal border
draw.rounded_rectangle(
    (0, 0, WIDTH - 1, HEIGHT - 1),
    radius=12,
    outline="#30363d"
)

# Font
font = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 20)

# First terminal line
draw.text(
    (30, 25),
    "$ neofetch",
    fill="#58a6ff",
    font=font
)

# Save first frame
image.save("assets/frame1.png")

print("Frame 1 created!")