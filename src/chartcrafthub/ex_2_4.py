#!/usr/bin/env python

"""
Solution for exercise 4 in chapter_2_1.ipynb

Usage:
$ python ex_2_4.py
"""

import logging

from abstractions import Plot, Point, Vector

from chartcrafthub.utils import setup_logger

logger = logging.getLogger(__name__)


def main():
    grid_element = [
        Point(0, 0),
        Point(0, 1),
        Point(1, 1),
        Point(1, 0),
    ]

    grid = set()  # Use a set to store unique points
    for i in range(4):  # Rows
        for j in range(2):  # Columns
            translated_element = [Point(p.x + i, p.y + j) for p in grid_element]
            grid.update(translated_element)  # Update the set with translated points

    dashed_line = {
        "linestyle": ":",
        "linewidth": 1,
        "color": "gray",
        "alpha": 0.5,
    }

    figure, ax = (
        Plot()
        .add(list(grid), {"color": "lightblue", "marker": "o"})
        .add(Vector(Point(0, 0), Point(4, 0)), dashed_line)
        .add(Vector(Point(0, 0), Point(0, 2)), dashed_line)
        .add(Vector(Point(4, 0), Point(4, 2)), dashed_line)
        .add(Vector(Point(0, 2), Point(4, 2)), dashed_line)
        .add(Vector(Point(1, 0), Point(1, 2)), dashed_line)
        .add(Vector(Point(2, 0), Point(2, 2)), dashed_line)
        .add(Vector(Point(3, 0), Point(3, 2)), dashed_line)
        .add(Vector(Point(0, 1), Point(4, 1)), dashed_line)
        .add(Vector(Point(0, 0), Point(4, 0)), dashed_line)
        .add(Vector(Point(0, 0), Point(0, 2)), dashed_line)
        .add(Vector(Point(4, 0), Point(4, 2)), dashed_line)
        .add(Vector(Point(0, 2), Point(4, 2)), dashed_line)
        .add(Vector(Point(1, 0), Point(1, 2)), dashed_line)
        .add(Vector(Point(2, 0), Point(2, 2)), dashed_line)
        .add(Vector(Point(3, 0), Point(3, 2)), dashed_line)
        .add(Vector(Point(0, 1), Point(4, 1)), dashed_line)
        .get_figure()
    )

    figure.set_size_inches((3, 3))
    ax.set_aspect("equal")
    ax.set_title("Grid of Points")
    ax.set_xlim(-1, 5)
    ax.set_ylim(-1, 3)
    ax.set_xlabel("X")
    ax.set_ylabel("Y", rotation=0)
    ax.spines[["right", "top"]].set_visible(False)
    return figure


if __name__ == "__main__":
    setup_logger()
    fig = main()
    save_path = "results/ex_2_4.png"
    fig.tight_layout()
    fig.savefig(save_path, dpi=600)
    logger.info(f"Saved plot to {save_path}")
