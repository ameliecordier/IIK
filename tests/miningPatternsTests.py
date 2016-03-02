#-*- coding: utf-8 -*-
import random

from nose.tools import assert_equals

from datahandler import miningPatterns


class TestMiningPatterns:

    patterns = []
    nbTests = 15

    @classmethod
    def setup_class(cls):
        print("")
        print("Test de la classe MiningPatterns")
        print("Lecture des résultats dans le fichier")
        filename = "DATA/Ibert_Entracte_out1.csv"
        firstSize = 13
        packSize = 11
        cls.patterns = list(miningPatterns.readRows(filename, firstSize, packSize))


    @classmethod
    def teardown_class(cls):
        print("=== Fin de test de la classe MiningPatterns")


    def test_validFreq(cls):
        """
        Vérifie que la fréquence annoncée est égale au nb d'occurrences
        """
        def validFreq(p):
            assert p.infos.get("freq") == p.getNbOccs()


        testSet = random.sample(cls.patterns,cls.nbTests)
        for pattern in testSet:
            yield validFreq, pattern


    def test_validPatternLength(cls):
        """
        Vérifie que la longueur annoncée correspond à la longueur réelle
        """
        def validPatternLength(p):
            assert len(p.infos["motif Lily"].split(',')) == p.infos["long"]

        testSet = random.sample(cls.patterns,cls.nbTests)
        for pattern in testSet:
            yield validPatternLength, pattern


    def test_validStampList(cls):
        """
        Vérifie que la longueur de chaque occurrence (nb de timestamps) est valide
        """
        def validStampList(p):
            patternLength = p.infos["long"]
            for occ in p.occ:
                assert_equals(patternLength, len(occ["Stamps list"].split(",")))
        testSet = random.sample(cls.patterns,cls.nbTests)
        for pattern in testSet:
            yield validStampList, pattern

