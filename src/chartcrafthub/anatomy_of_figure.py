"""
This script generates an image of the anatomy of a figure in Matplotlib.

Original Script Information:
Title: Scientific Visualization - Python & Matplotlib
Author: Nicolas P. Rougier
License: BSD

Modifications:
- Extracted the code into a function that could be imported or run as a script
- Refactored the code to improve readability
- Formatted the code using Ruff

Modified by: Artem Kislovskiy
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle
from matplotlib.patheffects import withStroke
from matplotlib.ticker import AutoMinorLocator, MultipleLocator, FuncFormatter


def format_minor_tick_value(value, _):
    return "%.2f" % value if value % 1 else ""


def generate_data():
    np.random.seed(123)
    x = np.linspace(0.5, 3.5, 100)
    y1 = 3 + np.cos(x)
    y2 = 1 + np.cos(1 + x / 0.75) / 2
    y3 = np.random.uniform(y1, y2, len(x))
    return x, y1, y2, y3


def setup_plot():
    figure = plt.figure(figsize=(8, 8))
    ax = figure.add_subplot(1, 1, 1, aspect=1)
    ax.set_xlim(0, 4)
    ax.set_ylim(0, 4)
    return figure, ax


def set_major_minor_ticks(ax: plt.Axes) -> None:
    ax.xaxis.set_major_locator(MultipleLocator(1.0))
    ax.xaxis.set_minor_locator(AutoMinorLocator(4))
    ax.yaxis.set_major_locator(MultipleLocator(1.0))
    ax.yaxis.set_minor_locator(AutoMinorLocator(4))
    ax.xaxis.set_minor_formatter(FuncFormatter(format_minor_tick_value))


def customize_ticks_and_grid(ax: plt.Axes) -> None:
    ax.tick_params(which="major", width=1.0, length=10)
    ax.tick_params(which="minor", width=1.0, length=5, labelsize=10, labelcolor="0.25")
    ax.grid(linestyle="--", linewidth=0.5, color=".25", zorder=-10)


def plot_signals(ax, x, y1, y2, y3):
    ax.plot(x, y1, c=(0.25, 0.25, 1.00), lw=2, label="Blue signal", zorder=10)
    ax.plot(x, y2, c=(1.00, 0.25, 0.25), lw=2, label="Red signal")
    ax.plot(x, y3, linewidth=0, marker="o", markerfacecolor="w", markeredgecolor="k")


def add_annotations(ax: plt.Axes) -> None:
    annotations = [
        (0.50, -0.10, "Minor tick label"),
        (-0.03, 4.00, "Major tick"),
        (0.00, 3.50, "Minor tick"),
        (-0.15, 3.00, "Major tick label"),
        (1.80, -0.27, "X axis label"),
        (-0.27, 1.80, "Y axis label"),
        (1.60, 4.13, "Title"),
        (1.75, 2.80, "Line\n(line plot)"),
        (1.20, 0.60, "Line\n(line plot)"),
        (3.20, 1.75, "Markers\n(scatter plot)"),
        (3.00, 3.00, "Grid"),
        (3.70, 3.80, "Legend"),
        (0.5, 0.5, "Axes"),
        (-0.3, 0.65, "Figure"),
    ]

    for x, y, text in annotations:
        circle = Circle(
            (x, y),
            0.15,
            clip_on=False,
            zorder=10,
            linewidth=1,
            edgecolor="black",
            facecolor=(0, 0, 0, 0.0125),
            path_effects=[withStroke(linewidth=5, foreground="w")],
        )
        ax.add_artist(circle)
        ax.text(
            x,
            y - 0.2,
            text,
            backgroundcolor="white",
            ha="center",
            va="top",
            weight="regular",
            color="#000099",
        )


def add_spines_annotation(ax):
    color = "#000099"
    ax.annotate(
        "Spines",
        xy=(4.0, 0.35),
        xytext=(3.3, 0.5),
        color=color,
        weight="regular",
        arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color=color),
    )

    ax.annotate(
        "",
        xy=(3.15, 0.0),
        xytext=(3.45, 0.45),
        color=color,
        weight="regular",
        arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color=color),
    )


def main() -> plt.Figure:
    x, y1, y2, y3 = generate_data()
    figure, ax = setup_plot()
    set_major_minor_ticks(ax)
    customize_ticks_and_grid(ax)
    plot_signals(ax, x, y1, y2, y3)
    add_annotations(ax)
    add_spines_annotation(ax)
    ax.set_title("Anatomy of a figure", fontsize=20, verticalalignment="bottom")
    ax.set_xlabel("X axis label")
    ax.set_ylabel("Y axis label")
    ax.legend(loc="upper right")
    return figure


if __name__ == "__main__":
    fig = main()
