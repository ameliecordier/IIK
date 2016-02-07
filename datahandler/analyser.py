#-*- coding: utf-8 -*-
from datahandler import expertPatterns
from datahandler import miningPatterns
import operator


def sortByFreq(mp):
    """
    Trie un résultat de type miningPatterns par fréquence
    Retourne un objet de type miningPatterns
    :param mp: un objet de type miningPatterns
    :return:
    """
    mpFreq = miningPatterns.MiningPatterns()
    mpFreq.results = sorted(mp.results, key=lambda x: int(operator.itemgetter(4)(x)), reverse=True)
    return mpFreq

def sortByCouv(mp):
    """
    Trie un résultat de type miningPatterns par couverture
    Retourne un objet de type miningPatterns
    :param mp: un objet de type miningPatterns
    :return:
    """
    mpFreq = miningPatterns.MiningPatterns()
    mpFreq.results = sorted(mp.results, key=lambda x: int(operator.itemgetter(7)(x)), reverse=True)
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



