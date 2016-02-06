#-*- coding: utf-8 -*-
import csv
import pprint

class ExpertPatterns:

    def __init__(self):
        self.patterns = []

    def getPatterns(self, filename):
        """
        Récupère une liste de patterns depuis un fichier CSV sans entête
        :param filename: nom du fichier CSV
        :return: liste de strings (une string = un pattern Lily)
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