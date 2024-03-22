#!/usr/bin/env python

"""
Solution for exercise 3 in chapter_2_1.ipynb

Usage:
$ python ex_2_3.py
"""

import logging

import numpy as np
from abstractions import Plot, Point
from ex_1_1 import setup_logger
from matplotlib import pyplot as plt

logger = logging.getLogger(__name__)
setup_logger()


def main():
    x = np.linspace(-2 * np.pi, +2 * np.pi, 500)
    y = np.sin(x) + 0.4 * np.cos(3 + 5 * x)

    figure, ax = Plot().add([Point(x, y) for x, y in zip(x, y)]).get_figure()

    cmap = plt.cm.viridis
    ax.get_children()
    colors = np.linspace(0, 1, len(x))
    for i, child in enumerate(ax.get_children()):
        # Check if the child is an instance of matplotlib.lines.Line2D
        if isinstance(child, plt.Line2D):
            # Set the color of the line using the colormap
            child.set_color(cmap(colors[i]))
    return figure


if __name__ == "__main__":
    fig = main()
    save_path = "results/ex_2_3.svg"
    fig.savefig(save_path)
    logger.info(f"Saved plot to {save_path}")
