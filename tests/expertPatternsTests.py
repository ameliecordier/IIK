from csvhandler import expertPatterns
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
        On vérifie que l'on a bien récupéré tous les patterns
        """
        assert len(ep.patterns) == 25

def test_isAGoodPatterns():
        """
        On vérifie que la liste est bien remplie
        """
        assert ep.patterns[4] == "do,la,si,do"







