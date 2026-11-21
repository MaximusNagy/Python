from PIL import Image, ImageDraw, ImageFont

def create_motivational_wallpaper(width=1920, height=1080):
    # Create a new RGB image with the given dimensions
    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)

    # Define gradient colors for a sunrise effect (top: deep blue, bottom: warm sunrise color)
    top_color = (0, 70, 140)         # Deep blue
    bottom_color = (255, 200, 100)     # Warm sunrise hue

    # Create a vertical gradient background
    for y in range(height):
        # Calculate the color for each line using linear interpolation
        r = int(top_color[0] + (bottom_color[0] - top_color[0]) * y / height)
        g = int(top_color[1] + (bottom_color[1] - top_color[1]) * y / height)
        b = int(top_color[2] + (bottom_color[2] - top_color[2]) * y / height)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # Draw mountain silhouettes using polygons
    mountain_color = (20, 20, 20)  # Dark shade for mountains
    # First mountain polygon
    mountain1 = [(0, height), (int(width * 0.3), int(height * 0.5)), (int(width * 0.6), height)]
    # Second mountain polygon
    mountain2 = [(int(width * 0.4), height), (int(width * 0.7), int(height * 0.45)), (width, height)]
    draw.polygon(mountain1, fill=mountain_color)
    draw.polygon(mountain2, fill=mountain_color)

    # Add a motivational quote at the top center
    quote = "Unleash Your Potential"
    try:
        # Attempt to load a TrueType font (adjust the path as needed)
        font = ImageFont.truetype("arial.ttf", 60)
    except IOError:
        # Fallback if the specified font is not found
        font = ImageFont.load_default()

    # Use textbbox to get the bounding box of the text
    bbox = draw.textbbox((0, 0), quote, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Calculate the position to center the text at the top of the image
    text_position = ((width - text_width) // 2, int(height * 0.1))
    text_color = (255, 255, 255)  # White text for contrast
    draw.text(text_position, quote, fill=text_color, font=font)

    # Save the generated image as JPEG
    image.save("motivational_wallpaper.jpg")
    print("Wallpaper saved as 'motivational_wallpaper.jpg'.")

if __name__ == "__main__":
    create_motivational_wallpaper()
