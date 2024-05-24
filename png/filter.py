from PIL import Image

# Load the image
image_path = "complex_color_filtered_text.png"
image = Image.open(image_path)

# Function to apply filter
def apply_filter(image, filter_color):
    width, height = image.size
    filtered_image = Image.new("RGB", (width, height))

    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            if filter_color == "red":
                filtered_image.putpixel((x, y), (r, 0, 0))
            elif filter_color == "green":
                filtered_image.putpixel((x, y), (0, g, 0))
            elif filter_color == "blue":
                filtered_image.putpixel((x, y), (0, 0, b))

    return filtered_image


# Apply and save the filters
red_filtered = apply_filter(image, "red")
green_filtered = apply_filter(image, "green")
blue_filtered = apply_filter(image, "blue")

red_filtered.save("filtered/red_filtered_text.png")
green_filtered.save("filtered/green_filtered_text.png")
blue_filtered.save("filtered/blue_filtered_text.png")
