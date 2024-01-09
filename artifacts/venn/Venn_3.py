#!/usr/bin/env python

# venn3 can only do a venn diagram of up to 3 sets.

import matplotlib.pyplot as plt
from matplotlib_venn import venn3
import sys
import pandas as pd

args = sys.argv[1:]

if len(sys.argv) != 4:  # Includes the script name
  print(
      'There should be exactly 3 arguments to select 3 coordination approaches! Current arguments:',
      str(args))
  sys.exit(1)

df = pd.read_excel('../classification.xlsx')

approaches = []
for approach in args:
  # Filter nan, to lowercase, to array.
  values = df[approach][df[approach].notnull()].str.lower().values
  approaches.append(set(values))

venn3(approaches, args)

# plt.savefig("coordination_venn3.svg", format="svg", bbox_inches="tight")
plt.show()
