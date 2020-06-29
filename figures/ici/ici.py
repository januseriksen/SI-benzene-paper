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

dets_hf = np.array([
71137,
147228,
225685,
333495,
480806,
921928,
1120558,
1410356,
1849734,
2570589,
3869123
])

dets_hf_updated = np.array([
1172202,
1561473,
2273564,
3856238,
9150757,
17861976,
46457235,
59119837
])

dets_no = np.array([
50944,
106317,
199486,
358274,
586272,
1277001,
1585683,
2028558,
2697171,
3759324,
5580152
])

dets_no_updated = np.array([
1379097,
1932040,
2991370,
5436028,
12849733,
23479710,
52744912,
64497488
])

e_var_hf = np.array([
-589.336,
-649.922,
-667.714,
-675.959,
-681.083,
-688.358,
-690.363,
-692.695,
-695.422,
-698.767,
-703.066
]) * 1.e-3 + HF

e_var_hf_updated = np.array([
-231.411342,
-231.414156,
-231.417867,
-231.423134,
-231.432506,
-231.440956,
-231.455449,
-231.459591
])

e_var_no = np.array([
-612.591,
-656.729,
-676.147,
-687.627,
-695.623,
-707.243,
-710.440,
-714.110,
-718.441,
-723.616,
-729.983
]) * 1.e-3 + HF

e_var_no_updated = np.array([
-231.426918,
-231.431718,
-231.438173,
-231.447469,
-231.462064,
-231.473090,
-231.488602,
-231.492514
])

e_tot_hf = np.array([
-802.909,
-810.127,
-812.884,
-814.997,
-816.564,
-818.664,
-819.194,
-819.797,
-820.487,
-821.330,
-822.427
]) * 1.e-3 + HF

e_tot_hf_updated = np.array([
-231.540665,
-231.541358,
-231.542292,
-231.543609,
-231.546084,
-231.548393,
-231.552376,
-231.553511
])

e_tot_no = np.array([
-816.724,
-819.366,
-822.384,
-824.699,
-826.403,
-828.807,
-829.460,
-830.223,
-831.135,
-832.289,
-833.690
]) * 1.e-3 + HF

e_tot_no_updated = np.array([
-231.549914,
-231.550900,
-231.552260,
-231.554286,
-231.557577,
-231.560117,
-231.563737,
-231.564653
])

# set seaborn
sns.set(style='darkgrid', palette='Set2', font='DejaVu Sans')

# set subplot
fig, ax = plt.subplots()

# plot results
ax.semilogx(dets_hf, (e_var_hf - HF) * 1000., marker='x', linewidth=2, mew=1, linestyle='-', color=PALETTE[0], label='$E_{{\mathrm{var}}}$ (HF)')
ax.semilogx(dets_hf_updated, (e_var_hf_updated - HF) * 1000., marker='x', linewidth=2, mew=1, linestyle='--', color=PALETTE[1])
ax.semilogx(dets_hf, (e_tot_hf - HF) * 1000., marker='x', linewidth=2, mew=1, linestyle='-', color=PALETTE[1], label='$E_{{\mathrm{var+PT2}}}$ (HF)')
ax.semilogx(dets_hf_updated, (e_tot_hf_updated - HF) * 1000., marker='x', linewidth=2, mew=1, linestyle='--', color=PALETTE[1])
ax.semilogx(dets_no, (e_var_no - HF) * 1000., marker='x', linewidth=2, mew=1, linestyle='-', color=PALETTE[2], label='$E_{{\mathrm{var}}}$ (NO)')
ax.semilogx(dets_no_updated, (e_var_no_updated - HF) * 1000., marker='x', linewidth=2, mew=1, linestyle='--', color=PALETTE[2])
ax.semilogx(dets_no, (e_tot_no - HF) * 1000., marker='x', linewidth=2, mew=1, linestyle='-', color=PALETTE[3], label='$E_{{\mathrm{var+PT2}}}$ (NO)')
ax.semilogx(dets_no_updated, (e_tot_no_updated - HF) * 1000., marker='x', linewidth=2, mew=1, linestyle='--', color=PALETTE[3])

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
plt.savefig('ici.pdf', bbox_inches = 'tight', dpi=1000)

