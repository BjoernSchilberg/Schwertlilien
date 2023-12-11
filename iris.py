import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# knn from sklearn
from sklearn import neighbors, datasets
import seaborn as sns


# import some data to play with
iris= datasets.load_iris()

# Auswahl der Merkmale für die Modellierung
# X wird so definiert, dass es nur die ersten zwei Merkmale (Sepallänge und
# Sepalbreite) für jede Blume enthält. Die restlichen zwei Merkmale werden
# ignoriert
# nimmt alle Zeilen (:) und die ersten zwei Spalten (:2) des Datensatzes.
X= iris.data[:,:2]

# Zielvariable festlegen
# Y enthält die Zielvariable, d.h. die Klassifizierung der Iris-Blumen in eine der drei Arten.
Y=iris.target

# Erstellen des k-NN-Klassifikators
#Hier wird ein k-NN-Klassifikator (clf) erstellt. Der Parameter n_neighbors=15
#bedeutet, dass das Modell die 15 nächsten Nachbarn jeder Beobachtung betrachten
#wird, um die Klassifizierung vorzunehmen.

clf= neighbors.KNeighborsClassifier(n_neighbors=3)


# Training des Modells
# Der Klassifikator wird mit den Daten X (Merkmale) und Y (Zielvariable)
# trainiert. Nach diesem Schritt ist das Modell bereit, Vorhersagen über neue,
# unbekannte Daten zu treffen, basierend auf den 15 nächsten Nachbarn.
clf.fit(X,Y)


# Entscheidungsgrenzen visualisieren

# Farb-Gitter zur Visualisierung
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                     np.arange(y_min, y_max, 0.1))

# Klassifizieren Sie jeden Punkt im Meshgrid
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# benutzerdefinierte Farbpalette für die Entscheidungsgrenzen
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])

# Entscheidungsgrenze
plt.figure(figsize=(10, 6))
#plt.contourf(xx, yy, Z, cmap=cmap_light)
plt.contourf(xx, yy, Z, alpha=0.4)

## Farben für die Scatterplot-Punkte
palette_bold = ['#5a2f79', '#3b8e99', '#dbe430']

## Trainingspunkte
sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=iris.target_names[Y], palette=palette_bold)

plt.title("3-Class classification (k = 15)")
plt.xlabel('Sepallänge')
plt.ylabel('Sepalbreite')
plt.show()
