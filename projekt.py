import os
import argparse
import numpy as np
from PIL import Image
import gui
#import cli
#from pattern import *

# TODO: random colors, custom randomness, convert to ascii, read file + change colors, loop generation

def upscale(img, scale):
    original_size = img.size  # (width, height)
    new_size = (original_size[0] * scale, original_size[1] * scale)
    img_upscaled = img.resize(new_size, Image.NEAREST)
    return img_upscaled

def radial():
    quad = np.random.rand(4, 4)
    top_half = np.concatenate((quad, np.flip(quad, axis=1)), axis=1)
    bottom_half = np.flip(top_half, axis=0)
    grid = np.concatenate((top_half, bottom_half), axis=0)
    return grid

def vertical():
    right_half = np.random.rand(8, 4)
    left_half = np.flip(right_half, axis=1)
    grid = np.concatenate((right_half, left_half), axis=1)
    return grid

def horizontal():
    top_half = np.random.rand(4, 8)
    bottom_half = np.flip(top_half, axis=0)
    grid = np.concatenate((top_half, bottom_half), axis=0)
    return grid

# WTF
def alien():
    right_half = np.random.rand(8, 4)
    right_half[3, 2] = 0
    left_half = np.flip(right_half, axis=1)
    grid = np.concatenate((right_half, left_half), axis=1)
    return grid

parser = argparse.ArgumentParser(
        prog='Projekt',
        description='Generate symmetrical 8-Bit Images',
        )

parser.add_argument('-g', '--grayscale', action='store_true')
parser.add_argument('-i', '--invert', action='store_true')
parser.add_argument('-p', '--pattern', help='{(h)orizontal, (v)ertical, (r)adial, (a)lien}')
parser.add_argument('-c', '--color', default="ffffff")
parser.add_argument('--gui', action='store_true')
args = parser.parse_args()

grayscale = args.grayscale
invert = args.invert
pattern = args.pattern
color = tuple(int(args.color[i:i+2], 16) for i in (0, 2, 4)) # convert hex to rgb

if not grayscale:
    option = 'g'
if invert:
    option = 'i'

if args.gui:
    app = gui.GUI()
    app.mainloop()
    values = app.get_values()
    pattern = values[0]
    option = values[1]
    color = values[2]

match pattern:
    case 'h' | 'horizontal':
        grid = horizontal()
    case 'v' | 'vertical':
        grid = vertical()
    case 'r' | 'radial':
        grid = radial()
    case 'a' | 'alien':
        grid = alien()
    case _:
        grid = np.random.rand(8, 8)

if option != 'g':
    np.around(grid, 0, grid)

if option == 'i':
    grid = grid.astype(int)
    grid = grid ^ 1

# convert grid to 8bit image grayscaled
grid_8bit = (grid * 255).astype(np.uint8)
img = Image.fromarray(grid_8bit, 'L')

# colored bits
# divide by 255 to get the bit to 1 and multiply by the color rgb code
grid_colored = np.stack([
    ((grid_8bit/255) * color[0]).astype(np.uint8),
    ((grid_8bit/255) * color[1]).astype(np.uint8),
    ((grid_8bit/255) * color[2]).astype(np.uint8)
], axis=-1)

base_dir = os.path.dirname(os.path.abspath(__file__))

# Convert to RGB image
img_colored = Image.fromarray(grid_colored, mode='RGB')
img_colored = upscale(img_colored, 50)
img_colored.save(os.path.join(base_dir, 'grid_colored.png'))
img_colored.show()

