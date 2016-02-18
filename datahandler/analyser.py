#-*- coding: utf-8 -*-
from datahandler import expertPatterns
from datahandler import miningPatterns
import operator
from matplotlib import pyplot as plt
import numpy as np
import csv

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
        idxmining+=1

    return analyser

def findPatternsWithRevision(expertPatterns, miningPatterns):
    """
    """
    editedMP = miningPatterns
    linenumber = 0
    results = []
    for line in editedMP.results:
        pattern = line[1]
        try:
            idx = expertPatterns.patterns.index(pattern)
            # Start du cleanup
            # On supprime le patter de la liste
            #editedMP.results
            #for candidate in editedMP.results:
            #    print(candidate)
            print(pattern)
            print(line)
            timestamps = []
            timestamps.append(line[2].split(','))
            for i in range(13, len(line)):
                timestamps.append(line[i][2].split(','))

            flattimestamps = [y for x in timestamps for y in x]
            #print(timestamps)
            #print(flattimestamps)

            for candidate in editedMP.results:
                print("Candidate")
                print(candidate)
                print(len(candidate))
                # Traitement de la première occurrence

                # Traitement des autres occurrences
                for j in range(13,len(candidate)):
                    print("PLop")
                    ts = candidate[j][2].split(',')
                    print(ts)
                    for k in ts:
                        if k in flattimestamps:
                            print("Should be removed")
#                    remove
#                    print("Removed  ")

            # Mise à jour du patters
            element = []
            element.append(pattern)
            element.append(linenumber)
            element.append(idx)
            results.append(element)
        except ValueError:
            #print("Pattern non trouvé : "+pattern)
            pass
        linenumber+=1
    return results

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

