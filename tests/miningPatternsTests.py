from csvhandler import miningPatterns
import random

mp = miningPatterns.MiningPatterns()

def setup_module(module):
    print("")
    print("Test de la classe MiningPatterns")
    print("Lecture des résultats dans le fichier")
    mp.getMiningResults("DATA/ibert_results_test.csv")

def teardown_module(module):
    print("=== Fin de test de la classe MiningPatterns")

def test_validFrequence():
    """
    On vérifie que la fréquence est égale au nb d'occurrences
    Nb occurrence = longueur d'une ligne - 13 premières colonnes
    Fréquence est dans la col 4
    """
    testValues = random.sample(range(len(mp.results)),10)

    for val in testValues:
        assert int(mp.results[val][4]) == len(mp.results[val]) - 13

def test_validLength():
    """
    On vérifie que la longueur des patterns est valide
    Nb occurrence = longueur d'une ligne - 13 premières colonnes
    Pattern est dans la col 1
    Longueur est dans la col 3
    """
    testValues = random.sample(range(len(mp.results)),10)

    for val in testValues:
        assert len(mp.results[val][1].split(",")) == int(mp.results[val][3])

def test_validStampList():
    """
    On vérifie que la longueur de chaque stampList est valide
    Les stampLists sont dans les colonnes d'indice : results[ligne][13][2]
    La longueur est dans la col 3
    La fréquence (et donc le nb d'occurrences) est dans la col 4
    """
    testValues = random.sample(range(len(mp.results)),10)

    for val in testValues:
        for i in range(int(mp.results[val][4])):
            x = int(mp.results[val][3])
            y = len(mp.results[val][13+i][2].split(","))
            assert  x == y
