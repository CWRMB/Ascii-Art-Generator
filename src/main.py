from src.ascii.ascii_operations import image_to_ascii, ascii_to_image
from src import *


INPUT_FILE_NAME = "testing_image_1.jpg"
OUTPUT_FILE_NAME = "testing_ascii_1.jpg"
FONT_NAME = "UbuntuMono-Regular.ttf"

if __name__ == '__main__':
    ascii_output = image_to_ascii(input_dir / INPUT_FILE_NAME)
    # if write_to_file(ascii_output, output_dir / OUTPUT_FILE_NAME):
    #     print("Writing done")
    ascii_to_image(ascii_output, output_dir / OUTPUT_FILE_NAME, font_path=font_path / FONT_NAME)
