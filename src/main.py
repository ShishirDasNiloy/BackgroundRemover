from rembg import remove
from PIL import Image

input_image_path = "../input_image/input.jpg"
output_image_path = "../output_image/removedbg.png"


def removebg():
    input = Image.open(input_image_path)
    output = remove(input)
    output.save(output_image_path)


if __name__ == "__main__":
    removebg()
