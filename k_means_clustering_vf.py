import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

import numpy as np
from sklearn.cluster import KMeans

from random import random

X = np.array([
[random(), random()],
[random(), random()],
[random(), random()],
[random(), random()],
[random(), random()],
[random(), random()],
[random(), random()],
[random(), random()],
[random(), random()],
[random(), random()],
[random(), random()],
[random(), random()]])


plt.scatter(X[:,0], X[:,1], s=150)
plt.show()

class K_Means:
	def __init__(self, k=3, tol=0.001, max_iter=300):
		self.k = k
		self.tol = tol
		self.max_iter = max_iter

	def fit(self, data):
		self.centroids = {}

		for i in range(self.k):
			self.centroids[i] = data[i]

		for i in range(self.max_iter):
			self.classifications = {}

			for i in range(self.k):
				self.classifications[i] = []

			for featureset in data:
				distances = [np.linalg.norm(featureset-self.centroids[centroid]) for centroid in self.centroids]
				classification = distances.index(min(distances))
				self.classifications[classification].append(featureset)

			prev_centroids = dict(self.centroids)

			for classification in self.classifications:
				pass
				self.centroids[classification] = np.average(self.classifications[classification], axis=0)

			optimized = True

			for c in self.centroids:
				original_centroid = prev_centroids[c]
				current_centroid = self.centroids[c]
				if np.sum((current_centroid - original_centroid)/original_centroid*100.0) > self.tol:
					optimized = False

			if optimized:
				break

	def predict(self, data):
		distances = [np.linalg.norm(data-self.centroids[centroid]) for centroid in self.centroids]
		classifications = distances.index(min(distances))
		return classifications

clf = K_Means()
clf.fit(X)

colors = 10*["g", "r", "c", "b", "k"]

for centroid in clf.centroids:
	plt.scatter(clf.centroids[centroid][0], clf.centroids[centroid][1],
				marker="o", color="k", s=150, linewidths=5)

for classification in clf.classifications:
	color = colors[classification]
	for featureset in clf.classifications[classification]:
		plt.scatter(featureset[0], featureset[1], marker="x", color=color, s=150, linewidths=5)

plt.show()