# Generate Venn diagrams of the feature sets of three approaches

1. Clone this repository.
2. Open a cmd/bash in this folder.
3. Run one of the following commands:

## Venn Diagram: BCoorLang Linda MontiArc

```bash
py Generate_Venn.py BCoorLang Linda MontiArc
```

Generates the **first Venn diagram** in the paper:

![venn diagram 3 approaches](./venn-diagrams/BCoorLang_Linda_MontiArc_venn.svg)).

Venn diagrams with feature labels can be obtained as described in the next section.

## Venn Diagram: BCoorLang DACCOSIM MontiArc

```bash
py Generate_Venn.py BCoorLang DACCOSIM MontiArc
```

Generates the **second Venn diagram** in the paper:

![venn diagram 3 approaches](./venn-diagrams/BCoorLang_DACCOSIM_MontiArc_venn.svg)).

Venn diagrams with feature labels can be obtained as described in the next section.

## Venn Diagrams with feature labels

To obtain venn diagrams with feature labels follow the same procedure as before but use one of the commands below:

### Venn Diagram: BCoorLang Linda MontiArc

**Script:**

```bash
py Generate_Venn_With_Labels.py BCoorLang Linda MontiArc
```

**Output:**

![venn diagram 3 approaches with feature labels](./venn-diagrams/BCoorLang_Linda_MontiArc_venn_labeled.svg)).

### Venn Diagram: BCoorLang DACCOSIM MontiArc

**Script:**

```bash
py Generate_Venn_With_Labels.py BCoorLang DACCOSIM MontiArc
```

**Output:**

![venn diagram 3 approaches with feature labels](./venn-diagrams/BCoorLang_DACCOSIM_MontiArc_venn_labeled.svg)).

## Equivalent UpSet plots

More information about [UpSet plots](https://upset.app/).
Follow the same procedure as before but use one of the new commands below to generate UpSet plots:

### UpSet plot: BCoorLang Linda MontiArc

**Script:**

```bash
py Generate_Upset.py BCoorLang Linda MontiArc
```

**Output:**

![upset plot 3 approaches](./upset-plots/BCoorLang_Linda_MontiArc_upset.svg)).

### UpSet plot: BCoorLang DACCOSIM MontiArc

**Script:**

```bash
py Generate_Upset.py BCoorLang DACCOSIM MontiArc
```

**Output:**

![upset plot 3 approaches](./upset-plots/BCoorLang_DACCOSIM_MontiArc_upset.svg)).

### UpSet plot: Custom approaches

UpSet plots make most sense for more than three approaches. You can add as many approaches as arguments as you want.

**Script:**

```bash
py Generate_Upset.py BCoorLang Linda MontiArc DACCOSIM
```

**Output:**

![upset plot 4 approaches](./upset-plots/BCoorLang_Linda_MontiArc_DACCOSIM_upset.svg)).

## Clustering

We clustered the approaches using the [DBSCAN](https://en.wikipedia.org/wiki/DBSCAN) algorithm with
the [Jaccard distance](https://en.wikipedia.org/wiki/Jaccard_index#Overview) metric.
You can find a table with the calculated distances later.

**Parameters:**

- Number of minimum samples in a cluster = two (`min_samples=2`)
- Maximum distance between two samples to be considered neighbors (`eps=0.34`).
- Precomputed distance metric given by the Jaccard_distance (`metric='precomputed'`)

### Clustering results

The results of the clustering are the following:

```
Number of clusters: 3
Number of not clustered points: 1
Clusters:                        
0: {'BCoorLang', 'BCOoL'}
1: {'UMoC++', 'Metropolis', 'LinguaFranca', 'Manifold', 'Linda', 'ForSyDe', 'MontiArc', 'CommUnity', 'Reo', 'BIP', 'Wright'}
2: {'DACCOSIM', 'MECSYCO'}
Not clustered: {'Ptolemy'}
```

You can run the following script to reproduce the results:

```bash
py Cluster_approaches.py
```

The distance matrix together with the clustering visualized in the following scatter plot (see `Scatter_approachey_by_distance.py`):

![distance scatter plot](distance/approach_scatter.svg)).

The plot approximates the position of each approach relative to the others by using the distance matrix.
It cannot be exact but paints a good overall picture.

### Jaccard distance matrix (clustering input)

Tabel which shows the **Jaccard distance** between the feature sets.
This data is the precomputed input for the clustering (see `Calculate_distance_matrix.py`).

|              | BCoorLang |    BCOoL |  Ptolemy |   Wright | MontiArc | CommUnity | Metropolis |  MECSYCO | DACCOSIM |   UMoC++ | LinguaFranca |      Reo |    Linda |      BIP | Manifold |  ForSyDe |
|:-------------|----------:|---------:|---------:|---------:|---------:|----------:|-----------:|---------:|---------:|---------:|-------------:|---------:|---------:|---------:|---------:|---------:|
| BCoorLang    |         0 | 0.333333 |    0.625 |      0.6 |     0.75 |  0.571429 |   0.666667 | 0.733333 |   0.8125 | 0.733333 |     0.777778 |   0.6875 | 0.882353 |   0.5625 |   0.8125 | 0.764706 |
| BCOoL        |  0.333333 |        0 |    0.625 |      0.5 |     0.75 |  0.571429 |       0.75 | 0.733333 |   0.8125 | 0.733333 |     0.777778 |      0.6 | 0.882353 |   0.5625 |   0.8125 | 0.764706 |
| Ptolemy      |     0.625 |    0.625 |        0 | 0.647059 | 0.533333 |  0.428571 |   0.533333 | 0.384615 |      0.5 |      0.5 |          0.5 | 0.466667 | 0.764706 | 0.529412 |      0.6 |   0.5625 |
| Wright       |       0.6 |      0.5 | 0.647059 |        0 |      0.6 |  0.384615 |        0.6 |     0.75 | 0.666667 | 0.571429 |     0.647059 | 0.307692 | 0.823529 | 0.285714 | 0.666667 |    0.625 |
| MontiArc     |      0.75 |     0.75 | 0.533333 |      0.6 |        0 |  0.333333 |   0.333333 | 0.642857 | 0.538462 | 0.272727 |     0.166667 | 0.384615 | 0.416667 | 0.466667 | 0.416667 |     0.25 |
| CommUnity    |  0.571429 | 0.571429 | 0.428571 | 0.384615 | 0.333333 |         0 |   0.333333 | 0.642857 | 0.538462 | 0.272727 |     0.428571 |     0.25 | 0.642857 | 0.357143 | 0.416667 | 0.384615 |
| Metropolis   |  0.666667 |     0.75 | 0.533333 |      0.6 | 0.333333 |  0.333333 |          0 | 0.538462 | 0.416667 |      0.1 |     0.428571 | 0.384615 | 0.538462 | 0.466667 | 0.272727 |      0.5 |
| MECSYCO      |  0.733333 | 0.733333 | 0.384615 |     0.75 | 0.642857 |  0.642857 |   0.538462 |        0 |      0.2 |      0.5 |       0.6875 | 0.666667 |      0.8 |    0.625 | 0.615385 |     0.75 |
| DACCOSIM     |    0.8125 |   0.8125 |      0.5 | 0.666667 | 0.538462 |  0.538462 |   0.416667 |      0.2 |        0 | 0.363636 |          0.6 | 0.571429 | 0.714286 | 0.533333 |      0.5 | 0.666667 |
| UMoC++       |  0.733333 | 0.733333 |      0.5 | 0.571429 | 0.272727 |  0.272727 |        0.1 |      0.5 | 0.363636 |        0 |     0.384615 | 0.333333 |      0.5 | 0.428571 |      0.2 | 0.461538 |
| LinguaFranca |  0.777778 | 0.777778 |      0.5 | 0.647059 | 0.166667 |  0.428571 |   0.428571 |   0.6875 |      0.6 | 0.384615 |            0 | 0.466667 | 0.384615 |   0.4375 | 0.384615 | 0.230769 |
| Reo          |    0.6875 |      0.6 | 0.466667 | 0.307692 | 0.384615 |      0.25 |   0.384615 | 0.666667 | 0.571429 | 0.333333 |     0.466667 |        0 | 0.666667 |      0.4 | 0.461538 | 0.428571 |
| Linda        |  0.882353 | 0.882353 | 0.764706 | 0.823529 | 0.416667 |  0.642857 |   0.538462 |      0.8 | 0.714286 |      0.5 |     0.384615 | 0.666667 |        0 |    0.625 | 0.363636 | 0.333333 |
| BIP          |    0.5625 |   0.5625 | 0.529412 | 0.285714 | 0.466667 |  0.357143 |   0.466667 |    0.625 | 0.533333 | 0.428571 |       0.4375 |      0.4 |    0.625 |        0 | 0.428571 |      0.4 |
| Manifold     |    0.8125 |   0.8125 |      0.6 | 0.666667 | 0.416667 |  0.416667 |   0.272727 | 0.615385 |      0.5 |      0.2 |     0.384615 | 0.461538 | 0.363636 | 0.428571 |        0 | 0.333333 |
| ForSyDe      |  0.764706 | 0.764706 |   0.5625 |    0.625 |     0.25 |  0.384615 |        0.5 |     0.75 | 0.666667 | 0.461538 |     0.230769 | 0.428571 | 0.333333 |      0.4 | 0.333333 |        0 |
