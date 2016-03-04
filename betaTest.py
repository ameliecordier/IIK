from datahandler import expertPatterns
from datahandler import miningPatterns
from datahandler import analyser as analyser

from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages



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
        if (len(line) - 13) % 11 != 0:
            print("error")
    for line in rb.rawResults:
        if (len(line) - 13) % 11 != 0:
            print("error")
    for line in rr.rawResults:
        if (len(line) - 13) % 11 != 0:
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
    analyser.generateGraph(ra, rb, rc)


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


def tryAnalysisWithRemove(mining, expert, outputRev):

    ep = expertPatterns.ExpertPatterns()
    ep.getPatterns(expert)

    mp = list(miningPatterns.readRows(mining, 13, 11))
    analyserRes = analyser.findPatternsWithRevision(ep, mp)
    analyserRes.toFile(outputRev)

    print(analyserRes)


def tryComparativeAnalysis(mining, expert, outputStand, outputRev):

    ep = expertPatterns.ExpertPatterns()
    ep.getPatterns(expert)

    mp = list(miningPatterns.readRows(mining, 13, 11))

    mpRev = list(miningPatterns.readRows(mining, 13, 11))


    miningPatterns.sortBy(mp, [("cov evt", "desc"), ("long", "asc")])
    analyserRes = analyser.findPatterns(ep, mp)
    analyserRes.toFile(outputStand)


    miningPatterns.sortBy(mpRev, [("cov evt", "desc"), ("long", "asc")])
    analyserResRev = analyser.findPatternsWithRevision(ep, mpRev)
    analyserResRev.toFile(outputRev)

    print(analyserRes)


def niemeRefacto(mining, expert):

    ep = expertPatterns.ExpertPatterns()
    ep.getPatterns(expert)


    mp = miningPatterns.Patterns(mining, ";", 13, 11)
    mp.sortBy([("freq", "asc"), ("cov evt", "desc")])
    for pattern in mp.patterns:
        print(pattern)

    mp.printInfos()
    mp.printOccInfos()

def tryAnalyser(mining, expert, nameExpe):

    ep = expertPatterns.ExpertPatterns()
    ep.getPatterns(expert)

    mpRand = miningPatterns.Patterns(mining, ";", 13, 11)
    mpFreq = miningPatterns.Patterns(mining, ";", 13, 11)
    mpCove = miningPatterns.Patterns(mining, ";", 13, 11)

    mpRandNoRev = miningPatterns.Patterns(mining, ";", 13, 11)
    mpFreqNoRev = miningPatterns.Patterns(mining, ";", 13, 11)
    mpCoveNoRev = miningPatterns.Patterns(mining, ";", 13, 11)


    # Random
    fname = "DATA/" + nameExpe + "_no-rev_beforeSortRandom.csv"
    mpRandNoRev.toFile(fname)
    anaRandNoRev = mpRandNoRev.findPatterns(ep)
    fname = "DATA/" + nameExpe + "_no-rev_analyseRandom.csv"
    anaRandNoRev.toFile(fname)
    fname = "DATA/" + nameExpe + "_no-rev_afterSortRandom.csv"
    mpRandNoRev.toFile(fname)

    # Freq
    fname = "DATA/" + nameExpe + "_no-rev_beforeSortFreq.csv"
    mpFreqNoRev.toFile(fname)
    mpFreqNoRev.sortBy([("freq", "desc")])
    anaFreqNoRev = mpFreqNoRev.findPatterns(ep)
    fname = "DATA/" + nameExpe + "_no-rev_analyseFreq.csv"
    anaFreqNoRev.toFile(fname)
    fname = "DATA/" + nameExpe + "_no-rev_afterSortFreq.csv"
    mpFreqNoRev.toFile(fname)

    # Cov evt
    fname = "DATA/" + nameExpe + "_no-rev_beforeSortCovEvt.csv"
    mpCoveNoRev.toFile(fname)
    mpCoveNoRev.sortBy([("cov evt", "desc")])
    anaCoveNoRev = mpCoveNoRev.findPatterns(ep)
    fname = "DATA/" + nameExpe + "_no-rev_analyseCovEvt.csv"
    anaCoveNoRev.toFile(fname)
    fname = "DATA/" + nameExpe + "_no-rev_afterSortCovEvt.csv"
    mpCoveNoRev.toFile(fname)


    # Avec rév
    mpRand = miningPatterns.Patterns(mining, ";", 13, 11)
    mpFreq = miningPatterns.Patterns(mining, ";", 13, 11)
    mpCove = miningPatterns.Patterns(mining, ";", 13, 11)


    # Random
    fname = "DATA/" + nameExpe + "_rev_beforeSortRandom.csv"
    mpRand.toFile(fname)
    anaRand = mpRand.findPatternsWithRevision(ep)
    fname = "DATA/" + nameExpe + "_rev_analyseRandom.csv"
    anaRand.toFile(fname)
    fname = "DATA/" + nameExpe + "_rev_afterSortRandom.csv"
    mpRand.toFile(fname)

    # Freq
    fname = "DATA/" + nameExpe + "_rev_beforeSortFreq.csv"
    mpFreq.toFile(fname)
    mpFreq.sortBy([("freq", "desc")])
    anaFreq = mpFreq.findPatternsWithRevision(ep)
    fname = "DATA/" + nameExpe + "_rev_analyseFreq.csv"
    anaFreq.toFile(fname)
    fname = "DATA/" + nameExpe + "_rev_afterSortFreq.csv"
    mpFreq.toFile(fname)

    # Cov evt
    fname = "DATA/" + nameExpe + "_rev_beforeSortCovEvt.csv"
    mpCove.toFile(fname)
    mpCove.sortBy([("cov evt", "desc")])
    anaCove = mpCove.findPatternsWithRevision(ep)
    fname = "DATA/" + nameExpe + "_rev_analyseCovEvt.csv"
    anaCove.toFile(fname)
    fname = "DATA/" + nameExpe + "_rev_afterSortCovEvt.csv"
    mpCove.toFile(fname)


    # Génération des graphs
    x = list(range(len(anaRandNoRev.results)))
    y = list(range(len(anaFreqNoRev.results)))
    z = list(range(len(anaCoveNoRev.results)))
    xrev = list(range(len(anaRand.results)))
    yrev = list(range(len(anaFreq.results)))
    zrev = list(range(len(anaCove.results)))

    random = []
    freq = []
    cov = []
    randomrev = []
    freqrev = []
    covrev = []

    for elt in anaRandNoRev.results:
        random.append(elt["idxMining"])
    for elt in anaFreqNoRev.results:
        freq.append(elt["idxMining"])
    for elt in anaCoveNoRev.results:
        cov.append(elt["idxMining"])
    for elt in anaRand.results:
        randomrev.append(elt["idxMining"])
    for elt in anaFreq.results:
        freqrev.append(elt["idxMining"])
    for elt in anaCove.results:
        covrev.append(elt["idxMining"])


    pdfname = "DATA/" + nameExpe + ".pdf"
    pp = PdfPages(pdfname)

    plt.figure(1)
    plt.plot(x, random, 'r',  linestyle="-", label="Random")
    plt.plot(y, freq, 'g',  linestyle="--", label="Fréq")
    plt.plot(z, cov, 'b',  linestyle="-.", label="Cov")
    plt.xlabel('Itération')
    plt.ylabel('Rang du pattern')
    plt.title('Comparaison des résultats sans révision')
    plt.legend()
    plt.savefig(pp, format="pdf")


    plt.figure(2)
    plt.plot(xrev, randomrev, 'r', linestyle="-", label="Random")
    plt.plot(yrev, freqrev, 'g',  linestyle="--", label="Fréq")
    plt.plot(zrev, covrev, 'b',  linestyle="-.", label="Cov")
    plt.xlabel('Itération')
    plt.ylabel('Rang du pattern')
    plt.title('Comparaison des résultats avec révision')
    plt.legend()
    plt.savefig(pp, format="pdf")


    plt.figure(3)
    plt.plot(x, random, 'r',  linestyle="-", label="Random sans révision")
    plt.plot(xrev, randomrev, 'g', linestyle="--", label="Random avec révision")
    plt.xlabel('Itération')
    plt.ylabel('Rang du pattern')
    plt.title('Performances de random avec / sans révision')
    plt.legend()
    plt.savefig(pp, format="pdf")

    plt.figure(4)
    plt.plot(y, freq, 'r', linestyle="-", label="Freq sans révision")
    plt.plot(yrev, freqrev, 'g', linestyle="--", label="Freq avec révision")
    plt.xlabel('Itération')
    plt.ylabel('Rang du pattern')
    plt.title('Performances de freq avec / sans révision')
    plt.legend()
    plt.savefig(pp, format="pdf")

    plt.figure(5)
    plt.plot(z, cov, 'r', linestyle="-", label="Cov evt sans révision")
    plt.plot(zrev, covrev, 'g', linestyle="--", label="Cov evt avec révision")
    plt.xlabel('Itération')
    plt.ylabel('Rang du pattern')
    plt.title('Performances de cov evt avec / sans révision')
    plt.legend()
    plt.savefig(pp, format="pdf")


    pp.close()

def tryAnalyserLongeur(mining, expert, nameExpe):

    ep = expertPatterns.ExpertPatterns()
    ep.getPatterns(expert)

    print(ep.patterns)

    mpRand = miningPatterns.Patterns(mining, ";", 13, 11)
    mpFreq = miningPatterns.Patterns(mining, ";", 13, 11)
    mpCove = miningPatterns.Patterns(mining, ";", 13, 11)

    mpRandNoRev = miningPatterns.Patterns(mining, ";", 13, 11)
    mpFreqNoRev = miningPatterns.Patterns(mining, ";", 13, 11)
    mpCoveNoRev = miningPatterns.Patterns(mining, ";", 13, 11)


    # Random
    fname = "DATA/" + nameExpe + "_no-rev_beforeSortRandom.csv"
    mpRandNoRev.toFile(fname)
    anaRandNoRev = mpRandNoRev.findPatterns(ep)
    fname = "DATA/" + nameExpe + "_no-rev_analyseRandom.csv"
    anaRandNoRev.toFile(fname)
    fname = "DATA/" + nameExpe + "_no-rev_afterSortRandom.csv"
    mpRandNoRev.toFile(fname)

    # Freq
    fname = "DATA/" + nameExpe + "_no-rev_beforeSortFreq.csv"
    mpFreqNoRev.toFile(fname)
    mpFreqNoRev.sortBy([("long", "desc"), ("freq", "desc")])
    anaFreqNoRev = mpFreqNoRev.findPatterns(ep)
    fname = "DATA/" + nameExpe + "_no-rev_analyseFreq.csv"
    anaFreqNoRev.toFile(fname)
    fname = "DATA/" + nameExpe + "_no-rev_afterSortFreq.csv"
    mpFreqNoRev.toFile(fname)

    # Cov evt
    fname = "DATA/" + nameExpe + "_no-rev_beforeSortCovEvt.csv"
    mpCoveNoRev.toFile(fname)
    mpCoveNoRev.sortBy([("long", "desc"), ("cov evt", "desc")])
    anaCoveNoRev = mpCoveNoRev.findPatterns(ep)
    fname = "DATA/" + nameExpe + "_no-rev_analyseCovEvt.csv"
    anaCoveNoRev.toFile(fname)
    fname = "DATA/" + nameExpe + "_no-rev_afterSortCovEvt.csv"
    mpCoveNoRev.toFile(fname)


    # Avec rév
    mpRand = miningPatterns.Patterns(mining, ";", 13, 11)
    mpFreq = miningPatterns.Patterns(mining, ";", 13, 11)
    mpCove = miningPatterns.Patterns(mining, ";", 13, 11)


    # Random
    fname = "DATA/" + nameExpe + "_rev_beforeSortRandom.csv"
    mpRand.toFile(fname)
    anaRand = mpRand.findPatternsWithRevision(ep)
    fname = "DATA/" + nameExpe + "_rev_analyseRandom.csv"
    anaRand.toFile(fname)
    fname = "DATA/" + nameExpe + "_rev_afterSortRandom.csv"
    mpRand.toFile(fname)

    # Freq
    fname = "DATA/" + nameExpe + "_rev_beforeSortFreq.csv"
    mpFreq.toFile(fname)
    mpFreq.sortBy([("long", "desc"), ("freq", "desc")])
    anaFreq = mpFreq.findPatternsWithRevision(ep)
    fname = "DATA/" + nameExpe + "_rev_analyseFreq.csv"
    anaFreq.toFile(fname)
    fname = "DATA/" + nameExpe + "_rev_afterSortFreq.csv"
    mpFreq.toFile(fname)

    # Cov evt
    fname = "DATA/" + nameExpe + "_rev_beforeSortCovEvt.csv"
    mpCove.toFile(fname)
    mpCove.sortBy([("long", "desc"), ("cov evt", "desc")])
    anaCove = mpCove.findPatternsWithRevision(ep)
    fname = "DATA/" + nameExpe + "_rev_analyseCovEvt.csv"
    anaCove.toFile(fname)
    fname = "DATA/" + nameExpe + "_rev_afterSortCovEvt.csv"
    mpCove.toFile(fname)


    # Génération des graphs
    x = list(range(len(anaRandNoRev.results)))
    y = list(range(len(anaFreqNoRev.results)))
    z = list(range(len(anaCoveNoRev.results)))
    xrev = list(range(len(anaRand.results)))
    yrev = list(range(len(anaFreq.results)))
    zrev = list(range(len(anaCove.results)))

    random = []
    freq = []
    cov = []
    randomrev = []
    freqrev = []
    covrev = []

    for elt in anaRandNoRev.results:
        random.append(elt["idxMining"])
    for elt in anaFreqNoRev.results:
        freq.append(elt["idxMining"])
    for elt in anaCoveNoRev.results:
        cov.append(elt["idxMining"])
    for elt in anaRand.results:
        randomrev.append(elt["idxMining"])
    for elt in anaFreq.results:
        freqrev.append(elt["idxMining"])
    for elt in anaCove.results:
        covrev.append(elt["idxMining"])



    pp = PdfPages("DATA/reichertLong.pdf")

    plt.figure(1)
    plt.plot(x, random, 'r',  linestyle="-", label="Random")
    plt.plot(y, freq, 'g',  linestyle="--", label="Fréq")
    plt.plot(z, cov, 'b',  linestyle="-.", label="Cov")
    plt.xlabel('Itération')
    plt.ylabel('Rang du pattern')
    plt.title('Comparaison des résultats sans révision')
    plt.legend()
    plt.savefig(pp, format="pdf")


    plt.figure(2)
    plt.plot(xrev, randomrev, 'r', linestyle="-", label="Random")
    plt.plot(yrev, freqrev, 'g',  linestyle="--", label="Fréq")
    plt.plot(zrev, covrev, 'b',  linestyle="-.", label="Cov")
    plt.xlabel('Itération')
    plt.ylabel('Rang du pattern')
    plt.title('Comparaison des résultats avec révision')
    plt.legend()
    plt.savefig(pp, format="pdf")


    plt.figure(3)
    plt.plot(x, random, 'r',  linestyle="-", label="Random sans révision")
    plt.plot(xrev, randomrev, 'g', linestyle="--", label="Random avec révision")
    plt.xlabel('Itération')
    plt.ylabel('Rang du pattern')
    plt.title('Performances de random avec / sans révision')
    plt.legend()
    plt.savefig(pp, format="pdf")

    plt.figure(4)
    plt.plot(y, freq, 'r', linestyle="-", label="Freq sans révision")
    plt.plot(yrev, freqrev, 'g', linestyle="--", label="Freq avec révision")
    plt.xlabel('Itération')
    plt.ylabel('Rang du pattern')
    plt.title('Performances de freq avec / sans révision')
    plt.legend()
    plt.savefig(pp, format="pdf")

    plt.figure(5)
    plt.plot(z, cov, 'r', linestyle="-", label="Cov evt sans révision")
    plt.plot(zrev, covrev, 'g', linestyle="--", label="Cov evt avec révision")
    plt.xlabel('Itération')
    plt.ylabel('Rang du pattern')
    plt.title('Performances de cov evt avec / sans révision')
    plt.legend()
    plt.savefig(pp, format="pdf")


    pp.close()

def tryAnalyserDebussy(mining, expert, nameExpe):

    ep = expertPatterns.ExpertPatterns()
    ep.getPatterns(expert)

    print(ep.patterns)

    mpRand = miningPatterns.Patterns(mining, ";", 13, 11)
    mpFreq = miningPatterns.Patterns(mining, ";", 13, 11)
    mpCove = miningPatterns.Patterns(mining, ";", 13, 11)

    mpRandNoRev = miningPatterns.Patterns(mining, ";", 13, 11)
    mpFreqNoRev = miningPatterns.Patterns(mining, ";", 13, 11)
    mpCoveNoRev = miningPatterns.Patterns(mining, ";", 13, 11)


    # Random
    fname = "DATA/" + nameExpe + "_no-rev_beforeSortRandom.csv"
    mpRandNoRev.toFile(fname)
    anaRandNoRev = mpRandNoRev.findPatterns(ep)
    fname = "DATA/" + nameExpe + "_no-rev_analyseRandom.csv"
    anaRandNoRev.toFile(fname)
    fname = "DATA/" + nameExpe + "_no-rev_afterSortRandom.csv"
    mpRandNoRev.toFile(fname)

    # Freq
    fname = "DATA/" + nameExpe + "_no-rev_beforeSortFreq.csv"
    mpFreqNoRev.toFile(fname)
    mpFreqNoRev.sortBy([("long", "desc"), ("freq", "desc")])
    anaFreqNoRev = mpFreqNoRev.findPatterns(ep)
    fname = "DATA/" + nameExpe + "_no-rev_analyseFreq.csv"
    anaFreqNoRev.toFile(fname)
    fname = "DATA/" + nameExpe + "_no-rev_afterSortFreq.csv"
    mpFreqNoRev.toFile(fname)

    # Cov evt
    fname = "DATA/" + nameExpe + "_no-rev_beforeSortCovEvt.csv"
    mpCoveNoRev.toFile(fname)
    mpCoveNoRev.sortBy([("long", "desc"), ("cov evt", "desc")])
    anaCoveNoRev = mpCoveNoRev.findPatterns(ep)
    fname = "DATA/" + nameExpe + "_no-rev_analyseCovEvt.csv"
    anaCoveNoRev.toFile(fname)
    fname = "DATA/" + nameExpe + "_no-rev_afterSortCovEvt.csv"
    mpCoveNoRev.toFile(fname)


    # Avec rév
    mpRand = miningPatterns.Patterns(mining, ";", 13, 11)
    mpFreq = miningPatterns.Patterns(mining, ";", 13, 11)
    mpCove = miningPatterns.Patterns(mining, ";", 13, 11)


    # Random
    fname = "DATA/" + nameExpe + "_rev_beforeSortRandom.csv"
    mpRand.toFile(fname)
    anaRand = mpRand.findPatternsWithRevision(ep)
    fname = "DATA/" + nameExpe + "_rev_analyseRandom.csv"
    anaRand.toFile(fname)
    fname = "DATA/" + nameExpe + "_rev_afterSortRandom.csv"
    mpRand.toFile(fname)

    # Freq
    fname = "DATA/" + nameExpe + "_rev_beforeSortFreq.csv"
    mpFreq.toFile(fname)
    mpFreq.sortBy([("long", "desc"), ("freq", "desc")])
    anaFreq = mpFreq.findPatternsWithRevision(ep)
    fname = "DATA/" + nameExpe + "_rev_analyseFreq.csv"
    anaFreq.toFile(fname)
    fname = "DATA/" + nameExpe + "_rev_afterSortFreq.csv"
    mpFreq.toFile(fname)

    # Cov evt
    fname = "DATA/" + nameExpe + "_rev_beforeSortCovEvt.csv"
    mpCove.toFile(fname)
    mpCove.sortBy([("long", "desc"), ("cov evt", "desc")])
    anaCove = mpCove.findPatternsWithRevision(ep)
    fname = "DATA/" + nameExpe + "_rev_analyseCovEvt.csv"
    anaCove.toFile(fname)
    fname = "DATA/" + nameExpe + "_rev_afterSortCovEvt.csv"
    mpCove.toFile(fname)


    # Génération des graphs
    x = list(range(len(anaRandNoRev.results)))
    y = list(range(len(anaFreqNoRev.results)))
    z = list(range(len(anaCoveNoRev.results)))
    xrev = list(range(len(anaRand.results)))
    yrev = list(range(len(anaFreq.results)))
    zrev = list(range(len(anaCove.results)))

    random = []
    freq = []
    cov = []
    randomrev = []
    freqrev = []
    covrev = []

    for elt in anaRandNoRev.results:
        random.append(elt["idxMining"])
    for elt in anaFreqNoRev.results:
        freq.append(elt["idxMining"])
    for elt in anaCoveNoRev.results:
        cov.append(elt["idxMining"])
    for elt in anaRand.results:
        randomrev.append(elt["idxMining"])
    for elt in anaFreq.results:
        freqrev.append(elt["idxMining"])
    for elt in anaCove.results:
        covrev.append(elt["idxMining"])



    pp = PdfPages("DATA/reichertLong.pdf")

    plt.figure(1)
    plt.plot(x, random, 'r',  linestyle="-", label="Random")
    plt.plot(y, freq, 'g',  linestyle="--", label="Fréq")
    plt.plot(z, cov, 'b',  linestyle="-.", label="Cov")
    plt.xlabel('Itération')
    plt.ylabel('Rang du pattern')
    plt.title('Comparaison des résultats sans révision')
    plt.legend()
    plt.savefig(pp, format="pdf")


    plt.figure(2)
    plt.plot(xrev, randomrev, 'r', linestyle="-", label="Random")
    plt.plot(yrev, freqrev, 'g',  linestyle="--", label="Fréq")
    plt.plot(zrev, covrev, 'b',  linestyle="-.", label="Cov")
    plt.xlabel('Itération')
    plt.ylabel('Rang du pattern')
    plt.title('Comparaison des résultats avec révision')
    plt.legend()
    plt.savefig(pp, format="pdf")


    plt.figure(3)
    plt.plot(x, random, 'r',  linestyle="-", label="Random sans révision")
    plt.plot(xrev, randomrev, 'g', linestyle="--", label="Random avec révision")
    plt.xlabel('Itération')
    plt.ylabel('Rang du pattern')
    plt.title('Performances de random avec / sans révision')
    plt.legend()
    plt.savefig(pp, format="pdf")

    plt.figure(4)
    plt.plot(y, freq, 'r', linestyle="-", label="Freq sans révision")
    plt.plot(yrev, freqrev, 'g', linestyle="--", label="Freq avec révision")
    plt.xlabel('Itération')
    plt.ylabel('Rang du pattern')
    plt.title('Performances de freq avec / sans révision')
    plt.legend()
    plt.savefig(pp, format="pdf")

    plt.figure(5)
    plt.plot(z, cov, 'r', linestyle="-", label="Cov evt sans révision")
    plt.plot(zrev, covrev, 'g', linestyle="--", label="Cov evt avec révision")
    plt.xlabel('Itération')
    plt.ylabel('Rang du pattern')
    plt.title('Performances de cov evt avec / sans révision')
    plt.legend()
    plt.savefig(pp, format="pdf")


    pp.close()

def tryAnalyserIbert(mining, expert, nameExpe):

    ep = expertPatterns.ExpertPatterns()
    ep.getPatterns(expert)

    print("Patterns read")

    # Avec rév
    mpFreq = miningPatterns.Patterns(mining, ";", 13, 11)

    print("mp Freq ok")


    mpCove = mpFreq
    #miningPatterns.Patterns(mining, ";", 13, 11)

    print("mp Cove ok")


    # Freq
    fname = "DATA/" + nameExpe + "_rev_beforeSortFreq.csv"
    mpFreq.toFile(fname)
    mpFreq.sortBy([("freq", "desc")])
    anaFreq = mpFreq.findPatternsWithRevision(ep)
    fname = "DATA/" + nameExpe + "_rev_analyseFreq.csv"
    anaFreq.toFile(fname)
    fname = "DATA/" + nameExpe + "_rev_afterSortFreq.csv"
    mpFreq.toFile(fname)

    # Cov evt
    fname = "DATA/" + nameExpe + "_rev_beforeSortCovEvt.csv"
    mpCove.toFile(fname)
    mpCove.sortBy([("cov evt", "desc")])
    anaCove = mpCove.findPatternsWithRevision(ep)
    fname = "DATA/" + nameExpe + "_rev_analyseCovEvt.csv"
    anaCove.toFile(fname)
    fname = "DATA/" + nameExpe + "_rev_afterSortCovEvt.csv"
    mpCove.toFile(fname)


    # Génération des graphs
    yrev = list(range(len(anaFreq.results)))
    zrev = list(range(len(anaCove.results)))

    freqrev = []
    covrev = []

    for elt in anaFreq.results:
        freqrev.append(elt["idxMining"])
    for elt in anaCove.results:
        covrev.append(elt["idxMining"])


    pdfname = "DATA/" + nameExpe + ".pdf"
    pp = PdfPages(pdfname)

    plt.figure(1)
    plt.plot(yrev, freqrev, 'g',  linestyle="--", label="Fréq")
    plt.plot(zrev, covrev, 'b',  linestyle="-.", label="Cov")
    plt.xlabel('Itération')
    plt.ylabel('Rang du pattern')
    plt.title('Comparaison des résultats avec révision')
    plt.legend()
    plt.savefig(pp, format="pdf")

    pp.close()


# Nom des fichiers
debussy = "DATA/debussy_motifs.csv"
debussy_expert = "DATA/Debussy_Syrinx_court.txt"
ibert = "DATA/Ibert_Entracte_out2.csv"
ibert_expert = "DATA/ibert_motifs.csv"
reichert = "DATA/Reichert_tarentelle_out1.csv"
reichert_expert = "DATA/Reichert_tarentelle_motifs.txt"
dataperso = "DATA/datatest.csv"
dataperso_expert = "DATA/datatest_expert.csv"

mining = ibert
expert = ibert_expert

# tryExpertPatterns(filename)
# tryRawResults(filea, fileb, filec)
# tryResults(filename)
# tryFindPatterns(mining, expert, output)
# tryNewMiningPatterns(filename)
# tryAnalysis(mining, expert, output, output2)
# tryAnalysisWithRemove(mining, expert, outputRev)
# tryComparativeAnalysis(mining, expert, outputStand, outputRev)
# niemeRefacto(mining, expert)
#tryAnalyserLongeur(mining, expert, "reichert_long")
tryAnalyserIbert(mining, expert, "ibert_longmotifs2")

