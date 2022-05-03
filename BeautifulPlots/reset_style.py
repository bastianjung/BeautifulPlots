import pkg_resources
from BeautifulPlots import plt
import matplotlib

def reset_style():
    plt.style.use(pkg_resources.resource_filename('BeautifulPlots.styles', 'style_white_serif.mplstyle'))
    font_paths = pkg_resources.resource_listdir('BeautifulPlots.font','')
    for font in font_paths:
        if 'ttf' in font:
            path = pkg_resources.resource_filename('BeautifulPlots.font', font)
            matplotlib.font_manager.fontManager.addfont(path)
    matplotlib.rcParams['axes.unicode_minus'] = False
    font = {'family': 'CMU Serif'}
    matplotlib.rcParams['pdf.fonttype'] = 42
    matplotlib.rcParams['ps.fonttype'] = 42
    matplotlib.rc('font', **font)
