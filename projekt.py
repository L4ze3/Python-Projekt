import os
import numpy as np
from PIL import Image
import gui

def upscale(img, scale):
    scale = 50 
    original_size = img.size  # (width, height)
    new_size = (original_size[0] * scale, original_size[1] * scale)
    img_upscaled = img.resize(new_size, Image.NEAREST)
    return img_upscaled

# generated using 4x4 bitmap as base
grid = np.random.rand(4, 4)
np.around(grid, 0, grid)
grid_flipped = np.flip(grid, 1)
grid_8x4 = np.concatenate((grid, grid_flipped), axis=1)
grid_8x4_flipped = np.flip(grid_8x4, 0)
grid_8x8 = np.concatenate((grid_8x4, grid_8x4_flipped), axis=0)
print(grid_8x8)

print()

# convert grid to 8bit image greyscaled
grid_8bit = (grid_8x8 * 255).astype(np.uint8)
img = Image.fromarray(grid_8bit, 'L')


color = gui.color_picker()
print(color)

# Stack grayscale data into 3 channels to make it RGB
grid_rgb = np.stack([grid_8bit]*3, axis=-1)  # shape: (4, 8, 3)

grid_colored = np.stack([
    (grid_8bit * color[0][0] / 255).astype(np.uint8),
    (grid_8bit * color[0][1] / 255).astype(np.uint8),
    (grid_8bit * color[0][2] / 255).astype(np.uint8)
], axis=-1)


#grid_colored = np.stack([np.zeros_like(grid_8bit),  # Red channel
#                         np.zeros_like(grid_8bit),  # Green channel
#                         grid_8bit], axis=-1)       # Blue channel

[np.zeros_like(grid_8bit), np.zeros_like(grid_8bit), grid_8bit]

print(grid_colored)

img = upscale(img, 50)
img.save('grid.png')
img.show()

# Convert to RGB image
img_colored = Image.fromarray(grid_colored, mode='RGB')
img_colored = upscale(img_colored, 50)
img_colored.save("grid_colored_blue.png")
img_colored.show()