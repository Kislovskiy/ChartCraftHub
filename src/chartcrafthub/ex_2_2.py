#!/usr/bin/env python

"""
Solution for exercise 2 in chapter_2_1.ipynb

Usage:
$ python ex_2_2.py
"""

import logging

from abstractions import Plot, Point, Vector
from ex_1_1 import setup_logger

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
    grid_vectors = [
        Vector(start, end)
        for start, end in zip(grid_points, grid_points[1:] + [grid_points[0]])
    ]

    point_style = {"marker": "o", "color": "black"}
    vector_style = {
        "head_width": 0.2,
        "head_length": 0.2,
        "fc": "blue",
        "ec": "blue",
        "length_includes_head": "True",
    }

    # the plotting happens here
    figure, ax = (
        Plot()
        .add(grid_points, point_style)
        .add(grid_vectors, vector_style)
        .get_figure()
    )
    return figure


if __name__ == "__main__":
    setup_logger()
    fig = main()
    save_path = "results/dino_ex_2_2.png"
    fig.savefig(save_path, dpi=600)
    logger.info(f"Figure saved successfully to {save_path}.")
