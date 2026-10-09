# Écart depuis la version du 8 septembre 2026

**Pour qui.** Le développeur qui a repris le dépôt et la maquette le 8 septembre 2026 à 14 h 14, et qui doit se remettre à niveau.

**Départ.** `5e7ae6b`, l'état de `main` à 14 h 14 ce jour-là. La consolidation des specs dans `docs/current/` est arrivée le même jour, plus tard, à 16 h 43 (`7f50eda`) : elle ne fait pas partie de cette version.

**Arrivée.** `main` au 9 octobre 2026 (`b675936`), plus l'alignement de la maquette sur DEC-025 et DEC-012 fait le même jour, après l'analyse (`3d779af`).

**Ampleur.**
- 163 commits, dont 148 hors fusions.
- 82 fichiers touchés, soit +16 071 / −5 929 lignes, sans compter `index.html` et `docreview-app.html`, qui sont des sorties du build.
- 125 décisions numérotées (DEC-001 à DEC-125), toutes versées après la reprise.

## Comment lire

| Document | Contenu | Quand |
|---|---|---|
| [SPECS.md](SPECS.md) | Les règles métier, domaine par domaine : ce qui est nouveau, modifié, retiré, encore ouvert, avec les décisions et les règles de `docs/current/`. Commence par la carte des documents : où est passé chaque fichier de spec du 8 septembre. | D'abord |
| [DECISIONS.md](DECISIONS.md) | Les 125 décisions, chacune avec son effet par rapport au 8 septembre. On y trouve aussi le sort des anciennes décisions D1–D15, les 15 décisions qui renversent le plus et la liste complète des points ouverts. | En référence |
| [CODE.md](CODE.md) | Le prototype : écrans, shell, build, données, fonctions ajoutées ou retirées, et ce qui ne relève que de la démo. | Pour reprendre un comportement ou retrouver où il est implémenté |

**Marques.**
- **(R)** : règle métier, à appliquer dans le produit.
- **(P)** : comportement du prototype ou de la démo, à ne pas reproduire.
- **(X)** : retiré.
- « (déduit) » : conclusion tirée de la lecture du code ou des documents, non vérifiée autrement.

**Méthode.** L'analyse compare les deux versions du dépôt : code, documents et messages de commit. Rien n'a été retesté dans un navigateur pour l'écrire.

**Hors périmètre.** Les user stories, qui seront refaites entièrement.

**Règle d'autorité.** La décision la plus récente prime. Elle l'emporte sur une spec du 8 septembre, sur un constat du prototype, et même sur une ligne de `docs/current/` restée en retard (liste plus bas).

## Ce qui change le plus

**Organisation des specs.**
- La référence est `docs/current/` : un fichier par domaine, des règles identifiées (`ALLOC-`, `CONF-`, `LIFE-`…) et le registre des décisions dans `OPEN-QUESTIONS.md`.
- Les `docs/specs/SPEC-*.md` du 8 septembre ne sont plus que des renvois ; les originaux sont archivés dans `docs/archive/specs-2026-09-08/`.
- Ordre de lecture : `docs/current/README.md`, puis le fichier du domaine, puis les décisions.

**Vocabulaire.**
- « Activity » / « typology » deviennent **système** dans tout ce que lit l'utilisateur (DEC-045). « Activity » ne désigne plus que l'ABS.
- Manager et expert sont remplacés par **contributor** (DEC-030).
- Les deux étapes s'appellent **Allocation** et **Compliance** (DEC-029), et elles tournent en parallèle.
- Le code garde les anciens identifiants (`typology`, `manager`…).

**Modèle d'allocation.**
- La chaîne devient **ABS → PBS → OBS → personne** (DEC-008).
- ABS et PBS sont uniques par exigence ; l'OBS est multiple (DEC-055).
- Un OBS est une **organisation**, jamais une personne (DEC-054).
- Une allocation = une organisation + sa personne (DEC-060). Cette personne est responsable de la conformité ; il n'y a plus de responsable de suivi global (DEC-087).
- « Assigned to » se lit sur les allocations (DEC-123).
- Une personne n'appartient qu'à **un seul système** (DEC-102). Un système n'a pas besoin de manager (DEC-124).

**Profils de tender.**
- Un tender porte un seul système. Le Turnkey répartit vers des sous-systèmes.
- Le **produit** choisit le modèle (DEC-046 à DEC-049). Pour SIG, les modèles Mainline viennent du vrai classeur de clés (DEC-061/062).
- Ligne produit, produit et mode IA sont figés à la création (DEC-095).
- Un tender SIG autonome réel sert de référence : RFP-2026-114 (DEC-044).

**Validation.**
- Une seule validation par exigence (DEC-099). Plus de « Finalize allocation » (DEC-084).
- Sur Turnkey, le PM valide l'aiguillage, puis chaque système est validé à part (DEC-104).
- Titres et blocs d'information n'ont pas de statut (DEC-073).
- La nature vaut Information / Heading / Requirement (DEC-074). Seul le PM la modifie, ainsi que la classe (DEC-086).

**Relances des modèles.** Nouvelles :
- unitaire, en masse, ou proposée après un changement de nature ou de classe ;
- globale lors d'un changement de modèle, dans les paramètres.

Elles portent sur l'exigence entière et ne touchent jamais la personne. Une réponse ou un verdict les bloque ; une question au client ne les bloque pas (DEC-040 à DEC-056, DEC-075, DEC-089, DEC-091).

**Conformité.**
- **Deux verdicts** : Compliant et Not compliant. « R&D » devient une mention dans un Compliant (DEC-031).
- Plus aucun verrou (DEC-028).
- Ce que reçoit le client est une **conformité externe dérivée** de la **stratégie d'écart** choisie après un Not compliant ; le PM peut la corriger, avec un motif (DEC-106).
- Chaque Not compliant attend un **risque** `RSK-` du tender, rédigé en trois phrases. La page **Risks** est nouvelle (DEC-105 à DEC-114).

**Écran Compliance.**
- Panneau de décision du contributeur : choisir, puis confirmer (DEC-079 à DEC-081).
- Ordre du document, tri par en-têtes. Plus de statuts overdue / outdated (DEC-078, DEC-083).
- Une question au client ne bloque rien (DEC-092). Elle est impossible une fois le verdict donné (DEC-121).
- Compliance lit le registre Q&A (DEC-122).
- Une seule action de relance (DEC-125).

**Versions.**
- Les versions appartiennent aux **documents** (DEC-069).
- Les changements se lisent dans une **colonne Changes** et dans l'**onglet Changes** de la vue Document. Le mode Compare disparaît (DEC-119).
- Une exigence ajoutée ou modifiée repasse To review (DEC-072).
- Ses verdicts sont **rouverts** dans Compliance (DEC-016, DEC-122).

**Q&A.**
- Une seule liste, en deux vues : Our questions / Other bidders.
- Statuts To send / Sent / Answered, marqués à la main.
- Plus de lot, de revue interne, de doublons, d'exclusion ni de file d'arbitrage (DEC-116).

**Nouveautés transverses.**
- Colonnes personnalisées, communes à Allocation et Compliance (DEC-064 à DEC-068, DEC-097).
- Partenaires externes sur Turnkey (DEC-082, DEC-093).
- Clavier complet et annulation ⌘/Ctrl+Z (DEC-085).
- Journal d'activité par exigence, commun aux deux écrans.

**Pilotage.**
- Statistiques purement métier, **jamais par personne** (DEC-117, DEC-118). La mesure de l'IA ne sort plus que dans Configuration › AI feedback.
- La carte Allocation passe à « Done » quand tout est alloué (DEC-098).
- La page d'accueil est refaite.

**IA.** La confiance de caractérisation s'exprime en **Low / Medium / High**. Les modèles d'allocation gardent leurs pourcentages (DEC-120).

**Plateforme et marque.**
- Cible : 100 000 lignes et 10 utilisateurs simultanés (DEC-023).
- Police Alstom (non publiée tant que la licence n'est pas réglée), accent marine (DEC-063, DEC-115).
- Le rouge ne porte jamais d'état. L'en-tête affiche le logo de l'entreprise, puis « SRM ».

## Le code en bref

**Écrans.**
- 8 écrans au lieu de 7 : `risks.html` est nouveau.
- `tender-chat.html` existe, mais il est masqué (`CHAT_ENABLED = False`).

**Volumes depuis le 8 septembre.**

| Fichier | Lignes ajoutées / retirées | Commits |
|---|---|---|
| Allocation (`revue-documentaire.html`) | +3 659 / −1 584 | 83 |
| Compliance | +2 827 / −733 | 58 |
| Tableau de bord, configuration et casting | +1 856 / −712 | 43 |
| Q&A | +432 / −498 | 16 |
| Accueil | +315 / −130 | 19 |
| Documents | +211 / −66 | 12 |
| Création | +202 / −90 | 12 |
| `build_merge.py` (shell) | +491 / −75 | 30 |

**Shell.** Il devient le lieu des **données partagées par tender** : stratégies, risques, documentation d'écart, questions et registre Q&A, versions, journal, colonnes personnalisées, partenaires, progression. Ce sont des boîtes aux lettres en mémoire. Dans le produit, ce sont des ressources serveur ; il faut reproduire les objets et les règles, pas la mécanique.

**Build.**
- `keys.js` (clés SIG) devient obligatoire.
- Dans `data.js`, la confiance de caractérisation passe en niveaux.
- Deux sorties locales s'ajoutent.
- Deux interrupteurs à connaître : `PUBLISH_BRAND_FONT` et `CHAT_ENABLED`.

**Retiré du shell.**
- `isReviewValidated` / `setReviewValidated` (Finalize) ;
- `getProjectMeta` / `setProjectMeta`.

`isV22Uploaded` existe encore, mais plus aucun écran ne le lit.

## À savoir avant de reprendre

### La documentation de référence n'est pas partout à jour

Ces lignes de `docs/current/` décrivent encore l'état antérieur. La décision la plus récente prime :
- **Trois verdicts et verrou :**
  - `COMPLIANCE.md` (CONF-003, CONF-005 à CONF-007, CONF-014 à CONF-017, CONF-020, plusieurs CONF-T, lignes « verrou » des transitions) ;
  - `DOMAIN.md` (axe « trois valeurs », DOM-009) ;
  - `ACCESS.md` (ligne « verrouiller » de la matrice) ;
  - `PLATFORM.md` (FR 5–6).
- **Ancien responsable de suivi (DEC-010) :** ACC-009 (le § « Absence de responsable » d'`ALLOCATION.md` a été réaligné le 9 oct.).
- **Lot, fusion et arbitrage du Q&A :** QA-010 et JRN-006.
- **Mode Compare, onglet Document et suppression manuelle :** `JOURNEYS.md`.
- **Colonnes personnalisées « créées deux fois » :** CUST-T01 et CUST-T11, contre DEC-097.
- **Bouton Confirm :** ALLOC-017, contre DEC-099.
- **Validation en deux gestes :** ALLOC-T30.
- **Sept sources, et DEC-001 à DEC-027 seulement :** `docs/current/README.md`.
- **Copies anciennes non converties en renvois :** `docs/SPEC-qa-screen.md` et `docs/TICKET-casting-screen-redesign.md`, à la racine de `docs/`.

### Le prototype ne suit pas encore toutes les décisions

Deux écarts ont été corrigés après l'analyse, le 9 octobre (`3d779af`) : la validation sans personne (DEC-025) et la lecture de tout le tender par un contributeur, en lecture seule hors de son système (DEC-012). Restent :

- **Saisie d'un verdict par le PM (DEC-013, OPEN-14) :** le prototype ne le permet que pour un partenaire.
- **Verdict par organisation OBS (CONF-004, DEC-055/060) :** Compliance saisit encore le verdict au niveau du système.
- **Casting par les contributeurs (DEC-003, ACC-T06) :** seuls le PM et les managers sont simulés.
- **Mode IA par tender (DEC-095) :** c'est encore une valeur unique pour toute la démo, absente des paramètres.
- **Correction de traduction (LIFE-008, DEC-026) :** elle ne repasse pas l'exigence en revue.
- **Langue de l'export client (LANG-003) :** l'anglais est coché par défaut.
- **Relance automatique sur une nouvelle version (DEC-027, LIFE-011) :** non démontrée.
- **Contrôle de relance sur les cartes système Turnkey (ALLOC-014, ALLOC-T23) :** retiré de la maquette.
- **Valeurs Functional / Performance (ALLOC-T26) :** encore présentes dans la recherche et sur des puces de la vue Document.

### Ce que le prototype simule (à ne pas reproduire)

- **Aucune persistance :** tout est perdu au rechargement de la page.
- **État propre à chaque écran :** l'état d'un écran se perd à chaque navigation (Compliance : verdicts, réaffectations).
- **Écrans non reliés :**
  - valider une allocation ne crée pas les affectations de Compliance ;
  - une version téléversée dans Documents n'atteint pas Allocation ;
  - le casting reste local à son écran.
- **Contenu de démo partagé entre tenders :** Q&A et Documents affichent le contenu de STB-2026 sur tous les tenders. Les compteurs du tableau de bord sont écrits à la main.
- **Modèles IA, similarité, import et export :** simulés.

### Points à faire arbitrer (ne pas trancher seul)

Restent à arbitrer :
- la borne du premier pilote (DEC-022 : jusqu'à la validation de l'allocation), alors que l'essentiel des décisions récentes porte sur Compliance, Q&A et Risks ;
- la ligne produit « Services », toujours proposée alors que DEC-004 fixe quatre types ;
- ce que deviennent la stratégie d'écart, les risques et la correction du PM quand une version rouvre un verdict ;
- l'effet d'une correction de traduction sur une exigence déjà répondue ;
- la langue par défaut de l'export client.

**Données attendues :**
- la légende des 16 codes système ;
- la matrice des combinaisons Turnkey ;
- les catégories de non-conformité ;
- les produits RSC et le rapport RSC / RST ;
- les régions ;
- le rouge exact de la marque, les fichiers Antarctica et la licence de la police.

La liste complète est dans [DECISIONS.md](DECISIONS.md), section « Toujours ouvert ».
