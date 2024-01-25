import matplotlib.pyplot as plt
from sklearn.manifold import MDS
import pandas as pd
from sklearn.cluster import DBSCAN

# Load distance matrix
distance_matrix = pd.read_excel("./distance/distances.xlsx")

# Clustering
clustering = DBSCAN(eps=0.34, min_samples=2, metric='precomputed')
clustering.fit(distance_matrix)
clusters = clustering.labels_

# Create MDS instance
mds = MDS(n_components=2, dissimilarity='precomputed', random_state=42, normalized_stress="auto")

# Fit the model to the distance matrix and transform the data to the lower-dimensional space
mds_result = mds.fit_transform(distance_matrix)

# Scatter plot with colored points based on clusters
for cluster in set(clusters):
    indices = [i for i, c in enumerate(clusters) if c == cluster]
    if cluster == -1:
        plt.scatter(mds_result[indices, 0], mds_result[indices, 1], label='Unclustered')
    else:
        plt.scatter(mds_result[indices, 0], mds_result[indices, 1], label=f'Cluster {cluster}')

# Add labels to each point (optional)
for i, label in enumerate(distance_matrix.columns):
    plt.annotate(label, (mds_result[i, 0], mds_result[i, 1]), ha='right', va='bottom')

# Add legend
plt.legend()

# Save and show the plot
# plt.title('Feature distance & clustering')
plt.savefig("../../images/approach_scatter.pdf", format="pdf")
plt.savefig("./distance/approach_scatter.svg", format="svg")
plt.show()
