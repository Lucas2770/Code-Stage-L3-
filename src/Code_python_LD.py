"""
Ce code permet l'analyse de fichier de séquençages de Nanopore Minion
afin d'étudier la régulation de l'utilisation différentielle des exons.

date: 3/08/2021
auteur: Lucas Domingues
"""


import re
import sys

def filtredexeq(file,logfc_sup,logfc_inf, suppartie, word1, word2 , valpadj):
    """
    fonction qui filtres selon des critères de pvalue, de types de gènes,
    de minimum de ride, et de fold change
    des données de Minion sur les isoformes des celulles sinfectées ou contrôle
    """
    pathout=file.replace("data/ctl_vs_inf_DEXseq2_ok_num_complet.txt",\
                         "results/ctl_vs_inf_DEXseq2_ok_num_complet_LD.txt")
    pathout2="/Users/victordomingues/Desktop/src/results/compte.txt"
    regex = re.compile("[0-9]+.[0-9]+")
    with open (file,"r") as filtre, open(pathout, "w") as fileout, open (pathout2,"a") as resume:
        filtre= filtre.readlines()
        number=0
        for index, line  in enumerate(filtre):
            if index == 0:
                fileout.write(line)
            else:
                line=line.split("\t")
                logfc=line[-1].rstrip()
                if regex.search(logfc):
                    logfc=float(logfc.replace(",","."))
                    if logfc >=logfc_sup or logfc<=logfc_inf:
                        maxride=line[-5].replace(",",".")
                        if float(maxride)>=suppartie:
                            texte=line[0]
                            if word1 not in texte:
                                if word2 not in texte :
                                    padj=float(line[6].replace(",","."))
                                    if padj <= valpadj and padj !=0:
                                        line=("\t").join(line)
                                        number=number+1
                                        fileout.write(line)
        file=file.split("/")
        newline=file[-1]+" => "+str(number)+"\n"
        resume.write(newline)

def fichieresume (file, rapportfc,inverserapportfc):
    """
    fonction qui résume à partir du filtre précédent les isoformes
    les plus différentiellement régulées
    """
    file2=file.replace("data/ctl_vs_inf_DEXseq2_ok_num_complet.txt",\
                       "results/ctl_vs_inf_DEXseq2_ok_num_complet_LD.txt")
    pathout=file2.replace(".txt", "_resume.txt")
    with open (file2,"r") as filtre, open(pathout, "w") as fileout:
        filtre= filtre.readlines()
        for index, line in enumerate (filtre):
            line=line.rstrip()
            line=line.split("\t")
            newline=line[0:4]
            newline[0]=line[1]
            newline[1]=line[2]
            newline[2]=line[-3]
            newline[3]=line[-4]
            if index == 0:
                newline=("\t").join(newline)+"\n"
                fileout.write(newline)
            else:
                meantat=newline[2].replace(",",".")
                meantat=float(meantat)
                meandtat=float(newline[3].replace(",","."))
                if meantat !=0 or meandtat != 0:
                    fcrapp=(meantat)/(meandtat)
                    inversefc=(meandtat)/(meantat)
                    newline=("\t").join(newline)+"\n"
                    if inversefc < inverserapportfc or fcrapp > rapportfc:
                        fileout.write(newline)

def main():
    """
    fonction qui permet de lancer le code à partir du terminal
    """
    file=sys.argv[1]
    logfc_sup = float(sys.argv[2])
    logfc_inf= float(sys.argv[3])
    suppartie= float(sys.argv[4])
    word1= sys.argv[5]
    word2= sys.argv[6]
    valpadj= float(sys.argv[7])
    rapportfc= float(sys.argv[8])
    inverserapportfc= float(sys.argv[9])
    filtredexeq (file,logfc_sup,logfc_inf, suppartie, word1, word2 , valpadj)
    fichieresume (file, rapportfc,inverserapportfc)


if __name__ == "__main__":
    main()
