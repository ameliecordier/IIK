#-*- coding: utf-8 -*-
import csv
import pprint

# UTILS
def groupByPack(it, n):
    """
    Récupère une liste et fait des paquets de taille n
    :param it: la liste
    :param n: la taille des paquets souhaités
    :return: un générateur de paquets
    """
    first = it[:n]
    yield first

    nextValue = it[n:]

    if nextValue:
        yield from groupByPack(it[n:], n)


def readRows(filename, firstSize, packSize):
    """
    Retourne un générateur de patterns à partir d'un fichier CSV
    :param filename: nom du fichier
    :param firstSize: taille du bloc d'infos générales
    :param packSize: taille d'un bloc d'infos sur une occurrence
    :return: générateur de Pattern avec les ints convertis
    """

    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=';',)
        headings = next(reader)
        infosHeadings = headings[:firstSize]
        occHeadings = headings[firstSize:firstSize+packSize]
        print(len(occHeadings))
        for row in reader:
            infos = row[:firstSize]
            occ = list(map(lambda  x : dict(zip(occHeadings, x)), groupByPack(row[firstSize:], packSize)))
            #yield (Pattern(dict(zip(infosHeadings, infos)), occ)).convertDataToInt()
            p = Pattern(dict(zip(infosHeadings, infos)), occ)
            p.dataPreprocessing()
            yield p


# CLASS PATTERN
class Pattern:
    """
    Représentation d'un pattern et toutes les données, issus du mining
    """
    def __init__(self, infos, occ):
        """
        Un pattern contient les infos communes puis une liste par occurrence
        :param infos: les infos générales sur le pattern (dans un dictionnaire)
        :param occ: listes de paquets d'infos pour chaque occurrence (dans un dictionnaire)
        """
        self.infos = infos
        self.occ = occ

    def __str__(self):
        """
        Affichage brut d'un pattern
        """
        return "Pattern(%r, %r)" % (self.infos, self.occ)

    def getNbOccs(self):
        """
        Retourne le nombre d'occurrences connues d'un pattern
        d'après le nombre de listes
        :return: int (nombre d'occurrences)
        """
        return len(self.occ)

    def dataPreprocessing(self):
        """
        Utilitaire de conversion des strings en int sur les données d'entrée
        Convertit également les stamps list en sets
        """
        def convertToInt(x):
            try:
                value = int(x)
            except:
                value = x
            return value

        for key, value in self.infos.items():
            self.infos[key] = convertToInt(value)
        for occ in self.occ:
            for keyocc, valueocc in occ.items():
                if keyocc == "Stamps list":
                    occ[keyocc] = set(list(map(int, valueocc.split(","))))
                else:
                    occ[keyocc] = convertToInt(valueocc)

    def printInfos(self):
        """
        Affiche les titres de colonnes d'infos sur les patterns
        """
        print("Infos :")
        print(self.infos.keys())

    def printOccInfos(self):
        """
        Affiche les titres des colonnes d'infos sur les occurrences
        """
        print("Infos des occurences")
        print(self.occ[0].keys())
