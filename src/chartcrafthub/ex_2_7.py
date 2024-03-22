import logging
from io import BytesIO

from ex_1_1 import setup_logger
from matplotlib import image as mpimg
from matplotlib import pyplot as plt

logger = logging.getLogger(__name__)
setup_logger()


def render_hello_world_image(dpi):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.text(x=0.5, y=0.5, s="Hello World", fontsize=50, ha="center", va="center")

    # Save the figure to an in-memory BytesIO object
    img_buffer = BytesIO()
    fig.savefig(img_buffer, format="png", dpi=dpi)
    img_buffer.seek(0)

    # Read the image from the BytesIO object
    image = mpimg.imread(img_buffer)
    plt.close()

    return image


def get_common_size(images):
    heights, widths, _ = zip(*[img.shape for img in images])
    common_height = max(heights)
    common_width = max(widths)
    return common_width, common_height


def plot_images(images):
    num_images = len(images)
    ncols = int(num_images**0.5)
    nrows = (num_images + ncols - 1) // ncols

    fig, ax = plt.subplots(figsize=(6, 6), nrows=nrows, ncols=ncols)

    for i, img in enumerate(images):
        row = i // ncols
        col = i % ncols
        ax[row, col].imshow(img, extent=[0, common_width, 0, common_height])

    return fig


if __name__ == "__main__":
    dpis = [10, 100, 300, 600]
    hello_world_images = [render_hello_world_image(dpi) for dpi in dpis]
    common_width, common_height = get_common_size(hello_world_images)
    fig = plot_images(hello_world_images)
    fig.tight_layout()
    save_path = "results/ex_2_7.png"
    fig.savefig(save_path, dpi=600)
    logger.info(f"Saved plot to {save_path}")
