# Automatische Datenanalyse

- [Automatische Datenanalyse](#automatische-datenanalyse)
  - [Am Beispiel des Iris Datensatz](#am-beispiel-des-iris-datensatz)
    - [Merkmale des Iris-Datensatzes](#merkmale-des-iris-datensatzes)
    - [Warum eignet sich der Datensatz gut?](#warum-eignet-sich-der-datensatz-gut)
  - [kNN (k-Nächste-Nachbarn-Modell)](#knn-k-nächste-nachbarn-modell)
    - [Automatische Datenanalyse mittels Orange3 (kNN)](#automatische-datenanalyse-mittels-orange3-knn)
    - [Automatische Datenanalyse mittels Python](#automatische-datenanalyse-mittels-python)
  - [Random Forest](#random-forest)
    - [Automatische Datenanalyse mittels Orange3 (Random Forest)](#automatische-datenanalyse-mittels-orange3-random-forest)
    - [Automatische Datenanalyse mittels Python (kNN)](#automatische-datenanalyse-mittels-python-knn)
  - [Link-Halde](#link-halde)

## Am Beispiel des Iris Datensatz

<https://de.wikipedia.org/wiki/Portal:Statistik/Datens%C3%A4tze#Iris>

Beim Iris Datensatz, handelt es sich um einen Datensatz mit 150 Beobachtungen
von 4 Attributen der Blüte von [Schwertlilien](https://de.wikipedia.org/wiki/Schwertlilien).

Gemessen wurden dabei jeweils die Breite (`width`) und die Länge (`length`) des
Kelchblatts (**Sepalum**) sowie des Kronblatts (**Petalum**) in Zentimeter (cm). Des
weiteren ist für jeden Datensatz die Art der Schwertlilie ([Iris setosa](https://de.wikipedia.org/wiki/Borsten-Schwertlilie), [Iris
virginica](https://en.wikipedia.org/wiki/Iris_virginica) oder [Iris versicolor](https://de.wikipedia.org/wiki/Verschiedenfarbige_Schwertlilie)) angegeben. Für jede der 3 Schwertlilienarten liegen 50
Datensätze vor.

### Merkmale des Iris-Datensatzes

- Datenpunkte: 150
- Klassen: 3 (Iris Setosa, Iris Versicolour, Iris Virginica)
- Merkmale pro Datenpunkt: 4 (Sepallänge, Sepalbreite, Petallänge, Petalbreite)
- Problemart: Klassifikation

### Warum eignet sich der Datensatz gut?

- Übersichtlichkeit: Nur 4 Merkmale und 3 Klassen.
- Verständlichkeit: Leicht zu visualisieren, da die Merkmale klare biologische Bedeutungen haben.
- Standard-Beispiel: Häufig in Lehrmaterialien verwendet, was den Zugang zu zusätzlichen Ressourcen erleichtert.

## kNN (k-Nächste-Nachbarn-Modell)

Das k-Nächste-Nachbarn-Modell entscheidet auf Basis der Zielmerkmale der
Datenpunkte mit den ähnlichsten Merkmalsausprägungen (die nächsten Nachbarn)

- Einstieg: [Biberaufgabe 2020: Neues Haus](neues_haus.pdf)

### Automatische Datenanalyse mittels Orange3 (kNN)

- <https://orange3.readthedocs.io/projects/orange-visual-programming/en/latest/widgets/model/knn.html>
- [Orange3 Hilfekarte (pdf)](orange3_hilfekarte_knn.pdf)

![Automatische Datenanalyse mittels Orange3 und kNN](orange3_iris_knn.png)

### Automatische Datenanalyse mittels Python

Mittels scikit-learn und Nearest Neighbors Classification (KNeighborsClassifier)

- <https://scikit-learn.org/stable/modules/neighbors.html#classification>
- <https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier>

Benötigte Biblotheken installieren

```shell
pip install matplotlib seaborn scikit-learn numpy
```

Ausführen

```python
python knn.py
```

k=3             |  k=15
:-------------------------:|:-------------------------:
![Automatische Datenanalyse mittels Python und kNN: K=3 ](knn_3.png) | ![Automatische Datenanalyse mittels Python und kNN: K=15 ](knn_15.png)

## Random Forest

Random Forest Modelle enthalten mehrere Entscheidungsbäume und stimmen im
Mehrheitsverfahren ab.

### Automatische Datenanalyse mittels Orange3 (Random Forest)

- Einstieg: <https://www.youtube.com/watch?v=gSQsFIMcA8A>
- <https://orangedatamining.com/blog/pythagorean-trees-and-forests/>
- [Orange3 Hilfekarte (pdf)](orange3_hilfekarte_random_forest.pdf)

![Automatische Datenanalyse mittels Orange3 und Random Forest](orange3_iris_random_forest.png)

### Automatische Datenanalyse mittels Python (kNN)

```python
python rf.py
```

## Link-Halde

<https://www.wanderinformatiker.at/unipages/general/iris.html>
