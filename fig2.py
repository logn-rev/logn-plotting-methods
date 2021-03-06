import matplotlib as mpl
mpl.use('Agg')
import pylab as pl

import numpy as np

def uniform_pdf(x, scale):
    return np.ones_like(x)/float(scale)

from scipy.stats import uniform

loc, scale = 0, 80
xs = uniform.rvs(loc=loc, scale=scale, size=500000)

fig = pl.figure()

# ----- 2x2 -----
fig.set_size_inches(8,6.)
ax1 = pl.subplot2grid((2, 2), (0, 0))
ax2 = pl.subplot2grid((2, 2), (0, 1))
ax3 = pl.subplot2grid((2, 2), (1, 0))
ax4 = pl.subplot2grid((2, 2), (1, 1))


bin_min, bin_max = 0,80
bin_N = 1000
s=0.01

xr = np.arange(bin_min, bin_max+s, s)

ax1.set_xlim(0,bin_max)
ax1.hist(xs, np.linspace(bin_min, bin_max, bin_N), normed=True)
ax1.plot(xr, uniform_pdf(xr, scale), 'r')

ax2.plot(np.log10(xr), uniform_pdf(xr, scale), 'r')
ax2.hist(np.log10(xs), bins=bin_N, normed=True)


counts, edges = np.histogram(xs, bins=np.linspace(bin_min, bin_max, bin_N),
                             density=True)
centers = (edges[1:] + edges[:-1])/2.
ax3.plot(np.log10(centers), counts, '.', color='k')
ax3.plot(np.log10(xr), uniform_pdf(xr, scale), 'r')


ax4.hist(xs, 10**np.linspace(-2,2,bin_N), normed=True)
ax4.set_xscale('log')
ax4.plot(xr, uniform_pdf(xr, scale), 'r')


import os
fname = os.path.splitext(os.path.basename(__file__))[0]

pl.tight_layout()
pl.savefig("{}.png".format(fname), dpi=300, bbox_inches='tight')



