# Ce qui a été fait 29/06/2026

**objectifs** :
- avoir une structure modulaire dès le début pour développer/tester chaque composant de manière indépendante
- pouvoir remplacer facilement le modèle/prétraitement des données sans modifier le reste du code

1. Mise en place du squelette du projet pour structurer le **pipeline d'apprentissage**

2. Séparation des **différentes responsabilités** en plusieurs modules :
 - `dataset.py` pour le chargement des données
 - `model.py` pour la définition du modèle
 - `train.py` pour l'entrainement
 - `evaluate.py` pour l'évaluation
 - `main.py` le script principal qui lancera l'ensemble

Pour l'instant les fichiers sont connectés mais modèle et traitement de données seront à adapter une fois confirmation exacte des signaux EEG

**à faire** :
- déterminer le format exact des données EEG (dimensions des tenseurs) 
- implémenter l'architecture de réseau la plus adaptée (MLP, CNN 1D, EEGNet ...)
- finaliser les fonctions d'entraînement et d'évaluation 
- effectuer les premiers essais et ajuster les hyperparamètres

# Ce qui a été fait 30/06/2026

création de l'arborescence :

`data/`
- `raw/`
- `preprocessed/`
- `metadata/`

## Exploration des données 

Les données brutes :
- format : .edf 
- 41 canaux EEG 
- fréquence : 512 Hz 
- durée = 24 minutes

Les données prétraitées :
- 44 époques
- 41 canaux
- durée époque 10 secondes : réparties en 2 fenêtres -> 5-15s = 22 époques ; 25-35s = 22

a quoi correspondent S 1, S 2, S 6, S 7, S 11, S 12 CMS in range ?

métadonnées dispo :
- label
- duration
- tmin
- tmax
- segment_type : 5-15 ou 25-35

event + leur nombre :
- S12 : 12 
- S11 : 10 
- S1 : 6 
- S2 : 6 
- S6 : 4 
- S7 : 4 
- CMS in range : 2

signification expérimentale : condition sociale, contrôle, mouvement, repos....????

**chaque époque possède un code expérimental**

S6 = type événement/condition expérimentale
5A15 = segment de 5 à 15 secondes
25A35 = segment de 25 à 35 secondes

**type d'archi possible** :
- EEGNet 
- Shallow ConvNet 
- CNN 1D
à voir...