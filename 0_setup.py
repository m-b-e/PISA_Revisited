#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 12:35:39 2022

@author: Jo
"""

# Python ≥3.5 is required
import sys
assert sys.version_info >= (3, 5)

# Scikit-Learn ≥0.20 is required
import sklearn
assert sklearn.__version__ >= "0.20"

# Common imports
import numpy as np
import pandas as pd
import os

# set working directory
os.getcwd()
os.chdir('/GoogleDrive/My Drive/PISA_Revisited/')

# to make the output stable across runs
np.random.seed(42)

# To plot figures
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)

# Where to save the figures
from pathlib import Path
Path("figures").mkdir(parents=True, exist_ok=True)


# Where to save the figures
PROJECT_ROOT_DIR = "." 
IMAGES_PATH = os.path.join(PROJECT_ROOT_DIR) #deleted: , "images")
os.makedirs(IMAGES_PATH, exist_ok=True)

def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    path = os.path.join(IMAGES_PATH, fig_id + "." + fig_extension)
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)

