from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


def entrenar_modelos(repeticiones):
    iris_dataset = load_iris()
    knn = KNeighborsClassifier(n_neighbors = 1)
    clf = DecisionTreeClassifier()
    fclf = RandomForestClassifier()

    knn_score = 0.0
    clf_score = 0.0
    fclf_score = 0.0

    for _ in range(repeticiones):
        X_train, X_test, y_train, y_test = train_test_split(
            iris_dataset['data'], iris_dataset['target'])
        knn.fit(X_train, y_train)
        clf.fit(X_train,y_train)
        fclf.fit(X_train,y_train)
        knn_score += knn.score(X_test, y_test)
        clf_score += clf.score(X_test, y_test)
        fclf_score += fclf.score(X_test, y_test)

    return knn_score, clf_score, fclf_score


if __name__ == '__main__':
    repeticiones = 100
    knn_score, clf_score, fclf_score = entrenar_modelos(repeticiones)
    print("Test knn set score promedio: {:.2f}".format(knn_score / repeticiones))
    print("Test clf set score promedio: {:.2f}".format(clf_score / repeticiones))
    print("Test fclf set score promedio: {:.2f}".format(fclf_score / repeticiones))
