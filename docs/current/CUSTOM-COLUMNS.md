# Colonnes personnalisées

Spec reçue le 23 septembre 2026 (`SPEC-custom-columns.md`), reprise ici avec les décisions prises et ce que le prototype en fait.

**L'intention.** Garder la souplesse d'un tableur sans perdre le modèle dessous : sans cette fonction, le premier système qui a un besoin particulier repart dans Excel.

## Ce qu'est une colonne personnalisée

Une **définition de champ** créée par un chef de projet, qui porte une donnée **saisie par des humains** sur chaque exigence.

- **Portée : un tender, une phase.** Une colonne créée dans Allocation n'existe que dans Allocation, sur ce tender. Elle n'apparaît pas dans Compliance et ne passe pas au tender suivant.
- **Deux types** : **texte libre** et **liste** — un ensemble fermé d'options défini à la création. Une liste est à **choix unique ou multiple** (DEC-066).
- **Seuls les chefs de projet** créent, modifient et suppriment les colonnes. Les contributeurs les remplissent, dans leur périmètre, comme n'importe quel champ.
- **L'IA ne les remplit jamais.** Pas de confiance, pas de doute, et elles ne font jamais passer une exigence « à revoir ».
- **Toujours facultatives** (DEC-067) : une colonne vide ne bloque jamais la validation. Cohérent avec DEC-025, où même l'absence de responsable ne bloque pas.

## Stockage (cible produit)

Recommandé par la spec : une table `field_definitions` (id, tender, phase, nom, type, options, ordre) et les valeurs dans une colonne `JSONB` de l'exigence, indexée par id de champ. Écartés : l'EAV (200 000 lignes par tender à 10 000 exigences × 20 champs, une jointure à chaque lecture) et le `ALTER TABLE` (une migration de schéma à chaque colonne ajoutée).

**Le vrai coût est dans le filtrage**, pas dans le stockage : SPEC-advanced-filters exige un filtrage côté serveur à l'échelle d'un tender, donc des requêtes construites dynamiquement sur du JSON, avec les index qui vont avec.

## Où elles apparaissent

Partout où une colonne native apparaît, sans cas particulier : la table (réordonnable, masquable depuis *View*, triable), le panneau de détail, les filtres, les exports internes.

**Filtres** — opérateurs par type :

| Type | Opérateurs |
|---|---|
| Texte libre | contient, ne contient pas, est, n'est pas, commence par, est vide, n'est pas vide |
| Liste à choix unique | est, n'est pas, est parmi, n'est parmi aucun, est vide |
| Liste à choix multiple | contient l'un de, ne contient aucun de, est vide, n'est pas vide |

## Export — hors du livrable client

Retenu par défaut, sur la recommandation de la spec : **incluses dans les exports internes, jamais dans la matrice de conformité envoyée au client.** Le risque est concret : une colonne libre sert tôt ou tard de note interne — un doute sur un fournisseur, une réserve commerciale, un commentaire sur le client. Une option « inclure dans l'export client » par colonne pourra s'ajouter si un vrai besoin apparaît ; le défaut sûr est dehors. La portée par phase le garantit déjà pour Allocation : ces colonnes n'existent pas dans Compliance, d'où part la matrice.

## Suppression et modification

**Supprimer une colonne supprime toutes ses valeurs**, irréversiblement. La confirmation donne **le nombre d'exigences qui ont une valeur** : « supprimer cette colonne » et « supprimer 340 valeurs » sont la même action, et c'est la seconde formulation que l'utilisateur doit voir.

**Retirer une option d'une liste** est **refusé tant qu'elle est utilisée** (DEC-065), avec le nombre d'exigences concernées. Aucune valeur n'est jamais perdue ni laissée orpheline en silence ; le chef de projet sait ce qu'il doit nettoyer d'abord.

**Modifier une définition** (défaut retenu, §8.5 de la spec) : renommer est toujours permis ; **changer le type est bloqué dès qu'une valeur existe**. Passer une liste de choix unique à multiple est permis — chaque valeur devient une liste d'un élément, rien ne se perd. L'inverse est bloqué dès qu'une exigence tient plusieurs valeurs.

**Nouvelle version de document** (défaut retenu, §8.6) : les valeurs **survivent** à la remise à zéro d'une exigence. Ce sont des données humaines, étrangères au pipeline d'IA.

## Conséquences de la portée, à connaître

**Rien n'est comparable d'un tender à l'autre.** Les colonnes personnalisées n'alimentent ni les statistiques transverses ni le tableau de bord VIP — c'est voulu. Si un champ s'avère utile partout, c'est le signe qu'il doit devenir un vrai champ modélisé.

**Un champ utile en Allocation et en Compliance doit être créé deux fois**, comme deux colonnes indépendantes aux données sans lien. Acceptable en principe, irritant en pratique — à confirmer quand Compliance sera construit.

## État du prototype (23 septembre 2026)

Construit **dans Allocation uniquement** (DEC-064) ; Compliance viendra ensuite sur le même modèle.

**24 septembre 2026 (DEC-081) : Compliance a ses propres colonnes**, même modèle, phase « compliance » — une colonne créée dans Compliance n'existe que là, et celles d'Allocation n'y apparaissent pas (la portée par phase tient). Mêmes règles d'édition, de verrou et de suppression ; valeurs par exigence, vides sur les lignes système/équipe. Différences : pas de filtre depuis l'en-tête (les filtres de colonne de Compliance portent sur les affectations) — le constructeur de filtres les couvre ; pas de tri par en-tête (l'écran trie par sa liste). À l'export, une colonne personnalisée est **décochée par défaut et marquée « internal »** ; la cocher déclenche un avertissement.

- Bouton **＋ Column** dans la barre de la table, visible des seuls chefs de projet ; ✎ sur l'en-tête de chaque colonne personnalisée pour la modifier ou la supprimer.
- Cellules éditables dans la table : champ texte, liste déroulante, ou sélecteur à cases pour le choix multiple. Les sous-lignes système/équipe et les blocs d'information ont une cellule vide, pour garder la grille alignée.
- Section dans le panneau de détail, avec une ligne qui rappelle que ce sont des données humaines.
- Groupe **Custom columns** dans le constructeur de filtres ; entonnoir d'en-tête pour les listes ; tri par l'en-tête.
- L'export interne annonce les colonnes incluses et rappelle qu'elles ne partent jamais dans la matrice client.
- Définitions et valeurs sont conservées dans la coquille, par tender : elles survivent à la navigation entre écrans et sont effacées par « Reset demo ».
- **Clavier** : les flèches atteignent ces colonnes comme les autres ; **Entrée ou F2** ouvre l'édition de la cellule active ; Entrée valide et descend d'une ligne, Échap rétablit la valeur. Le sélecteur à choix multiple suit le même contrat (↑/↓ entre les options, Espace coche). Au passage, ←/→ suivent désormais l'ordre **affiché** des colonnes, y compris après un réordonnancement dans *View* — elles suivaient jusque-là une liste figée.
- Non fait : renommer une option existante (on peut en ajouter et en retirer).

## Critères d'acceptation

- CUST-T01 : une colonne créée sur un tender n'apparaît ni sur un autre tender, ni dans Compliance.
- CUST-T02 : un contributeur remplit une colonne mais ne voit ni la création, ni la modification, ni la suppression.
- CUST-T03 : aucune colonne personnalisée ne porte de confiance ni ne met une exigence « à revoir ».
- CUST-T04 : la confirmation de suppression énonce le nombre de valeurs détruites avant d'agir.
- CUST-T05 : retirer une option utilisée est refusé avec le nombre d'exigences qui l'utilisent.
- CUST-T06 : changer le type d'une colonne qui a des valeurs est impossible ; la renommer l'est toujours.
- CUST-T07 : une colonne se filtre avec les opérateurs de son type, dans le constructeur comme depuis l'en-tête (listes).
- CUST-T08 : aucune colonne personnalisée ne figure dans la matrice de conformité client.
- CUST-T09 : une valeur survit à la navigation entre écrans et à la remise à zéro d'une exigence par une nouvelle version.
- CUST-T10 : une colonne personnalisée se remplit entièrement au clavier : l'atteindre aux flèches, l'éditer avec Entrée, valider en descendant, annuler avec Échap — y compris une liste à choix multiple.
- CUST-T11 : dans Compliance, une colonne créée n'apparaît que dans Compliance ; à l'export, elle est proposée décochée et marquée interne.
