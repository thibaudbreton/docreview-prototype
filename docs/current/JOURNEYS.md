# Parcours et interactions

Les écrans sources constituent la référence visuelle. Cette spec décrit le comportement et renvoie aux règles communes. Les scénarios sont des critères de recette, pas le compte rendu d'une recette exécutée.

## Applicabilité obligatoire

Lire [TENDER-PROFILES](TENDER-PROFILES.md). Chaque scénario est décliné Turnkey / SIG / Mainline / RSC. SIG conserve tous les écrans, supprime les éléments de la passe 1, ouvre son détail directement et utilise ABS → PBS → OBS → personne. Le prototype est la référence Turnkey, pas une preuve d’interface universelle.

Premier pilote : création jusqu’à validation de l’allocation pour les quatre types ; parcours de conformité et Q&A documentés pour la suite, REX/Chat hors V1.

## JRN-001 — Créer et reprendre un projet

Acteur : utilisateur habilité à créer (politique globale à préciser), puis PM. Accueil → création en quatre étapes → Allocation en manuel ou Dashboard pendant traitement. Références : LIFE-001 à LIFE-003, ACC-001/002.

Acceptation : identité obligatoire contrôlée, rattachement au projet conservé, retour au projet après reconnexion (cible de persistance). Les limitations « seul projet de démonstration navigable » et les temporisations de progression ne font pas partie de la cible. L'accueil bloque actuellement l'ouverture d'un projet en traitement alors que la création ouvre son dashboard : comportement de reprise OPEN-05.

## JRN-002 — Corriger et valider l'allocation

Acteur : contributeurs dans leur activité ; validation par l’équipe de gestion du projet (DEC-009). Ouvrir Allocation → isoler les éléments à revoir → inspecter source/propositions → corriger → valider l'allocation → retrouver le travail dans Compliance. Références : ALLOC-001 à ALLOC-010.

Acceptation : identité conservée après changement Type, dépendances invalidées après correction amont, progression indépendante des branches. Les champs techniques exacts et droits de validation restent liés aux questions ouvertes.

## JRN-003 — Répondre et suivre la conformité

Acteurs : Contributor / PM. Même écran Compliance, périmètre et actions selon rôle ; tableau et détail Document ; REX/Chat hors V1. Voir [spec pilote](COMPLIANCE.md) pour règles, transitions et dix cas d'acceptation. Aucun verdict automatique après réponse client.

## JRN-004 — Maintenir le casting

PM → équipe projet et activités ; tout contributeur → rattachements de sa propre activité (DEC-003). Recherche annuaire → personne → activité/périmètre optionnel → ajout → champ prêt pour l'ajout suivant. Références ACC-001 à ACC-006. Roster 150–200 personnes décrit comme besoin, pas mesure de charge exécutée.

## JRN-005 — Ajouter/remplacer un document

Documents → ajouter, réordonner ou nouvelle version → comparaison → relance automatique des modèles nécessaires sur les exigences modifiées → consulter les nouvelles propositions → revoir/valider le travail affecté. Références LIFE-004 à LIFE-011. La suppression manuelle affiche l’impact avant confirmation ; conservation/récupération reste distincte des suppressions lors de comparaison (LIFE-006).

## JRN-006 — Traiter les questions client

Contributor soulève une question liée ; PM prépare le lot et exporte ; envoi hors outil ; PM importe les réponses et arbitre les associations ; contributeur reprend son travail. Références QA-001 à QA-009. Lecture ouverte aux autres activités du même projet (DEC-012) ; formats et cas résiduels dans OPEN-06/10.

## JRN-007 — Piloter et configurer

Dashboard : indicateurs ouvrant le travail correspondant, sans transformer le processus en phases globalement bloquantes. Références PLAT-008. Configuration : identifier les paramètres réellement appliqués et ceux seulement représentés. L'absence de persistance et les toasts « Save configuration » ne définissent pas la cible de sauvegarde. Paramètres et droits à confirmer OPEN-05/12.

## Interactions communes de table

- UX-001 — DOC/OBS : sélection simple, étendue, multi-sélection, actions groupées, navigation clavier, cellule active visible, colonnes masquables/réordonnables. Référence visuelle : Allocation et `table-engine.js` ; ne pas recréer une variante par écran.
- UX-002 — DOC : filtres par colonne, filtre avancé et sélection doivent exposer clairement le périmètre actif. Filtrer ne modifie pas les données.
- UX-003 — DOC : filtre avancé avec opérateur AND/OR et un niveau de groupes ; opérateurs adaptés au type ; application après confirmation avec aperçu du nombre de résultats.
- UX-004 — DOC : filtres nommés personnels, réutilisables entre projets sur une même table ; pas de partage implicite. Champ indisponible dans le nouveau projet : OPEN-13.
- UX-005 — DOC/PROP : filtrage sur tout le jeu autorisé, pas seulement la page chargée ; l'implémentation serveur est la cible de la spec historique.
- UX-006 — OPEN-13 : « Filter to Selection » suspend les filtres de colonnes dans le comportement historique ; sa composition exacte avec le filtre avancé et la sélection de toutes les pages reste à définir.

## États de production à concevoir — PROP

Pour chaque parcours : chargement réel, aucun résultat, échec récupérable, absence de droit, traitement partiellement terminé, conflit d'édition. La réussite n'est affichée qu'après confirmation réelle ; la saisie est conservée lors d'un échec lorsque possible. Les écrans actuels ne permettent pas de déclarer ces états validés.

## Détails préservés

Les anciennes specs de table, filtres, création, casting, configuration et dashboard sont conservées en archive pour les détails d'interaction. Leurs règles métier contradictoires ne font pas autorité sur cette édition ; les lacunes recensées dans OPEN ne sont pas résolues par leur ancienneté.
