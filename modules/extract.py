# Install PIL:
# py -m pip install Pillow

from PIL import Image
import csv

def extract(name):
    image_path = name + '.jpg'
    output_path = name + '.csv'

    rgb_values = get_rgb_values(image_path)
    save_csv(rgb_values, output_path)    

def get_rgb_values(image_path):
    image = Image.open(image_path)
    pixels = image.load()
    width, height = image.size

    rgb_values = []

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            rgb_values.append([x, y, r, g, b])

    return rgb_values

def save_csv(rgb_values, output_path):
    with open(output_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['X', 'Y', 'R', 'G', 'B'])
        for row in rgb_values:
            writer.writerow(row)
