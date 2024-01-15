# Generate Venn diagrams of the feature sets of three approaches

1. Clone this repository.
2. Open a cmd/bash in this folder.
3. Run one of the following commands:


## Venn Diagram 1


```bash
py Venn_3.py BCoorLang Linda MontiArc
```
Generates the **first Venn diagram** in the paper (see output [diagram](./BCoordLang_Linda_MontiArc_venn.svg)).
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


## Venn Diagram 2


```bash
py Venn_3.py BCoorLang DACCOSIM MontiArc
```
Generates the **second Venn diagram** in the paper (see output [diagram](./BCoordLang_DACCOSIM_MontiArc_venn.svg)).
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
