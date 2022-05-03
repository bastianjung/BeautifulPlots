import pkg_resources
from BeautifulPlots import plt
import matplotlib

def reset_style():
    plt.style.use(pkg_resources.resource_filename('BeautifulPlots.styles', 'style_white_serif.mplstyle'))
    matplotlib.rcParams['pdf.fonttype'] = 42
    matplotlib.rcParams['ps.fonttype'] = 42
