# from sklearn.model_selection import train_test_split
# from sklearn.datasets import load_iris
# from sklearn.neighbors import KNeighborsClassifier

# iris_dataset = load_iris()


# X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state = 0)

# print("X_train shape:", X_train.shape)
# print("y_train shape:", y_train.shape)


# knn = KNeighborsClassifier(n_neighbors = 1)

# import numpy as np
# X_new = np.array([[5, 2.9, 1, 0.2]])
# print("X_new.shape:", X_new.shape)


# import matplotlib.pyplot as plt
# plt.scatter(X_train[:, 1], X_train[:, 3], c = y_train)
# plt.scatter(X_new[:, 1], X_new[:, 3], c = 'red')
# # plt.show()

# knn.fit(X_train, y_train)
# prediction = knn.predict(X_new)

# print("Predicción:", prediction)
# print("Nombre de la Especie Predicha:", iris_dataset['target_names'][prediction])

# y_pred = knn.predict(X_test)
# print("Predicciones para el conjunto de Test:\n", y_pred)
# print("Etiquetas originales de este conjunto:\n", y_test)

# print("Test set score: {:.2f}".format(knn.score(X_test, y_test)))


# 1) Separar los datos en dos conjuntos: train y test.
# 2) Definir un clasificador knn y entrenarlo con los datos de training.
# 3) Evaluar el clasificador con los datos de testing.
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

iris_dataset = load_iris()

X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'])

knn = KNeighborsClassifier(n_neighbors = 1)
knn.fit(X_train, y_train)

print("Test set score: {:.2f}".format(knn.score(X_test, y_test)))



from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
