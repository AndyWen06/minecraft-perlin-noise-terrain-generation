import random
import math
import numpy as np

# changes width of output window (visual feature)
import sys

np.set_printoptions(threshold=sys.maxsize)

# generate gradient vectors at vertices of grid
def generate_gradient(width, length):
    gradient = [
        [(math.cos(math.pi * (random.random() * 2)), math.sin(math.pi * (random.random() * 2))) for _ in range(width)]
        for _ in range(length)
    ]
    return gradient


# calculation of dot product
def dot_product(gradient, pos_x, pos_y, grid_x, grid_y):
    gradient_vector = gradient[grid_y][grid_x]
    return pos_x * gradient_vector[0] + pos_y * gradient_vector[1]


# deduced formula for linear interpolation
def interpolate(t, a, b):
    return a + t * (b - a)


# Ken Perlin's Fade Function
def fade(t):
    return 6 * t ** 5 - 15 * t ** 4 + 10 * t ** 3


# this function generates a Perlin Noise field given the dimensions
def perlin_noise(width, length, grid_size):
    grid_width = int(width / grid_size + 1)
    grid_length = int(length / grid_size + 1)

    gradient = generate_gradient(grid_width, grid_length)
    noise_grid = []

    for y in range(length):
        row = []
        for x in range(width):
            grid_x = x // grid_size
            grid_y = y // grid_size
            pos_x = ((x % grid_size) + 1) / (grid_size + 1)
            pos_y = (((grid_size - 1) - (y % grid_size)) + 1) / (grid_size + 1)

            tl = (dot_product(gradient, pos_x, pos_y - 1, grid_x, grid_y) + 1) / 2
            tr = (dot_product(gradient, pos_x - 1, pos_y - 1, grid_x + 1, grid_y) + 1) / 2
            bl = (dot_product(gradient, pos_x, pos_y, grid_x, grid_y + 1) + 1) / 2
            br = (dot_product(gradient, pos_x - 1, pos_y, grid_x + 1, grid_y + 1) + 1) / 2

            top = interpolate(pos_x, tl, tr)
            bottom = interpolate(pos_x, bl, br)

            value = fade(interpolate(pos_y, bottom, top))

            block_height = int(round(value * grid_size, 0))

            row.append(block_height)

        noise_grid.append(row)

    return noise_grid


# this is the final function that we run, it has the other functions embedded in it
def main():
    # here we define the parameters of our noise field
    width = 32
    length = 32
    grid_size = 8
    # add a parameter for how many octaves we want
    octave = 3
    # then we create an empty noise field
    final_grid = []
    for z in range(length):
        final_row = []
        for x in range(width):
            final_row.append(0)
        final_grid.append(final_row)

    # we now create our octaves, and add it to the noise field above every time
    for o in range(octave):
        print(o)
        perlin_noise_grid = perlin_noise(width, length, int(grid_size / (2 ** o)))
        for z in range(length):
            for x in range(width):
                final_grid[x][z] += perlin_noise_grid[x][z]

    # finally, we print the noise field
    print("Perlin Noise Grid:")
    for final_row in final_grid:
        print(final_row)


# this is where we run the main function
main()
