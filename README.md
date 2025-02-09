# Script de Fusion de Tables d'Oiseaux

## Description
Ce script Python effectue une fusion de données à partir de plusieurs fichiers CSV contenant des informations sur les oiseaux. Il combine les données de trois fichiers CSV d'entrée et génère deux fichiers de sortie :
1. `Oiseaux3.csv` : Données fusionnées des deux premiers fichiers d'entrée
2. `bilan_oiseaux.csv` : Table finale fusionnée avec les noms d'oiseaux, la première couleur et la deuxième couleur

## Prérequis
- Python 3.x
- Bibliothèques standard de Python (csv, os)

## Fichiers d'Entrée
Le script attend trois fichiers CSV d'entrée :
1. `Oiseaux1.csv`
2. `Oiseaux2.csv`
3. `couleur2.csv`

Chaque fichier doit être un CSV avec les en-têtes appropriés.

## Utilisation
1. Dézippez le projet
2. Assurez-vous que tous les fichiers CSV d'entrée sont dans le même répertoire que le script
3. Exécutez le script : `python oiseaux.py`
4. Vérifiez les fichiers de sortie : `Oiseaux3.csv` et `bilan_oiseaux.csv`

## Fonctionnalités
- Lecture sécurisée des fichiers avec gestion des erreurs
- Jointure de tables efficace
- Support de l'encodage UTF-8
- Messages d'erreur informatifs

## Dépannage
- Vérifiez les noms et emplacements des fichiers CSV d'entrée
- Assurez-vous que les fichiers CSV ont les en-têtes attendus
- Vérifiez que Python 3.x est installé