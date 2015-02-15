# -*- coding: utf-8 -*-

__author__ = 'Kian Ho'
__email__ = 'hui.kian.ho@googlemail.com'
__version__ = '0.1.0'


import matplotlib as mpl

mpl.use("Agg")

from matplotlib import pylab


def init_mpl(linewidth=1.05):
    """Dynamically initialise certain matplotlib settings.

    """

    mpl.rc("lines", linewidth=linewidth)
    mpl.rc("xtick", **{"direction" : "out" })
    mpl.rc("ytick", **{"direction" : "out" })
    mpl.rc("font", **{"family" : "FreeSans", "size" : 10.})
    mpl.rc("legend", frameon=False, fontsize=10., numpoints=1)

    pylab.tick_params(axis="x", which="both", top="off")
    pylab.tick_params(axis="y", which="both", right="off")

    ax = pylab.gca()

    for key, spine in ax.spines.items():
        spine.set_linewidth(linewidth)

    return


init_mpl()
