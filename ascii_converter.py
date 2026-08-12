from PIL import Image, ImageOps

# Open the image
image = Image.open("assets/input.jpg")

print("Original size:", image.size)

# Crop around the subject
image = image.crop((180, 250, 500, 680))
print("Cropped size:", image.size)

# Convert to grayscale
image = image.convert("L")

# Improve contrast
image = ImageOps.autocontrast(image)

# Target width
new_width = 70

# Correct for terminal character proportions
width, height = image.size
new_height = int(height * new_width / width * 0.5)

# Resize
image = image.resize((new_width, new_height))


print("ASCII size:", image.size)

# Characters ordered from dark to light
ascii_chars = "@%#*+=-:. "

# Convert pixels into ASCII
pixels = image.load()

for y in range(image.height):
    row = ""

    for x in range(image.width):
        brightness = pixels[x, y]

        # Convert 0-255 brightness to character index
        index = brightness * (len(ascii_chars) - 1) // 255

        row += ascii_chars[index]

    print(row)

print("ASCII conversion complete")