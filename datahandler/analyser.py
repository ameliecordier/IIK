#-*- coding: utf-8 -*-
from datahandler import expertPatterns
from datahandler import miningPatterns
import operator


def sortBy(col, mp):
    """
    Trie un résultat de type miningPatterns par la colonne choisie
    :param col: la colonne selon laquelle trier (int)
        possibilités pour col :
            0 : rang brut
            4 : fréquence
            7 : couverture
    :param mp: un objet de type miningPatterns
    :return: un objet de type miningPatterns
    """
    mpFreq = miningPatterns.MiningPatterns()
    mpFreq.results = sorted(mp.results, key=lambda x: int(operator.itemgetter(col)(x)), reverse=True)
    return mpFreq


def findPatterns(expertPatterns, miningPatterns):
    """
    Recherche dans les patterns minés les patterns identifiés par l'expert
    :param expertPatterns: la structure des patterns de l'expert
    :param miningPatterns: les patterns issus de la fouille
    :return: TODO
    """
    for line in miningPatterns.results:
        pattern = line[1]
        try:
            idx = expertPatterns.patterns.index(pattern)
            print("Pattern fouillé : "+ pattern)
            print("Pattern expert : "+expertPatterns.patterns[idx])
        except ValueError:
            print("Pattern non trouvé : "+pattern)
            pass



