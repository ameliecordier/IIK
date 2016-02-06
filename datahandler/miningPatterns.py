#-*- coding: utf-8 -*-
import csv
import pprint

class MiningPatterns:
    """
    headings contient les entêtes de colonnes
    results est une liste de patterns.
    Chaque ligne de results est structurée de la façon suivante :
    results[0] : numéro de motif
    results[1] : motif Lily
    results[2] : motif dmt4sp
    results[3] : longueur
    results[4] : frequence
    results[5] : longueur * fréquence
    results[6] : fermé ou non
    results[7] : couverture événementielle
    results[8] - results[12] : données DMT4SP
    results[13+i] - fin : occurrences
       results[13+i][0] : estampille de début du motif
       results[13+i][1] : estampille de fin du motif (pas besoin)
       results[13+i][2] : liste des estampilles de l'occurrence de motif
       results[13+i][3] - results[13+i][fin] : données DMT4SP
    """

    def __init__(self):
        # On a deux modes : raw pour les tests, et normal pour le fonctionnement classique
        self.rawHeadings = []
        self.rawResults = []
        self.headings = []
        self.results = []

    def getMiningResults(self, filename):
        """
        Initialise headings et results avec leurs contenus respectifs
        :param filename: non du fichier
        """
        with open(filename, newline='') as csvfile:
            linereader = csv.reader(csvfile, delimiter=";")
            self.headings = next(linereader)

            for row in linereader:
                pos = 0
                lenLine = len(row)
                pattern = []
                while pos < 13: # Traitement des colonnes 1 à 13
                    pattern.append(row[pos])
                    pos += 1
                while pos < lenLine:
                    occurence = []
                    for i in range(11):
                        occurence.append(row[pos+i])
                    pattern.append(occurence)
                    pos += 11
                self.results.append(pattern)

    def printMiningResults(self):
        pprint.pprint(self.headings)
        pprint.pprint(self.results)

    def exportResults(self, filename):
        """
        Écriture des résultats dans un fichier dont le nom doit être passé en paramètre
        """
        with open(filename, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=';')
            for line in self.results:
                csvwriter.writerow(line)

    """
    Tout ce qui est "raw" est là à des fins de debug uniquement,
    et n'est donc pas testé
    """
    def getRawMiningResults(self, filename):
        """
        Remplit la liste contenant les headers, et les résultats non structurés
        :param filename: nom du fichier CSV
        """
        with open(filename, newline='') as csvfile:
            linereader = csv.reader(csvfile, delimiter=';')
            self.rawHeadings = next(linereader)

            for row in linereader:
                self.rawResults.append(row)

    def printRawHeading(self):
        pprint.pprint(self.rawHeadings)

    def printRawResults(self):
        pprint.pprint(self.rawResults)


