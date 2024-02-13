# SUJET_PARTIE2_4ETI_AdmCO_20232024

## Sujet : Jeu de Pierre/Feuille/Ciseaux
![RPS](images/RPS_m.jpg)

Votre rendu sera un unique dépôt Git. Vous devrez définir et justifier l'organisation des branches, l'utilisation ou non de branches `dev`, de branches liées aux fonctionnalités, de branches distinctes pour les versions, ou l'utilisation de tags.


Testez le code `RPS_jeu.py`. Il vous servira d'inspiration pour la suite.vous (Vous pouvez aussi sauter cette étape)

Pour chaque fonctionnalité, vous devrez :

1. **Préciser vos choix concernant la gestion des retours** : en particulier, comment gérez-vous les éventuelles erreurs ?
1. **Coder la classe et le package associé** : cela doit être accessible sur la branche principale de votre projet.
1. **Afficher les choix sur le code final de la classe** : après diverses corrections liées aux retours de Pylint. Affichez votre score et le retour de Pylint.
1. **Faire un gros effort sur les commentaires** : utilisez intensivement les docstrings.
1. **Mettre en place la logique des tests associés**.
1. **Procéder à la génération du whl** (1).
1. **Automatiser les phases de test et de création du .whl sur GitLab** (2).
1. **Autres ...**

### Fonctionnalité 1

Le but est de mettre en forme le code précédent pour jouer à Pierre/Feuille/Ciseaux et de créer un package.

- Créez un package `Game`.
- Proposez un module `RPS_Game`.
- Créez un sous-module `RPS_Tools` contenant une classe :
  - Créez une classe `RPS_SimpleGame`.

#### RPS_SimpleGame

Cette classe propose deux méthodes :

1. `SimplegameTwoplayers(player1choice, player2choice)` : retourne 0 en cas d'égalité, 1 si le joueur 1 gagne et 2 si le joueur 2 gagne.
2. `SimplegameOneplayer(player1choice)` : retourne 0 en cas d'égalité (même choix aléatoire fait par l'ordinateur), 1 si le joueur gagne ou 2 si l'ordinateur gagne.
   - `player1choice` et `player2choice` sont des caractères 'R', 'P' ou 'S'.

### Fonctionnalité 2

Créez une seconde classe `RPS_MultipleGame`. Dans cette classe, un joueur humain joue contre l'ordinateur en gardant une trace des parties précédentes. Cette classe utilisera la classe `RPS_SimpleGame`, plus précisément la méthode `SimplegameTwoplayers`. On souhaite stocker (à vous de définir comment) à la fois les anciennes parties pour analyse et avoir un historique récent pour la prise de décision. Il peut être pertinent d'associer les parties à des joueurs "identifiés".

### Fonctionnalité 3

L'ordinateur pourra alors utiliser l'historique des parties précédentes pour proposer une stratégie non aléatoire. Faites une proposition de structuration de code. Vous pourrez proposer une ou plusieurs stratégies qui utilisent cet historique.

---
**Note**:

- Assurez-vous de créer des fichiers README.md pour chaque branche ou fonctionnalité, expliquant clairement les changements et la logique derrière eux.
- Utilisez des outils d'intégration continue pour automatiser les tests et la génération de fichiers `.whl`.
