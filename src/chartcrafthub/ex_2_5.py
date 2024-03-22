#!/usr/bin/env python

"""
Solution for exercise 5 in chapter_2_1.ipynb

Usage:
$ python ex_2_5.py
"""

import logging

import matplotlib.pyplot as plt
import numpy as np
from ex_1_1 import setup_logger

logger = logging.getLogger(__name__)
setup_logger()


def main():
    x = np.linspace(-5, 5, 100)
    y = np.sin(x)
    fixed_height = 1.0

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    ax.plot(x, y, zs=fixed_height, zdir="z", label="2D Plot in 3D")

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("2D Plot in 3D with Fixed Height")
    return fig


if __name__ == "__main__":
    fig = main()
    save_path = "results/ex_2_5.png"
    fig.tight_layout()
    fig.savefig(save_path, dpi=600)
    logger.info(f"Saved plot to {save_path}")
