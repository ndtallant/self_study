import numpy as np
from scipy.spatial.distance import cdist 


class KNearestNick:
    '''Currently only predicts one point at a time.'''
    
    def __init__(self, k, distance='euclidean'):
        self.k = k
        self.distance = distance

    # TODO: Set properties

    def fit(self, X, y):
        '''Stores a reference to training data, will add ndarray verification
        later.''' 
        self.X_train = X
        self.y_train = y

    def predict_proba(self, X):
        '''Predicts probabilites for each class'''
        _, y = self.get_neighbors(X)
        unique, counts = np.unique(y, return_counts=True)
        return unique, (counts / sum(counts))

    def predict(self, X):
        '''Chooses class with highest probability'''
        classes, probabilities = self.predict_proba(X)
        return classes[np.argsort(probabilities)[-1]]
    
    def get_neighbors(self, X):
        '''Returns k nearest neighbors of given X'''
        array_index = np.argsort(self._get_distance(X))[0, 0:self.k]
        return self.X_train[array_index], self.y_train[array_index]

    def _get_distance(self, X):
        '''Computes Euclidean distance of X to X_train'''
        return cdist(X, self.X_train, self.distance)

    def __repr__(self):
        return f'KNN with {self.k} neighbors and {self.distance} distance.'
