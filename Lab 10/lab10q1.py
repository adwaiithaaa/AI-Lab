import numpy as np
import pandas as pd

# Load CSV (no header)
data = pd.read_csv("cities.csv", header=None)

# Take first 2 columns as coordinates
points = data.iloc[:, :2].values

k = 3  # number of airports

# Initialize centroids randomly
np.random.seed(42)
centroids = points[np.random.choice(len(points), k, replace=False)]

# Function to compute squared distance
def compute_distance(a, b):
    return np.sum((a - b) ** 2)

# Assign clusters
def assign_clusters(points, centroids):
    clusters = []
    for p in points:
        distances = [compute_distance(p, c) for c in centroids]
        clusters.append(np.argmin(distances))
    return np.array(clusters)

# Update centroids
def update_centroids(points, clusters, k):
    new_centroids = []
    for i in range(k):
        cluster_points = points[clusters == i]
        
        if len(cluster_points) > 0:
            new_centroids.append(cluster_points.mean(axis=0))
        else:
            new_centroids.append(points[np.random.randint(len(points))])
    
    return np.array(new_centroids)

# Compute loss
def compute_loss(points, centroids, clusters):
    loss = 0
    for i, p in enumerate(points):
        c = centroids[clusters[i]]
        loss += compute_distance(p, c)
    return loss

# Training loop
for i in range(100):
    clusters = assign_clusters(points, centroids)
    new_centroids = update_centroids(points, clusters, k)
    
    if np.allclose(centroids, new_centroids):
        break
    
    centroids = new_centroids

# Results
final_loss = compute_loss(points, centroids, clusters)

print("Final Airport Locations:")
print(centroids)

print("\nCluster assignment:")
print(clusters)

print("\nTotal squared distance:")
print(final_loss)