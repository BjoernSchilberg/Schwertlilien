from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

# Laden des Iris-Datensatzes
iris = load_iris()
X, y = iris.data, iris.target

# Training des Random Forest Classifiers
rf = RandomForestClassifier(n_estimators=3, random_state=42)
rf.fit(X, y)

# Visualisierung aller Entscheidungsbäume im Random Forest und Speicherung als PNG
for i, tree in enumerate(rf.estimators_):
    plt.figure(figsize=(20, 10))
    plot_tree(
        tree,
        filled=True,
        feature_names=iris.feature_names,
        class_names=iris.target_names,
    )
    plt.title(f"Visualisierung des Entscheidungsbaums {i+1} des Random Forest")
    # Speichern als PNG
    plt.savefig(f"entscheidungsbaum_{i+1}.png")
    plt.close()  # Schließen der Figur, um Speicher zu sparen
