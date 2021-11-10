from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

iris_dataset = load_iris()

X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'])

knn = KNeighborsClassifier(n_neighbors = 1)
knn.fit(X_train, y_train)

print("Test knn set score: {:.2f}".format(knn.score(X_test, y_test)))

clf = DecisionTreeClassifier()
clf = clf.fit(X_train,y_train)

print("Test clf set score: {:.2f}".format(clf.score(X_test, y_test)))
