import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

boundary_points = np.array([
    [5.9, 3.0, 4.8, 1.8],
    [6.5, 3.0, 5.5, 2.0],
    [5.5, 2.5, 4.0, 1.3]
])
boundary_labels = np.array([1, 2, 1])

X_test_modified = np.vstack([X_test, boundary_points])
y_test_modified = np.hstack([y_test, boundary_labels])

y_pred_modified = knn.predict(X_test_modified)

print("\n--- Correct Predictions ---")
for i in range(len(y_test_modified)):
    if y_pred_modified[i] == y_test_modified[i]:
        print(f"Sample {i}: Predicted = {iris.target_names[y_pred_modified[i]]}, Actual = {iris.target_names[y_test_modified[i]]}")

print("\n--- Wrong Predictions ---")
for i in range(len(y_test_modified)):
    if y_pred_modified[i] != y_test_modified[i]:
        print(f"Sample {i}: Predicted = {iris.target_names[y_pred_modified[i]]}, Actual = {iris.target_names[y_test_modified[i]]}")

accuracy = np.mean(y_pred_modified == y_test_modified)
print(f"\nModel Accuracy: {accuracy*100:.2f}%")
