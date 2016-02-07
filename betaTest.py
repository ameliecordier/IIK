from datahandler import expertPatterns
from datahandler import miningPatterns

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

#tryExpertPatterns()
#tryRawResults()
#tryResults()



"""
filename="../DATA/ibert_results_test.csv"
outputfilename="../DATA/output.csv"
expertfile = "../DATA/ibert_motifs.csv"
rr = miningPatterns.MiningPatterns()
ep = expertPatterns.ExpertPatterns()
ep.getPatterns(expertfile)
rr.getMiningResults(filename)
sortedrr = sortByFreq(rr)
findPatterns(ep, rr)
sortedrr.exportResults(outputfilename)
"""
