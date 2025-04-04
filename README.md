# Jeu des 8 Dames - IA

Ce projet implémente une solution au problème des 8 dames en utilisant deux algorithmes d'intelligence artificielle : le **recuit simulé** (Simulated Annealing) et le **backtracking**. L'application est développée en Python avec Pygame pour l'interface graphique.

---

## Table des matières

- [Jeu des 8 Dames - IA](#jeu-des-8-dames---ia)
  - [Table des matières](#table-des-matières)
  - [Description](#description)
  - [Prérequis](#prérequis)
  - [Installation](#installation)
  - [Utilisation](#utilisation)
    - [Interaction avec l'application](#interaction-avec-lapplication)
  - [Explication du code](#explication-du-code)
  - [IA](#ia)
    - [Recuit Simulé (Simulated Annealing)](#recuit-simulé-simulated-annealing)
    - [Backtracking](#backtracking)
  - [Explication des algorithmes](#explication-des-algorithmes)
    - [1. Recuit Simulé (Simulated Annealing)](#1-recuit-simulé-simulated-annealing)
    - [2. Backtracking](#2-backtracking)
  - [Structure du projet](#structure-du-projet)
  - [Contribuer](#contribuer)

---

## Description

Le problème des 8 dames consiste à placer 8 dames sur un échiquier 8x8 de manière à ce qu'aucune dame ne puisse en attaquer une autre (pas sur la même ligne, colonne ou diagonale). Ce projet propose :

- Une interface graphique pour interagir avec l'échiquier.
- Deux algorithmes pour résoudre le problème automatiquement.
- La possibilité de placer ou déplacer des dames manuellement.

---

## Prérequis

- Python 3.6 ou supérieur
- Bibliothèques Python :
  - `pygame`
  - `psutil`
  - `numpy`

---

## Installation

1. Clonez le dépôt :

   ```bash
   git clone <URL-du-dépôt>
   cd <nom-du-dépôt>
   ```

2. Installez les dépendances :

   ```bash
   pip install pygame psutil numpy
   ```

3. (Optionnel) Placez une image `queen.png` dans le dossier `assets/images/` pour représenter les dames. Sinon, une représentation par défaut sera utilisée.
4. Lancez le programme :

   ```bash
   python main.py
   ```

---

## Utilisation

### Interaction avec l'application

- **Démarrage** : Exécutez `python main.py` pour ouvrir la fenêtre graphique.
- **Interaction manuelle** :
  - **Clic gauche** : Cliquez sur une case pour placer une dame (si moins de 8 dames sont présentes) ou sélectionner/déplacer une dame existante.
  - Une fois une dame sélectionnée, cliquez sur une autre case pour la déplacer.
- **Commandes clavier** :
  - `a` : Lance l'algorithme de recuit simulé.
  - `b` : Lance l'algorithme de backtracking.
  - `r` : Réinitialise l'échiquier (supprime toutes les dames).
  - `q` : Ferme l'application.
- **Affichage** :
  - Le titre "Jeu des 8 Dames" est affiché en haut.
  - L'état de l'algorithme (énergie, température, étapes, temps) apparaît en bas à gauche.
  - Les instructions clavier sont affichées en bas.

---

## Explication du code

Le projet est structuré de manière modulaire :

- **`main.py`** :
  - Point d'entrée du programme.
  - Initialise Pygame et la fenêtre graphique.
  - Gère les événements et met à jour l'affichage.
  - Exécute les algorithmes dans des threads séparés pour ne pas bloquer l'interface.
- **`models/board.py`** :
  - Classe `Board` représentant l'échiquier.
  - Gère le placement, le déplacement et la suppression des dames.
  - Vérifie la validité d'une solution et calcule les conflits.
- **`models/piece.py`** :
  - Classe `Piece` pour représenter les dames (position, affichage).
- **`models/constants.py`** :
  - Définit les constantes du projet (taille de l'échiquier, couleurs, paramètres IA).
- **`ai/annealing.py`** :
  - Implémentation du recuit simulé.
- **`ai/backtracking.py`** :
  - Implémentation du backtracking.

---

## IA

Le projet intègre deux approches d'intelligence artificielle :

### Recuit Simulé (Simulated Annealing)

- Méthode probabiliste inspirée du refroidissement des métaux.
- Explore l'espace des solutions et accepte parfois des états moins optimaux.
- Paramètres principaux : température initiale, taux de refroidissement.
- **Avantages** : Trouve souvent une solution rapidement.
- **Inconvénients** : Pas toujours optimal, sensible aux paramètres.

### Backtracking

- Approche déterministe qui construit la solution pas à pas.
- Explore toutes les solutions possibles en revenant en arrière si nécessaire.
- **Avantages** : Garantie de trouver une solution.
- **Inconvénients** : Peut être plus lent.

---

## Explication des algorithmes

### 1. Recuit Simulé (Simulated Annealing)

- **Principe** : Inspiré de la métallurgie, il explore l'espace des solutions en acceptant parfois des états moins bons pour éviter les minima locaux.
- **Fonctionnement** :
  - Commence avec une configuration aléatoire.
  - Génère un état voisin en déplaçant une dame.
  - Accepte le nouvel état selon la formule de Metropolis : `exp(-ΔE/T)`.
  - La température diminue progressivement.

### 2. Backtracking

- **Principe** : Algorithme exhaustif qui place les dames colonne par colonne.
- **Fonctionnement** :
  - Place une dame dans une colonne en vérifiant les conflits.
  - Passe à la colonne suivante si valide, sinon revient en arrière.
  - Continue jusqu'à remplir l'échiquier ou épuiser les possibilités.

---

## Structure du projet

```
├── ai/
│   ├── annealing.py        # Implémentation du recuit simulé
│   └── backtracking.py     # Implémentation du backtracking
├── models/
│   ├── board.py           # Classe de l'échiquier
│   ├── constants.py       # Constantes du projet
│   └── piece.py           # Classe des pièces (dames)
├── assets/
│   └── images/            # Dossier pour les images (ex: queen.png)
└── main.py                # Point d'entrée du programme
```

---

## Contribuer

Toute contribution est la bienvenue !

- **Forkez** le projet.
- **Créez** une branche.
- **Apportez** vos modifications.
- **Soumettez** une Pull Request.

Merci et bon codage ! 🎯
