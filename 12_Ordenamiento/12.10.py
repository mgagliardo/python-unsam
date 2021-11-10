import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris


def get_iris_dataframe():
    iris_dataset = load_iris()
    iris_dataframe = pd.DataFrame(iris_dataset['data'], columns = iris_dataset.feature_names)
    iris_dataframe['target'] = iris_dataset['target']
    return iris_dataframe

def graficar(dataframe, key):
    sns.pairplot(dataframe, hue=key)
    plt.show()

if __name__ == '__main__':
    graficar(get_iris_dataframe(), 'target')
