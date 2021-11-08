# Authors: Clemens Brunner <clemens.brunner@gmail.com>
#
# License: BSD (3-clause)

import sys
import multiprocessing as mp
import matplotlib
from qtpy.QtWidgets import QApplication
from qtpy.QtCore import Qt

from .mainwindow import MainWindow
from .model import Model


__version__ = "0.6.5"


def main():
    mp.set_start_method("spawn", force=True)  # required for Linux
    app_name = "MNELAB"
    if sys.platform.startswith("darwin"):
        # set bundle name on macOS (app name shown in the menu bar)
        from Foundation import NSBundle
        bundle = NSBundle.mainBundle()
        info = bundle.localizedInfoDictionary() or bundle.infoDictionary()
        info["CFBundleName"] = app_name

    matplotlib.use("Qt5Agg")
    app = QApplication(sys.argv)
    app.setApplicationName(app_name)
    app.setOrganizationName("cbrnr")
    if sys.platform.startswith("darwin"):
        app.setAttribute(Qt.AA_DontShowIconsInMenus, True)
    app.setAttribute(Qt.AA_UseHighDpiPixmaps)
    model = Model()
    model.view = MainWindow(model)
    if len(sys.argv) > 1:  # open files from command line arguments
        for f in sys.argv[1:]:
            model.load(f)
    model.view.show()
    sys.exit(app.exec_())
