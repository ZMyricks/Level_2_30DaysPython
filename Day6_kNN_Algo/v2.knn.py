# Import machine learning library
# spcific class for kNN
from sklearn.neighbors import KNeighborsClassifier
# specific class to train the model data
from sklearn.model_selection import train_test_split
# load the data set from sklearn
from sklearn.datasets import load_iris
# data viz library
import matplotlib.pyplot as plt
# library for math and scientific functions
import numpy as np

# Loading data
# The iris dataset = multi-class classification dataset.
irisData = load_iris()
'''Classes: 3
Samples per class: 50
Samples total: 150
Dimensionality: 4
Features: real, positive'''

# Create feature and target arrays
X = irisData.data
y = irisData.target


# Split into training and test set
X_train, X_test, y_train, y_test = train_test_split(
             X, y, test_size = 0.2, random_state=42)

neighbors = np.arange(1, 9)
train_accuracy = np.empty(len(neighbors))
test_accuracy = np.empty(len(neighbors))

# Loop over K values
for i, k in enumerate(neighbors):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)

    # Compute training and test data accuracy
    train_accuracy[i] = knn.score(X_train, y_train)
    test_accuracy[i] = knn.score(X_test, y_test)

# plot to see the k-value for which we have high accuracy
plt.plot(neighbors, test_accuracy, label = 'Testing dataset Accuracy')
plt.plot(neighbors, train_accuracy, label = 'Training dataset Accuracy')

plt.legend()
plt.xlabel('n_neighbors')
plt.ylabel('Accuracy')
plt.show()
