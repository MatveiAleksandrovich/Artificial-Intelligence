import numpy as np
import pandas as pd
from sklearn import neighbors, metrics, svm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Getting data from data file.
data = pd.read_csv('car.data')

# Creating features.
X = data[['buying', 'maint', 'safety']].values
# Creating label.
y = data[['class']]
# Converting X data to numpy array
X = np.array(X)

# Converting features into numbers.
Le = LabelEncoder()
for i in range(len(X[0])):
    X[:, i] = Le.fit_transform(X[:, i])


# Converting label into numbers.
label_mapping = {
    'unacc':0,
    'acc':1,
    'good':2,
    'vgood':3
}
y['class'] = y['class'].map(label_mapping)
# Converting to numpy array.
y = np.array(y)

# Check shape of the data.
print(X.shape)
print(y.shape)

# Create model.
knn = neighbors.KNeighborsClassifier()
# Split data to train and test.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# Train the model.
knn.fit(X_train, y_train)
# Get predictions.
prediction = knn.predict(X_test)
# Get an accuracy of the model.
accuracy = metrics.accuracy_score(y_test, prediction)

# Print predictions and accuracy.
print("Predictions:", prediction)
print("Accuracy: ", accuracy)

# Prediction of your own values.
if __name__ == '__main__':
    actual_value = int(input('\n\nPlease, enter the value you want to get prediction about: '))
    print(f'Your value is {actual_value}')
    print(f'Predicted value is {knn.predict(X)[actual_value]}')
