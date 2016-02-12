from datahandler import expertPatterns
"""
ATTENTION
Les tests ici sont directement dépendants du fichier choisi
"""

ep = expertPatterns.ExpertPatterns()


def setup_module(module):
    print("")
    print("Test de ExpertPatterns")
    print("Lecture des données dans le fichier")
    ep.getPatterns("DATA/ibert_motifs.csv")

def teardown_module(module):
    print("=== Fin de test de la classe ExpertPatterns")

def test_LenPatterns():
    """
    Vérification que tous les patterns sont récupérés
    """
    assert len(ep.patterns) == 25

def test_isAGoodPatterns():
    """
    Vérification que les patterns récupérés sont corrects
    """
    assert ep.patterns[4] == "do,la,si,do"

def test_returnsAGoodSet():
    """
    Vérification que le set des types est complet
    """
    test_set = {"do", "dod", "fa", "fad", "la", "mi", "re", "si", "sib", "sol", "sold"}
    assert test_set == ep.getSetOfObselTypes()


