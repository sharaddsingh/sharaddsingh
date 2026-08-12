from PIL import Image
from pathlib import Path

# Folder containing frames
frames_dir = Path("assets")

# Load all frames in order
frames = []

for i in range(1, 8):
    frame_path = frames_dir / f"frame{i}.png"
    frame = Image.open(frame_path).convert("RGB")
    frames.append(frame)

# Create animated GIF
frames[0].save(
    "assets/terminal-animation.gif",
    save_all=True,
    append_images=frames[1:],
    duration=700,
    loop=0
)

print("Terminal animation created!")