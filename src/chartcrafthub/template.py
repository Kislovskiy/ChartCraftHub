import logging
from pathlib import Path

from matplotlib import pyplot as plt
from rich.logging import RichHandler

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler()],
)


def main():
    def y(x):
        return x + (x * x * 8) / 4

    figure, ax = plt.subplots(figsize=(6, 4))
    x_values = [i / 100 for i in range(101)]
    y_values = [y(x) for x in x_values]
    ax.plot(x_values, y_values, label="y(x)")
    ax.legend()
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Plot Title")
    logger.info("Figure created successfully.")
    return figure


if __name__ == "__main__":
    fig = main()
    fig.tight_layout()
    results_dir = Path("results")
    results_dir.mkdir(parents=True, exist_ok=True)
    save_path = results_dir.joinpath("plot.png")
    fig.savefig(save_path, format="png", bbox_inches="tight")
    logger.info(f"Figure saved to {save_path}.")
