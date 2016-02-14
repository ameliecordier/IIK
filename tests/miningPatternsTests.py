from datahandler import miningPatterns
import random


class TestMiningPatterns:

    patterns = []

    @classmethod
    def setup_class(cls):
        print("")
        print("Test de la classe MiningPatterns")
        print("Lecture des résultats dans le fichier")
        filename = "DATA/Debussy_Syrinx_out1.csv"
        firstSize = 13
        packSize = 11
        cls.patterns = list(miningPatterns.readRows(filename, firstSize, packSize))
        for line in cls.patterns:
            line.convertDataToInt()

    @classmethod
    def teardown_class(cls):
        print("=== Fin de test de la classe MiningPatterns")

    def test_validFreq(cls):
        """
        Vérifie que la fréquence est égale au nb d'occurrences
        """
        testValues = random.sample(range(len(cls.patterns)),10)
        for val in testValues:
            assert cls.patterns[val].infos.get("freq") == cls.patterns[val].getNbOccs()

    def test_validPatternLengthv(cls):
        """
        Vérifie que la longueur annoncée du pattern correspond
        bien à la longueur réelle
        """
        testSet = random.sample(cls.patterns,10)
        for pattern in testSet:
            yield cls.validPattern, pattern

    def validPattern(self, p):
        assert len(p.infos["motif Lily"].split(',')) == p.infos["long"]


"""    def test_validStampList(cls):
        """
   """     Vérifie que la longueur de chaque occurrence est valide
        """
      """  testValues = random.sample(range(len(cls.patterns)),10)
        for val in testValues:
            for occ in cls.patterns[val].occ:
                x = (cls.patterns[val].infos["long"])
                y = (len(occ["Stamps list"].split(",")))
                print(x, y)
                assert x == y
""