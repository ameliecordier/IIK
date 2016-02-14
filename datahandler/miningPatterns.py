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
        assert len(nextValue) >= n
        yield from groupByPack(it[n:], n)

def readRows(filename, firstSize, packSize):
    """
    Retourne un générateur de patterns à partir d'un fichier CSV
    :param filename: nom du fichier
    :param firstSize: taille du bloc d'infos générales
    :param packSize: taille d'un bloc d'infos sur une occurrence
    :return: générateur de Pattern
    """
    #assert len(columnNames) == firstSize

    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=';',)
        headings = next(reader)
        infosHeadings = headings[:firstSize]
        occHeadings = headings[firstSize:firstSize+packSize]
        print(len(occHeadings))
        for row in reader:
            infos = row[:firstSize]
            occ = list(map(lambda  x : dict(zip(occHeadings, x)), groupByPack(row[firstSize:], packSize)))
            yield Pattern(dict(zip(infosHeadings, infos)), occ)


# CLASS PATTERN
class Pattern:
    """
    Représentation d'un pattern et toutes les données, issus du mining
    """
    def __init__(self, infos, occ):
        """
        Un pattern contient les infos communes puis une liste par occurrence
        :param infos: les infos générales sur le pattern
        :param occ: les paquets d'infos pour chaque occurence
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

    def convertDataToInt(self):
        # TODO : could be
        # TODO : ou alors, on déplace dans la création des listes
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
                occ[keyocc] = convertToInt(valueocc)

