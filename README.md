# Pierre Feuille Ciseaux

Ce code a été rédigé durant pour les cours Administration Système et gestion de code (4ETI) en février 2024 à CPE Lyon majeure robotique.
## Fonctionnement

Ce code permet donc de jouer à pierre feuille ciseaux, deux modes de jeux sont disponible le mode joueur simple qui se fait contre un ordinateur (mode ordi), et le mode de jeux 2 joueurs ou (mode 1v1), le choix du mode de jeux se fait au départ à l'aide d'un input utilisateur. Afin de jouer correctement il suffit de lancer rps_simplegame.py avec Python3. Le reste du jeux se fait avec des inputs console utilisateur. Pour quitter le jeux rentrer "no" après la fin d'une manche.
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
unittest est présent dans la bibliothèque standart python il ne faut rien installer

4. Ajouter le package Game
```bash
pip install -e .
#ou
pip install -e chemin/vers/game
```
Tout fonctionne vous pouvez lancer testop.py

## Fonctionnalité 1

Cette fonctionnalité permet de gérer les différents mode de jeux ici mode joueur simple et deux joueurs (1v1).

#### 1. Organisation du code

Le code étant développé par uniquement par moi même et cette fonctionnalité étant au coeur du fonctionnement général du projet. Elle a été développé sur une branche develop puis merge sur main afin de pouvoir publier une version fonctionnelle avec un tag
#### 2. Gestion des erreurs

Il y a différent types d'erreurs possible pour les erreurs qui sont liée aux inputs uitlisateurs, l'input sur le choix pierre feuille ou ciseaux (R,P,S) ne raise aucune erreur en cas de mauvais input, mais relance simplement la question avec un re.match si l'input ne correspondait pas aux attentes.

Pour ce qui est de l'input Yes ou No pour relancer ou quitter le jeu, Il raise bien une erreur mais l'utilisation d'un try execept permet à cette erreur de ne pas être bloquante?

La mise en place des test a été facilité par la mise en place de fake inputs, si jamais il y a erreur dans ces fakes input il y a un raise d'erreur qui cette fois est bloquant.
#### 3. Retour Pylint

Après toute les modifications possibles, le score final de pylint pour cette version est de 9.70/10 pour le module de test (testrps.py), de 10/10 pour le module de gestion des parties (rps_simplegame.py). Et de 9.52 pour le module de gestion des manches (rps_game.py)

#### 4. Les tests

Les tests s'exécutent en lancant le fichier testrps.py. Il ont été automatisé avec le module python unittest. 
Ils ont été particulièrement difficile à mettre en place notamment à cause d'erreurs fondamentale dans l'architecture et l'agencement du code. Il y a de nombreux inputs bloquant dans le module qui traite les manches ce qui pose ce qui rend la mise en place de tests très laborieux.
Finalement seul un petit nombre de test sur la méthode rps_play du module rps_game ont pu être mis en place.

La gestion de problématiques liée aux problèmes de codes n'étant pas l'objectif du module, mes codes de tests rentent incomplet et à améliorer.

#### 5. L'automatisation des tests et création du .whl

Pour tester, une copie du repository a été faite sur gitlab.
tout fonctionne correctement à la fois le test et la création de .whl.

![illustration](images/testauto.png)



