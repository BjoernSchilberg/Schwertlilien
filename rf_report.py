from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Laden des Iris-Datensatzes
iris = load_iris()
X, y = iris.data, iris.target

# Aufteilen des Datensatzes in Trainings- und Testdatensätze
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Training des Random Forest Classifiers
rf = RandomForestClassifier(n_estimators=3, random_state=42)
rf.fit(X_train, y_train)

# Vorhersagen auf dem Testdatensatz
y_pred = rf.predict(X_test)

# Erstellung des Klassifikationsberichts
report = classification_report(y_test, y_pred, target_names=iris.target_names)
print(report)

