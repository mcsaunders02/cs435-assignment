import os
import re
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw

# Gets all ints from a string
def ints(string: str) -> list[int]:
    return [int(i) for i in re.findall('\\d+', string)]

# Path to the directory
DIRECTORY_PATH = "./Programming-Assignment-Data/Programming-Assignment-Data"
OUTPUT_PATH = "./Output"

# Width of the highlighted rectangle's sides
HIGHLIGHT_WIDTH = 10
HIGHLIGHT_HALF_WIDTH = HIGHLIGHT_WIDTH / 2

# Highlight color
HIGHLIGHT_COLOR = (255, 255, 0)

# Create output directory if it doesn't exist
if not os.path.exists(OUTPUT_PATH):
    os.mkdir(OUTPUT_PATH)

# Get the list of file names, not including the extensions
# Set is easier for avoiding duplicates, then it can be turned back into a list
file_names_set: set[str] = set()

for file_name in os.listdir(DIRECTORY_PATH):
    # The file extension is always 3 characters long
    file_names_set.add(file_name[:-4])
    
file_names = list(file_names_set)

# For each file name, get the nodes with no children and highlight them, then save the resulting .PNG in a new file
for file_name in file_names:
    png_file_path = f"{DIRECTORY_PATH}/{file_name}.png"
    xml_file_path = f"{DIRECTORY_PATH}/{file_name}.xml"
    
    # Open the image for editing
    image = Image.open(png_file_path)
    draw = ImageDraw.Draw(image)
    
    # Let's get an idea of what the XML file is like
    xml_file = open(xml_file_path, "r")
    xml_contents = xml_file.read()
    
    # Parse the XML into a usable object
    parsed_xml = ET.fromstring(xml_contents)
    
    for item in parsed_xml.iter():
        # Find which nodes have no child nodes
        if item.find("node") is None:
            # Find the bounds of the node
            bounds = item.attrib["bounds"]
            
            # Parse the values
            x1, y1, x2, y2 = ints(bounds)
            
            # Draw rectangles based on the bounds
            # Left side
            draw.rectangle((x1 - HIGHLIGHT_HALF_WIDTH, y1 - HIGHLIGHT_HALF_WIDTH, x1 + HIGHLIGHT_HALF_WIDTH, y2 + HIGHLIGHT_HALF_WIDTH), fill = HIGHLIGHT_COLOR)
            
            # Right side
            draw.rectangle((x2 - HIGHLIGHT_HALF_WIDTH, y1 - HIGHLIGHT_HALF_WIDTH, x2 + HIGHLIGHT_HALF_WIDTH, y2 + HIGHLIGHT_HALF_WIDTH), fill = HIGHLIGHT_COLOR)
            
            # Top side
            draw.rectangle((x1 - HIGHLIGHT_HALF_WIDTH, y1 - HIGHLIGHT_HALF_WIDTH, x2 + HIGHLIGHT_HALF_WIDTH, y1 + HIGHLIGHT_HALF_WIDTH), fill = HIGHLIGHT_COLOR)
            
            # Bottom side
            draw.rectangle((x1 - HIGHLIGHT_HALF_WIDTH, y2 - HIGHLIGHT_HALF_WIDTH, x2 + HIGHLIGHT_HALF_WIDTH, y2 + HIGHLIGHT_HALF_WIDTH), fill = HIGHLIGHT_COLOR)
    
    # Save image to new file
    image.save(f"output/{file_name}.png")
            
    # Close opened files
    xml_file.close()
    image.close()