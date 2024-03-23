"""
Solution for exercise 2 in chapter_1_0.ipynb

Usage:
$ python ex_1_2.py
"""

import logging
from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt

from chartcrafthub.utils import setup_logger

logger = logging.getLogger(__name__)


def y(x):
    return x + np.sin(x * x * 8) / 4


def main():
    setup_logger()
    figure, ax = plt.subplots(figsize=(6, 4))

    ax.set_title("Title", loc="left", fontweight="bold", fontsize=18, pad=20)

    ax.set_ylabel(
        "y-label", fontsize=12, labelpad=10, rotation=0, loc="top", fontstyle="italic"
    )
    ax.set_xlabel("x-label", fontsize=12, labelpad=10, loc="right", fontstyle="italic")

    x = np.linspace(0, 1, 100)
    ax.plot(x, y(x), linewidth=4, color="black", label="label 1")
    ax.plot(x, x, linewidth=4, color="lightsteelblue", label="label 2")

    ax.set_ylim(bottom=0)
    ax.set_xlim(left=0, right=1)

    ax.scatter(0.5, y(0.5), s=100, color="indianred", zorder=10)
    ax.annotate(
        "Data Point",
        xy=(0.5, y(0.5)),
        xytext=(0.5, y(0.5) + 0.1),
        arrowprops=dict(arrowstyle="->"),
        zorder=11,
    )

    for line in ax.lines:
        if line.get_label().startswith("label 1"):
            latest_x, latest_y = line.get_data()

    ax.text(
        latest_x[-1] + 0.02,
        latest_y[-1],
        "label 1",
        ha="left",
        va="center",
        fontsize=12,
    )

    for line in ax.lines:
        if line.get_label().startswith("label 2"):
            latest_x, latest_y = line.get_data()

    ax.text(
        latest_x[-1] + 0.02,
        latest_y[-1],
        "label 2",
        ha="left",
        va="center",
        fontsize=12,
    )

    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)

    ax.tick_params(axis="both", which="both", length=0)
    ax.set_xticks([])
    ax.set_yticks([])

    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    ax.plot(
        xmin,
        ymax,
        "^k",
        transform=ax.get_yaxis_transform(),
        clip_on=False,
        zorder=10,
        label="y_arrow",
    )
    ax.plot(
        xmax,
        ymin,
        ">k",
        transform=ax.get_xaxis_transform(),
        clip_on=False,
        zorder=10,
        label="x_arrow",
    )

    ax.text(
        x=0,
        y=-0.2,
        s="Notes/Sources/Credits:_________",
        fontsize=12,
        ha="left",
        transform=ax.transAxes,
    )

    logger.info("Figure created successfully.")
    return figure


if __name__ == "__main__":
    with plt.xkcd():
        fig = main()
        fig.tight_layout()

        results_dir = Path("results")
        results_dir.mkdir(parents=True, exist_ok=True)
        with plt.xkcd():
            fig = main()
            save_path = results_dir.joinpath("common_chart_xkcd.png")
            fig.savefig(
                f"{save_path}",
                format="png",
                bbox_inches="tight",
                pad_inches=0.5,
                dpi=600,
            )
            logger.info(f"Figure saved to {save_path}.")
