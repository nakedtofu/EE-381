# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 03:38:04 2018

@author: NAO
"""

import numpy as np
import matplotlib.pyplot as plt

aa1 = [0,1,1,2,3,3,4,4,5,9]
aa2 = [0,1,3,3,4,4,4,4,5,6,7,9]
bins = [0,3,9]
height = [np.histogram( xs, bins=bins)[0] for xs in [aa1, aa2]]
left, n = np.arange(len(bins)-1), len(height)

ax = plt.subplot(111)
color_cycle = ax._get_lines.color_cycle

for j, h in enumerate(height):
    ax.bar(left + j / n, h, width=1.0/n, color=next(color_cycle))

ax.set_xticks(np.arange(0, len(bins)))
ax.set_xticklabels(map(str, bins))