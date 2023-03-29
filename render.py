from PIL import Image
import csv

def render(name):
    csv_path = name + '.csv'
    output_path = name + '_out.jpg'

    image = create_image_from_csv(csv_path)
    image.save(output_path)
    

def create_image_from_csv(csv_path):
    with open(csv_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader) # skip header row
        width = 0
        height = 0
        rgb_values = []
        for row in reader:
            x, y, r, g, b = map(int, row)
            if g < 150:
                g = g + 100
            rgb_values.append((r, g, b))
            if x+1 > width:
                width = x+1 
            if y+1 > height:
                height = y+1
       
        image = Image.new('RGB', (width, height))
        pixels = image.load()

        for i, rgb in enumerate(rgb_values):
            x, y = i % width, i // width
            pixels[x, y] = rgb

    return image
