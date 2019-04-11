import numpy as np
from knn import KNearestNick
from sklearn.datasets import load_iris

d = load_iris()
X = d['data']
y = d['target']

test_point = np.array([[3, 5, 2, 4]])

model = KNearestNick(k=5, distance='euclidean')
model.fit(X, y)

print(model)
print('Probabilites:', model.predict_proba(test_point))
print(model.predict(test_point))
