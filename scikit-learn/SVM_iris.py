from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

# load data
iris = datasets.load_iris()

# split data in features and labels
X = iris.data
y = iris.target


classes = ['Iris Setosa', 'Iris Versicolour', 'Iris Virginica']
print(X.shape)
print(y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = svm.SVC()
model.fit(X_train, y_train)

print(model)
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print(f'Predictions: {predictions}')
print(f'Actual: {y_test}')
print(f'Accuracy: {accuracy}')
