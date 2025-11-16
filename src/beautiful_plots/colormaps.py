"""Custom colormaps for BeautifulPlots package."""

import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap

# Define the dark_beauty colormap
# Colors transition: cyan/turquoise -> teal -> purple -> red/orange
dark_beauty_colors = [
    "#6DF8D7",  # Bright cyan
    "#61DFC3",  # Cyan-teal
    "#4CB19A",  # Teal
    "#7183F8",  # Purple-blue
    "#3725A7",  # Deep purple
    "#DC496B",  # Red-pink
    "#C0391C",  # Deep red
]

dark_beauty = LinearSegmentedColormap.from_list("dark_beauty", dark_beauty_colors[::-1])
dark_beauty_reverse = LinearSegmentedColormap.from_list("dark_beauty_reverse", dark_beauty_colors)


def register_colormaps():
    """Register all custom colormaps with matplotlib."""
    mpl.colormaps.register(dark_beauty_reverse)
    mpl.colormaps.register(dark_beauty)
