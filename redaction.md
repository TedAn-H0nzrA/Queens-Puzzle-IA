# Résolution du Problème des 8 Dames : Une Approche Multi-Algorithmique

## 1. Introduction

Le problème des 8 dames est un défi classique en intelligence artificielle et en algorithmique, consistant à placer 8 dames sur un échiquier de 8x8 sans qu'aucune dame ne puisse en attaquer une autre. Notre projet vise à résoudre ce problème en utilisant deux approches algorithmiques distinctes : le recuit simulé (Simulated Annealing) et le backtracking.

## 2. Environnement de Développement

### 2.1 Choix Technologiques

#### Pygame
- **Raison du choix**: Pygame offre une bibliothèque graphique légère et performante pour le développement de jeux et d'interfaces interactives en Python.
- **Avantages**:
  - Gestion simplifiée des événements graphiques
  - Performance optimale pour les applications en temps réel
  - Compatible avec les algorithmes de recherche de solutions

#### Python
- **Justification du langage**:
  - Syntaxe claire et lisible
  - Excellentes bibliothèques scientifiques et de calcul
  - Rapidité de prototypage
  - Performance suffisante pour les algorithmes de recherche

### 2.2 Configuration Technique
- Version Python : 3.10+
- Version Pygame : 2.6.1+
- Plateforme : Multiplateforme (Windows, macOS, Linux)

## 3. Algorithmes de Résolution

### 3.1 Recuit Simulé (Simulated Annealing)

#### Principe
Le recuit simulé est un algorithme probabiliste inspiré du processus métallurgique de recuit. Il permet d'explorer l'espace des solutions de manière adaptative, en acceptant parfois des solutions sous-optimales pour éviter les minimums locaux.

#### Caractéristiques
- **Exploration probabiliste**: Capacité d'échapper aux configurations localement piégées
- **Paramètres dynamiques**: 
  - Température initiale élevée
  - Taux de refroidissement progressif
- **Critère de Metropolis**: Acceptation de solutions moins bonnes avec une probabilité décroissante

#### Avantages
- Flexibilité algorithmique
- Probabilité de trouver des solutions globales
- Adapté aux problèmes combinatoires complexes

### 3.2 Backtracking

#### Principe
Le backtracking est une méthode de recherche exhaustive par force brute, explorant systématiquement toutes les configurations possibles et revenant en arrière dès qu'une configuration est invalide.

#### Caractéristiques
- **Recherche systématique**: Exploration exhaustive de l'espace des solutions
- **Algorithme déterministe**: Garantit une solution si elle existe
- **Stratégie de retour arrière**: Annulation immédiate des configurations invalides

#### Avantages
- Complétude garantie
- Simplicité conceptuelle
- Performance pour les espaces de recherche limités

## 4. Comparaison des Approches

### 4.1 Performance
- **Recuit Simulé**:
  - + Rapidité de convergence
  - + Moins sensible aux configurations initiales
  - - Solution non garantie
- **Backtracking**:
  - + Solution garantie
  - + Précision
  - - Temps de calcul potentiellement long

### 4.2 Cas d'Usage
- **Recuit Simulé**: Problèmes complexes, optimisation
- **Backtracking**: Problèmes avec solutions définitives, espaces restreints

## 5. Conclusion

Notre projet démontre la complémentarité des approches algorithmiques en intelligence artificielle. Le choix de Python et Pygame nous a permis de créer une interface interactive illustrant ces méthodes de résolution.

Les algorithmes de recuit simulé et de backtracking offrent des perspectives différentes mais complémentaires pour résoudre des problèmes combinatoires complexes.

## Bibliographie
- Russell, S., & Norvig, P. (2009). Artificial Intelligence: A Modern Approach.
- Kirkpatrick, S., et al. (1983). Optimization by Simulated Annealing.
- Pearl, J. (1984). Heuristics: Intelligent Search Strategies for Computer Problem Solving.

## Annexes
- Code source du projet
- Captures d'écran de l'interface

## Fonction heuristique
1-Heuristique de conflit
But : Minimiser le nombre de reines qui se menacent mutuellement
Calcul : Nombre de paires de reines qui partagent une ligne, colonne ou diagonale
Valeur optimale : 0 (aucun conflit)

2-Heuristique de placement
Position initiale : Placement stratégique de la première reine
Distribution : Éviter de placer les reines trop proches
Équilibre : Assurer une répartition uniforme sur le plateau

3-Heuristique de distance
Distance minimale : Maintenir une distance optimale entre les reines
Diagonales : Éviter les alignements diagonaux
Zones sûres : Maximiser les cases non menacées

4-Critères d'évaluation

Score = W1 * (Nombre de conflits) +
        W2 * (Distribution spatiale) +
        W3 * (Nombre de cases menacées)

Où:
- W1, W2, W3 sont des poids d'importance
- Score plus bas = meilleure solution


5-Contraintes à respecter
Une seule reine par ligne
Une seule reine par colonne
Pas de reines sur la même diagonale
Total de 8 reines sur le plateau

6-Stratégies de recherche
Pour le recuit simulé :

Température initiale élevée pour exploration large
Refroidissement progressif pour convergence
Acceptation de solutions moins bonnes possible

Pour le backtracking :

Placement séquentiel ligne par ligne
Vérification immédiate des conflits
Retour en arrière si conflit détecté

7-Retour en arrière si conflit détecté
Métriques de performance
Temps d'exécution
Utilisation mémoire
Nombre d'itérations
Taux de réussite

Ces heuristiques guident l'implémentation des algorithmes dans votre code et assurent :

Une recherche efficace de solutions
Une convergence plus rapide
Une meilleure qualité des solutions trouvées
Une utilisation optimale des ressources