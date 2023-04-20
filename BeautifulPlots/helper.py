import os
import matplotlib.pyplot as plt
import pathlib as pl
import matplotlib


def set_style(name: str):
    style_path = pl.Path(__file__).parents[0] / "styles" / (name + ".mplstyle")
    if not os.path.exists(style_path):
        raise Exception(f"File not found: {style_path}")
    plt.style.use(style_path)


def get_style_names() -> list[str]:
    style_base = pl.Path(__file__).parents[0] / "styles"
    styles = []
    for file in os.listdir(style_base):
        if file[-9:] == ".mplstyle":
            styles.append(file[:-9])
    return styles
