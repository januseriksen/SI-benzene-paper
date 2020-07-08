#!/usr/bin/env python
# -*- coding: utf-8 -*

import numpy as np
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['font.sans-serif'] = ['DejaVu Sans']
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator, FormatStrFormatter, MultipleLocator
import seaborn as sns

HF = -230.721819

w = np.array([
5.272e-05,
2.898e-05,
2.055e-05,
1.558e-05,
1.253e-05,
1.019e-05
])

e = np.array([
-231.5667,
-231.5747,
-231.5778,
-231.5794,
-231.5803,
-231.5810
])

# extrapolation
coef = np.polyfit(w, (e - HF) * 1000., 1)
f = np.poly1d(coef) 
w_extrap = np.array([0.0, 5.272e-05])
e_extrap = f(w_extrap)

# set seaborn
sns.set(style='darkgrid', palette='Set2', font='DejaVu Sans')

# set subplot
fig, ax = plt.subplots()

# plot results
ax.scatter(w, (e - HF) * 1000., marker ='s', s=20, linewidths=1, color="none", edgecolor=sns.color_palette("Set2")[0], label='$E_{{\mathrm{DMRG}}}$')
ax.plot(w_extrap, e_extrap, linewidth=2, dashes=[6,2], linestyle='-') 

# turn off x-grid
ax.xaxis.grid(False)

# set labels
ax.set_xlabel('Discarded Weight')
ax.set_ylabel('Total Correlation Energy (in m$E_{{\mathrm{H}}}$)')

# x-axis, y-axis format
ax.set_xlim([0,6e-5])
ax.xaxis.set_major_formatter(FormatStrFormatter('%.0e'))
ax.xaxis.set_ticks(np.arange(0, 7e-5, 1e-5))
ax.set_ylim([-863,-843])
ax.yaxis.set_major_formatter(FormatStrFormatter('%d'))
ax.yaxis.set_ticks(np.arange(-863, -839, 4))

# despine
sns.despine()

# set legend
ax.legend(loc='upper left', frameon=False)

# save plot
plt.savefig('dmrg.pdf', bbox_inches = 'tight', dpi=1000)

