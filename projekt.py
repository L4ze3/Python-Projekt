import os
import numpy as np
from PIL import Image
import gui

# TODO: random colors, custom randomness, gui flag, cli interface, convert to ascii

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
    bottom_half = np.flip(right_half, axis=0)
    grid = np.concatenate((top_half, bottom_half), axis=0)
    return grid

def alien():
    right_half = np.random.rand(8, 4)
    right_half[3, 2] = 0
    left_half = np.flip(right_half, axis=1)
    grid = np.concatenate((right_half, left_half), axis=1)
    return grid

grayscale = False
grid = alien()

if not (grayscale):
    np.around(grid, 0, grid)

# convert grid to 8bit image grayscaled
grid_8bit = (grid * 255).astype(np.uint8)
img = Image.fromarray(grid_8bit, 'L')

color = gui.color_picker()
print(color)

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
