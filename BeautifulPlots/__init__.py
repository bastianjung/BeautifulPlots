from .helper import set_style, get_style_names
import shutil
import matplotlib

matplotlib.font_manager._load_fontmanager(try_read_cache=False)

__all__ = ["set_style", "get_style_names"]
