#-*- coding: utf-8 -*-
from datahandler import expertPatterns
from datahandler import miningPatterns
import operator
from matplotlib import pyplot as plt
import numpy as np



def sortBy(col, reversed, mp):
    """
    Trie un résultat de type miningPatterns par la colonne choisie
    :param col: la colonne selon laquelle trier (int)
        possibilités pour col :
            0 : rang brut
            4 : fréquence
            7 : couverture
    :param reversed: ordre croissant ou décroissant
        reversed = True => tri décroissant
        reversed = False => tri croissant
    :param mp: un objet de type miningPatterns
    :return: un objet de type miningPatterns
    """
    mpFreq = miningPatterns.MiningPatterns()
    mpFreq.results = sorted(mp.results, key=lambda x: int(operator.itemgetter(col)(x)), reverse=reversed)
    return mpFreq


def findPatterns(expertPatterns, miningPatterns):
    """
    Recherche dans les patterns minés les patterns identifiés par l'expert
    :param expertPatterns: la structure des patterns de l'expert
    :param miningPatterns: les patterns issus de la fouille
    :return: TODO
    """
    linenumber = 0
    results = []
    for line in miningPatterns.results:
        pattern = line[1]
        try:
            idx = expertPatterns.patterns.index(pattern)
            element = []
            element.append(pattern)
            element.append(linenumber)
            element.append(idx)
            results.append(element)
        except ValueError:
            print("Pattern non trouvé : "+pattern)
            pass
        linenumber+=1
    return results

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



