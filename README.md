# minecraft-perlin-noise-terrain-generation
Originally written in 2024, I've ported this high school project of mine onto GitHub. This code uses a basic version of Perlin Noise generation to create realistic random terrain in Minecraft.

The implementation follows a simplified Perlin Noise process of: generating gradient vectors, calculating dot products, mapping values to 0--1, interpolating, applying the fade function, and converting the final values into block heights.

## Requirements

-   Python 3
-   NumPy

## Running the Code

Run the main script with:

``` bash
python perlin_noise.py
```

The default `main()` function generates a **32 × 32 Perlin Noise field** using a grid size of **8** and prints the resulting block heights.

## Octaves

The code also includes `main_with_octaves()`, which combines **3 octaves** of Perlin Noise to produce additional smaller-scale terrain variations.

To use it, change:

``` python
main()
```

to:

``` python
main_with_octaves()
```

under the `if __name__ == "__main__":` section.

## Main Functions

-   `generate_gradient()` --- generates random unit gradient vectors.
-   `dot_product()` --- calculates the dot product between gradient and
    position vectors.
-   `interpolate()` --- performs linear interpolation.
-   `fade()` --- applies Ken Perlin's fade function.
-   `perlin_noise()` --- generates the Perlin Noise field.
-   `main()` --- generates the base 32 × 32 terrain.
-   `main_with_octaves()` --- generates terrain using 3 octaves.
