# -*- coding: utf-8 -*-
import csv

from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def isValid(p, ep):
    return p in ep.patterns


def findPatternsWithRevision(expertPatterns, miningPatternsList):

    analyser = Analyser()
    patternList = [elt.infos["motif Lily"] for elt in reversed(miningPatternsList)]

    while patternList:
        # Récup du nom du pattern
        pattern = patternList.pop()

        if isValid(pattern, expertPatterns):
            # Récup du pattern dans mp
            for elt in miningPatternsList:
                if elt.infos["motif Lily"] == pattern:
                    fullPattern = elt
                    fullPatternIdx = miningPatternsList.index(elt)
                    break

            # Récup de l'index du pattern dans ep
            idx = expertPatterns.patterns.index(pattern)

            # Ajout des infos du pattern aux résultats
            result = {}
            result["pattern"] = pattern
            result["idxExpert"] = idx
            result["idxMining"] = fullPatternIdx
            analyser.addResult(result)

            # Récupération du set d'occurrences
            stampsSet = [elt.get("Stamps list") for elt in fullPattern.occ]
            stampsSet = list(map(list, stampsSet))
            stampsSet = set([y for x in stampsSet for y in x])

            # Élimination de tous les patterns recouverts
            datahandler.miningPatterns.clearObsoletePatterns(miningPatternsList, stampsSet, patternList)

            # Suppression du pattern étudié
            #miningPatterns.remove(miningPatternsList, pattern)
            #miningPatternsList.remove(fullPattern)
            print(len(miningPatternsList))
            # Mining patterns : recalcul de support


    return analyser



def generateGraph(anaRandom, anaFreq, anaCov, fignum):



    linestyles = ['-', '--', '-.', ':']

    plt.figure(fignum)
    plt.axis([0, 30, 0, 10000])
    plt.plot(x, random, 'r', linestyle="- ", label="Random")
    plt.plot(y, freq, 'g', linestyle="-- ", label="Fréq")
    plt.plot(z, cov, 'b', linestyle="* ", label="Cov")
    plt.xlabel('Itération')
    plt.ylabel('Rang du pattern')
    plt.title('Résultats')
    plt.legend()
    #plt.show()
    #plt.savefig(pp, format="pdf")

    return plt

# CLASS ANALYSER
class Analyser:
    """
    Représentation d'un résultat d'analyse
    """

    def __init__(self):
        """
        :param results: contient les résultats de l'analyse
        """
        self.results = []

    def addResult(self, result):
        """
        Ajoute une liste de résultats à l'ensemble des résultats
        :param result: la ligne de résultats
        :return: None
        """
        self.results.append(result)

    def __str__(self):
        """
        Affichage des résultats sur la sortie standard
        """
        return "Résultats : %r" % self.results

    def toFile(self, filename):
        with open(filename, "w") as outfile:
            fieldnames = ['idxExpert', 'idxMining', 'pattern expert', 'pattern mining' , 'full pattern']
            w = csv.DictWriter(outfile, delimiter=";", fieldnames=fieldnames)
            w.writeheader()
            w.writerows(self.results)
