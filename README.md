

# Pierre Feuille Ciseaux

Ce code a été rédigé durant pour les cours Administration Système et gestion de code (4ETI) en février 2024 à CPE Lyon majeure robotique.
## Fonctionnement

## Installation
Le code a été rédigé avec Python 3.10.12

1. Cloner le dépôt depuis GitHub :
   ```bash
   git clone git@github.com:Darksasuke02/RPS_PARTIE2_4ETI_AdmCO_20232024.git
   ```

2. Créer un environnement virtuel
Pour télécharger venv sur Ubuntu (souvent déjà inclus dans le téléchargement de Python)
```console
sudo apt install python3-venv
```

Pour créer et utiliser un environnement virtuel:
```console
# Pour créer mon_environnement
python3 -m venv mon_environnement

# Pour activer mon_environnment 
source mon_environnement/bin/activate
#Vous pouvez désormais télécharger vos modules

# Pour désactiver mon_environnment
deactivate
```



3. Installer les dépendances 
```bash
pip install setuptools
```
unittest est sont présent dans la bibliothèque standart python il ne faut rien installer

4. Ajouter le package Game
```bash
pip install -e .
#ou
pip install -e chemin/vers/game
```
Tout fonctionne vous pouvez lancer testop.py

## Tests
Les tests s'exécutent en lancant le fichier testop.py du package test. Il ont été automatisé avec le module python unittest

