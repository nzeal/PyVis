import matplotlib.pyplot as plt
import numpy as np
import glob
import math
import pandas as pd

from statistics import mean

file = open("fld_ene")

plt.figure(figsize=(16,10), dpi= 80)
plt.title("B-field Vs time", fontsize=22)
plt.xlabel(r"Time", size=20)
plt.ylabel(r"B-field ene", size=20)

plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
#plt.ylim(15, 30)

with file as f:
    time, b1, b2, b3, e1, e2, e3 = np.loadtxt(file, skiprows=2, usecols=(1, 2, 3, 4, 5, 6, 7), unpack=True)
    _, indx = np.unique(time, return_index=True)
    time = time[indx]
    b1 = b1[indx]
    b2 = b2[indx]
    b3 = b3[indx]
    e1 = e1[indx]
    e2 = e2[indx]
    e3 = e3[indx]
    
    plt.semilogy(time, b3)
