import pkg_resources
from BeautifulPlots import plt
def reset_style():
    plt.style.use(pkg_resources.resource_filename('BeautifulPlots.styles', 'style_white.mplstyle'))
