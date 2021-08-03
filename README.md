# Code-Stage-L3

## Ce code a été produit lors de mon stage de L3. Il permet l'analyse de fichier de séquençage de Nanopore Minion dans le cadre de l'étude de la régulation des isoformes cellulaires après infection par le VIH-1. 
## Le code se lance depuis Unix avec la ligne de commande: python3 Code_python_LD nomdufichier filtre1 filtre2 filtre3 filtre4 filtre5 filtre6 filtre7 filtre8
### Le filtre 1 permet de conserver les isoformes dont le log2 du fold change est supérieur à une certaine valeur
### Le filtre 2 permet de conserver les isoformes dont le log2 du fold change est inférieur à une certaine valeur
### Le filtre 3 permet de conserver les isoformes qui ont été détectées au moins un nombre de fois dans un des duplicats
### Le filtre 4 et 5 permet de récupérer que les isoformes connues
### Le filtre 6 permet de conserver les isoformes dans la p-value ajustée soient inférieures à une certaine valeur 
### Le filtre 7 permet de conserver les isoformes dont le fold change est supérieur à une certaine valeur 
### Le filtre 8 permet de conserver les isofromes dont le fold change est inférieur à une certaine valeur


