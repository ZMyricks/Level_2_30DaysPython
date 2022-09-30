# import libraries
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# import data
dog_costume_data = pd.read_csv("30DaysofPythonChallenge/day6_K_nearest_neighbors/dog_costume.csv")

# check data
print(dog_costume_data.head())

X = dog_costume_data['Weight'].array.reshape(-1,1)
y = dog_costume_data['Costume Size']

# Splitting data into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state= 100)

'''
KNeighborsClassifier in Sklearn

KNeighborsClassifier(
    n_neighbors=5,          # The number of neighbours to consider
    weights='uniform',      # How to weight distances
    algorithm='auto',       # Algorithm to compute the neighbours
    leaf_size=30,           # The leaf size to speed up searches
    p=2,                    # The power parameter for the Minkowski metric
    metric='minkowski',     # The type of distance to use
    metric_params=None,     # Keyword arguments for the metric function
    n_jobs=None             # How many parallel jobs to run
)
'''

# Creating a classifier object in sklearn
clf = KNeighborsClassifier(n_neighbors=3, metric= 'euclidean')

# Fitting our model
clf.fit(X_train, y_train)


# general predictions
predictions = clf.predict(X_test)
print(predictions)

# specific predictions
predictions = clf.predict([[20]])
print(predictions)

# Measuring the accuracy of our model
print(accuracy_score(y_test, predictions))
