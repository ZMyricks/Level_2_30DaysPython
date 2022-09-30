# Import machine learning library
# spcific class for kNN
from sklearn.neighbors import KNeighborsClassifier
# specific class to train the model data
from sklearn.model_selection import train_test_split
# load the data set from sklearn
from sklearn.datasets import load_iris

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

knn = KNeighborsClassifier(n_neighbors=7)

knn.fit(X_train, y_train)

# Calculate the accuracy of the model
print(knn.score(X_test, y_test))
