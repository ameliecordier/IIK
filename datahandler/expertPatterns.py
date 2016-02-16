#-*- coding: utf-8 -*-
import csv
import pprint


class ExpertPatterns:
    """
    Classe de manipulation des patterns experts
    Le fichier CSV est supposé sans entêtes
    La liste des patterns est une liste de strings, séparées par des virgules.
    Exemple : ep = ['la,si,la,sold', 'la,si,do,si']
    """


    def __init__(self):
        self.patterns = []

    def getPatterns(self, filename):
        """
        Récupère une liste de patterns depuis un fichier CSV sans entête
        remplit patterns par une liste de strings (une string = un pattern Lily)
        :param filename: nom du fichier CSV
        """
        with open(filename, newline='') as csvfile:
            linereader = csv.reader(csvfile, delimiter=',')
            for row in linereader:
                self.patterns.append(','.join(row))

    def printPatterns(self):
        """
        Affiche simplement la liste des patterns sur la sortie standard
        """
        pprint.pprint(self.patterns)

    def getSetOfObselTypes(self):
        """
        Récupère un set de types d'obsels
        :return: retourne le set des types d'obsels
        """
        temp = list(map(lambda x: x.split(","), self.patterns))
        setOfObsels = set([y for x in temp for y in x])

        return setOfObsels