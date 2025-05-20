import os
import numpy as np
from PIL import Image

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

# generated using 4x8 bitmap as base
grid2 = np.random.rand(4, 8)
np.around(grid2, 0, grid2)
grid2_flipped = np.flip(grid2, 1)
grid2_8x8 = np.concatenate((grid2, grid2_flipped), axis=0)

print(grid2_8x8)



# convert grid to 8bit image greyscaled
grid_8bit = (grid_8x8 * 255).astype(np.uint8)
img = Image.fromarray(grid_8bit, 'L')

grid2_8bit = (grid2_8x8 * 255).astype(np.uint8)
img2 = Image.fromarray(grid2_8bit, 'L')



img = upscale(img, 50)
img.save('grid.png')
img.show()

#img2 = upscael(img2, 50)
#img2.save('grid2.png')
#img2.show()

# Stack grayscale data into 3 channels to make it RGB
grid_rgb = np.stack([grid_8bit]*3, axis=-1)  # shape: (4, 8, 3)

# Create RGB image
img_rgb = Image.fromarray(grid_rgb, mode='RGB')
img_rgb = upscale(img_rgb, 50)
img_rgb.save('grid_rgb.png')
img_rgb.show()

grid_colored = np.stack([np.zeros_like(grid_8bit),  # Red channel
                         np.zeros_like(grid_8bit),  # Green channel
                         grid_8bit], axis=-1)       # Blue channel

# Convert to RGB image
img_colored = Image.fromarray(grid_colored, mode='RGB')
img_colored = img_colored.resize((grid_colored.shape[1] * 50, grid_colored.shape[0] * 50), Image.NEAREST)
img_colored.save("grid_colored_blue.png")
img_colored.show()