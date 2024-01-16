# Coordination-2024
This repository contains the sources of [our paper](./paper.pdf) submitted to the [26th International Conference on Coordination Models and Languages (Coordination 2024)](https://www.discotec.org/2024/coordination) and associated artifacts.

# Feature model
The following figure shows the complete feature model.

![](./artifacts/images/feature-model.svg)

# Application of the feature model
All classification data can be found [here](./artifacts/classification.xlsx).

## Venn diagrams and other plots
A script to generate **Venn diagrams** and **UpSet plots** from the classification data with explanation is located [here](./artifacts/venn-diagram-scripts/).

**Venn diagrams:**

![venn diagram](./artifacts/venn-diagram-scripts/venn-diagrams/BCoorLang_DACCOSIM_MontiArc_venn.svg)

**UpSet plots:**

![venn diagram](./artifacts/venn-diagram-scripts/upset-plots/BCoorLang_Linda_MontiArc_DACCOSIM_upset.svg)

# Running example: Pedestrian crossing

![](./artifacts/images/runningExample.svg)

## MontiArc
The source code for the MontiArc implementation can be found [here](https://github.com/timKraeuter/montiarc/tree/develop/applications/crossing/main/montiarc/crossing).
