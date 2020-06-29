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

dets = np.array([
100000,
250000,
500000,
1000000,
2000000,
5000000
])

e_var = np.array([
-231.38299,
-231.40772,
-231.42016,
-231.43178,
-231.44350,
-231.45895
])

e_tot = np.array([
-231.542957,
-231.547269,
-231.549569,
-231.551819,
-231.554105,
-231.557199
])

# set seaborn
sns.set(style='darkgrid', palette='Set2', font='DejaVu Sans')

# set subplot
fig, ax = plt.subplots()

# plot results
ax.semilogx(dets, (e_var - HF) * 1000., marker='x', linewidth=2, mew=1, linestyle='-', label='$E_{{\mathrm{var}}}$')
ax.semilogx(dets, (e_tot - HF) * 1000., marker='x', linewidth=2, mew=1, linestyle='-', label='$E_{{\mathrm{var+PT2}}}$')

# turn off x-grid
ax.xaxis.grid(False)

# set labels
ax.set_xlabel('Number of Determinants')
ax.set_ylabel('Total Correlation Energy (in m$E_{{\mathrm{H}}}$)')

# despine
sns.despine()

# set legend
ax.legend(loc=1, frameon=False)

# save plot
plt.savefig('asci.pdf', bbox_inches = 'tight', dpi=1000)

