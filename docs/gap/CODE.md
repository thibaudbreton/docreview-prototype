# Écart de code — du 8 septembre au 9 octobre 2026

Départ : `5e7ae6b` (`main` le 8 septembre 2026 à 14 h 14). Arrivée : `main` au 9 octobre 2026 (`b675936`). Synthèse et mode d'emploi : [README.md](README.md). Règles métier : [SPECS.md](SPECS.md).

Chaque point porte une marque : **(R)** règle métier, à appliquer dans le produit ; **(P)** comportement de prototype ou de démonstration, à ne pas reproduire ; **(X)** retiré. « (déduit) » signale une conclusion tirée de la lecture du code ou des documents, non vérifiée autrement. Références : `DEC-xxx` = décisions (`docs/current/OPEN-QUESTIONS.md`, détail dans [DECISIONS.md](DECISIONS.md)) ; `ALLOC-`, `CONF-`, `LIFE-`, `ACC-`, `QA-`, `AI-`, `PLAT-`, `JRN-`, `UX-`, `CUST-`, `KEY-`, `TYPE-` = règles de `docs/current/` ; les hash (`8c748a3`…) sont des commits (`git show <hash>`).

**Lecture.** Le prototype reste un ensemble de pages HTML autonomes assemblées par `build_merge.py` ; chaque écran est rechargé à chaque navigation, et ce qui doit survivre vit en mémoire dans le shell. Ce document décrit ce qui a changé dans ce code — comportements, données, fonctions — pour reprendre un comportement ou retrouver où il est implémenté. Ce n'est pas une architecture cible : les marques (P) disent ce qui ne relève que de la démonstration. Les volumes excluent `index.html` et `docreview-app.html`, sorties du build.

## Sommaire

- [Mise à jour du 9 octobre — DEC-025 et DEC-012 (3d779af)](#mise-à-jour-du-9-octobre--dec-025-et-dec-012-3d779af)
- [Partie 1 — Vue d'ensemble](#partie-1--vue-densemble)
  - [Vue d'ensemble](#vue-densemble)
- [Partie 2 — Socle : shell, build, code partagé, charte, inventaire des composants](#partie-2--socle--shell-build-code-partagé-charte-inventaire-des-composants)
  - [Shell : routage et état partagé — build_merge.py (gabarits HEADER / FOOTER)](#shell--routage-et-état-partagé--build_mergepy-gabarits-header--footer)
  - [Chaîne de build — build_merge.py (main()), build_fonts.py, build_keys.py, keys.js, import_capture*.py, .gitignore](#chaîne-de-build--build_mergepy-main-build_fontspy-build_keyspy-keysjs-import_capturepy-gitignore)
  - [Chat du tender (masqué) — tender-chat.html](#chat-du-tender-masqué--tender-chathtml)
  - [Code partagé entre écrans — table-engine.js, components.css](#code-partagé-entre-écrans--table-enginejs-componentscss)
  - [Charte dans le code — jetons, polices, logo, icônes (8 écrans), fonts/README.md, CLAUDE.md](#charte-dans-le-code--jetons-polices-logo-icônes-8-écrans-fontsreadmemd-claudemd)
  - [Inventaire des composants — COMPONENTS.md](#inventaire-des-composants--componentsmd)
  - [Documents racine — README.md, HANDOVER.md, CLAUDE.md](#documents-racine--readmemd-handovermd-claudemd)
- [Partie 3 — Allocation](#partie-3--allocation)
  - [Allocation — vue d'ensemble — revue-documentaire.html](#allocation--vue-densemble--revue-documentairehtml)
  - [Allocation — modèle d'allocation, personnes, statuts et validation — revue-documentaire.html](#allocation--modèle-dallocation-personnes-statuts-et-validation--revue-documentairehtml)
  - [Allocation — relance des modèles et clés PBS/OBS/ABS — revue-documentaire.html](#allocation--relance-des-modèles-et-clés-pbsobsabs--revue-documentairehtml)
  - [Allocation — tableau, filtres, clavier et actions groupées — revue-documentaire.html](#allocation--tableau-filtres-clavier-et-actions-groupées--revue-documentairehtml)
  - [Allocation — panneau de détail et journal d'activité — revue-documentaire.html](#allocation--panneau-de-détail-et-journal-dactivité--revue-documentairehtml)
  - [Allocation — versions, colonne Changes et vue Document — revue-documentaire.html](#allocation--versions-colonne-changes-et-vue-document--revue-documentairehtml)
  - [Allocation — colonnes personnalisées — revue-documentaire.html](#allocation--colonnes-personnalisées--revue-documentairehtml)
  - [Clés PBS / OBS / ABS — build_keys.py, keys.js](#clés-pbs--obs--abs--build_keyspy-keysjs)
  - [Données de capture réelles — import_capture_doors.py (et chargement de data.js)](#données-de-capture-réelles--import_capture_doorspy-et-chargement-de-datajs)
- [Partie 4 — Compliance et Risks](#partie-4--compliance-et-risks)
  - [Écran Compliance — compliance.html](#écran-compliance--compliancehtml)
  - [Page Risks — risks.html](#page-risks--riskshtml)
  - [Contrats du shell utilisés par Compliance et Risks — build_merge.py](#contrats-du-shell-utilisés-par-compliance-et-risks--build_mergepy)
- [Partie 5 — Documents et versions, Q&A, capture](#partie-5--documents-et-versions-qa-capture)
  - [Documents & versions — documents.html](#documents--versions--documentshtml)
  - [Q&A — qa.html](#qa--qahtml)
  - [Shell, parties utilisées par Documents, Q&A et Compliance — build_merge.py](#shell-parties-utilisées-par-documents-qa-et-compliance--build_mergepy)
  - [Importeurs de capture — import_capture_doors.py, import_capture.py](#importeurs-de-capture--import_capture_doorspy-import_capturepy)
  - [Transverse — langue, capture, IA et versions dans les écrans de travail — revue-documentaire.html, compliance.html, dashboard-et-config.html, creation-projet.html](#transverse--langue-capture-ia-et-versions-dans-les-écrans-de-travail--revue-documentairehtml-compliancehtml-dashboard-et-confightml-creation-projethtml)
- [Partie 6 — Accueil, création, tableau de bord, statistiques, configuration, casting](#partie-6--accueil-création-tableau-de-bord-statistiques-configuration-casting)
  - [Accueil — accueil.html](#accueil--accueilhtml)
  - [Création d'un tender — creation-projet.html](#création-dun-tender--creation-projethtml)
  - [Tableau de bord — dashboard-et-config.html (#dash-screen)](#tableau-de-bord--dashboard-et-confightml-dash-screen)
  - [Statistiques — dashboard-et-config.html (.stats-panel)](#statistiques--dashboard-et-confightml-stats-panel)
  - [Configuration — dashboard-et-config.html (#cfg-screen)](#configuration--dashboard-et-confightml-cfg-screen)
  - [Team casting — dashboard-et-config.html (#team-screen)](#team-casting--dashboard-et-confightml-team-screen)
  - [Shell — partie projets et identité — build_merge.py](#shell--partie-projets-et-identité--build_mergepy)

## Mise à jour du 9 octobre — DEC-025 et DEC-012 (`3d779af`)

Fait après la rédaction de ce document ; les parties qui suivent décrivent l'état d'avant pour ces deux points.
- **DEC-025** (`revue-documentaire.html`) — `computeAllocStatus()` / `markAllocEdited()` : Incomplete seulement si ABS, PBS et OBS sont tous vides ; une entrée OBS sans personne ne bloque plus rien. `targetAssigned()` est supprimé, remplacé par `unassignedNoteHTML()` (note sous le bouton de validation, jamais désactivant). Les raisons de blocage ne parlent plus d'assigner quelqu'un.
- **DEC-012** (`revue-documentaire.html`) — `visibleTo()` devient `isMine()` (« puis-je modifier ») et ne filtre plus la table, les compteurs, le filtre avancé ni l'export ; caviardage supprimé de `renderDoc()` (variante `.blk.redacted`, `state.redactMode`) ; `body.restricted` → `body.as-contributor`, bannière `.viewas-banner` neutre ; `keepOwnSelection()` écarte des actions groupées les lignes hors système ; N reste sur le travail du contributeur.
- **DEC-012** (`compliance.html`) — `passesB()` ne retire plus les autres systèmes ; `canEditReq()` ; panneau en lecture seule sur l'affectation d'un autre système (pas de relance, réaffectation, question ni mise de côté) ; pastille « My system » (`#tp-mine`, désactivée par défaut) ; colonnes personnalisées en lecture seule hors de son système.
- **DEC-012** (`dashboard-et-config.html`, `build_merge.py`) — réglage « Restricted view (Redacted / Hidden) » et `applyRedactUI` supprimés ; `redactMode`, `getRedactMode`, `setRedactMode` retirés du shell.

# Partie 1 — Vue d'ensemble

## Vue d'ensemble

### Écrans et routes — 7 sources au 8 sept., 8 aujourd'hui

| Source | Clé `SOURCES` | Routes (`#hash`) | Écran | Changement | Lignes 8 sept. → auj. |
|---|---|---|---|---|---|
| `accueil.html` | `home` | `#home` (défaut) | Accueil + Mes tenders | refondu en page d'accueil (`b862a20`, 6 oct.) | 304 → 489 |
| `creation-projet.html` | `create` | `#new` | Assistant de création | | 739 → 851 |
| `dashboard-et-config.html` | `dash` | `#dashboard`, `#config`, `#team` | Tableau de bord, Paramètres, Casting | | 2 059 → 3 203 |
| `revue-documentaire.html` | `review` | `#review` | Allocation | | 6 039 → 8 114 |
| `compliance.html` | `compliance` | `#compliance`, `#compliance-contributor` | Compliance (+ vue contributeur de démo) | | 1 974 → 4 068 |
| `documents.html` | `documents` | `#documents` | Documents & versions | | 686 → 831 |
| `qa.html` | `qa` | `#qa` | Q&A | | 684 → 618 |
| `risks.html` | `risks` | `#risks` | Risks (registre des risques du tender) | **nouveau** (`b7161d3`, 30 sept.) | 0 → 296 |

- Routes : 10 → 11 (`risks`). Une route inconnue mène toujours à `dashboard`. `URLMAP` gagne `'risks.html'`. Les crochets de sous-route (`showConfig`, `showScreen('team')`, `setScreen(2)`, `setDemoContributorView`) sont inchangés.
- Hors écrans : `tender-chat.html` s'insère dans le shell, hors iframe ; il est désactivé (`CHAT_ENABLED = False`).

### Fichiers nouveaux, supprimés, générés
- **Nouveaux (versionnés)** : `risks.html`, `tender-chat.html`, `build_fonts.py`, `build_keys.py`, `keys.js` (généré puis commité), `fonts/README.md`. Côté `docs/` : 17 fichiers `docs/current/`, 16 dans `docs/archive/specs-2026-09-08/`, 5 specs dans `docs/specs/`, `docs/stories/STORIES-extracted-from-prototype.md` (voir la carte des documents, SPECS.md, partie 1).
- **Supprimé** : aucun fichier de code ; côté docs, `docs/specs/SPEC-expert-space.md`.
- **Générés, non versionnés** (`.gitignore`) : `local/index.html` (police embarquée), `artifact/srm-prototype.html` (version pour claude.ai), `fonts/*.woff` / `*.woff2` / `*.otf` / `*.ttf`, `deck/` (outillage de captures), `data.js` (déjà ignoré au 8 sept.).
- **Sorties versionnées** : `index.html` et `docreview-app.html`, identiques et reconstruits à chaque commit (137 commits chacun). Ne jamais les éditer.

### Volume par fichier

`index.html` et `docreview-app.html` sont exclus : ce sont des sorties de build, avec une ligne base64 par écran, et leur diff en lignes (+372 / −59) ne signifie rien. Totaux hors `docs/` et hors ces deux sorties : 23 fichiers, **+11 828 / −4 350**, dont les 8 écrans **+9 798 / −3 813**. `docs/` : 59 fichiers, +4 243 / −1 579.

| Fichier | + / − | Commits | Lignes 8 sept. → auj. |
|---|---|---|---|
| `revue-documentaire.html` | +3 659 / −1 584 | 83 | 6 039 → 8 114 |
| `compliance.html` | +2 827 / −733 | 58 | 1 974 → 4 068 |
| `dashboard-et-config.html` | +1 856 / −712 | 43 | 2 059 → 3 203 |
| `qa.html` | +432 / −498 | 16 | 684 → 618 |
| `accueil.html` | +315 / −130 | 19 | 304 → 489 |
| `risks.html` | +296 | 9 | nouveau |
| `documents.html` | +211 / −66 | 12 | 686 → 831 |
| `creation-projet.html` | +202 / −90 | 12 | 739 → 851 |
| `build_merge.py` | +491 / −75 | 30 | 363 → 779 |
| `tender-chat.html` | +254 | 2 | nouveau |
| `build_fonts.py` | +101 | 1 | nouveau |
| `build_keys.py` | +99 | 1 | nouveau |
| `keys.js` | +2 (≈ 37 Ko sur 2 lignes) | 1 | nouveau |
| `table-engine.js` | +60 / −12 | 4 | 289 → 337 |
| `import_capture_doors.py` | +23 / −11 | 2 | |
| `import_capture.py` | +4 / −3 | 1 | |
| `components.css` | +6 / −5 | 1 | 235 → 236 |
| `COMPONENTS.md` | +954 / −429 | 79 | 1 671 → 2 196 |
| `fonts/README.md` | +16 | 2 | nouveau |
| `.gitignore` | +11 / −1 | 5 | |
| `README.md` | +6 | 2 | |
| `HANDOVER.md` | +2 | 2 | |
| `CLAUDE.md` | +1 / −1 | 1 | |

### Chronologie des vagues

163 commits : 148 hors merges et 15 merges (mesuré avec `git rev-list 5e7ae6b..main`).

**S37 — 7 → 13 sept. (19 commits)**
- 8 sept. : consolidation des specs dans `docs/current/` et archivage, sans code (`7f50eda`).
- 10–11 sept. : une seule personne assignée par système (fusion manager/expert dans Allocation `326291b` et Compliance `b932fb4`), assignation par recherche d'annuaire (`94eadd4`), statut propre au contributeur et retrait de « Pass 1/Pass 2 » de l'UI (`a900e09`), correctifs de réaffectation (`ee9ee21`).
- 13 sept. : vague du ticket de corrections consolidé (§1–§4, fichier absent du dépôt). Cartes Mes tenders à deux jauges (`2dd1fb4`, `eff7b95`), écran projet (`f21b2b5`), Allocation avec OBS en liste éditable et activités supprimables (`5b5bc8a`, `7892738`, `e151286`), Compliance avec split interne/externe, lignes à deux niveaux et filtres d'en-tête façon Excel (`e4b1b31`, `5b5bd98`, `8e83ca8`).

**S38 — 14 → 20 sept. (28 commits)**
- 14 sept. : relecture du prototype → DEC-028…039. Tableau Compliance (colonne verdict, vert/rouge réservés au verdict, colonnes déclaration externe et risque accepté), vocabulaire phase 1 (`39e277b`), deux verdicts sans verrou (`22d651b`), liste des 16 codes (`2a7aa6b`, `762f9c0`).
- 15–16 sept. : « typology » → « activity » (`f76c38b`) ; Statistiques du dashboard par étape, rail de support (`d2793d2` → `a568853`).
- 17 sept. : DEC-027…057. « activity » → « system » (`7d737b8`, `d72a2a9`). Tender SIG autonome RFP-2026-114 construit (`376c6a5`, `dcd6449`, `ebf4668`). Relance d'allocation (`10891a8`, `5a4730a`). Étape OBS restaurée, OBS multiples, OBS = organisation (`48cc854`, `d931f40`, `7e9b462`, `b851a7a`).

**S39 — 21 → 27 sept. (42 commits)**
- 21 sept. : allocation = organisation + personne (DEC-060). Clés PBS/OBS/ABS réelles avec `build_keys.py` et `keys.js` (`132eef3`, DEC-061/062). Quatre défauts et produit du wizard (`b3a195d`, DEC-049).
- 22 sept. : réglages de capture (`b2ac7af`), charte Noto Sans / Antarctica / marine / rouge (`dd816be`, DEC-063).
- 23 sept. : colonnes personnalisées (`9f677cf`, DEC-064…068), colonnes redimensionnables (`aac89b1`), gap par document et onglet Versions (`82ab34e`, DEC-069…072), DEC-073…077 (titres sans statut, nature/classe, suppression jusqu'à zéro, TK OBS dans System).
- 24 sept. : Compliance restructuré et panneau de décision (DEC-078…081, 083), partenaires externes (DEC-082), suppression de Finalize (DEC-084), clavier et annulation (DEC-085), icônes SVG (`49ae3a3`).

**S40 — 28 sept. → 4 oct. (31 commits)**
- 28–29 sept. : DEC-086…104 (nature/classe réservées au PM, responsabilité par OBS, questions client en brouillon, une validation par exigence, une personne = un système, validation Turnkey à deux niveaux…) ; démo Turnkey « To review ».
- 30 sept. : module Risks (`a4a115d` → `f9b9145`, DEC-105…114, `risks.html` 8ᵉ source) ; spec de la vue Document sur PDF, non implémentée (`7fb3faa` → `6e6ad8b`).
- 1ᵉʳ oct. : journal d'activité par exigence dans le shell (`7a1d771`) ; chat du tender ajouté puis masqué (`86dbb39`, `683763c`) ; retouches pour les captures du deck (`df69bfc`).

**S41 — 5 → 9 oct. (28 commits)**
- 6 oct. : police Alstom (`e82c293`, DEC-115), barre marine essayée puis annulée (`a79114e` / `4341e56`), Q&A simplifié (`47de775`, DEC-116), page d'accueil refondue (`b862a20` → `bef01a1`). Dashboard : ligne du tender essayée, retour aux deux cartes (`41de42d`, `d143a45`, `2a42509`). Statistiques métier (`d109c66`, DEC-117). Boutons de validation accessibles et titre intégré à la barre de statut (`1129260`, `6b8d477`). Lignes INFRA / Rolling Stock retirées du wizard (`2169056`).
- 7 oct. : statistiques par système, jamais par personne (`1c6fe67`, DEC-118) ; colonne Changes et fin du mode Compare (`73c7fe7`, `8365089`, DEC-119) ; passe UI (`e962c96`).
- 8 oct. : confiance de caractérisation Low / Medium / High (`e5ee6e3`, DEC-120).
- 9 oct. : nettoyage du code mort (`14e3059`), DEC-121…125 (`8c748a3`), en-tête avec logo de l'entreprise et favicon SRM (`575fbbe`).

---

# Partie 2 — Socle : shell, build, code partagé, charte, inventaire des composants

Périmètre : le shell (`build_merge.py` : routes, sources assemblées, état partagé `window.*`), la chaîne de build et ses sorties, `tender-chat.html`, le code partagé (`table-engine.js`, `components.css`), la charte dans le code (jetons, polices, logo, icônes), `COMPONENTS.md` et les documents racine. Le détail fonctionnel de chaque écran relève des autres parties.


## Shell : routage et état partagé — `build_merge.py` (gabarits `HEADER` / `FOOTER`)
Volume : +491 / −75 lignes depuis 5e7ae6b (fichier entier, build compris) ; 30 commits ; 363 → 779 lignes.

### Ajouté
- (R) **Route `#risks`** vers `risks.html`, 8ᵉ source (`b7161d3`).
- (P) **Principe** : tout état qui doit survivre à la navigation vit dans le shell, **indexé par tender** (`projectId`, clé `"_"` par défaut), car chaque route recharge l'iframe de l'écran (`srcdoc`). Chaque écran garde ses propres données de démo et **rapporte** des compteurs au shell (`report*`), que d'autres écrans lisent. Le shell est pré-rempli avec ce que les écrans calculent sur la démo (`seedStrategyUsage`, `seedGapStats`, `seedPartnerUsage`, `seedDocReqIndex`) pour que Paramètres et Dashboard affichent des chiffres avant la première visite de l'écran source.
- (P) **Convention de retour des mutateurs** (nouveaux magasins) : `{entry}`, `{removed}` ou `{error:"empty"|"duplicate"|"used"|"missing"}`. L'écran affiche la raison du refus ; c'est l'application des refus motivés de DEC-093 (partenaire utilisé), DEC-110 (stratégie utilisée) et DEC-113 (risque sans ses trois réponses).
- (R) **Avancement de l'allocation** — `reportAllocationProgress` / `getAllocationProgress` (`3537205`, DEC-098).
- (R) **Questions au client et registre Q&A** :
  - `pushQuestion` / `getQuestions` / `withdrawQuestion` (`d6efd7f`, DEC-088) : une question posée sur Compliance arrive dans Q&A ; `withdrawQuestion` sert à l'annulation ;
  - `getQaRegister` (`47de775`, DEC-116) : état propre du registre, lu aussi par Compliance depuis `8c748a3` (DEC-122).
- (R) **Changements de version** — `recordVersionChange` / `getVersionChanges` / `reportDocReqIndex` (`8c748a3`, DEC-122, LIFE-007). Documents enregistre chaque upload par tender ; Compliance rouvre les verdicts des exigences modifiées et réécrit le nombre réel ; le Dashboard raconte le dernier upload.
- (R) **Journal d'activité par exigence** — `logReqEvent` / `getReqLog` (`7a1d771`), plus `getActivityLog` qui rend tout le journal du tender (`d109c66`, DEC-117).
- (R) **Colonnes personnalisées** — `getCustomFields` (`9f677cf`, DEC-064 ; communes à Allocation et Compliance depuis DEC-097).
- (P) **Largeurs de colonnes** — `getTableLayout`, par tender et par table (`aac89b1`).
- (R) **Stratégies d'écart** :
  - `getStrategies` / `addStrategy` / `renameStrategy` / `setStrategyResult` / `removeStrategy` ;
  - `reportStrategyUsage` / `getStrategyUsage` (`efc2777`, DEC-110/111) ;
  - suppression refusée si la stratégie est utilisée ; noms uniques, sans tenir compte de la casse.
- (R) **Risques et documentation d'écart** :
  - `getRisks` / `addRisk` (`4a6015f`, réduits par `93f80d9` puis `f9b9145`, DEC-113/114) ;
  - `getGapDocs` / `getGapDoc` / `setGapDoc` (`4a6015f`) ;
  - `reportGapStats` / `getGapStats` (`18294c4`).
- (R) **Partenaires externes** — `getPartners` / `addPartner` (`54fb4cf`, DEC-082) ; `removePartner` / `reportPartnerUsage` / `getPartnerUsage` (`42676d5`, DEC-093 : retrait refusé tant qu'une exigence l'utilise).
- (P) **Passage de relais ponctuel entre écrans** — `setScreenFocus` / `takeScreenFocus` (`b7161d3`), par exemple « ouvrir ce risque » ou « filtrer Compliance sur ce risque ».
- (P) **Accueil** — `getHomeIntroHidden` / `setHomeIntroHidden` : bloc « How a tender travels through SRM » masquable, réaffiché par Reset demo (`b862a20`).
- (P) **Polices** — `BRAND_FONTS` (`window.BRAND_FONTS`) et `withBrandFonts(html)` : à chaque chargement d'écran, les `url("fonts/Alstom-*.woff")` sont remplacées par la copie embarquée quand elle existe (`e82c293`).

### Modifié (avant → maintenant)
- (R) **Champs d'un projet** (`seedProjects`, `addProject`) :
  - Avant : `done`/`total` (sens double), `health`/`healthNote`, `deadline:1` → Maintenant : `total`, **`allocated`**, **`complianceFilled`** (`2dd1fb4`) ; `health`, `healthNote` et `deadline` supprimés (`2dd1fb4`, `14e3059`) ;
  - `addProject` conserve désormais **`product`** saisi dans le wizard (`b3a195d`, DEC-049) ;
  - `status` n'est plus lu que pour `processing` et `submitted`. Accueil déduit l'étape (Allocation / Compliance) des compteurs, et aucun écran ne lit plus `requirement_review`, `qa_versioning` ni `expert_review`.
- (P) **Tenders de démo** :
  - `rfp114` devient navigable (`builtOut:true`, DEC-044, `376c6a5`), avec `status` `expert_review` → `requirement_review`, 12 exigences dont 4 allouées, `language:"en"`, `system:"Mainline"`, `product:"Mainline Wayside"` (`132eef3`, DEC-061) ;
  - rôles « Expert » → « Contributor » (`39e277b`) ;
  - lignes « Rolling Stock » et « INFRA » conservées sur deux tenders d'illustration, alors que le wizard ne les propose plus (`2169056`).
- (P) **Boucle de traitement** — libellé « Allocating to experts… » → « Allocating to contributors… » (`39e277b`).
- (R) **Drapeau v2.2** (`isV22Uploaded` / `setV22Uploaded`) — Avant : lu par le Dashboard, jamais levé → Maintenant : levé par `documents.html` à l'upload d'une nouvelle version de `d1` (`b3a195d`). Depuis `8c748a3`, le Dashboard lit `getVersionChanges()` à la place : **plus aucun écran ne le lit**. Le commentaire de `documents.html` dit encore le contraire.
- (P) **Demandes de réaffectation** (`pushReassignRequest` / `getReassignRequests` / `updateReassignRequest`) — API inchangée. Le Dashboard les lit désormais (fil de commentaires et carte « réaffectations en attente » depuis `f21b2b5`, statistiques de réallocation depuis `d109c66`). C'est le seul magasin **non indexé par tender** ; le Dashboard filtre par préfixe d'identifiant.
- (P) **`resetDemo()`** — réinitialise tous les nouveaux magasins et ne touche plus `reviewValidated` ni `projectMeta`. `Ctrl+Shift+R` est inchangé.
- (P) **`load(routeKey)`** — `frame.srcdoc = withBrandFonts(b64utf8(BLOBS[…]))`.
- (P) **Docstring** :
  - 8 sources ;
  - `components.css` inclus par Allocation et Compliance seulement ;
  - périmètre de `table-engine.js` précisé ;
  - `data.js` produit par `import_capture_doors.py` ;
  - repli `seedDemoSections()` (la mention `buildBigData(n)` était déjà caduque au 8 sept. : la fonction n'existait plus).

### Retiré
- (X) `isReviewValidated` / `setReviewValidated` et la variable `reviewValidated` — le jalon Finalize n'existe plus (DEC-084). Appelants supprimés par `5019c2b`, shell nettoyé par `14e3059`.
- (X) `getProjectMeta` / `setProjectMeta` — écrits par le wizard, jamais lus (`14e3059`).
- (X) `clearGapDoc` (`14e3059`).
- (X) Ajoutés puis retirés dans la période : `updateRisk`, `addRiskComment`, `mergeRisks`, ainsi que les champs de risque `weight`, `status`, `comments`, `desc` (`4a6015f` / `b7161d3` → `93f80d9`, DEC-113) et `activities` (`f9b9145`, DEC-114).
- (X) Champs de projet `health`, `healthNote`, `deadline`, `done`.

### Modèle de données et état (magasins du shell)

**Par tender (clé `projectId`)**
- **Projet** : `{id, ref, name, line, days, status, total, allocated, complianceFilled, updated, role, builtOut, language, product?, system?, primary?, progress?, procLabel?, reqs?, experts[], pmTeam[]}`.
- `customFields[t] = {defs[], values{<reqId>…}, seq}` : valeurs indexées par exigence, survivent à une remise à zéro par nouvelle version.
- `tableLayouts["<t>::<table>"] = {widths{}}`.
- `partners[t] = [{id:"p_<code>", code (≤ 8 car., majuscules), label}]` ; `partnerUsage[t][partnerId] = {allocation:n, compliance:n}`.
- `allocProgress[t] = {allocated, total}`.
- `strategies[t] = [{id:"gs_<n>", name, ext:"not_compliant"|"pending"|"compliant"}]`, `ext` à `pending` par défaut ; `strategyUsage[t][gs] = {used, corrected}`.
- `risks[t] = [{id:"RSK-00001", that, cause, impact, createdBy, createdAt}]` : numérotation par tender, trois champs obligatoires, aucun système.
- `gapDocs[t]["<reqId>#<code système>"] = {strategy, risks[], override: null | {ext, reason, by, date}, meta:{reqId, typology, sec, text, managerName}}`.
- `gapStats[t] = {reqs, assignments, assigned, answered, compliant, nc, ncLogged, byStrategy{}, noStrategy, ext{compliant, not_compliant, pending, none}}`.
- `reqLog[t][reqId] = [{ts, time, who, cat, what, from?, to?, milestone?, k, live?}]` : `milestone` vaut `allocated`, `answered` ou `declared` dans la démo, `live` marque un événement de la session.
- `sharedQuestions[t] = [{id:"QA-5n", st:"draft"|"sent"|"answered", q, refs:[{req, typology}], from, date, origin:"compliance", ans?}]` : `draft` = « To send ».
- `qaRegister[t] = {flags:{<qaId>:{st, sentDate, ans, ansDate, suggest}}, others:[…]}` : marques « envoyé », réponses confirmées, Q&A des autres soumissionnaires.
- `docReqIndex[t][docId] = [{id, answered}]` ; `versionChanges[t] = [{doc, docName, num, m, gap:{a,m,r}, note, modified[], reopened, logged}]`.

**Globaux**
- `reassignRequests[] = [{id:"RR-<n>", at, requestStatus, …}]`.
- `screenFocus[écran] = payload` (consommé une seule fois).
- `homeIntroHidden`.
- Inchangés : `CURRENT_USER`, `projectMode`, `aiFeedback[]`, `theme`, `v22Uploaded`. `redactMode` (`getRedactMode` / `setRedactMode`) est supprimé le 9 oct. (`3d779af`, DEC-012).

### Fonctions / points d'entrée clés

| Groupe | Fonctions | Statut | Écrans qui les appellent |
|---|---|---|---|
| Navigation | `route`, `routeUrl` | inchangées (+ `risks`) | tous / Dashboard |
| Tenders | `getProjects`, `getCurrentProject`, `setCurrentProject`, `addProject`, `openProject` | signatures inchangées, champs modifiés | Accueil, Création, tous |
| Utilisateur | `getCurrentUser` | inchangée | tous |
| Accueil | `getHomeIntroHidden`, `setHomeIntroHidden` | **nouvelles** | Accueil |
| Avancement allocation | `reportAllocationProgress`, `getAllocationProgress` | **nouvelles** | Allocation → Dashboard |
| Réaffectations | `pushReassignRequest`, `getReassignRequests`, `updateReassignRequest` | inchangées | Allocation, Compliance, Dashboard (nouveau lecteur) |
| Questions / Q&A | `pushQuestion`, `getQuestions`, `withdrawQuestion`, `getQaRegister` | **nouvelles** | Compliance ↔ Q&A |
| Versions | `recordVersionChange`, `getVersionChanges`, `reportDocReqIndex` | **nouvelles** | Documents, Compliance, Dashboard |
| Drapeau v2.2 | `isV22Uploaded`, `setV22Uploaded` | conservées, sans lecteur | Documents |
| Journal | `logReqEvent`, `getReqLog`, `getActivityLog` | **nouvelles** | Allocation, Compliance, Dashboard, chat |
| Colonnes | `getCustomFields`, `getTableLayout` | **nouvelles** | Allocation, Compliance |
| Stratégies | `getStrategies`, `addStrategy`, `renameStrategy`, `setStrategyResult`, `removeStrategy`, `reportStrategyUsage`, `getStrategyUsage` | **nouvelles** | Paramètres, Compliance, chat |
| Risques / écarts | `getRisks`, `addRisk`, `getGapDocs`, `getGapDoc`, `setGapDoc`, `reportGapStats`, `getGapStats` | **nouvelles** | Compliance, Risks, Dashboard, chat |
| Partenaires | `getPartners`, `addPartner`, `removePartner`, `reportPartnerUsage`, `getPartnerUsage` | **nouvelles** | Paramètres, Allocation, Compliance |
| Relais | `setScreenFocus`, `takeScreenFocus` | **nouvelles** | Compliance ↔ Risks |
| Divers | `getTheme`/`setTheme`, `getProjectMode`/`setProjectMode`, `getRedactMode`/`setRedactMode`, `pushAIFeedback`/`getAIFeedback`, `resetDemo` | inchangées (`resetDemo` étendue) | tous / Création, Allocation / Paramètres / Accueil |
| Polices | `withBrandFonts` (interne), `window.BRAND_FONTS` | **nouvelles** | shell |
| Supprimées | `isReviewValidated`, `setReviewValidated`, `getProjectMeta`, `setProjectMeta`, `clearGapDoc` (+ `updateRisk`, `addRiskComment`, `mergeRisks`, éphémères) | retirées | aucun appel résiduel (vérifié) |

### Prototype seulement (à ne pas reproduire)
- Tout l'état est en mémoire, dans un seul onglet ; recharger la page remet la démo à zéro. L'iframe est reconstruite à chaque route.
- **Mécanisme « rapporter / pré-remplir »** : les écrans recalculent et poussent des compteurs, et le shell en duplique une copie figée pour la démo. Dans le produit, ce sont des requêtes sur une source unique (déduit).
- `recordVersionChange` choisit les `m` premières exigences ayant des réponses, dans l'ordre du document, et les chiffres de gap viennent de `documents.html` : simulation de l'analyse d'écart.
- Identifiants fabriqués par le shell : `QA-` + (50 + n) par tender, `RSK-` max + 1 par tender, `gs_<n>`, `p_<CODE>`, `RR-<n>` global.
- `live:true` sur les événements de la session : le classement hebdomadaire du Dashboard ne compte qu'eux.
- Données de démo :
  - stratégies sur les 5 tenders d'exemple (un nouveau tender n'en a aucune, DEC-110) ;
  - 6 risques sur STB-2026 et 1 sur RFP-2026-114 ;
  - documentation d'écart et historiques du journal ;
  - partenaire fictif « Voltara Engineering » sur STB-2026 ;
  - index d'exigences par document.
- Inchangés au 8 sept. : `builtOut` qui bloque les tenders d'illustration, boucle de traitement simulée, identité `CURRENT_USER` figée, boîte de réaffectation globale.

### Visuel
- Favicon du shell : deux SVG (clair/sombre) → un seul SVG, la marque SRM « 02 Fan Ribbons » (`575fbbe`). Titre de page inchangé (« … STB-2026 · Full app »), alors que deux tenders sont navigables.

### Synthèse
- Le shell passe d'une dizaine de fonctions (projets, validation, v2.2, mode, méta, feedback IA, réaffectations, thème) à **une vingtaine de magasins par tender**. C'est là que se lit le modèle de données transverse : stratégies, risques, écarts, questions, versions, journal, partenaires, colonnes.
- À reproduire : **les objets et les règles** (refus motivés, statuts des questions, réouverture par version, journal avant/après). À ne pas reproduire : la boîte aux lettres, les rapports de compteurs, les seeds miroirs.
- Disparus : la porte « revue validée » (Finalize) et `projectMeta`. Le drapeau v2.2 ne sert plus à rien.


## Chaîne de build — `build_merge.py` (`main()`), `build_fonts.py`, `build_keys.py`, `keys.js`, `import_capture*.py`, `.gitignore`
Volume : `build_merge.py` voir ci-dessus (même fichier) ; `build_fonts.py` +101 (1 commit) ; `build_keys.py` +99 (1) ; `keys.js` +2 (1) ; `import_capture_doors.py` +23 / −11 (2) ; `import_capture.py` +4 / −3 (1) ; `.gitignore` +11 / −1 (5).

### Ajouté
- (P) **Inclusion `/* @include keys.js */`** — produit `window.SRM_KEYS`, utilisé par `revue-documentaire.html` seulement. **`keys.js` est obligatoire** (le build échoue s'il manque), alors que `data.js` reste facultatif. Le marqueur était d'abord traité dans la branche `data.js` (`132eef3`) ; il est autonome depuis `14e3059`.
- (P) **`build_keys.py`** (openpyxl) — classeur « PBS/OBS/ABS Keys » v260720 → `keys.js` :
  - PBS en arbre à trois niveaux, avec les lignes sans identifiant rattachées ;
  - 16 catégories ABS ;
  - OBS = postes rangés sous les ABS, avec codes skills / SoA / job ;
  - une colonne par produit : `urban`, `mainline-wayside`, `mainline-onboard` ;
  - anomalies chargées telles quelles (DEC-061) ;
  - chemin par défaut du classeur codé en dur sur le poste de l'auteur.
- (P) **Polices dans le build** :
  - `antarctica_present` retire les `url("fonts/Antarctica-*.woff2")` quand les fichiers manquent (`dd816be`) ;
  - `BRAND_FONT_FILES` (Alstom Regular / Medium / Bold en `.woff`), `BRAND_FONT_RULE`, **`PUBLISH_BRAND_FONT = False`** ;
  - `page(with_font)` produit une **variante publiée** sans les règles `@font-face "Alstom UI"` (repli Noto Sans) et une **variante locale** avec `window.BRAND_FONTS` (base64) injecté avant `BLOBS` (`e82c293`) ;
  - si l'un des trois fichiers manque, aucune sortie n'a la police.
- (P) **`build_fonts.py`** — TTF de bureau → WOFF 1.0 (zlib). Supprime les tables EBDT / EBLC / EBSC (bitmaps 1 bit) et hdmx / VDMX / LTSH, recalcule les sommes de contrôle et écrit `fonts/Alstom-{Regular,Medium,Bold}.woff`. Bibliothèque standard seulement.
- (P) **Nouvelles sorties** :
  - `LOCAL_OUTPUT = "local/index.html"` : non versionnée, police embarquée, s'ouvre en `file://` ;
  - `ARTIFACT_OUTPUT = "artifact/srm-prototype.html"` : non versionnée, écrite **à chaque build** (`<title>` + style du shell + corps de la variante publiée), pour publication sur claude.ai (`86dbb39`).
- (P) **Chat** — `CHAT_FILE`, **`CHAT_ENABLED = False`**. Une fois activé, le build insère avant `</body>` un `<script>window.CHAT_CAPTURE=…</script>` (documents triés par `order`, lignes `[id, index du document, section, category, texte]` tirées de `data.js`), puis `tender-chat.html` (`86dbb39`, `683763c`).
- (R) **Contrat de `data.js`** (`import_capture_doors.py`) — la confiance de **caractérisation** (`confidence.type`, `confidence.class`) devient un niveau `"low"` / `"medium"` / `"high"` (moins de 75 : low ; moins de 85 : medium). Les champs d'allocation (`abs`, `pbs`, `obs`) gardent un nombre de 0 à 99 (`_char_level()`, `e5ee6e3`, DEC-120).
- (P) **`.gitignore`** : `fonts/*.woff2`, `*.woff`, `*.otf`, `*.ttf` (`dd816be`, `e82c293`), `local/` (`e82c293`), `artifact/` (`86dbb39`), `deck/` (outillage de captures du deck, `df69bfc`).

### Modifié (avant → maintenant)
- (P) **Sorties** — Avant : 2 (`docreview-app.html` et `index.html`, identiques) → Maintenant : 4 (+ `local/index.html`, + `artifact/srm-prototype.html`).
- (P) **Importeurs** — `import_capture.py` est marqué *LEGACY* (captures `.xlsx`, sans niveau de titre, sans système ni confiance) et perd son avertissement « plus de 3 000 lignes ». `import_capture_doors.py` est l'importeur de référence de `data.js` ; « activity » y devient « system » dans les commentaires et les sorties console.
- (P) **Messages de build** (`Note: …`) — signalent l'absence de `data.js`, d'Antarctica et des WOFF Alstom.

### Retiré
- Rien.

### Modèle de données et état
- `window.SRM_KEYS = {version:"v260720", products:[3], pbs:[223 × {id, parent, level, name, label, products[]}], abs:[16 × {id, label, note, products[]}], obs:[66 × {id, title, abs, skills, soa, code, products[]}]}`.
- `window.SRM_DATA` (`data.js`, inchangé sinon) : `rows[].confidence.type|class` → niveau texte ; `abs|pbs|obs` → nombre.
- `window.BRAND_FONTS = {"fonts/Alstom-Regular.woff": "<base64>", …}` (variante locale seulement).
- `window.CHAT_CAPTURE = {docs:[noms], rows:[[id, doc, section, category, text]]}` (seulement si le chat est activé).

### Fonctions / points d'entrée clés
- `build_merge.main()` restructuré : collecte `screens`, puis appelle **`page(with_font)`** (nouvelle) deux fois.
- `build_fonts.main(src)`, avec `strip()` et `to_woff()`.
- `build_keys.py` : script, sans fonction d'entrée.
- `import_capture_doors._char_level(score)` (nouvelle).

### Prototype seulement (à ne pas reproduire)
- Architecture inchangée : un fichier unique, un blob base64 par écran, des iframes `srcdoc`, pas de bundler.
- **Confidentialité** : `data.js` contient des données client réelles ; il est ignoré par git et ne doit jamais être publié, or le build l'inline dès qu'il est présent localement — vérifier avant de publier une sortie. Activer `CHAT_ENABLED` ajouterait le texte de la capture dans le shell, et `artifact/` est régénéré à chaque build. `PUBLISH_BRAND_FONT` est un interrupteur de licence, à ne pas activer sans accord (DEC-115).

### Visuel
- Variante publiée en Noto Sans, variante locale en Alstom : même mise en page, car la police Alstom est calée sur les métriques de Noto Sans.

### Synthèse
- `keys.js` est une **dépendance obligatoire** du build. `data.js` change de contrat sur la confiance (niveaux texte pour type et classe).
- Quatre sorties, dont deux locales non versionnées. Trois interrupteurs à connaître : `PUBLISH_BRAND_FONT`, `CHAT_ENABLED`, et la présence de `data.js`.


## Chat du tender (masqué) — `tender-chat.html`
Volume : +254 (nouveau) ; 2 commits.

### Ajouté
- (P) **Panneau flottant « Ask the tender »** inséré dans le shell, hors iframe. Il interroge Claude par `window.claude.use("sample")` du runtime d'artifact claude.ai, sur le compte de l'utilisateur. Hors claude.ai, il l'annonce (« Available in the version published on claude.ai »).
- (P) **Six outils de page** :
  - `search_blocks`, `get_blocks`, `list_documents`, `count_blocks` sur les blocs capturés ;
  - `requirement_record` : stratégie, risques, correction PM et 15 derniers événements du journal ;
  - `list_risks`.
  Sans outils, une recherche par mots-clés côté page envoie les 25 meilleurs extraits.
- (P) **Citations `[SRM-…]` / `[L4-…]` cliquables** — bascule sur `stb2026`, route `review`, puis appelle `selectBlock(id, {scroll:true})` dans l'écran Allocation.

### Modifié (avant → maintenant)
- (P) Masqué dès le 1ᵉʳ oct. par `CHAT_ENABLED = False` (`683763c`), parce qu'il ne fait pas partie de ce qui sera construit ensuite. REX et Chat sont hors V1 (DEC-021).

### Retiré
- —

### Modèle de données et état
- Lit `window.CHAT_CAPTURE`, c'est-à-dire la capture de STB-2026, quel que soit le tender ouvert.
- API du shell utilisée : `getCurrentProject`, `getStrategies`, `getRisks`, `getGapDocs`, `getReqLog`, `setCurrentProject`, `route`, `getTheme`.

### Fonctions / points d'entrée clés
- `TOOLS[]`, `RULES` (consigne système), `search()`, `contextFor()`, `ask()`, `render()`, `md()`.

### Prototype seulement (à ne pas reproduire)
- Tout le fichier.

### Visuel
- Jetons propres `--tc-*`, valeurs littérales copiées des écrans ; signalé dans `COMPONENTS.md` (« Tender Chat »).

### Synthèse
- Rien à construire. Ne pas réactiver sans revoir la confidentialité (voir la chaîne de build).


## Code partagé entre écrans — `table-engine.js`, `components.css`
Volume : `table-engine.js` +60 / −12, 4 commits (289 → 337 l.) ; `components.css` +6 / −5, 1 commit (235 → 236 l.).

### Ajouté
- (R) **`TE.bindColumnResize(headEl, opts)`** (`aac89b1`) :
  - une poignée sur chaque en-tête, sauf la gouttière de sélection ;
  - glisser pour redimensionner, double-clic pour revenir à la largeur par défaut, ←/→ par pas de 16 px ;
  - l'engine mesure et rapporte, l'écran possède ses largeurs (`opts.set / min / live / commit`) ;
  - largeurs gardées par tender et par table dans le shell (`getTableLayout`), effacées par « Reset column widths ».
- (R) **Type de champ `multi`** dans le filtre avancé (`TE.OPS_BY_TYPE.multi` : `is_any_of`, `is_none_of`, `is_empty`, `is_not_empty`), pour les colonnes personnalisées à choix multiple (DEC-066, `9f677cf`).
- (P) **`components.css` inclus par `compliance.html`** (marqueur ajouté par `5b5bd98`, 13 sept.) ; au 8 sept., seul `revue-documentaire.html` l'incluait.

### Modifié (avant → maintenant)
- (P) `TE.focusActiveCellControl` mémorise la valeur d'origine (`dataset.orig`) dès le focus clavier, pour qu'Échap la restaure même quand l'événement `focus` ne se déclenche pas (`cdce5a9`).
- (P) **En-tête de `table-engine.js` corrigé** — l'engine porte la sélection, Filter to Selection, la navigation clavier, le redimensionnement, le menu de visibilité et d'ordre des colonnes, le filtre avancé et les filtres enregistrés. La barre d'actions groupées, les popovers de filtre par colonne, le tri et le rendu restent dans chaque écran.
- (P) `components.css` : commentaires seulement (« + Add activity » → « + Add system ») ; `ui-list`, `ui-select` et `ui-input` sont inchangés.

### Retiré
- —

### Modèle de données et état
- —

### Fonctions / points d'entrée clés
- `TE.bindColumnResize` (nouvelle), `TE.OPS_BY_TYPE.multi` (nouveau), `TE.focusActiveCellControl` (modifiée).

### Prototype seulement (à ne pas reproduire)
- **Clavier et annulation (DEC-085) dupliqués dans chaque écran** : `UNDO_STACK` et `undoLast()` existent à l'identique dans `revue-documentaire.html` et dans `compliance.html` (pile limitée à 30 dans les deux), plutôt que dans l'engine. À factoriser dans le produit.
- Les 33 icônes sont aussi copiées dans chaque écran (voir la charte).

### Visuel
- Classe `col-resizing` sur `body` pendant le glissement.

### Synthèse
- Le partage réel reste limité à deux fichiers inclus par Allocation et Compliance. Seuls le redimensionnement et l'opérateur `multi` sont nouveaux ; le reste du comportement commun (raccourcis, annulation, icônes) est dupliqué écran par écran.


## Charte dans le code — jetons, polices, logo, icônes (8 écrans), `fonts/README.md`, `CLAUDE.md`
Volume : réparti dans les 8 écrans, sans volume isolable. Commits `dd816be`, `4bedc2a`, `49ae3a3`, `73efa97`, `e82c293`, `a79114e` / `4341e56`, `4953fea`, `575fbbe`. `fonts/README.md` +16 (2 commits) ; `CLAUDE.md` +1 / −1.

### Ajouté
- (R) **Jetons `--font-heading` et `--brand-red`** :
  - `--font-heading` : `"Antarctica","Alstom UI","Noto Sans","Inter",…` ;
  - `--brand-red` : `#E4002B` provisoire, défini dans `:root` seulement et donc hérité en thème clair ;
  - tous deux ajoutés à l'échelle suivie dans `CLAUDE.md`.
- (P) **`--brand-blue`, `--brand-blue-soft`, `--brand-slate`** — dans `accueil.html` et `dashboard-et-config.html` seulement, hors échelle suivie (`4953fea`).
- (R) **`@font-face "Alstom UI"`** — graisses 400 et 500, 600 tracé avec le Medium, 700, 800 tracé avec le Bold. Réglages `size-adjust:112%`, `ascent-override:95.4%`, `descent-override:26.2%`, `line-gap-override:0%`, pour garder les métriques de Noto Sans.
- (R) **Autres polices** — `@font-face "Antarctica"` (`local()` + `fonts/Antarctica-*.woff2`) ; lien Google Fonts **Noto Sans 400–700** dans chaque écran.
- (R) **Marque de titre** `h1::before, h2::before` : barre rouge de 5 px en `--brand-red`, dans les 8 écrans.
- (R) **En-tête** (`575fbbe`) — `.brand-logo` (logo de l'entreprise en PNG base64, variantes `.brand-light` / `.brand-dark` selon le thème, filet à droite), puis `.logo` contenant « SRM » en texte.
- (R) **Icônes** (`49ae3a3`) — `<i class=ic-NAME>`, masque CSS (`--i`) sur `currentColor`, règle `i[class^="ic-"]`. 33 icônes, **copiées dans chacun des 8 écrans** et non dans `components.css`.

### Modifié (avant → maintenant)
- (R) **Thème sombre** (`:root`) :
  - `--bg` #141F2B → #071A30 ;
  - `--panel` #1E3246 → #0B294A ;
  - `--panel-2` #26374C → #143556 ;
  - `--panel-3` #2F4257 → #1D4062 ;
  - `--line` #2C3E52 → #1F3E5F ;
  - `--line-2` #3A4E66 → #2E4E70 ;
  - `--accent-soft` #1E3A63 → #1B3F6B ;
  - `--accent` #4C82FF inchangé.
- (R) **Thème clair** (`html[data-theme="light"]`) : `--accent` #0050E3 → **#0B294A** ; `--accent-soft` #E9EFFD → #E6EBF2.
- (R) **Polices** — `--font-ui` : `"Inter",…` → `"Alstom UI","Noto Sans","Inter",…`. `--font-mono` : `ui-monospace,…` → `"Alstom UI",ui-monospace,…` (identifiants et codes dans la police de marque). `--font-doc` (Georgia) inchangé.
- (P) **Favicon** — deux SVG (clair/sombre) → un seul, dans chaque écran et dans le shell (`575fbbe`).
- (P) **Pastilles de statut** sans point initial (`73efa97`).
- (P) **`fonts/README.md`** — créé pour Antarctica (`dd816be`), puis réécrit pour la police Alstom (`e82c293`) : licence, build des WOFF, jamais `local()`, Georgia pour le document.

### Retiré
- (X) `.logo-mark` : marque SRM en SVG dans l'en-tête, variantes clair/sombre (`575fbbe`).
- (X) Surcharge rouge du point du logo (`4bedc2a`).
- (X) Barre supérieure marine, ajoutée puis annulée (`a79114e` / `4341e56`) : effet nul.

### Modèle de données et état
- Aucun changement : le thème clair par défaut vient toujours du shell (`theme='light'`). Ouvert seul, un écran s'affiche en sombre (`:root`).

### Fonctions / points d'entrée clés
- `withBrandFonts()` (shell, voir plus haut).

### Prototype seulement (à ne pas reproduire)
- Le logo en base64 et les 33 icônes sont dupliqués dans 8 fichiers ; les jetons sont redéfinis à l'identique dans chaque écran. La version publiée n'a pas la police de marque.

### Visuel
- Accent marine, surfaces marine en thème sombre, barre rouge devant les titres, logo de l'entreprise suivi de « SRM », icônes au trait.

### Synthèse
- Échelle de jetons inchangée dans sa forme, avec deux jetons de plus (`--font-heading`, `--brand-red`) et de nouvelles valeurs de surface et d'accent.
- À reprendre dans un vrai système de design : police calée, jeu d'icônes, logo. **Le rouge ne porte jamais d'état** (DEC-063).


## Inventaire des composants — `COMPONENTS.md`
Volume : +954 / −429 ; 79 commits ; 1 671 → 2 196 lignes.

### Ajouté
- (P) **61 nouvelles entrées actives** : 16 atomes, 36 molécules, 9 organismes. Total actif : 165 au 8 sept. (37 / 84 / 44) → **205** aujourd'hui (52 / 107 / 46).
  - **Shell et marque** : Icon, Brand Logo, Page Title, Block Badge, Tender Chat.
  - **Allocation** : Custom Column Tag / Cell / Header Cell / Editor, Custom Fields Panel Section, Column Resize Handle, Word Diff, Versions Tab, Removed Requirement Panel, Changes Cell, Changes Navigator, Version Picker Button / Popover, Change Type Tag, Change List Card, Nature Picker, Nature and Class Fields, Confidence Level Badge, Re-run Control, Re-run Prompt, Derivation Chain, OBS List, Turnkey System Card, Validate Zone, Paragraph Reference, Shortcut Help.
  - **Compliance** : Decision Panel, Partner Verdict Entry, Gap Editor (Strategy + Risk), External Compliance Field, Risk Chip, Export Options Modal.
  - **Risks** : Risk List.
  - **Paramètres** : Gap Strategy Editor, Turnkey OBS List Setting.
  - **Dashboard** : Progress Sequence, Key Dates List, Progress Trend Chart, Leaderboard Row, Avatar Stack, Team Role Row, Stacked Bar, System Manager Row, Reallocation Breakdown, System Answers Row, Waiting Queue Row, Risk Summary Row.
  - **Accueil** : Home Hero, Continue Card, Onboarding Line, Home Section Head, Tender Line, Product Line Badge, Role Chip.
  - **Q&A** : Q&A View Switch, Q&A Status Filter.

### Modifié (avant → maintenant)
- (P) **81 entrées du 8 sept. modifiées** (63 inchangées). Les plus réécrites : Statistics Panel, Requirement Table (Review Grid), Stat Block, Activity / Requirement Tag, Detail / Assignment Panel, Triage Bar, Tab Bar, Activity Timeline, Config Section, Nav Tree Section Header.

### Retiré
- (X) **33 entrées marquées « — removed »** : 21 du 8 sept. et 12 ajoutées puis retirées dans la période.
  - **Retirées depuis l'inventaire du 8 sept.** : Version Pill, Change Card, Compare Bar, Flag Tag, Verdict Entry Form, Finalize / Export Modal, Export Option Card, Duplicate Alert, Context Row, Arbitration Guess Button, Q&A Dossier Import Box, Arbitration Queue Card, Bottleneck Row, Q&A Blocked Row, AI Reliability Row, Compliance Bar, Compliance Summary Panel, Dedup Alert Card, Peek Paper Excerpt, Expert Card, AI Feedback Panel (Why Box).
  - Motifs : DEC-069/071/072 (versions), DEC-078 (plus d'état « outdated »), DEC-079 (panneau de décision), DEC-084 (Finalize), DEC-116 (Q&A), DEC-117 (statistiques), DEC-119 (Compare), plus du code mort (`14e3059`).
- (X) **Anomalie de structure** : le titre `## Removed` a été écrasé par l'entrée Tender Chat (`86dbb39`). Les 33 entrées retirées sont désormais rangées à la fin de `## Organisms`, ce qui contredisait la structure imposée par `CLAUDE.md` ; titre rétabli le 9 oct. (`70a0d23`).

### Modèle de données et état
- —

### Fonctions / points d'entrée clés
- —

### Prototype seulement (à ne pas reproduire)
- Les signalements de dérive de jetons (propriétés non suivies comme `--panel-2` ou `--line-2`, valeurs codées en dur) augmentent : 99 lignes de `notes` en parlent au 8 sept., 156 aujourd'hui. Ce sont des dettes à traiter avant tout passage dans Figma.

### Visuel
- —

### Synthèse
- L'inventaire a grandi d'environ 25 % (+61 / −21). Les nouveautés se concentrent sur Allocation (colonnes personnalisées, changements de version, nature/classe), Compliance (panneau de décision, écarts), Dashboard (statistiques) et Accueil. Le titre `## Removed` a été rétabli (`70a0d23`).


## Documents racine — `README.md`, `HANDOVER.md`, `CLAUDE.md`
Volume : `README.md` +6 (2 commits) ; `HANDOVER.md` +2 (2) ; `CLAUDE.md` +1 / −1 (1).

### Ajouté
- (P) `README.md` : bandeau vers `docs/current/README.md` (`7f50eda`) et paragraphe sur la version locale avec police de marque (`build_fonts.py`, puis `build_merge.py`, puis `local/index.html`) (`e82c293`).
- (P) `HANDOVER.md` : bandeau vers `docs/current/`. Il mentionne l'assemblage à **huit** sources et `data.js` venant d'`import_capture_doors.py` (`7f50eda`, `14e3059`).

### Modifié (avant → maintenant)
- (P) `CLAUDE.md` : échelle de jetons suivie + `--font-heading`, `--brand-red` (`dd816be`). Les règles de maintenance de `COMPONENTS.md` sont inchangées.

### Retiré
- —

### Modèle de données et état
- —

### Fonctions / points d'entrée clés
- —

### Prototype seulement (à ne pas reproduire)
- Le corps de `README.md` est antérieur au 8 sept. et reste **périmé** :
  - « six standalone screens », `suivi-experts-et-versions.html`, `expert-space.html` ;
  - « the one fully navigable project » ;
  - « Image containers » ;
  - son bandeau dit « sept sources », au lieu de huit.

### Visuel
- —

### Synthèse
- Se fier à `docs/current/README.md` et à la docstring de `build_merge.py`, pas au corps du `README.md` racine.

# Partie 3 — Allocation

## Allocation — vue d'ensemble — `revue-documentaire.html`
Volume : +3 659 / −1 584 lignes depuis 5e7ae6b (6 039 → 8 114 lignes) ; 83 commits. Les blocs suivants découpent ce même fichier par sous-domaine (modèle et statuts, relance et clés, tableau, panneau, versions / vue Document, colonnes personnalisées).

### Ajouté
- (R) **Tender SIG autonome servi par le même écran** — `IS_SIG_TENDER` (ligne du projet = "SIG") choisit `seedSigDocs()` / `seedSigSections()` au lieu de la capture ou de la démo STB-2026 (`376c6a5`, DEC-044) ; `runsPassOne()` (ligne = Turnkey) pilote tout ce qui relève de la passe de routage.
- (R) **Lecture du projet ouvert dans le shell** — fil d'Ariane `#crumb-project`, titre de la vue Document (`docTitleHTML()`), langue (`TENDER_LANGUAGE`), produit (`TENDER_PRODUCT_ID`), partenaires (`PARTNERS`) lus via `getCurrentProject()` / `getPartners()` (plus de « STB-2026 » codé en dur).
- (P) **Journal, colonnes, largeurs, progression remontés au shell** — voir « Modèle de données et état » ci-dessous.

### Modifié (avant → maintenant)
- (R) **Titre de l'écran** — `<h2>Requirements review</h2>` dans `.review-head` → `<h2 class="tri-title">Allocation</h2>` en tête de la barre de statut (`6b8d477`).
- (R) **Modes d'affichage** — Review / Document / Compare → Review / Document ; « Compare » devient l'onglet Changes de la vue Document, mais l'état interne reste `state.mode==="compare"` (lentille de la vue Document) (`73c7fe7`).
- (R) **En-tête** — bouton « Finalize allocation » (`#finalize-btn`), pastille de version « v2.1 active » et « Modified 12 min ago » supprimés ; menu « View as » limité à l'admin + deux contributeurs.

### Retiré
- (X) Fenêtre « Finalize allocation » (`#export-overlay`, `renderExportModal`, `EXPORT_EXPERTS`), boîte « Why » (`#why-box`), table cachée héritée `table.review`, barre Compare (`.compare-bar`), `.kbd-hint`.

### Modèle de données et état (champs, statuts, clés partagées entre écrans, API du shell utilisée)
- **Bloc exigence** — supprimés : `alloc` (l'« expert »/OBS choisi), `expert` (branches et équipes), `complianceLocked`, `lockedBy`, `derivedCompliance`, `changeDesc`, diff stocké en HTML dans `text`. Ajoutés : `history[]` (`{from,to,type:added|modified|removed,prevText,desc}`), `change` (recalculé par `applyVersionChanges()`), `abs`/`pbs`/`obs` = `{v,id?,c}` (`id` = clé du classeur sur tender à clés), `charLevel` / `charConf` (`{type:{v,level}, class:{v,level}}`, DEC-120), `derivedWith` (`{nature,tech}` au moment de la dérivation, DEC-075), `systemsCleared` (plus aucun système, DEC-076), `figLabel` (figure). `manager` au niveau exigence n'est plus lu que **tant qu'il n'y a aucun système** (DEC-087) ; `type` (Functional…) subsiste dans les données mais n'est plus affiché ni éditable dans le détail/la table (voir Prototype seulement).
- **Branche (= système de l'exigence)** — `{typology,label,manager,branchStatus,allocStatus,allocDoubtField,allocReviewReason,compliance,abs,pbs,obs,tkObs,teams[],proposal,reassignRequest,partner?}` ; `expert` retiré ; `partner:true` + `allocStatus:"allocated"` pour un partenaire (pas de passe 2).
- **Équipe (= entrée OBS)** — `{team,manager,branchStatus,allocStatus,compliance,obs}` ; **plus d'`abs`/`pbs` par équipe** (DEC-055) ; `expert` retiré.
- **Document** — `{id,name,file,versions:[{v,date,note}]}` ; un document sans historique reçoit `[{v:"v1.0"}]`.
- **Personnes** — `MANAGERS` : rôle unique, chaque entrée porte `system` (DEC-102) et `viewAs` ; `ALLOCS` supprimé (ses 3 entrées deviennent des personnes de `MANAGERS`) ; `DIRECTORY` (annuaire simulé).
- **Statuts** — `STATUS_LABEL` + `reassign:"Reassignment requested"` ; `STATUS_RANK.reassign=1` ; `COMPLIANCE_DEFS` = compliant / not_compliant / pending (plus `rnd_needed`) ; `CMP_RANK={not_compliant:2, compliant:1}` ; `DOUBT_FIELD_LABEL` : `type:"Nature"`, `typo:"System"`.
- **`state`** — `colOrder` `["class","typo","abs","type","tkobs","obs","mgr","status","compliance"]` → `["chg","class","typo","abs","pbs","obs","mgr","status","compliance"]` (+ colonnes `cf_*`) ; `colCollapsed` initial = `typo` sur SIG, `chg` si aucun document n'a plusieurs versions ; `colFilters` : `type` et `obs` retirés, `chg` ajouté (+ `cf_*` de type liste) ; nouveaux : `chgBase`, `chgAll`, `ncFilter`, `cmpDoc`, `cmpFrom`, `cmpAutoTab`, `logCat`.
- **API du shell utilisée** — inchangées : `getCurrentUser`, `getTheme`, `route`, `getProjectMode`, `getRedactMode`, `pushAIFeedback`, `pushReassignRequest` / `getReassignRequests` / `updateReassignRequest`. Nouvelles : `getCurrentProject()` (champs `id`, `ref`, `name`, `line`, `product`, `language`), `getPartners(pid)`, `getCustomFields(pid)`, `getTableLayout(pid,"allocation")`, `logReqEvent(pid,reqId,ev)` / `getReqLog(pid,reqId)`, `reportPartnerUsage(pid,"allocation",counts)`, `reportAllocationProgress(pid,{allocated,total})`. Retirée : `setReviewValidated` (Finalize).
- **Ordre d'initialisation** (à respecter) — `DOCS` / `SECTIONS` → `applyProjectMode` → `syncBranchesFromPerim()` sur chaque exigence → `applyCaptureDemoStatuses()` (capture, hors SIG) → `alignDemoPeopleAndModels()` (Turnkey) → `initProgressionStatus()` → `deriveRequirementCompliance()` sur chaque exigence à branches (et `r.manager=null`) → `syncCustomColumns()` → `applyPanels()` / `applyViewColumns()` → `applyFreshProjectStatuses()` (projet neuf) → `applyVersionChanges()` → `seedPartnerBranches()` → `seedTurnkeyReviewMix()` → `seedCharConfidence()` → `snapshotCharacterisation()` → `setMode("review")`. Les blocs « colonnes personnalisées » utilisent `var` car la table peut se rendre avant eux.

### Fonctions / points d'entrée clés (nouveaux, renommés, supprimés)
- `refresh()` appelle désormais, avant tout rendu : `logReqDiffs()`, `syncReassignRequestsFromShell()`, `reportPartnerUse()`, `reportAllocProgress()`.
- Supprimées (fichier entier) : `setAlloc`, `bulkAssignExpert`, `bulkSetType`, `managerViewHTML`, `perimHTML`, `isTurnkey`, `finalVerdictHTML`, `activityAllocStatus`, `reqNeedsManualAllocation`, `askWhy`, `submitWhy`, `renderExportModal`, `renderChangePanel`, `togglePeek` ; constantes `ALLOCS`, `TYPE_SUGGEST`, `HICONF`, `REASONS`, `ACT_ALLOC_LABEL`, `NAV_COLS`, `changesOrder`, `EXPORT_EXPERTS`, `EXPORT_STATS`.
- Identifiants **non renommés** malgré le nouveau vocabulaire (choix assumé, DEC-045) : `typology`, `perim`, `TYPO`/`TY()`, colonne `typo`, `ACTIVITY_MODEL`, `activityHasModel`, `deriveActivityCompliance`, `panelView:"activity"`/`panelActivity`, `activityBlocksHTML`/`activityDetailHTML`, champ `manager` (= « Assigned to »), `branchStatus`, `byRole:"expert"`, `b.domain` (= valeur d'ABS), `b.tech` (= Class), `b.typeAI`/`blockNature()` (= Nature).

### Prototype seulement (à ne pas reproduire)
- Tout l'état vit en mémoire de l'iframe et du shell (effacé par « Reset demo ») ; pas de persistance serveur.
- Les seeds de démonstration sont décrits dans les blocs suivants.

### Visuel
- Police de marque « Alstom UI » / Noto Sans / Antarctica, accent marine, marque rouge devant les titres (DEC-063, DEC-115) ; logo Alstom + « SRM » en texte, marque SRM en favicon (`575fbbe`) ; icônes SVG `<i class=ic-…>` au lieu des emoji (`49ae3a3`) ; pastilles de statut sans point (`73efa97`) ; essai de bandeau marine annulé (`a79114e` / `4341e56`).

### Synthèse
- Un seul fichier sert deux profils (Turnkey `runsPassOne()`, SIG `IS_SIG_TENDER`).
- Le modèle de données a changé de forme (personne par entrée OBS, ABS/PBS au niveau exigence, historique de versions par bloc).
- Plusieurs états partagés passent par le shell : colonnes personnalisées, largeurs, journal, progression, partenaires.

## Allocation — modèle d'allocation, personnes, statuts et validation — `revue-documentaire.html`
Volume : fichier commun (voir le bloc d'ensemble). Commits principaux : `a900e09`, `94eadd4`, `a9b74d2`, `326291b`, `ee9ee21`, `7892738`, `5b5bc8a`, `39e277b`, `22d651b`, `7d737b8`, `7e9b462`, `b851a7a`, `1982965`, `5410006`, `d8937b5`, `e808e7b`, `daaa04e`, `3a5f5f5`, `54fb4cf`, `5019c2b`, `f9ca232`, `f85841f`, `5db101e`, `8b4e790`, `9a4cbb2`, `e5ee6e3`, `8c748a3`.

### Ajouté
- (R) **Une personne par entrée OBS** (DEC-087/123) — `slotsOfBranch()`, `allocSlots(b)` (entrées OBS de tous les systèmes non partenaires, ou l'exigence elle-même si elle n'a aucun système), `allocPeople()`, `assignCount()`, `unassignedLabel()` (« Unassigned » / « n/m assigned »), `targetAssigned()` ; **seul point d'écriture** : `setAllocManager(b, branch, tidx, id)` (garde `branch.manager` et `teams[0].manager` alignés sur un système à une entrée).
- (R) **Membres d'un système** (DEC-102) — `viewerSystem()`, `systemMembers(typ)`, `mgrOptionsFor(typ, current, full)` : les sélecteurs de personne ne proposent que les membres du système (+ la personne en place) ; `viewerOnBranch(br)`.
- (R) **OBS en liste éditable** — `obsListHTML()` / `bindObsList()` : ajout par **recherche** (sur clés : postes de l'ABS en premier puis les autres, recherche sur intitulé + codes ; sinon organisations déjà utilisées sur le tender + « Add “…” » en texte libre), ✕ sur **chaque** ligne y compris la dernière (le dernier retrait vide l'entrée et repasse Incomplete, DEC-076) ; confirmation si l'entrée a une réponse ; `OBS_NOUN` = « role » sur clés, « organisation » sinon.
- (R) **Systèmes retirables jusqu'à zéro et ajout direct par le PM** — `removeSystem(b, typology)` (confirmation si réponse, `systemsCleared`), `openAddSystem(b, body)` (recherche code/nom, partenaires listés à part) (`e808e7b`, `daaa04e`).
- (R) **Partenaires** — `PARTNERS` (depuis `getPartners`, Turnkey seulement) ajoutés à `TYPO` avec `partner:true` ; `isPartner()`, `ptagCls()`, `PARTNER_TIP` ; branche partenaire sans passe 2, « PM · for partner » (`54fb4cf`, DEC-082).
- (R) **Statut au bon endroit** — `allocHolder(b)` : le statut d'allocation d'une exigence à un système se lit sur sa branche (DEC-084) ; `blockedBranchOf()` (réassignation en attente, quel que soit le flux) ; statut `reassign` côté Turnkey (DEC-104).
- (R) **Validation unique** — `confirmCharacterisation(b)` (statut Allocated + efface `typeAI`/`techAI`/`perimAI`, DEC-099) ; `validateZone()` / `validateCtaInner()` : bouton toujours rendu, désactivé avec sa raison (« Characterisation incomplete… », « Allocation incomplete — assign someone and complete ABS / PBS / OBS first. », « A system asked for a reassignment… »), une ligne par système si plusieurs.
- (R) **Droits** — `canCharacterise()` (= PM) / `charDenied()` (DEC-086) ; garde DEC-100 dans `validateBlock()` (« Not your system — read only »).
- (R) **Confiance de caractérisation** — `charLevel()` (nombres < 75 Low, < 85 Medium), `charConfOf()`, `charConfBadgeHTML()`, `dropCharConf()` (un choix humain efface le niveau), `CHAR_HIGH_FROM`, `CHAR_LEVEL_LABEL` (DEC-120).
- (R) **Progression remontée** — `reportAllocProgress()` (nb `isFullyAllocated` / total, DEC-098), `reportPartnerUse()` (DEC-093).

### Modifié (avant → maintenant)
- (R) **Personnes** — manager **et** expert (`alloc` sur l'exigence, `expert` sur branches/équipes, liste fixe `ALLOCS`) → une seule personne (`manager`) par entrée OBS ; « Manager » → « Assigned to » partout (`326291b`, DEC-030/087/123).
- (R) **`ensureBranches()`** — créait une branche avec `manager`/`expert` seulement et la marquait `answered` dès qu'il y avait un propriétaire → recopie `pbs/abs/obs/tkObs/allocStatus/…`, garde le `branchStatus` du seed, **met `b.manager` à null** (la personne passe sur l'entrée OBS), respecte `systemsCleared`.
- (R) **`syncBranchesFromPerim()`** — crée une branche partenaire spéciale ; efface `systemsCleared`. Retirer un système dans le sélecteur du panneau retire aussi sa branche (`7892738`).
- (R) **`computeCharStatus()`** — un titre/une information était « doubt » si `typeAI` → **aucun statut** pour tout non-requirement, testé en premier (DEC-073) ; motifs « Nature/Class proposed by the AI with low confidence », « System is AI-detected, unconfirmed ».
- (R) **`computeAllocStatus()` / `markAllocEdited()`** — Incomplete si `alloc`/`expert` vide → Incomplete si `targetAssigned()` est faux (une entrée OBS sans personne suffit) ou si ABS/PBS/OBS sont tous vides (DEC-103) ; sinon To review si le maillon le plus faible < 75 %, sinon To validate.
- (R) **`effectiveStatus()`** — non-requirement → `null` ; Turnkey : statut du système du contributeur, sinon `reassign` si une réassignation attend, sinon niveau Turnkey (`b.status`) ; multi-système non Turnkey : statut de caractérisation puis « Allocated » ; un système : plus restrictif entre `b.status` et `allocHolder(b).allocStatus`.
- (R) **`validateProgress()` / `validateBlock()`** — deux gestes (caractérisation, puis allocation) → un seul (DEC-099) ; Turnkey : sans index = aiguillage (« turnkey »), avec index = le système ; un contributeur Turnkey valide automatiquement son système ; annulation restaure aussi la branche unique et les drapeaux IA ; toast « … allocated — sent to Compliance » / « … routing validated — sent to its systems ».
- (R) **`visibleTo()` / `myBranchOf()`** — `b.manager===VIEWER` / `branch.manager===VIEWER` → personne présente sur une entrée OBS, ou système d'appartenance du lecteur (DEC-102).
- (R) **Réassignation** — `renderReassignForm(b, body, branch)` vise le système ouvert ; personnes de remplacement prises dans `MANAGERS` (plus `ALLOCS`) ; `approveReassign()` écrit via `setAllocManager()` sur les entrées que tenait le demandeur ; libellés « Right system, wrong person » / « Wrong system » / « This system doesn't apply here ».
- (R) **Consolidation** — `deriveRequirementCompliance()` ne gère plus de verrou ; échelle à deux verdicts (`CMP_RANK`).
- (R) **`reclassify()`** — refus si contributeur ; re-choisir la nature en place confirme une nature IA ; Information → Requirement sur SIG reçoit `perim:["sig"]` et sa branche (DEC-075).
- (R) **`needsManualAllocation()`** — ne sert plus qu'à l'étiquette « no model » des sous-lignes (ex-« manual »).

### Retiré
- (X) `ALLOCS`, `setAlloc()`, `bulkAssignExpert()`, `managerViewHTML()`, `TYPE_SUGGEST` + carte « AI Suggestion » d'assignation, `askWhy()`/`submitWhy()` + `REASONS`/`HICONF` (DEC-054).
- (X) `finalVerdictHTML()`, `complianceLocked`/`lockedBy`, sélecteurs de verdict sur sous-lignes système/équipe (`data-branchcompl`, `data-teamcompl`) (DEC-028/039).
- (X) `activityAllocStatus()` + `ACT_ALLOC_LABEL` (trois états Not started / In progress / Allocated), `reqNeedsManualAllocation()`, pastille `#pill-manual`, filtre `manual` (DEC-103).
- (X) Finalize : `#finalize-btn`, `#export-overlay`, `renderExportModal()`, garde « all requirements allocated », appel `setReviewValidated(true)` (DEC-084).

### Modèle de données et état (champs, statuts, clés partagées entre écrans, API du shell utilisée)
- `MANAGERS` (démo) : `admin`, `m_sig` (SIG, View as), `m_inf` (SEN, View as), `sup` (SIG), `m_mln` (TRK), `infra` (SEN), `cyber` (RAMS) ; une personne choisie dans l'annuaire est ajoutée avec `role:"Assigned from search"` et sans `system`.
- Statuts lisibles : exigence `status` (caractérisation ou niveau Turnkey), branche/équipe `allocStatus`, progression `branchStatus` (`proposed` / `assigned` / `awaiting_answer` / `awaiting_qa` / `reassignment_needed` / `answered`) ; valider une branche met `branchStatus` à `awaiting_answer`.
- Motifs To review produits : nature ou classe IA Low, système IA non confirmé, « Weak ABS/PBS/OBS derivation (NN%) … », « Added/Modified in vX of its document — see the Versions tab », « Flagged for review in bulk ».

### Fonctions / points d'entrée clés (nouveaux, renommés, supprimés)
- Nouvelles : `setAllocManager`, `allocSlots`, `allocPeople`, `assignCount`, `unassignedLabel`, `targetAssigned`, `viewerSystem`, `systemMembers`, `mgrOptionsFor`, `viewerOnBranch`, `allocHolder`, `blockedBranchOf`, `confirmCharacterisation`, `validateZone`, `validateCtaInner`, `removeSystem`, `openAddSystem`, `obsListHTML`, `bindObsList`, `isPartner`, `ptagCls`, `canCharacterise`, `charDenied`, `charLevel`, `charConfOf`, `charConfBadgeHTML`, `dropCharConf`, `seedCharConfidence`, `reportAllocProgress`, `reportPartnerUse`, `registerPerson`, `assignPerson`, `personLabel`, `personSearchHTML`/`bindPersonSearch` (ne sert plus que pour une exigence **sans système**).
- Modifiées : `computeCharStatus`, `computeAllocStatus`, `markAllocEdited`, `effectiveStatus`, `isFullyAllocated`, `validateCtaHTML`, `validateProgress`, `validateBlock`, `ensureBranches`, `syncBranchesFromPerim`, `visibleTo`, `myBranchOf`, `reclassify`, `renderReassignForm`, `submitPropose`, `approveReassign`, `deriveRequirementCompliance`.

### Prototype seulement (à ne pas reproduire)
- (P) `DIRECTORY` (20 noms) simule l'annuaire ; `registerPerson()` fait grossir `MANAGERS` à la volée.
- (P) `alignDemoPeopleAndModels()` (Turnkey) : vide ABS/PBS/OBS/personne des systèmes sans modèle (SEN…) et remplit les valeurs SIG/RST depuis le modèle simulé en gardant les confiances de la capture ; `seedPartnerBranches()` : Voltara sur les deux premières exigences mono-système ; `seedTurnkeyReviewMix()` : 12 % de To review sur `stb2026` seulement ; `applyFreshProjectStatuses()` pour un projet neuf.
- (P) Écarts relevés à la lecture du code (déduit, non testés au navigateur) : le formulaire de réassignation propose tous les contributeurs (non filtré par système, contrairement à DEC-102) ; la cellule System de la table et l'action groupée « Assign › System » ne vérifient pas que l'utilisateur est PM (ALLOC-020 réserve l'ajout direct au PM), et retirer un système depuis la cellule ne supprime pas sa branche (seuls ✕ / `removeSystem()` le font) ; le motif « Weak … derivation — the proposed assignment may be wrong » garde le mot « assignment » (DEC-054 dit « organisation ») ; « % allocated » de la barre compte `effectiveStatus()==="allocated"` (aiguillage validé pour le PM Turnkey) alors que le tableau de bord reçoit `isFullyAllocated()` (tous les systèmes validés).

### Visuel
- Carte système Turnkey : statut en coin, une ligne par OBS (organisation à gauche, personne à droite, manquants en gris), Compliance en ligne de données, « Open system detail » seul en bas (`ad66940`, `cc8f62a`) ; couleur partenaire `--partner` (#1b9aaa, hors échelle de tokens suivie).

### Synthèse
- Toute écriture de personne passe par `setAllocManager()` ; toute lecture par `allocSlots()`/`allocPeople()` — ne pas réintroduire `b.manager` comme source.
- Statuts : non-requirement sans statut ; Incomplete dès qu'une entrée OBS n'a pas sa personne ; validation en un geste ; niveau Turnkey séparé des systèmes.
- Plus de lock, plus d'expert, plus d'« awaiting manual allocation », plus de Finalize.

## Allocation — relance des modèles et clés PBS/OBS/ABS — `revue-documentaire.html`
Volume : fichier commun. Commits principaux : `10891a8`, `48cc854`, `d931f40`, `b851a7a`, `132eef3`, `f909cb7`, `41bbcef`, `920072e`, `42676d5`, `d6efd7f`.

### Ajouté
- (R) **Produits et modèles** — `SYSTEM_PRODUCTS` (sig : Urban, Mainline Wayside, Mainline Onboard ; rst : Metro, High speed), `PRODUCT()`, `productSystem()`, `defaultProductFor()` (produit du tender présélectionné), `rerunModelChoices()` (produits du système, puis « Borrow another system's model »).
- (R) **Relance** — `applyRerunTo(b, branchIdx, productId)` : re-dérive ABS/PBS une fois (écrits sur la branche, et sur l'exigence si un seul système) puis **toutes** les entrées OBS comme un ensemble de valeurs distinctes ; ne touche jamais `manager`, `team`, statuts ; met à jour `derivedWith` ; renvoie `changed` (DEC-091 : silencieux si identique). `rerunBlockedReason()` (réponse ou verdict enregistré ; `awaiting_qa` ne bloque plus, DEC-089), `branchRerunBlockedReason()` (une entrée bloquée bloque tout, DEC-056).
- (R) **Contrôles** — `rerunControlHTML()` (« ↻ Re-run ▾ », inerte avec motif si bloqué) sur l'en-tête du bloc de modèle quand une seule feuille est en jeu (système du contributeur, système unique, détail de système Turnkey) ; `bindRerunControls()` ; trace via `pushBranchLog()` (« Re-ran allocation with … (borrowed …) — same result »).
- (R) **Relance en masse** — `bulkRerun(productId)` + menu `#sel-rerun-menu` (tous les produits) : seulement les exigences à un système ; compte à part bloquées, multi-systèmes (« re-run those from the panel ») et non-exigences (vérifiées **avant** `ensureBranches()`).
- (R) **Proposition après changement de nature/classe** — `snapshotCharacterisation()`, `charChange()`, `rerunPromptHTML()` : ligne « ↻ Re-run the model » (ou « re-run blocked » / « check ABS / PBS / OBS by hand » si pas de modèle) au-dessus d'ABS (DEC-075).
- (R) **Clés** — `KEYS = window.SRM_KEYS` (inclus par `/* @include keys.js */`), `KEY_PRODUCT`, `keyedVocab(productId)`, `TENDER_PRODUCT_ID` (depuis `project.product`), `TENDER_KEYS`, `KEY_ABS()`, `KEY_PBS()`, `PBS_LABEL()`, `pbsOptionsHTML()` (familles en optgroups, élément hors liste sous « From another product's model »), `absControlHTML()` / `pbsControlHTML()` (listes sur tender à clés, texte sinon), libellé d'en-tête patché en « OBS · role ».

### Modifié (avant → maintenant)
- (R) **Ordre de chaîne** — `DERIV_CHAIN=["pbs","abs","obs"]` → `["abs","pbs","obs"]` (DEC-008) ; `invalidateDownstream()` efface sur **tous** les détenteurs (exigence, branche unique, et `teams[i].obs`) et annonce ce qui a été effacé.
- (R) **`derivationChainHTML(b, myBranch, derivSrc)`** — paramètre `rmView` supprimé ; plus de bloc « Pass 1 / Distribution across activities » ni de flèche « ↓ » ; ABS puis PBS puis la liste OBS (`obsListHTML`) dès qu'une feuille est résolue ; un OBS sans valeur affiche « — No organisation derived yet — » (plus le nom de la personne, DEC-054).

### Retiré
- (X) Contrôles de relance par organisation (`d931f40` puis retirés par `b851a7a`, DEC-056) ; contrôle de relance sur les cartes système Turnkey (ajouté par `f909cb7`, retiré par `920072e`).

### Modèle de données et état (champs, statuts, clés partagées entre écrans, API du shell utilisée)
- `KEYS` : `{version, products, pbs:[{id,parent,level,name,label,products}], abs:[{id,label,note,products}], obs:[{id,title,abs,skills,soa,code,products}]}` ; seuls les produits Mainline sont « à clés » (`KEY_PRODUCT`).
- Valeurs de dérivation à clés : `abs={v,id,c}`, `pbs={v:"<id> · <name>",id,c}`, `obs={v:title,id,c}` ; une valeur choisie à la main a `c:null`.

### Fonctions / points d'entrée clés (nouveaux, renommés, supprimés)
- Nouvelles : `runAllocationModel`, `applyRerunTo`, `rerunBlockedReason`, `branchRerunBlockedReason`, `rerunModelChoices`, `rerunControlHTML`, `bindRerunControls`, `bulkRerun`, `snapshotCharacterisation`, `charChange`, `defaultProductFor`, `rerunPromptHTML`, `keyedVocab`, `absControlHTML`, `pbsControlHTML`, `pbsOptionsHTML`.

### Prototype seulement (à ne pas reproduire)
- (P) **Modèles simulés** — `runAllocationModel()` tire déterministiquement (hash de l'id + produit) dans les clés (Mainline) ou dans `MODEL_VOCAB` (vocabulaires **inventés** pour SIG Urban, RST Metro, RST High speed) ; `ACTIVITY_MODEL={sig, rst}` : RST « avec modèle » est une hypothèse (DEC-059).
- (P) La relance globale (ALLOC-015) n'existe pas dans cet écran ; les paramètres ne l'affichent qu'à titre indicatif.

### Visuel
- Ligne de proposition de relance pleine couleur, une seule ligne de hauteur ; menu de relance en deux sections.

### Synthèse
- Relance = niveau exigence, ABS/PBS/toutes les OBS, jamais la personne ; bloquée par réponse/verdict ; silencieuse si identique.
- Sur un tender Mainline, la chaîne est faite de listes issues de `keys.js` ; ailleurs, texte libre.

## Allocation — tableau, filtres, clavier et actions groupées — `revue-documentaire.html`
Volume : fichier commun. Commits principaux : `3e0e369`, `171651e`, `aac89b1`, `cdce5a9`, `083e9a3`, `3a5f5f5`, `5ba326f`, `0e0c64a`, `9a4cbb2`, `6b8d477`, `df69bfc`, `73c7fe7`, `8365089`, `14e3059`, `8c748a3`.

### Ajouté
- (R) **Colonne Changes** (`c-chg`, voir bloc Versions) et **cellules de colonnes personnalisées** ajoutées par `rowHTML()` (`cfCellsHTML`/`cfAppendCells`), vides sur sous-lignes et lignes d'information.
- (R) **Clavier** (DEC-085) — gestionnaire `keydown` global : X, Maj+↑/↓ (J/K), ⌘/Ctrl+A (tout ce qui est visible), Échap, V (sélection ou ligne active), N (`nextNeedingAction()` / `needsAllocAction()`), C (`toggleChgColumn()`), Entrée/F2 (`editActiveCell()`), A (focus « Assigned to » de la ligne), ⌘/Ctrl+Z (`undoLast()`), ] / [ dans la lentille Changes ; `focusin` sur une cellule la rend active ; ←/→ suivent `["sel","id","req",...state.colOrder]` (ordre affiché, colonnes perso comprises).
- (R) **Annulation** — `UNDO_STACK` (30 entrées) alimenté par tout `toast(msg, kind, undo)` ; aujourd'hui : assignation via la cellule « Assigned to » d'une ligne, validation unitaire, validation groupée.
- (R) **Colonnes redimensionnables** — `tableLayout()` (shell `getTableLayout(pid,"allocation")`), `colW()`, `COL_MIN`, `bindHeaderResize()` → `TE.bindColumnResize()` ; la cellule System se re-rend quand sa largeur change ; « Reset column widths » dans View.
- (R) **Cellule System sur une ligne** — `typoTagsHTML(per, proposed)` + `typoCellBudget()` : autant d'étiquettes que la largeur le permet puis « +N » (infobulle « Also: … ») ; toutes en Wrap text ; `sys-conf` = certitude du routage Turnkey (`tkObs.c`) à côté de l'étiquette (DEC-077).
- (R) **« Assigned to » multi-entrées** — `assignSummaryHTML(b)` (noms, « n/m assigned » ou « Unassigned », détail par système en infobulle ; « PM · for partner »).
- (R) **Lignes d'autrui verrouillées** — `lockForeignRows(win)` (DEC-100) : contrôles désactivés sauf case de sélection et chevron.
- (R) **OBS faible signalé dans la cellule** — `weakObsHTML()` sur sous-lignes système/équipe.
- (R) **Barre de statut** — `#alloc-pct` (« % allocated »), compteurs limités à `reqs().filter(visibleTo)`, « N of M shown » dans la barre d'outils seulement quand un filtre réduit la liste ; icône d'aide clavier `.kbd-help`.

### Modifié (avant → maintenant)
- (R) **Colonnes (`RCOLS`)** — `sel,id,req,class,typo(112px),abs,type(PBS 5 valeurs),tkobs,obs,mgr,status,compliance` → `sel,id,req,chg,class,typo(136px),abs,pbs(150px),obs,mgr,status,compliance` + `cf_*` ; en-têtes « Activity » → « System », « Manager » → « Assigned to », « OBS · team » sans filtre de colonne.
- (R) **`rowInnerHTML()`** — Class désactivée pour un contributeur ; ABS = `<select>` sur clés, texte sinon ; PBS = `<select>` sur clés, **lecture seule** sinon ; OBS = texte (plus `<select data-alloc>`) ; Assigned to = `<select data-mgr>` limité aux membres du système si **une** entrée OBS, sinon résumé ; Compliance en lecture ; chevron de sous-lignes déplacé de la cellule ID vers Requirement ; badges « ⑂ N », « ⚠ Blocked » calculé en direct (`blockedBranchOf`), « Δ vX » (seulement quand la colonne Changes est masquée).
- (R) **Clic sur la pastille de statut** — valide si To review ou To validate (avant : tout sauf Incomplete) ; sur Turnkey (PM) = valide l'aiguillage.
- (R) **`branchRowHTML()` / `teamRowHTML()`** — sélecteurs manager + expert + verdict → un sélecteur de personne (membres du système) via `setAllocManager`, OBS/ABS/PBS en texte, verdict en lecture ; statut des sous-lignes masqué pour le PM sur Turnkey ; partenaire « PM · for partner » ; équipe sans nom = « Organisation N » / « Role N ».
- (R) **`infoRowHTML()` / titres** — plus de pastille « To review » (DEC-073) ; bouton de reclassement ▾ retiré (`083e9a3`).
- (R) **Tri (`SORT_KEYS`)** — `type` → `pbs` ; `mgr` = noms des personnes des entrées OBS ; `obs` = valeur OBS de l'exigence.
- (R) **Filtres de colonne (`COL_FILTER_DEFS`)** — `type` et `obs` retirés ; `mgr` « Assigned to » = une valeur par entrée OBS (+ `__pm`) ; `chg` ajouté ; libellé System ; `emptyColFilters()` construit depuis les clés vivantes (corrige « Show only these » qui cassait les entonnoirs Changes et colonnes perso).
- (R) **Constructeur avancé (`ADV_FILTER_FIELDS`, `ADV_FIELD_GROUPS`)** — `type`/`obs` énumérés → `pbs`/`obs` texte ; `mgr` « Assigned to » ; `passdoubt` « Doubt — where » ; `changed` « Changed in latest version » ; `manualalloc` retiré ; groupe « Custom columns » (type `multi` pour les listes multiples).
- (R) **Actions groupées** — Assign : 4 champs (Manager, OBS, Activity, PBS) → 2 (Assigned to, System) ; `bulkAssignManager(mid)` écrit sur les entrées OBS du système de la personne (remplace une entrée unique, remplit seulement les entrées vides si plusieurs), refuse sans système pour un contributeur ; `bulkSetTypology()` crée la branche du système ajouté ; `bulkSetClass()` refusé aux contributeurs (bouton Classify masqué en vue restreinte) ; `bulkValidate()` annulable ; nouveau menu « Re-run ».
- (R) **`VIEW_COLUMNS`** (préréglages Turnkey) — vue PM : masque ABS/PBS/OBS/Assigned to, montre System/Status/Compliance ; vue système : tout (TK OBS et PBS-type retirés).
- (R) **Performance** — `renderReview()` ne reconstruit plus la table hors du mode Review ; `findBlock()` mémorise les positions (`_blockAt`, revalidées contre `SECTIONS`) (`8365089`).

### Retiré
- (X) Colonnes `c-type` (PBS à 5 valeurs) et `c-tkobs` ; `tkObsCellHTML` ; `.row-natpick` ; `#pill-manual` ; `.kbd-hint` (J/K/V/A) ; sélecteurs `data-alloc`, `data-type`, `data-branchexp`, `data-teamexp`, `data-branchcompl`, `data-teamcompl` ; `NAV_COLS` figé.

### Modèle de données et état (champs, statuts, clés partagées entre écrans, API du shell utilisée)
- Largeurs : `getTableLayout(pid,"allocation").widths[col]` en px (mémoire du shell, effacée par Reset demo).
- Filtres enregistrés : inchangés, `localStorage` via `TE.loadSavedFilters("review")`.

### Fonctions / points d'entrée clés (nouveaux, renommés, supprimés)
- Nouvelles : `typoCellBudget`, `typoTagsHTML`, `assignSummaryHTML`, `weakObsHTML`, `lockForeignRows`, `needsAllocAction`, `nextNeedingAction`, `editActiveCell`, `undoLast`, `tableLayout`, `colW`, `bindHeaderResize`.
- Modifiées : `rowInnerHTML`, `infoRowHTML`, `branchRowHTML`, `teamRowHTML`, `bindVRows`, `navCols`, `renderTriage`, `renderReview`, `toast`, `bulkAssignManager`, `bulkSetTypology`, `bulkSetClass`, `bulkValidate`, `applyViewColumns`, `renderColumnsPanel` (groupement par système masqué sur SIG, « Reset column widths »).
- Supprimées : `bulkAssignExpert`, `bulkSetType`, `togglePeek`.

### Prototype seulement (à ne pas reproduire)
- (P) Toutes les lignes sont rendues (pas de virtualisation ; le commentaire de la baseline qui parlait de « virtualized grid » a été corrigé, le comportement était déjà celui-là) — insuffisant pour 100 000 lignes (DEC-023).
- (P) La recherche plein texte matche encore `b.type` (Functional…), champ sorti d'Allocation (DEC-074).

### Visuel
- Titre dans la barre de statut, mini-barre « % allocated » ; chips de filtre qui passent à la ligne au lieu d'être tronqués ; texte libre avec ellipse ; poignées de redimensionnement visibles au survol ; pastille Changes en couleur IA.

### Synthèse
- Colonnes : + Changes, + colonnes perso, − TK OBS, − PBS-type ; OBS et Compliance en lecture ; PBS éditable seulement sur clés.
- « Assigned to » = entrées OBS ; assignation de masse cantonnée au système de la personne.
- Clavier et annulation complets ; colonnes redimensionnables persistées par tender dans le shell.

## Allocation — panneau de détail et journal d'activité — `revue-documentaire.html`
Volume : fichier commun. Commits principaux : `a900e09`, `092baee`, `74d3c51`, `e151286`, `1982965`, `f8aa992`, `9435d3f`, `d8937b5`, `920072e`, `f85841f`, `40dae81`, `ad66940`, `cc8f62a`, `7a1d771`, `db723a1`, `1129260`, `41de42d`, `e962c96`, `8dd5f94`.

### Ajouté
- (R) **`renderSettings()` à quatre branches** — PM Turnkey (`pmClassificationHTML` + validation + `activityBlocksHTML`, ou `activityDetailHTML` quand un système est ouvert) ; contributeur (`contributorDetailHTML`) ; lecture seule (`readOnlyReqHTML`, DEC-100, pour tout contributeur sans système à lui sur l'exigence) ; sinon vue « SIG », de fait celle du PM hors Turnkey (Nature, Class, champ System hors SIG, `derivationChainHTML`, cartes Allocations, recherche de personne seulement si l'exigence n'a aucun système, validation, colonnes perso, source).
- (R) **`contributorDetailHTML()`** — ordre fixe : Nature, Class (lecture seule), modèle du système + relance, ABS, PBS, liste OBS, `systemAllocationsHTML()` (une carte par OBS avec statut et personne), demande de réassignation à traiter, validation du système, colonnes perso, proposition, source.
- (R) **`activityDetailHTML()` = vue SIG du système** (DEC-101) — Nature, Class, `derivationChainHTML(b, branch, branch)`, `systemAllocationsHTML()`, validation du système, bloc de proposition ; détail partenaire = encadré explicatif (`.partner-box`).
- (R) **`readOnlyReqHTML()`** — « Not assigned to you — read only », Nature, Class, puis par système ABS / PBS / OBS · personne.
- (R) **Cartes système Turnkey** — `obsBreakdownHTML()` : une ligne organisation / personne ; statut d'allocation du système en coin ; Compliance ; « Open system detail → ».
- (R) **Champs** — `natureFieldHTML()` (3 natures, niveau de confiance, lecture seule pour contributeur), `classFieldHTML()` (dans tout détail d'exigence), `sourceFieldHTML()` (seulement sans lien §), lien paragraphe `#set-para` (`paragraphOf()`).
- (R) **Journal d'activité partagé** — `logReq(id, ev)` → shell `logReqEvent()` ; `reqLogOf(id)` → `getReqLog()` ; `logReqDiffs()` compare à chaque `refresh()` un instantané (`snapReq()` : nature, classe, statut, par système statut / ABS / PBS / OBS / personnes, allocation complète) et journalise chaque écart au nom du lecteur ; jalons `captured` / `allocated` (« Allocated — sent to Compliance ») ; `activityFor()` fusionne journal partagé + capture + historique de versions ; filtre par catégorie (`LOG_CATS`, `state.logCat`) ; un commentaire est journalisé (`cat:"comment"`).

### Modifié (avant → maintenant)
- (R) **En-tête du panneau** — pastille = statut **du système du contributeur** s'il en a un ; badge « N assignments » (`.assignments-badge`) supprimé ; motif de revue sur la même source ; lien « § n° titre ».
- (R) **`pmClassificationHTML()`** — « Type » → « Class » ; PBS de la passe Turnkey = élément produit (texte, plus les 5 valeurs) ; confiance affichée seulement s'il y a une valeur ; liste « System » : % de l'IA **ou** « manual » (ajouté à la main), « has a model », ✕ par système, « + Add system » (recherche) au lieu d'ouvrir le formulaire de proposition (qui plantait).
- (R) **`activityBlocksHTML()`** — « Activities (N) » → « Systems (N) » ; « OBS · team » + « Manager / expert » joints par « · » → une ligne par organisation avec sa personne.
- (R) **Bloc Allocations (PM, hors Turnkey)** — une carte par **système** avec Manager + Expert → une carte par **organisation** (DEC-060) avec son système en étiquette seulement sur Turnkey ou multi-système, son statut, « Assigned to » (`data-panelallocmgr`).
- (R) **`roleRecapHTML()`** — Admin / Manager / Expert → Admin + une ligne par personne des entrées OBS + « To assign — k of m ».
- (R) **`proposeBlockHTML()`** — boutons `.propose-btn` ; « + Missing activity » → « + Missing system » ; un seul bloc partout (plus « Raise a problem » dans le détail d'activité).
- (R) **Validation** — `validateCtaHTML()` en fin de panneau → zone `.validate-zone` juste après les données confirmées, collante en bas tant qu'elle est hors écran (`1129260`).
- (R) **Onglet Activity** — lignes fabriquées (`activityFor()` codé en dur pour SRM-00017, SRM-00021…) et `b.branchLog` local → journal partagé ; `pushBranchLog()` écrit désormais dans ce journal.
- (R) **Onglets** — + Versions (conditionnel) ; Translation masqué si `TENDER_LANGUAGE==="en"` ; « Read in » met la langue originale en premier (§3.8).

### Retiré
- (X) `finalVerdictHTML()` (Lock/Unlock), carte « AI Suggestion » d'assignation, `managerViewHTML()` + `#mgr-view`/`#f-manager`, « Classification » + indice de routage, « Confirm AI activity » (`#perim-confirm`), note Turnkey (`.tky-note`), champ « Specialty », bloc « Distribution across systems » (`db723a1`, `14e3059`), fiche de changement (`renderChangePanel`).

### Modèle de données et état (champs, statuts, clés partagées entre écrans, API du shell utilisée)
- Événement de journal : `{ts, time, live, who, cat: status|alloc|compliance|comment, what, from?, to?, k: human|ok|warn|ia|comment, milestone?: captured|allocated|answered|declared}`, stocké par le shell par projet puis exigence ; lu aussi par Compliance et le tableau de bord (`getActivityLog`).

### Fonctions / points d'entrée clés (nouveaux, renommés, supprimés)
- Nouvelles : `contributorDetailHTML`, `readOnlyReqHTML`, `systemAllocationsHTML`, `obsBreakdownHTML`, `natureFieldHTML`, `classFieldHTML`, `sourceFieldHTML`, `paragraphOf`, `versionsTabHTML`, `renderRemovedPanel`, `logReq`, `reqLogOf`, `snapReq`, `logReqDiffs`, `activityItemHTML`.
- Modifiées : `renderSettings`, `derivationChainHTML`, `pmClassificationHTML`, `activityBlocksHTML`, `activityDetailHTML`, `roleRecapHTML`, `proposeBlockHTML`, `activityFor`, `pushBranchLog`, `selectBlock` (id inconnu → toast « This requirement isn't in this tender »).

### Prototype seulement (à ne pas reproduire)
- (P) Historiques de démonstration semés par le shell (`seedReqLog`) ; l'auteur d'un écart détecté par instantané est le lecteur courant (« View as » compris).
- (P) Onglet REX (titres seulement) toujours présent alors que REX est hors V1 (DEC-021).

### Visuel
- Journal dessiné en « ligne de rail » avec stations pour les jalons (`41de42d`) ; en-tête d'id dégagé du bouton de repli ; onglets à défilement horizontal ; boutons de proposition renforcés.

### Synthèse
- Quatre vues de panneau (PM Turnkey, système, contributeur, lecture seule) ; le détail d'un système Turnkey réutilise la vue SIG.
- Une carte par organisation avec sa personne ; validation collée aux données.
- Journal d'activité unique, partagé avec Compliance via le shell.

## Allocation — versions, colonne Changes et vue Document — `revue-documentaire.html`
Volume : fichier commun. Commits principaux : `82ab34e`, `5410006`, `f8aa992`, `73c7fe7`, `8365089`, `df69bfc`, `14e3059`.

### Ajouté
- (R) **Modèle de versions** — `docOfBlock()`, `activeVersion()`, `verIdx()`, `latestChange(b)` (changement de la version en vigueur), `rangeChange(b, fromV)` (changements repliés depuis une version), `wordDiffOps()` / `wordDiffHTML()` (diff mot à mot par LCS ; le texte stocké reste propre).
- (R) **`applyVersionChanges()`** (DEC-072) — à l'init, toute exigence ajoutée/modifiée dans la version en vigueur reçoit `change`, `status:"doubt"`, motif « Added/Modified in vX of its document — see the Versions tab ».
- (R) **Colonne Changes** — `chgBaseOf()`, `chgOf()`, `chgVersionsOf()`, `chgDiffHTML()` (sur une ligne : quelques mots avant le premier changement, « … » ailleurs), `chgCellHTML()` (« Single version », « No change », étiquette « New » ou versions, sélecteur « vs vX ▾ »), popovers `openChgRowPop()` / `openChgAllPop()` (« vs previous » / « vs first », réinitialise les choix par ligne), `toggleChgColumn()` (touche C), `renderChgHead()`.
- (R) **Onglet Changes de la vue Document** — `cmpDocs()`, `cmpEnsure()`, `cmpBlocksOf()`, `cmpChangeIds()`, `cmpChangeOf()`, `renderNavTabs()` (Outline / Changes, seulement si un document a plusieurs versions), `changeImpact()` (« ↺ Was answered — back to To review », « New — needs allocation », « Removed — its work stays archived… »), `ncItems()` + `NC_FILTERS` (added / modified / removed / reopen), `renderNavChanges()` ; `gotoChange()` parcourt la liste filtrée ; rail `#nav-rail-chg` quand le navigateur est replié.
- (R) **Onglet Versions** — `versionsTabHTML(b)` (type, date, note, document comparé, diff, texte précédent repliable, versions antérieures, « Show in the document → ») ; **`renderRemovedPanel()`** pour un bloc `ghost`.

### Modifié (avant → maintenant)
- (R) **Mode Compare** — `body.mode-compare` avec barre `.compare-bar` (sélecteurs inertes, « +1 ~2 −1 » et « Change 1/3 » codés en dur, `changesOrder` figé) → lentille `state.mode="compare"` de la vue Document, pilotée par le navigateur ; le bouton Document reste actif ; `setMode("compare")` déplie le navigateur.
- (R) **`renderDoc()`** — en lentille Changes : un seul document (`state.cmpDoc`), en-tête « vA → vB », blocs modifiés rendus avec `wordDiffHTML()`, `data-chlabel` (« Added/Modified in vX », au lieu du CSS « Added in v2.1 »), blocs supprimés seulement dans la plage comparée ; pied de page `Doc i / n — <version en vigueur>` ; titre = tender ouvert.
- (R) **Données de changement** — `change:"modified"` + `changeDesc` + `<span class="diff-…">` dans `text`/`textOriginal` → `history[]` par bloc ; versions par document (démo : volume principal v1.0 → v2.1, annexe A v1.0 → v1.1 ; SIG : spécification v1.0 → v2.1, annexe une version ; capture : une version par document).
- (R) **Pastille « changes »** — « changes v2.0 → v2.1 » avec un « + 1 » ajouté au compte → « changed in latest version », compte des exigences avec `change`.
- (R) **Vue Document** — `natureTag()` en pointillés « is-ai » avec infobulle de niveau ; `attachReclassify()` inerte pour un contributeur ; badge « Unassigned » → `data-unassigned` (« Unassigned » / « n/m assigned ») ; puce d'exigence « Requirement · <statut> » (au lieu de « <type> · <statut> ») ; figure de démonstration étiquetée (`figLabel`).
- (R) **`renderNav()`** — compteurs de changements par section retirés ; non redessiné tant que l'onglet Changes est ouvert.

### Retiré
- (X) `.compare-bar`, `#ver-a`/`#ver-b`, `.version-pill`, `changesOrder`, `renderChangePanel()` (New / Reviewed, no impact / Action required, « Create action / reminder »), badges `.b-change`, `.sec-changes`.

### Modèle de données et état (champs, statuts, clés partagées entre écrans, API du shell utilisée)
- `history[{from,to,type,prevText,desc}]` sur chaque bloc (y compris `kind:"ghost"` pour un supprimé) ; `DOCS[i].versions[]` ; état `chgBase{id:v}`, `chgAll:"prev"|"first"`, `cmpDoc`, `cmpFrom`, `changeIndex`, `ncFilter`, `cmpAutoTab`.
- Aucune lecture des versions téléversées dans Documents (`documents.html`) : les versions d'Allocation sont ses propres seeds (déduit : aucun appel shell correspondant).

### Fonctions / points d'entrée clés (nouveaux, renommés, supprimés)
- Nouvelles : celles listées en « Ajouté » + `docTitleHTML`.
- Modifiées : `renderDoc`, `renderNav`, `renderTable`/`rowBlock` (marqueur « n/m assigned »), `natureTag`, `natureLabelChip`, `attachReclassify`, `gotoChange`, `setMode`, `findBlock` (cache).
- Supprimées : `renderChangePanel`.

### Prototype seulement (à ne pas reproduire)
- (P) Historiques de versions écrits à la main dans les seeds (STB-2026 démo et RFP-2026-114) ; jamais de texte inventé dans un document capturé.
- (P) Puce des lignes de tableau dans la vue Document (`rowBlock`) affiche encore `r.type` (« Interface · … ») — résidu contraire à ALLOC-T26.

### Visuel
- Diff : supprimés barrés sur fond rouge pâle, ajoutés sur fond vert pâle ; cartes de changement avec type coloré et impact en orange quand une réponse est rouverte.

### Synthèse
- Versions par document, diff calculé, retour en To review : tout part de `history[]`.
- Plus de mode Compare ; colonne Changes dans la table et onglet Changes dans la vue Document.
- Mesuré à 4 000 exigences (~150–170 ms par clic) après les optimisations de `8365089`.

## Allocation — colonnes personnalisées — `revue-documentaire.html`
Volume : fichier commun. Commits principaux : `9f677cf`, `cdce5a9`, `aac89b1`, `3537205`, `14e3059`.

### Ajouté
- (R) **Registre** — `syncCustomColumns()` fait de chaque définition une colonne de premier rang : `RCOLS`, `state.colOrder`, `COLUMN_TOGGLE_DEFS` (étiquette « custom »), `ADV_FILTER_FIELDS` (`text` / `enum` / `multi`), `SORT_KEYS`, `COL_FILTER_DEFS` (listes), groupe « Custom columns » ; nettoie tout ce qui référence une colonne supprimée (y compris une condition de filtre avancé) ; `cfRenderStyle()` (CSS d'ordre et de masquage générée), `cfRenderHead()` (en-tête, tri, entonnoir pour les listes, ✎).
- (R) **Cellules** — `cfCellsHTML()` (texte `.cell-text`, liste `.cell-select`, multiple = bouton `cf-multi` + popover `#cf-pop` à cases, clavier ↑/↓/Espace/Entrée/Échap), `cfBindCells()`, `cfCommit()`.
- (R) **Panneau** — `cfPanelHTML()` / `cfBindPanel()` (chips pour le choix multiple) avec la mention « entered by people… ».
- (R) **Éditeur (PM seulement)** — `cfOpenEditor()` (refus pour un contributeur ; bouton `#cf-add-btn` et ✎ masqués en vue restreinte), `cfRenderEditor()` : nom, type texte/liste, options (retrait refusé si utilisée, avec le compte), « Allow several values », verrou de type si des valeurs existent, verrou multiple → simple si une exigence tient plusieurs valeurs ; suppression en deux temps avec le nombre de valeurs détruites ; `cfSaveEditor()` (nom unique y compris face aux colonnes natives, liste ≥ 1 option, simple → multiple enveloppe les valeurs).
- (R) **Visibilité par écran** (DEC-097) — `cfShownHere()` lit `d.shownIn.allocation` (sinon visible si `phase==="allocation"`) ; `cfRememberVisibility()` mémorise le choix View.
- (R) **Export** — l'export interne annonce « N custom columns included — internal exports only ».

### Modifié (avant → maintenant)
- (R) **Moteur de filtres** — nouveau type `multi` (any of / none of / empty / not empty) utilisé par les listes multiples.

### Retiré
- —

### Modèle de données et état (champs, statuts, clés partagées entre écrans, API du shell utilisée)
- Shell `getCustomFields(pid)` → `{defs:[{id:"f<n>", name, type:"text"|"list", multi, options[], phase:"allocation"|"compliance", shownIn:{allocation?,compliance?}}], values:{<reqId>:{<fid>:valeur|[valeurs]}}, seq}` — **commun à Allocation et Compliance** ; valeurs indexées par id d'exigence (survivent aux remises à zéro) ; clé de colonne `cf_<fid>`.

### Fonctions / points d'entrée clés (nouveaux, renommés, supprimés)
- `cfProjectId`, `cfStore`, `cfDefs`, `cfDef`, `cfKey`, `cfHas`, `cfGet`, `cfSet`, `cfUsage`, `cfOptionUsage`, `cfMultiHeld`, `cfDisplay`, `syncCustomColumns`, `cfRenderStyle`, `cfRenderHead`, `cfAppendCells`, `cfCellsHTML`, `cfCommit`, `cfBindCells`, `cfOpenMulti`, `cfCloseMulti`, `cfPanelHTML`, `cfBindPanel`, `cfOpenEditor`, `cfCloseEditor`, `cfRenderEditor`, `cfSaveEditor`, `cfShownHere`, `cfRememberVisibility` ; variables `CF_SYNCED`, `cfEditor` en `var`.

### Prototype seulement (à ne pas reproduire)
- (P) Stockage en mémoire du shell, effacé par Reset demo (cible : définitions + JSONB, filtrage serveur).
- (P) Renommer une option existante : non fait.

### Visuel
- Étiquette « custom » dans View, ✎ sur l'en-tête, fenêtre d'édition avec encadré de danger pour la suppression.

### Synthèse
- Colonnes de premier rang (grille, tri, filtres, panneau, export interne), PM seulement, partagées avec Compliance.
- Toutes les règles destructrices annoncent leur coût avant d'agir.

## Clés PBS / OBS / ABS — `build_keys.py`, `keys.js`
Volume : `build_keys.py` +99 / −0 (nouveau) ; `keys.js` +2 / −0 (nouveau, une ligne de données générée) ; 1 commit (`132eef3`).

### Ajouté
- (R) **`build_keys.py`** — lit le classeur « PBS OBS ABS Keys » (openpyxl) : feuille PBS → arbre à 3 niveaux (lignes sans id rattachées au niveau 3 de la famille ou au niveau 4 selon la fratrie, ids `x<n>`), feuille « ABS (2) » → 16 catégories (id slugifié, note), feuille « OBS (2) » → postes rangés sous la catégorie ABS précédente (lignes « ABS » = en-têtes), codes Skills / SoA / Job ; colonnes produit `urban`, `mainline-wayside`, `mainline-onboard` (croix x/X). Écrit `keys.js` : `window.SRM_KEYS={version,products,pbs,abs,obs}` (223 PBS, 16 ABS, 66 OBS).
- (R) **`keys.js` versionné et obligatoire** — inclus dans `revue-documentaire.html` par `/* @include keys.js */` (le build échoue s'il manque).

### Modifié (avant → maintenant)
- —

### Retiré
- —

### Modèle de données et état (champs, statuts, clés partagées entre écrans, API du shell utilisée)
- Voir le bloc « relance et clés » (`KEYS`, `keyedVocab`).

### Fonctions / points d'entrée clés (nouveaux, renommés, supprimés)
- Script sans fonction exportée ; usage `python3 build_keys.py [classeur.xlsx]`.

### Prototype seulement (à ne pas reproduire)
- (P) Le chemin par défaut du classeur est un chemin local codé en dur : passer le classeur en argument. Le classeur n'est pas versionné (KEY-T01 : `keys.js` doit se reproduire à l'identique).

### Visuel
- —

### Synthèse
- Source unique des listes ABS/PBS/OBS du modèle SIG Mainline ; régénérer plutôt qu'éditer.

## Données de capture réelles — `import_capture_doors.py` (et chargement de `data.js`)
Volume : +23 / −11 lignes depuis 5e7ae6b ; 2 commits (`e5ee6e3`, `14e3059`).

### Ajouté
- (R) **Niveaux de caractérisation** — `_char_level(score)` (< 75 low, < 85 medium, sinon high) ; `seed_demo_confidence()` écrit un **niveau** pour `type` et `class`, et garde un pourcentage pour `abs`/`pbs`/`obs` (DEC-120). L'écran relit aussi les anciens nombres avec les mêmes seuils.

### Modifié (avant → maintenant)
- (R) **Statut du script** — « importeur séparé, au choix » → **le** script qui produit le `data.js` courant ; `import_capture.py` (.xlsx) devient l'ancien importeur (sans niveau de titre, sans systèmes, sans confiance). Vocabulaire « activity » → « system » dans la doc et les messages.

### Retiré
- —

### Modèle de données et état (champs, statuts, clés partagées entre écrans, API du shell utilisée)
- **Chemin de chargement** (inchangé dans son principe) : `import_capture_doors.py` → `data.js` (non versionné) qui pose `window.SRM_DATA = {documents, rows}` → `build_merge.py` l'inline via `/* @include data.js */` dans `revue-documentaire.html` seulement (marqueur remplacé par une chaîne vide s'il n'existe pas) → `buildDataFromCapture()` mappe `rows` (`section`, `docId`, `category` heading/information/requirement, `level`, `perim` issu de « Responsible Entity », `confidence`) en sections/blocs ; sinon `seedDemoSections()`.
- **Nouveau** : la capture n'est **jamais** lue sur un tender SIG (`IS_SIG_TENDER`) ; chaque document de capture reçoit une seule version « As captured » ; `addCaptureFigureAndTable()` y insère une figure et un tableau d'interfaces **de démonstration** (SRM-01401 à SRM-01405, contenu illustratif).

### Fonctions / points d'entrée clés (nouveaux, renommés, supprimés)
- `_char_level` (nouvelle), `seed_demo_confidence` (modifiée) ; côté écran `buildDataFromCapture`, `addCaptureFigureAndTable` (nouvelle), `applyCaptureDemoStatuses` (modifiée).

### Prototype seulement (à ne pas reproduire)
- (P) Confiances générées (≈ 87 % des lignes entièrement confiantes, un seul champ faible sinon, déterministes par id) : échafaudage de démo, pas une mesure.
- (P) `applyCaptureDemoStatuses()` invente classe, ABS (`domain`), `type`, personne et statuts par hash (≈ 2 % Incomplete) ; `seedTurnkeyReviewMix()` force 12 % de To review sur STB-2026.

### Visuel
- —

### Synthèse
- Le chargement de la capture n'a pas changé ; seuls les niveaux de confiance (DEC-120) et la mise à l'écart sur SIG sont nouveaux.

# Partie 4 — Compliance et Risks

> Cette partie couvre `compliance.html` et `risks.html` en entier, ainsi que les contrats du shell (`build_merge.py`) dont ces deux écrans dépendent. Le shell lui-même, `table-engine.js`, Q&A, Documents et le tableau de bord sont décrits dans les autres parties ; ils ne sont cités ici que comme producteurs ou consommateurs. Les règles métier derrière chaque changement sont dans SPECS.md, partie 4.

## Écran Compliance — `compliance.html`
Volume : +2 827 / −733 lignes depuis 5e7ae6b (1 974 → 4 068 lignes) ; 58 commits.

### Ajouté
- **Panneau de décision du contributeur** — `renderDecisionPanel(p,r,br)`. `renderPanel2()` l'appelle dès que `isDeciding(br)` est vrai, c'est-à-dire rôle contributor, système de l'affectation égal au sien, statut ni `answered` ni `reassignment_needed`. Ce panneau contient (DEC-079/080/081) :
  - la file (`myQueue()`, « N left · this is k of N », « Next » qui saute les mises de côté) ;
  - les outils « Set aside » (`toggleAside()`) et « Widen panel » (`state.panelWide` → classe `.wide` sur `#settings2-outer`) ;
  - l'ID et le bouton « § section », qui ouvre la vue Document ;
  - les bandeaux « Reopened by … » et « N questions in the Q&A register » ;
  - le texte, avec l'interrupteur « Original · <langue> » (`state.showOriginal`, `r.textOriginal`) et « View in the document » ;
  - le bloc « Your verdict » : choix (`[data-dpick]`), puis `gapEditorHTML()` sur un NC, Category + Topic sur Turnkey, commentaire, puis `#dp-confirm` ;
  - les actions secondaires « Ask the client » (`state.openForm="ask"`, texte requis) et « Not mine — return it » (`openForm="reassign"`) ;
  - les ressources `state.resTab` (`qa` / `sim` / `rex` / `chat`).
- **Brouillons et mises de côté personnels** — `CMP_PERSONAL` (`drafts`, `aside`), clé `personalKey()` = `<VIEWER>:<reqId>:<typology>`. Le brouillon s'enregistre à chaque saisie (« Draft saved · HH:MM ») et s'efface à la confirmation. La pastille de filtre `#tp-aside` (contributeur) s'ajoute, ainsi que les marques ⚑ / ✎ dans la cellule ID et la classe de ligne `.is-aside`.
- **Exigences similaires** — `similarReqs()` / `simTokens()` : recouvrement des mots de 4 lettres ou plus, au moins 25 %, trois au plus. **Questions publiées aux autres soumissionnaires** — `PUBLISHED_QA`, complété par les Q&A importées dans Q&A (`reg.others`).
- **Documentation d'écart et conformité externe** (DEC-105 à DEC-114) :
  - éditeur : `gapEditorHTML(r,br,editable)` / `bindGapEditor()` ;
  - champ externe et correction PM : `externalFieldHTML()` / `bindExternalField()` (`state.openForm="extfix"`, `state.extFixPick`) ;
  - calcul : `branchExternal()`, `externalOf()`, `gapMissing()` ;
  - cellules et pastilles : `strategyCellHTML()`, `riskCellHTML()`, `extPillHTML()`, `externalPillHTML()` ;
  - risques : `riskSuggestions()` (même chapitre, puis reste), `riskLinkCounts()`, `riskText()`, `riskFirstLine()`, `RISK_Q` ;
  - lectures shell : `gapStrategies()`, `riskList()`, `strategyById()`, `riskById()`, `gapOf()` ; écriture : `setGap()`.
- **Colonnes** `compliance`, `strategy`, `risk` et `external`, ajoutées à `F_RCOLS`, `F_COLUMN_TOGGLE_DEFS`, `F_NAV_COLS` et `state.colOrder`. Le verdict a sa propre pastille, `cmpPillHTML()` avec `CMP_ICON` ✓ / ✕.
- **Structure de la table** :
  - lignes de titre de document et de section (types `doctitle` / `sec` dans `fVROWS`, quand aucun tri n'est actif) ;
  - une flèche par exigence multi-système (`state.expandedBranches`, `[data-branchtoggle]`) ;
  - le niveau 2 des équipes, `fTeamRowHTML()` / `ensureFTeams()`, affiché quand un système a plus d'une équipe.
- **Tri par en-têtes** — `F_SORT_KEYS`, `sortKeyOf()` (colonnes `cf_*` comprises), `setSortCol()` avec le cycle asc → desc → ordre du document, `bindSortHeaders()`, `renderSortIndicators()`, `#sort-reset`.
- **Filtres** :
  - de colonne, « à la Excel », sur System et Assigned to : `COL_FILTER_DEFS`, `state.colFilters` (valeurs **exclues**), `openColFilterPop()`, `#colf-pop`, `.colf-btn` dans l'en-tête ;
  - **filtre avancé**, porté d'Allocation : `ADV_FILTER_FIELDS` (id, text, typo, internal, external, strategy dont `__missing`, risk linked/missing, status, contributor, age, doc, section, plus `cf_*`), `ADV_FIELD_GROUPS`, `renderAdvFilterPanel()`, `passesAdvFilter()` via `TE.matchesFilter`, bandeau `#adv-filter-banner`.
- **Colonnes personnalisées** (DEC-097) — `cfStore()` (shell `getCustomFields`), `syncCustomColumns()`, `cfShownHere()` / `cfRememberVisibility()` (`d.shownIn.compliance`), cellules `cfCellsHTML()` / `cfBindCells()`, éditeur `#cf-overlay` (`cfOpenEditor()`, `cfSaveEditor()`), valeurs dans l'onglet Requirement (`cfPanelHTML()`), bouton `#cf-add-btn` (PM seulement).
- **Redimensionnement des colonnes** — `TE.bindColumnResize` et `fTableLayout()` (shell `getTableLayout(pid,"compliance")`), `fColW()`, « Reset column widths » dans View.
- **« Wrap text »** — `#wrap-toggle`, `state.wrapText`, classe `.wrap-text` sur `#frgrid-body`.
- **Export à options** — `openExport()`, `renderExport()`, `XP_COLS()`, `#xp-overlay` : format, lignes (`all` / `view` / `sel` avec `viewWords`), colonnes, langue.
- **Cloche** — `notifItems()` (retournés, questions chez le client, réponses rouvertes), `renderNotifDrop()`, `#notif-btn` / `#notif-drop`.
- **Annulation** — `UNDO_STACK` (30 entrées), `toast(msg,kind,undo)` avec un bouton « Undo », `undoLast()` (⌘/Ctrl+Z), `snapBranch()` / `BR_UNDO_FIELDS`.
- **Clavier** — X, Maj+↑/↓ (et J/K), ⌘/Ctrl+A, Échap, N (`nextNeedingAction()` / `needsMyTurn()`), ⌘/Ctrl+Z, S, plus l'aide `.kbd-help`. R et Q ont été revus (voir « Modifié »).
- **Phrase d'attente** — `nextStepFor(r,br)` renvoie `{t, act}` dans chaque état ; son `act` décide de l'action primaire (CONF-019/020).
- **Relance unique** — `remindBlock(br)` (raison du refus, ou `null`) et `sendReminder(r,br)` (`lastFollowup="Today"` + journal).
- **Q&A partagé** — `pullQaRegister()` au chargement, `qaStLabel()` ; `ASK_DONE_TIP` sert à griser « Ask the client ».
- **Réouverture par version** — `applyVersionChanges()` au chargement, `docOfReq()`, champ `reopenedBy`.
- **Journal partagé** :
  - écriture : `logReq()` → shell `logReqEvent` ;
  - lecture : `reqLogOf()` → `getReqLog` ;
  - capture des changements : `logCmpDiffs()` / `snapCmp()`, un diff à chaque `refreshAll()` ;
  - affichage : `activityForReq()` (ajoute « Captured » et les réponses déjà enregistrées), `activityItemHTML()`, filtre `LOG_CATS`, champ commentaire `#log-comment-in`.
- **Partenaires** (DEC-082) :
  - `PARTNERS` (lu dans le shell, Turnkey seulement), injecté dans `TYPOS` avec `partner:true` ; `isPartner()`, `ptagCls()`, infobulle ;
  - « PM · for partner » dans `branchWhoHTML()` et `.partner-box` dans le panneau ;
  - formulaire de verdict partenaire (`state.openForm="partner"`, `state.partnerPick`, `#pp-confirm`, `resp.byPM:true`).
- **Liens avec Risks** :
  - icône dans l'en-tête (`parent.route('risks')`) ;
  - écouteur en capture sur `[data-gorisk]` → `setScreenFocus("risks",{risk})` ;
  - à l'arrivée, `takeScreenFocus("compliance")` → `state.riskFocus` (bandeau `#risk-focus-banner`, `riskFocusPasses()`) ou `select(f.select)`.
- **Tender SIG** — `SIG_REQS` (12 exigences L4-), `SIG_QA`, `IS_SIG_TENDER` : il supprime la colonne System du menu View, `COL_FILTER_DEFS.typo` et `ADV_FILTER_FIELDS.typo`, ainsi que le libellé « Assignment · <système> ». `IS_TURNKEY` conditionne Category + Topic.
- **Arrivée du contributeur sur sa file** — `openFirstInQueue()`, appelé après un changement de rôle ou de personne.
- **Remontées vers le shell à chaque `refreshAll()`** : `reportStrategyUsage`, `reportGapStats`, `reportPartnerUsage`. Au chargement : `reportDocReqIndex`.

### Modifié (avant → maintenant)
- **Personnes.** `EXPERTS` (3) + `MANAGERS` (3) deviennent **`MANAGERS` seul** (6 personnes, chacune avec son `typology` ; `viewAs` pour Louis Renaud (SIG) et Paolo Ferri (SEN)). `branch.expert` disparaît : `branch.manager` est **la** personne de l'affectation. (`b932fb4`, `5db101e`)
- **Verdict.** `branch.compliance` devient `branch.internal` (`e4b1b31`). `consolidate()` renvoie `{internal, pending, blocking, remaining, comment}` au lieu de `{compliance, …}`. La règle ne change pas : en attente tant qu'une affectation n'est pas `answered`, puis `CMP_ORDER` `["not_compliant","compliant"]`.
- **Systèmes.** `TYPOS` passe de 5 activités inventées (sig, mln, sys, tlc, inf, avec des libellés longs) aux **16 codes de la capture** (libellé = code), plus les partenaires. Les seeds sont remappés. `REASON_LABEL` dit désormais « system ». (`2a7aa6b`, `7d737b8`)
- **`BLOCK_PRIORITY`.** Avant : `reassignment_needed, awaiting_qa, awaiting_answer, assigned, proposed`. → Maintenant : `reassignment_needed, awaiting_answer, awaiting_qa, assigned, proposed`. Cet ordre décide du libellé Status d'une exigence en attente, du tri par Status et de l'affectation ouverte par `select()`. (DEC-125)
- **`passesB()`.** Avant : `state.filter` (dont `over`), `fExpert`, `fTypo`, `needsMe`. → Maintenant : `state.filter` ∈ {answered, await, qa, reassign} et `passesColFilters()`. **`passes()`** gagne `riskFocusPasses()`, le filtre `aside` et `passesAdvFilter()`, et perd le filtre `out`.
- **`tableRows()`.** Avant : `state.sortBy` (action / status / expert / req, défaut « action »). → Maintenant : `state.sortCol` / `state.sortDir`, sinon ordre du document (`docRank()`, `secCmp()`).
- **`buildFVRows()`.** Avant : les sous-lignes système étaient toujours poussées, sauf sous un filtre de branche. → Maintenant : elles n'apparaissent que si l'exigence est dépliée, avec les équipes et les titres de document et de section.
- **Cellules de ligne.** `consolidatedStatusHTML()` (une pastille fusionnée verdict / Pending / ⛔) est remplacé par `consolidatedProgressHTML()` + `consolidatedComplianceHTML()`, et `branchStatusHTML()` par `branchProgressHTML()` + `branchComplianceHTML()`. Colonnes Expert + Manager → « Assigned to » (`branchWhoHTML()` : une personne, « — unassigned — » ou « PM · for partner »).
- **`renderPanel2()`.** Il délègue au panneau de décision. L'onglet Assignment est construit par état : répondu, `awaiting_qa`, `reassignment_needed`, partenaire (PM), en attente.
  - Réaffectation : **un seul sélecteur `#ra-mgr`**, filtré sur les membres du système (avant : `#ra-mgr` + `#ra-exp`).
  - « Ask the client » est désactivé sur une affectation répondue (avant : « ⇗ Escalate to client Q&A » actif).
  - L'onglet `doc` est supprimé. Le contributeur est ramené sur l'affectation de son système (`state.selBranch`). Le formulaire de verdict de l'onglet Assignment n'existe plus.
- **`escalate(r,br,question)`** (était `escalate(r,br)`).
  - Refus si l'affectation est `answered`.
  - La question part au shell, `pushQuestion(pid,{st:"draft",q,refs:[{req,typology}],from,date,origin:"compliance"})` ; l'id vient du shell (`QA-5N`), alors qu'avant il était local (`"QA-0"+n`).
  - `awaiting_qa` n'est posé que depuis `awaiting_answer`, et l'id rejoint `qaRefs[]`.
  - Une entrée de journal est créée. L'annulation appelle `withdrawQuestion()`.
- **Relance.** Avant : `sendReminderToSelection()` (n'agissait que sur `awaiting_answer`, sans journal) ; R (mettait à jour `lastFollowup` sur toute branche ayant un expert) ; le bouton du panneau n'affichait qu'un toast ; `remindExpert()` ; `#remind-all`. → Maintenant : `remindBlock()` / `sendReminder()` sur chaque chemin. Le bouton groupé `#f-sel-remind` est masqué pour un contributeur, et les affectations non éligibles sont comptées « skipped ».
- **Clavier.** Q : pour le contributeur, il ouvre le formulaire « Ask the client » ; pour le PM, il lance `escalate()` avec une question générique ; il est refusé sur une affectation répondue (avant : `escalate()` sans condition).
- **`renderDoc2()`.** Avant : une seule feuille, légende à 5 états (dont `partial` / `needs-clar`), et un NC sans couleur (`.dblk.non` / `.vdot.non` ne correspondaient pas à `not_compliant`). → Maintenant : **une `.paper` par document** (`SEC_DOC`), légende à 3 états, classes `not_compliant` stylées.
- **`renderNav2()`.** Il ne fait plus que la navigation par section. **`renderTriage2()`** : l'anneau `.p2-ring` (`--p`) avec une infobulle, et la pastille « set aside » ; les compteurs `n-over` / `n-out` disparaissent ; le titre « Compliance » et `#tri-assign` entrent dans la barre.
- **`refreshAll()`.** Il ajoute `logCmpDiffs()`, les remontées au shell, `syncCustomColumns()` au changement de rôle, les bandeaux, les indicateurs de filtre et `renderNotifDrop()`. Il garde `syncReassignRequestsFromShell()`, inchangé.
- **`initViewer()`.** Le sélecteur « Viewing as » est limité à `viewAs`. Un changement de rôle ou de personne vide la sélection puis appelle `openFirstInQueue()`. **`setDemoContributorView()`** est inchangé.
- **Défauts de `state`.** `ownTeamOnly:true` → `false` (`1010d5a`) ; `navPanelCollapsed:false` → `true` ; `colCollapsed` {typo, mgr, age} → {typo, age} ; `colFilters` était déclaré mais inutilisé, il sert désormais.
- **En-têtes de colonne.** Un clic masquait la colonne (le gestionnaire « collapsed » sur `[data-col]`) ; il trie maintenant. Le masquage passe par View seulement. (`f2129b1`)
- **Onglet Requirement.** « 🔒 Frozen at review export » devient « The requirement text changes only through a new document version ». La ligne Type est supprimée. Les colonnes personnalisées sont ajoutées.
- **Onglet Activity.** Avant : une frise synthétisée à partir du statut, dont un événement « Overdue threshold reached » et « export from Allocation ». → Maintenant : le journal partagé, avec filtre et commentaire.
- **Libellés.** Expert → contributor ; « Escalate to client Q&A » → « Ask the client » ; « Activity » → « System » ; « Request reassignment » → « Not mine — return it » ; « Reassign expert » → « Reassign contributor » ; « Blocked on the issuer » → « Question to the client ».

### Retiré
- **Données et utilitaires** — `EXPERTS`, `expOf()`, `ALLOC_EXPERTS()`, `GEN_EXPERT`, `CATEGORY_LIST_PLACEHOLDER`.
- **Overdue et outdated** — `OVERDUE_DAYS`, `isOverB()`, la classe `.over` sur Age, la pastille `n-over`, `#remind-all` ; le champ `r.outdated`, `.flag-out` (« Δ outdated »), la pastille `n-out`, la mention « Answered on outdated version ». (DEC-078)
- **« Needs my action » et les sélecteurs de barre** — `needsMyAction()`, `#f10-needsme`, `actionScore()`, `#f10-sort`, `#f10-expert`, `#f10-typo` ; le champ lu `unblockedAt`.
- **Navigation « By expert »** — `.nav-toggle`, `state.navBy`, les cartes `.exp-card`, `remindExpert()` (la bascule a disparu le 24 sept., le code le 9 oct., `14e3059`).
- **Registre Q&A résiduel** — `qaGroups()`, `questionsToSend()`, `questionsSent()`, `branchRefsOfQ()`, `branchesOfQ()`, `branchOfQ()` ; dans les questions, les champs `branch`, `extraBranches`, `dup` et `expert`, et le statut `internal`. (`b3a195d`, `14e3059`)
- **Ancien formulaire de verdict** — `#a-verdict`, `#v-submit-compliant`, `#v-submit-notcompliant`, `state.verdictPick`, et le bouton de relance que le contributeur voyait sur sa propre affectation.
- **`.blocking-chip`** (« ⛔ Reassignment needed »). Attention : COMPONENTS.md liste encore un composant « Blocking Chip » pour `compliance.html`. Les indications `.kbd-hint` de la barre d'état ont aussi disparu.
- **Onglet Document** du panneau.

### Modèle de données et état (champs, statuts, clés partagées entre écrans, API du shell utilisée)
- **Exigence** (`REQS`). Avant : `{id, sec, type, text, outdated?, branches}`. → Maintenant : `{id, sec, type (plus affiché), text, textFr?, textOriginal?, branches}`.
- **Affectation** (`branch`). Avant : `{typology, manager, expert, status, compliance, age, resp:{note,att,date}, lastFollowup?, reassignComment?, reassignRequest?, qaRef?, qaNote?, reassignedAt?}`. → Maintenant :
  - `{typology, manager, status, internal, age, resp:{note,att,date,byPM?}, lastFollowup?, reassignComment?, reassignRequest?, qaRef?, qaRefs?[], qaNote?, reassignedAt?, teams?[], reopenedBy?}` ;
  - une équipe a la forme `{manager, status, internal, resp, age}`.
- **Statuts** (`BST`) — inchangés : `proposed` / `assigned` / `awaiting_answer` / `awaiting_qa` / `reassignment_needed` / `answered`. `assigned` n'est produit nulle part. **Verdicts** (`CMP`) : `compliant` / `not_compliant`. **Externe** (`EXT_LABEL`) : `compliant` / `not_compliant` / `pending`.
- **Note d'un Not compliant** — sur Turnkey, `resp.note` vaut `"<Category> — <Topic>. <commentaire>"`. Ailleurs, c'est le commentaire seul, éventuellement vide. Confirmer un Compliant remet la stratégie et les risques à vide (`setGap(...,{strategy:null,risks:[]})`).
- **Question** (registre local `QA`) — `{id, st: draft|sent|answered, q, reqs[], from, date, ans?, ansDate?, sentDate?, suggest?}`. Avant : `st` ∈ draft|internal|sent|answered, plus `branch`, `extraBranches`, `expert` et `dup`.
- **Clés partagées avec les autres écrans** :
  - documentation d'écart : `"<reqId>#<typology>"` → `{strategy, risks[], override:{ext,reason,by,date}|null, meta:{reqId,typology,sec,text,manager,managerName}}` ;
  - personnel : `"<VIEWER>:<reqId>:<typology>"` ;
  - largeurs : `getTableLayout(pid,"compliance").widths` ;
  - focus : `"compliance"` → `{risk}` ou `{select}`, `"risks"` → `{risk}` ;
  - référence de question : `refs:[{req,typology}]`, avec `origin:"compliance"` ;
  - demande de réaffectation : `byRole:"expert"` (valeur de fil inchangée, que lit la file d'Allocation), `requestStatus` `pending` → `approved` (réaffectation dans Compliance) ou **`withdrawn`** (nouveau, sur annulation d'un renvoi).
- **API du shell utilisée.** Avant : `getCurrentUser`, `getCurrentProject` (langue), `getTheme`, `route`, `pushReassignRequest`, `getReassignRequests`, `updateReassignRequest`. → Maintenant, en plus :
  - stratégies, risques et écart : `getStrategies`, `getRisks`, `addRisk`, `getGapDocs`, `getGapDoc`, `setGapDoc`, `reportStrategyUsage`, `reportGapStats` ;
  - journal : `logReqEvent`, `getReqLog` ;
  - navigation entre écrans : `setScreenFocus`, `takeScreenFocus` ;
  - questions : `pushQuestion`, `getQuestions`, `getQaRegister`, `withdrawQuestion` ;
  - partenaires : `getPartners`, `reportPartnerUsage` ;
  - colonnes et disposition : `getCustomFields`, `getTableLayout` ;
  - versions : `reportDocReqIndex`, `getVersionChanges` ;
  - et l'objet global `window.parent.__cmpPersonal`, qui ne fait pas partie de l'API.
- **`state`** :
  - nouveaux champs : `riskQ`, `newRisk`, `extFixPick`, `riskFocus`, `sortCol`, `sortDir`, `wrapText`, `advFilter`, `advFilterDraft`, `advFilterOpen`, `expandedBranches` ;
  - champs dynamiques : `panelWide`, `resTab`, `showOriginal`, `logCat`, `partnerPick`, `_gapKey` ;
  - `openForm` ∈ {ask, reassign, extfix, partner} ;
  - supprimés : `navBy`, `selQ`, `uploaded`, `verdictPick`, `sortBy`, `fExpert`, `fTypo`, `needsMe`.

### Fonctions / points d'entrée clés (nouveaux, renommés, supprimés)
- **Points d'entrée inchangés, appelés par le shell** : `setScreen(n)` (route `compliance`) et `window.setDemoContributorView()` (route `compliance-contributor`). L'initialisation enchaîne désormais `pullQaRegister()` → `applyVersionChanges()` → `setScreen(2)` → `applyFPanels()` → lecture du focus Risks.
- **Nouveaux, centraux** :
  - `renderDecisionPanel`, `isDeciding`, `myQueue`, `toggleAside` ;
  - `gapEditorHTML` / `bindGapEditor`, `externalFieldHTML` / `bindExternalField`, `branchExternal`, `externalOf`, `gapMissing` ;
  - `nextStepFor`, `remindBlock`, `sendReminder` ;
  - `pullQaRegister`, `applyVersionChanges`, `logCmpDiffs`, `activityForReq` ;
  - `needsMyTurn`, `nextNeedingAction`, `openFirstInQueue` ;
  - `notifItems`, `undoLast`, `openExport`, `syncCustomColumns`.
- **Renommés ou scindés** : `consolidatedStatusHTML` → `consolidatedProgressHTML` + `consolidatedComplianceHTML` ; `branchStatusHTML` → `branchProgressHTML` + `branchComplianceHTML` ; `escalate(r,br)` → `escalate(r,br,question)`.
- **Supprimés** : `expOf`, `ALLOC_EXPERTS`, `isOverB`, `needsMyAction`, `actionScore`, `remindExpert`, `qaGroups`, `questionsToSend`, `questionsSent`, `branchRefsOfQ`, `branchesOfQ`, `branchOfQ`.

### Prototype seulement (à ne pas reproduire)
- (P) **Données de démonstration** :
  - STB-2026 : `REQS_HAND` (14) + `genFollowupReqs(90)`, soit 104 exigences aux textes générés par gabarit ; RFP-2026-114 : `SIG_REQS` (12) ;
  - les originaux français `ORIGINAL_FR` / `GEN_*_FR`, `REX_BASE`, `PUBLISHED_QA`, les questions `QA` ;
  - les équipes de SRM-00011, écrites à la main ;
  - les lignes du partenaire de démo, injectées sur SRM-00006 et SRM-00008.
- (P) **Aucune persistance de l'état de l'écran.** Chaque route recharge l'iframe et le seed. Un verdict, une réaffectation ou une relance (`lastFollowup`) sont perdus en quittant l'écran. Seul survit ce qui est rangé dans le shell : documentation d'écart, risques, questions, journal, colonnes personnalisées, brouillons et mises de côté, versions, et les renvois encore `pending` (réappliqués par `syncReassignRequestsFromShell()`). (déduit du code)
- (P) **Aucun lien Allocation → Compliance** — les deux écrans tiennent des copies indépendantes. Valider une allocation ne crée ni ne met à jour les affectations de Compliance. « Assigned to » vient du seed de Compliance, pas des entrées OBS d'Allocation (DEC-123 ne concerne que la table d'Allocation). (déduit du code)
- (P) **Contrôle « Viewing as »** (rôle + personne) et `setDemoContributorView()`. Repasser en PM réactive « My team only » (`ownTeamOnly=true`). L'auteur des entrées de journal est la personne simulée (`currentPersonName()`).
- (P) **`CMP_PERSONAL` est un objet global sur la fenêtre du shell.** `resetDemo()` ne le vide pas. La cible est un stockage serveur privé (DEC-090).
- (P) **Substituts** : la similarité par mots communs (`similarReqs()`), le Chat en bouchon, le REX en exemples ; l'export et la relance se limitent à des toasts (le résumé d'export compte les NC **internes**).
- (P) **Q pressé par le PM** crée une question générique (« [Draft] Clarification needed on … »), et le panneau PM n'a plus de bouton actif pour questionner le client.
- (P) **`applyVersionChanges()`** rejoue à chaque chargement les versions enregistrées par Documents. Le choix des exigences « modifiées » est simulé par le shell (`recordVersionChange()` prend d'abord celles qui ont des réponses, dans l'ordre du document).
- (P) **Trous connus** (déduit du code) :
  - le formulaire de réaffectation n'a **pas de garde de rôle** : un contributeur qui ouvre un renvoi de son système le voit ;
  - Compliance ne réaffecte qu'à une personne du même système : un renvoi « Wrong system » ne se résout que dans Allocation ;
  - un contributeur peut répondre à une affectation `proposed` ;
  - les compteurs de la barre d'état portent sur tout le tender, même pour un contributeur ;
  - la documentation d'écart n'est pas purgée à la réouverture d'un verdict, et une correction PM (`override`) n'est pas effacée quand le verdict redevient Compliant ;
  - `ensureFTeams()` copie la branche dans `teams[0]` une seule fois, et le verdict système n'est jamais dérivé des équipes.
- (P) **Annulation** gardée en mémoire (pile de 30), propre à l'écran.

### Visuel
- **En-tête** : logo de la marque en PNG intégré, puis « SRM » en texte et favicon (`575fbbe`) ; icônes Risks et cloche ajoutées au groupe. Police de la marque (DEC-115, repli Noto Sans), Antarctica prévue pour les titres, accent marine, marque rouge devant le titre (`--brand-red`, placeholder) (`dd816be`, `e82c293`). L'essai d'une barre marine (`a79114e`) a été annulé (`4341e56`).
- **Icônes** : un jeu SVG en trait (`<i class=ic-*>`) remplace les emoji (`49ae3a3`).
- **Pastilles d'avancement** : plus de point initial (`73efa97`). Couleurs : « Answered » violet, « Reassignment needed » ambre, « Awaiting Q&A » bleu. Le vert et le rouge sont réservés à la pastille de verdict ✓ / ✕ (`10821d4`).
- **Barre d'état** : titre dans la barre, anneau de consolidation (`6b8d477`) ; recherche de 220 px avec icône (`0e1af9e`) ; Filter / ＋ Column / View côte à côte (`0ae2983`) ; aide ⌨ au survol (`5ba326f`).
- **Table** : lignes de titre de document et de section (`.rgrid-doctitle`, `.rgrid-sec`) ; cellules « Strategy missing » / « Risk missing » en pointillé rouge ; puces RSK ; « ✎ » sur un externe corrigé ; cellule ID violette pour une mise de côté ; barre d'onglets du détail défilant horizontalement.
- **Panneau de décision** : texte sur un fond « papier » teinté, choix vert / rouge, boutons secondaires au style des boutons de réassignation d'Allocation, bouton Confirm collant en bas (`1129260`), largeur élargissable.
- **Partenaires** : couleur sarcelle `--partner` / `--partner-soft`, hors de l'échelle de tokens.
- **Journal** : dessiné comme une ligne ferroviaire (gares = jalons) (`41de42d`).
- **Vue Document** : une feuille par document, bloc NC rouge.

### Synthèse
- **Le modèle** : `branch.manager` est la seule personne, `branch.internal` le verdict, `teams[]` le niveau 2 (affichage seulement). La documentation d'écart vit **dans le shell**, sous la clé `"<reqId>#<typology>"`, et l'externe est calculé (`branchExternal()` / `externalOf()`).
- **Deux panneaux** : le panneau de décision pour le contributeur qui doit répondre ; pour les autres cas, un panneau par état avec une phrase d'attente (`nextStepFor()`). La relance, la question et le renvoi ont chacun un seul chemin.
- **La table** est désormais au niveau d'Allocation : ordre du document, tri par en-têtes, filtres de colonne et avancé, colonnes personnalisées partagées, redimensionnement, raccourcis, annulation.
- **Le shell devient le point d'échange** avec Q&A (questions), Documents (versions), Risks et le tableau de bord (stratégies, risques, statistiques), et Allocation (journal, renvois).
- **Limite majeure du prototype** : l'état propre de l'écran (verdicts, réaffectations) ne survit pas à la navigation, et rien ne relie la validation d'Allocation aux affectations de Compliance.

## Page Risks — `risks.html`
Volume : +296 / −0 lignes (nouveau fichier) ; 9 commits.

### Ajouté
- **Écran de support** (8ᵉ source), route `risks`. En-tête : logo, « SRM », fil d'Ariane du tender, bouton « Compliance », icône des réglages (« gap strategies are under Compliance »), avatar. Pas de cloche. Titre « Risks » et sous-titre. (`b7161d3`, puis `93f80d9`)
- **`render()`** construit `#rk-register` :
  - outils : recherche `#rk-q` sur l'ID et les trois réponses, compteur « N of M », « Export » simulé ;
  - table `.rk-table` : ID, les trois questions de `RISK_Q` en colonnes, Requirements, Created by et date ;
  - les exigences liées (`reqsOf(id)`) sont des boutons `[data-goreq]` → `go("compliance",{select})` ; « all → » `[data-golinks]` → `go("compliance",{risk})` dès qu'il y a plus d'un lien ;
  - états vides : aucun risque (avec renvoi vers Compliance) ou aucun résultat.
- **Arrivée depuis Compliance** : `takeScreenFocus("risks")` → `state.focus`, ligne `.focus`, puis `scrollIntoView`.

### Modifié (avant → maintenant)
- La page n'existait pas au 8 sept. Son évolution du 30 sept. : un registre avec matrice poids × stratégie, filtres statut / poids / système, panneau de détail, fermeture / réouverture, commentaires, fusion et cloche (`b7161d3`), est devenu la liste des risques et de leur justification (`93f80d9`, DEC-113), sans système (`f9b9145`, DEC-114).

### Retiré
- Rien par rapport à la base. Les fonctions intermédiaires du 30 sept. (matrice, détail, fusion, statut, poids, filtre système) ont toutes été retirées.

### Modèle de données et état (champs, statuts, clés partagées entre écrans, API du shell utilisée)
- **Lecture seule.** Risque `{id:"RSK-00001", that, cause, impact, createdBy, createdAt}`. Les liens sont dérivés de `getGapDocs()` (`meta.reqId` des documentations dont `risks` contient l'ID). État local : `{q, focus}`.
- **API du shell utilisée** : `getCurrentUser`, `getCurrentProject`, `getTheme`, `route`, `getRisks`, `getGapDocs`, `setScreenFocus`, `takeScreenFocus`.

### Fonctions / points d'entrée clés (nouveaux, renommés, supprimés)
- `shell(name,...args)` (le même enrobage que dans Compliance), `go(route,focus)`, `risks()`, `reqsOf(id)`, `visible()`, `render()`, `toast()`.

### Prototype seulement (à ne pas reproduire)
- (P) L'export est un toast.
- (P) Les liens viennent de la documentation d'écart brute : une exigence dont le verdict a été rouvert par une version reste comptée comme liée. (déduit du code)
- (P) Risques de démo semés par le shell (`seedRisks()`).

### Visuel
- Une table propre à l'écran, pas le moteur `table-engine.js`. Elle dépend des custom properties `--line-2` et `--panel-2`, hors échelle. Logo et police comme les autres écrans.

### Synthèse
- Une liste en lecture des risques du tender : trois réponses, liens vers Compliance, créateur. Tout se crée et se lie dans Compliance ; la page lit le shell.

## Contrats du shell utilisés par Compliance et Risks — `build_merge.py`
Volume : +491 / −75 lignes (tout le shell, 363 → 779 lignes) ; 30 commits. Seules les parties dont dépendent Compliance et Risks sont décrites ici ; le reste du shell est décrit dans la partie Socle.

### Ajouté
- **Route** : `("risks","risks.html")` dans `SOURCES`, `ROUTES.risks`, `URLMAP['risks.html']`.
- **Stratégies d'écart** :
  - `getStrategies(pid)` ;
  - `addStrategy(pid,name,ext)` : refuse un nom vide ou en double ; id `gs_N` ; `ext` vaut `pending` par défaut ;
  - `renameStrategy(pid,id,name)` ;
  - `setStrategyResult(pid,id,ext)` ;
  - `removeStrategy(pid,id)` : refus `{error:"used"}` si la stratégie est utilisée ;
  - `reportStrategyUsage(pid,counts)` / `getStrategyUsage(pid,id)` → `{used, corrected}`.
- **Risques** — `getRisks(pid)` ; `addRisk(pid,{that,cause,impact,createdBy})`, qui exige les trois champs, numérote `RSK-#####` séquentiellement par tender et n'attache aucun système.
- **Documentation d'écart** — `getGapDocs(pid)`, `getGapDoc(pid,key)`, `setGapDoc(pid,key,patch)` (fusion d'un patch dans `{strategy, risks, override}`).
- **Statistiques** — `reportGapStats(pid,st)` / `getGapStats(pid)`, avec `st = {reqs, assignments, assigned, answered, compliant, nc, ncLogged, byStrategy, noStrategy, ext:{compliant,not_compliant,pending,none}}`.
- **Journal** — `logReqEvent(pid,reqId,ev)` (ajoute `ts`, `time`, `live`), `getReqLog(pid,reqId)` (trié du plus récent au plus ancien), `getActivityLog(pid)`. Format d'un événement : `{ts, time, who, cat:"status"|"alloc"|"compliance"|"comment", what, from?, to?, k, milestone?}`.
- **Passage de relais entre écrans** — `setScreenFocus(screen,payload)` / `takeScreenFocus(screen)` (lecture unique).
- **Questions au client** :
  - `pushQuestion(pid,q)` (id `QA-` + 50 + n), `getQuestions(pid)`, `withdrawQuestion(pid,id)` ;
  - `getQaRegister(pid)` : `flags[id] = {st, sentDate, ans, ansDate, suggest}` et `others[]`, écrits par `qa.html`.
- **Versions (LIFE-007)** :
  - `reportDocReqIndex(pid,idx)` : les premières exigences de chaque document, avec leur nombre de réponses ;
  - `recordVersionChange(pid,{doc,docName,num,m,gap,note})` : choisit les `m` exigences modifiées, celles qui ont des réponses d'abord, en sautant celles qu'une version précédente a déjà modifiées, puis renvoie `{modified[], reopened, logged}` ;
  - `getVersionChanges(pid)`.
- **Partenaires** — `getPartners`, `addPartner`, `removePartner` (refusé si utilisé), `reportPartnerUsage(pid,screen,counts)`, `getPartnerUsage`.
- **Colonnes et disposition** — `getCustomFields(pid)`, `getTableLayout(pid,table)`.
- **`resetDemo()`** remet à zéro tout ce qui précède (sauf `__cmpPersonal`).

### Modifié (avant → maintenant)
- **`setV22Uploaded`** n'est plus déclenché par Compliance : son ancien bouton « Simulate upload — v2.2 » a disparu avant la base. C'est Documents qui le déclenche (`b3a195d`). Le tableau de bord raconte désormais la dernière version enregistrée, lue dans `getVersionChanges()` (DEC-122).
- **Boîte des réaffectations** (`pushReassignRequest`, `getReassignRequests`, `updateReassignRequest`) : l'API ne change pas, mais Compliance écrit maintenant `requestStatus:"withdrawn"` quand un renvoi est annulé. Le tableau de bord ignore ces demandes retirées.

### Retiré
- Rien de ce que Compliance et Risks utilisaient.

### Modèle de données et état (champs, statuts, clés partagées entre écrans, API du shell utilisée)
- Tout est en mémoire de la fenêtre du shell, **par tender** (clé `projectId`) : `strategies`, `strategyUsage`, `risks`, `gapDocs`, `gapStats`, `reqLog`, `sharedQuestions`, `qaRegister`, `docReqIndex`, `versionChanges`, `partners`, `partnerUsage`, `customFields`, `tableLayouts`.
- **Producteurs et consommateurs** :
  - Settings (`dashboard-et-config.html`) : `renderStrategiesSetting()` dans la section `data-sec="compliance"` (renommer, changer le résultat avec confirmation « N requirements will change … · K corrected by the PM keep their value », supprimer si inutilisée, ajouter), et `renderPartnersSetting()` dans « Allocation model » ;
  - tableau de bord : `renderStatsProgressClient()`, `renderStatsNCStrategy()`, `renderStatsRisks()`, `renderNarrativeCards()`, carte Risks ;
  - Documents : `uploadVersion` → `recordVersionChange`, `replayVersionChanges()` ;
  - Q&A : `getQuestions`, `getQaRegister`.

### Fonctions / points d'entrée clés (nouveaux, renommés, supprimés)
- Voir « Ajouté ». Aucune fonction du shell utilisée par Compliance au 8 sept. n'a été renommée ni supprimée.

### Prototype seulement (à ne pas reproduire)
- (P) **Seeds** :
  - `seedStrategies()` : les quatre stratégies, sur cinq tenders de démo ;
  - `seedRisks()` : six risques sur STB-2026, un sur RFP-2026-114 ;
  - `seedGapDocs()` : la documentation de SRM-00005, -00007, -00011, -00026, -00038, -00056, -00068 (corrigée par le PM), -00086, et de L4-0010 ;
  - `seedStrategyUsage()`, `seedGapStats()`, `seedPartnerUsage()`, `seedDocReqIndex()` : ce sont les valeurs que Compliance calculerait, semées pour que Settings et le tableau de bord aient des chiffres avant toute ouverture de Compliance ;
  - `seedReqLog()` : historiques crédibles sur quelques exigences ;
  - `seedPartners()` : le partenaire de démo.
- (P) **Choix simulé des exigences « modifiées »** par une version (`recordVersionChange`).
- (P) **Identifiants** `QA-5N` et `RSK-#####` attribués en mémoire.
- (P) **Aucune persistance** au-delà de la session ; `resetDemo()` (Ctrl+Maj+R) remet tout à zéro.

### Visuel
- Sans objet pour ces contrats ; la police de marque est injectée par `withBrandFonts()`, traitée ailleurs.

### Synthèse
- Le shell porte désormais les **données partagées du domaine** : stratégies, risques, documentation d'écart, questions, versions, journal, statistiques et partenaires. En production, ces contrats deviennent des ressources serveur par tender. Il ne faut pas en reproduire les seeds, ni la répartition « chaque écran garde sa copie ».

# Partie 5 — Documents et versions, Q&A, capture

Périmètre : `5e7ae6b` (8 sept. 2026) → `main` (`b675936`). Les écrans sont des iframes rechargées à chaque route ; tout ce qui doit survivre à une navigation vit dans le shell (`build_merge.py`, objet `window` du parent), **en mémoire seulement** (perdu au rechargement de la page, remis à zéro par `resetDemo()` / Ctrl+Maj+R). Les parties d'Allocation, Compliance et Configuration citées ici ne couvrent que ce périmètre ; le reste de ces fichiers est décrit dans les autres parties.

## Documents & versions — `documents.html`
Volume : +211 / −66 lignes depuis 5e7ae6b ; 12 commits.

### Ajouté
- **Enregistrement d'une version dans le shell** : `uploadVersion()` appelle `parent.recordVersionChange(PID, {doc, docName, num, m: gap.m, gap, note})` et affiche le `.reopened` retourné ; l'IIFE `replayVersionChanges()` (fin de script) rejoue au chargement les versions déjà téléversées sur ce tender (`getVersionChanges(PID)`), avec le nombre rouvert que Compliance a réécrit entre-temps. (`8c748a3`, DEC-122)
- **Drapeau v2.2** : téléverser une nouvelle version de `d1` appelle `parent.setV22Uploaded(true)`. (`b3a195d`) — voir Prototype seulement.
- **Cloche de notifications** calculée depuis `DOCS` : `notifItems()` (réponses rouvertes par la version courante d'un document ; documents sans exigence = non traités), `renderNotifDrop()`, `wireBell()` (rendu à l'ouverture, sous try/catch). (`b3a195d`)
- **Fil d'Ariane** = tender courant (`getCurrentProject()` : « ref · nom ») au lieu de « STB-2026 » en dur. (`14e3059`)
- **CSS de la zone de toasts** (`#toast-zone`, `.toast`) : au 8 sept. la zone existait sans style, les toasts de l'écran ne s'affichaient jamais. (`14e3059`)
- Constantes `PID` (id du tender courant, `"_"` hors shell) et `docShort(d)`.

### Modifié (avant → maintenant)
- **Valeur `stale` d'une nouvelle version** : `stale = gap.m` (nombre d'exigences modifiées, présenté comme « verdicts made stale ») → `stale = recordVersionChange(...).reopened` = nombre d'**affectations répondues** que Compliance rouvre ; 0 si l'écran tourne hors shell. Le champ garde son nom `stale`. (`8c748a3`)
- **Libellés** « stale verdicts » → « answers reopened » partout : tuile « Answers reopened by a new version », option de filtre « Has reopened answers » (valeur `stale` inchangée), ligne « ⚠ N answers reopened », note de version (« … so their verdicts went back to pending. See Allocation › Document view › Changes. » + lien « Open Compliance → »), toast d'upload. (`14e3059`)
- **Seed** : `d29` « Q&A response dossier — round 1 » devient « Addendum n°3 — technical clarifications » (`EMS_add_3.pdf`) ; le dossier de réponses du client n'est plus présenté comme un document du tender (déduit : il passe par l'import du Q&A). (`14e3059`)
- « activity » → « system » dans la modale d'export (« Characterisation — class, system, type and status ») et dans les libellés de progression. (`7d737b8`, DEC-045)
- Inchangé : ordre (↑/↓), ajout d'un document avec progression capture → traduction (si langue ≠ en) → caractérisation, suppression avec énoncé des pertes, filtres, recherche, export par document (Excel / CSV / ReqIF / DOORS 9).

### Retiré
- `PSTATE_FULL` (inutilisé), CSS mort `.mode-switch*`, `.triage`, `main{…}` ; logo SVG inline. (`14e3059`, `575fbbe`)

### Modèle de données et état (champs, statuts, clés partagées entre écrans, API du shell utilisée)
- `DOCS[]` : `{id:"d1"…"d30" | "d-new<n>", name, file, rows, state:"ready"|"running"|"queued", prog?, progLabel?, added, versions:[{num:"vX.Y", date, note, gap:{a,m,r}|null, stale}]}` — versions **de la plus récente à la plus ancienne** ; `PSTATE` = Ready / Processing / Not processed ; `state = {expanded:Set, removeId, addSeq, search, filter}`.
- **Clés partagées dans le shell** : `versionChanges[pid]` (écrit par `recordVersionChange`, lu par Documents, Compliance et le dashboard) ; `v22Uploaded`.
- **Rapprochement par identifiant** : `d1` / `d2` de Documents = `d1` / `d2` de Compliance et d'Allocation ; le shell choisit les exigences touchées dans `docReqIndex[pid][docId]`.
- API du shell utilisée : `getCurrentUser`, `getCurrentProject` (crumb, `PID`, `language`), `getTheme`, `recordVersionChange`, `getVersionChanges`, `setV22Uploaded`, `route`.
- Aucune notion de rôle : réordonner, téléverser, supprimer et exporter sont ouverts à tout lecteur (spec : équipe projet).

### Fonctions / points d'entrée clés (nouveaux, renommés, supprimés)
- Nouveaux : `notifItems`, `renderNotifDrop`, `wireBell`, `replayVersionChanges`, `docShort`.
- Modifié : `uploadVersion`.
- Inchangés : `renderSummary`, `versionsHTML`, `docRowHTML`, `visibleDocs`, `renderDocs`, `bindDocs`, `move`, `askRemove`, `doRemove`, `addDocument`, `fillExportDocs`, `toast`, `esc`.

### Prototype seulement (à ne pas reproduire)
- Seed de 30 documents `EMS_*` (STB-2026) affiché **sur tous les tenders**, RFP-2026-114 compris ; échelles de versions générées par index.
- Écart simulé : `gap = {a:1+(n%3), m:2+(n%2), r:n%2}` (n = nombre de versions), numéro = mineur +1, date « Today », aucun fichier lu.
- Choix des exigences « modifiées » par le shell : les `m` premières de `docReqIndex` (12 au plus par document, celles qui ont une réponse d'abord, en sautant celles qu'une version précédente a déjà touchées) ; seuls `d1`/`d2` de STB-2026 et `d1` de RFP-2026-114 ont des exigences → une version de tout autre document rouvre 0 réponse.
- Le « 2 answers reopened » de `d1` v2.1 est écrit à la main, sans contrepartie dans Compliance.
- `setV22Uploaded` : drapeau vestigial — écrit ici, plus lu nulle part depuis que le dashboard lit `getVersionChanges` (`8c748a3`) ; le commentaire de `uploadVersion` qui dit le contraire est périmé.
- Ajout de document : nom et fichier inventés (« Addendum N — new scope »), progression minutée, puis `rows = 40 + (N×17 mod 60)` ; suppression en mémoire ; export = toast.
- **Une version téléversée ici n'apparaît pas dans Allocation** (ni colonne/onglet Changes, ni retour To review, ni relance) : Allocation a son propre `DOCS` et des historiques seedés.

### Visuel
- Police de marque Alstom (`--font-ui`), titres en `--font-heading`, marque rouge décorative devant h1/h2 (`--brand-red`, jamais sur un élément cliquable ou porteur d'état), accent marine `#0B294A` en thème clair, palette sombre recalée. (DEC-063/115)
- Logo de la marque puis « SRM » en texte, favicon SRM (`575fbbe`) ; icônes SVG en masque CSS (`i.ic-*`) au lieu d'emoji (`49ae3a3`) ; pastilles d'état sans point (`73efa97`).

### Synthèse
- L'upload d'une version passe désormais par le shell (`recordVersionChange`) et son compte « answers reopened » est celui que Compliance rouvre réellement.
- Le libellé « stale verdicts » a disparu, le champ `stale` est resté.
- Toujours un écran 100 % simulé, mono-seed STB-2026, sans rôles, et déconnecté de l'historique de versions d'Allocation.

## Q&A — `qa.html`
Volume : +432 / −498 lignes depuis 5e7ae6b ; 16 commits.

### Ajouté
- **Barre unique** (`.qa-bar`) : bascule de vue « Our questions N » / « Other bidders N » (« — » avant import), recherche, filtre système (vue « ours » seulement), « Export to Excel » (vue « ours »), « Import the client's answers ». (`47de775`, DEC-116)
- **Filtre de statut** (`.qa-st-filter`) : All / To send / Sent / Answer to confirm (seulement s'il en existe) / Answered, chacun avec son compte ; tri par statut (à confirmer, à envoyer, envoyé, répondu).
- **Marquage manuel** : case à cocher sur chaque question To send, « Select the N to send », barre « N selected · Mark as sent · Clear », bouton « Mark as sent » par carte, « Not sent » pour revenir en arrière (sur une Sent sans suggestion) ; `sentDate = "Today"`.
- **Carte de question** (`cardHTML`) : pastille de statut (To send / Sent · date / Answered · date / Answer to confirm), métadonnées (exigence, système, auteur, date, « · from Compliance »), réponse du client sous la question.
- **Réponse à confirmer** (`.qa-suggest`) : « Probably the client's answer — N% sure… », boutons « ✓ It's the answer » (→ Answered) / « Not this one » (→ reste Sent).
- **Vue Other bidders** (`othersHTML`) : cartes en lecture (question, réponse du client, exigence ou « No requirement linked »), compteur, recherche sur question/réponse/exigence ; état vide avec bouton d'import.
- **Persistance dans le shell** : `REG = parent.getQaRegister(PID)` (`flags` par question, `others`), `saveFlag(q)` qui recopie aussi `st`/`ans` sur la question partagée.
- **Questions venues de Compliance** : `pullSharedQuestions()` ajoute en tête les questions de `parent.getQuestions(PID)` (`origin:"compliance"`), puis réapplique `REG.flags`. (`d6efd7f`, DEC-088 ; `47de775`)
- **Cloche** : `notifItems()` (à confirmer / à envoyer / envoyées sans réponse, chacune ouvrant le filtre correspondant). (`b3a195d`)
- **Ligne des dates** (`datesHTML`, `.qa-dates`) ; fil d'Ariane = tender courant ; CSS des toasts (invisibles au 8 sept.). (`14e3059`)

### Modifié (avant → maintenant)
- **Statuts** : `draft | sent | answered | excluded` → `draft | sent | answered` + statut dérivé `confirm` (`stOf(q)` : `sent` avec `suggest`). Libellés : Drafts / Sent to the issuer / Answered / Excluded from export → To send / Sent / Answered / Answer to confirm.
- **Export** : « ⬇ Export batch for issuer » faisait passer **tous** les brouillons en `sent` (date Today) → « Export to Excel » = toast sur les questions à envoyer, ne marque rien.
- **Import** (`runImport`) : extraction simulée d'un dossier de 50 paires (nos questions + concurrents), rapprochement auto ou mis en file d'arbitrage → passe directement chaque question `sent` en `answered` (textes `ANSWERS_OURS` ou texte générique), sauf la première au **premier** import qui reçoit `suggest:{text, conf:63}` ; remplit `REG.others` (15 Q&A, ~25 % sans exigence, répartition déterministe) ; toast récapitulatif.
- **Systèmes** : 5 valeurs inventées (SIG & Urban, Mainline Wayside…) → les 16 codes de la capture, libellé = code ; « All activities » → « All systems » ; typologies de QA-01/QA-02 passées de `mln` à `trk`. (`2a7aa6b`, `7d737b8`)
- **Dates** : cut-off Aug 22 « passed », réponses Aug 24 « overdue » (deux bannières, une par onglet, avec le nombre de branches bloquées) → une ligne, cut-off Jul 17 « passed », réponses Jul 24 non en retard. (`d109c66`, DEC-117 ; `47de775`)
- **Recherche** : texte ou exigence → texte, ID de question ou exigence (ours) ; question, réponse ou exigence (others).
- `refsLabel` tolère une typologie vide ; vocabulaire « issuer » → « client », « competitor » → « other bidders ».

### Retiré
- Onglets `.hub-tabs` Questions / Answers (+ badge `#answers-count`), carte d'export du lot, alerte de doublon + « Merge into » (et les champs `dup` du seed), Exclude / « Include again » (+ groupe Excluded, `prevSt`, note d'exclusion), groupes par statut, bannières de délai par onglet, boîte d'import (modes fichier / collage, textarea « Extract Q&A pairs »), tuiles de progression, file d'arbitrage (carte, propositions avec %, touches 1–9 / N / S, Skip, « No matching requirement »), liste « Resolved & context ». (`47de775`)
- Fonctions supprimées : `renderQuestions`, `renderAnswers`, `renderAll`, `renderDeadlineBanner`, `questionsToSend`, `questionsSent`, `syntheticAnswer`, `buildDossier`, `queuedItems`, `decideArb`, `skipArb`, `renderArbitration`, `renderResolvedList`, `renderImportBox`, `bindImportBox`, gestionnaire `keydown` ; constantes `COMPETITOR_Q`, `DOSSIER` ; CSS `.arb-*`, `.export-*`, `.dup-alert`, `.ctx-row`, `.qa-deadline`, `.qa-progress`/`.qa-pstat`, `.qa-group`, `.sec-head` ; `.mode-switch` mort ; logo SVG.

### Modèle de données et état (champs, statuts, clés partagées entre écrans, API du shell utilisée)
- Question : `{id, st:"draft"|"sent"|"answered", q, refs:[{req, typology}], from, date, sentDate?, ans?, ansDate?, suggest?:{text, conf}, origin?:"compliance"}`.
- Q&A d'un autre soumissionnaire : `REG.others[] = {id:"OB-n", q, a, req|null}`.
- `state = {view:"ours"|"others", status:"all"|"draft"|"sent"|"confirm"|"answered", qSearch, qActivity, sel:Set, importing, visibleDrafts}` (avant : `{htab, qSearch, qActivity, imported, arbTotal}`).
- **Clés partagées (shell, par tender)** : `qaRegister[pid] = {flags:{[id]:{st, sentDate, ans, ansDate, suggest}}, others:[…]}` — objet muté en place par `qa.html`, lu par Compliance (`pullQaRegister`) ; `sharedQuestions[pid] = [{id:"QA-51"…, st, q, refs, from, date, origin, ans}]` — écrit par Compliance, statut/réponse recopiés par `saveFlag`.
- Identifiants : seed QA-01 à QA-05 ; questions issues de Compliance `QA-51`, `QA-52`… (attribués par `pushQuestion`) ; autres soumissionnaires `OB-1`…`OB-15`.
- API du shell utilisée : `getQaRegister`, `getQuestions`, `getCurrentProject`, `getCurrentUser`, `getTheme`, `route`.

### Fonctions / points d'entrée clés (nouveaux, renommés, supprimés)
- Nouveaux : `stOf`, `saveFlag`, `notifItems`, `renderNotifDrop`, `wireBell`, `datesHTML`, `oursHTML`, `cardHTML`, `othersHTML`, `render`, `markSent`, `bind`, `pullSharedQuestions` ; constantes `ST_ORDER`, `PID`, `REG`, `ANSWERS_OURS`, `OTHER_QA`.
- Réécrit : `runImport`. Conservés : `preserveFocus`, `toast`, `esc`, `refsLabel`, `REQ_POOL`, `TENDER_QA_DATES`.
- Supprimés : voir Retiré.

### Prototype seulement (à ne pas reproduire)
- Seed STB-2026 (QA-01 à QA-05, `SRM-…`) affiché **sur tous les tenders** ; les questions seedées du tender SIG (`QA-L1`, `QA-L2`) n'existent que dans `compliance.html` ; les dates Jul 17 / Jul 24 sont les mêmes sur tous les tenders alors que le dashboard donne au SIG Jul 10 / Jul 21.
- Import : réponses écrites à la main, certitude constante 63 %, une seule « à confirmer » au premier import, rattachements tirés d'un `REQ_POOL` fixe ; rien n'est lu.
- Export Excel = toast ; aucune vérification de rôle (n'importe qui marque « envoyée » ou importe).
- Les chiffres Q&A du dashboard (« 5 questions · 1 answered », « 2 questions to send ») sont écrits en dur, sans lecture du registre.

### Visuel
- Pastilles : To send neutre, Sent accent, Answered vert, Answer to confirm violet (`--human`, encadré pointillé) ; réponse du client sur fond vert pâle ; « No requirement linked » en italique gris ; retard en couleur `--warn` dans la ligne des dates.
- Mêmes changements de marque que Documents (police, logo, favicon, icônes SVG, accent marine).

### Synthèse
- L'écran passe de deux onglets + file d'arbitrage à une liste filtrée par statut, avec marquage manuel « Mark as sent » et confirmation d'une réponse incertaine sur la question elle-même.
- Son état (drapeaux, import) vit dans le shell par tender et il récupère les questions posées depuis Compliance.
- Tout l'aller-retour client (export, import, rapprochement) reste simulé.

## Shell, parties utilisées par Documents, Q&A et Compliance — `build_merge.py`
Volume : +491 / −75 lignes depuis 5e7ae6b ; 30 commits (le fichier entier ; seules les parties de ce périmètre sont décrites ici, le reste est décrit dans la partie Socle).

### Ajouté
- **Magasin de questions** (DEC-088, `d6efd7f`) : `sharedQuestions` par tender ; `pushQuestion(projectId, q)` attribue l'id `QA-<50 + rang + 1>` (QA-51, QA-52…) et range la question ; `getQuestions(projectId)` ; `withdrawQuestion(projectId, id)` (Undo dans Compliance).
- **Registre Q&A** (DEC-116, `47de775`) : `qaRegister` par tender ; `getQaRegister(projectId)` renvoie l'objet (créé au besoin), muté en place par `qa.html`.
- **Versions de documents** (LIFE-007, DEC-122, `8c748a3`) : `seedDocReqIndex()` / `docReqIndex` (par tender et document, liste ordonnée `{id, answered}`), `reportDocReqIndex(projectId, idx)` (Compliance le réécrit à chaque chargement), `versionChanges` + `getVersionChanges(projectId)`, `recordVersionChange(projectId, ch)` → ajoute `{…ch, modified:[ids], reopened, logged:false}` et le renvoie.
- `resetDemo()` remet aussi à zéro `sharedQuestions`, `qaRegister`, `docReqIndex`, `versionChanges`.

### Modifié (avant → maintenant)
- **Drapeau v2.2** : commentaire « déclenché par le bouton Simulate upload — v2.2 de Follow-up » (qui n'existait plus : drapeau jamais levé) → déclenché par Documents (`b3a195d`) ; depuis `8c748a3` plus aucun écran ne lit `isV22Uploaded()`.
- **Docstring data.js** : produit par `import_capture.py`, repli `buildBigData(n)` → produit par `import_capture_doors.py` (`import_capture.py` = ancien importeur .xlsx), repli `seedDemoSections()` (démo STB-2026 écrite à la main).
- **`main()`** : `data.js` reste facultatif et n'est inliné que dans l'écran qui porte le marqueur `/* @include data.js */` (Allocation) ; nouveau : copie compacte de la capture pour le chat du tender (`window.CHAT_CAPTURE`, seulement si `CHAT_ENABLED`, à `False` depuis `683763c`).
- `seedProjects()` : `rfp114` devient un tender construit (`builtOut:true`, DEC-044, `376c6a5`) avec `language:"en"` explicite et le produit Mainline Wayside (`132eef3`, DEC-061) ; `stb2026` garde `language:"fr"` ; libellé de traitement « Allocating to experts… » → « … contributors… » (`39e277b`).

### Retiré
- Rien dans ce périmètre.

### Modèle de données et état (champs, statuts, clés partagées entre écrans, API du shell utilisée)
- Toutes les clés sont indexées par id de tender (`"_"` hors tender) : `sharedQuestions[pid]`, `qaRegister[pid]`, `docReqIndex[pid][docId]`, `versionChanges[pid]`.
- Enregistrement de version : `{doc, docName, num, m, gap:{a,m,r}, note, modified:[reqIds], reopened, logged}` ; `reopened` et `logged` sont réécrits par Compliance quand il applique la version.
- Inchangés : `aiFeedback` + `pushAIFeedback(f)` / `getAIFeedback()` (entrée `{surface, id, before, after, conf, reason, at}`) ; `isV22Uploaded` / `setV22Uploaded`.

### Fonctions / points d'entrée clés (nouveaux, renommés, supprimés)
- Nouveaux (`window.*`) : `pushQuestion`, `getQuestions`, `withdrawQuestion`, `getQaRegister`, `reportDocReqIndex`, `getVersionChanges`, `recordVersionChange` ; interne : `seedDocReqIndex`.

### Prototype seulement (à ne pas reproduire)
- `seedDocReqIndex()` recopie à la main ce que Compliance calcule sur ses données de démo (12 exigences au plus par document) ; le choix des exigences « modifiées » privilégie celles qui ont des réponses, pour que la démo rouvre quelque chose.
- Aucun stockage : tout est perdu au rechargement de la page.

### Visuel
- Sans objet.

### Synthèse
- Le shell porte désormais trois canaux transverses du périmètre : questions (Compliance → Q&A), registre Q&A (Q&A → Compliance), versions (Documents → Compliance → dashboard).
- Ce sont des boîtes aux lettres en mémoire : en production, ce sont des données serveur (registre de questions, versions de documents, réouvertures).

## Importeurs de capture — `import_capture_doors.py`, `import_capture.py`
Volume : `import_capture_doors.py` +23 / −11 (2 commits) ; `import_capture.py` +4 / −3 (1 commit).

### Ajouté
- `import_capture_doors.py` : `CHAR_FIELDS = {"type", "class"}` et `_char_level(score)` (< 75 → `"low"`, < 85 → `"medium"`, sinon `"high"`) ; `seed_demo_confidence()` écrit un **niveau** pour `type` et `class`, garde l'entier 0–99 pour `abs`, `pbs`, `obs`. (`e5ee6e3`, DEC-120)
- `import_capture.py` : mention **LEGACY** en tête (remplacé par l'importeur DOORS ; ses lignes n'ont ni niveau de titre, ni systèmes, ni confiance).

### Modifié (avant → maintenant)
- Docstring de `import_capture_doors.py` : « importeur séparé, au choix » → « c'est lui qui produit le data.js actuel » ; « activity » → « system » (colonne Responsible Entity, sortie console). (`d72a2a9`)

### Retiré
- `import_capture.py` : l'avertissement « plus de 3 000 lignes : la table sera lente ».

### Modèle de données et état (champs, statuts, clés partagées entre écrans, API du shell utilisée)
- Sortie inchangée hors confiance : `data.js` = `window.SRM_DATA = {documents:[{id:"DOC-n", name, order, rowCount}], rows:[{id:"SRM-00001"…, sourceId, docId, docName, docIndex, position, index, category:"heading"|"requirement"|"information", unknownCategory, text, section, numHeading, level, perim:[codes], confidence:{generated:true, type, class?, abs?, pbs?, obs?}}], meta:{totalRows, sourceFiles, demoStateSeeded:true, demoStateNote, importer}}`.
- `confidence.type` / `confidence.class` : `"low"|"medium"|"high"` (avant : entiers) ; `abs` / `pbs` / `obs` : entiers.
- **Chargement par le prototype** : `build_merge.py` inline `data.js` (fichier ignoré par git, facultatif) au marqueur de `revue-documentaire.html` seulement ; il pose `window.SRM_DATA`. Allocation ne l'utilise que **hors tender SIG** (TYPE-T07, DEC-044 — avant : sur le seul tender construit) : `DOCS` = documents de la capture (une version `v1.0` chacun), `SECTIONS` = `buildDataFromCapture()`, puis `applyCaptureDemoStatuses()` lit les niveaux (`charLevel`) ; Compliance, Documents et Q&A ne lisent jamais la capture.

### Fonctions / points d'entrée clés (nouveaux, renommés, supprimés)
- Nouveau : `_char_level` ; modifié : `seed_demo_confidence`.

### Prototype seulement (à ne pas reproduire)
- Toute la confiance est générée (`seed_demo_confidence`, ~87 % de lignes confiantes, un seul champ faible par ligne à revoir, dérivé de l'id) ; les statuts de démo et les valeurs ABS/PBS/OBS vides sont fabriqués côté écran (`applyCaptureDemoStatuses`). Le format d'entrée (export DOORS « ViewText » en `.numbers`) est celui d'un jeu de test, pas un contrat d'import.

### Visuel
- Sans objet.

### Synthèse
- Seul changement de fond : la confiance de caractérisation (type, classe) arrive en niveaux, celle d'allocation reste en pourcentage (DEC-120).
- Le lecteur de capture ne vaut que pour la démo STB-2026 ; le tender SIG a son propre contenu.

## Transverse — langue, capture, IA et versions dans les écrans de travail — `revue-documentaire.html`, `compliance.html`, `dashboard-et-config.html`, `creation-projet.html`
Volume : non compté ici (fichiers couverts par les parties Allocation, Compliance et Pilotage) ; commits cités par point.

### Ajouté
- **Allocation, confiance de caractérisation** (DEC-120, `e5ee6e3`) : `CHAR_HIGH_FROM = 85`, `CHAR_LEVEL_LABEL`, `charLevel(v)` (lit un niveau ou convertit un nombre), `charConfOf(b, axis)`, `charConfBadgeHTML()` (badge Low/Medium/High à côté de la nature et de la classe tant que la valeur est celle de l'IA), `dropCharConf()`, `seedCharConfidence()` ; champs `b.charLevel = {type, class}` et `b.charConf = {type:{v, level}, class:{v, level}}` ; `typeAI` / `techAI` = niveau `"low"`.
- **Allocation, versions par document** (DEC-069 à 072, `82ab34e` ; DEC-119, `73c7fe7`/`8365089`) : `DOCS[].versions = [{v, date, note}]` (de la plus ancienne à la plus récente) par tender (`seedDemoDocs`, `seedSigDocs`, ou capture) ; `b.history = [{from, to, type:"added"|"modified"|"removed", prevText?, desc?}]` ; `activeVersion`, `latestChange`, `rangeChange`, `wordDiffHTML` ; `applyVersionChanges()` (exigence ajoutée/modifiée → `status:"doubt"` + `reviewReason`) ; onglet Versions `versionsTabHTML()` ; panneau d'exigence supprimée `renderRemovedPanel()` ; colonne Changes `chgBaseOf`, `chgOf`, `chgCellHTML`, `chgDiffHTML`, `openChgRowPop`, `openChgAllPop`, `toggleChgColumn` (touche C), `renderChgHead`, `state.chgAll` / `state.chgBase` ; onglet Changes `renderNavTabs`, `renderNavChanges`, `changeImpact`, `ncItems`, `NC_FILTERS`, `state.ncFilter`, `cmpDocs` / `cmpEnsure` / `cmpChangeIds` (le mode interne s'appelle toujours `state.mode === "compare"`).
- **Compliance, questions au client** : `escalate(r, br, question)` (texte écrit par la personne depuis `dd4b8fd`, DEC-080) → `parent.pushQuestion(pid, {st:"draft", q, refs:[{req, typology}], from, date:"Today", origin:"compliance"})`, id renvoyé (`QA-51`…), repli local `"QA-0" + (QA.length + 2)` hors shell (`d6efd7f`) ; `br.qaRefs[]` (plusieurs questions) + `br.qaRef`, seule une affectation `awaiting_answer` passe à `awaiting_qa` (`42676d5`, DEC-092) ; refus sur une affectation répondue (`8c748a3`, DEC-121) ; Undo → `withdrawQuestion`. `pullQaRegister()` (`8c748a3`, DEC-122) fusionne questions partagées, `REG.flags` et les `REG.others` liés à une exigence (ajoutés à `PUBLISHED_QA`) ; `qaStLabel()`. Avant : id local `QA-0N`, passage inconditionnel en `awaiting_qa` avec une note « bloquante », rien n'atteignait `qa.html`.
- **Compliance, réouverture par version** (`8c748a3`) : `applyVersionChanges()` publie d'abord `reportDocReqIndex` (12 premières exigences par document avec leur nombre de réponses), puis pour chaque `getVersionChanges` : affectations répondues des exigences modifiées → `status:"awaiting_answer"`, `internal = null`, `resp = null`, `age = 0`, `reopenedBy = "<document> <version>"`, journal écrit une fois (`ch.logged`), `ch.reopened` réécrit ; affichage « Reopened by … » dans le panneau, l'étape suivante et la cloche.
- **Compliance, langue** (DEC-081, `f6bdf9e`) : originaux `ORIGINAL_FR` → `r.textOriginal` sur un tender en français ; interrupteur `#dp-orig` (`state.showOriginal`, anglais par défaut) ; export avec choix « Original / English translation » (`xpState.orig`, **anglais par défaut**).
- **Configuration › Capture & segmentation** (`b2ac7af`) : contrôles `data-seg="convrange"` (+ champ `#convrange-pages` / `#convrange-input` affiché avec « Specific pages »), `tableformat`, `gran` (déplacé à côté du format), `sentences`, `equations` — affichage seul (avertissement TE2).
- **Configuration › Language** : « Working language: English », non modifiable (`14e3059`).
- **Dashboard** : `versionChangesHere()`, `lastVersionChange()`, `renderVersionNews()` racontent la dernière version téléversée sur ce tender (carte d'attention vers Documents, deux entrées du fil) au lieu de `v22Done()`. (`8c748a3`)

### Modifié (avant → maintenant)
- **Allocation, traduction** : option « original » en tête du sélecteur « Read in » (`langReadOptions`, `3e0e369`) — le titre du panneau reste pourtant l'anglais tant qu'on ne change pas la sélection (déduit du code) ; onglet Translation masqué quand le tender est en anglais (`8dd5f94`) ; une correction s'écrit aussi dans le journal de l'exigence (`pushTranslationLog` → `logReq(… "English text corrected")`, `7a1d771`). **Inchangé et contraire à LIFE-008/DEC-026** : enregistrer une correction (`#corr-save`) met à jour `b.text` et `b.translationCorrected` sans toucher au statut.
- **Allocation, capture** : `SECTIONS = IS_SIG_TENDER ? seedSigSections() : (buildDataFromCapture() || seedDemoSections())` et `applyCaptureDemoStatuses()` seulement si `SRM_DATA && !IS_SIG_TENDER` (avant : sans condition de tender) ; `applyCaptureDemoStatuses()` lit les niveaux de confiance au lieu de comparer des nombres au seuil. (`376c6a5`, `e5ee6e3`)
- **Allocation, retour IA** : appels à `logFeedback` réduits à `"char"` (nature, classe), `"typo"` (système proposé par l'IA) et `"deriv"` (dérivation faible validée telle quelle) ; plus de `"alloc"` (proposition de personne), plus de boîte « Why » (`askWhy`, `REASONS`, `HICONF`) (`14e3059`), plus de sélecteur de type Functional/Performance (`d8937b5`).
- **Configuration** : section « AI & segmentation » → « Capture & segmentation » (`b2ac7af`) ; carte « Activity » → « System » dans AI feedback (`7d737b8`) ; Q&A : seul « Issuer channel » reste ; Versions : seuls « Numbering » et « Detect addendum-as-answer » restent (`14e3059`).
- **Création** : la langue affichée sur chaque document du wizard = langue source choisie à l'étape 1 (`docLang()`), au lieu de « English » en dur. (`14e3059`, DEC-096)

### Retiré
- **Allocation** : mode Compare (barre Compare, sélecteur de versions du tender), pastille `.version-pill` « v2.1 active », panneau de changement `renderChangePanel` (New / Reviewed, no impact / Action required, « Create action / reminder »). (`82ab34e`, `73c7fe7`)
- **Allocation** : carte de proposition IA d'une personne et boîte « Why » ; bouton « ✓ Confirm AI activity » (`f85841f`, `14e3059`).
- **Configuration** : « Default translation target », « AI duplicate detection », « Internal review before sending », réglage de notification au changement de version. (`14e3059`)
- **Compliance** : registre Q&A résiduel (groupes Draft / Internal review / Exported / Answered) (`b3a195d`).

### Modèle de données et état (champs, statuts, clés partagées entre écrans, API du shell utilisée)
- Traduction : `project.language` ; bloc `{text (anglais, texte de travail), textOriginal (immuable), translationCorrected, translationLog:[{who, before, after, time}]}` ; Compliance : `r.textOriginal`.
- Questions côté Compliance : `QA[] = {id, st, q, reqs:[…], from, date, sentDate?, ans?, ansDate?, suggest?}` ; branche `{status:"awaiting_qa", qaRef, qaRefs:[…], qaNote, reopenedBy?}`.
- Versions : Allocation (`DOCS[].versions[].v`, `b.history`, `b.change`) et Documents (`DOCS[].versions[].num`, `stale`) sont **deux magasins distincts** ; seul Compliance consomme `versionChanges`.
- API du shell : `pushQuestion`, `withdrawQuestion`, `getQuestions`, `getQaRegister`, `reportDocReqIndex`, `getVersionChanges`, `pushAIFeedback`, `getAIFeedback`.

### Fonctions / points d'entrée clés (nouveaux, renommés, supprimés)
- Nouveaux : voir Ajouté. Supprimés : `renderChangePanel`, `askWhy`, `submitWhy`, `REASONS`, `HICONF` (Allocation) ; `qaGroups` (Compliance).
- Inchangés : `ensureTranslationFields`, `readInLanguage`, `LANG_READ_EXTRA`, `segAction` / `doSeg`, `FLAGS.captureCorrection = false`, drapeau `b.uncertain` (puce « Check boundaries », badge « Uncertain segmentation », avertissement du panneau).

### Prototype seulement (à ne pas reproduire)
- Originaux français de STB-2026 traduits à la main ; lecture dans une langue tierce = texte anglais préfixé « [German] » ; RFP-2026-114 est en anglais.
- Mode de correction de segmentation (scinder / fusionner) masqué par `FLAGS.captureCorrection = false` ; la scission découpe au point, la fusion concatène, les deux remettent seulement en To review.
- Historiques de versions d'Allocation seedés (`b.history`), sans lien avec les uploads de Documents ; aucune relance automatique simulée sur une exigence modifiée (LIFE-011).
- AI feedback : taux d'acceptation et motifs récurrents écrits en dur (`FB_RATES`, `FB_PATTERNS`), seul le fil « This session » est réel ; son texte promet encore des explications demandées en cas de forte confiance.
- Chat du tender (`tender-chat.html`, alimenté par la capture) masqué (`CHAT_ENABLED = False`).

### Visuel
- Badge Low / Medium / High dans le style des pourcentages de dérivation (`.deriv-conf.char-conf`, variante faible en couleur IA). Interrupteur « Original · French » sur fond teinté dans le panneau de Compliance.

### Synthèse
- À reprendre en production : niveaux de confiance pour la caractérisation, versions par document, colonne et onglet Changes, réouverture des verdicts, registre Q&A partagé.
- À ne pas recopier : la correction de traduction sans retour en revue, l'export qui coche l'anglais par défaut, les deux magasins de versions non reliés.

# Partie 6 — Accueil, création, tableau de bord, statistiques, configuration, casting

Comparaison `5e7ae6b` (8 sept. 2026) → `main` (`b675936`). Fichiers : `accueil.html`, `creation-projet.html`, `dashboard-et-config.html` (trois écrans dans un fichier : `#dash-screen`, `#cfg-screen`, `#team-screen`, basculés par `showScreen()`), plus la partie du shell (`build_merge.py`) que ces écrans appellent. Rappel de convention inchangée : chaque écran garde son propre miroir de données écrit à la main ; le shell ne sert que de boîte aux lettres entre écrans.

## Accueil — `accueil.html`
Volume : +315 / −130 lignes depuis 5e7ae6b ; 19 commits.

### Ajouté
- Bandeau `.home-hero` : `#hero-hello` (salutation selon l'heure + prénom tiré de `getCurrentUser()`), phrase d'objet de SRM, `#hero-roles` (« You lead N tenders as project manager and contribute to M », compté sur `role` des tenders), boutons `#new-btn-2` et `#howto-btn`, carte métro décorative `svg.hero-map`. (b862a20, bef01a1)
- Carte de reprise `#continue-slot` / `#continue-card` : `continueProject()` (tender `primary` parmi les ouverts — ni `processing`, ni `submitted`, ni `builtOut:false` — sinon le premier), `nextStep()` (« N requirements still to allocate » / « still to answer in Compliance »), mini-ligne, bouton « Continue → ». (b862a20)
- Onboarding `#howto` : constante `HOWTO` (4 stations, phrase, « qui », classe de rôle `pm` / `contrib`), `renderHowto()`, `introHidden()` ; « Got it — hide » → `setHomeIntroHidden(true)` ; `#howto-btn` → `setHomeIntroHidden(false)` + défilement. (b862a20, 58781b0)
- En-tête de section `.home-sec` (« My tenders » + `#home-sub` « N tenders »), marque rouge décorative devant le titre.
- Carte de tender : badge de ligne `.pc-lineb` (`l-turnkey` / `l-sig` / `l-other`), puce de rôle `.pc-role` (`is-pm` + `ic-flag`, sinon `ic-users`), mini-ligne `gaugeHTML(p)` (`LINE_STATIONS` = Capture, Allocation, Compliance, Submission ; `.ml`, `.ml-seg`, `.ml-dot.done/.current`, `.ml-lbl`), pied `.pc-proc` (pastille animée). (41de42d, 8f87319)
- `openTender(p)` commun à la carte et à la carte de reprise ; utilitaires `escH`, `isPM`, `currentUser()`.

### Modifié (avant → maintenant)
- `cardHTML(p)` : avant ref + badge d'étape (`STATUS`) / nom / `.pc-meta` (rôle, ligne, `deadlineChip`) / `.pc-health` / corps selon statut (barre de traitement, « done/total », « Response submitted ») / pied → maintenant badge de ligne + ref + puce de rôle / nom / `gaugeHTML` / pied. Le libellé de traitement et « Response submitted · N requirements » passent dans l'infobulle de la ligne.
- Jauge : avant `done/total` à sens variable selon le statut → maintenant `allocated/total` puis `complianceFilled/total` dès que `allocated >= total` ; `processing` = Capture avec %, `submitted` = toutes stations faites.
- `render()` : sous-titre « N tenders · you lead as Bid Director » → « N tenders » ; appelle `renderHero()` ; clic carte → `openTender()`.
- Toast « demo-only » : cite STB-2026 et RFP-2026-114 (deux tenders construits).
- Rôle : avant badge texte libre (`p.role` tel quel : « Project manager », « Signalling manager », « Expert ») → maintenant deux libellés, `/project\s*manager/i` → « Project manager », tout le reste → « Contributor ».
- En-tête : marque SRM en SVG inline (variantes clair / sombre) → logo Alstom (`.brand-logo`, deux PNG clair / sombre) + `.logo` « SRM » en texte ; deux favicons → un seul (marque SRM). (575fbbe)

### Retiré
- `STATUS` (Processing / Allocation / Expert review / Q&A & Versioning / Submitted), `HEALTH_LABEL`, `deadlineChip()`, `roleBadge()` ; CSS `.pc-badge`, `.b-*`, `.pc-meta`, `.pc-health`, `.pc-prog`, `.pc-bar`, `.pc-stat`, `.deadline-chip`.
- Le titre « My tenders » en `h1` du hero (le `h1` porte maintenant la salutation).
- Ajoutés puis retirés le 6 oct. (absents des deux versions) : bloc glossaire « Words you'll meet » (c2bb430), frise « Next submissions » (1ba9f3d), fond dégradé bleu en haut de page (1a573c6).

### Modèle de données et état (champs, statuts, clés partagées entre écrans, API du shell utilisée)
- Lit `getProjects()`. Champs utilisés : `id, ref, name, line, role, status, progress, procLabel, total, allocated, complianceFilled, reqs, updated, builtOut, primary`. Champs abandonnés par l'écran : `done`, `health`, `healthNote`, `deadline`, `days` (les jours ne s'affichent plus sur l'accueil).
- Statuts encore lus : `processing`, `submitted`, autre = « In progress » (onglets All / Processing / In progress / Submitted inchangés). `expert_review` n'est plus semé ; `qa_versioning` subsiste (stb133) et s'affiche en station Compliance.
- API du shell : `getProjects`, `getCurrentUser`, `getHomeIntroHidden` / `setHomeIntroHidden` (nouvelles), `openProject`, `route("new")`, `resetDemo`, `getTheme`.

### Fonctions / points d'entrée clés (nouveaux, renommés, supprimés)
- Nouvelles : `gaugeHTML`, `continueProject`, `nextStep`, `renderHero`, `introHidden`, `renderHowto`, `openTender`, `currentUser`.
- Supprimées : `deadlineChip`, `roleBadge`.
- Inchangées : `getProjects`, `inTab`, `render`, `toast` ; sondage `setInterval` 700 ms tant qu'un tender est en traitement.

### Prototype seulement (à ne pas reproduire)
- Bouton « ↺ Reset demo » + `confirm()` natif ; blocage des tenders `builtOut:false` ; temporisation de traitement simulée par le shell.
- Choix du tender à reprendre par le drapeau de démo `primary` (pas « le dernier ouvert »).
- Rôle déduit par regex d'un texte libre : « Signalling manager » (RFP-2026-114) s'affiche « Contributor ».
- Chiffres semés incohérents avec le dashboard : STB-2026 = 10/12 alloués ici, 5/14 sur le dashboard (déjà le cas au 8 sept.).
- Salutation calculée sur l'heure du poste ; « Updated today / 2h ago » sont des chaînes de démo.

### Visuel
- Bleus de la page (`--brand-blue`, `--brand-blue-soft`, `--brand-slate`, hors échelle suivie) : kicker, prénom, carte métro, badges (Turnkey marine, SIG bleu, autres ardoise), couleurs de rôle ; `h1` à 32 px ; `.wrap` 1120 → 1180 px ; sous 1220 px la carte de reprise passe sous la salutation et la carte métro occupe le coin.
- Police Alstom / Noto Sans, titres `--font-heading`, marque rouge devant `h1`/`h2` et les titres de section ; icônes `<i class=ic-…>`.

### Synthèse
- L'accueil devient une page d'entrée : bandeau, reprise, onboarding masquable, puis la grille.
- La carte de tender est reconstruite : ligne produit, rôle à deux valeurs, ligne à 4 stations ; plus de santé, de compte à rebours ni de badge d'étape.
- Nouveau contrat avec le shell : `allocated` / `complianceFilled` remplacent `done`, et `homeIntroHidden`.

## Création d'un tender — `creation-projet.html`
Volume : +202 / −90 lignes depuis 5e7ae6b ; 12 commits.

### Ajouté
- Champ produit `#f-product` (+ `#f-product-label`, `#f-product-help`, `#f-product-note`) piloté par `renderProductField()` : `SYSTEM_PRODUCTS = {SIG: [Urban, Mainline Wayside, Mainline Onboard]}` ; Turnkey → libellé « Combination », select désactivé « — Not available — » + note placeholder (DEC-048) ; ligne sans liste (RSC, Services) → « Product » désactivé + note « products have not been supplied » ; SIG → select, note différente pour les deux produits sur clés (`KEYED`) et pour Urban. (b3a195d, DEC-049)
- `CREATOR` : le créateur vient de `getCurrentUser()` (repli codé si l'écran est ouvert seul). (14e3059)
- Langue unique : `LANG_LABEL`, `docLang()` ; `goStep(2)` redessine la liste de documents (la langue peut avoir changé en étape 1). (14e3059, DEC-096)
- `esc()` ; `STEP_LABEL` dans `modeLabel()` (« Custom — Capture, Characterisation… » au lieu des clés `seg, char`).

### Modifié (avant → maintenant)
- Sélecteur de ligne `#line-picker` : Turnkey / RCS / SIG / INFRA / Rolling Stock / Services → Turnkey / RSC / SIG / Services (d72a2a9 pour RSC, 2169056 pour INFRA et Rolling Stock).
- `LINE_NOTE` / `LINE_NOTE_DEFAULT` : « resolves to an activity / to a person » → Turnkey « Routes to systems; each derives its ABS / PBS / OBS and person », SIG « Derives ABS, PBS and OBS, then the person for each OBS », défaut « No model supplied yet — allocated by hand ». `renderLineNote()` appelle `renderProductField()`.
- État `P` : `system:"Mainline"` → `product:""` ; `file` supprimé. `validate(1)` lit `#f-product` au lieu de `#f-system`.
- Résumé (`renderSummary`) : ligne « System » → « Combination » (Turnkey) ou « Product ».
- `createProject()` : n'appelle plus `setReviewValidated(false)` ni `setProjectMeta({...})` (14e3059) ; `addProject({…, product: P.product, …})` au lieu de `system: P.system` (b3a195d).
- Textes : étape 1 (l'échéance ne pilote plus que le compte à rebours), étape 2 (versions dans Documents & versions ; « Allocation stays empty »), étape 3 (« This mode is fixed once the tender is created », DEC-095 ; descriptions Characterisation — nature, classe, Low / Medium / High — et Allocation — routage Turnkey ou dérivation ABS / PBS / OBS), étape 4 (« Team casting »), vocabulaire activity → system.
- Liste de recherche PM : le CSS ciblait `.cast-add-list` alors que l'élément `#pm-add-list` porte la classe `.pm-add-list` — liste jamais masquée ; règles renommées `.pm-add-list` / `.pm-add-list.open` (14e3059).
- En-tête : logo Alstom + « SRM » ; favicon unique.

### Retiré
- `#f-system` (Mainline, Urban / Metro, Tramway, Monorail, Multiple systems) ; champ `lang` par document ; `P.file` ; CSS `.filecard` (mort).

### Modèle de données et état (champs, statuts, clés partagées entre écrans, API du shell utilisée)
- `P = {step, name, ref, line, product, region, language, issuer, deadline, preset, ai:{seg, char, alloc}, docs:[{name, pages, size}], pmTeam:[{id, name, title, init, color}]}`.
- Mode calculé (`computedMode`, inchangé) : `manual` si ni capture ni caractérisation, `segmentation` si pas de caractérisation, sinon `ai`.
- Appels au shell : `setProjectMode(mode)`, `addProject({name, ref, line, product, region, language, mode, days, pmTeam})`, `setCurrentProject(newId)`, `route("review" | "dashboard" | "home")`, `getCurrentUser`, `getTheme`.
- Ce que `addProject` garde (voir Shell) : `product` désormais ; `region` est transmis mais non stocké ; ni l'émetteur, ni la date d'échéance (seulement `days`, calculé à la création), ni les documents, ni les toggles IA.

### Fonctions / points d'entrée clés (nouveaux, renommés, supprimés)
- Nouvelles : `renderProductField`, `docLang`, `esc`, `CREATOR`.
- Modifiées : `renderLineNote`, `validate`, `goStep`, `addDoc`, `renderDocs`, `modeLabel`, `renderSummary`, `createProject`.
- Inchangées : `applyPreset`, `detectPreset`, `syncAI`, `renderPMTeam`, `renderPMAddList`, `addPMMember`, `goReview` ; fin de parcours inchangée (manuel → Allocation ; sinon overlay puis dashboard).

### Prototype seulement (à ne pas reproduire)
- Documents synthétiques (`SAMPLE_DOCS`), pas de sélecteur de fichier ni de glisser-déposer ; overlay fixe de 1,4 s ; estimation de traitement en dur.
- Échéance par défaut fixe `2026-08-12` ; régions = acronymes placeholder ; annuaire PM local de 12 noms.
- Le mode est une seule valeur globale du shell (`projectMode`), pas une propriété du tender ; aucun écran de paramètres ne l'affiche (DEC-095 le demande en lecture seule).
- L'équipe PM saisie ici (`pmTeam`) est stockée sur le tender mais Team casting ne la lit pas (son `PM_TEAM` est semé à part).
- Un tender créé réutilise le contenu de référence (bandeau « Prototype scope ») ; s'il est SIG, il réutilise le miroir de RFP-2026-114.

### Visuel
- Police Alstom, titres `--font-heading`, marque rouge, accent marine ; icônes `ic-upload`, `ic-clock`.

### Synthèse
- Le champ « System » devient Produit / Combinaison, transporté jusqu'au tender (`product`).
- Lignes proposées : Turnkey, RSC, SIG, Services.
- Plus de `setReviewValidated` / `setProjectMeta` à la création : ces API n'existent plus dans le shell.
- Le mode IA reste global dans le shell : à stocker par tender dans le produit réel.

## Tableau de bord — `dashboard-et-config.html` (`#dash-screen`)
Volume : +1856 / −712 lignes depuis 5e7ae6b ; 43 commits (fichier entier : dashboard, statistiques, configuration, casting).

### Ajouté
- `IS_SIG_TENDER` (`CURRENT_PROJECT.line === "SIG"`) et miroirs du tender SIG : `SIG_REVIEW_REQS`, `SIG_FOLLOWUP_REQS`, `SIG_OVERDUE_BRANCHES`, `SIG_COMMENT_FEED`, `SIG_QA_BLOCKED` ; les miroirs STB deviennent `*_BASE` et la constante publique choisit selon le tender (ebf4668, DEC-044). Déclarés avant les données qui en dépendent (une `const` n'est pas hissée).
- Hero : `#dash-total-reqs` (`renderHeroVolume()`, taille du miroir) ; `#dash-line-sub` (existant, « Multi-site EMS » en dur) porte maintenant le produit, masqué s'il égale la ligne ; jours restants = `p.days` du tender ouvert (avant : 23 en dur).
- Descriptions `.ph-desc` sous Allocation et Compliance (texte provisoire signalé comme tel).
- Rail « Always open » : carte `#ph-risks` (nombre de risques via `getRisks`, IIFE `renderRisksCard`) ; descriptions des quatre cartes passées en attribut `title`.
- Cloche : `#notif-btn` + `#notif-drop`, `notifItems()` (à revoir, OBS faibles, retards, dernière version), `renderNotifDrop()` rendu à l'ouverture dans un `try/catch`, « Nothing waiting on you here ». (b3a195d)
- `#reassign-rollup-card` : `renderReassignRollup()` (demandes `requestStatus === "pending"` de `getReassignRequests()`, 5 au plus, vers Allocation). (f21b2b5)
- `#comments-feed` « Recent comments » : `renderCommentsFeed()` (demandes de réaffectation en direct + `COMMENT_FEED_DEMO`, 6 plus récentes). (f21b2b5)
- `#exp-summary` « Answers by system » : `renderAnswersCard()` (les trois systèmes — sous-systèmes sur SIG — qui ont le plus d'affectations confiées, avec répondues / confiées ou « N late »). (1c6fe67)
- Récit de version : `versionChangesHere()`, `lastVersionChange()`, `renderVersionNews()` (`#att-ver-t`, `#att-ver-sub`, `#feed-ver`, `#feed-ver-reopen`, suppression de `#feed-ver-reopen-item` si rien n'est rouvert). (8c748a3, DEC-122)
- `allocProgress()` : `getAllocationProgress(projectId)` si Allocation a rapporté, sinon le miroir (DEC-098). `renderNarrativeCards()` : élément Not compliant lu sur `getGapStats` (repli miroir) et dernière réponse du fil.
- `showScreen("dash")` redessine la courbe et `renderCastingProgress()` / `renderStatsTeam()` / `renderStatsBySystem()` (les éditions du casting se voient au retour).

### Modifié (avant → maintenant)
- `applyGating()` : avant `reviewDone()` (= `isReviewValidated()` du shell) masquait `.p2only` avant finalisation et `.p1only` après → maintenant `done = allocated === total` (DEC-098) ; seul `.p1only` (« Requirements still to validate ») se masque ; `.v22only` visible si `lastVersionChange()` ; carte Done « / N allocated · done » au lieu de « / 14 validated · finalized » en dur.
- `renderReviewKPIs()` : lit `allocProgress()` ; « requirements validated » → « requirements allocated » ; n'alimente plus `#hs-total-reqs` / `#hs-validated`.
- Éléments « What needs you now » : « Allocation not finalized / Finalize allocation → » → « Requirements still to validate / Open Allocation → » ; « New version v2.2… SRM-00009 » en dur → texte calculé ; « Fix in review » → « Fix in Allocation » ; « 2 questions awaiting internal review… duplicate » (→ Compliance) → « 2 questions to send » (→ `qa.html`) ; « 1 non-compliant requirement (Infrastructure) » en dur → `#att-noncomp-t/-sub` calculés ; plus aucun élément `.p2only`.
- Hero : avant réécrit seulement pour un tender non construit (STB codé en dur sinon) → toujours réécrit d'après le tender ouvert (376c6a5) ; produit lu sur `p.product || p.system` (e962c96).
- Bandeau `#dash-scope-banner` : « Team casting is this project's own » → « Allocation, Compliance, Statistics and Team casting reuse a reference tender's content ».
- `renderCastingProgress()` : « / 7 activities fully staffed » + barre → « / M staffed » = systèmes avec au moins une ligne de roster ; badge « K pending » / « Complete » ; plus de barre.
- Rail de support : 3 cartes (chiffre ; barre + badge « N pending » sur Team casting, badge « Open » sur Documents et Q&A) → 4 cartes sur deux lignes (nom, chiffre), description en infobulle, badge seulement sur Team casting, plus de barre. (9fad58e, e962c96)
- Fil « Recent activity » : entrées v2.2 en dur → `#feed-ver*` calculés ; « responded … Needs clarification » → dernière réponse du miroir ; « Q&A batch sent » → « QA-01 marked as sent » ; « Allocation milestone reached » et lien « View all » supprimés.
- `OVERDUE_BRANCHES` : 1 entrée → 4 (STB) avec champ `unit` (système ; sous-système sur SIG).
- Navigation : `#ph-risks` → `goRoute("risks.html")` (nouvelle route `risks` du shell).

### Retiré
- `reviewDone()`, `v22Done()`, `renderComplianceKPIs()`.
- Cartes Project health (`.health-stats`, `#hs-*`, « Managers assigned » 100 %), Compliance de la colonne (`#compseg-*`, `#compleg-*`), Experts (lignes nominatives en dur), `.locked-hint` ; classe `.p2only`.
- Rangée de KPI (ajoutée en f21b2b5, retirée en 633685b) ; essais « ligne du tender » à quatre stations (41de42d, d143a45, retirés en 2a42509 — plus de `renderTenderLine`).
- CSS mort : `.screen-nav`, `.team-mgr-*`, `.ph-sub`, `.exp-ln`, `.card h3 a`.

### Modèle de données et état (champs, statuts, clés partagées entre écrans, API du shell utilisée)
- `REVIEW_REQS` : `{id, status}` → `{id, status: suggested|toreview|edited|allocated, activity: code système ou null (non routé), obsWeak?}`.
- `FOLLOWUP_REQS` : `branchesAnswered/branchesTotal` → `branchStatuses: [proposed|assigned|awaiting_answer|awaiting_qa|reassignment_needed|answered]` + `overdueBranches?` ; `compliance` ∈ `compliant | not_compliant | null` (plus de `rnd_needed`, 22d651b).
- `OVERDUE_BRANCHES` : `{reqId, expert, days, unit}` ; `COMMENT_FEED_DEMO` : `{kind, who, what, when, sortKey}`.
- API du shell lues : `getCurrentProject`, `getCurrentUser`, `getAllocationProgress`, `getVersionChanges` (`[{doc, docName, num, m, gap:{a,m,r}, modified:[ids], reopened, logged}]`), `getGapStats`, `getRisks`, `getReassignRequests`, `routeUrl`. Plus lues : `isReviewValidated`, `isV22Uploaded`.

### Fonctions / points d'entrée clés (nouveaux, renommés, supprimés)
- Nouvelles : `notifItems`, `renderNotifDrop`, `versionChangesHere`, `lastVersionChange`, `renderVersionNews`, `allocProgress`, `renderHeroVolume`, `renderCommentsFeed`, `renderReassignRollup`, `renderAnswersCard`, `renderNarrativeCards`.
- Modifiées : `applyGating`, `renderReviewKPIs`, `renderCastingProgress`, `showScreen` (`renderOverdueCard` inchangée, mais nourrie par les 4 entrées de `OVERDUE_BRANCHES`).
- Supprimées : `reviewDone`, `v22Done`, `renderComplianceKPIs`.
- Point d'entrée shell inchangé : `showConfig(bool)` / `showScreen("team")` appelés par le routeur (`config`, `dashboard`, `team`).

### Prototype seulement (à ne pas reproduire)
- Miroirs écrits à la main (convention « pas de couche de données partagée ») ; chiffres fixes : Documents (« 3 docs · 1 processing »), Q&A (« 5 questions · 1 answered »), « 2 uncertain segmentations », « 2 questions to send » (ne lit pas le registre Q&A du shell).
- Le hero et les statistiques comptent le miroir (14 exigences sur STB) alors que la carte Allocation lit le rapport réel d'Allocation dès qu'il existe (capture complète) : les deux peuvent diverger.
- « Bid Director: » suivi du nom de l'utilisateur de démo, en dur dans le hero (pas lu sur `getCurrentUser`) ; lien « DEMO Compliance (contributor) → ».
- Fil de commentaires et fil d'activité en partie écrits à la main ; ni l'un ni l'autre ne lit le journal `getActivityLog`.
- Un tender créé dans l'assistant affiche le contenu de référence (STB, ou RFP-2026-114 s'il est SIG) ; le nom de classe `.v22only` est un reste de l'ancien drapeau v2.2.

### Visuel
- Rail de support en 4 colonnes (2 sous 1000 px), cartes sur deux lignes ; descriptions d'étape ; menu déroulant de la cloche ; icônes au trait à la place des emoji ; thème sombre sur la famille marine.

### Synthèse
- Plus de finalisation : `isReviewValidated` disparaît, la carte Allocation lit `getAllocationProgress` (DEC-098).
- Le dashboard lit désormais le shell pour : progression d'Allocation, versions enregistrées, totaux de Compliance, risques, demandes de réaffectation.
- Deux jeux de miroirs (STB / SIG) choisis par `IS_SIG_TENDER`.
- Colonne de droite refaite : commentaires + réponses par système ; Project health, barre de conformité et Experts supprimés.

## Statistiques — `dashboard-et-config.html` (`.stats-panel`)
Volume : voir le bloc Tableau de bord (même fichier).

### Ajouté
- Onglets `data-stab="proj" | "alloc" | "compl"` (Project, Allocation, Compliance). (d109c66, DEC-117)
- Project : `renderStatsTimeline()` (liste de dates clés `.kd` + courbe SVG % alloué / % répondu, projection pointillée « at this week's pace » via `progressSeries`, `valueAt`, `finishAt` ; dessinée à la largeur disponible, redessinée à l'affichage de l'onglet) ; `renderStatsLeaderboard()` + `weekActivity()` (par système et sous-système ; ajoute les événements `live` de `getActivityLog` dont `what` vaut « CODE — allocation » vers Allocated ou « CODE — verdict », une fois par exigence) ; `renderStatsTeam()` (PM, managers, contributeurs, systèmes sans personne, systèmes actifs cette semaine).
- Allocation : `renderStatsAllocStatus()` (`ALLOC_STAGES` : suggested → Incomplete, toreview → To review, edited → To validate, allocated → Allocated ; `stackedBarHTML()`), `renderStatsBySystem()` (charge et qui est sur chaque système ; masqué si un seul système, la réallocation prend la largeur), `renderStatsRealloc()` + `reallocations()` (mailbox en direct + `REALLOC`, `REASON_LABEL`).
- Compliance : `renderStatsProgressClient()` (4 étapes sur `getGapStats`), `renderStatsAnswers()` + `lateByUnit()` (`ANSWERS_BY_SYSTEM`, `ANSWERS_UNIT` = system / sub-system), `renderStatsWaiting()` (quatre files exclusives : réallocation, client, contributeur, non affectée), `renderStatsNCStrategy()` (par stratégie + « Strategy missing »), `renderStatsRisks()` (risques, liens comptés sur `getGapDocs`, partagés, 4 plus liés avec avatar du créateur). (18294c4, 93f80d9, d109c66, 1c6fe67)
- Utilitaires : `shellGet()`, `bindGo()` (`data-go` = route, `data-screen` = écran interne), `personOf()`, `avHTML()`, `escH`, `isoDate`, `fmtDay`, `pctOf`, `nOf`, `sumOf`, `andList`.
- Phrase d'ouverture `.stat-take` dans chaque bloc ; lien « Team casting → » (`#stats-team-open`).

### Modifié (avant → maintenant)
- Onglets `pm` / `stake` (« For you » / « For stakeholders ») → `proj` / `alloc` / `compl`.
- `renderStatsInvalidated()` : avant SRM-00009 si le drapeau v2.2 est levé → maintenant somme des `reopened` de `getVersionChanges()` (bloc dans l'onglet Allocation, seulement si non nul).
- `renderStatsPanel()` appelle la nouvelle liste ; `TODAY` = soumission − jours restants (`DAYS_LEFT` = `p.days` d'un tender construit, sinon `TENDER_DATES.days`).

### Retiré
- Fonctions : `renderStatsBottlenecks`, `complianceCounts`, `renderStatsComplianceBar`, `renderStatsQABlocked`, `renderStatsCasting`, `renderStatsTrajectory`, `renderStatsProgressDeadline`, `renderStatsAIReliability`.
- Constantes : `STATS_BOTTLENECKS`, `STATS_TRAJECTORY`, `STATS_DEADLINE_LABEL`, `STATS_AI_RELIABILITY` (`STATS_QA_BLOCKED` reste, utilisée par « waiting on »).
- Blocs intermédiaires apparus puis supprimés après le 8 sept. : entonnoir passe 1 → passe 2, qualité de dérivation, consolidation, entonnoir d'affectation, retards par contributeur (d2793d2 → d109c66) ; « Internal vs declared » (retiré en 18294c4, DEC-106) ; poids des risques et matrice poids × stratégie (93f80d9, DEC-113) ; classements nominatifs (1c6fe67, DEC-118).

### Modèle de données et état (champs, statuts, clés partagées entre écrans, API du shell utilisée)
- Écrits à la main : `TENDER_DATES(_BASE)` / `SIG_TENDER_DATES` (`received, qaCutoff, qaAnswers, submission, days`), `STATS_HISTORY(_BASE)` / `SIG_STATS_HISTORY` (`{d, alloc %, answered %}`), `WEEK_BY_SYSTEM(_BASE)` / `SIG_WEEK_BY_SYSTEM` (`{lastWeek, systems:[{code, subs:[{k, a, r, c}] | a, r, c}]}` — a = validées en Allocation, r = réponses, c = commentaires et questions), `REALLOC(_BASE)` / `SIG_REALLOC` (`{reqId, sys, by, reason: wrong_person|wrong_typology|not_applicable, status: pending|approved|rejected, at}`), `ANSWERS_BY_SYSTEM(_BASE)` / `SIG_ANSWERS_BY_SYSTEM` (`{unit, given, answered}`).
- Shell : `getGapStats` → `{reqs, assignments, assigned, answered, compliant, nc, ncLogged, byStrategy:{gs_id:n}, noStrategy, ext:{compliant, not_compliant, pending, none}}` ; `getActivityLog` → événements `{reqId, ts, time, who, cat, what, from, to, k, milestone?, live?}` ; `getStrategies` → `[{id, name, ext}]` ; `getRisks` → `[{id, that, cause, impact, createdBy, createdAt}]` ; `getGapDocs` → `{"reqId#système": {strategy, risks:[ids], override, meta}}` ; `getReassignRequests` → `[{id, reqId, typology, byName, reason, note, requestStatus, at}]`.

### Fonctions / points d'entrée clés (nouveaux, renommés, supprimés)
- Voir Ajouté / Retiré. Entrée : `renderStatsPanel()` au chargement ; `renderStatsTimeline()` à nouveau au clic sur l'onglet Project et au retour sur le dashboard.

### Prototype seulement (à ne pas reproduire)
- Historique, semaine, réallocations décidées, réponses par système : écrits à la main (réponses calées sur 100 confiées / 58 répondues de `getGapStats`) ; la cible exige des snapshots et un journal exploitable (PLAT-008).
- Le point « aujourd'hui » de la courbe vient du miroir (14 exigences), pas du rapport réel d'Allocation.
- La mailbox de réaffectation n'est pas par tender : filtrage par préfixe d'identifiant (`L4-` / `SRM-`).
- Les retards sont une liste fixe (`OVERDUE_BRANCHES`), pas un calcul d'âge ≥ 5 jours ; « Overdue threshold » de la configuration n'y est pas relié.
- Sans visite préalable de Compliance, `getGapStats` renvoie les valeurs semées par le shell ; pour un tender neuf : « Counted from Compliance — open it once… ».

### Visuel
- Composants propres (`COMPONENTS.md`) : Key Dates List, Progress Trend Chart, Leaderboard Row, Team Role Row, Avatar Stack, Stacked Bar, System Manager Row, Reallocation Breakdown, Progress Sequence, System Answers Row, Waiting Queue Row, Risk Summary Row ; couleurs `is-late` / `is-tight` / `is-good` dans les phrases ; bleus de l'accueil réutilisés.

### Synthèse
- Panneau entièrement réécrit : 3 onglets, ~15 fonctions de rendu nouvelles, aucune ancienne conservée hors `renderStatsInvalidated` (réécrite).
- Unité système / sous-système partout (DEC-118) ; les personnes n'apparaissent que pour relancer, renvoyer, créer un risque ou être staffées.
- Sources : shell quand un écran a rapporté (gap stats, risques, mailbox, journal, versions), miroir sinon.

## Configuration — `dashboard-et-config.html` (`#cfg-screen`)
Volume : voir le bloc Tableau de bord (même fichier).

### Ajouté
- Navigation : `data-sec="model"` (Allocation model) et `data-sec="compliance"` (Compliance) ; icônes au trait pour les 11 entrées.
- Section `model` (5a4730a, 54fb4cf) : `#cfg-model-system` et `#cfg-model-product` en lecture seule (`.fval`), `#cfg-partners-row` (Turnkey seulement : `TK_MODEL_SYSTEMS` = 16 codes du modèle en étiquettes, partenaires ajoutés en couleur `--partner` avec ✕), `#cfg-partner-name` / `#cfg-partner-add`, `#cfg-model-select` (SIG : `sig-urban`, `sig-mainline-wayside`, `sig-mainline-onboard`, présélection = produit du tender ; sinon une option « Per-system models » désactivée), `#cfg-model-danger` (chiffres tirés du miroir : exigences, réponses enregistrées, verdicts internes) et `#cfg-model-rerun` désactivé.
- Section `compliance` (efc2777) : `#gs-list` (ligne par stratégie : nom renommable, résultat externe, « used N× », suppression désactivée si utilisée), confirmation en ligne `.gs-confirm` quand le résultat d'une stratégie utilisée change, `#gs-new-name` / `#gs-new-ext` / `#gs-add-btn`, message vide « No strategy yet… Strategy missing… Pending ».
- Capture (b2ac7af) : lignes `data-seg="convrange" | "tableformat" | "sentences" | "equations"`, champ `#convrange-pages` / `#convrange-input` affiché seulement avec « Specific pages » (gestionnaire des segmented controls, attribut `data-range`).
- General : `#cfg-general-line` (ligne en lecture seule) et ligne « Documents — Managed in Documents & versions ».
- Language : « Working language — English » en lecture seule.
- Fonctions `renderAllocationModelSection()`, `renderPartnersSetting()`, `renderStrategiesSetting()` (+ IIFE d'ajout pour chacune), constantes `TK_MODEL_SYSTEMS`, `GS_EXT_LABEL`, état `gsPending`.

### Modifié (avant → maintenant)
- Libellés : « Team & experts » → « Team & contributors » ; « Workflow & milestones » → « Reminders » ; « AI & segmentation » → « Capture & segmentation » ; « Add expert » → « Add contributor » ; textes « review screen » → « Allocation ».
- General : `<select>` de ligne (avec SIG présélectionné sur un tender Turnkey) → valeur lue sur `CURRENT_PROJECT.line` (3537205, DEC-095).
- Team & contributors : `EXPERTS` ne lit plus `CURRENT_PROJECT.experts` (liste écrite à la main, toujours la même).
- Seuil d'incertitude : « Confidence … never shown to users as a score » → « Segmentation confidence … not shown as a score ».
- AI feedback : `FB_RATES` « Activity » → « System » ; `FB_PATTERNS` 4 → 3 motifs, réécrits sur les codes de systèmes et les équipes (le motif « Turnkey added » disparaît) ; `SURF_LABEL.typo` « TYPO » → « SYS » ; « live signal from Allocation ».
- Toast de `#cfg-save` : « Theme, restricted view, partners and gap strategies apply immediately… » ; échantillons du sélecteur de thème aux nouvelles couleurs.

### Retiré
- Lignes : « Review milestone gate » (toggle `data-tog="gate"`), « Outdated-response re-flag » (`data-seg="reflag"`), « AI duplicate detection » (`data-tog="dedup"`), « Internal review before sending » (`data-tog="review"`), « Expert / Contributor notification on version switch » (`data-seg="notif"`), « Default translation target », « Source document » (fichier actif), puce « Discipline », `<select>` de ligne produit (avec INFRA / Rolling Stock).

### Modèle de données et état (champs, statuts, clés partagées entre écrans, API du shell utilisée)
- Shell — partenaires : `getPartners(pid)` → `[{id:"p_<code>", code, label}]` ; `addPartner(pid, name)` → `{entry}` | `{error:"empty"|"duplicate"}` (code = premier mot en majuscules, 8 caractères max, dédoublonné) ; `removePartner(pid, id)` → `{removed}` | `{error:"used"|"missing"}` ; `getPartnerUsage(pid, id)` = max des usages rapportés par Allocation et Compliance (`reportPartnerUsage`).
- Shell — stratégies : `getStrategies(pid)` → `[{id:"gs_n", name, ext: compliant|not_compliant|pending}]` ; `addStrategy`, `renameStrategy` (`empty` / `duplicate`), `setStrategyResult`, `removeStrategy` (`used`) ; `getStrategyUsage(pid, id)` → `{used, corrected}` (rapporté par Compliance, `reportStrategyUsage`). Liste vide pour un tender neuf ; les cinq tenders de démo ont les quatre stratégies usuelles.
- Inchangé : `getTheme` / `setTheme`, `getAIFeedback` (`[{at, surface, id, before, after, conf, reason}]`).
- Lit `CURRENT_PROJECT.line` et `.product` ; le miroir `REVIEW_REQS` / `FOLLOWUP_REQS` pour les chiffres de la relance globale.

### Fonctions / points d'entrée clés (nouveaux, renommés, supprimés)
- Nouvelles : `renderAllocationModelSection` (appelle aussi `renderStrategiesSetting` et `renderPartnersSetting`), `renderPartnersSetting`, `renderStrategiesSetting`.
- Inchangées : `renderExperts`, `applyThemeUI`, `applyRedactUI`, `renderFeedback` ; deep link `#config` → `showConfig(true)`.

### Prototype seulement (à ne pas reproduire)
- La plupart des sections ne sont pas câblées (bandeau « TE2 — demo only ») ; la section Allocation model est un affichage (sélecteur sans effet, bouton désactivé).
- « Save configuration » / « Discard changes » ne font qu'afficher un toast ; rien n'est persisté au-delà de la session.
- Liste « Team & contributors » saisie au clavier (pas d'annuaire), indépendante du roster du casting.
- Sur un tender sans produit qui n'est pas Turnkey (RSC, Services), le produit affiche quand même le message de combinaison Turnkey (DEC-048).
- Partenaire semé sur STB-2026 et usages semés pour que les refus soient démontrables avant ouverture d'Allocation / Compliance.

### Visuel
- Icônes de navigation au trait ; `.fval` pour les valeurs en lecture seule ; `.dangerbox` + `.btn-danger` pour la relance globale ; étiquettes `.pt-tag` (partenaire en `--partner`, couleur hors échelle) ; lignes `.gs-row`.

### Synthèse
- 9 → 11 sections ; deux réglages réellement agissants ajoutés (partenaires Turnkey, stratégies d'écart), tous deux stockés dans le shell par tender.
- Ligne produit, produit et langue de travail en lecture seule.
- Sept réglages sans réalité retirés ; réglages de capture ajoutés en affichage seul.

## Team casting — `dashboard-et-config.html` (`#team-screen`)
Volume : voir le bloc Tableau de bord (même fichier).

### Ajouté
- `SIG_CAST_ACTIVITIES` (un seul système SIG) et `SIG_ROSTER` (4 personnes sur des périmètres) ; « + Add system » masqué sur un tender SIG.
- Une personne = un système : `castOtherSystemOf(personId, activityId)`, `castRefuseOther(p, other)` ; dans la recherche, option grisée `.cast-add-opt.is-blocked` avec `.cast-add-opt-where` (« In XXX — one system per person » ; « Already in XXX » pour un autre périmètre du même système) ; refus par toast au choix ou à la confirmation. (8c748a3, DEC-102 / DEC-124)
- Choix du périmètre par `<select>` (« — No perimeter — staffed directly — » + liste partagée).

### Modifié (avant → maintenant)
- `CAST_ACTIVITIES` : 7 activités inventées (SIG « Signalling & Urban », MLN, INF, PWR, TLC, CVL sans manager, SYS) → 7 codes de la liste de 16 (`CAST_ACTIVITIES_BASE` : SIG, TRK, SEN, POS, COM, RST, RAMS ; libellé = code ; `hasModel` sur SIG et RST ; RST sans manager). (762f9c0, 5db101e)
- `REFERENCE_ACTIVITIES` : RST, COM, SAF, ARC → `REFERENCE_ACTIVITIES_BASE` = AFC, CJV, CYB, DEQ, ILS, PSD, SCADA, OCS, SPM (vide sur SIG).
- `PERIMETERS` : dictionnaire de listes par activité, extensible → tableau unique fermé DBM, Risk, BTM, Wayside, Design, V&V ; `perimetersOf()` renvoie toujours ce tableau ; `perimeterLabel()` adapté.
- `activityCoverage(a)` : avant périmètres propres (ou « direct » si aucun) → maintenant 6 périmètres + 1 emplacement « direct » = 7 groupes ; « Fully staffed » seulement si les 7 sont pourvus.
- `castGroupHTML(a, viewerIsAdmin)` : droits avant `!!managerId && (admin || manager)` → maintenant `admin || (managerId === viewer)` ; système sans manager : avant corps bloquant `.cast-noperm` + badge « No manager cast » → maintenant périmètres + ajout pour le PM, ligne « No manager — contributors only », note en lecture seule pour les autres ; badge toujours = couverture.
- `castPerimeterHTML(a, perim, label, editable)` : les ✕ de retrait suivent les droits (avant affichés aussi dans les groupes en lecture seule).
- `bindCastAddFlow()` : périmètre saisi / datalist + `resolvePerimeter` → `<select>` fermé ; contrôle « un système par personne » avant le contrôle de doublon.
- `renderCoverageStrip()` : plus d'état « No manager cast yet ».
- `renderTeamScreen()` : puce « Just added » limitée au système (`CAST_LAST_ADDED.activityId`) ; « + Add system » masqué sur SIG.
- `renderAddActivityPop()` : toast « … added — cast a manager… » → « … added — staff it below » ; le système ajouté s'ouvre avec sa boîte d'ajout.
- `generateScaleRoster()` : avant activités avec manager seulement → maintenant tous les systèmes, en respectant « un système par personne ».
- `initTeamViewer()` : groupe « Activity managers » → « System managers ».
- `MANAGERS` : rôles « Mainline / Infrastructure / Power Supply / Telecom / Systems Integration manager » → « TRK / SEN / POS / COM / RAMS manager ».
- `ROSTER` → `ROSTER_BASE` remappé sur les nouveaux codes et périmètres ; chaque personne dans un seul système (DEC-102).

### Retiré
- `resolvePerimeter()`, `<datalist>` de périmètres, création de périmètre `custom`.
- `.cast-noperm`, `.cast-group-badge.noperm`, badge « No manager cast », exclusion des systèmes sans manager de la génération d'échelle.

### Modèle de données et état (champs, statuts, clés partagées entre écrans, API du shell utilisée)
- `CAST_ACTIVITIES` : `{id, code, label, managerId | null, hasModel?}` ; `ROSTER` : `{personId, activityId, perimeterId | null, addedBy, addedAt, count}` (`count > 0` = travail assigné → retrait refusé) ; `PM_TEAM` : `{id, name, title, init, color, addedBy, addedAt}` ; `MANAGERS` : `{id, name, role, init, color}` ; `DIRECTORY` : `{id, name, init, color}` ; `PERIMETERS` : `[{id, label}]`.
- Tout est local à l'écran : ni le shell, ni Allocation, ni Compliance ne lisent ces données (leurs `MANAGERS` sont des miroirs séparés) ; toute modification est perdue au changement de route (l'iframe se recharge).
- API du shell : aucune (hors `getCurrentProject` pour `IS_SIG_TENDER`).

### Fonctions / points d'entrée clés (nouveaux, renommés, supprimés)
- Nouvelles : `castOtherSystemOf`, `castRefuseOther`.
- Signature modifiée : `castPerimeterHTML(a, perim, label, editable)`.
- Supprimée : `resolvePerimeter`.
- Modifiées : `activityCoverage`, `castGroupHTML`, `bindCastAddFlow`, `renderCoverageStrip`, `renderTeamScreen`, `renderAddActivityPop`, `generateScaleRoster`, `renderCastingProgress`, `initTeamViewer`.

### Prototype seulement (à ne pas reproduire)
- Sélecteur « Viewing as » (PM ou manager simulé) ; aucun contributeur simple ne peut être simulé, alors que la cible lui donne la gestion des rattachements de son système (DEC-003).
- Bouton « DEMO Simulate 200 roster » ; annuaire SSO simulé (35 noms + noms générés).
- Pas de persistance ; `PM_TEAM` semé indépendamment de l'équipe saisie à la création.
- Formule de couverture à 7 groupes : artefact de la liste de périmètres partagée ; la règle cible est « non staffé = personne » (DEC-124).

### Visuel
- Option de recherche grisée avec le système d'appartenance ; ligne « No manager — contributors only » en gris neutre ; icônes `ic-search`, `ic-lock`, `ic-eye`.

### Synthèse
- Liste des systèmes = codes de la capture, périmètres = liste fermée partagée (DEC-032, DEC-036).
- Le PM staffe tout système, avec ou sans manager ; « un système par personne » refusé dès la recherche.
- Casting toujours local à l'écran, non persisté et non partagé avec Allocation / Compliance.

## Shell — partie projets et identité — `build_merge.py`
Volume : +491 / −75 lignes depuis 5e7ae6b ; 30 commits (fichier entier ; seule la partie appelée par ces trois écrans est décrite ici).

### Ajouté
- `homeIntroHidden` + `getHomeIntroHidden()` / `setHomeIntroHidden(v)` (remis à `false` par `resetDemo`). (b862a20)
- Champs de tender : `allocated`, `complianceFilled` (2dd1fb4), `product` (b3a195d) ; `system` sur la graine RFP-2026-114.
- Route `risks` dans `ROUTES` et `risks.html` dans `URLMAP` (Risks dans le rail du dashboard).
- APIs consommées par le dashboard et la configuration (détail dans les blocs ci-dessus) : `getAllocationProgress`, `getVersionChanges`, `getGapStats`, `getActivityLog`, partenaires, stratégies, risques, `getGapDocs`.

### Modifié (avant → maintenant)
- `seedProjects()` : `rfp114` construit (`builtOut:true`, « Line 4 Resignalling — ETCS L2 », `requirement_review`, 12 exigences dont 4 allouées, `language:"en"`, `system:"Mainline"`, `product:"Mainline Wayside"`) ; rôles « Expert » → « Contributor » ; `done` → `allocated` / `complianceFilled`.
- `addProject(meta)` : stocke `product` ; `done` → `allocated` / `complianceFilled` à 0 ; plus de drapeau `deadline`.
- `startProcLoop()` : « Allocating to experts… » → « Allocating to contributors… » ; plus de `done = 0` en fin de traitement.
- `resetDemo()` : remet aussi à zéro partenaires, stratégies, risques, journal, totaux de Compliance, progression d'Allocation, versions enregistrées, registre Q&A, colonnes personnalisées, onboarding ; ne touche plus `reviewValidated` ni `projectMeta`.
- `HEADER` : favicon unique (marque SRM) au lieu de deux favicons clair / sombre.

### Retiré
- `isReviewValidated` / `setReviewValidated` et `getProjectMeta` / `setProjectMeta` (14e3059 ; le dashboard avait cessé de lire `isReviewValidated` dès 3537205, DEC-098).
- Champs de graine `deadline:1`, `done`, `health`, `healthNote`.

### Modèle de données et état (champs, statuts, clés partagées entre écrans, API du shell utilisée)
- Tender : `{id, ref, name, line, days, status, total, allocated, complianceFilled, progress?, procLabel?, reqs?, updated, role, builtOut?, primary?, language, system?, product?, experts:[], pmTeam:[]}`.
- `CURRENT_USER` inchangé (`title:"Bid Director"`) ; `projectMode` reste une valeur globale (`ai` | `segmentation` | `manual`).
- `isV22Uploaded` / `setV22Uploaded` existent encore (Documents lève le drapeau) mais le dashboard ne les lit plus.

### Fonctions / points d'entrée clés (nouveaux, renommés, supprimés)
- Nouvelles : `getHomeIntroHidden`, `setHomeIntroHidden` (et les API listées plus haut).
- Supprimées : `isReviewValidated`, `setReviewValidated`, `getProjectMeta`, `setProjectMeta`.

### Prototype seulement (à ne pas reproduire)
- Graines : trois tenders « demo-only » (dont des lignes INFRA et Rolling Stock que l'assistant ne propose plus) ; boucle de traitement aléatoire ; `Ctrl+Shift+R` = reset.
- `region`, émetteur, échéance et documents saisis à la création ne sont pas stockés ; `days` est figé à la création.

### Visuel
- Néant (hors favicon).

### Synthèse
- Le contrat « tender » change : `allocated` / `complianceFilled` / `product`, sans `done` / `health` / `deadline`.
- Deux API de l'ancien flux de finalisation disparaissent ; le mode de traitement reste global.
