#!/usr/bin/env python

"""
Solution for exercise 1 in chapter_1_0.ipynb

Usage:
$ python ex_1_1.py
"""

import logging
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from rich.logging import RichHandler

# Configure rich logging
logger = logging.getLogger(__name__)


def setup_logger() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler()],
    )


def main() -> plt.Figure:
    setup_logger()

    figure, ax = plt.subplots(figsize=(6, 2), dpi=100)

    custom_font_path = Path("./fonts/cmr10.ttf")
    if custom_font_path.exists():
        custom_font = FontProperties(fname=custom_font_path)
        plt.rcParams.update(
            {
                "font.family": custom_font.get_name(),
                "font.size": 16,
                "axes.formatter.use_mathtext": True,
            }
        )
    else:
        logger.warning("Custom font not found, using default font settings.")

    ax.set_xlabel("This is the default font")
    ax.text(
        x=0.5,
        y=0.5,
        s="The quick brown fox jumps over the lazy dog",
        ha="center",
        va="center",
    )
    ax.tick_params(axis="both", which="major", labelsize=16)
    ax.set_title("Matplotlib primer")
    ax.set_xlabel("X-axis", fontsize=16)
    ax.set_ylabel("Y-axis", fontsize=16)
    ax.set_xticks([0, 0.5, 1])
    ax.set_yticks([0, 0.5, 1])
    logger.info("Figure created successfully.")
    return figure


if __name__ == "__main__":
    fig = main()
    fig.tight_layout()
    save_dir = Path("results")
    save_dir.mkdir(parents=True, exist_ok=True)
    save_path = save_dir / "pangram_cmr10.svg"
    fig.savefig(save_path)
    logger.info(f"Figure saved to {save_path}.")
    plt.show()
