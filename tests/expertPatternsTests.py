from nose import with_setup
from csvhandler import expertPatterns

ep = expertPatterns.ExpertPatterns()


def setup_module(module):
    print ("") # this is to get a newline after the dots
    print ("setup_module before anything in this file")
    ep.getPatterns("../DATA/ibert_motifs.csv")

def teardown_module(module):
    print ("=== Fin de test de la classe ExpertPatterns")

def test_LenPatterns():
        assert len(ep.patterns) == 25

def test_isAGoodPatterns():
        assert ep.patterns[4] == "do,la,si,do"







