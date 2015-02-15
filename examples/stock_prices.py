#!/usr/bin/env python
# encoding: utf-8
"""

Date:
    Sun Feb 15 21:57:25 AEDT 2015

Author:
    Kian Ho <hui.kian.ho@gmail.com>

Description:
    TODO

Usage:
    stock_prices.py

"""

from __future__ import print_function

import datetime
import mpl_preamble

from pandas.io import data
from mpl_preamble import mpl, pylab

import matplotlib.ticker as ticker


def ytick_format_func(x, pos):
    return "%.2f" % x


if __name__ == '__main__':

    df = data.DataReader("FB", "google",
            start="2013-01-01")

    xs = df.index.to_pydatetime()
    ys = df.Open

    pylab.plot(xs, ys, drawstyle="steps", label="FB")

    df = data.DataReader("TWTR", "google",
            start="2013-01-01")

    xs = df.index.to_pydatetime()
    ys = df.Open

    pylab.plot(xs, ys, drawstyle="steps", label="TWTR")

    ax = pylab.gca()

    # x-tick labels in the "%b '%y" python datetime string format.
    formatter = mpl.dates.DateFormatter("%b '%y")
    ax.xaxis.set_major_formatter(formatter)

    # monthly x-tick labels.
    ax.xaxis.set_major_locator(mpl.dates.MonthLocator(interval=3))

    # y-tick labels in the "%.2f" format.
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(ytick_format_func))

    ax.xaxis.grid(True, color="grey")
    ax.yaxis.grid(True, color="grey")

    # place the grid below each series line. 
    ax.set_axisbelow(True)

    # rotate and right-justify the x-tick labels.
    pylab.xticks(rotation=30, ha="right")

    pylab.legend(loc="upper left", ncol=1)
    pylab.xlabel("Date")
    pylab.ylabel("Price (USD)")

    pylab.savefig("stock_prices.pdf", bbox_inches="tight")
