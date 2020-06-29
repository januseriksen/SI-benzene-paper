#!/usr/bin/env python
# -*- coding: utf-8 -*

import numpy as np
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['font.sans-serif'] = ['DejaVu Sans']
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator, FormatStrFormatter
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

# set seaborn
sns.set(style='darkgrid', palette='Set2', font='DejaVu Sans')

# set subplot
fig, ax = plt.subplots()

# plot results
ax.plot(w, (e - HF) * 1000., marker='x', linewidth=2, mew=1, linestyle='-', label='$E_{{\mathrm{DMRG}}}$')

# turn off x-grid
ax.xaxis.grid(False)

# set labels
ax.set_xlabel('Discarded Weight')
ax.set_ylabel('Total Correlation Energy (in m$E_{{\mathrm{H}}}$)')

# x-axis format
ax.xaxis.set_major_formatter(FormatStrFormatter('%.1e'))

# despine
sns.despine()

# set legend
ax.legend(loc='upper left', frameon=False)

# save plot
plt.savefig('dmrg.pdf', bbox_inches = 'tight', dpi=1000)

