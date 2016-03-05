from datahandler import expertPatterns
from datahandler import miningPatterns
from datahandler import analyser as analyser
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import os
import time

def plot_two_results(norev, rev, fignum, legend, pp):
    """
    Utilitaire d'affichage d'une courbe de comparaison révision / no révision
    """

    x = list(range(len(norev.results)))
    xrev = list(range(len(rev.results)))
   
    norevList = []
    revList = []
    
    for elt in norev.results:
        norevList.append(elt["idxMining"])
    
    for elt in rev.results:
        revList.append(elt["idxMining"])
    

    plt.figure(fignum)
    plt.plot(x, norevList, 'r',  linestyle="-", label="Sans révision")
    plt.plot(xrev, revList, 'g', linestyle="--", label="Avec révision")
    plt.xlabel('Itération')
    plt.ylabel('Rang du pattern')
    plt.title(legend)
    plt.legend()
    plt.savefig(pp, format="pdf")


def plot_three_results(rand, freq, cove, figNum, legend, pp):
    """ 
    Utilitaire d'affichage d'une courbe de comparaison des trois méthodes
    """

    # Génération des graphs
    x = list(range(len(rand.results)))
    y = list(range(len(freq.results)))
    z = list(range(len(cove.results)))

    randomList = []
    freqList = []
    covList = []

    for elt in rand.results:
        randomList.append(elt["idxMining"])
    for elt in freq.results:
        freqList.append(elt["idxMining"])
    for elt in cove.results:
        covList.append(elt["idxMining"])

    plt.figure(figNum)
    plt.plot(x, randomList, 'r',  linestyle="-", label="Random")
    plt.plot(y, freqList, 'g',  linestyle="--", label="Fréq")
    plt.plot(z, covList, 'b',  linestyle="-.", label="Cov")
    plt.xlabel('Itération')
    plt.ylabel('Rang du pattern')
    plt.title(legend)
    plt.legend()
    plt.savefig(pp, format="pdf")


def threefold_comp(mining, expert, nameExpe, sortingFreq, sortingCov):
    """
    Compare random, fréquence et couverture événementielle
    Pour fréquence et couverture, le critère de tri est celui passé en paramètre
    Les résultats sont stockés dans le répertoire nameExpe
    """

    # Lecture des patterns
    ep = expertPatterns.ExpertPatterns()
    ep.getPatterns(expert)

    # Création du répertoire pour stocker les résultats
    try:
        os.mkdir("DATA/" + nameExpe)
    except:
        print("Directory already there")


    # Random
    randnorevbegin = time.time()
    mpRandNoRev = miningPatterns.Patterns(mining, ";", 13, 11)
    fname = "DATA/" + nameExpe + "/no-rev_beforeSortRandom.csv"
    mpRandNoRev.toFile(fname)
    anaRandNoRev = mpRandNoRev.findPatterns(ep)
    fname = "DATA/" + nameExpe + "/no-rev_analyseRandom.csv"
    anaRandNoRev.toFile(fname)
    fname = "DATA/" + nameExpe + "/no-rev_afterSortRandom.csv"
    mpRandNoRev.toFile(fname)
    del mpRandNoRev
    randnorevend = time.time()
    randnorevtime = randnorevend-randnorevbegin
    print(randnorevtime)


    # Freq
    freqnorevbegin = time.time()
    mpFreqNoRev = miningPatterns.Patterns(mining, ";", 13, 11)
    fname = "DATA/" + nameExpe + "/no-rev_beforeSortFreq.csv"
    mpFreqNoRev.toFile(fname)
    mpFreqNoRev.sortBy(sortingFreq)
    anaFreqNoRev = mpFreqNoRev.findPatterns(ep)
    fname = "DATA/" + nameExpe + "/no-rev_analyseFreq.csv"
    anaFreqNoRev.toFile(fname)
    fname = "DATA/" + nameExpe + "/no-rev_afterSortFreq.csv"
    mpFreqNoRev.toFile(fname)
    del mpFreqNoRev
    freqnorevend = time.time()
    freqnorevtime = freqnorevend-freqnorevbegin
    print(freqnorevtime)


    # Cov evt
    covnorevbegin = time.time()
    mpCoveNoRev = miningPatterns.Patterns(mining, ";", 13, 11)
    fname = "DATA/" + nameExpe + "/no-rev_beforeSortCovEvt.csv"
    mpCoveNoRev.toFile(fname)
    mpCoveNoRev.sortBy(sortingCov)
    anaCoveNoRev = mpCoveNoRev.findPatterns(ep)
    fname = "DATA/" + nameExpe + "/no-rev_analyseCovEvt.csv"
    anaCoveNoRev.toFile(fname)
    fname = "DATA/" + nameExpe + "/no-rev_afterSortCovEvt.csv"
    mpCoveNoRev.toFile(fname)
    del mpCoveNoRev
    covnorevend = time.time()
    covnorevtime = covnorevend-covnorevbegin
    print(covnorevtime)

    # Random
    randbegin = time.time()
    mpRand = miningPatterns.Patterns(mining, ";", 13, 11)
    fname = "DATA/" + nameExpe + "/rev_beforeSortRandom.csv"
    mpRand.toFile(fname)
    anaRand = mpRand.findPatternsWithRevision(ep)
    fname = "DATA/" + nameExpe + "/rev_analyseRandom.csv"
    anaRand.toFile(fname)
    fname = "DATA/" + nameExpe + "/rev_afterSortRandom.csv"
    mpRand.toFile(fname)
    del mpRand
    randend = time.time()
    randtime = randend - randbegin
    print(randtime)


    # Freq
    freqbegin = time.time()
    mpFreq = miningPatterns.Patterns(mining, ";", 13, 11)
    fname = "DATA/" + nameExpe + "/rev_beforeSortFreq.csv"
    mpFreq.toFile(fname)
    mpFreq.sortBy(sortingFreq)
    anaFreq = mpFreq.findPatternsWithRevision(ep)
    fname = "DATA/" + nameExpe + "/rev_analyseFreq.csv"
    anaFreq.toFile(fname)
    fname = "DATA/" + nameExpe + "/rev_afterSortFreq.csv"
    mpFreq.toFile(fname)
    del mpFreq
    freqend = time.time()
    freqtime = freqend - freqbegin
    print(freqtime)

    # Cov evt
    covbegin = time.time()
    mpCove = miningPatterns.Patterns(mining, ";", 13, 11)
    fname = "DATA/" + nameExpe + "/rev_beforeSortCovEvt.csv"
    mpCove.toFile(fname)
    mpCove.sortBy(sortingCov)
    anaCove = mpCove.findPatternsWithRevision(ep)
    fname = "DATA/" + nameExpe + "/rev_analyseCovEvt.csv"
    anaCove.toFile(fname)
    fname = "DATA/" + nameExpe + "/rev_afterSortCovEvt.csv"
    mpCove.toFile(fname)
    del mpCove
    covend = time.time()
    covtime = covend - covbegin
    print(covtime)



    # Génération des graphes résultats 
    pdfname = "DATA/" + nameExpe + "/results.pdf"
    pp = PdfPages(pdfname)

    legende = "Comparaison des résultats sans révision"
    plot_three_results(anaRandNoRev, anaFreqNoRev, anaCoveNoRev, 1, legende, pp)
    
    legende = "Comparaison des résultats avec révision"
    plot_three_results(anaRand, anaFreq, anaCove, 2, legende, pp)

    legende = "Performances de random"
    plot_two_results(anaRandNoRev, anaRand, 3, legende, pp)

    legende = "Performances de freq"
    plot_two_results(anaFreqNoRev, anaFreq, 4, legende, pp)
    
    legende = "Performances de cov evt"
    plot_two_results(anaCoveNoRev, anaCove, 5, legende, pp)

    pp.close()

    print(randtime, covtime, freqtime, randnorevtime, freqnorevtime, covnorevtime)

def threefold_compNoFiles(mining, expert, nameExpe, sortingFreq, sortingCov):
    """
    Compare random, fréquence et couverture événementielle
    Pour fréquence et couverture, le critère de tri est celui passé en paramètre
    Les résultats sont stockés dans le répertoire nameExpe
    Spécificité : à part les graphes résultats, pas de fichiers générés
    """

    # Lecture des patterns
    ep = expertPatterns.ExpertPatterns()
    ep.getPatterns(expert)

    # Création du répertoire pour stocker les résultats
    try:
        os.mkdir("DATA/" + nameExpe)
    except:
        print("Directory already there")

    # Random
    a = time.time()
    mpRandNoRev = miningPatterns.Patterns(mining, ";", 13, 11)
    anaRandNoRev = mpRandNoRev.findPatterns(ep)
    b = time.time()
    del mpRandNoRev
    print(b-a)

    # Freq
    mpFreqNoRev = miningPatterns.Patterns(mining, ";", 13, 11)
    mpFreqNoRev.sortBy(sortingFreq)
    anaFreqNoRev = mpFreqNoRev.findPatterns(ep)
    del mpFreqNoRev

    # Cov evt
    mpCoveNoRev = miningPatterns.Patterns(mining, ";", 13, 11)
    mpCoveNoRev.sortBy(sortingCov)
    anaCoveNoRev = mpCoveNoRev.findPatterns(ep)
    del mpCoveNoRev

    # Random
    mpRand = miningPatterns.Patterns(mining, ";", 13, 11)
    anaRand = mpRand.findPatternsWithRevision(ep)
    del mpRand

    # Freq
    mpFreq = miningPatterns.Patterns(mining, ";", 13, 11)
    mpFreq.sortBy(sortingFreq)
    anaFreq = mpFreq.findPatternsWithRevision(ep)
    del mpFreq

    # Cov evt
    mpCove = miningPatterns.Patterns(mining, ";", 13, 11)
    mpCove.sortBy(sortingCov)
    anaCove = mpCove.findPatternsWithRevision(ep)
    del mpCove

    # Génération des graphes résultats 
    pdfname = "DATA/" + nameExpe + "/results.pdf"
    pp = PdfPages(pdfname)

    legende = "Comparaison des résultats sans révision"
    plot_three_results(anaRandNoRev, anaFreqNoRev, anaCoveNoRev, 1, legende, pp)
    
    legende = "Comparaison des résultats avec révision"
    plot_three_results(anaRand, anaFreq, anaCove, 2, legende, pp)

    legende = "Performances de random"
    plot_two_results(anaRandNoRev, anaRand, 3, legende, pp)

    legende = "Performances de freq"
    plot_two_results(anaFreqNoRev, anaFreq, 4, legende, pp)
    
    legende = "Performances de cov evt"
    plot_two_results(anaCoveNoRev, anaCove, 5, legende, pp)

    pp.close()


# Expé 1 : ibert original, tri simple
'''
mining = "DATA/v1_ibert_fouille.csv"
expert = "DATA/v1_ibert_expert.csv"
xpname = "v1_ibert_standard"
sortingFreq = [("freq", "desc")]
sortingCov = [("cov evt", "desc")]
'''

# Expé 2 : ibert original, tri par longueur en premier
'''
mining = "DATA/v1_ibert_fouille.csv"
expert = "DATA/v1_ibert_expert.csv"
xpname = "v1_ibert_tri_longueur"
sortingFreq = [("long", "desc"), ("freq", "desc")]
sortingCov = [("long", "desc"), ("cov evt", "desc")]
'''

# Expé 3 : debussy original, tri simple
'''
mining = "DATA/v1_debussy_fouille.csv"
expert = "DATA/v1_debussy_expert.csv"
xpname = "v1_debussy_standard"
sortingFreq = [("freq", "desc")]
sortingCov = [("cov evt", "desc")]
'''

# Expé 4 : debussy original, tri par longueur en premier
'''
mining = "DATA/v1_debussy_fouille.csv"
expert = "DATA/v1_debussy_expert.csv"
xpname = "v1_debussy_tri_longueur"
sortingFreq = [("long", "desc"), ("freq", "desc")]
sortingCov = [("long", "desc"), ("cov evt", "desc")]
'''

# Expé 5 : reichert original, tri simple
'''
mining = "DATA/v1_reichert_fouille.csv"
expert = "DATA/v1_reichert_expert.csv"
xpname = "v1_reichert_standard"
sortingFreq = [("freq", "desc")]
sortingCov = [("cov evt", "desc")]
'''

# Expé 6 : reichert original, tri par longueur en premier
'''
mining = "DATA/v1_reichert_fouille.csv"
expert = "DATA/v1_reichert_expert.csv"
xpname = "v1_reichert_tri_longueur"
sortingFreq = [("long", "desc"), ("freq", "desc")]
sortingCov = [("long", "desc"), ("cov evt", "desc")]
'''

# Expé 7 : ibert v2, tri simple
'''
mining = "DATA/v2_ibert_fouille.csv"
expert = "DATA/v2_ibert_expert.csv"
xpname = "v2_ibert_standard"
sortingFreq = [("freq", "desc")]
sortingCov = [("cov evt", "desc")]
'''

# Expé 8 : ibert v2, tri par longueur en premier
# Super long

mining = "DATA/v2_ibert_fouille.csv"
expert = "DATA/v2_ibert_expert.csv"
xpname = "v2_ibert_tri_longueur"
sortingFreq = [("long", "desc"), ("freq", "desc")]
sortingCov = [("long", "desc"), ("cov evt", "desc")]


# Expé 9 : debussy v2, tri simple
'''
mining = "DATA/v2_debussy_fouille.csv"
expert = "DATA/v2_debussy_expert.csv"
xpname = "v2_debussy_standard"
sortingFreq = [("freq", "desc")]
sortingCov = [("cov evt", "desc")]
'''

# Expé 10 : debussy v2, tri par longueur en premier
'''
mining = "DATA/v2_debussy_fouille.csv"
expert = "DATA/v2_debussy_expert.csv"
xpname = "v2_debussy_tri_longueur"
sortingFreq = [("long", "desc"), ("freq", "desc")]
sortingCov = [("long", "desc"), ("cov evt", "desc")]
'''


# Main code
a = time.time()
threefold_comp(mining, expert, xpname, sortingFreq, sortingCov)
b = time.time()

print(b-a)
