## **1. Présentation du jeu


**Concept :** Eco-Factory Challenge est un jeu de plateau stratégique où 4 joueurs s'affrontent pour développer l'industrie la plus prospère tout en minimisant leur impact environnemental. Le jeu combine des mécaniques de gestion de ressources, de développement technologique et de prise de décision économique, le tout dans un contexte de sensibilisation aux enjeux écologiques. Les joueurs jouent le rôle d'un entrepreneur a partir de zero. 

**Objectif :**  Le gagnant est le joueur qui obtient le meilleur ratio capital/pollution à la fin de la partie, lorsque toutes les ressources sont épuisées.

**Mécaniques principales :**

*   **Plateau de jeu :** Représente un territoire avec des ressources réparties aléatoirement.
*   **Budget initial :** Limité, obligeant les joueurs à faire des choix stratégiques.
*   **Achat de terrains :** Les terrains proches des ressources sont plus chers mais réduisent les coûts de transport.
*   **5 types d'éléments :**
    *   **Usines :** Permettent de transformer les ressources.
    *   **Ressources :** Matériaux nécessaires à la production.
    *   **Transports :** Déplacement des ressources et des produits finis (choix entre électrique et hydrocarbure).
    *   **Travailleurs :** Main-d'œuvre nécessaire au fonctionnement des usines.
    *   **Technologies :** Améliorations et innovations influençant l'efficacité, les coûts et l'impact environnemental (voir tableau des technologies).
*   **Système d'achat :** Permet d'acquérir des terrains, des usines, des technologies, etc.
*   **Gestion des ressources :** Optimisation de l'extraction, du transport et de la transformation des ressources.
*   **Pollution :** Générée par les activités industrielles, impacte le score final via la taxe carbone.
*   **Cartes Technologie :** Offrent des avantages économiques et environnementaux, avec des coûts d'investissement et de maintenance (voir détail des cartes plus bas).

**Versions :**

*   **Version physique (DIY) :** Plateau de jeu, pions, cartes, etc. fabriqués manuellement.
*   **Version virtuelle :** Développement d'une version numérique du jeu avec des fonctionnalités automatisées.


## **Détails de la version numérique**

La version numérique d'Eco-Factory Challenge sera développée en tant que **jeu de cartes** utilisant la bibliothèque **Pygame** en Python. Voici les choix techniques et la structure du code :

*   **Langage de programmation :** Python
*   **Bibliothèque :** Pygame
*   **Type d'interaction :** Jeu de cartes et plateau au tour par tour, 4 joueurs sur le même ordinateur.
*   **Données des cartes :** Les données des cartes etc sont stockées dans des fichiers **JSON** externes. Cela permet de modifier facilement les caractéristiques des cartes sans altérer le code du jeu, facilitant ainsi l'équilibrage.
*   **Gestion des tours :** Le jeu se déroule au tour par tour (round). Chaque joueur effectue ses actions pendant son tour, puis passe la main au joueur suivant.
*   **Interface utilisateur :** L'interface utilisateur est conçue pour être claire et intuitive, avec des informations visuelles sur l'état du jeu (ressources, pollution, main du joueur, etc.) et des boutons pour les actions possibles.

**Enjeux clés :**

1. **Ressources et efficacité :**
    *   L'industrie est une grande consommatrice de ressources naturelles (matières premières, eau, énergie). L'épuisement de ces ressources et la volatilité de leurs prix incitent à une utilisation plus efficiente et au développement de l'économie circulaire (réutilisation, recyclage, valorisation des déchets).
    *   L'optimisation des processus industriels, l'éco-conception des produits et la réduction des pertes sont des leviers essentiels pour améliorer l'efficacité des ressources.
    *   Les choix d'approvisionnement sont déterminant sur les flux de ressources et les coûts.

2. **Énergie et climat :**
    *   L'industrie est responsable d'une part importante des émissions de gaz à effet de serre. La transition vers des sources d'énergie renouvelables (solaire, éolien, biomasse) et l'amélioration de l'efficacité énergétique sont cruciales pour réduire l'empreinte carbone du secteur.
    *   La capture et le stockage du carbone sont des technologies émergentes qui pourraient jouer un rôle dans la décarbonation de l'industrie.

3. **Pollution et impacts environnementaux :**
    *   Les activités industrielles génèrent diverses formes de pollution (air, eau, sol) qui affectent les écosystèmes et la santé humaine. La réduction des émissions polluantes, le traitement des effluents et la gestion des déchets dangereux sont des priorités environnementales.
    *   L'évaluation de l'impact environnemental des produits et des processus industriels, tout au long de leur cycle de vie, permet d'identifier les points d'amélioration et de minimiser les impacts négatifs.

4. **Innovation et technologies vertes :**
    *   Le développement de technologies propres et innovantes est un facteur clé de la transition vers une industrie durable. Les investissements dans la recherche et le développement, ainsi que le soutien aux start-ups et aux PME innovantes, sont essentiels pour stimuler l'innovation verte.
    *   L'automatisation, la digitalisation et l'intelligence artificielle offrent des opportunités d'optimisation des processus industriels et de réduction de l'impact environnemental.

5. **Responsabilité sociale et gouvernance :**
    *   Les entreprises ont une responsabilité sociale et environnementale croissante. La transparence, l'éthique, le dialogue avec les parties prenantes et la prise en compte des impacts sociaux et environnementaux dans les décisions stratégiques sont des éléments clés d'une gouvernance responsable.
    *   Les normes et les certifications environnementales (ISO 14001, EMAS) peuvent aider les entreprises à structurer leur démarche environnementale et à améliorer leur performance.
