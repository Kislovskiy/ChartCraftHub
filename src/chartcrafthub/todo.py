from matplotlib import pyplot as plt


def run_to_do():
    fig, ax = plt.subplots()
    ax.text(
        0.5,
        0.5,
        "to do",
        fontsize=20,
        ha="center",
        font="monospace",
        bbox=dict(facecolor="red", alpha=0.5, edgecolor="blue", boxstyle="round"),
    )
    fig.savefig("results/to_do.png")


if __name__ == "__main__":
    run_to_do()
