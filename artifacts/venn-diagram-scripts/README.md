# Generate Venn diagrams of the feature sets of three approaches

1. Clone this repository.
2. Open a cmd/bash in this folder.
3. Run one of the following commands:


## Venn Diagram 1


```bash
py Venn_3.py BCoordLang Linda MontiArc
```
Generates the **first Venn diagram** in the paper.
See sample output diagram in `./BCoordLang_BCOol_MontiArc_venn.svg`.
The console outputs will **contain** which **features are overlapping/unique**.

**Command output:**

> BCoordLang's unique features (6): {'formal language', 'event-scheduling', 'non-intrusive', 'heterogeneous', 'dedicated elements', 'custom properties'}
> BCoordLang's and Linda's common features (0) without MontiArc: set()                                                                          
> BCoordLang's and MontiArc's common features (2) without Linda: {'logical', 'simulation'}
>
> Linda's unique features (2): {'execution', 'name based'}                                                                                      
> Linda's and MontiArc's common features (5) without BCoordLang: {'intrusive', 'homogeneous', 'programming language', 'data-exchange', 'causal'}
>                                                                                                                                             
> MontiArc's unique features (1): {'architecture based'}                                                                                        
> Common features (2): {'discrete event', 'predefined'}


## Venn Diagram 2


```bash
py Venn_3.py BCoordLang DACCOSIM MontiArc
```
Generates the **second Venn diagram** in the paper.
See sample output diagram in `./BCoordLang_DACCOSIM_MontiArc_venn.svg`.
The console outputs will **contain** which **features are overlapping/unique**.

**Command output:**

> BCoordLang's unique features (5): {'custom properties', 'dedicated elements', 'formal language', 'non-intrusive', 'event-scheduling'}
> BCoordLang's and DACCOSIM's common features (1) without MontiArc: {'heterogeneous'}                          
> BCoordLang's and MontiArc's common features (3) without DACCOSIM: {'discrete event', 'logical', 'predefined'}
> 
> DACCOSIM's unique features (5): {'co-simulation', 'hybrid?', 'predefined?', '?', '-'}
> DACCOSIM's and MontiArc's common features (3) without BCoordLang: {'causal', 'intrusive', 'data-exchange'}
> 
> MontiArc's unique features (3): {'programming language', 'homogeneous', 'architecture based'}
> Common features (1): {'simulation'}
