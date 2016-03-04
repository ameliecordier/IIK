# -*- coding: utf-8 -*-
import csv

from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def isValid(p, ep):
    return p in ep.patterns



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
