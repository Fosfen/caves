Caves: Generate random map layouts
****

Overview
----

Caves is a tiny library providing a single function you can use to generate a random cave map as a matrix.
You can use it if you're building a 2D video game and want a closed cave area, or if you want to simulate anything
interacting with a cave-like environment.

How to use
""""

In order to use the cave modules, first install it in your project::

    pip install caves

then, in your project, you can generate a random cave map::

    import cave

    random_cave = cave.generate_cave()

By default, it will generate a 256 by 256 matrix with predefined parameters, but you can tweak those as you need !

Example of a custom cave generation::

    random_cave = cave.generate_cave(size_x=500, size_y=1000, density=0.55, iterations=15)

If you need more details about the function's parameters, please refer to its documentation.

Example of generated maps
""""

Example 1:
    .. image:: example_imgs/example_cave_1.png

Example 2:
    .. image:: example_imgs/example_cave_2.png

Note: The borders of the caves might be open, the walls aren't forced on the edges.
