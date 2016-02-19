# -*- coding: utf-8 -*-
import csv

from matplotlib import pyplot as plt
from datahandler import miningPatterns

def findPatterns(expertPatterns, miningPatterns):
    """
    Recherche dans les patterns minés les patterns identifiés par l'expert
    :param expertPatterns: la structure des patterns de l'expert
    :param miningPatterns: les patterns issus de la fouille
    :return: TODO => stoc dans un resutls
    """

    analyser = Analyser()

    idxmining = 0
    for line in miningPatterns:
        pattern = line.infos["motif Lily"]
        try:
            idx = expertPatterns.patterns.index(pattern)
            result = {}
            result["pattern"] = pattern
            result["idxExpert"] = idx
            result["idxMining"] = idxmining
            analyser.addResult(result)
        except ValueError:
            pass
        idxmining += 1

    return analyser

def isValid(p, ep):
    return p in ep.patterns


def findPatternsWithRevision(expertPatterns, miningPatternsList):
    """
    Retrouve la position des patterns experts avec révision du fichier
    :param expertPatterns:
    :param miningPatterns:
    :return:
    """
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
            miningPatterns.clearObsoletePatterns(miningPatternsList, stampsSet, patternList)

            # Suppression du pattern étudié
            #miningPatterns.remove(miningPatternsList, pattern)
            #miningPatternsList.remove(fullPattern)
            print(len(miningPatternsList))

    return analyser



def generateGraph(ra, rb, rc):
    x = list(range(len(ra)))

    a = []
    b = []
    c = []

    for elt in ra:
        a.append(elt[1])
    for elt in rb:
        b.append(elt[1])
    for elt in rc:
        c.append(elt[1])

    print(x)
    print(a)
    print(b)
    print(c)

    plt.figure(1)
    plt.plot(x, a, 'r')
    plt.plot(x, b, 'g')
    plt.plot(x, c, 'b')
    plt.xlabel('Itération')
    plt.ylabel('Rang du pattern')
    plt.title('Résultats')
    plt.show()


# CLASS ANALYSER
class Analyser:
    """
    Représentation d'un résultat d'analyse
    """

    def __init__(self):
        """
        :param results: contient l
        :return:
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
            w = csv.DictWriter(outfile, self.results[0].keys())
            w.writeheader()
            w.writerows(self.results)
