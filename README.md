# Jeu des 8 Dames (8 Queens Puzzle)

## Description du Projet
Un jeu interactif implémentant le célèbre problème mathématique des 8 dames, où le but est de placer 8 dames sur un échiquier de manière à ce qu'aucune dame ne puisse attaquer une autre.

## Fonctionnalités

### Placement des Dames
- Placez manuellement des dames sur l'échiquier en cliquant
- Validation en temps réel des positions des dames
- Vérification des conflits (attaques) entre les dames

### Algorithmes de Résolution
Deux algorithmes de résolution sont disponibles :
1. **Recuit Simulé (Simulated Annealing)**
   - Algorithme probabiliste de recherche de solution
   - Explore différentes configurations
   - Adaptatif et flexible

2. **Backtracking**
   - Algorithme de recherche exhaustive
   - Exploration systématique de toutes les possibilités
   - Garantit une solution si elle existe

### Commandes Clavier
- `Entrée` : Résoudre le problème des 8 dames
- `R` : Réinitialiser le plateau
- `S` : Passer en mode Recuit Simulé
- `B` : Passer en mode Backtracking

## Prérequis
- Python 3.10+
- Pygame 2.6.1+

## Installation

1. Clonez le dépôt
```bash
git clone <url-du-depot>
cd Intelligence Artificielle
```

2. Installez les dépendances
```bash
pip install -r requirements.txt
```

3. Lancez le jeu
```bash
python3 main.py
```

## Structure du Projet
```
Intelligence Artificille/
│
├── main.py           # Point d'entrée principal
├── Models/
│   ├── Board.py      # Logique de l'échiquier
│   └── Constant.py   # Constantes du jeu
└── AI/
    └── annealing.py  # Algorithmes de résolution
```

## Algorithmes

### Recuit Simulé
- Inspiré du recuit métallurgique
- Exploration probabiliste de l'espace des solutions
- Capacité d'échapper aux minimums locaux

### Backtracking
- Méthode de résolution par force brute
- Explore systématiquement toutes les configurations possibles
- Retourne en arrière quand une configuration est invalide

## Captures d'Écran
[Vous pouvez ajouter des captures d'écran ici]

## Collaborateur
RANDRIANASOLO Ialimeva Rindraniaina
RAVELONJANAHARY Tsanta Nomena Odon
RAKOTOZAFY Teddy Andrianina
ANDRIAMASINA Marcelo
Laurie Arthure

## Professeur
Madame Livaniaina

## Remerciements
- Communauté Pygame
- Algorithmes de résolution de problèmes
```