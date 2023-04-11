from PIL import Image, ImageDraw, ImageFont
import argparse
import sys

def print_help():
    print("Usage: python ascii_to_image.py <ascii_file> <output_file> [OPTIONS]")
    print("\nConvert ASCII art to image.\n")
    print("Required arguments:")
    print("  ascii_file         Path to the input ASCII art file")
    print("  output_file        Path to the output PNG file to be created")
    print("\nOptions:")
    print("  -f, --font-size    Font size of the text (default: 14)")
    print("  -t, --font-type    Font type of the text (default: LiberationMono-Regular.ttf)")
    print("  -c, --text-color   Text color in RGB format (default: 255 255 255)")
    print("  -b, --bg-color     Background color in RGB format (default: 0 0 0)")
    print("  -h, --help         Show this help message and exit\n")
    print("Example:")
    print("  python ascii_to_image.py my_ascii_art.txt my_image.png -f 20 -t Arial.ttf -c 255 0 0 -b 255 255 255")
    print("")

if len(sys.argv) < 2:
    print_help()
    #sys.exit()

def create_image(ascii_file, output_file, font_size=14, font_type="/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf",
                 text_color=(255, 255, 255), bg_color=(0, 0, 0)):
    # Set up image and font parameters
    char_width = 10
    char_height = 18
    font = ImageFont.truetype(font_type, size=font_size)

    # Open ASCII art file and read contents
    with open(ascii_file, 'r') as f:
        ascii_text = f.read()

    # Calculate image size based on ASCII art dimensions
    num_chars_wide = max([len(line) for line in ascii_text.split('\n')])
    num_chars_high = ascii_text.count('\n') + 1
    image_width = num_chars_wide * char_width
    image_height = num_chars_high * char_height

    # Create new image with specified background color
    image = Image.new('RGB', (image_width, image_height), bg_color)

    # Draw text onto image with specified text color and font
    draw = ImageDraw.Draw(image)
    x, y = 0, 0
    for char in ascii_text:
        if char == '\n':
            x = 0
            y += char_height
        else:
            draw.text((x, y), char, font=font, fill=text_color)
            x += char_width

    # Save image as PNG
    image.save(output_file)

# Parse command line arguments
parser = argparse.ArgumentParser(description="Convert ASCII art to PNG image.")
parser.add_argument("ascii_file", help="input ASCII art file")
parser.add_argument("output_file", help="output PNG file")
parser.add_argument("-f", "--font-size", help="font size", type=int, default=14)
parser.add_argument("-t", "--font-type", help="font type", default="/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf")
parser.add_argument("-c", "--text-color", help="text color as RGB tuple, e.g. '(255, 255, 255)'", type=lambda x: tuple(map(int, x.strip('()').split(','))), default=(255, 255, 255))
parser.add_argument("-b", "--bg-color", help="background color as RGB tuple, e.g. '(0, 0, 0)'", type=lambda x: tuple(map(int, x.strip('()').split(','))), default=(0, 0, 0))
args = parser.parse_args()


# Create image with specified options
create_image(args.ascii_file, args.output_file, args.font_size, args.font_type, args.text_color, args.bg_color)
