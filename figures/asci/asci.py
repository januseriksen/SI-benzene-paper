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

PALETTE = sns.color_palette('Set2')

HF = -230.721819

dets = np.array([
100000,
250000,
500000,
1000000,
2000000,
5000000
])

e_cvar = np.array([
-661.17,
-685.91,
-698.34,
-709.96,
-721.68,
-737.13
])

e_ctot = np.array([
-821.14,
-825.45,
-827.75,
-830.00  ,
-832.29 ,
-835.38
])


dets_updated = np.array([
100000,
250000,
500000,
1000000,
2000000,
4000000
])

e_cvar_updated = np.array([
-698.31,
-719.63,
-735.12,
-749.43,
-761.51,
-772.35
])

e_ctot_updated = np.array([
-815.05,
-820.65,
-824.62,
 -828.60  ,
-832.00 ,
-835.18
])

# set seaborn
sns.set(style='darkgrid', palette='Set2', font='DejaVu Sans')

# set subplot
fig, ax = plt.subplots()

# plot results
ax.semilogx(dets, e_cvar, marker='x', linewidth=2, mew=1, linestyle='-', label='$E_{\mathrm{c}}^{\mathrm{var}}$')
ax.semilogx(dets_updated, e_cvar_updated, marker='x', linewidth=2, mew=1, linestyle='--', color=PALETTE[0])
ax.semilogx(dets, e_ctot, marker='x', linewidth=2, mew=1, linestyle='-', label='$E_{\mathrm{c}}^{\mathrm{var+PT2}}$')
ax.semilogx(dets_updated, e_ctot_updated, marker='x', linewidth=2, mew=1, linestyle='--', color=PALETTE[1])
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

