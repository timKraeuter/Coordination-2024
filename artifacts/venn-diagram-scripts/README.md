# Generate Venn diagrams of the feature sets of three approaches

1. Clone this repository.
2. Open a cmd/bash in this folder.
3. Run one of the following commands:


## Venn Diagram 1


```bash
py Venn_3.py BCoordLang Linda MontiArc
```
Generates the **first Venn diagram** in the paper (see output [diagram](./BCoordLang_Linda_MontiArc_venn.svg)).
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
Generates the **second Venn diagram** in the paper (see output [diagram](./BCoordLang_DACCOSIM_MontiArc_venn.svg)).
The console outputs will **contain** which **features are overlapping/unique**.

**Command output:**

> BCoordLang's unique features (6): {'heterogeneous', 'non-intrusive', 'event-scheduling', 'formal language', 'custom properties', 'dedicated elements'}    
> BCoordLang's and DACCOSIM's common features (0) without MontiArc: set()    
> BCoordLang's and MontiArc's common features (2) without DACCOSIM: {'discrete event', 'logical'} 
> 
> DACCOSIM's unique features (3): {'hybrid', 'co-simulation', 'name based'}   
> DACCOSIM's and MontiArc's common features (4) without BCoordLang: {'causal', 'data-exchange', 'intrusive', 'homogeneous'} 
> 
> MontiArc's unique features (2): {'architecture based', 'programming language'} 
> Common features (2): {'predefined', 'simulation'} 
