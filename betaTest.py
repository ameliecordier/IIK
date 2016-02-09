from datahandler import expertPatterns
from datahandler import miningPatterns
from datahandler import analyser
import pprint


def tryExpertPatterns():
    """
    Expérimentations avec la classe expertPatterns
    """
    filename = "DATA/ibert_motifs.csv"

    ep = expertPatterns.ExpertPatterns()
    ep.getPatterns(filename)
    ep.printPatterns()

def tryRawResults():
    """
    Expérimentations de la classe MiningPatterns en mode Raw
    """
    filename = "DATA/ibert_results_test.csv"

    rr = miningPatterns.MiningPatterns()
    rr.getRawMiningResults(filename)
    rr.printRawHeading()
    rr.printRawResults()

def tryResults():
    """
    Expérimentations de la classe MiningPatterns en mode standard
    """
    filename = "DATA/ibert_results_test.csv"

    rr = miningPatterns.MiningPatterns()
    rr.getMiningResults(filename)
    rr.printMiningResults()

def tryFindPatterns():
    """
    Expérimentation de la méthode findPatterns
    """

    filename="DATA/ibert_results.csv"
    outputfilename="DATA/output.csv"
    expertfile = "DATA/ibert_motifs.csv"

    rr = miningPatterns.MiningPatterns()
    ep = expertPatterns.ExpertPatterns()
    rr.getMiningResults(filename)
    ep.getPatterns(expertfile)
    sortedrr = analyser.sortBy(4, True, rr)
    resultats = analyser.findPatterns(ep, sortedrr)
    print("Résultats : ")
    pprint.pprint(resultats)



#tryExpertPatterns()
#tryRawResults()
#tryResults()
tryFindPatterns()


