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

The console outputs will **contain** which **features are overlapping/unique**.

**Command output:**

> BCoorLang's unique features (6): {'formal language', 'event-scheduling', 'non-intrusive', 'heterogeneous', 'dedicated elements', 'custom properties'}    
> BCoorLang's and Linda's common features (0) without MontiArc: set()                                                                          
> BCoorLang's and MontiArc's common features (2) without Linda: {'logical', 'simulation'}
>
> Linda's unique features (2): {'execution', 'name based'}                                                                                      
> Linda's and MontiArc's common features (5) without BCoorLang: {'intrusive', 'homogeneous', 'programming language', 'data-exchange', 'causal'}
>                                                                                                                                             
> MontiArc's unique features (1): {'architecture based'}                                                                                        
> Common features (2): {'discrete event', 'predefined'}


## Venn Diagram: BCoorLang DACCOSIM MontiArc


```bash
py Generate_Venn.py BCoorLang DACCOSIM MontiArc
```
Generates the **second Venn diagram** in the paper:

![diagram](./venn-diagrams/BCoorLang_DACCOSIM_MontiArc_venn.svg)).

The console outputs will **contain** which **features are overlapping/unique**.

**Command output:**

>BCoorLang's unique features (6): {'non-intrusive', 'custom properties', 'formal language', 'heterogeneous', 'dedicated elements', 'event-scheduling'}      
>BCoorLang's and DACCOSIM's common features (0) without MontiArc: set()       
>BCoorLang's and MontiArc's common features (2) without DACCOSIM: {'discrete event', 'logical'}
>
>DACCOSIM's unique features (4): {'name based', 'a-causal', 'co-simulation', 'hybrid'}    
>DACCOSIM's and MontiArc's common features (4) without BCoorLang: {'data-exchange', 'intrusive', 'homogeneous', 'causal'}
>
>MontiArc's unique features (2): {'programming language', 'architecture based'}     
>Common features (2): {'simulation', 'predefined'}

## Venn Diagrams with feature labels

Follow the same procedure as before but use one of the new commands below:

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

UpSet plots make most sense for more than three approaches. You can add as many approac

**Script:**

```bash
py Generate_Upset.py BCoorLang Linda MontiArc DACCOSIM
```

**Output:**

![diagram](./upset-plots/BCoorLang_Linda_MontiArc_DACCOSIM_upset.svg)).