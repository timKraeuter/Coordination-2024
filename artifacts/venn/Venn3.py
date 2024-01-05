#!/usr/bin/env python

import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Can only do up to 3 sets but calculates real overlaps of the venn diagrams.
# Upset plots for more?
tim = {"Event-Scheduling coordination", "Dedicated coordination elements", "Predefined", "Timed:Logical", "Formal language", "Heterogeneous", "Non-Intrusive", "Discrete event system", "Coordinated simulation", "Custom properties"}
wright = {"Data-driven coordination", "Architecture based", "Customizable", "Timed:Logical", "Causal", "Formal language", "Homogeneous", "Intrusive", "Discrete event system", "Coordinated simulation", "Model checking"}
linda = {"Data-driven coordination", "Name based", "Predefined", "Causal", "Programming language", "Homogeneous", "Intrusive", "Discrete event system", "Coordinated execution"}

venn3([tim, wright, linda], ("BCoordLang", "Wright", "Linda"))

plt.show()
