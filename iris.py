import pandas as pd


def load_dataset_iris():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
    return pd.read_csv(url, names=names)

if __name__ == '__main__':
    df = load_dataset_iris()
    csv = df.to_csv(index=False)
    with open('iris.csv', 'w') as f:
        f.write(csv)