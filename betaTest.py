from datahandler import expertPatterns
from datahandler import miningPatterns
from datahandler import analyser
import random


def tryExpertPatterns():
    """
    Expérimentations avec la classe expertPatterns
    """
    filename = "DATA/ibert_motifs.csv"

    ep = expertPatterns.ExpertPatterns()
    ep.getPatterns(filename)
    ep.printPatterns()
    print(ep.getSetOfObselTypes())

def tryRawResults():
    """
    Expérimentations de la classe MiningPatterns en mode Raw
    """
    ibert = "DATA/ibert_results.csv"
    debussy = "DATA/Debussy_Syrinx_out1.csv"
    reichert = "DATA/Reichert_tarentelle_out1.csv"

    ri = miningPatterns.MiningPatterns()
    rb = miningPatterns.MiningPatterns()
    rr = miningPatterns.MiningPatterns()

    ri.getRawMiningResults(ibert)
    rb.getRawMiningResults(debussy)
    rr.getRawMiningResults(reichert)
    for line in ri.rawResults:
        if (len(line)-13)%11 != 0:
            print("error")
    for line in rb.rawResults:
        if (len(line)-13)%11 != 0:
            print("error")
    for line in rr.rawResults:
        if (len(line)-13)%11 != 0:
            print("error")


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
    sortedra = analyser.sortBy(0, False, rr)
    sortedrb = analyser.sortBy(4, True, rr)
    sortedrc = analyser.sortBy(7, True, rr)

    ra = analyser.findPatterns(ep, sortedra)
    rb = analyser.findPatterns(ep, sortedrb)
    rc = analyser.findPatterns(ep, sortedrc)

    print("Résultats : ")
    analyser.generateGraph(ra,rb,rc)

def tryFindPatternsWithRevision():
    """
    Expérimentation de la méthode findPatternsWithRevision
    """

    filename="DATA/ibert_results.csv"
    outputfilename="DATA/output.csv"
    expertfile = "DATA/ibert_motifs.csv"

    rr = miningPatterns.MiningPatterns()
    ep = expertPatterns.ExpertPatterns()
    rr.getMiningResults(filename)
    ep.getPatterns(expertfile)

    analyser.findPatternsWithRevision(ep, rr)



#tryExpertPatterns()
#tryRawResults()
#tryResults()
#tryFindPatterns()
#tryFindPatternsWithRevision()

