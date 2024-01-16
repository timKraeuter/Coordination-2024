import os

from sympy.utilities.iterables import multiset_permutations

approaches_string = (
    "BCoorLang BCOoL Ptolemy Wright MontiArc CommUnity Metropolis MECSYCO DACCOSIM UMoC++ LinguaFranca Reo "
    "Linda BIP Manifold ForSyDe")

approaches = approaches_string.split(" ")

permutations = set()
for permutation in multiset_permutations(approaches, 3):
    permutations.add(frozenset(permutation))

for i in permutations:
    args = " ".join(i)
    print("")
    print(args)
    os.system("Venn_3.py " + args)
