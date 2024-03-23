#!/usr/bin/env python

"""
Solution for exercise 6 in chapter_2_1.ipynb

Usage:
$ python ex_2_6.py
"""

import logging

import matplotlib.pyplot as plt
import numpy as np
from abstractions import Point
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from chartcrafthub.utils import setup_logger

logger = logging.getLogger(__name__)


def main():
    dino_vectors = (
        (6, 4),
        (3, 1),
        (1, 2),
        (-1, 5),
        (-2, 5),
        (-3, 4),
        (-4, 4),
        (-5, 3),
        (-5, 2),
        (-2, 2),
        (-5, 1),
        (-4, 0),
        (-2, 1),
        (-1, 0),
        (0, -3),
        (-1, -4),
        (1, -4),
        (2, -3),
        (1, -2),
        (3, -1),
        (5, 1),
    )

    grid_points = [Point(x, y) for x, y in dino_vectors]

    # Define the vertices of your 2D rectangle
    x = [point.x for point in grid_points]
    y = [point.y for point in grid_points]

    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # Create vertices for the bottom face
    verts = [list(zip(x, y, np.zeros_like(x)))]
    verts2 = [list(zip(x, y, 3 * np.ones_like(x)))]

    # print(verts)
    # Create 3D polygon from the vertices
    poly = Poly3DCollection(verts, alpha=0.5, facecolors="blue", edgecolors="black")
    poly2 = Poly3DCollection(verts2, alpha=0.5, facecolors="blue", edgecolors="black")

    ax.add_collection3d(poly)
    ax.add_collection3d(poly2)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("2D Rectangle Transformed to 3D and Filled")

    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])
    ax.set_zlim([-5, 5])
    return fig


if __name__ == "__main__":
    setup_logger()
    fig = main()
    save_path = "results/ex_2_6.png"
    fig.tight_layout()
    fig.savefig(save_path, dpi=600)
    logger.info(f"Saved plot to {save_path}")
