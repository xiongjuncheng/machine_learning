#!/usr/bin/python
from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)
X = [[5.8,2.9,5.2,2.1]]
predict = clf.predict(X)
print(predict)
