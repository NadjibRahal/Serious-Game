eco_factory_challenge/
├── main.py                 # Point d'entrée du jeu, initialise et lance la boucle de jeu
├── constants.py            # Constantes du jeu (couleurs, dimensions, textes, etc.)
├── game.py                 # Classe principale du jeu, gère la logique, les tours, etc.
├── player.py               # Classe pour les joueurs (gestion de la main, des ressources, etc.)
├── card.py                 # Classe pour les cartes (définition des types, effets, etc.)
├── deck.py                  # Classe pour le paquet de cartes 
├── board.py                 # Classe pour représenter le plateau de jeu
├── ui.py                   # Fonctions et classes pour l'interface utilisateur (affichage, boutons, etc.)
├── utils.py                # Fonctions utilitaires diverses
├── resources/              # Dossier pour les ressources
│   ├── images/             # Images des cartes, du plateau, des icônes, etc.
│   │   ├── card_fronts/    # Images pour le recto des cartes
│   │   ├── card_backs/     # Images pour le verso des cartes
│   │   └── ...
│   ├── fonts/              # Polices de caractères
│   │   └── ...
│   └── sounds/             # Effets sonores et musique
│       └── ...
├── tests/                  # Dossier pour les tests unitaires
│   ├── __init__.py
│   ├── test_game.py
│   ├── test_player.py
│   └── ...
├── .gitignore              # Fichier pour ignorer les fichiers non nécessaires dans le suivi de version (Git)
└── README.md               # Fichier de description du projet
