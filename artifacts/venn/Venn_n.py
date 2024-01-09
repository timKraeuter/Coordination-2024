import matplotlib.pyplot as plt
from venn import venn

# Can do up to 6 venn diagrams but overlaps are always the same only the numbers change.
features = {
    "Set1": {'A', 'B', 'C'},
    "Set2": {'A', 'B', 'D'},
    "Set3": {'A'},
    "Set4": {'C'}
}
venn(features)

plt.show()
