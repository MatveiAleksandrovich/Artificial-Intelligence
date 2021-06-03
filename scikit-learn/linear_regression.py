from sklearn import datasets
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt

boston = datasets.load_boston()

# Getting features / labels
X = boston.data
y = boston.target

print(f'X-shape is\n{X.shape}\n')
print(f'y-shape is\n{y.shape}')

regression = linear_model.LinearRegression()

plt.scatter(X.T[5], y)
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# train
model = regression.fit(X_train, y_train)
predictions = model.predict(X_test)
print(f'Predictions: {predictions}')
print(f'R^2 value: {regression.score(X, y)}')


