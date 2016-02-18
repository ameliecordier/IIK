from datahandler import expertPatterns
from datahandler import miningPatterns
from datahandler import analyser as analyser

def tryExpertPatterns(filename):
    """
    Expérimentations avec la classe expertPatterns
    """
    ep = expertPatterns.ExpertPatterns()
    ep.getPatterns(filename)
    ep.printPatterns()
    print(ep.getSetOfObselTypes())


def tryRawResults(filea, fileb, filec):
    """
    Expérimentations de la classe MiningPatterns en mode Raw
    """

    ri = miningPatterns.MiningPatterns()
    rb = miningPatterns.MiningPatterns()
    rr = miningPatterns.MiningPatterns()

    ri.getRawMiningResults(filea)
    rb.getRawMiningResults(fileb)
    rr.getRawMiningResults(filec)
    for line in ri.rawResults:
        if (len(line)-13)%11 != 0:
            print("error")
    for line in rb.rawResults:
        if (len(line)-13)%11 != 0:
            print("error")
    for line in rr.rawResults:
        if (len(line)-13)%11 != 0:
            print("error")


def tryResults(filename):
    """
    Expérimentations de la classe MiningPatterns en mode standard
    """

    rr = miningPatterns.MiningPatterns()
    rr.getMiningResults(filename)
    rr.printMiningResults()


def tryFindPatterns(mining, expert, output):
    """
    Expérimentation de la méthode findPatterns
    """

    rr = miningPatterns.MiningPatterns()
    ep = expertPatterns.ExpertPatterns()
    rr.getMiningResults(mining)
    ep.getPatterns(expert)
    sortedra = analyser.sortBy(0, False, rr)
    sortedrb = analyser.sortBy(4, True, rr)
    sortedrc = analyser.sortBy(7, True, rr)

    ra = analyser.findPatterns(ep, sortedra)
    rb = analyser.findPatterns(ep, sortedrb)
    rc = analyser.findPatterns(ep, sortedrc)

    print("Résultats : ")
    analyser.generateGraph(ra,rb,rc)


def tryNewMiningPatterns(filename):
    """
    Expérimentations de la méthode mining patterns
    """
    rr = list(miningPatterns.readRows(filename, 13, 11))
    for elt in rr:
        print(elt)
    print("Break")
    miningPatterns.sortBy(rr, [("freq", "desc"), ("cov int", "asc"), ("recov", "desc")])
    for elt in rr:
        print(elt.infos["freq"], elt.infos["cov int"], elt.infos["recov"])


def tryAnalysis(mining, expert, output, output2):
    """
    Experimentations des analyses brutes
    """


    ep = expertPatterns.ExpertPatterns()
    ep.getPatterns(expert)

    mp = list(miningPatterns.readRows(mining, 13, 11))
    analyserRes = analyser.findPatterns(ep, mp)
    analyserRes.toFile(output)

    miningPatterns.sortBy(mp, [("freq", "desc")])
    for i in range(40):
        print(mp[i].infos)

    analyserRes = analyser.findPatterns(ep, mp)
    analyserRes.toFile(output2)


debussy = "DATA/Debussy_Syrinx_out1_court.csv"
debussy_expert = "DATA/Debussy_Syrinx_court.txt"
ibert = "DATA/Ibert_Entracte_out1.csv"
ibert_expert = "DATA/ibert_motifs.csv"
reichert = "DATA/Reichert_tarentelle_out1.csv"
reichert_expert = "DATA/Reichert_tarentelle_motifs.txt"


#tryExpertPatterns(filename)
#tryRawResults(filea, fileb, filec)
#tryResults(filename)
#tryFindPatterns(mining, expert, output)
#tryNewMiningPatterns(filename)

#TODO : tests des méthodes above
mining = ibert
expert =ibert_expert
output = "DATA/output.csv"
output2 = "DATA/output2.csv"
tryAnalysis(mining, expert, output, output2)