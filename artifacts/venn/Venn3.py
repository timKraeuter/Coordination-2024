#!/usr/bin/env python

import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Can only do up to 3 sets but calculates real overlaps of the venn diagrams.
# Upset plots for more?
set1 = {'A', 'B', 'C'}
set2 = {'A', 'B', 'D'}
set3 = {'A'}

venn3([set1, set2, set3], ('set1', 'set2', 'set3'))

plt.show()
