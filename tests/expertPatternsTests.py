from nose.tools import assert_equals
from datahandler import expertPatterns
"""
ATTENTION
Les tests ici sont directement dépendants du fichier choisi
"""

ep = expertPatterns.ExpertPatterns()


def setup_module(module):
    print("")
    print("Test de ExpertPatterns")
    print("Lecture des données dans le fichier ibert_motifs.csv")
    ep.getPatterns("DATA/ibert_motifs.csv")

def teardown_module(module):
    print("=== Fin de test de la classe ExpertPatterns")

def test_LenPatterns():
    """
    Vérification que tous les patterns sont récupérés
    """
    assert_equals(len(ep.patterns), 22)

def test_isAGoodPatterns():
    """
    Vérification que les patterns récupérés sont corrects
    """
    assert_equals(ep.patterns[4], "si,do,re,mi,fa,sol")

def test_returnsAGoodSet():
    """
    Vérification que le set des types est complet
    """
    test_set = {"do", "dod", "fa", "fad", "la", "mi", "re", "si", "sib", "sol", "sold"}
    assert_equals(test_set, ep.getSetOfObselTypes())


