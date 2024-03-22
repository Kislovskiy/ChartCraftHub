#!/usr/bin/env python

"""
Solution for exercise 1 in chapter_2_1.ipynb

Usage:
$ python ex_2_1.py
"""

import logging

from abstractions import Point
from ex_1_1 import setup_logger

logger = logging.getLogger(__name__)
setup_logger()


class Vector:
    def __init__(self, origin: Point, tip: Point):
        self.start = origin
        self.end = tip

    def __str__(self):
        return f"Vector({self.start}, {self.end})"

    def plot(self, ax, kwargs):
        ax.arrow(
            self.start.x,
            self.start.y,
            self.end.x - self.start.x,
            self.end.y - self.start.y,
            **kwargs,
        )

    def add(self, other_vector):
        new_start = Point(
            self.start.x + other_vector.start.x, self.start.y + other_vector.start.y
        )
        new_end = Point(
            self.end.x + other_vector.end.x, self.end.y + other_vector.end.y
        )
        return Vector(new_start, new_end)


if __name__ == "__main__":
    start = Point(0, 0)
    end = Point(1, 1)
    vector = Vector(start, end)
    logger.info(f"Vector: {vector}")
