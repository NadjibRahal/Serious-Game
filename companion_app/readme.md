# ECO-FACTORY CHALLENGE Companion App

Bienvenue dans le **Companion App ECO-FACTORY CHALLENGE**, une application Python conçue pour accompagner et améliorer votre expérience de jeu. Cette application offre une interface conviviale pour gérer vos ressources, usines, technologies, travailleurs et terrains, tout en surveillant la pollution et les coûts associés.

## Table des Matières

- [Description](#description)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Fonctionnalités](#fonctionnalités)
- [Contribution](#contribution)
- [Licence](#licence)
- [Remerciements](#remerciements)

## Description

**ECO-FACTORY CHALLENGE Companion App** est une application de bureau développée en Python avec Tkinter, visant à fournir aux joueurs un outil puissant pour gérer et optimiser leur empire industriel écologique. Grâce à cette application, vous pouvez :

- Ajouter et gérer jusqu'à 4 joueurs.
- Acheter et attribuer des terrains avec des ressources spécifiques.
- Construire, supprimer et gérer des usines en fonction des terrains et des ressources disponibles.
- Acheter et gérer des technologies pour améliorer l'efficacité et réduire la pollution.
- Embaucher, assigner et gérer des travailleurs spécialisés.
- Suivre la production, la consommation et le commerce de ressources.
- Calculer les pollutions et les coûts liés à vos activités industrielles.
- Simuler des tours de jeu et visualiser les performances finales.

## Prérequis

Avant d'installer et d'utiliser l'application, assurez-vous d'avoir les éléments suivants :

- **Python 3.x** : Téléchargez et installez Python depuis [python.org](https://www.python.org/downloads/).
- **Tkinter** : Généralement inclus avec les installations Python standard. Si ce n'est pas le cas, vous pouvez l'installer via votre gestionnaire de paquets.

## Installation

1. **Télécharger le Code Source**

   Téléchargez le fichier `eco_factory_challenge.py` depuis le dépôt ou la source fournie.

2. **Vérifier les Prérequis**

   Assurez-vous que Python 3.x est installé sur votre système. Vous pouvez vérifier cela en ouvrant un terminal ou une invite de commande et en tapant :

   ```bash
   python --version
   ```

   ou

   ```bash
   python3 --version
   ```

3. **Installer Tkinter (si nécessaire)**

   Si Tkinter n'est pas installé, vous pouvez l'installer en fonction de votre système d'exploitation :

   - **Windows** : Tkinter est généralement inclus avec Python sur Windows.
   - **macOS** : Tkinter est inclus avec Python sur macOS.
   - **Linux** : Utilisez votre gestionnaire de paquets. Par exemple, sur Debian/Ubuntu :

     ```bash
     sudo apt-get install python3-tk
     ```

## Utilisation

1. **Naviguer vers le Répertoire**

   Ouvrez un terminal ou une invite de commande et naviguez vers le répertoire contenant le fichier `eco_factory_challenge.py`.

   ```bash
   cd chemin/vers/le/dossier
   ```

2. **Lancer l'Application**

   Exécutez le script Python pour lancer l'application.

   ```bash
   python eco_factory_challenge.py
   ```

   ou

   ```bash
   python3 eco_factory_challenge.py
   ```

3. **Interface Utilisateur**
   - **Sélection du Joueur** : Ajoutez des joueurs en cliquant sur "Add Player" et sélectionnez le joueur actif depuis le menu déroulant.
   - **Navigation par Onglets** : Utilisez les onglets en haut de la fenêtre pour accéder aux différentes sections telles que Dashboard, Terrain, Factories, Technologies, Workers, Resources, et Pollution & Costs.

## Fonctionnalités

### Dashboard

- Vue d'ensemble des Eco-Credits (EC), Pollution Points (PP) et Carbon Credits pour le joueur sélectionné.

### Terrain

- Visualiser tous les terrains disponibles avec leurs types, coûts, ressources et propriétaires.
- Acheter des terrains pour accéder à des ressources spécifiques et bénéficier de réductions de carbone.

### Factories

- Ajouter des usines depuis une liste pré-définie en sélectionnant le type d'usine et le terrain associé.
- Gérer les usines existantes, y compris la suppression et la modification.
- Assigner des types de transport pour les ressources nécessaires à la production.

### Technologies

- Acheter des technologies pour améliorer l'efficacité des usines et réduire la pollution.
- Gérer les technologies acquises, y compris la suppression avec remboursement partiel.

### Workers

- Embaucher des travailleurs spécialisés tels qu'Ingénieurs, Techniciens, Conseillers Environnementaux et Travailleurs Universels.
- Assigner des travailleurs aux usines en fonction des besoins.
- Gérer les travailleurs existants, y compris la suppression.

### Resources

- Suivre la production, la consommation et le commerce des ressources.
- Effectuer des échanges de ressources avec la banque.

### Pollution & Costs

- Calculer les coûts et la pollution générés par les activités industrielles.
- Simuler des tours de jeu pour voir l'impact économique et environnemental.
- Terminer le jeu après un nombre défini de tours et afficher les scores finaux.

## Contribution

1. Fork le dépôt.
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`).
3. Commit vos changements (`git commit -m 'Add some AmazingFeature'`).
4. Push la branche (`git push origin feature/AmazingFeature`).
5. Ouvrez une Pull Request.

