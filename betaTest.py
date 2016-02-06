from csvhandler import expertPatterns


def testExpertPatterns():
    """
    Expérimentations avec la classe expertPatterns
    """
    filename = "DATA/ibert_motifs.csv"

    ep = expertPatterns.ExpertPatterns()
    ep.getPatterns(filename)
    ep.printPatterns()

testExpertPatterns()