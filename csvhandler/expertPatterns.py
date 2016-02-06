#-*- coding: utf-8 -*-
import csv
import pprint

"""
Classe de manipulation des patterns experts
Le fichier CSV est supposé sans entêtes
La liste des patterns est une liste de strings, séparées par des virgules
Exemple : ep = ['la,si,la,sold', 'la,si,do,si']
"""

class ExpertPatterns:

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