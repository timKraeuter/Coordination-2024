from sklearn.cluster import DBSCAN
import pandas as pd

df = pd.read_excel('../classification.xlsx')
# Lower case to find things more conveniently.
df.columns = map(str.lower, df.columns)

approach_names = ['BCoorLang', 'BCOoL', 'Ptolemy', 'Wright', 'MontiArc', 'CommUnity', 'Metropolis', 'MECSYCO',
                  'DACCOSIM', 'UMoC++', 'LinguaFranca', 'Reo', 'Linda', 'BIP', 'Manifold', 'ForSyDe']

content = {}
for approach in approach_names:
    approach_original = approach
    approach = approach.lower()
    # Filter nan, to lowercase, to array.
    feature_cells = df[approach][df[approach].notnull()].str.lower().values
    feature_set = set()
    for feature_cell in feature_cells:
        # Handle cells that contain multiple features separated by ,
        if feature_cell.find(",") != -1:
            for feature in feature_cell.split(","):
                feature = feature.strip()
                feature_set.add(feature)
        else:
            feature_set.add(feature_cell)
    content[approach_original] = feature_set

distance_matrix = {}


def jaccard_distance(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return 1 - intersection / union


def feature_distance(set1, set2):
    return len(set1 - set2) + len(set2 - set1)


for approach1 in approach_names:
    distance_matrix[approach1] = {}
    for approach2 in approach_names:
        distance_matrix[approach1][approach2] = feature_distance(content[approach1], content[approach2])

distance_matrix = pd.DataFrame(distance_matrix, index=approach_names, columns=approach_names)

print(distance_matrix.to_string())

# Clustering with jaccard (use jaccard_distance in line 44)
# clustering = DBSCAN(eps=0.4, min_samples=2, metric='precomputed')

# Clustering with feature distance (use feature_distance in line 44)
clustering = DBSCAN(eps=5, min_samples=2, metric='precomputed')

clustering.fit(distance_matrix)

labels = clustering.labels_

n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

print("\n")
print("Number of clusters: %d" % n_clusters_)
print("Number of not clustered points: %d" % n_noise_)

clusters = {}
for label in labels:
    if label == -1:
        clusters["Not clustered"] = set()
    else:
        clusters[label] = set()

for idx, label in enumerate(labels):
    if label == -1:
        clusters["Not clustered"].add(approach_names[idx])
    else:
        clusters[label].add(approach_names[idx])

print("Clusters:")
print(clusters)
