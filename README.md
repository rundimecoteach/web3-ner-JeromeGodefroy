#SPACY

##Introduction

le but ici est d'extraire les entités nommées à partir de plusieurs sources web. Le sujet de notre ontologie est l'Univers.


##Mise en oeuvre

Ainsi, nous avons 4 sites internets à propos de ce sujet. Avec BeautifulSoup (bs4), nous prenons que le texte du site.

Nous avons créé un fichier texte contenant les différentes URL de nos sources.

Le traitement de chaque url est effectué en utilisant Spacy, sur le modèle Anglais.

Nous filtrons les résultats afin d'avoir les entités attendues telles que la Terre ou la Lune,...

