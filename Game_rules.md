```markdown
# DÉFI ÉCO-USINE (CONCEPTION)

## 1. VUE D'ENSEMBLE & PRINCIPALES AMÉLIORATIONS

**Objectif**  
Construire le réseau industriel le plus économiquement performant tout en étant durable. Les joueurs s'efforcent d'obtenir le meilleur *Ratio Capital-Pollution* à la fin du jeu.

1. **Mécaniques de Transport**
   - **Types** : Transport électrique et aux combustibles fossiles.
   - **Coûts & Pollution** : Les coûts de transport et la pollution varient en fonction de la distance et du type.

2. **Gestion des Ressources**
   - **Ressources** : Minéraux, Bois, Pétrole, Eau, Plastiques.
   - **Allocation des Ressources** : Les usines nécessitent des ressources spécifiques à chaque tour pour fonctionner.
   - **Distribution des Ressources** : Les ressources sont liées à des tuiles de terrain spécifiques.

3. **Coûts et Pollution Basés sur la Distance**
   - **Calcul de la Distance** : Nombre de tuiles entre la ressource et l'usine.
   - **Impact** : Augmentation des coûts opérationnels et de la pollution en fonction de la distance de transport.

4. **Carte**
   - **Distribution des Ressources** : Chaque tuile de terrain fournit certaines ressources.
   - **Placement Stratégique** : Les joueurs doivent placer stratégiquement les usines près des ressources ou investir dans le transport.


---

## 2. COMPOSANTS

### 2.1 Plateau & Terrain

- **Disposition du Plateau** : Une grille **4×5** de tuiles de terrain (20 tuiles au total), idéale pour 4 joueurs.
- **Types de Terrain** :
  1. **Plaines (P)** : 
     - **Ressources** : Bois, Eau.
     - **Caractéristiques** : Coût moyen, bon pour l'agriculture, construction modérée.
  2. **Forêt (F)** :
     - **Ressources** : Bois.
     - **Caractéristiques** : Coût plus élevé, production de bois, sert de puits de carbone.
  3. **Montagne (M)** :
     - **Ressources** : Minéraux, Pétrole.
     - **Caractéristiques** : Riche en minéraux et pétrole, risque de pollution élevé.
  4. **Côtier (C)** :
     - **Ressources** : Eau, Pétrole.
     - **Caractéristiques** : Coût moyen, accès aux routes maritimes, possible captage de carbone.
  5. **Urbain (U)** :
     - **Ressources** : Plastiques, Eau.
     - **Caractéristiques** : Coût élevé, grande capacité d'usine, taxes sur la pollution potentielles plus élevées.

Chaque tuile affiche :
- **Coût d'Achat** (par exemple, 200–350 EC).
- **Potentiel de Ressources** (par exemple, Minéraux, Bois).
- **Compensation de Carbone** si laissée partiellement non développée (par exemple, Forêt ou zones reboisées).

### 2.2 Monnaies & Suivi

- **Eco-Credits (EC)** : Monnaie principale pour toutes les transactions.
- **Points de Pollution (PP)** : Une seule piste pour la pollution totale (englobant air, eau, etc.).

### 2.3 Transport

- **Types** :
  1. **Transport Électrique** :
     - **Coût** : 50 EC par unité de distance.
     - **Pollution** : 1 PP par unité de distance.
  2. **Transport aux Combustibles Fossiles** :
     - **Coût** : 30 EC par unité de distance.
     - **Pollution** : 3 PP par unité de distance.

- **Mise en Œuvre** :
  - **Calcul de la Distance** : Distance de Manhattan entre la tuile de ressource et la tuile de l'usine.
  - **Utilisation** : Chaque usine nécessitant des ressources de tuiles éloignées doit investir dans le transport.

### 2.4 Usines

Chaque carte d'usine comprend :
- **Nom** (par exemple, Assemblage de Panneaux Solaires, Installation Minière, Centre de Recyclage).
- **Coût de Construction** (EC).
- **Coût Opérationnel** (EC par tour).
- **Exigences en Ressources** (ressources spécifiques nécessaires à chaque tour).
- **Production** (produits ou services par tour).
- **Pollution de Base** (PP par tour).
- **Exigence d'Espace** (certaines usines peuvent partager une tuile si une technologie spécifique est utilisée).
- **Besoins en Transport** : 
  - **Type** : Électrique ou Combustibles Fossiles.
  - **Distance** : Nombre de tuiles depuis chaque ressource requise.

### 2.5 Technologies

- **Cartes de Technologie** : Chaque carte a :
  - **Nom**
  - **Effet sur les Usines ou le Terrain**
  - **Coût** (Initial + Maintenance)
  - **Modificateur de Pollution**
  - **Prérequis** (optionnel ; moins qu'avant)

### 2.6 Travailleurs

Un système de travailleurs simplifié :
- **Rôles** :
  - **Ingénieur**
  - **Technicien**
  - **Conseiller Environnemental**
  - **Travailleur Universel**
- **Affectation** : Les travailleurs sont affectés aux usines pour améliorer la production ou réduire la pollution.

### 2.7 Résumé des Changements dans Cette Révision

- **Mécaniques de Transport** : Introduction des transports électriques et aux combustibles fossiles avec coûts et pollution associés.
- **Gestion des Ressources** : Les usines nécessitent désormais des ressources spécifiques à chaque tour, avec des coûts basés sur la distance de transport.
- **Types de Ressources** : Standardisation en Minéraux, Bois, Pétrole, Eau, Plastiques.
- **Impact de la Distance** : Les coûts opérationnels et la pollution prennent désormais en compte la distance que les ressources doivent parcourir.

---

## 3. RÈGLES DE JEU RÉVISÉES COMPLÈTES

### 3.1 Installation du Jeu

1. **Disposition du Plateau**
   - Disposez une grille **4×5** de tuiles de terrain face visible (20 au total).
   - Chaque tuile montre son coût, ses types de ressources et son potentiel de compensation de carbone.

2. **Ressources de Départ des Joueurs**
   - Chaque joueur commence avec **1500 EC**.
   - Chaque joueur a initialement **0 PP**.

3. **Draft de Terrain**
   - Dans l'ordre de jeu (alphabétique ou autre méthode équitable), chaque joueur sélectionne **2 tuiles** à acheter.
   - Payer le coût d'achat en EC de départ.
   - Exemple de coûts d'achat : Plaines 200 EC, Forêt 250 EC, Montagne 300 EC, Côtier 250 EC, Urbain 350 EC.
   - Si une tuile est trop chère, passer ou acheter une moins chère jusqu'à ce que chacun ait 2 tuiles.

4. **Construction Optionnelle de la Première Usine**
   - Chaque joueur peut construire **1** usine sur n'importe laquelle de ses tuiles de terrain.
   - Payer le coût de construction.
   - Optionnellement embaucher **1** travailleur (Ingénieur, Technicien ou Conseiller Environnemental) lors de l'installation.

5. **Technologie de Départ (Optionnel)**
   - Révéler 3 cartes de technologie.
   - Chaque joueur peut en acheter **une** au début s'il le souhaite.

### 3.2 Structure du Tour

Chaque tour de jeu se compose de **4 phases**, répétées pour **4–6 tours** jusqu'à ce qu'un déclencheur de victoire convenu soit atteint :

1. **Phase de Production**
   - **Opérer les Usines** : 
     - Les usines produisent des biens/services si les exigences en ressources sont satisfaites.
     - Affecter les travailleurs : Chaque travailleur peut staffer une seule usine par tour.
     - Payer les coûts opérationnels + générer la pollution de base.
     - Gérer le transport : Affecter le type de transport et calculer les coûts et la pollution en fonction de la distance.

2. **Phase de Construction & Technologie**
   - **Acheter de Nouvelles Tuiles** : Si disponibles, acheter des tuiles de terrain supplémentaires.
   - **Construire de Nouvelles Usines ou Améliorations** : Placer des usines sur le terrain possédé ou améliorer les existantes.
   - **Acheter ou Implémenter des Cartes de Technologie** : Acquérir des technologies pour améliorer les opérations ou réduire la pollution.

3. **Phase de Commerce & Négociation**
   - **Échanger des Ressources** : Vendre des biens à la banque à des prix de base ou négocier des échanges avec d'autres joueurs.
   - **Personnaliser les Transactions** : Exemple : « Je te donne 2 Bois pour 1 Matériau Recyclé. »
   - **Échanges de Travailleurs** : Négocier les affectations ou échanges de travailleurs si les règles maison le permettent.

4. **Phase de Maintenance & Pollution**
   - **Calculer la Pollution Totale** :
     - Additionner la pollution des opérations des usines.
     - Inclure la pollution du transport basée sur le type de transport et la distance.
   - **Taxe Carbone** : Payer **5 EC × (Total PP)**.
   - **Appliquer l'Atténuation de la Pollution** :
     - Technologies, compensations forestières, crédits carbone.
   - **Payer les Dépenses** :
     - Salaires des travailleurs.
     - Maintenance des usines.
     - Coûts de transport.
     - Maintenance des technologies.
   - **Ajuster le Capital** : Déduire les dépenses des EC du joueur.

**Fin du Tour** : Vérifier les déclencheurs de victoire. Si non atteints, passer au tour suivant.

### 3.3 Conditions de Fin de Jeu & Victoire

1. **Limite de Tours** : Le jeu se termine généralement après le **6ème tour** ou plus tôt si :
   - Toutes les tuiles de ressources sont achetées et en grande partie épuisées.
   - Les joueurs conviennent mutuellement d'arrêter (par exemple, plus de mouvements stratégiques possibles).

2. **Score Final**
   - **Capital** : EC restants.
   - **Pollution Totale** : Somme de tous les PP.
   - **Score** : Capital ÷ (1 + Pollution Totale).
   - **Vainqueur** : Le score le plus élevé gagne.

### 3.4 Système d'Économie, de Transport & de Pollution

1. **Ressources**
   - **Types** : Minéraux, Bois, Pétrole, Eau, Plastiques.
   - **Allocation** : Chaque tuile de terrain fournit des ressources spécifiques.
   - **Utilisation** : Les usines nécessitent des ressources spécifiques à chaque tour pour fonctionner.

2. **Mécaniques de Transport**
   - **Livraison des Ressources** : Les usines doivent transporter les ressources requises depuis leurs tuiles sources.
   - **Type de Transport** : Choisir entre Transport Électrique ou aux Combustibles Fossiles.
   - **Impact de la Distance** :
     - **Coût** : 
       - Électrique : 50 EC × distance.
       - Combustibles Fossiles : 30 EC × distance.
     - **Pollution** :
       - Électrique : 1 PP × distance.
       - Combustibles Fossiles : 3 PP × distance.
   - **Calcul de la Distance** : Distance de Manhattan (somme des pas horizontaux et verticaux) entre la tuile de ressource et la tuile de l'usine.
   - **Mise en Œuvre** : Affecter le transport pour chaque ressource dont une usine a besoin à chaque tour.

3. **Pollution**
   - **Sources** :
     - Opérations des usines (pollution de base).
     - Transport.
   - **Réduction** :
     - Conseillers Environnementaux.
     - Cartes de Technologie.
     - Crédits carbone provenant de projets verts.

4. **Mécanique de Rattrapage**
   - **Crédits Carbone** : Investir dans la reforestation ou les technologies vertes pour gagner des crédits.
   - **Utilisation** : Compense la taxe carbone ou vendre à d'autres joueurs.

### 3.5 Système de Travailleurs Simplifié

- **Ingénieur**
  - **Salaire** : 50 EC/tour
  - **Avantage** : +20% de production dans les usines avancées, ou +10% dans les usines de base.
  
- **Technicien**
  - **Salaire** : 30 EC/tour
  - **Avantage** : Maintient la production de base. Requis pour certaines usines.
  
- **Conseiller Environnemental**
  - **Salaire** : 40 EC/tour
  - **Avantage** : -3 PP dans l'usine à laquelle il est affecté. Requis pour les améliorations vertes avancées.
  
- **Travailleur Universel**
  - **Salaire** : 20 EC/tour
  - **Avantage** : Aide minimale à la production ; aucun bonus spécial de pollution ou d'efficacité.

*(Les travailleurs peuvent être réaffectés chaque tour selon les besoins.)*

### 3.6 Règles/Améliorations Supplémentaires

1. **Marché**
   - **Vendre des Produits Finis** : Prix de base fixes (par exemple, 50 EC par unité).
   - **Échanges entre Joueurs** : Négocier des accords personnalisés.
   - **Pas de Fluctuations d'Offre/Demande** : Accélère le gameplay.

2. **Améliorations Rationalisées**
   - **Améliorations des Usines** : Chaque usine peut avoir jusqu'à **2 améliorations**.
   - **Coûts des Améliorations** : Coût universel (par exemple, 200 EC pour installer, 10 EC/tour de maintenance).
   - **Effets** : Réduction de la pollution, augmentation de la production, efficacité du transport.

3. **Développement Plus Rapide du Terrain**
   - **Densité des Usines** :
     - **Standard** : 1 grande usine par tuile.
     - **Technologie d'Infrastructure Compacte** : 2 petites usines par tuile.
   - **Avantages** : Expansion plus rapide sans avoir besoin de multiples nouvelles tuiles.

4. **Optimisation du Transport**
   - **Transport en Vrac** : Affecter plusieurs ressources à une seule route de transport pour optimiser les coûts et la pollution.
   - **Synergies Technologiques** : Certaines technologies peuvent réduire les coûts ou la pollution du transport.

---

## 4. CARTES DE TECHNOLOGIE 

1. **Réseau Hybride Solaire-Éolien**
   - **Catégorie** : Énergie Renouvelable
   - **Coût** : 250 EC pour installer, 20 EC/tour de maintenance
   - **Effet** : Réduit le coût opérationnel d'une usine de 10 EC/tour et la pollution de 3 PP.
   - **Prérequis** : Aucun

2. **Module d'Automatisation Avancée**
   - **Catégorie** : Optimisation des Processus
   - **Coût** : 200 EC pour installer, 15 EC/tour de maintenance
   - **Effet** : +20% de production dans cette usine.
   - **Prérequis** : Ingénieur doit être affecté pour superviser.

3. **Système de Capture de Carbone**
   - **Catégorie** : Contrôle de la Pollution
   - **Coût** : 250 EC, 20 EC/tour de maintenance
   - **Effet** : -6 PP de l'usine assignée chaque tour.
   - **Prérequis** : Conseiller Environnemental sur place.

4. **Amélioration de Synthèse de Bioplastiques**
   - **Catégorie** : Chimie Verte
   - **Coût** : 200 EC, 10 EC/tour
   - **Effet** : Transforme certaines ressources agricoles ou en bois en Bioplastiques de valeur supérieure. +10 EC par produit vendu de cette usine.
   - **Prérequis** : Accès au Bois/Agriculture.

5. **Unité de Recyclage Industriel**
   - **Catégorie** : Gestion des Déchets
   - **Coût** : 200 EC, 15 EC/tour
   - **Effet** : Convertit les déchets de l'usine en Matériaux Recyclés pouvant être vendus ou utilisés. +5 EC/tour et -3 PP.
   - **Prérequis** : Technicien requis.

6. **Système d'Eau en Circuit Fermé**
   - **Catégorie** : Contrôle de la Pollution
   - **Coût** : 150 EC, 10 EC/tour
   - **Effet** : -2 PP de la pollution de l'eau, économise 5 EC/tour en frais d'élimination.
   - **Prérequis** : Conseiller Environnemental sur place.

7. **Logistique d'Intégration Verticale**
   - **Catégorie** : Logistique
   - **Coût** : 300 EC, 20 EC/tour
   - **Effet** : Gérer jusqu'à 2 usines sur la même tuile (synergie Infrastructure Compacte). +5 EC/tour en économies de transport.
   - **Prérequis** : Aucun

8. **Agriculture Urbaine sur les Toits**
   - **Catégorie** : Agriculture / Urbain
   - **Coût** : 100 EC, 5 EC/tour
   - **Effet** : Sur une tuile Urbaine, produire +2 unités de produits frais avec une pollution minimale (+1 PP).
   - **Prérequis** : Aucun

9. **Réseau de Transport Électrique**
   - **Catégorie** : Transport
   - **Coût** : 200 EC, 10 EC/tour
   - **Effet** : Réduit la pollution du transport de 50% pour les routes de Transport Électrique.
   - **Prérequis** : Déblocage de Technologie.

10. **Subvention aux Combustibles Fossiles**
    - **Catégorie** : Politique Économique
    - **Coût** : 150 EC, 5 EC/tour
    - **Effet** : Réduit les coûts de transport aux Combustibles Fossiles de 10 EC par unité de distance.
    - **Prérequis** : Aucun


---

## 5. CARTES D'USINE


1. **Camp de Coupe de Bois**
   - **Coût de Construction** : 150 EC
   - **Coût Opérationnel** : 20 EC/tour
   - **Pollution** : 3 PP
   - **Production** : 2 unités de Bois/tour (seulement sur une tuile Forêt)
   - **Exigence en Ressources** : Aucune
   - **Transport** : N/A
   - **Travailleur** : 1 Technicien recommandé

2. **Ferme Agricole**
   - **Coût de Construction** : 200 EC
   - **Coût Opérationnel** : 25 EC/tour
   - **Pollution** : 2 PP
   - **Production** : 3 unités d'Eau/tour (seulement sur une tuile Plaines, ou Côtier avec irrigation appropriée)
   - **Exigence en Ressources** : Aucune
   - **Transport** : N/A
   - **Travailleur** : 1 Travailleur Universel ou 1 Technicien pour un bonus de +1 unité

3. **Mine & Fonderie**
   - **Coût de Construction** : 300 EC
   - **Coût Opérationnel** : 40 EC/tour
   - **Pollution** : 8 PP
   - **Production** : 2 unités de Minéraux/tour
   - **Exigence en Ressources** : Nécessite des Minéraux
   - **Transport** : Doit transporter les Minéraux vers l'usine.
   - **Travailleur** : 1 Technicien

4. **Usine de Bioplastiques**
   - **Coût de Construction** : 250 EC
   - **Coût Opérationnel** : 30 EC/tour
   - **Pollution** : 5 PP
   - **Production** : 2 unités de Plastiques/tour (nécessite 1 entrée en Bois ou Eau/tour)
   - **Exigence en Ressources** : Bois ou Eau
   - **Transport** : Affecter le transport en fonction de la source de la ressource.
   - **Travailleur** : 1 Conseiller Environnemental recommandé pour réduire la pollution

5. **Assemblage de Panneaux Solaires**
   - **Coût de Construction** : 300 EC
   - **Coût Opérationnel** : 25 EC/tour
   - **Pollution** : 3 PP
   - **Production** : 2 unités de Panneaux Solaires/tour (Urbain ou Plaines)
   - **Exigence en Ressources** : Aucune
   - **Transport** : N/A
   - **Travailleur** : 1 Ingénieur pour capacité maximale

6. **Usine d'Éoliennes**
   - **Coût de Construction** : 350 EC
   - **Coût Opérationnel** : 30 EC/tour
   - **Pollution** : 4 PP
   - **Production** : 1 unité d'Éolienne/tour (peut être vendue pour 70 EC)
   - **Exigence en Ressources** : Aucune
   - **Transport** : N/A
   - **Travailleur** : 1 Ingénieur, 1 Technicien recommandé

7. **Centre de Recyclage**
   - **Coût de Construction** : 200 EC
   - **Coût Opérationnel** : 20 EC/tour
   - **Pollution** : 4 PP
   - **Production** : 1 unité de Matériaux Recyclés/tour
   - **Exigence en Ressources** : Plastiques
   - **Transport** : Affecter le transport en fonction de la source de la ressource.
   - **Travailleur** : 1 Technicien

8. **Usine de Fabrication Urbaine**
   - **Coût de Construction** : 300 EC
   - **Coût Opérationnel** : 35 EC/tour
   - **Pollution** : 6 PP
   - **Production** : 2 unités de Biens Manufacturés/tour (nécessite 2 entrées en Minéraux ou Recyclés)
   - **Exigence en Ressources** : Minéraux ou Matériaux Recyclés
   - **Transport** : Affecter le transport en fonction de la source de la ressource.
   - **Travailleur** : 1 Ingénieur, 1 Technicien

9. **Pêcherie Durable**
   - **Coût de Construction** : 250 EC
   - **Coût Opérationnel** : 20 EC/tour
   - **Pollution** : 2 PP
   - **Production** : 2 unités d'Eau/tour (seulement sur une tuile Côtier)
   - **Exigence en Ressources** : Eau
   - **Transport** : Affecter le transport en fonction de la source de la ressource.
   - **Travailleur** : 1 Travailleur Universel

10. **Agence de Conseil Écologique**
    - **Coût de Construction** : 150 EC
    - **Coût Opérationnel** : 15 EC/tour
    - **Pollution** : 1 PP (déchets de bureau)
    - **Production** : Services de conseil d'une valeur de +20 EC/tour s'ils sont vendus à d'autres joueurs ou au marché.
    - **Exigence en Ressources** : Aucune
    - **Transport** : N/A
    - **Travailleur** : 1 Conseiller Environnemental recommandé

---

## 6. RÔLES DES TRAVAILLEURS 

1. **Ingénieur**
   - **Salaire** : 50 EC/tour
   - **Avantage** : +20% de production dans les usines avancées, ou +10% dans les usines de base.

2. **Technicien**
   - **Salaire** : 30 EC/tour
   - **Avantage** : Maintient la production de base. Certaines usines nécessitent au moins 1.

3. **Conseiller Environnemental**
   - **Salaire** : 40 EC/tour
   - **Avantage** : -3 PP dans l'usine à laquelle il est affecté. Requis pour les améliorations vertes avancées.

4. **Travailleur Universel**
   - **Salaire** : 20 EC/tour
   - **Avantage** : Aide minimale à la production ; aucun bonus spécial de pollution ou d'efficacité.

*(Les travailleurs peuvent être réaffectés chaque tour selon les besoins.)*

---

## 7. TUTORIEL POUR LES JOUEURS

### 7.1 Exemple d'Installation

1. **Disposer le Plateau**
   - Mélangez ou disposez les 20 tuiles de Terrain (4×5). Chaque tuile est face visible, montrant son coût, ses types de ressources et son potentiel de compensation de carbone.

2. **Distribuer les EC de Départ**
   - Chaque joueur prend **1500 Eco-Credits**.

3. **Draft de Terrain**
   - Dans l'ordre de jeu, choisissez **2 tuiles chacun**.
   - Payer le coût d'achat en EC de départ.
   - Marquer les tuiles achetées avec votre couleur.

4. **Usine Initiale & Travailleur**
   - Optionnellement, construire **1 usine** sur l'une de vos 2 tuiles. Payer son coût de construction.
   - Optionnellement, embaucher **1 travailleur** (Ingénieur, Technicien ou Conseiller Environnemental).

5. **Révéler 3 Cartes Tech**
   - Chaque joueur peut acheter **1** si désiré. Payer le coût et noter les frais de maintenance.

### 7.2 Exemple de Jeu (Structure du Tour)

Passons en revue un tour d'exemple.

#### Phase 1 : Production
- **Opérer les Usines** :
  - S'assurer que toutes les ressources requises sont disponibles.
  - Affecter les travailleurs aux usines.
  - Affecter le transport pour chaque ressource nécessaire aux usines :
    - Choisir Transport Électrique ou aux Combustibles Fossiles.
    - Calculer les coûts de transport et la pollution en fonction de la distance.
- **Payer les Coûts Opérationnels** :
  - Payer le coût opérationnel de chaque usine.
  - Payer les coûts de transport.
- **Générer la Production** :
  - Rassembler les biens produits (par exemple, Bois, Bioplastiques).
  - Ajouter les Points de Pollution (PP) des opérations des usines et du transport.

#### Phase 2 : Construction & Technologie
- **Acheter de Nouvelles Tuiles** :
  - Si désiré et disponible, acheter des tuiles de terrain supplémentaires.
- **Construire ou Améliorer des Usines** :
  - Placer de nouvelles usines sur le terrain possédé.
  - Ajouter des améliorations aux usines existantes (par exemple, *Système de Capture de Carbone*).
- **Acheter des Cartes Tech** :
  - Acquérir de nouvelles Cartes de Technologie en payant leur coût.

#### Phase 3 : Commerce & Négociation
- **Vendre des Biens** :
  - Vendre des biens finis à la banque à des prix de base.
- **Échanges entre Joueurs** :
  - Négocier des échanges avec d'autres joueurs (par exemple, « Je te donne 2 Bois pour 1 Matériau Recyclé »).
- **Échanges de Travailleurs** :
  - Réaffecter ou échanger des travailleurs si les règles maison le permettent.

#### Phase 4 : Maintenance & Pollution
- **Calculer la Pollution Totale** :
  - Additionner la pollution des opérations des usines et du transport.
- **Taxe Carbone** :
  - Payer **5 EC × Total PP**.
- **Appliquer l'Atténuation de la Pollution** :
  - Utiliser les technologies, compensations forestières ou crédits carbone pour réduire les PP.
- **Payer les Dépenses** :
  - Salaires des travailleurs.
  - Maintenance des usines.
  - Coûts de transport.
  - Maintenance des technologies.
- **Ajuster le Capital** :
  - Déduire toutes les dépenses des EC du joueur.

**Fin du Tour** : Vérifier si la limite de tours (par exemple, 6 tours) est atteinte ou si des déclencheurs de fin de jeu sont remplis.

### 7.3 Conseils & Stratégies Importants

1. **Équilibrer Croissance Économique vs Pollution**
   - Les usines à haute production génèrent plus de biens mais peuvent augmenter la pollution.
   - Utiliser des Conseillers Environnementaux ou des technologies de capture de carbone pour gérer la pollution.

2. **Placement Stratégique des Usines**
   - Placer les usines près des ressources nécessaires pour minimiser les coûts de transport et la pollution.
   - Investir dans des technologies de transport pour optimiser la livraison de ressources sur de longues distances.

3. **Optimiser les Choix de Transport**
   - Utiliser le Transport Électrique pour une pollution réduite si le budget le permet.
   - Utiliser le Transport aux Combustibles Fossiles pour économiser les coûts mais gérer l'augmentation de la pollution.

4. **Se Concentrer sur les Ressources Clés**
   - Se concentrer sur les types de ressources qui synergisent avec vos usines et technologies.
   - Diversifier l'approvisionnement en ressources pour éviter les goulots d'étranglement.

5. **Planifier les Synergies Technologiques**
   - Combiner des technologies qui améliorent la production et réduisent la pollution.
   - Exemple : *Usine de Bioplastiques* + *Amélioration de Synthèse de Bioplastiques* augmente les revenus et la durabilité.

6. **Gérer les Finances avec Soin**
   - Surveiller les salaires, les coûts de maintenance, les dépenses de transport et les taxes carbone.
   - Assurer que votre capital reste sain tout au long du jeu.

7. **Exploiter le Commerce et la Négociation**
   - Échanger les ressources excédentaires avec d'autres joueurs pour équilibrer vos besoins.
   - Former des alliances stratégiques pour des bénéfices mutuels.

8. **Préparer la Fin de Jeu**
   - Accumuler du capital tout en contrôlant la pollution.
   - Viser à optimiser votre **Ratio Capital-Pollution** final avant la fin du jeu.

### 7.4 Exemple de Démarrage Rapide

- **Tour 1** :
  - **Construire une Ferme Agricole** sur une tuile Plaines.
  - **Embaucher 1 Technicien**.
  - **Opérer la Ferme** : Produire 3 unités d'Eau.
  - **Affecter le Transport** : Aucun nécessaire car la Ferme Agricole ne nécessite pas de ressources externes.
  - **Payer les Coûts** : 25 EC (opérationnel) + 30 EC (salaire) + 0 EC (transport) = 55 EC.
  - **Générer la Pollution** : 2 PP de la Ferme Agricole.
  - **Payer la Taxe Carbone** : 5 EC × 2 PP = 10 EC.
  - **Capital de Fin du Tour 1** : 1500 - 55 - 10 = 1435 EC.

- **Tour 2** :
  - **Améliorer la Ferme** avec *Synthèse de Bioplastiques* pour 200 EC.
  - **Effet** : Convertir 2 unités d'Eau en 2 Plastiques, vendus à 50 EC chacune = +100 EC.
  - **Payer la Maintenance** : 10 EC pour l'amélioration.
  - **Pollution** : +1 PP dû à une légère augmentation de la production.
  - **Capital de Fin du Tour 2** : 1435 - 200 + 100 - 10 = 1325 EC.

- **Tours 3–6** :
  - **Étendre le Terrain** ou **Ajouter des Usines** seulement si vous pouvez gérer la pollution et les coûts.
  - **Acquérir un Conseiller Environnemental** pour réduire la pollution des nouvelles usines.
  - **Optimiser le Transport** pour tout besoin de ressource éloignée.
  - **Exploiter les Technologies** pour augmenter la production et gérer efficacement la pollution.

---

## 8. VALIDATION & POINTS FORTS DE LA CONCEPTION

- **Intégration Cohérente** :
  - Les mécaniques de transport sont intégrées de manière fluide avec les opérations des usines.
  - La gestion des ressources s'aligne avec les types de terrain et les besoins des usines.
  - Les sources de pollution sont logiquement liées aux opérations des usines et aux choix de transport.

- **Complexité Réduite** :
  - Maintien d'un nombre gérable de types de ressources et de tuiles de terrain.
  - Mécaniques de transport simplifiées entre Électrique et Combustibles Fossiles.
  - Suivi de la pollution consolidé en un seul système de PP.

- **Rythme de Jeu Plus Rapide** :
  - Le jeu se termine typiquement en ~6 tours, chaque tour prenant ~15 minutes avec 4 joueurs (~1,5 heures au total).
  - Structure de tour rationalisée et processus de prise de décision simplifiés.

- **Valeur Éducative** :
  - Démonstration de l'équilibre entre croissance économique et durabilité environnementale.
  - Mise en évidence de l'impact des choix de transport sur les coûts et la pollution.
  - Encourage la planification stratégique et l'optimisation des ressources.

- **Équité & Stratégie** :
  - Ressources de départ égales assurent un terrain de jeu équitable.
  - Placement stratégique, gestion du transport et utilisation des technologies déterminent le succès.
  - Dépendance minimale au hasard, mettant l'accent sur la prise de décision des joueurs.

---
