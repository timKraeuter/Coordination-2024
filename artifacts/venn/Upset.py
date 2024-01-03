from upsetplot import plot, from_contents
from matplotlib import pyplot as plt

mammals = ["Cat", "Dog", "Horse", "Sheep", "Pig", "Cattle", "Rhinoceros", "Moose"]
herbivores = ["Horse", "Sheep", "Cattle", "Moose", "Rhinoceros"]
domesticated = ["Dog", "Chicken", "Horse", "Sheep", "Pig", "Cattle", "Duck"]

animals = from_contents(
    {"mammal": mammals, "herbivore": herbivores, "domesticated": domesticated}
)

plot(animals)
plt.savefig("upsetplot.pdf", format="pdf", bbox_inches="tight")
plt.show()
