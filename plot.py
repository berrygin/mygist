import matplotlib.pyplot as plt
import pandas as pd

iris = pd.read_csv('iris.csv')
sepal_length = iris['sepal-length']
sepal_width = iris['sepal-width']
target = iris['class']

fig, ax = plt.subplots(figsize=(5, 5))
ax.scatter(sepal_length[target == 'Iris-setosa'], sepal_width[target == 'Iris-setosa'], label='Setosa', c='red', marker='o')
ax.scatter(sepal_length[target == 'Iris-versicolor'], sepal_width[target == 'Iris-versicolor'], label='Versicolor', c='blue', marker='x')
ax.scatter(sepal_length[target == 'Iris-virginica'], sepal_width[target == 'Iris-virginica'], label='Virginica', c='green', marker='^')

ax.set_xlabel('Sepal Length')
ax.set_ylabel('Sepal Width')
ax.set_title('Sepal Length vs Sepal Width')

ax.legend()
plt.show()
