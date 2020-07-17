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
1134081,
3901848,
13486304,
64100382,
102088555,
194977798,
276617654
])

e_cvar = np.array([
-231.468564,
-231.491252,
-231.511826,
-231.533720,
-231.539142,
-231.545790,
-231.548984
])

e_ctot = np.array([
-231.550787,
-231.557309,
-231.563444,
-231.570044,
-231.571697,
-231.573686,
-231.574641
])


dets_updated = np.array([
3780337,
12722141,
59310339,
94569745,
180662587,
536792289
])

e_cvar_updated = np.array([
-231.497568,
-231.516872,
-231.537074,
-231.542155,
-231.548415,
-231.557059
])

e_ctot_updated = np.array([
-231.558399,
-231.564290,
-231.570545,
-231.572140,
-231.574081,
-231.576736
])

# set seaborn
sns.set(style='darkgrid', palette='Set2', font='DejaVu Sans')

# set subplot
fig, ax = plt.subplots()

# plot results
ax.semilogx(dets, (e_cvar - HF) * 1000., marker='x', linewidth=2, mew=1, linestyle='-', label='$E_{\mathrm{c}}^{\mathrm{var}}$')
ax.semilogx(dets_updated, (e_cvar_updated - HF) * 1000., marker='x', linewidth=2, mew=1, linestyle='--', color=PALETTE[0])
ax.semilogx(dets, (e_ctot - HF) * 1000., marker='x', linewidth=2, mew=1, linestyle='-', label='$E_{\mathrm{c}}^{\mathrm{var+PT2}}$')
ax.semilogx(dets_updated, (e_ctot_updated - HF) * 1000., marker='x', linewidth=2, mew=1, linestyle='--', color=PALETTE[1])
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
plt.savefig('shci.pdf', bbox_inches = 'tight', dpi=1000)

