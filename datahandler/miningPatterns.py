# -*- coding: utf-8 -*-
import csv
from datahandler import analyser

# UTILS POUR LA LECTURE DU CSV
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


def readRows(filename, delimiter, firstSize, packSize):
    """
    Retourne un générateur de patterns à partir d'un fichier CSV
    :param filename: nom du fichier
    :param delimiter: délimiteur de csv
    :param firstSize: taille du bloc d'infos générales
    :param packSize: taille d'un bloc d'infos sur une occurrence
    :return: générateur de Pattern avec les ints convertis
    """

    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter, )
        headings = next(reader)
        infosHeadings = headings[:firstSize]
        occHeadings = headings[firstSize:firstSize + packSize]
        for row in reader:
            infos = row[:firstSize]
            occ = list(map(lambda x: dict(zip(occHeadings, x)), groupByPack(row[firstSize:], packSize)))
            p = Pattern(dict(zip(infosHeadings, infos)), occ)
            p.dataPreprocessing()
            yield p



# CLASS PATTERN
class Pattern:
    """
    Représentation d'un pattern et toutes les données issues du mining
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
            """
            Méthode locale de conversion des ints
            :param x: un élément de liste
            :return: le même élément converti en int si possible et non altéré sinon
            """
            try:
                value = int(x)
            except:
                value = x
            return value

        # Conversion en int des infos numériques
        for key, value in self.infos.items():
            self.infos[key] = convertToInt(value)
        # Conversion en int des infos d'occurences et, au passage,
        # regroupe les timestamps en sets
        for occ in self.occ:
            for keyocc, valueocc in occ.items():
                if len(valueocc) > 0:
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


# CLASS PATTERNS
class Patterns:
    """
    Représentation de l'ensemble des patterns
    """

    def __init__(self, mining, delimiter, firstSize, packSize):
        """
        Patterns représente une liste de patterns
        """
        self.patterns = list(readRows(mining, delimiter, firstSize, packSize))


    def getNbPatterns(self):
        """
        Nombre de patterns dans la structure
        :return: nombre de patterns dans la structure considérée
        """
        return len(self.patterns)


    def sortBy(self, criteria):
        """
         Trie la liste des patterns selon les colonnes et ordres passés en paramètres
         Exemples :
         miningPatterns.sortBy(rr, [("freq", "desc")])
         => trie par fréquence décroissante
         miningPatterns.sortBy(rr, [("freq", "desc"), ("cov int", "asc")])
         => trie par freq décroissante puis par cov int croissante
         :param criteria: liste de tuples (noms cols, ordre)
         :return: modifie l'objet courrant
         """

        # On inverse la liste des critères pour avoir au final un tri dans l'ordre naturel demandé
        criteria.reverse()
        for crit in criteria:
            # Détermine l'odre de tri
            if crit[1] == "asc":
                order = False
            else:
                order = True
            # Effectue le tri selon le critère courant
            self.patterns.sort(key=lambda pattern: pattern.infos[crit[0]], reverse=order)


    def printInfos(self):
        """
        Affiche les titres de colonnes d'infos sur les patterns
        (sur la base du premier pattern)
        """
        print("Infos :")
        print(self.patterns[0].infos.keys())


    def printOccInfos(self):
        """
        Affiche les titres des colonnes d'infos sur les occurrences
        (sur la base du premier pattern)
        """
        print("Infos des occurences")
        print(self.patterns[0].occ[0].keys())


    def findPatterns(self, expertPatterns):
        """
        Recherche dans les patterns minés les patterns identifiés par l'expert
        :param expertPatterns: la structure des patterns de l'expert
        :param miningPatterns: les patterns issus de la fouille
        :return analyser: un objet analyser
        """

        analyse = analyser.Analyser()

        for line in self.patterns:
            current_pattern = line.infos["motif Lily"]
            try:
                idx = expertPatterns.patterns.index(current_pattern)
                result = {}
                result["pattern mining"] = current_pattern
                result["pattern expert"] = expertPatterns.patterns[idx]
                result["idxExpert"] = idx
                result["idxMining"] = self.patterns.index(line)
                result["full pattern"] = line
                analyse.addResult(result)
            except ValueError:
                pass

        return analyse

    def findPatternsWithRevision(self, expertPatterns):
        """
        Recherche dans les patterns minés les patterns identifiés par l'expert, avec révision
        :param expertPatterns: la structure des patterns de l'expert
        :return analyser: un objet analyser
        """

        analyse = analyser.Analyser()

        # Constitution d'une liste de patterns à analyser
        patternList = [elt.infos["motif Lily"] for elt in reversed(self.patterns)]
        print("Pattern list : ", patternList)

        # On boucle tant qu'il reste des patterns à analyser
        while patternList:
            # Récupération du nom du pattern
            pattern = patternList.pop()
            print("Pattern removed", pattern)


            # Si c'est un pattern de l'expert, on note les résultats et on met à jour
            if pattern in expertPatterns.patterns:

                # Récupération des infos sur le pattern
                for elt in self.patterns:
                    if elt.infos["motif Lily"] == pattern:
                        fullPattern = elt
                        fullPatternIdx = self.patterns.index(elt)
                        break

                # Écriture des résultats dans l'analyseur
                result = {}
                result["pattern mining"] = pattern
                result["pattern expert"] = pattern
                result["idxExpert"] = expertPatterns.patterns.index(pattern)
                result["idxMining"] = fullPatternIdx
                result["full pattern"] = fullPattern
                analyse.addResult(result)

                for p in self.patterns:
                    print(p.infos["motif Lily"])

                 # Récupération de l'ensemble des occurrences de ce pattern (timestamps)
                stampsSet = [elt.get("Stamps list") for elt in fullPattern.occ]
                stampsSet = list(map(list, stampsSet))
                stampsSet = set([y for x in stampsSet for y in x])

                # Suppression du pattern courant
                self.patterns.remove(elt)


                # Nettoyage des autres occurrences
                pNb = 0
                while pNb < len(self.patterns):
                    occNb = 0
                    patate = self.patterns[pNb].infos["motif Lily"]
                    while occNb < len(self.patterns[pNb].occ):
                        try:
                            if stampsSet & self.patterns[pNb].occ[occNb]["Stamps list"]:
                                # On remove l'occurrence
                                del self.patterns[pNb].occ[occNb]
                                # On fait -1 à la fréquence
                                self.patterns[pNb].infos['freq'] -= 1
                                # Si la fréquence passe en dessous du seuil, on remove le pattern
                                if self.patterns[pNb].infos['freq'] < 14:
                                    pname = self.patterns[pNb].infos["motif Lily"]
                                    del self.patterns[pNb]
                                    try:
                                        patternList.remove(pname)
                                    except:
                                        pass
                                    pNb -=1
                                occNb -=1
                        except:
                            pass
                        occNb += 1
                    pNb +=1

        return analyse


    def toFile(self, filename):

        # Extraction des infos uniquement (pas les occurrences)
        toPrint = []
        for pattern in self.patterns:
            toPrint.append(pattern.infos)

        # Écriture du fichier résultat
        with open(filename, "w") as outfile:
            fieldnames = ['num', 'motif Lily', 'freq', 'cov evt', 'cov int', 'cov temp', 'l*f', 'long', 'support', 'bruit', 'motif dmt4sp',  'recov', 'clos' ]
            w = csv.DictWriter(outfile, delimiter=";", fieldnames=fieldnames)
            w.writeheader()
            w.writerows(toPrint)


