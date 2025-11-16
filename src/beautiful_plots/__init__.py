import os

import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

from .colormaps import register_colormaps

# # Rebuild the font cache to ensure all system fonts (including custom fonts) are detected
# # This is especially important for fonts like 'Inter' that may be installed on the system
# fm.fontManager = fm.FontManager()

# Get the absolute path to the 'styles' directory in this package
style_dir = os.path.join(os.path.dirname(__file__), "styles")

# Add this path to matplotlib's list of style libraries
plt.style.core.USER_LIBRARY_PATHS.append(style_dir)

# Reload the style library so matplotlib picks up the new styles
plt.style.reload_library()

# Set dark_x_clean as the default style
plt.style.use("dark_x_clean")

# Register custom colormaps
register_colormaps()

del os, plt, fm, style_dir, register_colormaps
