#!/usr/bin/env python

"""
Get WorldClim version 2 climate data for various vars between 1970-2000.
"""

__author__ = "Martin De Kauwe"
__version__ = "1.0 (20.02.2020)"
__email__ = "mdekauwe@gmail.com"

from urllib.request import urlretrieve
from pathlib import Path
import os


res = "10m" #"5m" "2.5m", "30s"
#vars = ["tmin", "tmax", "tavg", "prec", "srad", "wind", "vapr"]
vars = ["tavg"]
base_address = 'http://biogeo.ucdavis.edu/data/worldclim/v2.0/tif/base/'

for var in vars:
    print(var)

    fname = "wc2.0_%s_%s.zip" % (res, var)
    address = base_address + fname

    output_dir = "data/%s" % (var)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_fname = os.path.join(output_dir, fname)

    if not Path(fname).exists():
        urlretrieve(address, output_fname)
