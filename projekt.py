import os
import numpy as np
from PIL import Image
import gui

def upscale(img, scale):
    original_size = img.size  # (width, height)
    new_size = (original_size[0] * scale, original_size[1] * scale)
    img_upscaled = img.resize(new_size, Image.NEAREST)
    return img_upscaled

# generated using 4x4 bitmap as base
# TODO: random colors, add algorithm to get different patterns

grayscale = False

# generate image using 2 rotations
grid = np.random.rand(4, 4)

if not (grayscale):
    np.around(grid, 0, grid)

grid_flipped = np.flip(grid, 1) # flip horizontal
grid_8x4 = np.concatenate((grid, grid_flipped), axis=1)
grid_8x4_flipped = np.flip(grid_8x4, 0) # flip vertical
grid_8x8 = np.concatenate((grid_8x4, grid_8x4_flipped), axis=0)

# convert grid to 8bit image grayscaled
grid_8bit = (grid_8x8 * 255).astype(np.uint8)
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

img = upscale(img, 50)
img.save(os.path.join(base_dir, 'grid.png'))
#img.show()

# Convert to RGB image
img_colored = Image.fromarray(grid_colored, mode='RGB')
img_colored = upscale(img_colored, 50)
img_colored.save(os.path.join(base_dir, 'grid_colored.png'))
img_colored.show()