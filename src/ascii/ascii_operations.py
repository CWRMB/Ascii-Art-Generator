from src import Path
from . import ascii_keys
from PIL import Image, ImageFont, ImageDraw


def image_to_ascii(image_path: Path, aspect_ratio=0.55, new_width=800) -> [str]:
    # Convert image to grey scale
    image = Image.open(image_path).convert("L")

    original_width, original_height = image.size
    new_height = int(aspect_ratio * original_height * (new_width / original_width))

    image = image.resize((new_width, new_height))

    pixel_data = list(image.getdata())

    ascii_chars = map_value_to_char(pixel_data)

    ascii_rows = [ascii_chars[i:i + new_width] for i in range(0, len(ascii_chars), new_width)]

    return [''.join(row) for row in ascii_rows]


def map_value_to_char(data: list) -> [str]:
    output = []
    for bit in data:
        output.append(min(ascii_keys, key=lambda k: abs(ascii_keys[k] - bit)))
    return output


def ascii_to_image(ascii_art: [str], output_image_path: Path, font_path: Path = None, font_size=12,
                   text_color=(255, 255, 255)):
    # Calculate image size based on ASCII art dimensions and font size
    width = (len(ascii_art[0]) * font_size) // 2
    height = len(ascii_art) * font_size
    image = Image.new("RGB", (width, height), color=(0, 0, 0))  # Create a black background

    # Load a font
    font = ImageFont.load_default() if not font_path else ImageFont.truetype(str(font_path), font_size)

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Draw the ASCII characters onto the image
    for i, line in enumerate(ascii_art):
        draw.text((0, i * font_size), line, font=font, fill=text_color)

    # Save the image
    image.save(output_image_path)


# For writing to text file
def write_to_file(formatted_ascii: [str], output_dir: Path) -> bool:
    try:
        formatted_string = '\n'.join(formatted_ascii)
        with open(output_dir, 'w') as output_file:
            output_file.write(formatted_string)
    except Exception as e:
        print(f"Writing to output exited with exception: {e}")
        return False
    return True
