#!/usr/bin/env python

# venn3 can only do a venn diagram of up to 3 sets.

import itertools
import matplotlib.pyplot as plt
from matplotlib_venn import venn3
import sys
import pandas as pd

approach_names = sys.argv[1:]

if len(sys.argv) != 4:  # Includes the script name
    print(
        'There should be exactly 3 arguments to select 3 coordination approaches! Current arguments:',
        str(approach_names))
    sys.exit(1)

df = pd.read_excel('../classification.xlsx')
# Lower case to find things more conveniently.
df.columns = map(str.lower, df.columns)

approach_features = []
for approach in approach_names:
    approach = approach.lower()
    # Filter nan, to lowercase, to array.
    feature_cells = df[approach][df[approach].notnull()].str.lower().values
    feature_set = set()
    for feature_cell in feature_cells:
        # Handle cells that contain multiple features separated by ,
        if feature_cell.find(",") != -1:
            for feature in feature_cell.split(","):
                feature = feature.strip()
                feature_set.add(feature)
        else:
            feature_set.add(feature_cell)
    approach_features.append(feature_set)

venn3(approach_features, approach_names)

filename = '_'.join(approach_names) + "_venn"

plt.savefig(filename + ".svg", format="svg", bbox_inches="tight")
plt.show()

# Print diff and overlap statistics.
A = approach_features[0]
B = approach_features[1]
C = approach_features[2]
A_name = approach_names[0]
B_name = approach_names[1]
C_name = approach_names[2]

# Do A
print("{}'s unique features ({}): {}".format(A_name, len(A - B - C), str(A - B - C)))
print(
    "{}'s and {}'s common features ({}) without {}: {}".format(A_name, B_name, len(A & B - C), C_name, str(A & B - C)))
print(
    "{}'s and {}'s common features ({}) without {}: {}".format(A_name, C_name, len(A & C - B), B_name, str(A & C - B)))

# Do B
print("{}'s unique features ({}): {}".format(B_name, len(B - A - C), str(B - A - C)))
print(
    "{}'s and {}'s common features ({}) without {}: {}".format(B_name, C_name, len(B & C - A), A_name, str(B & C - A)))

# Do C
print("{}'s unique features ({}): {}".format(C_name, len(C - A - B), str(C - A - B)))
print("Common features ({}): {}".format(len(A & B & C), str(A & B & C)))
