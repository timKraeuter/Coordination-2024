# Generate Venn diagrams of the feature sets of three approaches

1. Clone this repository.
2. Open a cmd/bash in this folder.
3. Run one of the following commands:

## Venn Diagram: BCoorLang Linda MontiArc

```bash
py Generate_Venn.py BCoorLang Linda MontiArc
```

Generates the **first Venn diagram** in the paper:

![diagram](./venn-diagrams/BCoorLang_Linda_MontiArc_venn.svg)).

Venn diagrams with feature labels can be obtained as described in the next section.

## Venn Diagram: BCoorLang DACCOSIM MontiArc

```bash
py Generate_Venn.py BCoorLang DACCOSIM MontiArc
```

Generates the **second Venn diagram** in the paper:

![diagram](./venn-diagrams/BCoorLang_DACCOSIM_MontiArc_venn.svg)).

Venn diagrams with feature labels can be obtained as described in the next section.

## Venn Diagrams with feature labels

To obtain venn diagrams with feature labels follow the same procedure as before but use one of the commands below:

### Venn Diagram: BCoorLang Linda MontiArc

**Output:**

![diagram](./venn-diagrams/BCoorLang_Linda_MontiArc_venn_labeled.svg)).

**Script:**

```bash
py Generate_Venn_With_Labels.py BCoorLang Linda MontiArc
```

### Venn Diagram: BCoorLang DACCOSIM MontiArc

**Output:**

![diagram](./venn-diagrams/BCoorLang_DACCOSIM_MontiArc_venn_labeled.svg)).

**Script:**

```bash
py Generate_Venn_With_Labels.py BCoorLang DACCOSIM MontiArc
```

## Equivalent UpSet plots

More information about [UpSet plots](https://upset.app/).
Follow the same procedure as before but use one of the new commands below to generate UpSet plots:

### UpSet plot: BCoorLang Linda MontiArc

**Output:**

![diagram](./upset-plots/BCoorLang_Linda_MontiArc_upset.svg)).

**Script:**

```bash
py Generate_Upset.py BCoorLang Linda MontiArc
```

### UpSet plot: BCoorLang DACCOSIM MontiArc

**Output:**

![diagram](./upset-plots/BCoorLang_DACCOSIM_MontiArc_upset.svg)).

**Script:**

```bash
py Generate_Upset.py BCoorLang DACCOSIM MontiArc
```

### UpSet plot: Custom approaches

UpSet plots make most sense for more than three approaches. You can add as many approaches as arguments as you want.

**Script:**

```bash
py Generate_Upset.py BCoorLang Linda MontiArc DACCOSIM
```

**Output:**

![diagram](./upset-plots/BCoorLang_Linda_MontiArc_DACCOSIM_upset.svg)).

## Clustering

DATA here is not final yet!!!
We clustered the approaches using two distance metrics: Feature distance (Edit distance) and Jaccard distance.
You can find the distance matrices in the following two sections.

## Clustering results

### Feature distance matrix

Measures how many features have to be **added/removed** to get from one approach to another (Edit distance).

|              | BCoorLang | BCOoL | Ptolemy | Wright | MontiArc | CommUnity | Metropolis | MECSYCO | DACCOSIM | UMoC++ | LinguaFranca | Reo | Linda | BIP | Manifold | ForSyDe |
|:-------------|----------:|------:|--------:|-------:|---------:|----------:|-----------:|--------:|---------:|-------:|-------------:|----:|------:|----:|---------:|--------:|
| BCoorLang    |         0 |     4 |      13 |     11 |       12 |        10 |         12 |      13 |       15 |     13 |           14 |  13 |    15 |   9 |       15 |      13 |
| BCOoL        |         4 |     0 |      13 |      9 |       12 |        10 |         14 |      13 |       15 |     13 |           14 |  11 |    15 |   9 |       15 |      13 |
| Ptolemy      |        13 |    13 |       0 |     12 |        7 |         7 |          9 |       6 |        8 |      8 |            7 |   8 |    12 |  12 |       10 |       8 |
| Wright       |        11 |     9 |      12 |      0 |        7 |         5 |          9 |      12 |       10 |      8 |            9 |   4 |    12 |   6 |       10 |       8 |
| MontiArc     |        12 |    12 |       7 |      7 |        0 |         2 |          2 |       7 |        5 |      1 |            2 |   3 |     5 |   7 |        3 |       3 |
| CommUnity    |        10 |    10 |       7 |      5 |        2 |         0 |          4 |       9 |        7 |      3 |            4 |   3 |     7 |   7 |        5 |       3 |
| Metropolis   |        12 |    14 |       9 |      9 |        2 |         4 |          0 |       7 |        5 |      1 |            4 |   5 |     5 |   9 |        3 |       5 |
| MECSYCO      |        13 |    13 |       6 |     12 |        7 |         9 |          7 |       0 |        2 |      6 |            9 |  10 |    10 |  12 |        8 |      10 |
| DACCOSIM     |        15 |    15 |       8 |     10 |        5 |         7 |          5 |       2 |        0 |      4 |            7 |   8 |     8 |  10 |        6 |       8 |
| UMoC++       |        13 |    13 |       8 |      8 |        1 |         3 |          1 |       6 |        4 |      0 |            3 |   4 |     4 |   8 |        2 |       4 |
| LinguaFranca |        14 |    14 |       7 |      9 |        2 |         4 |          4 |       9 |        7 |      3 |            0 |   5 |     5 |   7 |        3 |       3 |
| Reo          |        13 |    11 |       8 |      4 |        3 |         3 |          5 |      10 |        8 |      4 |            5 |   0 |     8 |   8 |        6 |       4 |
| Linda        |        15 |    15 |      12 |     12 |        5 |         7 |          5 |      10 |        8 |      4 |            5 |   8 |     0 |  10 |        2 |       4 |
| BIP          |         9 |     9 |      12 |      6 |        7 |         7 |          9 |      12 |       10 |      8 |            7 |   8 |    10 |   0 |        8 |       6 |
| Manifold     |        15 |    15 |      10 |     10 |        3 |         5 |          3 |       8 |        6 |      2 |            3 |   6 |     2 |   8 |        0 |       2 |
| ForSyDe      |        13 |    13 |       8 |      8 |        3 |         3 |          5 |      10 |        8 |      4 |            3 |   4 |     4 |   6 |        2 |       0 |

### Jaccard distance matrix

Measures the [Jaccard distance](https://en.wikipedia.org/wiki/Jaccard_index#Overview) between the feature sets.

|              | BCoorLang |    BCOoL |  Ptolemy |   Wright | MontiArc | CommUnity | Metropolis |  MECSYCO | DACCOSIM |   UMoC++ | LinguaFranca |      Reo |    Linda |      BIP | Manifold |  ForSyDe |
|:-------------|----------:|---------:|---------:|---------:|---------:|----------:|-----------:|---------:|---------:|---------:|-------------:|---------:|---------:|---------:|---------:|---------:|
| BCoorLang    |         0 | 0.333333 | 0.722222 |   0.6875 |     0.75 |  0.666667 |       0.75 |   0.8125 | 0.882353 |   0.8125 |     0.777778 | 0.764706 | 0.882353 |   0.5625 | 0.882353 | 0.764706 |
| BCOoL        |  0.333333 |        0 | 0.722222 |      0.6 |     0.75 |  0.666667 |   0.823529 |   0.8125 | 0.882353 |   0.8125 |     0.777778 |   0.6875 | 0.882353 |   0.5625 | 0.882353 | 0.764706 |
| Ptolemy      |  0.722222 | 0.722222 |        0 | 0.666667 | 0.466667 |  0.466667 |     0.5625 | 0.428571 | 0.533333 | 0.533333 |       0.4375 |      0.5 | 0.705882 | 0.631579 |    0.625 |      0.5 |
| Wright       |    0.6875 |      0.6 | 0.666667 |        0 |      0.5 |  0.384615 |        0.6 |     0.75 | 0.666667 | 0.571429 |       0.5625 | 0.307692 |     0.75 |      0.4 | 0.666667 | 0.533333 |
| MontiArc     |      0.75 |     0.75 | 0.466667 |      0.5 |        0 |  0.181818 |   0.181818 | 0.538462 | 0.416667 |      0.1 |     0.166667 |     0.25 | 0.416667 | 0.466667 | 0.272727 |     0.25 |
| CommUnity    |  0.666667 | 0.666667 | 0.466667 | 0.384615 | 0.181818 |         0 |   0.333333 | 0.642857 | 0.538462 | 0.272727 |     0.307692 |     0.25 | 0.538462 | 0.466667 | 0.416667 |     0.25 |
| Metropolis   |      0.75 | 0.823529 |   0.5625 |      0.6 | 0.181818 |  0.333333 |          0 | 0.538462 | 0.416667 |      0.1 |     0.307692 | 0.384615 | 0.416667 |   0.5625 | 0.272727 | 0.384615 |
| MECSYCO      |    0.8125 |   0.8125 | 0.428571 |     0.75 | 0.538462 |  0.642857 |   0.538462 |        0 |      0.2 |      0.5 |          0.6 | 0.666667 | 0.714286 | 0.705882 | 0.615385 | 0.666667 |
| DACCOSIM     |  0.882353 | 0.882353 | 0.533333 | 0.666667 | 0.416667 |  0.538462 |   0.416667 |      0.2 |        0 | 0.363636 |          0.5 | 0.571429 | 0.615385 |    0.625 |      0.5 | 0.571429 |
| UMoC++       |    0.8125 |   0.8125 | 0.533333 | 0.571429 |      0.1 |  0.272727 |        0.1 |      0.5 | 0.363636 |        0 |         0.25 | 0.333333 | 0.363636 | 0.533333 |      0.2 | 0.333333 |
| LinguaFranca |  0.777778 | 0.777778 |   0.4375 |   0.5625 | 0.166667 |  0.307692 |   0.307692 |      0.6 |      0.5 |     0.25 |            0 | 0.357143 | 0.384615 |   0.4375 |     0.25 | 0.230769 |
| Reo          |  0.764706 |   0.6875 |      0.5 | 0.307692 |     0.25 |      0.25 |   0.384615 | 0.666667 | 0.571429 | 0.333333 |     0.357143 |        0 | 0.571429 |      0.5 | 0.461538 | 0.307692 |
| Linda        |  0.882353 | 0.882353 | 0.705882 |     0.75 | 0.416667 |  0.538462 |   0.416667 | 0.714286 | 0.615385 | 0.363636 |     0.384615 | 0.571429 |        0 |    0.625 |      0.2 | 0.333333 |
| BIP          |    0.5625 |   0.5625 | 0.631579 |      0.4 | 0.466667 |  0.466667 |     0.5625 | 0.705882 |    0.625 | 0.533333 |       0.4375 |      0.5 |    0.625 |        0 | 0.533333 |      0.4 |
| Manifold     |  0.882353 | 0.882353 |    0.625 | 0.666667 | 0.272727 |  0.416667 |   0.272727 | 0.615385 |      0.5 |      0.2 |         0.25 | 0.461538 |      0.2 | 0.533333 |        0 | 0.181818 |
| ForSyDe      |  0.764706 | 0.764706 |      0.5 | 0.533333 |     0.25 |      0.25 |   0.384615 | 0.666667 | 0.571429 | 0.333333 |     0.230769 | 0.307692 | 0.333333 |      0.4 | 0.181818 |        0 |
