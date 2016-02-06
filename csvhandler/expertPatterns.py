#-*- coding: utf-8 -*-
import csv
import pprint

def getPatternList(filename):
    """
    Récupère une liste de patterns depuis un fichier CSV sans entête
    :param filename: nom du fichier CSV
    :return: liste de strings (une string = un patter)
    """
    with open(filename, newline='') as csvfile:
        linereader = csv.reader(csvfile, delimiter=',')
        pattern = []
        for row in linereader:
            pattern.append(','.join(row))
    return pattern
