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

energy = np.array([
-230.816932,
-231.191703,
-231.437084,
-231.598456,
-231.598443,
-231.584808,
-231.584846,
-231.584846
])

# set seaborn
sns.set(style='darkgrid', palette='Set2', font='DejaVu Sans')

# set subplot
fig, ax = plt.subplots()

# plot results
ax.plot(np.arange(1, energy.size + 1), (energy - HF) * 1000., \
        marker='x', linewidth=2, mew=1, linestyle='-', \
        color='xkcd:kelly green', label='MBE-FCI')

# set x limits
ax.set_xlim([0.5, energy.size + 1 - 0.5])

# turn off x-grid
ax.xaxis.grid(False)

# set labels
ax.set_xlabel('Expansion order')
ax.set_ylabel('Total Correlation Energy (in m$E_{{\mathrm{H}}}$)')

# force integer ticks on x-axis
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
#ax.yaxis.set_major_formatter(FormatStrFormatter('%.3f'))

# despine
sns.despine()

# set legend
ax.legend(loc=1, frameon=False)

# save plot
plt.savefig('mbe_fci.pdf', bbox_inches = 'tight', dpi=1000)

