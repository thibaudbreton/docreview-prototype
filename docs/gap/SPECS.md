# Écart de spécifications — du 8 septembre au 9 octobre 2026

Départ : `5e7ae6b` (`main` le 8 septembre 2026 à 14 h 14). Arrivée : `main` au 9 octobre 2026 (`b675936`). Synthèse et mode d'emploi : [README.md](README.md). Registre des décisions : [DECISIONS.md](DECISIONS.md). Code : [CODE.md](CODE.md).

Chaque point porte une marque : **(R)** règle métier, à appliquer dans le produit ; **(P)** comportement de prototype ou de démonstration, à ne pas reproduire ; **(X)** retiré. « (déduit) » signale une conclusion tirée de la lecture du code ou des documents, non vérifiée autrement. Références : `DEC-xxx` = décisions (`docs/current/OPEN-QUESTIONS.md`, détail dans [DECISIONS.md](DECISIONS.md)) ; `ALLOC-`, `CONF-`, `LIFE-`, `ACC-`, `QA-`, `AI-`, `PLAT-`, `JRN-`, `UX-`, `CUST-`, `KEY-`, `TYPE-` = règles de `docs/current/` ; les hash (`8c748a3`…) sont des commits (`git show <hash>`).

**Autorité.** La décision la plus récente prime : sur une spec du 8 septembre, sur un constat du prototype, et sur les lignes de `docs/current/` restées en retard (elles sont signalées dans les rubriques « Toujours ouvert »).

## Sommaire

- [Partie 1 — Où sont les specs aujourd'hui](#partie-1--où-sont-les-specs-aujourdhui)
  - [Carte des documents](#carte-des-documents)
- [Partie 2 — Socle : organisation, modèle métier, plateforme, charte](#partie-2--socle--organisation-modèle-métier-plateforme-charte)
  - [1. Organisation documentaire et autorité](#1-organisation-documentaire-et-autorité)
  - [2. Modèle métier, vocabulaire et rôles](#2-modèle-métier-vocabulaire-et-rôles)
  - [3. Exigences transverses : plateforme, notifications, métriques, journal, clavier](#3-exigences-transverses--plateforme-notifications-métriques-journal-clavier)
  - [4. Charte graphique et marque](#4-charte-graphique-et-marque)
- [Partie 3 — Allocation](#partie-3--allocation)
  - [Allocation — sources et autorité (lire d'abord)](#allocation--sources-et-autorité-lire-dabord)
  - [Modèle d'allocation — vocabulaire, Turnkey / SIG, chaîne de dérivation, OBS et personnes](#modèle-dallocation--vocabulaire-turnkey--sig-chaîne-de-dérivation-obs-et-personnes)
  - [Statuts, revue et validation](#statuts-revue-et-validation)
  - [Relance des modèles d'allocation](#relance-des-modèles-dallocation)
  - [Nature, classe et caractérisation](#nature-classe-et-caractérisation)
  - [Clés PBS / OBS / ABS de SIG (modèle Mainline)](#clés-pbs--obs--abs-de-sig-modèle-mainline)
  - [Profils de tender : Turnkey, SIG autonome (RFP-2026-114) et partenaires externes](#profils-de-tender--turnkey-sig-autonome-rfp-2026-114-et-partenaires-externes)
  - [Accès : vue contributeur, lecture seule et « View as »](#accès--vue-contributeur-lecture-seule-et--view-as-)
  - [Tableau Allocation (ex-« Requirements review »)](#tableau-allocation-ex--requirements-review-)
  - [Filtres (colonnes et constructeur avancé)](#filtres-colonnes-et-constructeur-avancé)
  - [Colonnes personnalisées](#colonnes-personnalisées)
  - [Panneau de détail et journal d'activité](#panneau-de-détail-et-journal-dactivité)
  - [Versions, colonne Changes et vue Document (dont SPEC-document-view)](#versions-colonne-changes-et-vue-document-dont-spec-document-view)
- [Partie 4 — Compliance et Risks](#partie-4--compliance-et-risks)
  - [Modèle de conformité (verdicts, consolidation, ce que reçoit le client, droits)](#modèle-de-conformité-verdicts-consolidation-ce-que-reçoit-le-client-droits)
  - [Statuts d'une affectation et transitions (réponse, question au client, renvoi, relance, nouvelle version)](#statuts-dune-affectation-et-transitions-réponse-question-au-client-renvoi-relance-nouvelle-version)
  - [Panneaux de détail : panneau de décision du contributeur et panneau du chef de projet](#panneaux-de-détail--panneau-de-décision-du-contributeur-et-panneau-du-chef-de-projet)
  - [Écran Compliance : table, navigation, vue Document, export, notifications, colonnes](#écran-compliance--table-navigation-vue-document-export-notifications-colonnes)
  - [Stratégies d'écart, risques et conformité externe](#stratégies-décart-risques-et-conformité-externe)
  - [Page Risks (écran de support)](#page-risks-écran-de-support)
  - [Partenaires externes — côté Compliance](#partenaires-externes--côté-compliance)
  - [Journal d'activité d'une exigence (partagé Allocation / Compliance)](#journal-dactivité-dune-exigence-partagé-allocation--compliance)
- [Partie 5 — Documents et versions, Q&A, langue, capture, IA](#partie-5--documents-et-versions-qa-langue-capture-ia)
  - [Documents, versions et cycle de vie des exigences entre versions](#documents-versions-et-cycle-de-vie-des-exigences-entre-versions)
  - [Q&A avec le client](#qa-avec-le-client)
  - [Langue et traduction](#langue-et-traduction)
  - [Capture et segmentation](#capture-et-segmentation)
  - [IA : modèles, confiance, relances, retour d'expérience](#ia--modèles-confiance-relances-retour-dexpérience)
- [Partie 6 — Accueil, création, tableau de bord, statistiques, configuration, casting](#partie-6--accueil-création-tableau-de-bord-statistiques-configuration-casting)
  - [Accueil (My tenders)](#accueil-my-tenders)
  - [Création d'un tender (assistant)](#création-dun-tender-assistant)
  - [Tableau de bord du tender](#tableau-de-bord-du-tender)
  - [Statistiques du tableau de bord](#statistiques-du-tableau-de-bord)
  - [Configuration (paramètres du tender)](#configuration-paramètres-du-tender)
  - [Team casting (équipes et droits de casting)](#team-casting-équipes-et-droits-de-casting)

# Partie 1 — Où sont les specs aujourd'hui

Au 8 septembre à 14 h 14, les specs étaient dans `docs/specs/SPEC-*.md`, le glossaire et `docs/decisions/DECISIONS.md`. Le même jour à 16 h 43 (`7f50eda`), elles ont été consolidées dans `docs/current/` ; les fichiers que le développeur connaît ne sont plus que des renvois. Le tableau ci-dessous dit où vit aujourd'hui le contenu de chacun.

## Carte des documents

### Où se trouve aujourd'hui chaque document de référence du 8 sept.

| Document au 8 sept. | Contenu aujourd'hui dans | Original intégral | État du fichier |
|---|---|---|---|
| `docs/specs/SPEC-domain-model.md` | DOMAIN (DOM-001…013, §Axes, §OBS) ; ALLOCATION (deux passes, statuts, ALLOC-001…025) ; COMPLIANCE (consolidation, CONF-001…029) ; ACCESS (casting, équipes) | archive | pointeur (12 l.) ; §5 verrou et §9 hiérarchie abandonnés |
| `docs/specs/SPEC-backend-requirements.md` | PLATFORM (PLAT-001…008, table FR1–29) ; AI (AI-001…014) ; OPEN-QUESTIONS | archive (avec ses User Stories) | pointeur |
| `docs/specs/SPEC-advanced-filters.md` | JOURNEYS §Interactions communes de table (UX-001…006) | archive | pointeur |
| `docs/specs/SPEC-configuration.md` | JOURNEYS (JRN-007), LIFECYCLE ; depuis : CAPTURE (réglages de conversion), TENDER-PROFILES (modèle), CUSTOM-COLUMNS, SPEC-risks §2.1 (stratégies), DEC-095 | archive (une ligne diffère du commit) | pointeur |
| `docs/specs/SPEC-dashboard.md` | JOURNEYS (JRN-007), PLATFORM (PLAT-008, DEC-098) | archive | pointeur |
| `docs/specs/SPEC-dashboard-statistics.md` | PLATFORM (PLAT-008), DEC-117/118, SPEC-risks §9 | archive | pointeur |
| `docs/specs/SPEC-followup.md` | COMPLIANCE (CONF-001…029), JOURNEYS (JRN-003), SPEC-compliance-decision-panel | archive | pointeur |
| `docs/specs/SPEC-home.md` | JOURNEYS (JRN-001), LIFECYCLE | archive | pointeur |
| `docs/specs/SPEC-project-creation.md` | LIFECYCLE (LIFE-001…003), JOURNEYS (JRN-001), TENDER-PROFILES | archive | pointeur |
| `docs/specs/SPEC-qa-screen.md` | QA (QA-001…010 ; DEC-116 remplace QA-002 et QA-007) | archive | pointeur |
| `docs/SPEC-qa-screen.md` (racine `docs/`) | QA | — | **copie identique laissée en place, périmée** |
| `docs/specs/SPEC-review-table.md` | ALLOCATION, JOURNEYS (JRN-002, UX-…) | archive | pointeur |
| `docs/specs/SPEC-team-management.md` | ACCESS (ACC-001…014), JOURNEYS (JRN-004) | archive | pointeur |
| `docs/specs/SPEC-translation.md` | LIFECYCLE §Langue, AI ; DEC-096 | archive | pointeur |
| `docs/specs/SPEC-versions-qa.md` | LIFECYCLE (LIFE-004…011), QA ; DEC-069…072, DEC-119, DEC-122 | archive | pointeur |
| `docs/specs/SPEC-expert-space.md` | COMPLIANCE et ACCESS (fusion de l'Expert Space dans Compliance) | **aucun** (git seulement) | **supprimé** |
| `docs/GLOSSARY.md` | DOMAIN + DEC de vocabulaire (029/030/045/054/060/074…) | archive | pointeur (5 l.) |
| `docs/decisions/DECISIONS.md` (D1–D15) | historique ; décisions courantes = OPEN-QUESTIONS DEC-001…125 | — | conservé, bandeau ajouté |
| `docs/tickets/TICKET-two-pass-allocation.md` | ALLOCATION, TENDER-PROFILES, DOMAIN §OBS (ordre corrigé ABS → PBS → OBS) | — | inchangé, historique |
| `docs/tickets/TICKET-merge-expert-space-into-compliance.md` | COMPLIANCE, ACCESS, DEC-030/031 | — | inchangé, historique |
| `docs/tickets/TICKET-vocabulary-alignment.md` | DOMAIN, DEC-029/030/033/045 | — | inchangé, historique |
| `docs/tickets/TICKET-casting-screen-redesign.md` (+ copie identique `docs/TICKET-casting-screen-redesign.md`) | ACCESS ; DEC-033/036/102/124 | — | inchangés, historiques |
| `docs/tickets/TICKET-tender-creation-rework.md` | LIFECYCLE (LIFE-001…003) ; DEC-049/095 | — | inchangé, historique |
| `docs/tickets/TICKET-three-support-screens.md` | JOURNEYS (Documents, Q&A, Casting) ; s'y ajoute Risks (`risks.html`) | — | inchangé, historique |
| `docs/tickets/TICKET-ai-uncertainty-display.md` | ALLOCATION (statuts, confiance) ; DEC-073 remplace son « To review » sur titres et informations ; DEC-120 | — | inchangé, historique |
| `docs/tickets/TICKETS-prototype-batch6.md`, `TICKETS-review-expert-batch4.md` | sources des tickets B/T cités dans le code | — | inchangés, historiques |
| `docs/archive/TICKETS-continuity-fixes.md` | — | — | + « Group H » (TH1–TH6, ouvert) |
| `docs/stories/README.md` | renvoie à `docs/current/` et à TASK-TEMPLATE ; les stories sont facultatives | — | réécrit (`7f50eda`) |
| `docs/DOC-HEALTH.md` | rapport de la routine « Keep specs current », non normatif | — | mis à jour 4 fois |
| `docs/research/*`, `docs/prompts/*`, `INVENTORY.md`, `CLEANUP-REPORT.md`, `SPEC-DERIVATION-REPORT.md`, `USER-TEST-session-3_2.md` | sources citées dans AUDIT / DOMAIN | — | inchangés |
| *(cité, jamais versionné)* `TICKETS-prototype-corrections-consolidated.md` | vague du 13 sept. (§1–§4) puis DEC-028…039 | — | **absent du dépôt** |

« archive » = `docs/archive/specs-2026-09-08/<même nom>` (copie de l'état sur disque le 8 sept., index dans son `README.md`). « pointeur » = fichier de 9 à 12 lignes renvoyant aux domaines de `docs/current/`.

### Documents nouveaux depuis le 8 sept.

| Fichier | Créé | Contenu |
|---|---|---|
| `docs/current/README.md` | 8 sept. | carte de lecture, autorité DEC > OBS > DOC > PROP > OPEN, périmètre pilote |
| `docs/current/DOMAIN.md` | 8 sept. | DOM-001…013, axes, rôles, OBS (DEC-054/055/062) |
| `docs/current/LIFECYCLE.md` | 8 sept. | création, documents, versions, traduction (LIFE-001…016) |
| `docs/current/ALLOCATION.md` | 8 sept. | ALLOC-001…025, relances, clés, une allocation par organisation |
| `docs/current/COMPLIANCE.md` | 8 sept. | CONF-001…029, transitions, scénarios |
| `docs/current/ACCESS.md` | 8 sept. | ACC-001…014, matrice des droits |
| `docs/current/QA.md` | 8 sept. | QA-001…010 |
| `docs/current/AI.md` | 8 sept. | frontière IA, AI-001…014 |
| `docs/current/TENDER-PROFILES.md` | 8 sept. | Turnkey / SIG / Mainline / RSC, TYPE-T01…T11, tender SIG de démo |
| `docs/current/PLATFORM.md` | 8 sept. | PLAT-001…008, table FR1–29, DEC-090, DEC-098 |
| `docs/current/JOURNEYS.md` | 8 sept. | JRN-001…007, UX-001…006 |
| `docs/current/OPEN-QUESTIONS.md` | 8 sept. | DEC-001…125, OPEN-01…15, points ouverts |
| `docs/current/AUDIT.md` | 8 sept. | traçabilité de la consolidation |
| `docs/current/TASK-TEMPLATE.md` | 8 sept. | modèle de tâche pour agent |
| `docs/current/KEYS.md` | 21 sept. | classeur PBS/OBS/ABS (DEC-061/062), KEY-T01…05 |
| `docs/current/CAPTURE.md` | 22 sept. | réglages de conversion du document source |
| `docs/current/CUSTOM-COLUMNS.md` | 23 sept. | colonnes personnalisées, CUST-T01…12 |
| `docs/specs/SPEC-custom-columns.md` | 23 sept. | pointeur vers CUSTOM-COLUMNS |
| `docs/specs/SPEC-compliance-decision-panel.md` | 24 sept. | panneau de décision du contributeur (DEC-079…081) |
| `docs/specs/SPEC-external-partners.md` | 24 sept. | partenaires externes Turnkey (DEC-082/093) |
| `docs/specs/SPEC-risks.md` | 30 sept. | stratégies d'écart, risques, conformité externe (DEC-105…114) |
| `docs/specs/SPEC-document-view.md` | 30 sept. | vue Document sur le PDF original, prototype autonome (non implémenté ici) |
| `docs/archive/specs-2026-09-08/` (16 fichiers) | 8 sept. | README + GLOSSARY + 14 specs d'origine |
| `docs/stories/STORIES-extracted-from-prototype.md` | 17 sept. | backlog de user stories extrait du prototype (hors périmètre) |
| `fonts/README.md` (racine du dépôt) | 22 sept., révisé 6 oct. | polices de marque, licence, build des WOFF |

# Partie 2 — Socle : organisation, modèle métier, plateforme, charte

Périmètre : organisation documentaire et autorité, modèle métier et vocabulaire, exigences transverses (plateforme, notifications, métriques, journal, clavier), charte graphique. Les règles propres à chaque écran (Allocation, Compliance, Q&A, Documents, Dashboard, Création, Risks) sont traitées dans les autres parties ; on y renvoie par ID. La carte des documents est en partie 1.


## 1. Organisation documentaire et autorité

Où lire aujourd'hui : `docs/current/README.md` (§Lecture et autorité, §Carte de lecture, §Périmètre), `docs/current/OPEN-QUESTIONS.md` (registre DEC, suivi OPEN, « Ne pas redemander »), `docs/current/TASK-TEMPLATE.md`, `docs/current/AUDIT.md` — au 8 sept. : `docs/specs/SPEC-*.md` (15 fichiers), `docs/SPEC-qa-screen.md`, `docs/GLOSSARY.md`, `docs/decisions/DECISIONS.md` (D1–D15), `docs/tickets/*.md`

### Nouveau
- (R) **Une référence unique : `docs/current/`** — 17 fichiers par domaine, en français. 14 créés le 8 sept. à 16:43, après la base (`7f50eda`) ; puis `KEYS.md` (21 sept., `132eef3`), `CAPTURE.md` (22 sept., `b2ac7af`), `CUSTOM-COLUMNS.md` (23 sept., `9f677cf`). Les anciennes `docs/specs/SPEC-*.md` deviennent des points d'entrée de 9 à 12 lignes ; les originaux sont copiés dans `docs/archive/specs-2026-09-08/`.
- (R) **Statut de preuve sur chaque énoncé** — **DEC** (décision utilisateur, référence d'implémentation), **OBS** (constat dans le code, non validé métier), **DOC** (intention écrite, pas une preuve d'implémentation), **PROP** (proposition à valider), **OPEN** (à arbitrer, ne pas inventer). Une DEC prime sur un OBS contradictoire, même si le prototype n'est pas encore corrigé. Un OBS n'autorise pas à reproduire un défaut de démonstration. Les anciens prompts et tickets sont des sources historiques, pas des instructions. (README §Lecture et autorité)
- (R) **Identifiants de règle stables** — `DOM-`, `LIFE-`, `ALLOC-`, `CONF-`, `ACC-`, `QA-`, `AI-`, `PLAT-`, `JRN-`, `UX-`, avec des critères d'acceptation en `-Txx` (`TYPE-T`, `KEY-T`, `CUST-T`…). On cite l'ID sans recopier la définition, un numéro n'est jamais réattribué, et les anciennes ancres de section (§x.y) ne se citent plus dans les tâches. (TASK-TEMPLATE §Maintenance ; pointeurs `docs/specs/*`)
- (R) **Registre DEC-001 → DEC-125** (OPEN-QUESTIONS §Décisions consolidées) — DEC-001…026 dès le 8 sept. ; DEC-027…125 ajoutées du 17 sept. au 9 oct. La précision la plus récente remplace l'antérieure. Remplacements explicites : DEC-026→015, DEC-031→001 (DEC-024 sans objet), DEC-045→vocabulaire de DEC-033, DEC-056→granularité de DEC-040, DEC-060→057, DEC-087→010, DEC-089→051 (partiel), DEC-106→028, DEC-113 annule fermeture/fusion de DEC-111, DEC-118→« par personne » de DEC-117. DEC-058/059 sont des **déductions** à confirmer. Une section « Ne pas redemander » fige l'échelle des verdicts, le droit de lecture, le casting, DEC-029/030/033/035/036/087.
- (R) **Modèle de tâche pour agent** (`TASK-TEMPLATE.md`) — objectif, parcours `JRN` et variante de tender, règles par ID, OPEN préalables résolus, périmètre, contrat technique, acceptation, vérification, livraison. Exemple : valider l'allocation SIG sans responsable (JRN-002, ALLOC-003/007/010/011, ACC-007).
- (R) **Parcours JRN-001…JRN-007** (`JOURNEYS.md`) — décrivent les enchaînements entre écrans :
  - JRN-001 créer / reprendre un tender ;
  - JRN-002 corriger / valider l'allocation ;
  - JRN-003 répondre à la conformité ;
  - JRN-004 maintenir le casting ;
  - JRN-005 ajouter / remplacer un document ;
  - JRN-006 traiter les questions client ;
  - JRN-007 piloter / configurer.
  Leurs scénarios sont des **critères de recette**, pas un compte rendu de recette. Sont aussi exigés (PROP) les états de production à concevoir pour chaque parcours : chargement réel, aucun résultat, échec récupérable, absence de droit, traitement partiel, conflit d'édition.
- (R) **Périmètre du premier pilote** — de la création jusqu'à la validation de l'allocation, pour Turnkey, SIG, Mainline et RSC (DEC-022). Conformité, versions et Q&A sont décrits mais ne sont pas des livrables du premier parcours. REX et Chat hors V1 (DEC-021). Cible : 100 000 lignes et 10 utilisateurs simultanés (DEC-023).
- (R) **Variantes de tender obligatoires** — chaque parcours se décline Turnkey / SIG / Mainline / RSC ; « un tender SIG autonome n'est pas un Turnkey filtré ». (TENDER-PROFILES ; DOMAIN §Applicabilité ; JOURNEYS §Applicabilité obligatoire)
- (R) **Nouvelles specs détaillées dans `docs/specs/`**, en anglais : `SPEC-compliance-decision-panel.md` (24 sept., DEC-079), `SPEC-external-partners.md` (24 sept., DEC-082), `SPEC-risks.md` (30 sept., DEC-105…114), `SPEC-custom-columns.md` (pointeur vers CUSTOM-COLUMNS) et `SPEC-document-view.md` (30 sept., prototype autonome sur PDF ; aucune trace de pdf.js dans les écrans, donc non implémenté ici — déduit). Les DEC qui arbitrent ces specs priment sur leur texte.
- (P) **`AUDIT.md`** — trace de la consolidation : HEAD inspecté `3ef09ba` (antérieur à la base), tableau « constat → preuve dans le code », limites (aucun test navigateur). Ses constats (« Sept écrans », « deux verdicts et R&D en commentaire ») décrivent le 8 sept., pas l'état actuel.
- (P) **`docs/stories/STORIES-extracted-from-prototype.md`** (17 sept., `a6aeb84`, 798 l.) — backlog de user stories extrait d'une lecture du prototype (7 écrans + shell) : 10 zones, plus placeholders, ambiguïtés et incohérences de nommage, avec le vocabulaire d'origine non corrigé (« activity » = système). C'est la relecture d'où sont sorties DEC-028…039. **Hors périmètre ici** ; `docs/stories/README.md` rappelle que les règles et les critères font autorité, pas les stories.

### Modifié
- (R) **Où vivent les décisions** — Avant : `DECISIONS.md` (D1–D15, en anglais, append-only) et des notes « Correction (date) » dans chaque spec → Maintenant : `DECISIONS.md` gelé avec un bandeau « historique antérieur à la consolidation » ; décisions dans OPEN-QUESTIONS (DEC-xxx) ; règles dans le fichier du domaine. (`7f50eda`)
- (R) **Glossaire** — Avant : `docs/GLOSSARY.md` (88 l., termes renommés, termes ouverts) → Maintenant : pointeur de 5 lignes vers DOMAIN.md et OPEN-QUESTIONS ; l'original est archivé (voir §2).
- (R) **Specs d'écran** — Avant : une spec par écran, source de vérité → Maintenant : pointeurs vers des fichiers par règle métier (domaines) et par parcours (JOURNEYS). Le découpage n'est plus calqué sur les écrans.
- (P) **`README.md` / `HANDOVER.md` racine** — bandeau vers `docs/current/` ajouté ; corps historique conservé. Le README décrit encore 6 sources dont `suivi-experts-et-versions.html` et `expert-space.html`.
- (R) **`CLAUDE.md`** — l'échelle de jetons suivie gagne `--font-heading` et `--brand-red` (`dd816be`).

### Retiré / abandonné
- (X) **`docs/specs/SPEC-expert-space.md`** — supprimé : il s'agissait d'une suppression locale préexistante, commitée par `7f50eda`. **Non archivé**, récupérable seulement par `git show 5e7ae6b:docs/specs/SPEC-expert-space.md`. L'Expert Space est fusionné dans Compliance (TICKET-merge-expert-space-into-compliance).
- (X) **Notes de correction datées dans les specs** (« Correction (2026-09-04)… ») — plus maintenues : la règle courante est dans le registre et le fichier de domaine.

### Toujours ouvert
- **OPEN restant ouverts** : OPEN-06 (cycles Q&A multiples), OPEN-08 (budgets chronométrés, jeu de 100 000 lignes), OPEN-10 (formats, contrats, PDF entièrement image), OPEN-11 (sécurité, rétention, notifications détaillées), OPEN-12 (connecteur DOORS direct, date du pilote), OPEN-13 (libellés exacts, filtres multi-pages), OPEN-15 (particularités Mainline/RSC à ne pas inventer depuis SIG).
- **Incohérences constatées dans la référence** (la DEC la plus récente prime) :
  - `docs/current/README.md` : « Sept sources actives » alors qu'il y en a huit depuis `risks.html` ; « DEC-001 à DEC-027 figurent dans le registre » alors qu'il va jusqu'à DEC-125. La carte de lecture n'indexe ni SPEC-risks, ni SPEC-external-partners, ni SPEC-compliance-decision-panel, ni SPEC-document-view.
  - `DOMAIN.md` §Axes : « trois valeurs internes, deux à l'export (DEC-001) … R&D → Compliant (DEC-024) », remplacé par DEC-031. DOM-009 « un verrou peut les rendre différents » : le verrou a disparu (DEC-028/039, puis DEC-106).
  - `PLATFORM.md` : la ligne FR 5–6 cite encore « échelle interne DEC-001 et conversion DEC-024 » ; §Borne de pilote parle de « responsable facultatif unique » alors que DEC-087 remplace DEC-010.
  - `JOURNEYS.md` : JRN-003 « tableau et détail Document » (onglet Document retiré de Compliance, DEC-078) ; JRN-005 « comparaison » (mode Compare supprimé, DEC-119) et « suppression manuelle » (interdite pour un bloc capturé, DEC-094) ; JRN-006 « le PM importe et arbitre les associations » (plus de file d'arbitrage, DEC-116).
  - `OPEN-QUESTIONS.md` §Suivi : OPEN-01 renvoie à la « déclaration externe (DEC-028) », remplacée par DEC-106. OPEN-04 dit que Category « qualifie chaque Not Compliant », alors qu'elle ne vaut que pour Turnkey (DEC-107). §Autorité dit encore « Le prototype n'est pas modifié dans cette tâche ».
  - `docs/SPEC-qa-screen.md` et `docs/TICKET-casting-screen-redesign.md` (racine de `docs/`) : copies identiques des anciennes versions, ni archivées ni converties en pointeurs. À ne pas lire comme courantes (QA.md + DEC-116 ; ACCESS.md).
  - L'archive n'est pas strictement la version commitée. `SPEC-configuration.md` archivé diffère d'une ligne (mention Expert Space retirée). `docs/archive/TICKETS-continuity-fixes.md` a gagné un « Group H » (TH1–TH6, audit de densité verticale, ouvert), issu de modifications locales antérieures commitées par `7f50eda`.
  - La source de la vague du 13 sept. (§1–§4 des commits `2dd1fb4`…`8e83ca8`), `TICKETS-prototype-corrections-consolidated.md`, est citée dans `build_merge.py` mais **absente du dépôt**.
  - Le **journal d'activité par exigence** (`7a1d771`) n'a aucune règle écrite (voir §3).
  - `COMPONENTS.md` avait perdu son titre `## Removed` (`86dbb39`) ; rétabli le 9 oct. (`70a0d23`).

### Synthèse
- Tout ce que le dev a lu au 8 sept. dans `docs/specs/` est archivé ; les fichiers du même nom ne sont plus que des pointeurs. Lire `docs/current/README.md`, puis le fichier du domaine, puis OPEN-QUESTIONS.
- 125 DEC numérotées remplacent les 15 D ; ~100 datent d'après le 8 sept. **Une DEC récente l'emporte sur tout texte**, y compris sur des pages de `docs/current/` restées en retard (liste ci-dessus).
- Citer les règles par ID (ALLOC-0xx, CONF-0xx…), jamais par ancre de section historique.
- Le pilote s'arrête à la validation de l'allocation, pour quatre types de tender.


## 2. Modèle métier, vocabulaire et rôles

Où lire aujourd'hui : `docs/current/DOMAIN.md` (DOM-001…013, §Axes, §Vocabulaire de rôles, §OBS), `OPEN-QUESTIONS.md` (DEC-029/030/032…034/045…049/054/055/058…060/062/074/077/087), `TENDER-PROFILES.md` §Systèmes, produits et modèles, `ACCESS.md` (ACC-001…014) — au 8 sept. : `docs/specs/SPEC-domain-model.md`, `docs/GLOSSARY.md`, `docs/tickets/TICKET-vocabulary-alignment.md`, `TICKET-two-pass-allocation.md`

### Nouveau
- (R) **Objets fonctionnels DOM-001…DOM-013** — projet/tender, document/version, élément capturé (identifiant stable lors d'un changement de type), exigence, branche de système, affectation d'équipe, proposition IA (sa confiance n'est pas une validation), réponse, verdict dérivé/final, question/réponse client, événement d'audit (DOC, pas de stockage réel dans le prototype). DOM-012/013 (PROP) : relier l'exigence à son document, sa version et son passage source ; garder séparément proposition IA, valeur retenue et événement de correction, pour qu'une relance n'efface pas une décision humaine.
- (R) **Système / sous-système** (DEC-045, DEC-046) — « activity » devient **système** dans tout ce que lit l'utilisateur. La liste de référence est celle de la capture (16 codes de la colonne *Responsible Entity*, DEC-032). Un tender n'est émis que sur un seul système ; l'allocation Turnkey répartit vers des sous-systèmes. DEC-058 (déduction) : toute la liste est de niveau sous-système ; les systèmes sont les types de tender ; SIG et RSC existent aux deux niveaux, ce qui explique qu'eux seuls portent un modèle.
- (R) **Produit** (DEC-047…049, DEC-061) — chaque système a ses produits, et le produit sélectionne le modèle d'allocation. SIG : Urban, Mainline Wayside, Mainline Onboard. Le type « Mainline » de DEC-004 est un tender SIG de produit Mainline. Turnkey porte une **combinaison** nommée de produits (matrice à fournir). Le produit est figé à la création ; le modèle qui en découle reste réglable dans les paramètres.
- (R) **OBS = organisation, jamais une personne** (DEC-054) — trois granularités du même axe : **TK OBS** (système/sous-système, passe 1 Turnkey), **OBS · team** (équipe, passe 2), **OBS · role** (poste avec codes Skills/SoA/Job, modèle Mainline sur les clés, DEC-062). La personne vient après, séparément : en général le responsable de l'équipe dans la région du tender.
- (R) **Allocation = organisation + sa personne** (DEC-060, remplace le bloc d'affectations séparé de DEC-057). ABS et PBS sont **uniques** par exigence, l'OBS est **multiple** (DEC-055). On fait autant d'allocations qu'il y a d'organisations, et chacune porte sa personne et son verdict, consolidés au niveau exigence (DEC-037, le plus restrictif gagne).
- (R) **Nature** (DEC-074, précise DEC-062) — Information / Heading / Requirement, rien d'autre, et elle n'apparaît pas dans la table. La **classe** technique / non technique s'affiche dans le détail de toute exigence, SIG compris. Le **PBS** est un élément produit (DEC-062).
- (R) **Responsabilité portée par la personne de chaque OBS** (DEC-087, remplace DEC-010) — elle répond, et c'est elle qu'on relance. Il n'y a pas de responsable de suivi global ; plusieurs personnes dans un périmètre font plusieurs entrées OBS. L'absence de personne ne bloque pas la validation (DEC-025).
- (R) **Nouveaux termes métier** (définis dans les domaines concernés) : stratégie d'écart et conformité externe dérivée (DEC-105/106/110), risque `RSK-` rattaché au tender (DEC-113/114), partenaire externe Turnkey (DEC-082), colonne personnalisée (DEC-064…068, DEC-097), mise de côté / *Set aside* (DEC-079/090), question client To send / Sent / Answered (DEC-116), colonne **Changes** (DEC-119), niveau de confiance Low / Medium / High (DEC-120).
- (R) **Rôles et droits transverses** (détail : ACCESS.md) — l'équipe de gestion projet valide (DEC-009 ; plusieurs PM, ACC-001/002). Un contributeur lit tout le projet et ne modifie que son système (DEC-012). Il ne change ni la nature ni la classe (DEC-086) et ne modifie rien sur une exigence sans système à lui (DEC-100). Une personne appartient à un seul système (DEC-102). Un système n'a pas besoin de manager (DEC-124).

### Modifié
- (R) **« Activity » / « typology »** — Avant : *Activity* (remplaçant *typology*) = dimension de routage, imbriquable → Maintenant : **système** (DEC-045). « activity » ne désigne plus que l'ABS (*Activity Breakdown Structure*). Les identifiants de code gardent l'ancien mot (`CAST_ACTIVITIES`, `activityId`, `deriveActivityCompliance`, champ `typology`), volontairement non renommés (`d72a2a9`).
- (R) **« Allocated activity » (ex-*branch*)** — Avant : unité d'affectation avec manager + expert (SPEC-domain-model §1), ou un contributeur selon le glossaire après la fusion du 28 août → Maintenant : branche de système (DOM-005) et une allocation organisation + personne par OBS (DOM-006, DEC-060). **Une seule personne assignée** par système ou OBS, jamais un manager et un expert concurrents (`326291b`, `b932fb4`, 10 sept.).
- (R) **Noms des étapes** (DEC-029) — Avant : « Requirements review » / « Document review », « Expert Review », « Follow-up », « qualification » → Maintenant : **Allocation** et **Compliance**, qui tournent en parallèle (DEC-035).
- (R) **Rôles** (DEC-030) — Avant : glossaire « Contributor » mais modèle manager + expert ; FR24 à cinq rôles (PM, Requirement Manager limité SIG/RSC, Expert Reviewer, Admin, VIP) → Maintenant : équipe PM + **Contributor** pour qui répond. « Activity manager » était réservé à qui gère le casting d'un système, puis aucun manager n'est requis (DEC-124). Admin/VIP non détaillés pour le pilote (OPEN-02).
- (R) **Chaîne de dérivation** — Avant : **PBS → ABS → OBS** (glossaire, SPEC-domain-model §3.2) → Maintenant : **ABS → PBS → OBS → personne** (DEC-008, ALLOC-003), sans distinction technique / non technique pour SIG.
- (R) **Échelle de conformité** — Avant : contradiction entre le glossaire (2 valeurs, R&D en texte) et SPEC-domain-model §3/§9.2 (3 valeurs `compliant` / `rnd_needed` / `not_compliant`) → DEC-001 (3 internes, 2 à l'export) → Maintenant : **2 verdicts**, Compliant / Not compliant ; « R&D needed » est une mention portée par un Compliant (DEC-031). Ce qui part au client est la **conformité externe dérivée par système** (DEC-106).
- (R) **Statuts d'avancement** — Avant : Incomplete → To review → To validate → Allocated (SPEC-domain-model §8.2) → Maintenant : mêmes libellés, mais jamais sur un titre ou un bloc d'information (DEC-073). Pas d'« Awaiting manual allocation » : il manque des données, donc Incomplete (DEC-103). Nouveau statut « Reassignment requested » (DEC-104). Une seule validation par exigence (DEC-099). Détail : ALLOCATION.md.
- (R) **Types de tender** — Avant : *product line* libre (Signalling & Urban, Rolling stock, Services, Systems ; Turnkey vu comme une valeur d'activité) → Maintenant : Turnkey, SIG, Mainline (= produit SIG), RSC (DEC-004/047). L'orthographe « RCS » est corrigée en **RSC** (DEC-059).
- (R) **Nature vs Type** — Avant : renommage Nature → Type **bloqué** (collision avec le champ Type Functional / Interface / Performance / Security) → Maintenant : tranché par DEC-074 ; les valeurs Functional… quittent Allocation (table, détail, filtres, action groupée).
- (R) **TK OBS** — Avant : colonne « TK OBS » distincte (activité de passe 1) → Maintenant : concept documenté de la passe 1, **affiché dans la colonne System** (DEC-077, précise DEC-034).

### Retiré / abandonné
- (X) **Hiérarchie d'activités imbriquées** (droits hérités, `descendantsOf()`, SPEC-domain-model §9, D7) — « pas de hiérarchie interne » (DEC-012) ; elle a disparu avec l'Expert Space.
- (X) **Rôles in-tool Expert, Activity Manager, Expert Reviewer** — un seul rôle, Contributor (DEC-030) ; plus d'« Expert Space ».
- (X) **Responsable de suivi unique par exigence** (DEC-010) — remplacé par DEC-087.
- (X) **Verrou/déverrouillage du verdict final par le PM** (SPEC-domain-model §5, D6) — supprimé (DEC-028, puis DEC-106 : le PM corrige la conformité externe, motif obligatoire).
- (X) **« R&D Needed » comme verdict** (D8, SPEC-domain-model §9.2) — DEC-031.
- (X) **Mot « typology »** (DEC-033).

### Toujours ouvert
- **Légende des 16 codes** (DEC-032) : le libellé égale le code ; il faut la légende métier.
- **RST vs RSC** : DEC-059 ne règle que l'orthographe ; le rapport entre les deux codes reste à établir.
- **DEC-058 / DEC-059** : déductions, à confirmer par l'utilisateur.
- **Matrice des combinaisons Turnkey** (DEC-048) et liste réelle des produits par système.
- **Maille de l'OBS pour Urban** : DEC-062 n'en dit rien ; Urban garde la maille équipe.
- **Valeurs de Category** : placeholder explicite (DEC-038, OPEN-04), Turnkey seulement (DEC-107).
- **Libellés exacts des états** (OPEN-13). Les termes laissés ouverts par l'ancien glossaire (Casting, Class, Reassignment, Tender vs RFP) ne sont tranchés par aucune DEC (déduit).

### Synthèse
- « Activity » ne veut plus dire ce qu'il voulait dire : côté utilisateur, c'est **système** ; « activity » = ABS. Le code garde `typology` / `activity`.
- **OBS = organisation**, et une allocation = organisation + personne. ABS/PBS sont uniques par exigence, l'OBS multiple. La chaîne est **ABS → PBS → OBS → personne**.
- **Deux verdicts internes** ; le client reçoit la conformité externe dérivée. Plus de verrou ni de R&D comme valeur.
- **Une seule personne par allocation, responsable de sa conformité** ; plus de duo manager/expert ni de responsable de suivi global.
- Nature = Information / Heading / Requirement ; produit et ligne produit figés à la création.


## 3. Exigences transverses : plateforme, notifications, métriques, journal, clavier

Où lire aujourd'hui : `docs/current/PLATFORM.md` (PLAT-001…008, §Correspondance avec les 29 FR, §État personnel, §Carte Allocation), `DOMAIN.md` (DOM-011…013), `JOURNEYS.md` (UX-001…006), `AI.md` (AI-009), `OPEN-QUESTIONS.md` (DEC-023, DEC-085, DEC-090, DEC-098, DEC-117, DEC-118) — au 8 sept. : `docs/specs/SPEC-backend-requirements.md` (FR1–FR29), `SPEC-dashboard-statistics.md`, `SPEC-advanced-filters.md`

### Nouveau
- (R) **Stack cible** : React côté front, Azure côté back ; services, frameworks et schémas d'API non approuvés (PLATFORM, intro).
- (R) **PLAT-001…005** (DOC) :
  - persistance de tous les objets et états ;
  - SSO et droits projet/système contrôlés **côté serveur**, y compris pour les requêtes directes, compteurs, recherche et exports ; lecture de tous les systèmes du projet (DEC-012) ;
  - audit humain/machine avec identité, date, avant/après, et traçabilité IA avec coût (suivi de session et rétention : OPEN-11) ;
  - DOORS 9/NG et Excel ; les menus CSV/ReqIF du prototype ne prouvent pas une intégration ;
  - notifications in-app et email, déclencheurs non finalisés ; l'envoi Q&A au client reste hors outil (QA-003).
- (R) **Règle des notifications** (PLATFORM, introduite par `b3a195d`) — une cloche se calcule depuis l'état réel de l'écran. Elle résume **par nature avec un compte** (jamais une ligne par affectation), nomme l'exigence quand il n'y en a qu'une, et dit explicitement quand rien n'attend le lecteur. Pas de cloche inerte.
- (R) **Métriques PLAT-008 refondues** (DEC-117/118) :
  - profil de conformité = ce que le client recevra ;
  - exigences ouvertes rangées dans **une seule** file : réallocation → client → contributeur (en retard au-delà de 5 jours) → non affectée ;
  - trajectoire avec projection « à ce rythme » sur 7 jours, jamais présentée comme un plan ;
  - activité de la semaine et réponses **par système / sous-système, jamais par personne** (motif : CSE, Betriebsrat, RGPD) ;
  - réallocations par motif ;
  - corrections IA **hors** tableau de bord (Configuration › AI feedback) ;
  - toute métrique annonce son unité ; aucun indicateur composite sans définition métier.
- (R) **État personnel côté serveur** (DEC-090) — brouillons de verdict et mises de côté : privés à leur auteur, persistants d'un poste à l'autre, hors compteurs et exports. Le prototype ne les garde que dans la session.
- (R) **Carte Allocation du dashboard** (DEC-098) — passe à Done quand toutes les exigences sont allouées, redevient Current dès qu'une ne l'est plus. L'état se lit sur les données, jamais sur un clic : plus de jalon Finalize (DEC-084, DEC-035).
- (R) **Clavier et annulation, Allocation et Compliance** (DEC-085) :
  - sélection et navigation : X, Maj+↑/↓ (ou J/K), ⌘/Ctrl+A sur ce que les filtres montrent, Échap, V (valider), N (prochaine exigence qui attend) ;
  - **⌘/Ctrl+Z** annule la dernière action annulable, même après la disparition du toast ;
  - les champs texte gardent leur comportement natif ;
  - aide affichée au survol (`5ba326f`) ;
  - touches ajoutées depuis : C (colonne Changes, DEC-119), Q (question client, refusée après verdict, DEC-121), R (relance, DEC-125).
- (R) **Interactions de table communes** UX-001…006 :
  - multi-sélection, actions groupées, navigation clavier, colonnes masquables et réordonnables ;
  - filtres par colonne ; filtre avancé AND/OR à un seul niveau de groupe ;
  - filtres nommés personnels ; filtrage sur tout le jeu autorisé ;
  - composition de « Filter to Selection » : OPEN-13.
  - Colonnes redimensionnables ajoutées sans DEC (`aac89b1`).
- (P) **Journal d'activité par exigence** (`7a1d771`, 1ᵉʳ oct.) — un journal commun à Allocation et Compliance : qui, quand, avant → après, avec les jalons *Captured*, *Allocated*, *Answered*, *Declared to the client*. Il est lu par les onglets Activity et par le classement hebdomadaire du dashboard (DEC-117). **Aucune règle écrite** au-delà de DOM-011 / PLAT-003 : contenu, périmètre et rétention sont à spécifier avant de le reproduire.

### Modifié
- (R) **Dimensionnement** — Avant : FR21 10 000 utilisateurs, 30 000 exigences par déploiement (≈ 5 000 par projet) → Maintenant : **100 000 lignes** par tableau (titres et informations compris), **10 utilisateurs simultanés** (DEC-023, PLAT-006).
- (R) **Performance** — Avant : FR8 P95 ≤ 300 ms, FR9 < 3 s pour 10 000 lignes → Maintenant : références historiques, **pas de SLA confirmé à 100 000 lignes** ; budgets à définir (PLAT-007, OPEN-08).
- (R) **Rôles d'accès** — Avant : FR24 à cinq rôles → Maintenant : équipe PM et Contributor par système ; Admin et VIP non détaillés (ACC-001…014, OPEN-02).
- (R) **Mode de traitement** — Avant : FR4 manuel / IA choisi à la création → Maintenant : confirmé et étendu ; ligne produit et mode IA figés (DEC-095), produit figé (DEC-049). Se tromper oblige à recréer le tender.
- (R) **Verrous** — Avant : FR5 verrou d'édition concurrente confondu avec le verrou métier du PM → Maintenant : distinguer verrou métier et protection de concurrence (COMPLIANCE §Production) ; le verrou métier du verdict final n'existe plus (DEC-028/106). « Enregistrement concurrent sans perte silencieuse » est un test de production à préparer (PROP).
- (R) **Suppression d'exigence** — Avant : FR3 création, modification et suppression → Maintenant : pas de suppression manuelle d'un bloc capturé, on le reclasse en Information (DEC-094). Seules les lignes dupliquées depuis une image restent supprimables.
- (R) **Confiance IA** — Avant : FR13 un score par exigence → Maintenant : caractérisation (nature, classe) en **Low / Medium / High** ; routage Turnkey et ABS/PBS/OBS gardent leurs pourcentages (DEC-120).
- (R) **« Pipeline sans intervention »** — Avant : critère de succès → Maintenant : n'enlève pas les validations humaines (AI-009).
- (R) **Statistiques** — Avant : deux publics dans SPEC-dashboard-statistics, le PM (goulots par périmètre, profil de conformité, blocage client, casting, travail invalidé, trajectoire) et les VIP (comparaison entre tenders : santé composite §2.1, fiabilité IA par taux de correction §2.4) → Maintenant : statistiques du tender, métier seulement, sans mesure nominative (DEC-117/118). La vue VIP comparative n'est pas reprise (VIP non détaillé, OPEN-02).
- (R) **User stories du backend** — Avant : section « User Stories » de SPEC-backend → Maintenant : archivées ; les stories sont facultatives (`docs/stories/README.md`).

### Retiré / abandonné
- (X) **Indicateur composite de santé** (`health` / `healthNote`, « on track / at risk ») — retiré du modèle de projet (`2dd1fb4`, 13 sept.) ; PLATFORM refuse tout composite sans définition métier.
- (X) **Mesures IA et classement nominatif dans le dashboard** (DEC-117, DEC-118).
- (X) **Hypothèse 10 000 utilisateurs / 30 000 exigences** (DEC-023).

### Toujours ouvert
- OPEN-08 (budgets, protocole du test de charge), OPEN-10 (contrats d'échange), OPEN-11 (sécurité, rétention, déclencheurs et destinataires des notifications), OPEN-12 (connecteur DOORS direct), OPEN-13 (filtres multi-pages).
- Journal d'activité : événements, rétention, droits de lecture (non spécifiés).
- Persistance de l'annulation : DEC-085 décrit le geste, pas sa portée côté serveur (déduit).

### Synthèse
- Dimensionner pour **100 000 lignes et 10 utilisateurs simultanés** ; aucune cible de latence n'est validée.
- **Droits contrôlés côté serveur** jusque dans les compteurs, la recherche et les exports ; brouillons et mises de côté privés côté serveur.
- **Aucune statistique ne mesure une personne** ; les mesures de l'IA quittent le dashboard.
- Les notifications se calculent et se résument ; les raccourcis clavier et ⌘/Ctrl+Z font partie du comportement attendu.
- Le journal d'activité existe dans le prototype sans spec : à cadrer avant de l'implémenter.


## 4. Charte graphique et marque

Où lire aujourd'hui : `OPEN-QUESTIONS.md` (DEC-063, DEC-115), `fonts/README.md`, `CLAUDE.md` (échelle de jetons suivie), `COMPONENTS.md` (Brand Logo, Page Title, Icon) — au 8 sept. : aucune spec (seulement `docs/prompts/PROMPT-design-tokens.md` et `docs/archive/PROMPT-brand-colors.md`, historiques)

### Nouveau
- (R) **Typographie** (DEC-063, 22 sept., puis DEC-115, 6 oct.) :
  - la police de la marque, Alstom, sert à tout le texte d'interface, chiffres, identifiants et codes (chasse fixe des chiffres) ;
  - **Antarctica** pour les titres, quand ses fichiers seront fournis ;
  - **Noto Sans** est la police de repli, calée sur les mêmes métriques (même mise en page) ;
  - **Georgia** reste la police du document source (le papier se distingue de l'interface) ;
  - pas de SemiBold ni d'italique dans la famille ; jamais `local()` (bitmaps des TTF installés).
- (R) **Licence de la police** (DEC-115) — non diffusée dans la version publique (`index.html`, GitHub Pages) tant que la licence n'est pas établie ; seulement dans la version locale et les captures.
- (R) **Couleurs** (DEC-063) — accent = bleu marine **#0B294A** en thème clair. Le **rouge** est décoratif seulement (marque devant les titres h1/h2), **jamais sur un élément cliquable ou porteur d'état**, parce qu'il signifie « non conforme ». Rouge exact à confirmer (#E4002B provisoire).
- (R) **Vert/rouge réservés au verdict** sur Compliance ; les statuts d'avancement sont recolorés (`10821d4`, 14 sept.). Détail dans l'analyse Compliance.
- (R) **Logo dans l'en-tête de chaque écran** (`575fbbe`, 9 oct., sans DEC) — logo de l'entreprise en couleur sur clair, en blanc sur sombre, un filet, puis « SRM » en texte. La marque SRM devient le seul favicon.
- (R) **Un seul jeu d'icônes SVG au trait** (24 px, trait de 2 px) à la place des emoji et des glyphes absents (`49ae3a3`, 24 sept.).
- (P) **Couleurs de la page d'accueil** (`4953fea`) — bleu de marque secondaire et ardoise, page d'accueil seulement ; rôle PM en marine, contributeur en bleu ; badges de ligne produit Turnkey marine, SIG bleu, autres ardoise.

### Modifié
- (R) **Police** — Avant : Inter / police système → Maintenant : Alstom (version locale) ou Noto Sans (version publiée).
- (R) **Accent** — Avant : #0050E3 (clair) → Maintenant : #0B294A. En thème sombre, les surfaces passent dans la famille marine et l'accent #4C82FF reste.
- (P) **Favicon** — Avant : marque à trois lobes, variantes clair/sombre → Maintenant : marque « 02 Fan Ribbons », un seul fichier.
- (P) **Pastilles de statut** — sans point initial (`73efa97`).

### Retiré / abandonné
- (X) Point rouge sur le logo (essayé, retiré le 23 sept., `4bedc2a`).
- (X) Barre supérieure marine dans les deux thèmes (`a79114e`, annulée le jour même par `4341e56`).
- (X) Marque SRM dans l'en-tête (remplacée par le logo de l'entreprise).

### Toujours ouvert
- Rouge exact de la marque ; fichiers Antarctica ; autorisation de diffuser la police.
- Liens texte de la même couleur que le corps en thème clair : compromis signalé dans `dd816be`, sans décision.

### Synthèse
- Police Alstom avec repli Noto Sans calé sur les mêmes métriques ; Georgia pour le document source. **Ne pas publier la police.**
- Accent marine ; **le rouge ne porte jamais d'état ni d'action** ; vert/rouge réservés au verdict.
- Logo de l'entreprise obligatoire dans l'en-tête ; icônes SVG, pas d'emoji.


# Partie 3 — Allocation

## Allocation — sources et autorité (lire d'abord)
Où lire aujourd'hui : `docs/current/README.md` (autorité DEC > OBS > DOC…), `docs/current/ALLOCATION.md` (ALLOC-001 à ALLOC-025, ALLOC-T01 à T32), `docs/current/OPEN-QUESTIONS.md` (DEC-001 à DEC-125), `DOMAIN.md`, `TENDER-PROFILES.md`, `KEYS.md`, `CUSTOM-COLUMNS.md`, `LIFECYCLE.md`, `ACCESS.md`, `JOURNEYS.md` (UX-001 à UX-006), `AI.md` (AI-014) ; specs annexes `docs/specs/SPEC-external-partners.md`, `SPEC-document-view.md` — au 8 sept. : `docs/specs/SPEC-review-table.md`, `SPEC-advanced-filters.md`, `SPEC-domain-model.md`, `docs/tickets/TICKET-two-pass-allocation.md`, `TICKET-ai-uncertainty-display.md`, `TICKET-vocabulary-alignment.md`, `docs/GLOSSARY.md`, `docs/decisions/DECISIONS.md`

### Nouveau
- (R) **Corpus consolidé** — le 8 sept. à 16:43 (`7f50eda`, juste après la baseline) les specs ont été refondues en `docs/current/*.md` avec des identifiants de règle stables ; une règle se cite par son ID (ALLOC-0xx…), plus par ancre de section.
- (R) **Registre de décisions DEC-001 → DEC-125** — toutes postérieures à la baseline (DEC-001 à 027 arrivent avec `7f50eda`, 8 sept. 16:43). Une décision plus récente sur le même sujet remplace l'ancienne ; la colonne « Statut et portée » des tables dit DEC / OBS / DOC / PROP / OPEN.
- (R) **Périmètre du premier pilote** — création jusqu'à la **validation de l'allocation**, pour Turnkey, SIG, Mainline, RSC (DEC-022). Allocation est donc la borne du pilote ; Compliance/Q&A sont spécifiés « pour la suite ». REX/Chat hors V1 (DEC-021).
- (R) **Volumétrie cible** — jusqu'à 100 000 lignes et 10 utilisateurs simultanés (DEC-023, PLAT-007).

### Modifié
- (R) **Statut des anciennes specs** — Avant : `SPEC-review-table.md`, `SPEC-advanced-filters.md`, `SPEC-domain-model.md` faisaient foi → Maintenant : ce sont des **pointeurs** vers `docs/current/` ; le texte d'origine est archivé dans `docs/archive/specs-2026-09-08/` et ne fait plus autorité là où il contredit une règle ou une DEC.
- (R) **Tickets de la baseline** — `TICKET-two-pass-allocation.md`, `TICKET-ai-uncertainty-display.md`, `TICKET-vocabulary-alignment.md` n'ont **pas été modifiés** mais sont largement dépassés (détail par domaine ci-dessous) : chaîne PBS → ABS → OBS (→ DEC-008), état « allocation manuelle » filtrable (→ DEC-103), « jamais zéro activité » (→ DEC-076), « To review » sur titres/informations (→ DEC-073), confiance jamais affichée (→ DEC-120), cible « activity » (→ « system », DEC-045).
- (R) **Glossaire** — Avant : `docs/GLOSSARY.md` (activity, allocated activity, Nature/Type bloqué…) → Maintenant : `docs/GLOSSARY.md` renvoie à `DOMAIN.md` + DEC ; l'ancien glossaire est archivé.

### Retiré / abandonné
- (X) **`SPEC-expert-space.md`** — supprimé ; plus d'écran Expert Space (fusionné dans Compliance).

### Toujours ouvert
- **Docs pas toujours alignées entre elles** — plusieurs paragraphes de `docs/current` n'ont pas suivi les DEC récentes (listés domaine par domaine : ALLOC-010/T06 vs DEC-087/103, emplacement de la relance ALLOC-014/T23, ALLOC-017 « bouton Confirm » vs DEC-099, CUST-T01/T11 vs DEC-097, ACC-009 vs DEC-087, `COMPLIANCE.md`/`DOMAIN.md` « trois verdicts » vs DEC-031). Règle : la DEC la plus récente prime.

### Synthèse
- Lire `docs/current/ALLOCATION.md` + le registre DEC ; ne plus implémenter depuis `SPEC-domain-model.md` §3.2/§8 ni depuis les tickets.
- Le pilote s'arrête à la validation de l'allocation (DEC-022) : c'est le cœur du livrable.
- Cible 100 000 lignes (DEC-023), pas 10 000.

## Modèle d'allocation — vocabulaire, Turnkey / SIG, chaîne de dérivation, OBS et personnes
Où lire aujourd'hui : `ALLOCATION.md` (ALLOC-001 à 013, 016, 020, 021, 024, 025), `DOMAIN.md` (§ OBS, DOM-004 à 006), `TENDER-PROFILES.md` (§ Systèmes, produits et modèles), `ACCESS.md` (ACC-014), DEC-005 à 012, 029 à 037, 044 à 049, 054 à 060, 076, 077, 087, 101 à 104, 123, 124 — au 8 sept. : `SPEC-domain-model.md` §1, §3.2, §4, §6–7, `TICKET-two-pass-allocation.md`, `GLOSSARY.md`

### Nouveau
- (R) **« Système » remplace « activité »** dans tout ce que lit l'utilisateur (DEC-045, remplace le vocabulaire de DEC-033) : hiérarchie **Système → Périmètre → Personne**. « Activité » est rendu à l'ABS (Activity Breakdown Structure). Les identifiants de code gardent leurs noms (`typology`, `perim`, `ACTIVITY_MODEL`, `deriveActivityCompliance`…).
- (R) **Système / sous-système / produit / modèle** (DEC-046 à 049, DEC-058) — un tender est émis sur **un seul système** (Turnkey, SIG, RSC ; « Mainline » est un produit SIG) ; Turnkey répartit vers des **sous-systèmes** (les 16 codes de la capture sont tous du niveau sous-système, DEC-058, déduction à confirmer) ; chaque système a des **produits** qui **sélectionnent le modèle** ; le produit est figé à la création, le modèle est réglable dans les paramètres (DEC-049, DEC-095). Seuls SIG et RSC portent un modèle.
- (R) **OBS = une organisation, jamais une personne** (DEC-054) — trois mailles du même axe : **TK OBS** = système/sous-système (passe Turnkey), **OBS · team** = équipe dans un système, **OBS · role** = poste (intitulé + codes Skills/SoA/Job) sur le modèle Mainline à clés (DEC-062). Afficher un nom de personne sous un libellé OBS est interdit.
- (R) **ABS et PBS uniques, OBS multiple** (DEC-055) — une exigence a un seul ABS et un seul PBS ; elle peut atteindre plusieurs organisations, chacune avec **sa personne et son verdict**, consolidés (le plus restrictif gagne, DEC-037/014). Jamais d'ABS/PBS par équipe.
- (R) **Une allocation = une organisation + sa personne** (DEC-060, remplace DEC-057 ; ALLOC-016) — pas de bloc « qui vérifie » séparé ; le compte « Allocations (N) » est le nombre d'organisations, pas de systèmes (ALLOC-T18) ; un seul endroit pour désigner la personne d'une organisation (ALLOC-T19) ; sur une exigence à une organisation dans un système, la personne de l'allocation est celle de l'exigence partout (ALLOC-T20/T21).
- (R) **La personne assignée à un OBS est responsable de sa conformité** (DEC-087, remplace DEC-010 ; ALLOC-011) — elle répond et c'est elle qu'on relance ; **plus de « responsable du suivi » au niveau exigence**. Plusieurs personnes dans un périmètre = plusieurs entrées OBS.
- (R) **« Assigned to » se lit sur les allocations** (DEC-123) — la colonne et l'assignation en masse lisent/écrivent la personne de chaque entrée OBS ; plus de faux « Unassigned » sur une exigence multi-système (on affiche « n/m assigned »).
- (R) **Une personne appartient à un seul système** (DEC-102, ACC-014 ; précisé par DEC-124) — le sélecteur de personne d'un OBS ne propose que les membres de ce système (plus la personne déjà en place) ; « mon système » se lit par l'appartenance.
- (R) **Tout OBS et tout système se supprime, jusqu'à zéro** (DEC-076, ALLOC-020) — ✕ sur chaque ligne OBS et sur chaque système de la liste Turnkey ; vide → exigence Incomplete ; une entrée déjà répondue demande confirmation. Le PM ajoute un système directement (« + Add system », recherche code/nom) ; le contributeur passe par « + Missing system » (proposition).
- (R) **Détail d'un système Turnkey = le panneau SIG** (DEC-101, ALLOC-024) — nature, classe, modèle du système (ABS/PBS/OBS modifiables, relance), personne de chaque OBS, validation, plus les boutons de réassignation ; les modifications portent sur le système ouvert.
- (R) **Deux niveaux de validation sur Turnkey** (DEC-104, ALLOC-025) — le PM valide l'aiguillage (« Validate & send to the systems ») ; chaque système est validé par son contributeur ou le PM ; nouveau statut d'exigence **« Reassignment requested »** tant qu'une réassignation attend (validation bloquée).
- (R) **Qui valide l'allocation** — DEC-009 / ALLOC-012 : l'équipe de gestion du projet (tranche l'hypothèse « rôle de validation distinct » de `SPEC-review-table` §5) ; précisé par DEC-104 / ACC-014 : **chaque système est validé par son contributeur ou par le PM**, l'aiguillage Turnkey par le PM seul.
- (R) **Allocation SIG autonome = même modèle et mêmes actions que le SIG d'un Turnkey** (DEC-005) ; un tender SIG retire tout ce qui relève de la passe Turnkey et ouvre son détail directement en configuration SIG (DEC-006, ALLOC-T08, TYPE-T01/T02).

### Modifié
- (R) **Ordre de la chaîne** — Avant : **PBS → ABS → OBS** (`SPEC-domain-model` §3.2, ticket §2) → Maintenant : **ABS → PBS → OBS → personne**, sans distinction technique/non technique pour SIG (DEC-008, ALLOC-003, ALLOC-T02, TYPE-T09). Corriger ABS invalide PBS et OBS ; corriger PBS invalide OBS.
- (R) **Personne(s) sur une allocation** — Avant : un *manager* **et** un *expert* par activité allouée (`SPEC-domain-model` §1) → Maintenant : **une seule personne** par entrée OBS, « contributor » (DEC-030 ; `326291b`). « Activity manager » ne désigne plus qu'une fonction de casting, et un système n'a pas besoin de manager (DEC-124).
- (R) **OBS** — Avant : une valeur unique, sélection d'une équipe-personne (« OBS · team » = l'expert) → Maintenant : **liste éditable d'organisations** (ou de postes sur clés), chacune avec sa personne (DEC-054/055/060). La personne vient après, séparément (souvent le responsable de l'équipe dans la région du tender).
- (R) **Passe Turnkey (« TK OBS »)** — Avant : colonne « TK OBS » distincte de « OBS · team » (ticket, DEC-034) → Maintenant : **plus de colonne TK OBS**, c'est la colonne **System**, avec la certitude du routage à côté de l'étiquette (DEC-077 précise DEC-034 ; ALLOC-002). « TK OBS » reste un nom de concept dans la doc.
- (R) **Passe 1 / passe 2** — Avant : libellés « Pass 1 »/« Pass 2 » visibles → Maintenant : concept conservé dans les specs (ALLOC-002), **plus affiché** à l'utilisateur (`a900e09`) ; la passe Turnkey lit une seule dimension selon la classe (non technique → ABS, technique → PBS).
- (R) **Système sans modèle** — Avant : état de premier ordre « activité connue, allocation manuelle à faire », visible et **filtrable** (ticket §3, DoD 5) → Maintenant : **pas de statut dédié** ; ABS/PBS/OBS/personne vides, donc **Incomplete** jusqu'à ce que son contributeur les remplisse (DEC-103 amendé, ALLOC-025, ALLOC-T32) ; ALLOC-005 « identifiée et filtrable » ne tient plus que via Status + System.
- (R) **Zéro système** — Avant : « une exigence ne peut jamais finir sans activité » (ticket §5, B10) → Maintenant : vrai pour une **demande de réassignation** (toujours un remplacement, ALLOC-013) mais le **PM peut retirer jusqu'à zéro** (DEC-076).
- (R) **Réassignation** — Avant : demandée par expert ou manager, résolue par le PM → Maintenant : même mécanisme (DEC-011, ALLOC-013 : 3 motifs « Right system, wrong person » / « Wrong system » / « This system doesn't apply here », justification obligatoire ALLOC-T07), vocabulaire système/contributeur ; sur Turnkey elle bloque la validation de l'aiguillage (DEC-104).
- (R) **Droits des contributeurs** — Avant : hiérarchie d'activités pour les permissions (`SPEC-domain-model` §9, Expert Space) → Maintenant : tous les contributeurs d'un système au même niveau, lecture de tout le projet, modification de leur seul système (DEC-012, DEC-002/003, ACC-007/010).
- (R) **Confiance** — Avant : « la gradation n'atteint jamais l'écran » (TICKET-ai-uncertainty-display) → Maintenant : **pourcentages** affichés pour les modèles d'allocation (routage Turnkey, ABS, PBS, OBS) et **niveau Low/Medium/High** pour la caractérisation (DEC-120, AI-014).

### Retiré / abandonné
- (X) **Verrou du verdict final par le PM** (`SPEC-domain-model` §4–5, ticket §6) — supprimé : le verdict client est la conformité externe de Compliance (DEC-028, puis DEC-106) ; Allocation n'a plus de lock.
- (X) **Échelle à trois verdicts / R&D Needed** dans Allocation — deux verdicts internes (DEC-031) ; colonne Compliance **en lecture seule** dans Allocation (DEC-039).
- (X) **Responsable de suivi unique par exigence** (DEC-010) — remplacé par DEC-087.
- (X) **Bloc d'affectations séparé « qui vérifie »** (DEC-057) — remplacé par DEC-060.
- (X) **Proposition IA de personne** (carte « AI Suggestion » + boîte « Why ») — retirée : un OBS n'est pas une personne (DEC-054 ; `14e3059`).
- (X) **Hiérarchie d'activités pour les droits** (§9 du domain model) — sans objet (DEC-012 : pas de hiérarchie interne).

### Toujours ouvert
- **Validation sans personne ?** — DEC-025 / ALLOC-010 / ALLOC-T06 autorisent la validation sans responsable ; mais ALLOC-T32 (DEC-103) et le prototype exigent une personne sur **chaque** entrée OBS pour sortir d'Incomplete (donc pour valider). Contradiction à faire arbitrer ; le paragraphe « Absence de responsable — décision » d'`ALLOCATION.md` parle encore de « l'unique responsable du suivi » (DEC-010, remplacé).
- **Validation par l'équipe projet ou par le contributeur ?** — ALLOC-012 (DEC-009) n'a pas été réaligné sur ACC-014 / DEC-104 (le contributeur valide son système). La règle la plus récente (DEC-104) prime.
- **Matrice des combinaisons Turnkey** (DEC-048) — à fournir ; placeholder explicite d'ici là.
- **RSC / RST** (DEC-059) — orthographe tranchée (RSC) ; le rapport RSC ↔ RST reste à confirmer ; le prototype marque RST « avec modèle » par hypothèse. DEC-058/059 sont des **déductions** à confirmer.
- **Légende des codes système** (DEC-032) — libellé = code faute de source.
- **Maille OBS du modèle Urban** — DEC-062 ne dit rien d'Urban (garde la maille équipe).
- **Mainline / RSC autonomes** — particularités non fournies (OPEN-15) ; ne pas les déduire de SIG.
- **Un modèle peut-il ajouter ou retirer une organisation à la relance ?** — non tranché (relevé dans le code de `applyRerunTo`, qui garde la taille de l'ensemble).

### Synthèse
- Vocabulaire : système (pas activité), contributeur (pas manager/expert), une personne par entrée OBS, Assigned to lu sur les allocations (DEC-045/030/087/123).
- Chaîne ABS → PBS → OBS → personne (DEC-008) ; ABS/PBS uniques, OBS multiple (DEC-055) ; OBS = organisation (DEC-054).
- Turnkey : routage vers des systèmes (colonne System + certitude, DEC-077), validé par le PM ; chaque système validé à part (DEC-104) ; détail de système = panneau SIG (DEC-101).
- Système sans modèle = Incomplete, pas d'état « manuel » (DEC-103) ; tout se retire jusqu'à zéro (DEC-076).
- Une personne = un système (DEC-102) ; plus de lock, plus de R&D Needed (DEC-028/031/039).

## Statuts, revue et validation
Où lire aujourd'hui : `ALLOCATION.md` (ALLOC-007 à 010, 018, 022, 024, 025 ; § États et acceptation), `LIFECYCLE.md` (LIFE-015), `AI.md` (AI-014), DEC-035, 072, 073, 084, 098, 099, 103, 104, 120 — au 8 sept. : `SPEC-domain-model.md` §8 (B6/B7), `TICKET-ai-uncertainty-display.md`

### Nouveau
- (R) **Une seule validation par exigence** (DEC-099, ALLOC-024) — bouton, pastille ou touche V valident **ensemble** caractérisation et allocation (par système quand il y en a plusieurs, la validation d'un système validant aussi la caractérisation). Valider confirme ce que l'IA a détecté. Impossible tant que l'une des deux est Incomplete — le bouton le dit (ALLOC-T31).
- (R) **Bouton de validation toujours visible dans le panneau** (DEC-084, ALLOC-022) — grisé avec sa raison quand l'étape est impossible ; une ligne par système quand il y en a plusieurs (ALLOC-T30).
- (R) **Statut « Reassignment requested »** au niveau Turnkey (DEC-104) — tant qu'une demande de réassignation attend ; validation de l'aiguillage bloquée.
- (R) **Une exigence ajoutée ou modifiée par la version en vigueur de son document repasse To review** (DEC-072, LIFE-015) — la valider est le traitement ; le statut le plus restrictif continue de primer.
- (R) **Niveaux de confiance de caractérisation** (DEC-120) — nature et classe portent Low / Medium / High tant que la valeur est celle de l'IA ; **Low** = appel incertain → To review. Les nombres d'une ancienne capture se lisent < 75 Low, < 85 Medium.
- (R) **Carte « Allocation » du tableau de bord** passe à Done quand toutes les exigences sont allouées, et redevient Current sinon (DEC-098) — lue sur la progression réelle d'Allocation.

### Modifié
- (R) **Libellé et effet de la validation** — Avant : « Validate characterisation » puis « Validate & send to Expert Review » (deux gestes) → Maintenant : « Validate & send to Compliance » (un geste) ; sur Turnkey (PM) « Validate & send to the systems » (DEC-029, DEC-099, DEC-104).
- (R) **Statuts des titres et blocs d'information** — Avant : pouvaient être « To review » sur leur Type (ticket ai-uncertainty) → Maintenant : **aucun statut**, nulle part (DEC-073, ALLOC-018, ALLOC-T24) ; une nature proposée par l'IA se signale sur la puce de nature (pointillés), choisir la nature en place la confirme.
- (R) **Incomplete** — Avant : pas de valeur IA, ou OBS non assigné (« plancher absolu », §8.2.1) → Maintenant : classe ou système manquant ; ABS/PBS/OBS tous vides ; **une entrée OBS sans personne** ; dernier OBS ou dernier système retiré (DEC-076) ; système sans modèle (DEC-103).
- (R) **Motifs de To review** — Avant : Type/Class/Activity « AI-detected, unconfirmed », OBS faible → Maintenant : nature ou classe proposée avec confiance Low (DEC-120), système détecté par l'IA non confirmé, dérivation ABS/PBS/OBS sous le seuil (75 %), changement de version (DEC-072), marquage manuel « Mark to review ». Le motif s'affiche en tête du panneau.
- (R) **Statut d'une exigence Turnkey** — Avant : caractérisation au niveau exigence, allocation par branche → Maintenant : le PM voit le statut du **niveau Turnkey** (nature, classe, aiguillage) ; un contributeur voit le statut de **son** système (DEC-104).

### Retiré / abandonné
- (X) **« Finalize allocation »** (bouton, fenêtre, lien du tableau de bord, réglage « completeness gate ») — supprimé (DEC-084) ; rien n'attend ce jalon (DEC-035 : les deux étapes tournent en parallèle).
- (X) **« Awaiting manual allocation »** (statut, pastille, filtre, colonne) — supprimé (DEC-103 amendé).
- (X) **« Detected by the AI, not confirmed yet » + bouton Confirm** sur nature/classe, et « Confirm AI activity » — supprimés (DEC-099) : valider confirme.
- (X) **États propres à un changement de version** (New / Reviewed, no impact / Action required) — supprimés (DEC-072).

### Toujours ouvert
- **Textes non réalignés** — ALLOC-T30 parle encore de « valider la caractérisation fait apparaître Validate allocation & send » (deux gestes, antérieur à DEC-099) ; DEC-025 vs exigence d'une personne (voir domaine Modèle).
- **Libellés exacts des états et composition des filtres** — OPEN-13.

### Synthèse
- Une validation = caractérisation + allocation (DEC-099), bouton toujours présent avec sa raison (DEC-084), plus de Finalize.
- Statuts : Incomplete / To review / To validate / Allocated + « Reassignment requested » (Turnkey) ; titres et informations sans statut (DEC-073).
- Un changement de version renvoie en To review (DEC-072).
- Confiance de caractérisation en niveaux, pas en pourcentage (DEC-120).

## Relance des modèles d'allocation
Où lire aujourd'hui : `ALLOCATION.md` (ALLOC-014, 015, 019, 023 ; ALLOC-T09 à T17, T22, T23, T27), `DOMAIN.md` (§ OBS, précision de DEC-042), DEC-040 à 043, 047, 050 à 053, 056, 075, 089, 091 — au 8 sept. : rien (n'existait pas)

### Nouveau
- (R) **Relance unitaire** (ALLOC-014, DEC-040 à 043) — rejouer un modèle d'allocation sur une exigence déjà dérivée, en choisissant le modèle. Distincte de la réallocation (qui change **qui** répond).
- (R) **Granularité = l'exigence** (DEC-056, remplace la feuille de DEC-040) — elle re-dérive ABS, PBS et **toutes** les organisations ; bloquée dès qu'une seule est bloquée (ALLOC-T11).
- (R) **Effet** — application directe, sans aperçu ; écrase ABS/PBS/OBS et rien d'autre ; **la personne n'est jamais touchée** (DEC-042 précisé par DEC-054 ; ALLOC-T09).
- (R) **Blocage** — une réponse ou un verdict enregistré bloque (DEC-041) ; l'attente d'une réponse client **ne bloque plus** (DEC-089 remplace DEC-051) ; contrôle visible mais inactif avec le motif (ALLOC-T10).
- (R) **Choix du modèle en deux temps** (DEC-047, ALLOC-T14) — d'abord les produits du système (SIG Urban / Mainline…, produit du tender présélectionné), puis, séparément, **l'emprunt** du modèle d'un autre système (cas B, système sans modèle, DEC-043) ; emprunt ponctuel et silencieux, tracé seulement dans l'historique (ALLOC-T12/T13) ; ne change pas le produit du tender (ALLOC-T15).
- (R) **Relance en masse** depuis la barre de sélection (DEC-052) — mêmes règles ; bloquées sautées et comptées ; blocs non-exigence écartés et comptés (ALLOC-T22).
- (R) **Résultat identique silencieux** (DEC-091 précise DEC-053) — pas de message ; le journal note « same result » ; en masse seules les exigences changées sont comptées.
- (R) **Changer la nature ou la classe propose de relancer** (DEC-075, ALLOC-019, ALLOC-T27) — une ligne « ↻ Re-run the model » au-dessus d'ABS avec la raison ; rien n'est relancé automatiquement ; ligne neutre « re-run blocked » si bloqué ; sur SIG, un bloc reclassé en exigence devient SIG.
- (R) **Relance globale au changement de modèle** (ALLOC-015, DEC-050) — depuis les paramètres, **écrase tout, réponses comprises**, annonce avant confirmation le nombre d'exigences et de réponses détruites (ALLOC-T16/T17).
- (R) **Où se trouve le contrôle** (ALLOC-014, ALLOC-T23) — en tête du bloc de modèle (PM, tender à un système), en tête de la vue contributeur ; pour le PM Turnkey, voir « Toujours ouvert ».

### Modifié
- (R) **Ce que protège DEC-042** — Avant (17 sept.) : « ne touche ni l'équipe ni la personne » → Maintenant : la relance re-dérive l'organisation (c'est ce que produit un modèle) ; seule la **personne** est protégée (DEC-054).

### Retiré / abandonné
- (X) **Relance par organisation** (contrôles par ligne OBS) — abandonnée avec DEC-056.

### Toujours ouvert
- **Emplacement du contrôle sur Turnkey** — `ALLOCATION.md` dit « sur chaque carte système dans la vue PM d'un Turnkey » et ALLOC-T23 « sans navigation supplémentaire », mais le prototype l'a retiré des cartes système (`920072e`) : il n'est plus que dans le détail du système (un clic plus loin). À arbitrer.
- **Relance globale** — spécifiée (ALLOC-015) mais l'écran de paramètres ne fait que l'afficher (bouton inactif « Not wired in this build »).
- **Ajout/retrait d'organisations par un modèle** — non spécifié.
- **Relance automatique sur nouvelle version** (DEC-027, LIFE-011) — spécifiée, non démontrée dans Allocation (déduit de la lecture du code : un changement de version n'y fait que repasser l'exigence en To review).

### Synthèse
- Nouvelle capacité complète : relance unitaire, en masse, et proposée après changement de nature/classe ; globale spécifiée mais non câblée.
- Toujours au niveau de l'exigence ; ABS/PBS/OBS seulement ; jamais la personne.
- Bloquée par une réponse/un verdict, plus par une question client (DEC-089).

## Nature, classe et caractérisation
Où lire aujourd'hui : `ALLOCATION.md` (ALLOC-017 § Nature et classe, ALLOC-018, ALLOC-T25/T26), `ACCESS.md` (ACC-012), `AI.md` (AI-014), DEC-062, 073, 074, 075, 086, 094, 099, 120 — au 8 sept. : `SPEC-review-table.md` §4, `TICKET-ai-uncertainty-display.md`, `TICKET-vocabulary-alignment.md`, `GLOSSARY.md` (§ « Nature → Type — BLOCKED »)

### Nouveau
- (R) **Nature = Information, Heading ou Requirement — rien d'autre** (DEC-074, précise DEC-062) ; elle **n'a pas de colonne** dans la table ; elle se lit et se corrige en tête du détail (ou dans la vue Document) (ALLOC-T25/T26).
- (R) **Classe (technique / non technique) dans le détail de toute exigence**, SIG compris (DEC-074) — juste sous la nature, avant le bloc de modèle.
- (R) **Nature et classe appartiennent au chef de projet** (DEC-086, ACC-012) — lecture seule pour tout contributeur, partout (détail, bascule Class de la table, action groupée « Classify », sélecteur de nature de la vue Document), refus côté logique.
- (R) **Pas de suppression manuelle d'un bloc capturé** (DEC-094) — un bloc capturé par erreur se reclasse en Information ; seules les lignes dupliquées à la main depuis une image restent supprimables.
- (R) **Niveau de confiance** (DEC-120) — affiché à côté des libellés Nature et Class tant que la valeur est celle de l'IA ; un choix humain n'en a pas.

### Modifié
- (R) **« Nature » vs « Type »** — Avant : le ticket vocabulaire voulait renommer Nature → Type, bloqué par le glossaire (collision avec le « Type » Functional/Performance/…) ; le panneau affichait « Type » → Maintenant : le mot retenu est **Nature** (DEC-074) ; « Type » ne désigne plus rien dans Allocation.
- (R) **Les cinq valeurs Functional / Performance / Security / Interface / Regulatory** — Avant : colonne et champ « PBS » (sélecteur à 5 valeurs), action groupée « PBS » → Maintenant : **retirées d'Allocation** (table, détail, filtres, action groupée, puce de la vue Document, passe Turnkey) ; le PBS est un **élément produit** (DEC-062, KEY-T04).
- (R) **Classe** — Avant : « Classification » dans le panneau hors Turnkey, « Type » dans la vue PM Turnkey → Maintenant : « Class » partout.
- (R) **Confirmation d'une valeur IA** — Avant : bouton « Confirm AI activity », mention « AI-detected, unconfirmed » → Maintenant : valider l'exigence confirme (DEC-099) ; pour une nature seule, re-choisir la nature en place la confirme (DEC-073).
- (R) **Reclassement** — Avant : possible dans la table (bouton ▾ sur la ligne) → Maintenant : seulement dans le champ Nature du détail ou la vue Document (`083e9a3`).
- (R) **Information → Requirement** — reste à Incomplete (B8) ; nouveau : sur SIG, le bloc reçoit le système SIG (DEC-075).

### Retiré / abandonné
- (X) **Colonne « Nature »** (5 valeurs) apparue après DEC-062 — supprimée (DEC-074).
- (X) **Statut « To review » sur le Type d'un titre/information** — supprimé (DEC-073, remplace cette partie du ticket ai-uncertainty).

### Toujours ouvert
- **Texte d'ALLOC-017 non réaligné** — « Une nature ou une classe détectée par l'IA le dit, avec un bouton pour la confirmer » contredit DEC-099 (pas de bouton Confirm).
- **« Class » est-il le nom réel de la colonne des captures ?** — toujours non confirmé (ancien point du glossaire).

### Synthèse
- Nature = 3 valeurs, sans colonne ; Class dans tout détail ; les 5 « types » sortent d'Allocation (DEC-074).
- Nature/classe = droit du PM (DEC-086).
- Changer nature/classe propose une relance (DEC-075) ; niveaux Low/Medium/High (DEC-120).

## Clés PBS / OBS / ABS de SIG (modèle Mainline)
Où lire aujourd'hui : `docs/current/KEYS.md` (KEY-T01 à T05), `ALLOCATION.md` (ALLOC-017), `DOMAIN.md` (OBS · role), `TENDER-PROFILES.md` (TYPE-T11), DEC-061, DEC-062 — au 8 sept. : rien

### Nouveau
- (R) **Classeur de référence « PBS / OBS / ABS Keys v260720 »** (DEC-061) — trois feuilles, une par axe, liste partagée cochée par produit (URBAN, Mainline Wayside, Mainline Onboard) : le **modèle d'un produit est le sous-ensemble coché** (DEC-047 rendu concret). Anomalies du fichier chargées telles quelles.
- (R) **Mainline Wayside et Mainline Onboard sont deux produits SIG distincts** (DEC-061) — SIG a donc trois produits.
- (R) **Sur un tender à clés, ABS → PBS → OBS se choisissent dans les listes, jamais en texte libre** (ALLOC-017, KEY-T02) — 16 ABS ; éléments PBS groupés par famille ; OBS = postes, ceux rangés **sous l'ABS choisi** d'abord (la chaîne ABS → OBS est encodée dans le classeur, KEY-T03).
- (R) **Changer l'ABS efface PBS et OBS** (KEY-T03) ; la relance dérive l'OBS sous l'ABS dérivé ; un modèle emprunté peut produire un élément hors liste, affiché « from another product's model ».
- (R) **Tender Turnkey ou Urban : aucun sélecteur de clé** (KEY-T05) — Urban n'est pas branché sur les clés (DEC-062 silencieux).
- (R) **Aucune valeur des clés saisie ailleurs que dans le classeur** (KEY-T01) — génération reproductible.

### Modifié
- (R) **OBS du modèle Mainline** — Avant : équipe inventée (« … — FR ») → Maintenant : **poste** avec codes (DEC-062) ; libellé de colonne « OBS · role ».
- (R) **PBS** — Avant : nature d'exigence (5 valeurs) → Maintenant : élément produit (ex. famille › sous-système › élément) (DEC-062, KEY-T04).

### Retiré / abandonné
- (X) **Listes annexes de la feuille ABS** — ignorées (DEC-061).

### Toujours ouvert
- **Modèle Urban** (et RSC) sans clés réelles — vocabulaire du prototype inventé.

### Synthèse
- Les modèles SIG Mainline viennent d'un classeur réel ; listes fermées, OBS = poste sous l'ABS.
- Rien de cela ne s'applique à Turnkey ni à Urban.

## Profils de tender : Turnkey, SIG autonome (RFP-2026-114) et partenaires externes
Où lire aujourd'hui : `TENDER-PROFILES.md` (matrice d'applicabilité, TYPE-T01 à T11), `ALLOCATION.md` (ALLOC-001, 021, 023), `docs/specs/SPEC-external-partners.md`, DEC-004 à 007, 044, 049, 082, 093, 095 — au 8 sept. : `TICKET-two-pass-allocation.md` §1, `SPEC-domain-model.md` §3.2

### Nouveau
- (R) **Matrice d'applicabilité par type de tender** (TENDER-PROFILES) — Turnkey / SIG au sein d'un Turnkey / SIG autonome / Mainline-RSC autonomes ; « absents, pas simplement vides » pour les champs de passe Turnkey en SIG.
- (R) **SIG autonome : l'axe système est absent** (DEC-044, TYPE-T08) — une passe d'IA, ABS → PBS → OBS direct, une exigence = une dérivation ; pas de colonne System, pas de champ System, pas de regroupement par système ; conformité équipes → exigence.
- (P) **Tender SIG de démonstration construit** (DEC-044, TYPE-T07, TYPE-T11) — RFP-2026-114 « Line 4 Resignalling — ETCS L2 », produit Mainline Wayside, contenu propre (12 exigences sur 2 documents, langue source anglaise), jamais le contenu de STB-2026.
- (R) **Partenaires externes sur Turnkey** (DEC-082, SPEC-external-partners, ALLOC-021) — le PM ajoute une entreprise à la **liste OBS Turnkey** depuis les paramètres ; elle apparaît partout où la liste sert (table, détail, filtres, « + Add system ») dans une **couleur propre** avec infobulle « added for this tender, not part of the model » ; jamais dans le jeu d'étiquettes du modèle ; **pas de passe 2** (ni ABS/PBS/OBS ni équipe ni personne), branche allouée dès l'attribution ; responsable affiché **« PM · for partner »** ; le PM saisit le verdict du partenaire dans Compliance (au niveau système) ; envoi au partenaire par l'export filtré (qui énonce le filtre). Points 6.1 → (b) provenance lue au système, 6.2 → « PM · for partner », 6.3 → par tender en v1.
- (R) **Retrait d'un partenaire** (DEC-093) — possible tant qu'aucune exigence ne lui est attribuée ; sinon refusé avec le nombre à réattribuer.
- (R) **Ligne produit et mode IA figés à la création** (DEC-095) ; produit figé, modèle réglable (DEC-049).

### Modifié
- (R) **Type « Mainline »** — Avant : type de tender à part (DEC-004) → Maintenant : un tender SIG de produit Mainline (DEC-047).
- (P) **Projets de référence** — Avant : seul STB-2026 (ligne Turnkey) était construit ; RFP-2026-114 (« Urban Line 4 Signalling Upgrade », ligne SIG) figurait dans la liste sans contenu, et l'ouvrir montrait les données de STB-2026 → Maintenant : STB-2026 = référence **Turnkey** (passe de routage) ; RFP-2026-114 = référence **SIG autonome**, renommé et passé en Mainline Wayside (DEC-061).

### Retiré / abandonné
- —

### Toujours ouvert
- **Mainline/RSC autonomes** (OPEN-15), **matrice Turnkey** (DEC-048), **partenaires réutilisables entre tenders** (v2, SPEC §6.3).

### Synthèse
- Deux profils démontrés : Turnkey (STB-2026) et SIG autonome (RFP-2026-114) ; ne jamais montrer d'axe système en SIG.
- Partenaire = système ajouté à la main sur Turnkey, sans passe 2, « PM · for partner ».

## Accès : vue contributeur, lecture seule et « View as »
Où lire aujourd'hui : `ACCESS.md` (ACC-007, 010, 012, 013, 014 ; matrice métier), `ALLOCATION.md` (ALLOC-024, 025), DEC-012, 086, 100, 102, 124 — au 8 sept. : `SPEC-domain-model.md` §7, §9 ; `GLOSSARY.md` (Contributor)

### Nouveau
- (R) **Lecture seule complète sur une exigence qui n'est pas au contributeur** (DEC-100, ACC-013) — panneau en lecture (nature, classe, puis chaque système avec ABS, PBS, OBS et leurs personnes), sans sélecteur de système, sans proposition ni validation ; cellules de table verrouillées.
- (R) **« Mon système » = appartenance** (DEC-102, ACC-014) — un contributeur agit sur le système dont il est membre (ou une entrée qu'il tient) ; il valide son système (DEC-104).
- (R) **Nature/classe en lecture seule pour un contributeur** (DEC-086, ACC-012).
- (P) **« View as » limité à deux contributeurs** (DEC-102, démo) — Louis Renaud (SIG, système avec modèle) et Paolo Ferri (SEN, sans modèle).

### Modifié
- (R) **Vue restreinte** — Avant : « only requirements assigned to » un manager → Maintenant : le **système** du contributeur ; la règle produit reste « tout consulter, ne modifier que son système » (DEC-012, ACC-007).
- (R) **Rôles** — Avant : Admin / Manager / Expert (récapitulatif de l'onglet Activity) → Maintenant : Admin + une ligne « Assigned to » par personne des entrées OBS.

### Retiré / abandonné
- (X) **Restriction de lecture entre activités et hiérarchie manager/expert** — dépassées (ACCESS, DEC-012).

### Toujours ouvert
- **Écart maquette / règle de lecture** — la vue « View as » du prototype masque les exigences hors système dans la table et les caviarde (ou les masque, selon le réglage de caviardage) dans la vue Document, alors qu'ACC-007 dit « tout consulter » (en lecture seule, DEC-100). À ne pas reproduire tel quel ; à confirmer.
- **ACC-009 non réaligné** — cite encore « la personne responsable de l'exigence garde le suivi » (DEC-010) au lieu de DEC-087.

### Synthèse
- Contributeur : un système, lecture de tout, modification du sien, jamais nature/classe.
- Exigence d'un autre système : panneau et ligne en lecture seule (DEC-100).

## Tableau Allocation (ex-« Requirements review »)
Où lire aujourd'hui : `JOURNEYS.md` (UX-001 à UX-006, JRN-002), `ALLOCATION.md` (ALLOC-002, 016, 022), `LIFECYCLE.md` (LIFE-016), `PLATFORM.md` (PLAT-007), DEC-023, 029, 039, 074, 077, 085, 119, 123 — au 8 sept. : `docs/specs/SPEC-review-table.md`

### Nouveau
- (R) **Colonne Changes** (DEC-119, LIFE-016) — juste après Requirement : la même exigence, mots supprimés barrés et ajoutés surlignés « comme DOORS », comparée à une version antérieure de **son** document (précédente par défaut, ou première) ; sélecteur de version par cellule, et dans l'en-tête pour toutes (réinitialise les choix par ligne) ; filtre de colonne Modified / Added / No change ; touche **C** ; visible par défaut dès qu'un document a plusieurs versions ; une exigence supprimée n'y figure pas.
- (R) **Raccourcis de sélection et annulation** (DEC-085) — X coche la ligne active depuis n'importe quelle colonne ; Maj+↑/↓ (ou J/K) étend ; ⌘/Ctrl+A sélectionne ce que montrent les filtres ; Échap vide ; V valide la sélection, sinon l'exigence active ; N va à la prochaine exigence To review / To validate ; **⌘/Ctrl+Z annule la dernière action annulable** même après disparition du message (Allocation : assignation et validation unitaire et groupée). Dans un champ texte, ⌘/Ctrl+Z/A restent natifs.
- (R) **Colonnes personnalisées** dans la table (DEC-064 à 068, 097) — voir domaine dédié.
- (R) **Relance en masse** dans la barre d'actions groupées (DEC-052).
- (R, sans DEC) **Colonnes redimensionnables** (`aac89b1`) — poignée sur chaque en-tête, double-clic = largeur par défaut, ←/→ au clavier ; « Reset column widths » dans View ; largeurs par tender.
- (R, sans DEC) **Édition au clavier** — Entrée ou F2 ouvre l'édition de la cellule active (CUST-T10) ; ←/→ suivent l'ordre **affiché** des colonnes.

### Modifié
- (R) **Nom de l'écran** — Avant : « Requirements review » → Maintenant : « Allocation » (DEC-029).
- (R) **Colonnes** — Avant : ID, Requirement, Class, Activity, ABS, PBS (5 valeurs), TK OBS, OBS · team (sélection d'équipe), Manager, Status, Compliance → Maintenant : ID, Requirement, **Changes**, Class, **System** (avec certitude de routage sur Turnkey ; absente sur SIG), ABS, **PBS** (élément produit), **OBS · team** (« OBS · role » sur clés, lecture seule), **Assigned to**, Status, Compliance (lecture seule), puis colonnes personnalisées (DEC-074, 077, 123, 039, 119).
- (R) **Édition en ligne** — Avant : Class, Activity, Type, Manager, Expert, Status, compliance des sous-lignes éditables → Maintenant : Class (PM seulement, DEC-086), System, ABS (liste sur clés, texte sinon), PBS (liste sur clés seulement), Assigned to (si une seule entrée OBS ; sinon résumé « n/m assigned », changement par sous-ligne ou panneau), Status (clic = valider si To review / To validate) ; OBS et Compliance en lecture (DEC-039).
- (R) **« Unassigned »** — Avant : par exigence → Maintenant : par entrée OBS, « Unassigned » ou « n/m assigned » (DEC-087/123).
- (R) **Actions groupées** — Avant : Assign (Manager, OBS, Activity, PBS), Classify, Mark to review, Validate → Maintenant : Assign (**Assigned to**, **System**), **Re-run**, Classify (masqué pour un contributeur, DEC-086), Mark to review, Validate. L'assignation en masse écrit la personne sur les entrées OBS **de son propre système** (DEC-102/123).
- (R) **Volume** — Avant : 500 à 10 000+ lignes → Maintenant : jusqu'à 100 000 lignes et 10 utilisateurs (DEC-023) ; budgets à définir (OPEN-08).
- (R) **Barre de statut** — compteurs limités à ce que le lecteur peut voir, avec le statut de son système (`9a4cbb2`) ; « % allocated » ; pastille « changed in latest version » (au lieu de « changes v2.0 → v2.1 »).

### Retiré / abandonné
- (X) **Colonne TK OBS** (DEC-077), **colonne PBS à 5 valeurs** et **colonne Nature** (DEC-074), **sélection d'expert dans la colonne OBS**, **filtre de colonne OBS**.
- (X) **Reclassement ▾ dans la ligne** (`083e9a3`) — nature corrigée dans le détail ou la vue Document.
- (X) **Pastille « awaiting manual allocation »** (DEC-103), **bouton « Finalize allocation »** (DEC-084), **bandeau d'aide clavier** permanent (remplacé par une icône ⌨ au survol).

### Toujours ouvert
- **Composition « Filter to Selection » × filtre avancé × sélection multi-pages** — UX-006 / OPEN-13.
- **Performance à 100 000 lignes** — le prototype rend toutes les lignes (pas de virtualisation) ; mesures et protocole à définir (OPEN-08, PLAT-007).
- **Portée de l'annulation** (DEC-085) — « l'assignation et la validation (unitaire et groupée) » : le prototype n'annule que l'assignation faite dans la cellule de la ligne, pas l'assignation en masse ni celle du panneau (déduit de la lecture du code) ; à préciser.

### Synthèse
- Nouvelles colonnes : Changes, colonnes perso ; retirées : TK OBS, PBS-type, Nature ; OBS et Compliance en lecture.
- Assigned to = personnes des entrées OBS (DEC-123), assignation en masse cantonnée au système de la personne.
- Clavier complet (X, Maj, ⌘A, V, N, C, ⌘Z, Entrée/F2) et colonnes redimensionnables.
- Cible 100 000 lignes.

## Filtres (colonnes et constructeur avancé)
Où lire aujourd'hui : `JOURNEYS.md` (UX-002 à UX-006), `CUSTOM-COLUMNS.md` (§ Filtres), DEC-066, 103, 119 — au 8 sept. : `docs/specs/SPEC-advanced-filters.md`

### Nouveau
- (R) **Opérateurs « liste à choix multiple »** (DEC-066) — contient l'un de / ne contient aucun de / est vide / n'est pas vide.
- (R) **Groupe « Custom columns »** dans le constructeur ; entonnoir d'en-tête pour les colonnes personnalisées de type liste (CUST-T07).
- (R) **Filtre de la colonne Changes** — Modified / Added / No change, calculé contre la version que compare chaque ligne (DEC-119).
- (R) **« PM · for partner »** comme valeur du filtre Assigned to sur un Turnkey avec partenaire (DEC-082).

### Modifié
- (R) **Champs** — Avant (§2 de la spec) : Type, Activity, Responsible person, ABS/PBS/OBS · team (énumérations), TK OBS · activity, Doubt — which pass, Awaiting manual allocation, Changed since version, Compliance à 3 valeurs + pending → Maintenant : **Nature** (heading/information/requirement/image), **System**, **Assigned to** (une valeur par entrée OBS ; « Unassigned » dès qu'une entrée est vide), ABS / PBS / OBS en **texte**, « **Doubt — where** » (which system / within the system / none), « **Changed in latest version** », Compliance à **2 valeurs** + pending, champ de revue (Nature, Class, System, ABS, PBS, OBS).
- (R) **Groupes du constructeur** — Allocation : ABS, PBS, OBS, Assigned to, Allocation level (sans « manual alloc ») ; le reste inchangé (Progress, Characterisation, Content & source).

### Retiré / abandonné
- (X) **« Awaiting manual allocation »** (champ et pastille) — DEC-103 : c'est Incomplete, filtrable par Status.
- (X) **Champ « TK OBS »** et filtres de colonne PBS-type / OBS — avec DEC-077 / DEC-074.

### Toujours ouvert
- **Filtrage côté serveur à 100 000 lignes** (UX-005, cible ; non démontrable dans le prototype).
- **Filtres enregistrés** — personnels, réutilisables entre projets sur une même table (UX-004) ; un champ indisponible dans un autre projet : OPEN-13.

### Synthèse
- Mêmes mécanismes (filtres de colonne Excel, constructeur ET/OU à un niveau, filtres enregistrés), nouveaux champs alignés sur le vocabulaire système / Assigned to / Nature.
- Opérateurs « multi » et filtres des colonnes perso et Changes.

## Colonnes personnalisées
Où lire aujourd'hui : `docs/current/CUSTOM-COLUMNS.md` (CUST-T01 à T12), `docs/specs/SPEC-custom-columns.md` (pointeur), DEC-064 à 068, 081, 097 — au 8 sept. : rien (`SPEC-review-table` §5 disait au contraire « no arbitrary columns »)

### Nouveau
- (R) **Champ défini par un chef de projet, rempli par des humains** — texte libre ou liste fermée à choix unique ou multiple (DEC-066) ; **seuls les PM** créent / modifient / suppriment ; les contributeurs remplissent (CUST-T02).
- (R) **Jamais rempli par l'IA**, sans confiance, ne met jamais « à revoir » (CUST-T03), **toujours facultatif**, ne bloque jamais la validation (DEC-067).
- (R) **Portée : un tender, commun à Allocation et Compliance, mêmes valeurs** (DEC-097, remplace « une phase » de DEC-064) — visible par défaut sur l'écran de création, masqué par défaut sur l'autre et activable depuis View (choix retenu par écran) ; supprimer retire des deux (CUST-T12).
- (R) **Partout comme une colonne native** — table (réordonnable, masquable, triable), détail, filtres (opérateurs par type), exports internes.
- (R) **Hors export client** (DEC-068, défaut à confirmer) — inclus dans les exports internes, jamais dans la matrice client ; à l'export Compliance, décoché par défaut et marqué « internal » (DEC-081).
- (R) **Suppressions et modifications** — supprimer une colonne énonce le nombre de valeurs détruites (CUST-T04) ; retirer une option utilisée est refusé avec le compte (DEC-065, CUST-T05) ; type verrouillé dès qu'une valeur existe, renommer toujours permis (DEC-068, CUST-T06) ; simple → multiple permis, l'inverse bloqué si une exigence tient plusieurs valeurs.
- (R) **Survit à la remise à zéro d'une exigence par une nouvelle version** (DEC-068, CUST-T09).
- (R) **Clavier** — atteignable aux flèches, Entrée/F2 édite, Entrée valide et descend, Échap rétablit, sélecteur multiple au clavier (CUST-T10).
- (R) **Stockage cible recommandé** — table de définitions + valeurs en JSONB indexé par id de champ ; le coût est dans le filtrage serveur.

### Modifié
- (R) **Principe « pas un tableur libre »** — Avant : « No formulas, no arbitrary columns » (`SPEC-review-table` §5) → Maintenant : colonnes ajoutées autorisées, mais typées, humaines, internes.

### Retiré / abandonné
- —

### Toujours ouvert
- **Défauts DEC-068 à confirmer** (export client, verrou de type, survie aux versions).
- **Incohérences internes de `CUSTOM-COLUMNS.md`** — CUST-T01 (« n'apparaît ni dans Compliance »), CUST-T11, le paragraphe « un champ utile en Allocation et en Compliance doit être créé deux fois » et celui de l'export « ces colonnes n'existent pas dans Compliance » contredisent DEC-097 / CUST-T12 (colonne commune). DEC-097 prime.
- **Renommer une option existante** — non fait.

### Synthèse
- Nouvelle fonction complète, PM seulement, données humaines, facultatives, jamais vers le client.
- Commune aux deux écrans depuis DEC-097 ; ignorer CUST-T01/T11.

## Panneau de détail et journal d'activité
Où lire aujourd'hui : `ALLOCATION.md` (ALLOC-016, 019, 022, 024, 025), `LIFECYCLE.md` (LIFE-014), `DOMAIN.md` (DOM-011), DEC-060, 071, 078, 084, 086, 099, 100, 101, 104 — au 8 sept. : `SPEC-domain-model.md` §8.5, `TICKET-two-pass-allocation.md` (Prototype impact), `SPEC-review-table.md` §4

### Nouveau
- (R) **Ordre du détail d'une exigence** — Nature, Class, puis le **bloc de modèle du système** (ABS, PBS, OBS, relance), puis les **Allocations** (une carte par organisation, avec sa personne), validation, colonnes personnalisées, proposition de changement (contributeur seulement) (DEC-074, DEC-060 ; `9435d3f`).
- (R) **Quatre vues** — PM Turnkey (aiguillage : Nature, Class, dimension lue ABS ou PBS, liste System avec % ou « manual », ajout/retrait ; puis cartes Systems avec statut, organisations/personnes, Compliance, « Open system detail ») ; **détail d'un système Turnkey = vue SIG** (DEC-101) ; **vue contributeur** de son système ; **lecture seule** pour une exigence d'un autre système (DEC-100). Le PM d'un tender à un système voit la vue SIG.
- (R) **Onglet Versions** (DEC-071, LIFE-014) — seulement quand l'exigence a changé dans la version en vigueur de son document : quoi, depuis quelle version, diff mot à mot, texte précédent complet, versions antérieures, lien vers la vue Document.
- (R) **Panneau d'exigence supprimée** — lecture seule, n'existe que sous Changes de la vue Document (LIFE-006).
- (R) **Paragraphe source en tête** — « § n° titre » (le titre le plus profond au-dessus du bloc), cliquable vers la vue Document ; « Source section » n'apparaît que s'il manque.
- (R, sans DEC) **Journal d'activité unique par exigence, partagé avec Compliance** (`7a1d771`) — qui / quand / avant → après pour chaque changement (systèmes, réassignation, relances, commentaires, traduction, statuts, ABS/PBS/OBS, personne, nature, classe…), jalons Captured / Allocated / Answered / Declared to the client, filtre par catégorie et champ de commentaire. Matérialise DOM-011 (DOC) et la « trace » d'ALLOC-014.

### Modifié
- (R) **Champs de personne** — Avant : Manager (+ Expert) avec bascule lecture/édition, choix dans une liste fixe → Maintenant : **une personne par organisation** dans les cartes Allocations, choisie parmi les membres du système (DEC-060/102) ; une recherche dans l'annuaire ne subsiste que pour une exigence sans système.
- (R) **Bloc « propose a change »** — Avant : deux variantes (« Raise a problem » dans le détail d'activité) → Maintenant : un seul bloc « Request reassignment » / « + Missing system » partout ; dans un détail de système, la réassignation vise ce système.
- (R) **Validation** — bouton juste après les données qu'il confirme, épinglé en bas tant que cet endroit est hors écran (`1129260`).
- (R) **Onglets** — Details, Activity, REX (hors V1, DEC-021), **Versions** (conditionnel), Translation (masqué sur un tender en anglais ; la langue originale s'affiche d'abord) ; défilement horizontal (DEC-078).

### Retiré / abandonné
- (X) **Bloc « Final verdict » avec Lock/Unlock** (DEC-028).
- (X) **« Distribution across systems »** — retiré de la vue contributeur (`db723a1`), puis du code, où il ne s'affichait plus jamais (`14e3059`).
- (X) **Carte « AI Suggestion » d'assignation + boîte « Why »** (DEC-054).
- (X) **Champ « Specialty »** et récapitulatif en lecture seule du détail d'activité (remplacé par la vue SIG, DEC-101).
- (X) **Fiche « Change v2.0 → v2.1 »** avec New / Reviewed / Action required et « Create action / reminder » (DEC-072).

### Toujours ouvert
- **Statut des systèmes vu par le PM Turnkey** — DEC-104 « il ne voit pas le statut des systèmes sur la vue Turnkey » (vrai pour la pastille et la table), mais les cartes système du panneau affichent le statut de chaque système (`ad66940`). À préciser.
- **Pas de règle écrite pour le journal d'activité** (catégories, jalons, rétention) — seulement DOM-011 (DOC) ; AUDIT/PLATFORM à compléter.

### Synthèse
- Panneau réorganisé : Nature → Class → modèle du système → allocations (organisation + personne) → validation.
- Vues distinctes PM Turnkey / système / contributeur / lecture seule.
- Onglet Versions et journal d'activité partagé avec Compliance.

## Versions, colonne Changes et vue Document (dont SPEC-document-view)
Où lire aujourd'hui : `LIFECYCLE.md` (LIFE-006, 011 à 016, LIFE-T10 à T14), DEC-069 à 072, DEC-119 ; `docs/specs/SPEC-document-view.md` (30 sept., prototype autonome) — au 8 sept. : `SPEC-versions-qa.md` (déjà marqué SUPERSEDED), mode Compare du prototype (non spécifié)

### Nouveau
- (R) **Une version appartient à un document, pas au tender** (DEC-069, LIFE-012, LIFE-T10) — plus de pastille « v2.1 active » ; chaque document avance à son rythme.
- (R) **Lecture des changements dans la vue Document, sans mode dédié** (DEC-119, LIFE-013) — le navigateur a deux onglets **Outline** et **Changes** : choix du document, de la version de départ (comparée à celle en vigueur), compteurs, chaque changement avec son effet sur le travail déjà fait (réponse rouverte, allocation à faire, travail archivé), liste filtrable par type ou sur « reopens an answer », navigation ] / [ ; le papier montre les changements en place ; le panneau reste celui de l'exigence. Un document à une seule version le dit (LIFE-T11).
- (R) **Exigences supprimées visibles seulement sous Changes** (LIFE-006).
- (R) **Colonne Changes dans la table** (LIFE-016) — voir domaine Tableau.
- (R) **SPEC-document-view.md** — spec d'un **prototype autonome** : afficher le **PDF original intact** et dessiner les blocs capturés par-dessus (pdf.js, zones par page, lecture du texte capturé, reclassement, export JSON ; ni découpe ni fusion à la main). **Non construit dans le prototype** (aucun pdf.js dans `revue-documentaire.html`). Si l'essai convainc, il **remplacerait la vue Document d'Allocation** ; Compare garderait une forme texte, à concevoir (§13.4). Hors périmètre : statuts, allocation, compare. Critères DV-T01 à DV-T14 ; décidé le 30 sept. : un bloc par phrase par défaut, « will / should / is to be » comptent comme obligations.

### Modifié
- (R) **Comparer** — Avant : 3ᵉ mode « Compare » (barre statique : sélecteurs de version inertes, résumé et navigation codés en dur, diff stocké dans le texte) → Maintenant : onglet Changes de la vue Document, un document à la fois (DEC-070), comptes et diff **calculés** ; plus de mode Compare.
- (R) **Traitement d'un changement** — Avant : états New / Reviewed / Action required → Maintenant : l'exigence ajoutée ou modifiée repasse **To review** ; la valider traite le changement (DEC-072, LIFE-015, LIFE-T13).
- (R) **Vue Document** — titre de la première page = tender ouvert (plus STB-2026 partout) ; puce de nature en pointillés quand l'IA n'est pas sûre (DEC-073) ; sélecteur de nature inactif pour un contributeur (DEC-086) ; marqueur « Unassigned » ou « n/m assigned ».

### Retiré / abandonné
- (X) **Mode Compare** et sa barre (DEC-119), **pastille de version du projet** (DEC-069), **fiche de changement** (DEC-072).

### Toujours ouvert
- **Relance automatique des modèles sur une nouvelle version** (DEC-027, LIFE-011) et **réouverture des verdicts** (DEC-122, côté Compliance) — non démontrées dans Allocation : les versions et historiques y sont des données de démonstration propres à l'écran, qu'un téléversement dans Documents ne modifie pas (déduit de la lecture du code).
- **Devenir de la vue Document** — dépend de l'essai SPEC-document-view (§13.4).

### Synthèse
- Versions par document ; changements lus dans la table (colonne Changes) et dans la vue Document (onglet Changes) ; plus de mode Compare.
- Un changement = retour en To review, rien d'autre.
- SPEC-document-view : spec d'un prototype séparé, rien à implémenter dans Allocation pour l'instant.

# Partie 4 — Compliance et Risks

> Rappel de lecture. Au 8 sept. (14:14) le développeur ne disposait que de `docs/specs/SPEC-*.md`, du glossaire, de `docs/decisions/DECISIONS.md` (D1–D15) et des tickets. Ces sources étaient déjà contradictoires sur la conformité : `TICKET-merge-expert-space-into-compliance.md` et `GLOSSARY.md` disaient « deux verdicts, R&D en commentaire », alors que `SPEC-domain-model.md` §3/§9.2 et D8 disaient « trois verdicts, `rnd_needed` comptable ». `SPEC-followup.md` et `SPEC-expert-space.md` étaient marqués SUPERSEDED. Le code de référence était `compliance.html`.
> Depuis le 8 sept. (16:43), la référence est `docs/current/*.md` ; les décisions DEC priment (`docs/current/README.md`). **Attention** : plusieurs lignes de `docs/current/COMPLIANCE.md`, `DOMAIN.md`, `ACCESS.md` et `PLATFORM.md` décrivent encore l'état du 8 sept. et sont contredites par des DEC plus récentes. Elles sont listées dans la rubrique « Toujours ouvert » du premier bloc.

## Modèle de conformité (verdicts, consolidation, ce que reçoit le client, droits)
Où lire aujourd'hui : `docs/current/OPEN-QUESTIONS.md` (DEC-028, DEC-031, DEC-039, DEC-087, DEC-092, DEC-105 à DEC-108), `docs/current/COMPLIANCE.md` (CONF-001, CONF-002, CONF-004, CONF-009 à CONF-013, CONF-028, CONF-029), `docs/specs/SPEC-risks.md` (§8 et le bandeau de réconciliation en tête), `docs/current/ACCESS.md` (ACC-007, ACC-009, ACC-011, ACC-013, ACC-014), `docs/current/TENDER-PROFILES.md` (conformité SIG, TYPE-T08) — au 8 sept. : `docs/specs/SPEC-domain-model.md` §1–§5, §9, §9.2 ; `docs/tickets/TICKET-merge-expert-space-into-compliance.md` §2 et §4 ; `docs/GLOSSARY.md` ; `docs/decisions/DECISIONS.md` (D6, D7, D8, D13) ; `SPEC-backend-requirements.md` FR5–FR6.

### Nouveau
- (R) **Deux axes de conformité : interne et externe** — l'interne est le verdict technique du contributeur, par affectation. L'externe est ce que le client reçoit. Il est **dérivé par affectation** : interne Compliant → externe Compliant ; interne Not compliant → le résultat externe de la stratégie d'écart choisie, Pending tant qu'aucune n'est choisie. Personne ne le saisit directement ; seul le PM peut le corriger (puce suivante). (DEC-106 ; SPEC-risks §8 ; `4a6015f`)
- (R) **Consolidation de l'externe au niveau exigence** — Not compliant l'emporte, puis Pending, sinon Compliant. Rien n'est affiché tant que l'interne n'est pas consolidé (au moins une affectation sans verdict). (SPEC-risks §8 ; observé dans `externalOf()`)
- (R) **Correction de l'externe par le chef de projet**, par affectation. Valeur au choix (Compliant / Not compliant / Pending), **motif obligatoire et visible de tous**, affichée « corrigée par le PM » avec la valeur dérivée à côté, réversible vers la valeur dérivée. Une correction survit à un changement du résultat de la stratégie. (DEC-106, DEC-111 ; ACC-011)
- (R) **Stratégie d'écart et risque sur chaque Not compliant**, non bloquants : voir le bloc « Stratégies d'écart, risques ». Ils déterminent l'externe. (DEC-105, DEC-108 ; CONF-029)
- (R) **Responsabilité : la personne assignée** — c'est elle qui répond et qu'on relance. Il n'y a pas de responsable de suivi global, ni par exigence ni par système. Plusieurs personnes dans un périmètre font plusieurs entrées OBS, chacune avec sa personne. (DEC-087, qui remplace DEC-010 ; DOM-004, DOM-006)
- (R) **Une personne appartient à un seul système.** Les sélecteurs de personne, en réaffectation comme en renvoi, ne proposent que les membres du système de l'affectation. (DEC-102 ; ACC-014 ; `5db101e`)
- (R) **Tender SIG autonome** : il n'y a pas de niveau système dans Compliance. La consolidation va des équipes à l'exigence, avec une affectation par exigence, et l'axe système est absent de la table, des filtres et du panneau. (DEC-044 ; TENDER-PROFILES ; TYPE-T08 ; `dcd6449`)
- (R) **Périmètre du premier pilote** : il s'arrête à la validation de l'allocation. La conformité, Q&A et l'export client sont spécifiés pour la suite, sans être des conditions d'acceptation du pilote. (DEC-022 ; `docs/current/README.md` ; PLATFORM « Borne de pilote »)

### Modifié
- (R) **Échelle des verdicts.** Avant : le corpus se contredisait (ticket de fusion et glossaire : deux valeurs ; SPEC-domain-model §3.1/§9.2 et D8/D13 : `compliant` / `rnd_needed` / `not_compliant`), Allocation était codée à trois valeurs plus `pending`, et la légende de la vue Document de Compliance affichait encore « Partially » et « Needs clarification ». → Maintenant : **deux verdicts internes partout**, `compliant` et `not_compliant`. « R&D needed » est une mention écrite dans le commentaire d'un Compliant, pas un verdict. Il n'y a plus de conversion R&D → Compliant à l'export. (DEC-031, qui remplace DEC-001 et rend DEC-024 sans objet ; `22d651b`)
- (R) **Qualification d'un Not compliant.** Avant : Category (liste) + Topic (texte), obligatoires sur tout Not compliant. → Maintenant : **Category + Topic sur un tender Turnkey seulement**. Ailleurs, ce sont la stratégie d'écart et le risque qui qualifient le Not compliant. La liste Category reste un placeholder explicite. (DEC-107, qui amende DEC-031 ; DEC-038)
- (R) **Ce qui part au client.** Avant : le verdict consolidé, avec un éventuel remplacement et verrou par le PM (SPEC-domain-model §5). → Entre le 14 et le 30 sept., une déclaration externe saisie par le PM, avec risque obligatoire quand l'interne est Not compliant (DEC-028 ; jamais dans la base du dev). → Maintenant : l'externe **dérivé de la stratégie**, corrigeable par le PM (DEC-106).
- (R) **Verrou du verdict final.** Avant : le PM remplace puis verrouille le verdict de l'exigence. Un verdict verrouillé est exclu de la re-dérivation, le verdict d'origine reste visible, le verrou est visible de tous, et le déverrouillage le recale (SPEC-domain-model §4–§5, D6). → Maintenant : **aucun verrou**, nulle part. Le PM ne remplace pas le verdict interne. (DEC-028, ACC-011 « il ne verrouille plus rien » ; SPEC-risks §10)
- (R) **Colonne Compliance d'Allocation.** Avant : sélecteur éditable par branche et par équipe, trois valeurs plus le verrou du verdict final. → Maintenant : **lecture seule**, Compliant / Not Compliant / Pending. Un verdict ne se saisit que dans Compliance. (DEC-039 ; `22d651b`)
- (R) **Effet d'une question au client sur la consolidation.** Avant : `awaiting_qa` comptait comme non répondu et bloquait la consolidation ; le contributeur ne pouvait pas répondre tant que la question était ouverte. → Maintenant : une question **ne bloque rien**. Le contributeur rend son verdict quand il veut, et l'affectation se consolide sur ce verdict, pas sur la réponse du client. Une affectation encore sans verdict laisse évidemment l'exigence en attente. (DEC-092 ; CONF-028 ; QA-010)
- (R) **Grain du verdict.** Avant : arbre équipes → activité → exigence, avec le verrou au sommet. Chaque feuille portait un manager et un expert (SPEC-domain-model §3.2/§4). → Maintenant : la même dérivation (le plus restrictif gagne, l'attente remonte), sans verrou. L'ABS et le PBS sont uniques, l'**OBS peut être multiple**, et chaque organisation (entrée OBS) a **une** personne et **son** verdict. Le système est calculé depuis ses équipes, jamais saisi. (DEC-014, DEC-037, DEC-055, DEC-060, DEC-087 ; CONF-002, CONF-004)
- (R) **Droits.** Avant : le PM fait le suivi global, remplace et verrouille. L'expert avait une restriction stricte à son activité et à ses descendantes (hiérarchie d'activités, modèle à deux surfaces : SPEC-expert-space, SPEC-domain-model §9, D7, D11). → Maintenant : un contributeur **lit tout le projet** et ne modifie que son système. Tous les contributeurs du système peuvent répondre, même si une autre personne est affectée. Il n'y a pas de hiérarchie d'activités. Le PM peut saisir et modifier des réponses. Un contributeur sans système assigné sur une exigence ne modifie rien. (DEC-002, DEC-012, DEC-013 ; ACC-007, ACC-009, ACC-011, ACC-013 ; CONF-010)
- (R) **Vocabulaire.** « Expert » et « manager » deviennent « contributor » (DEC-030). L'étape s'appelle « Compliance », plus « Follow-up » ni « Expert Review » (DEC-029). « Activity » devient « system » partout où l'utilisateur lit (DEC-045, qui remplace le vocabulaire de DEC-033). La liste des systèmes est celle de la capture, avec 16 codes dont le libellé est égal au code (DEC-032). Les identifiants de code gardent leur nom (`typology`, `manager`, `byRole:"expert"`).

### Retiré / abandonné
- (X) **« R&D Needed » comme verdict** comptable, et sa conversion à l'export. Il reste une mention dans un Compliant. (DEC-031)
- (X) **Remplacement et verrou du verdict final par le PM**, et le verdict d'origine conservé sous le verrou. (DEC-028)
- (X) **Déclaration externe saisie par le PM, champ « Risk accepted » et marqueur « ≠ internal ».** C'était l'état du 14–30 sept., remplacé par l'externe dérivé. Les règles CONF-016, CONF-017, CONF-020 et CONF-T17, écrites pour ce modèle, sont caduques. (DEC-106, qui remplace DEC-028)
- (X) **Hiérarchie d'activités pour les permissions**, restriction stricte de lecture de l'expert et modèle « deux surfaces ». (DEC-012 : lecture du projet entier, pas de hiérarchie interne)
- (X) **Les deux rôles manager / expert sur une même affectation.** Il y a une personne par affectation. (DEC-030, DEC-087 ; `b932fb4`)

### Toujours ouvert
- **Saisie et modification d'une réponse par le PM** — DEC-013, ACC-011 et ACC-T08 le permettent, et OPEN-14 rappelle que « les interfaces de réédition doivent refléter cette décision ». Le prototype ne l'offre pas : le PM ne saisit que le verdict d'un partenaire. Personne ne peut non plus réviser un verdict déjà donné, hors annulation (⌘/Ctrl+Z) et réouverture par une nouvelle version.
- **Verdict par organisation (OBS) ou par système** — CONF-004 et DEC-055/060/087 donnent un verdict par organisation, et le système est calculé. Le prototype Compliance saisit le verdict au niveau de l'affectation système ; les équipes n'y sont qu'affichées, avec des valeurs écrites à la main. Le contrat de données reste à aligner sur Allocation, qui porte plusieurs entrées OBS avec personne par système.
- **Périmètre de lecture du contributeur dans Compliance** — DEC-012/ACC-007 donnent la lecture de tout le projet. Le prototype limite la table du contributeur aux exigences qui ont une affectation de son système (écart déjà noté dans ACCESS « Écart avec la maquette »).
- **Liste Category** — le vocabulaire réel n'est toujours pas fourni ; le placeholder reste explicite (DEC-038, OPEN-04). Elle ne sert plus que sur Turnkey (DEC-107).
- **Règles périmées encore écrites — ne pas implémenter** :
  - `COMPLIANCE.md` : le tableau d'en-tête « trois verdicts / DEC-001 / DEC-024 », CONF-003, CONF-005, CONF-006, CONF-007, CONF-014, CONF-015, CONF-016, CONF-017 et CONF-020, les lignes « verrou » du tableau Transitions, CONF-T05, T06, T09, T11, T13, la seconde CONF-T15, et CONF-T17. La mention « Risk accepted » de CONF-022 et « Compliant en un geste » de CONF-023 sont aussi dépassées.
  - `DOMAIN.md` (axe « Conformité : trois valeurs internes… DEC-001 », DOM-009 « verrou »).
  - `ACCESS.md` (ligne de matrice « Remplacer/verrouiller le verdict final »).
  - `PLATFORM.md` (correspondance FR 5–6 « échelle interne DEC-001 et conversion client DEC-024 »).
  - `OPEN-QUESTIONS.md` (OPEN-01 : « tout écart … passe par la déclaration externe (DEC-028) » ; DEC-085 : cible N du PM « un Not compliant sans déclaration »).
  - `docs/stories/STORIES-extracted-from-prototype.md` §8, qui décrit l'état du 14 sept.

### Synthèse
- Deux verdicts internes, Compliant et Not compliant, partout ; R&D est une mention ; aucun verrou ; Allocation n'affiche la conformité qu'en lecture seule.
- Ce que reçoit le client est un **second axe dérivé** de la stratégie d'écart, par affectation puis consolidé (NC > Pending > Compliant). Le PM n'agit que par une correction motivée.
- La responsabilité est portée par la personne de chaque OBS. Une personne appartient à un seul système. Le contributeur lit tout le projet mais ne modifie que son système.
- `COMPLIANCE.md` mélange des règles du 8 sept. (trois verdicts, verrou) et des DEC récentes : se fier aux DEC d'`OPEN-QUESTIONS.md`.
- Compliance est hors du premier pilote (DEC-022), mais son modèle est désormais arbitré.

## Statuts d'une affectation et transitions (réponse, question au client, renvoi, relance, nouvelle version)
Où lire aujourd'hui : `docs/current/COMPLIANCE.md` (CONF-001, CONF-011, CONF-012, CONF-019 à CONF-021, CONF-028 ; tableau Transitions partiellement périmé), `docs/current/OPEN-QUESTIONS.md` (DEC-078, DEC-088, DEC-092, DEC-121, DEC-122, DEC-125), `docs/current/QA.md` (QA-006, QA-010), `docs/current/LIFECYCLE.md` (LIFE-007), `docs/current/ALLOCATION.md` (ALLOC-013) — au 8 sept. : `SPEC-domain-model.md` §2, §2.1 ; `SPEC-followup.md` §6–§8 (SUPERSEDED) ; `TICKETS-review-expert-batch4.md` B10 ; `TICKET-three-support-screens.md` (Q&A, « stale work flagged ») ; `SPEC-versions-qa.md` §6/§8 (SUPERSEDED).

### Nouveau
- (R) **Plusieurs questions au client par affectation**, sans qu'aucune bloque. L'affectation garde la liste de ses questions. (DEC-092)
- (R) **Une question posée depuis Compliance entre dans le registre Q&A du tender**, au statut « To send ». Le chef de projet l'envoie hors outil puis la marque « Sent » dans Q&A. Annuler l'action retire la question du registre. (DEC-088, précisé par DEC-116 ; QA-010)
- (R) **Compliance lit le registre Q&A.** L'état d'une question (« To send » / « Sent » / « Answer to confirm » / « Answered ») et la réponse du client sont ceux du Q&A. Une question posée depuis Compliance y reste visible et survit à la navigation. (DEC-122)
- (R) **Pas de question sur une affectation déjà répondue.** « Ask the client » est grisé, avec sa raison, et la touche Q est refusée. Une question ne change jamais le statut d'une affectation répondue. (DEC-121)
- (R) **Réouverture par une nouvelle version (LIFE-007)** — une version qui modifie une exigence rouvre ses verdicts dans Compliance. Chaque affectation répondue revient à « Awaiting answer » ; le verdict et le commentaire sont effacés ; la mention « Reopened by <document> <version> » s'affiche ; une notification et une entrée de journal sont créées. Les exigences inchangées ne bougent pas. Le nombre de réponses rouvertes annoncé par Documents est celui que Compliance rouvre. (DEC-016, DEC-122 ; LIFE-007 ; `8c748a3`)
- (R) **La relance est une seule action** — bouton, touche R et action groupée. Elle met à jour « Last follow-up » et s'inscrit au journal de l'exigence. Elle n'est possible que sur une affectation encore due par son contributeur (« Awaiting answer » ou « Awaiting Q&A », avec une personne assignée), et n'est jamais proposée au contributeur lui-même. En groupe, les affectations non éligibles sont sautées et comptées. (DEC-125 ; CONF-021)
- (R) **Ordre de ce qui est dû** — dans une exigence en attente, une affectation qui attend son contributeur passe avant celle qui a une question au client. Cela vaut pour le libellé de statut, le tri par statut et l'affectation ouverte par défaut. (DEC-125)
- (R) **Annulation de la dernière action** par ⌘/Ctrl+Z, même après disparition du message : verdict, verdict partenaire, question au client, renvoi, réaffectation, mise de côté. (DEC-085)
- (R) **Chaque état du panneau dit en une phrase ce qui est attendu**, « rien » compris, et l'action nommée est l'action primaire. (CONF-019, CONF-020)

### Modifié
- (R) **`awaiting_qa`.** Avant : on pouvait escalader depuis n'importe quel état, y compris une affectation répondue, qui passait alors en `awaiting_qa` et cessait de compter comme répondue. La question restait propre à Compliance, sans atteindre `qa.html` (SPEC-followup §6, code de base). → Maintenant : seule une affectation « Awaiting answer » passe à « Awaiting Q&A ». Une affectation « Proposed » ou retournée garde son statut. Une affectation répondue refuse la question. « Awaiting Q&A » est une information d'avancement. (DEC-092, DEC-121)
- (R) **Retour de la réponse du client.** Avant (SPEC-versions-qa §8, SUPERSEDED) : la réponse débloquait l'affectation, qui revenait à `awaiting_answer`. → Maintenant : rien n'est bloqué. Compliance affiche la réponse du client sous la question, et le statut ne change qu'au verdict du contributeur. QA-006 (« débloquer le travail associé ») n'a plus d'objet côté Compliance. (déduit de DEC-092 et du code)
- (R) **Renvoi par le contributeur** (« Not mine — return it »). Avant : « Request reassignment » avec les trois motifs B10, une personne ou une activité de remplacement, et un motif écrit obligatoire. → Maintenant : même mécanisme (ALLOC-013 ; CONF-011), mais la personne proposée appartient au même système (DEC-102). La demande part toujours dans la file d'approbation d'Allocation et s'inscrit au journal ; l'annuler retire la demande. Au niveau Turnkey, Allocation affiche « Reassignment requested » tant que la demande attend (DEC-104).
- (R) **Réaffectation par le PM dans Compliance.** Avant : choisir un « activity manager » et un « expert », puis retour à `awaiting_answer` avec un âge de 0. → Maintenant : **une seule personne**, membre du système, puis retour à « Awaiting answer » avec un âge de 0 ; la demande est marquée approuvée dans la boîte partagée. (DEC-087, DEC-102)
- (R) **Effet d'une nouvelle version.** Avant : « work made stale is flagged » — un drapeau `outdated` et la mention « Answered on outdated version » (TICKET-three-support-screens ; code). → Le 8 sept. : CONF-014 / LIFE-007 disent « déverrouiller et remettre pending ». → Maintenant : **réouverture** des verdicts (DEC-122). Il n'y a plus d'état « outdated ».
- (R) **Relances.** Avant : plusieurs chemins incohérents — R mettait à jour « Last follow-up », le bouton du panneau ne le faisait pas, « Remind all overdue » existait, et un contributeur pouvait se relancer lui-même. → Maintenant : un seul chemin, éligibilité contrôlée (DEC-125).

### Retiré / abandonné
- (X) **Statuts « overdue »** (5 jours sans réponse) **et « outdated version »** : pastilles, marques, filtres, tri, entrées de fil, « Remind all overdue ». L'âge reste affiché comme une donnée. (DEC-078 ; CONF-022)
- (X) **« Needs my action »** : réaffectations, et affectations débloquées par le client. Il est remplacé par la touche N, « prochaine exigence qui attend » (DEC-078, DEC-085).
- (X) **Le registre Q&A propre à Compliance** — brouillon / revue interne / envoi par lot / import du dossier / fusion des doublons. Il était déjà sorti de l'écran au 8 sept. ; son reliquat a été supprimé, et le registre est désormais `qa.html` seul, simplifié par DEC-116 (ni lot, ni fusion, ni file d'arbitrage). (`b3a195d` ; DEC-116)
- (X) **L'escalade d'une affectation répondue**, qui la rouvrait. (DEC-121)

### Toujours ouvert
- **`proposed`** — le prototype laisse un contributeur répondre à une affectation non encore envoyée. `COMPLIANCE.md` précise que cela « ne valide pas leur autorisation en production ». La règle cible n'est pas écrite.
- **Le statut `assigned`** existe dans le vocabulaire (`BST`) mais n'est produit par aucun flux.
- **Le canal de relance** (e-mail, notification interne) n'est pas défini. Le prototype se contente de dater « Last follow-up » (PLAT-005, OPEN-11).
- **La documentation d'écart d'un verdict rouvert** (stratégie, risques, correction PM) — rien ne dit si elle est conservée, archivée ou effacée quand une version rouvre le verdict, ou quand un Not compliant redevient Compliant.
- **La table Transitions de `COMPLIANCE.md`** décrit encore « Réponse requérant clarification → `awaiting_qa` » sans les restrictions de DEC-121, ainsi que deux transitions de verrou caduques.

### Synthèse
- Statuts : `proposed` / `assigned` / `awaiting_answer` / `awaiting_qa` / `reassignment_needed` / `answered`. « Overdue » et « outdated » ne sont plus des statuts.
- « Awaiting Q&A » ne bloque plus rien. Plusieurs questions sont possibles. Aucune question sur une affectation répondue. L'état et la réponse viennent du registre Q&A.
- Une nouvelle version qui modifie une exigence **rouvre** ses verdicts. Le décompte annoncé par Documents est celui que Compliance rouvre.
- Relance : une seule action, réservée au PM, sur une affectation encore due, datée et journalisée.
- Renvoi et réaffectation : une personne par affectation, prise dans le même système.

## Panneaux de détail : panneau de décision du contributeur et panneau du chef de projet
Où lire aujourd'hui : `docs/specs/SPEC-compliance-decision-panel.md`, précisé par DEC-079, DEC-080 et DEC-081 ; `docs/current/COMPLIANCE.md` (CONF-018 à CONF-025) ; `docs/current/PLATFORM.md` § « État personnel (DEC-090) » — au 8 sept. : `TICKET-merge-expert-space-into-compliance.md` §2–§5 (formulaire de verdict, onglets Document / REX / Chat, garde-fou « Ask the client » ≠ Chat) ; `SPEC-expert-space.md` (les trois profils rapide / lent / mal routé — supprimé du dépôt le 8 sept., consultable par `git show 5e7ae6b:docs/specs/SPEC-expert-space.md`).

### Nouveau
- (R) **Panneau de décision du contributeur**, quand il ouvre une affectation qui attend son verdict. On y trouve :
  - sa file : « N left · this is k of N », le nombre mis de côté et « Next » ;
  - le texte de l'exigence en entier, dominant, sous un titre « Requirement » ;
  - le lien § vers la section et « View in the document », qui bascule sur la vue Document sans fermer le panneau ;
  - la décision, puis deux actions secondaires plus discrètes, « Ask the client » et « Not mine — return it » ;
  - les ressources repliées : Q&A, Similar, REX, Chat.
  
  Le panneau du PM est distinct. (DEC-079, DEC-080 ; CONF-023, CONF-024)
- (R) **Choisir puis confirmer.** Deux choix, en vert et en rouge ; puis seuls les champs du choix fait ; puis **un seul bouton** « Confirm — <verdict> » ; « Change » permet de revenir. Compliant demande donc deux gestes, contrairement à la spec qui en voulait un seul. Not compliant ouvre la stratégie d'écart et le risque, puis Category + Topic sur un tender Turnkey. Le commentaire est facultatif ; pour un Compliant, il porte la mention R&D. (DEC-080, DEC-031, DEC-107)
- (R) **« Ask the client » ouvre un champ** pour écrire la question, que le contributeur rédige lui-même. Elle part au registre Q&A ; le contributeur garde la main et peut décider sans attendre. (DEC-080, DEC-088)
- (R) **Le brouillon s'enregistre tout seul** (choix, commentaire, catégorie, topic). **« Set aside »** est un marqueur personnel, posé par un bouton ou la touche S : il est filtrable par une pastille dédiée et se voit à la cellule ID teintée. Les deux sont **privés, côté serveur**, et suivent la personne d'un poste à l'autre ; ils n'entrent dans aucun compteur ni export. (DEC-079, DEC-081, DEC-090 ; PLATFORM « État personnel »)
- (R) **Le panneau s'élargit** à la demande (« Widen panel »), pour les textes longs, les figures ou les formules. (DEC-079 ; spec §4)
- (R) **Interrupteur « Original · <langue> »** sur le texte, quand le tender n'est pas en anglais. Une seule langue source par tender. (DEC-081, DEC-096)
- (R) **Ressource Q&A** : nos questions sur l'exigence, avec leur état, et les réponses publiées par le client aux autres soumissionnaires. (DEC-080)
- (P) **Ressource Similar** : les trois exigences du tender les plus proches, à au moins 25 % de mots communs, avec leur verdict. C'est un substitut en attendant la capacité de similarité de la plateforme ; le besoin, lui, est (R). (DEC-079)
- (R) **Arrivée du contributeur sur sa file** — ouvrir Compliance, ou changer de contributeur, ouvre la première affectation de sa file au lieu d'un panneau vide. (`e962c96`)
- (R) **Un verdict n'est affiché qu'une fois par portée** : celui d'une affectation n'apparaît que si l'exigence en a plusieurs (CONF-018). **Aucune action adressée à soi-même**, donc pas de relance chez le contributeur attendu (CONF-021).

### Modifié
- (R) **Formulaire de verdict.** Avant : bouton « Render a verdict », bascule Compliant / Not compliant, commentaire ou Category + Topic, puis « Save verdict » — le tout dans l'onglet Assignment, parmi les autres champs. → Maintenant : il vit dans le panneau de décision ; voir ci-dessus.
- (R) **Rôle de l'interne et de l'externe dans le texte du panneau.** Avant, dans la spec du panneau (§2) : « le pari commercial appartient au PM ». → Maintenant : le contributeur donne la vérité technique, et **la stratégie qu'il choisit sur un Not compliant décide de ce que le client reçoit** ; le PM peut corriger. (DEC-105, DEC-106 ; SPEC-risks §1/§3)
- (R) **Onglets du panneau PM.** Avant : Assignment / Activity / Requirement / Document / REX / Chat, pour tous. → Maintenant : Assignment / Activity / Requirement / REX / Chat. L'onglet Document a disparu (DEC-078), remplacé par la vue Document et « View in the document ». Le panneau de décision remplace la ressource Document par Q&A (DEC-080).
- (R) **Onglet Assignment du PM, par état :**
  - **répondu** : la réponse ; le verdict propre à l'affectation s'il y en a plusieurs ; la phrase d'attente ; la documentation d'écart, en lecture seule pour le PM sauf sur un partenaire ; le champ « External compliance » avec Correct / Revert ; « Ask the client » grisé ;
  - **Awaiting Q&A** : les questions avec leur état et la réponse du client, plus la relance ;
  - **retourné** : la réaffectation ;
  - **partenaire** : la saisie du verdict ;
  - **en attente** : la phrase d'attente et la relance.
  
  Avant : répondu → réponse et « Escalate to client Q&A » ; `awaiting_qa` → « Blocked on the issuer » ; retourné → deux sélecteurs ; en attente → relance.
- (R) **En-tête du panneau.** Avant : la pastille du verdict consolidé à côté de l'ID, plus « Δ outdated version ». → Maintenant : l'ID, avec « Pending consolidation » seulement quand l'exigence est en attente. Le bloc « What the client receives » essayé le 21 sept. a été retiré (DEC-078, qui remplace CONF-016).

### Retiré / abandonné
- (X) **Onglet Document** du panneau (DEC-078) et **bloc « What the client receives »** (DEC-078).
- (X) **La ligne « Activity manager: X »** et le second sélecteur de personne (fusion manager / expert ; `b932fb4`).
- (X) **« Frozen at review export » et « Type: Functional »** dans l'onglet Requirement (DEC-074 ; `8dd5f94`). **Le libellé « Escalate to client Q&A »** devient « Ask the client ».

### Toujours ouvert
- **Exigences similaires** : le classement, le nombre et la source (plateforme) restent à spécifier. Le prototype n'a qu'un substitut. (spec §8 ; DEC-079)
- **Set aside** : DEC-079 dit « ni filtre ni vue », DEC-081 ajoute une pastille-filtre. La règle écrite la plus récente, DEC-081, est celle que suit le prototype.
- **REX et Chat** sont hors V1 (DEC-021, OPEN-12) mais encore affichés : REX sur des exemples, Chat en simple bouchon.
- **Corps de `SPEC-compliance-decision-panel.md`** — il dit encore « Compliant takes one gesture » et place le pari commercial chez le PM. Ces deux points sont dépassés par DEC-080 et DEC-106.

### Synthèse
- Le contributeur a un **panneau de décision** dédié : texte dominant, choisir puis confirmer, deux sorties secondaires, ressources repliées, brouillon automatique, mise de côté personnelle, file avec « Next ».
- Brouillons et mises de côté sont des données **privées, côté serveur** (DEC-090) ; il faut les prévoir dans l'API.
- Le panneau PM est construit par état, avec une phrase « ce qui est attendu ». Le PM y corrige l'externe ; il ne saisit pas l'interne.

## Écran Compliance : table, navigation, vue Document, export, notifications, colonnes
Où lire aujourd'hui : `docs/current/COMPLIANCE.md` (CONF-009, CONF-022, CONF-025 à CONF-027), DEC-078, DEC-081, DEC-083, DEC-085, DEC-097 ; `docs/current/CUSTOM-COLUMNS.md` ; `docs/current/JOURNEYS.md` (JRN-003, UX-001 à UX-006) ; `docs/current/PLATFORM.md` (cloche, PLAT-006) ; TYPE-T08 — au 8 sept. : `SPEC-followup.md` §4–§7 (SUPERSEDED) ; `SPEC-review-table.md` ; `SPEC-advanced-filters.md` ; `TICKET-merge-expert-space-into-compliance.md` §1 (« même table, mêmes composants qu'Allocation »).

### Nouveau
- (R) **Ordre du document par défaut**, avec les titres de document et de section comme lignes. **Tri par les en-têtes** (montant, descendant, puis retour à l'ordre du document), colonnes personnalisées comprises, et « ↺ Document order ». Les tris autres que l'ordre du document sont à plat. (DEC-078, DEC-083 ; CONF-022, CONF-027)
- (R) **Colonnes** : ID, Requirement, System, Assigned to, Status, **Compliance**, Compliance comment, **Gap strategy**, **Risk**, **External compliance**, Last follow-up, Age, plus les colonnes personnalisées. System et Age sont masquées par défaut. Status (l'avancement) et Compliance (le verdict) sont deux colonnes distinctes. (`06efeea`, `4a6015f`)
- (R) **Lignes à deux niveaux** : exigence → une ligne par système, repliée derrière une flèche par exigence → une ligne par équipe quand un système en a plusieurs. (`5b5bd98`, `0cfc101` ; DEC-037)
- (R) **Filtres de colonne « à la Excel »** sur System et Assigned to, plus un **filtre avancé** (ET/OU, groupes) qui porte aussi sur l'interne, l'externe, la stratégie (dont « Strategy missing »), le risque (« Linked » / « Risk missing »), le statut, la personne, l'âge, le document et la section. (`8e83ca8`, `5b5bd98` ; UX-002, UX-003)
- (R) **Colonnes personnalisées partagées avec Allocation**, avec les mêmes valeurs. Une colonne est visible par défaut sur l'écran qui l'a créée et masquée sur l'autre, où le menu View l'affiche. Le PM crée, modifie et supprime ; toute personne du périmètre remplit. Elles sont facultatives et internes. (DEC-097, qui remplace la portée « une phase » de DEC-064 et DEC-081 ; DEC-067, DEC-068)
- (R) **Colonnes redimensionnables** — glisser, double-cliquer pour revenir au défaut, ou ←/→. Les largeurs sont retenues par tender et par table ; View permet de les réinitialiser. (`aac89b1`)
- (R) **Interrupteur « Wrap text »** pour afficher le texte complet. (DEC-078)
- (R) **Clavier** :
  - X coche la ligne active ;
  - Maj+↑/↓ (ou J/K) étend la sélection ;
  - ⌘/Ctrl+A sélectionne ce que les filtres montrent ;
  - Échap vide la sélection ;
  - N va à la prochaine exigence qui attend la personne : pour le contributeur, à décider (hors mises de côté) ou un Not compliant non documenté ; pour le PM, une réaffectation ou un partenaire ;
  - ⌘/Ctrl+Z annule ;
  - R relance ;
  - Q pose une question ;
  - S met de côté ;
  - aide au survol de l'icône ⌨.
  
  (DEC-085)
- (R) **Export avec options** :
  - format Excel / CSV / PDF ;
  - lignes : tout / ce que montrent les filtres, avec le filtre dit en clair / la sélection ;
  - colonnes au choix, les colonnes personnalisées étant décochées par défaut et marquées « internal » ;
  - langue du texte : original ou anglais.
  
  (DEC-081, DEC-082 ; CONF-025, CONF-026)
- (R) **Cloche de notifications calculée** depuis l'état de l'écran. Elle résume par nature, avec un compte : affectations retournées à réaffecter, questions en cours chez le client (pour information), réponses rouvertes par une version. Elle dit « Nothing waiting on you here » quand rien n'attend. (PLATFORM.md § cloche ; `b3a195d`)
- (R) **Barre d'état** : le titre, l'anneau « N/M consolidated », le total des affectations, puis les pastilles answered / awaiting answer / awaiting Q&A / reassignment needed (et « set aside » pour le contributeur). « N of M requirements · K assignments shown » n'apparaît que sous un filtre. (DEC-081 ; `6b8d477`)
- (R) **Liens avec Risks** : une icône Risks dans l'en-tête. Une puce RSK ouvre le risque sur la page Risks. En venant de Risks, la table est filtrée sur les exigences d'un risque (bandeau effaçable) ou ouvre directement une exigence. (`b7161d3`)

### Modifié
- (R) **Navigation.** Avant : bascule « By section / By expert », avec des cartes par expert (compteurs, retard, « Remind ») ; panneau ouvert par défaut. → Maintenant : **par section seulement**, panneau replié par défaut. (DEC-081 ; `5b5bd98`, `14e3059`)
- (R) **Colonne Status.** Avant : une seule pastille par ligne — le verdict une fois répondu, sinon « Pending · N », ou « ⛔ Reassignment needed ». → Maintenant : l'avancement de l'affectation nommée en premier, plus « · N assignments » ; le verdict est dans la colonne Compliance, avec ✓ ou ✕, et « — » avant la réponse.
- (R) **Vert et rouge réservés au verdict** : un statut « Answered » ou « Reassignment needed » n'est plus coloré en vert ou en rouge. (`10821d4` — une règle visuelle qui fait office de spec)
- (R) **Barre d'outils.** Avant : recherche, « All experts », « All activities », la liste « Sort: … » et « Needs my action ». → Maintenant : recherche, puces de filtre actif, « ↺ Document order », Wrap text, « Filter ▾ », « ＋ Column », « View ▾ », ⌨. (`8e83ca8`, `0ae2983`)
- (R) **Portée par défaut du PM.** Avant : « My team only » actif à l'ouverture, ce qui masquait les autres systèmes. → Maintenant : tout le tender ; le chip devient un rétrécissement optionnel. (`1010d5a` ; spec de fusion §4)
- (R) **Un clic sur un en-tête.** Avant : il masquait la colonne. → Maintenant : il trie ; on masque par View seulement. (`f2129b1`)
- (R) **Vue Document.** Avant : une seule feuille « Technical Requirements Specification » ; légende à cinq états (Partially / Needs clarification compris) ; un Not compliant n'y était pas coloré. → Maintenant : **une feuille par document source**, légende Compliant / Not compliant / Pending, Not compliant en rouge. (`14e3059`)
- (R) **Barre d'actions groupées** : « Reassign contributor » amène à la première ligne sélectionnée, comme avant ; il n'y a pas de réaffectation en masse. « Send reminder » est réservé au PM et soumis à l'éligibilité de DEC-125.
- (R) **« Assigned to »** : une seule personne par affectation. « Multiple (N) » s'affiche sur une exigence à plusieurs systèmes ou un système à plusieurs équipes, et « PM · for partner » sur un partenaire. Avant : deux colonnes, Expert et Manager. (`b932fb4`)

### Retiré / abandonné
- (X) **Pastilles overdue / outdated, « Remind all overdue », « Needs my action », liste « Sort: … » et ordre « action needed first »**. (DEC-078, DEC-083)
- (X) **Bascule « By expert / By contributor » et raccourcis affichés en permanence dans la barre** — l'aide est passée dans l'icône ⌨. (DEC-081)
- (X) **Colonnes Expert et Manager en double.** (`b932fb4`)

### Toujours ouvert
- **Filtrage et tri côté serveur sur 100 000 lignes** (PLAT-006, UX-005, OPEN-08/13) — rien n'est prototypé.
- **Contenu de l'export client** — l'export ne distingue pas un mode « client » d'un mode interne. Rien ne dit quelles colonnes partent au client : l'externe seul ? l'interne ? Seule la règle « colonnes personnalisées hors export client » existe, et elle est « à confirmer » (DEC-068).
- **`CUSTOM-COLUMNS.md`** — le document se contredit : la portée commune de DEC-097 en tête et dans CUST-T12, la portée « une phase » dans « État du prototype », CUST-T01 et CUST-T11. DEC-097 prime.
- **« Retard ≥ 5 jours »** reste une mesure du tableau de bord (DEC-117, PLAT-008), alors qu'il n'est plus un statut dans Compliance (DEC-078). Les deux coexistent : une statistique d'un côté, pas un état de l'autre.

### Synthèse
- La table suit Allocation : ordre du document, tri par en-têtes, filtres de colonne et filtre avancé, colonnes personnalisées partagées, colonnes redimensionnables, mêmes raccourcis et annulation.
- Nouvelles colonnes : Compliance (le verdict) séparée de Status, Gap strategy, Risk, External compliance.
- Il n'y a plus d'« overdue », d'« outdated », de « Needs my action », de liste de tri, ni de navigation par expert.
- Export à options, cloche réelle, vue Document par document : ce sont les surfaces à reprendre.

## Stratégies d'écart, risques et conformité externe
Où lire aujourd'hui : `docs/specs/SPEC-risks.md` — **lire d'abord le bandeau de réconciliation en tête**, qui prime sur le corps ; DEC-105 à DEC-114 ; `docs/current/COMPLIANCE.md` CONF-029 ; `docs/current/ACCESS.md` ACC-011 ; Settings → Compliance — au 8 sept. : rien. Aucune notion de stratégie ni de risque ; seul le toast d'export « Risk summary included: N non-compliant » existait.

### Nouveau
- (R) **Stratégies d'écart propres à chaque tender**, écrites par le PM dans Settings → Compliance. Chaque stratégie a un **nom** et un **résultat externe** (Compliant / Not compliant / Pending). La liste est **vide à la création** du tender (les tenders de démo en ont quatre). Une stratégie utilisée ne se supprime pas, elle se renomme. **Changer le résultat d'une stratégie utilisée** recalcule les exigences concernées, après une confirmation qui annonce combien changent ; les corrections du PM sont conservées. (SPEC-risks §2.1 ; DEC-110, DEC-111)
- (R) **Après un Not compliant, le responsable choisit une stratégie.** Une ligne en lecture seule en dit la conséquence : « Declared to the client: <résultat> ». (SPEC-risks §3 ; DEC-105)
- (R) **Lier un risque, un existant d'abord.** Les suggestions sont classées : d'abord les risques déjà liés sous **le même chapitre**, puis le reste du tender. Chacune montre combien d'exigences y sont déjà liées, et une recherche texte filtre la liste. On ne crée un **nouveau risque** que si aucun ne convient. Une affectation peut porter plusieurs risques. Un même risque peut servir à plusieurs exigences avec des stratégies différentes : **la stratégie n'est pas sur le risque**. (SPEC-risks §4–§5 ; DEC-105, DEC-113, DEC-114)
- (R) **Un risque = sa justification et ses liens, rien d'autre.** La justification répond aux trois questions du modèle, en trois champs obligatoires : « There is a risk that… » / « The risk is caused by… » / « The direct impact of the risk will be… ». L'objet porte un ID `RSK-00001` propre au tender, son créateur, sa date et ses liens, qui sont dérivés et jamais saisis. Un risque appartient **au tender**, pas à un système. (DEC-113, DEC-114)
- (R) **Rien ne bloque.** Le Not compliant s'enregistre même sans stratégie ni risque. L'affectation est alors signalée « Strategy missing » ou « Risk missing », dans la table comme dans le panneau, filtrable et présente dans la file N. Sans stratégie, l'externe reste Pending. Un risque est attendu sur **tout** Not compliant, SIG compris : il n'y a pas de réglage « Risk logging » par système en v1. (DEC-108, DEC-109)
- (R) **Qui documente** : le responsable de l'affectation (un contributeur du système) choisit la stratégie et lie les risques, sur sa propre décision comme après coup. Le PM le fait pour un partenaire, et corrige l'externe partout. (SPEC-risks §1 ; DEC-106 ; ACC-011)
- (R) **Statistiques**, tirées des totaux que Compliance calcule :
  - la progression vers le client : Assigned → Internal compliance → **Not compliant logged** (Not compliant avec au moins un risque ÷ Not compliant) → External compliance ;
  - les Not compliant par stratégie, « Strategy missing » compris ;
  - les risques : leur nombre, le nombre de liens, les risques partagés, les plus liés ;
  - l'élément « What needs you now » compte les Not compliant sans risque ou sans stratégie.
  
  (SPEC-risks §9 tel qu'amendé ; DEC-108, DEC-113 ; la structure du tableau de bord relève de DEC-117 et DEC-118)

### Modifié
- (R) **SPEC-risks §1, « no PM override »** → le PM corrige l'externe, avec motif. (DEC-106)
- (R) **SPEC-risks §12.1** : la spec recommandait de laisser l'exigence « Incomplete » tant qu'un risque manquait → elle est **seulement signalée**, sans statut Incomplete. (DEC-108)
- (R) **SPEC-risks §12.2** : la spec recommandait une liste pré-remplie avec les quatre stratégies → **vide** à la création. (DEC-110)
- (R) **SPEC-risks §4.1, ordre des suggestions** : même chapitre → même activité → reste, devient même chapitre → reste du tender. (DEC-114)
- (R) **SPEC-risks §4.2, nouveau risque** : une description pré-remplie du modèle plus un poids à quatre niveaux, devient **trois champs obligatoires, sans poids**. (DEC-113)

### Retiré / abandonné
- (X) **Poids** (Negligible / Low / Medium / High), **statut Open / Closed**, **fil de commentaires**, **fusion de risques**, **panneau de détail**, **matrice poids × stratégie** et **statistiques par poids**. La fermeture d'un risque prévue par DEC-111 est annulée. Le travail sur les risques se fait hors de l'outil. (DEC-113)
- (X) **Champ Activity / système d'un risque** et ordre de suggestion par système. (DEC-114)
- (X) **Réglage « Risk logging » par activité** (« off pour SIG »). (DEC-109)
- (X) **Déclaration requirement-level du PM et texte « Risk accepted »** : remplacés par la stratégie et le risque lié (DEC-106, DEC-112). L'ancien cas « interne Compliant + externe Not compliant » ne peut plus naître d'une stratégie ; il ne subsiste que par une correction du PM. (déduit de SPEC-risks §10 et de DEC-106)

### Toujours ouvert
- **Modifier la justification d'un risque existant, ou supprimer un risque devenu inutile** : rien n'est spécifié depuis DEC-113, qui ne garde que justification et liens, et le prototype n'offre ni l'un ni l'autre. Le corps de la spec (§5 « Editing a shared risk ») n'est plus fiable sur ce point.
- **Hors v1 confirmé** (SPEC-risks §11) : la valeur interne « Over compliant », les économies et opportunités, les montants, la suggestion de risques par IA, l'approbation régionale de certaines stratégies, la réutilisation d'un risque entre tenders et son transfert vers la phase projet.
- **Sort de la stratégie, des risques et de la correction PM** quand un verdict est rouvert par une version ou repasse Compliant : non spécifié.
- **Références mortes** : SPEC-risks cite `SPEC-internal-external-compliance.md`, qui n'a jamais existé dans le dépôt (constat du commit `e4b1b31`).

### Synthèse
- Le cœur du module tient en un geste : **après un Not compliant, choisir une stratégie et lier un risque**, un existant d'abord. Tout le reste en découle : l'externe, les statistiques, la page Risks.
- Les stratégies sont par tender (nom + résultat externe), vides à la création et gérées dans Settings → Compliance ; changer le résultat d'une stratégie utilisée recalcule, après confirmation.
- Un risque n'est que trois phrases de justification plus des liens : pas de poids, de statut, de commentaires ni de fusion. Il appartient au tender.
- Rien ne bloque : les manques sont signalés, filtrables et comptés (« Not compliant logged »).

## Page Risks (écran de support)
Où lire aujourd'hui : `docs/specs/SPEC-risks.md` §6, à relire avec le bandeau (DEC-113, DEC-114) ; COMPONENTS.md « Risk List » — au 8 sept. : rien. L'écran n'existait pas.

### Nouveau
- (R) **Un écran de support au niveau du tender**, comme Q&A, Documents et Casting. On l'atteint par l'icône Risks de Compliance et par la carte Risks du tableau de bord. (SPEC-risks §6 ; `b7161d3`)
- (R) **Contenu : la liste des risques avec leur justification.** Colonnes : ID, les trois réponses en trois colonnes, les exigences liées (chacune ouvre Compliance sur elle ; « all → » ouvre Compliance filtrée sur ce risque), « Created by » avec la date. Une recherche porte sur l'ID et le texte ; l'export est simulé. (DEC-113 ; `93f80d9`)
- (R) **Création seulement depuis Compliance.** La page ne crée, ne modifie, ne délie ni ne supprime rien. Son état vide renvoie vers Compliance. (DEC-113)
- (R) **Arrivée depuis une puce RSK** dans Compliance : la ligne du risque est mise en évidence et amenée à l'écran.

### Modifié
- (R) **SPEC-risks §6.2, registre** (ID, description, poids, statut, activité, nombre de liens, date du dernier commentaire, filtres avancés, export filtré) → ID, les trois réponses, les liens, le créateur ; recherche ; ni filtre par statut, poids ou système. (DEC-113, DEC-114)

### Retiré / abandonné
- (X) **Matrice poids × stratégie** en tête de page, **panneau de détail**, **fermeture / réouverture**, **fusion**, **cloche**, **filtre par système** — tous prototypés le 30 sept., puis retirés le même jour. (DEC-113, DEC-114)

### Toujours ouvert
- **Filtres avancés et export filtré** « as on every table » (SPEC-risks §6.2) : rien n'est décidé pour la nouvelle liste. L'export du prototype est simulé et sans options.

### Synthèse
- La page Risks est une liste en lecture : un risque par ligne, ses trois réponses, ses exigences liées (qui ouvrent Compliance) et son créateur. Tout se crée et se lie depuis Compliance.

## Partenaires externes — côté Compliance
Où lire aujourd'hui : `docs/specs/SPEC-external-partners.md` (§3–§6), DEC-082, DEC-093, `docs/current/COMPLIANCE.md` CONF-026 — au 8 sept. : rien.

### Nouveau
- (R) **Tenders Turnkey seulement.** Le PM ajoute une entreprise partenaire à la liste OBS Turnkey depuis Settings → Allocation model. Elle apparaît comme un système partout où la liste sert, Compliance compris (colonne et filtre System). Elle a une **couleur propre** et une infobulle « added for this tender, not part of the Turnkey model ». Elle n'a ni passe 2, ni équipe, ni personne. (DEC-082 ; SPEC-external-partners §2)
- (R) **Le PM saisit le verdict du partenaire** au niveau système, à partir de ce que le partenaire a renvoyé (e-mail, Excel, appel), avec le même flux « choisir puis confirmer ». Un Not compliant demande Category + Topic (Turnkey). La stratégie et le risque y sont documentés par le PM, sans être bloquants (DEC-108). Le verdict consolide comme celui de tout autre système : pas d'exemption, pas de nouveau statut. (CONF-026 ; SPEC-external-partners §3 ; DEC-105)
- (R) **Provenance.** Elle se lit au système, sans champ dédié (option 6.1 (b)). Le responsable affiché est « PM · for partner » plutôt qu'un assigné vide (option 6.2). La réponse enregistrée dit qu'elle a été saisie par le PM à partir de la réponse du partenaire. (DEC-082)
- (R) **L'envoi au partenaire** passe par l'export « What the filters show », qui annonce le nombre de lignes et le filtre actif en clair. (SPEC-external-partners §4 ; CONF-026)
- (R) **Retrait d'un partenaire** : possible tant qu'aucune exigence ne lui est attribuée ; sinon il est refusé, avec le nombre d'exigences à réattribuer. Allocation et Compliance remontent chacune leur usage. (DEC-093)
- (R) **Pas de relance** vers un partenaire : il travaille hors de l'outil, et le suivi se fait directement. (DEC-125, déduit de « une personne assignée » ; code)

### Toujours ouvert
- **v2** : liste de partenaires partagée entre tenders (6.3), ré-import des réponses du partenaire, accès du partenaire à l'outil (SPEC-external-partners §5–§6).

### Synthèse
- Un partenaire est un système ajouté au tender Turnkey, sans modèle ni personne. Le PM saisit son verdict (et sa documentation d'écart), qui consolide normalement.

## Journal d'activité d'une exigence (partagé Allocation / Compliance)
Où lire aujourd'hui : pas de règle dédiée. Le besoin général est dans PLAT-003 et DOM-011 (audit : qui, quand, avant → après), et la mise en œuvre est décrite dans COMPONENTS.md « Activity Timeline » — au 8 sept. : `SPEC-followup.md` §5 (frise synthétisée) ; `SPEC-backend-requirements.md` FR5, FR23.

### Nouveau
- (R) **Un journal par exigence, commun à Allocation et Compliance.** Chaque changement y porte qui, quand, et avant → après. Il est filtrable par catégorie (Status, Allocation, Compliance, Comments) et dispose d'un champ de commentaire. Quatre jalons y sont marqués : Captured, Allocated, Answered, Declared to the client. Côté Compliance, il trace :
  - les verdicts, statuts et changements de personne ;
  - la stratégie, les liens et déliens de risques, et la correction PM ;
  - la consolidation, et ce qui est déclaré ou change pour le client ;
  - la question au client, le renvoi et la relance ;
  - la réouverture par une version.
  
  (`7a1d771` ; PLAT-003)

### Retiré / abandonné
- (X) **La frise fabriquée par écran** (auteur et date fixes, « export from Allocation », événement « Overdue threshold reached »). (`7a1d771`, `8dd5f94`)

### Toujours ouvert
- **Le périmètre exact de l'audit** (champs tracés, rétention, journal de session) relève d'OPEN-11. Aucune règle CONF ou PLAT ne fixe le contenu du journal de Compliance.

### Synthèse
- Le journal est la trace d'audit fonctionnelle d'une exigence, partagée entre les deux étapes. À construire côté serveur (PLAT-003), pas dans l'écran.

# Partie 5 — Documents et versions, Q&A, langue, capture, IA

Périmètre : de `5e7ae6b` (8 sept. 2026, 14:14) à `main` (`b675936`). Au 8 sept., aucune règle ne portait d'identifiant DEC/LIFE/QA/LANG/AI/CAPT : tous ces identifiants sont postérieurs (consolidation `7f50eda` du 8 sept. 16:43, puis ajouts). Les trois anciennes specs du périmètre (`SPEC-versions-qa.md`, `SPEC-qa-screen.md`, `SPEC-translation.md`) ne sont plus que des renvois ; leur texte d'origine est conservé tel quel dans `docs/archive/specs-2026-09-08/`.

## Documents, versions et cycle de vie des exigences entre versions
Où lire aujourd'hui : `docs/current/LIFECYCLE.md` (LIFE-004, LIFE-006 à LIFE-016, critères LIFE-T05/T06/T09 à T14), `docs/current/OPEN-QUESTIONS.md` (DEC-016, 017, 026, 027, 068, 069 à 072, 098, 119, 122 ; OPEN-07), `docs/current/AI.md` (AI-006, AI-011), `docs/current/COMPLIANCE.md` (CONF-014), `docs/current/JOURNEYS.md` (JRN-005), `docs/current/ACCESS.md` (matrice : « Gérer documents et relation client globaux ») — au 8 sept. : `docs/tickets/TICKET-three-support-screens.md` (« Screen 2 — Documents & versions »), `docs/specs/SPEC-backend-requirements.md` (FR12, FR16–17), `docs/specs/SPEC-domain-model.md` §8.6 ; `docs/specs/SPEC-versions-qa.md` était déjà marqué SUPERSEDED.

### Nouveau
- (R) **Une version appartient à un document, jamais au tender** — chaque document avance à son rythme, un écart se lit toujours entre deux versions d'un même document ; plus de version « de projet » affichée. (DEC-069 ; LIFE-012 ; LIFE-T10 ; `82ab34e`)
- (R) **Une nouvelle version qui modifie une exigence rouvre ses verdicts** : chaque affectation déjà répondue de cette exigence revient en attente de réponse (verdict effacé, consolidation de l'exigence à nouveau pending) ; les exigences inchangées ne bougent pas du seul fait de l'upload. Le nombre « N answers reopened » annoncé par Documents est exactement le nombre rouvert dans Compliance. (DEC-016 ; DEC-122 ; LIFE-007 ; CONF-014 ; LIFE-T05 ; `8c748a3`)
- (R) **Relance automatique des modèles nécessaires, sur les seules exigences modifiées** par la nouvelle version, selon le type de tender (jamais de passe 1 Turnkey sur un SIG) ; les nouvelles propositions restent à revoir/valider ; la relance ne rétablit ni les anciennes validations ni le verdict. Historique des anciennes décisions conservé pour l'audit, sans validité. (DEC-027 ; LIFE-011 ; AI-006 ; AI-011 ; LIFE-T09/T10)
- (R) **Ajoutée ou modifiée ⇒ To review**, sans état de traitement propre au changement : valider l'exigence est le traitement ; si un statut plus restrictif s'applique (allocation incomplète), c'est lui qui s'affiche. (DEC-072 ; LIFE-015 ; LIFE-T12/T13)
- (R) **Les changements se lisent dans Allocation, sans mode dédié** : (a) **colonne Changes** juste après Requirement — même exigence, mots supprimés barrés / ajoutés surlignés, comparée à une version antérieure de *son* document (la précédente par défaut, ou la première), sélecteur par ligne + sélecteur d'en-tête qui s'applique à toutes les lignes et remet à zéro les choix ligne par ligne, filtre Modified / Added / No change, touche **C**, visible par défaut dès qu'un document a plusieurs versions ; (b) **onglet Changes** du navigateur de la vue Document (choix du document puis de la version de départ, compteurs, chaque changement avec son effet sur le travail déjà fait — réponse rouverte / allocation à faire / travail archivé —, filtre par type ou « rouvre une réponse », navigation `]` / `[`), le panneau de droite restant celui de l'exigence. (DEC-119 ; DEC-070 ; LIFE-013 ; LIFE-016 ; LIFE-T11/T14 ; `73c7fe7`, `8365089`)
- (R) **Onglet Versions** dans le détail d'une exigence changée dans la version en vigueur de son document : ce qui a changé, depuis quelle version, le texte précédent (diff mot à mot) ; absent sur une exigence inchangée. (DEC-071 ; LIFE-014 ; LIFE-T12)
- (R) **Exigences supprimées par une version : visibles uniquement dans la comparaison** (onglet Changes), absentes de la vue courante ; l'historique n'est pas effacé. (DEC-017 ; LIFE-006 ; LIFE-T06)
- (R) **Fusion / scission** : les exigences résultantes s'ajoutent au document courant, décisions remises à zéro, relance automatique des modèles possible ; aucune décision ne se transfère à la nouvelle exigence. (DEC-017 ; LIFE-009 ; LIFE-T07)
- (R) **Les autres modifications passent par leur fonction dédiée** (réallocation…) : pas de remise à zéro globale à toute édition. (LIFE-010)
- (R) **Cloche de notification de l'écran** (règle transverse, aussi sur Q&A) : calculée depuis l'état réel de l'écran — ici, réponses rouvertes par la version en vigueur d'un document et documents pas encore traités —, résumée par nature avec son compte, et qui dit quand rien n'attend. (PLAT-008 ; `b3a195d`)
- (R) **Effets connexes** : valeurs des colonnes personnalisées **conservées** quand une version remet une exigence à zéro (défaut à confirmer, DEC-068) ; la carte Allocation du dashboard redevient « Current » dès qu'une exigence n'est plus allouée (nouvelle version, réouverture) (DEC-098) ; la relance globale au changement de modèle « écrase tout, réponses comprises, comme une nouvelle version » (DEC-050, ALLOC-015 — détail : partie Allocation).

### Modifié
- (R) **Effet aval d'une nouvelle version** — Avant (ticket Screen 2) : le travail rendu obsolète est *signalé* (« verdicts made stale ») et l'utilisateur va le confirmer ou le refaire dans Compliance → Maintenant : les verdicts des exigences modifiées sont **rouverts automatiquement** (pending) ; l'écran parle de « answers reopened » et renvoie vers Allocation › Document view › Changes et vers Compliance. (DEC-016 ; DEC-122 ; libellé `14e3059`)
- (R) **Comparaison** — Avant : mode Compare d'Allocation entre deux versions du tender (« v2.0 → v2.1 »), pastille de filtre « Changes v2.0 → v2.1 » dans la barre de statut (SPEC-domain-model §8.6), panneau de changement à états → Maintenant : un document à la fois, onglet Changes + colonne Changes, aucun état propre au changement. (DEC-069/070/072/119)
- (R) **Correction du texte ou de la traduction** — Avant : SPEC-translation §5 « pas de stale-work » (corrections mineures, faites avant le travail) → Maintenant : **toute** modification du texte ou de la traduction repasse l'exigence en revue, sans seuil majeur/mineur ; le retour en revue n'efface pas systématiquement les anciennes décisions. (DEC-026 remplace DEC-015 ; LIFE-008 ; LANG-004 ; LANG-T03)
- (R) **Écran Documents & versions** — le reste du ticket tient sous LIFE-004/JRN-005 : liste ordonnée, version courante et date, poids (nombre d'exigences), état de traitement, ajout à tout moment avec traitement IA après coup, nouvelle version qui remplace le document sur place (+ gap ajouté/modifié/supprimé), historique lisible par document, ordre éditable, suppression qui annonce ses pertes avant d'agir, export par document. **Gestion globale réservée à l'équipe projet** (pas à un contributeur au seul titre de son système). (LIFE-004 ; JRN-005 ; ACCESS ; TENDER-PROFILES DEC-005)

### Retiré / abandonné
- (X) **États de traitement d'un changement** (New / Reviewed, no impact / Action required) et action « Create action / reminder » depuis un changement. (DEC-072)
- (X) **Mode Compare** (troisième mode d'Allocation, barre Compare). (DEC-119)
- (X) **Version de projet** (pastille « v2.1 active » de la barre d'Allocation). (DEC-069)
- (X) **Statut « outdated version »** côté Compliance et réglage de re-signalement d'une réponse « outdated » : remplacés par la réouverture. (DEC-078 ; `14e3059`) — détail : partie Compliance.
- (X) **Réglage « notification des experts/contributeurs au changement de version »** (Configuration › Versions). (`14e3059`)

### Toujours ouvert
- **Identité d'une exigence entre deux versions** (qu'est-ce qu'une exigence « modifiée », correspondance en cas de fusion/scission) : besoin PROP (DOM-012), méthode non spécifiée ; le gap du prototype est simulé (`documents.html:uploadVersion`). (OPEN-07 ; DOM-012)
- **Sort de la documentation d'écart d'un Not compliant rouvert** (stratégie, risques liés, correction PM de la conformité externe) quand une version rouvre le verdict : non spécifié (déduit — le prototype efface verdict et réponse, laisse stratégie et risques).
- **« Repasser en revue » après une correction de traduction** sur une exigence déjà répondue : To review seulement, ou verdicts rouverts comme pour une version ? LIFE-008 dit seulement « pas d'effacement systématique ».
- **États de traitement d'un document** : l'écran ne connaît que Ready / Processing / Not processed ; AI-012 (PROP) demande aussi un état d'échec distinct et une reprise après incident sans doublon — non conçu.
- **Réglages affichés sans règle** : numérotation des versions (auto + alias / libre), « Detect addendum-as-answer », re-segmentation complète vs incrémentale à la nouvelle version, protection des corrections manuelles à la relance. (Configuration, « demo only »)
- **Incohérences doc** : `TICKET-three-support-screens.md` (non modifié) parle encore de « work made stale is flagged » ; LIFE-007 parle de « déverrouiller » alors que le verrou d'Allocation a disparu (DEC-028) — lire DEC-122 ; `LIFECYCLE.md` a deux critères numérotés LIFE-T10.

### Synthèse
- Une version = un document (DEC-069) ; plus de version de tender, plus de mode Compare : les changements se lisent dans la colonne Changes et l'onglet Changes d'Allocation (DEC-119).
- Exigence ajoutée/modifiée ⇒ To review, valider = traiter (DEC-072) ; ses verdicts sont rouverts en Compliance et le compte affiché par Documents est celui-là (DEC-016/122).
- Relance automatique ciblée des modèles sur les exigences modifiées, jamais sur les inchangées (DEC-027).
- Toute correction de texte ou de traduction repasse en revue, sans seuil (DEC-026) — l'inverse de SPEC-translation §5.
- Exigences supprimées : visibles seulement dans Changes ; fusion/scission : zéro décision héritée (DEC-017).

## Q&A avec le client
Où lire aujourd'hui : `docs/current/QA.md` (QA-001 à QA-010, critères QA-T03 à T07), `docs/current/OPEN-QUESTIONS.md` (DEC-012, 021, 088, 089, 092, 116, 117, 121, 122 ; OPEN-06), `docs/current/COMPLIANCE.md` (CONF-012, CONF-024, CONF-028), `docs/specs/SPEC-compliance-decision-panel.md` (« Ask the client ») — au 8 sept. : `docs/specs/SPEC-qa-screen.md` (identique à `docs/SPEC-qa-screen.md`), `docs/tickets/TICKET-three-support-screens.md` (« Screen 3 »), `docs/specs/SPEC-domain-model.md` §2, `docs/specs/SPEC-backend-requirements.md` FR19–20.

### Nouveau
- (R) **Une seule liste, deux vues avec compteur** : « Our questions » et « Other bidders », à la place des onglets Questions / Answers. On garde la recherche, le filtre par système et les deux dates (sur une ligne). (DEC-116 ; `47de775`)
- (R) **Statuts d'une question : To send / Sent / Answered**, plus « Answer to confirm » tant qu'une réponse importée incertaine attend sur la question : un clic l'accepte (→ Answered) ou l'écarte (→ reste Sent). (DEC-116 ; QA-002 ; QA-007)
- (R) **Le PM marque « envoyée » à la main**, une question ou une sélection, et peut revenir en arrière ; l'outil n'envoie rien ; l'export Excel (avec l'ID d'exigence ; dans le prototype, les seules questions à envoyer) ne marque rien. (DEC-116 ; QA-002 ; QA-003 ; QA-T07)
- (R) **La réponse du client s'affiche sous la question qu'elle concerne** ; les questions-réponses des autres soumissionnaires sont listées en lecture, avec l'exigence quand le lien est sûr, sinon « No requirement linked ». (DEC-116 ; QA-007)
- (R) **Une question posée depuis Compliance entre dans le registre du tender** (à envoyer), identifiée et liée à l'exigence et au système ; le contributeur ne l'envoie pas lui-même ; annuler (Undo) la retire du registre. (DEC-088 ; QA-010 ; `d6efd7f`)
- (R) **Une question ne bloque rien** : plusieurs questions peuvent être en cours sur une même affectation ; l'affectation se consolide sur le verdict de son contributeur ; « Awaiting Q&A » n'est plus qu'une information d'avancement. (DEC-092 ; CONF-028)
- (R) **Pas de question sur une affectation déjà répondue** : « Ask the client » grisé, touche Q refusée ; une question ne change jamais le statut d'une affectation répondue. (DEC-121 ; `8c748a3`)
- (R) **Compliance lit le registre Q&A** : l'état d'une question (To send / Sent / Answered) et la réponse du client sont ceux du Q&A ; une question posée depuis Compliance y reste visible ; les Q&A d'autres soumissionnaires liées à une exigence s'affichent dans l'onglet Q&A du panneau de décision. (DEC-122 ; DEC-080)
- (R) **« Ask the client »** ouvre une question écrite par la personne, sans bloquer la décision ; le libellé reste « Ask the client » pour ne jamais le confondre avec le chat. (DEC-080 ; QA-009 ; SPEC-compliance-decision-panel §3)
- (R) **Lecture** : un contributeur consulte tout le projet, autres systèmes compris — tranche l'ancienne question ouverte « périmètre de lecture du Q&A ». (DEC-012 ; QA.md)
- (R) **Même Q&A pour Turnkey et SIG** ; Q&A hors borne du premier pilote (création → validation de l'allocation). (DEC-021 ; DEC-022 ; AI-007)

### Modifié
- (R) **Effet d'une question en cours** — Avant : une affectation en Awaiting Q&A **bloque la consolidation** (SPEC-domain-model §2, ticket Screen 3) et la réponse du client la débloque → Maintenant : ne bloque ni la consolidation (DEC-092) ni la relance d'une dérivation (DEC-089, remplace DEC-051).
- (R) **Cycle sortant** — Avant : un lot unique par tender, relu par le PM (revue interne, détection et fusion des doublons, exclusion de l'export sans notification), « envoyé » au moment de l'export → Maintenant : ni lot, ni revue interne, ni fusion, ni exclusion ; envoi marqué à la main question par question. (DEC-116, remplace QA-002)
- (R) **Retour du dossier** — Avant : file d'arbitrage PM (un élément à la fois, clavier, Skip, « No matching requirement », avance automatique) et tuiles de progression → Maintenant : pas de file ; l'incertitude est portée par la question (« Answer to confirm »), une Q&A d'un autre soumissionnaire sans lien sûr reste dans la liste. (DEC-116, remplace QA-007)
- (R) **Dates** — toujours deux dates optionnelles (clôture des questions, retour attendu) : absentes = rien d'affiché ; une question tardive n'est jamais bloquée ; retard visible. Maintenant sur une seule ligne. (QA-008 ; DEC-116 ; QA-T06)
- (R) **Import** — la règle tient (fichier ou contenu, extraction des paires Q/R depuis une mise en page quelconque, liens proposés vers nos questions ou vers des exigences pour les autres) mais l'écran n'offre plus qu'un bouton « Import the client's answers ». (QA-005)
- (R) **Liste des systèmes du filtre** : celle de la capture (16 codes, libellé = code) au lieu d'une liste à 5 valeurs inventée. (DEC-032 ; DEC-045 ; `2a7aa6b`)
- (R) **Vocabulaire** : « issuer » → « client » ; « competitor » → « other bidders ».

### Retiré / abandonné
- (X) **Revue interne avant envoi, détection/fusion des doublons, exclusion de l'export**, carte « Export the batch », tuiles de progression, file d'arbitrage, liste « Resolved & context », onglets Questions/Answers. (DEC-116)
- (X) **Question ouverte « notifier un contributeur dont la question est exclue »** : sans objet, l'exclusion n'existe plus. (DEC-116 ; ancienne SPEC-qa-screen §7.3)
- (X) **« Une question bloque exactement une affectation »**. (DEC-092)
- (X) **Réglages Configuration › Q&A** « AI duplicate detection » et « Internal review before sending » (reste « Issuer channel »). (`14e3059`)

### Toujours ouvert
- **Origine des deux dates** (saisies à la création, dans les paramètres, ou lues dans les documents) : non tranché ; le prototype les écrit en dur. (ancienne SPEC-qa-screen §7.1)
- **Format réel du dossier de réponses du client** : à obtenir avant de construire l'extraction ; extraction et rapprochement restent simulés. (QA-005 ; ancienne §7.4 ; OPEN-10)
- **Plusieurs vagues / plusieurs dossiers importés** : QA-004 décrit un seul cycle ; depuis DEC-116 il n'y a plus de lot ; non spécifié. (QA-004 ; OPEN-06)
- **Ce que change l'arrivée de la réponse** : QA-006 / QA-T03 / CONF-T08 parlent encore de « débloquer » ; depuis DEC-092 rien n'est bloqué. L'état d'avancement de l'affectation après réponse et la notification du contributeur ne sont pas spécifiés (PLAT-005).
- **Seuil de certitude** d'un rapprochement « à confirmer », et **rattachement manuel** d'une Q&A « No requirement linked » à une exigence : non spécifiés.
- **Droits** : seul le PM marque « envoyée » (DEC-116) ; import et export : non précisés (déduit : PM, « relation client globale » de ACCESS).
- **Incohérences doc, à ne pas suivre** (toutes antérieures à DEC-116) : QA-010 (« le PM la fusionne… l'envoie avec le lot »), DEC-088 (« la fusionne et l'envoie par lot »), JRN-006 (« PM prépare le lot… arbitre les associations »), QA-T05 (« passer un arbitrage »), paragraphe « DEC-021 : aucune action lors de l'exclusion », README (« arbitrage ») ; `docs/SPEC-qa-screen.md` est une copie intégrale de l'ancienne spec, restée hors archive.

### Synthèse
- Le registre devient une liste à deux vues (Our questions / Other bidders) avec trois statuts + « Answer to confirm » ; plus de lot, de revue interne, de doublons, d'exclusion, ni de file d'arbitrage (DEC-116).
- « Sent » est un geste manuel du PM ; l'export n'envoie et ne marque rien.
- Une question ne bloque plus rien (DEC-092) et ne peut plus être posée sur une affectation répondue (DEC-121).
- Compliance et Q&A partagent le même registre : questions posées depuis Compliance, statuts et réponses visibles des deux côtés (DEC-088/122).
- Restent ouverts : origine des dates, format du dossier client, plusieurs vagues, effet de la réponse sur l'avancement.

## Langue et traduction
Où lire aujourd'hui : `docs/current/LIFECYCLE.md` §Langue (LANG-001 à LANG-005, LANG-T01 à T03) et LIFE-008, `docs/current/AI.md` (AI-003), `docs/current/OPEN-QUESTIONS.md` (DEC-015, 019, 026, 081, 096 ; OPEN-09) — au 8 sept. : `docs/specs/SPEC-translation.md`.

### Nouveau
- (R) **Une seule langue source par tender** : pas de dossier multilingue ; un document ajouté en cours de projet est dans la langue du tender et suit capture → traduction → caractérisation. (DEC-096 ; OPEN-09 ; ferme l'ancienne question §8.2)
- (R) **Interrupteur « Original · <langue> »** dans le panneau de décision de Compliance : le texte de l'exigence tel qu'écrit dans le tender, en lecture seule. (DEC-081 ; `f6bdf9e`)
- (R) **Export du registre de conformité avec choix de la langue du texte d'exigence** (original ou traduction anglaise) ; commentaires et catégories restent en anglais. (DEC-081 ; CONF-025)
- (R) **Langue de travail fixe : l'anglais**, affichée non modifiable en Configuration › Language (à la place d'une « cible de traduction par défaut »). (DEC-019 ; LANG-001 ; `14e3059`)

### Modifié
- (R) **Séquencement** — Avant : question ouverte n°1 (pause pour revue de traduction, ou caractérisation sur une traduction non revue ?) → Maintenant : traduction automatique de confiance, **sans validation intermédiaire**, puis caractérisation et allocation ; correction possible ensuite. (DEC-019 ; LANG-002 ; AI-003 ; OPEN-09 ; LANG-T01)
- (R) **Correction d'une traduction** — Avant : onglet dédié, original et anglais côte à côte, correction tracée (qui, quand, quoi), **pas de remise en revue** → Maintenant : même principe de correction tracée et d'original immuable, mais **toute correction, même mineure, repasse l'exigence en revue**. (DEC-026 remplace DEC-015 ; LIFE-008 ; LANG-004 ; LANG-T02/T03)
- (R) **Export client** : la règle reste « texte d'exigence en langue originale, contributions en anglais, pas de retraduction » (LANG-003, DEC-019), mais DEC-081 rend la langue du texte choisissable à l'export (voir Toujours ouvert).

### Retiré / abandonné
- (X) **« Pas de stale-work après correction de traduction »** (SPEC-translation §5). (DEC-026)
- (X) **« Default translation target »** en Configuration › Language. (`14e3059`)

### Toujours ouvert
- **Langue par défaut de l'export client** : LANG-003 dit l'original ; le prototype propose original/anglais avec l'anglais coché par défaut (DEC-081) — à trancher.
- **Langue affichée par défaut dans les panneaux** : l'ancienne §4 disait l'anglais ; aucune règle courante ; Allocation met l'original en tête de son sélecteur « Read in », Compliance montre l'anglais avec un interrupteur.
- **Lecture dans d'autres langues** (sélecteur « Read in » vers une langue tierce) : besoin de l'ancienne §4, non redit dans LANG-* ; seulement simulé.
- **Mesure de la qualité de traduction** (nombre de corrections par tender, ancienne §7) : non reprise dans `docs/current` (archive seulement, cf. AUDIT).
- **Incohérence doc** : LANG-005 dit encore « aucune nouvelle décision sur les dossiers multilingues » alors que DEC-096 a tranché.

### Synthèse
- Une langue source par tender (DEC-096) ; anglais = langue de travail fixe ; traduction automatique sans étape de validation (DEC-019).
- Toute correction de traduction repasse l'exigence en revue (DEC-026) — l'ancienne règle « pas de stale » est morte.
- Nouveaux points d'accès à l'original : interrupteur dans le panneau de Compliance, choix de langue à l'export (DEC-081).
- À arbitrer : langue par défaut de l'export (LANG-003 vs prototype) et des panneaux.

## Capture et segmentation
Où lire aujourd'hui : `docs/current/CAPTURE.md` (CAPT-T01 à T04), `docs/specs/SPEC-document-view.md` (nouveau, brouillon de prototype autonome), `docs/current/LIFECYCLE.md` (LIFE-005, §Formats et images), `docs/current/AI.md` (AI-002), `docs/current/DOMAIN.md` (DOM-003, DOM-012), `docs/current/OPEN-QUESTIONS.md` (DEC-018, 032, 058, 073, 074, 086, 094 ; OPEN-07, OPEN-10, OPEN-12) — au 8 sept. : `docs/specs/SPEC-backend-requirements.md` (FR2, FR10, FR16, FR28–29), `docs/specs/SPEC-domain-model.md` §8.6, `docs/specs/SPEC-configuration.md` (« AI & segmentation »), `docs/tickets/TICKET-ai-uncertainty-display.md`, `docs/decisions/DECISIONS.md` (D4, D9, D14).

### Nouveau
- (R) **Réglages avancés de conversion**, appliqués avant le découpage en blocs, en tête de la section de configuration « Capture & segmentation » : *Conversion range* (toutes les pages / pages spécifiques, avec un champ pour dire lesquelles ; une page hors plage **ne produit aucune exigence**, ce n'est pas un filtre), *Default table conversion format* (Image / Dataframe), *Sentences in paragraphs* (comme la source — défaut retenu — / découpé), *Format of equations* (images / formules). La granularité de tableau (une exigence par ligne / tableau entier) se lit juste après le format de tableau : elle n'a de sens qu'en dataframe. Liste connue probablement incomplète. (CAPTURE.md ; CAPT-T01 à T04 ; `b2ac7af`)
- (R) **Images** : capturées et affichées, contenu ni lu ni caractérisé ; formats évoqués PDF texte/scanné, Word, Excel, échanges DOORS ; un PDF entièrement image est une limite d'ingestion à expliciter. (DEC-018 ; AI-002 ; LIFE-T08 ; OPEN-10)
- (R) **Nature d'un bloc = Information / Heading / Requirement**, rien d'autre ; titres et informations n'ont **aucun statut** (ni Incomplete, ni To review…) et n'entrent ni en caractérisation ni en allocation ; le doute de l'IA sur le type se signale sur la puce de type (pointillés) et choisir le type en place le confirme. (DEC-073 ; DEC-074 ; ALLOC-018)
- (R) **Pas de suppression manuelle d'un bloc capturé** : un bloc capturé par erreur se reclasse en Information ; seules les lignes dupliquées à la main depuis une image restent supprimables. (DEC-094 ; OPEN-07 ; ALLOC-023)
- (R) **Identifiant stable** lors d'une correction de type ; original et passage source conservés. (LIFE-005 ; DOM-003)
- (R) **Liste de référence des systèmes = codes réellement présents dans la capture** (colonne « Responsible Entity », 16 codes, libellé = code faute de légende), lus au niveau sous-système. (DEC-032 ; DEC-058)
- (R) **Brouillon SPEC-document-view (30 sept.)** : prototype autonome qui affiche le **PDF original intact** et dessine chaque bloc en cadre par-dessus (zones issues des positions du texte) — lecture du texte capturé, **reclassement seul** (ni découpe, ni fusion, ni déplacement de frontière), zones ignorées (en-têtes, pieds, numéros de page) hachurées, export JSON des blocs et de leurs zones ; règles de classement par mots-clés (shall / must / will / should / is to be…, doit / devra… en français) ; **« doubtful cut »** défini par règle (deux obligations dans des phrases différentes, ou exigence visiblement coupée), qui ne change jamais la nature ; une phrase = un bloc par défaut dans ce prototype ; **s'il convainc, il remplace la vue Document d'Allocation**. Critères DV-T01 à T14. (`7fb3faa` → `6e6ad8b`)
- (R) **Nature et classe appartiennent au chef de projet** : un contributeur ne les modifie nulle part (refus aussi côté logique). (DEC-086 ; ACC-012) — détail : partie Allocation.

### Modifié
- (R) **« Uncertain segmentation »** — Avant : drapeau issu d'un seuil de confiance IA (réglage 50–95 %, défaut 80 %), bannière sur la ligne, distinct des statuts (SPEC-domain-model §8.6) → Maintenant : toujours un drapeau distinct du statut (« Check boundaries ») ; SPEC-document-view en donne une définition par règles textuelles au lieu d'un seuil. (SPEC-document-view §5)
- (R) **Section de configuration** « AI & segmentation » → « Capture & segmentation », conversion en tête. (CAPTURE.md ; `b2ac7af`)

### Retiré / abandonné
- (X) **Correction manuelle de la découpe dans la vue document** : explicitement hors v1 de SPEC-document-view (« re-cutting stays in the capture »), alors que la maquette garde un mode Segmentation masqué. (SPEC-document-view §12)

### Toujours ouvert
- **Réglages de conversion** : liste complète ? granularité désactivée quand le format est « Image » ? modifiables après capture (re-capture avec avertissement chiffré, comme DEC-050) ou figés à la création comme le produit (DEC-049) ? (CAPTURE.md)
- **Défaut « Sentences in paragraphs »** : « comme la source » pour le produit (CAPTURE.md) contre « Split » choisi pour tester le prototype de vue document (SPEC-document-view §13.2).
- **Vue document sur PDF original** : le remplacement de la vue Document est conditionné à l'essai sur les PDF de l'utilisateur ; la comparaison de versions y garderait une forme texte, à concevoir. (SPEC-document-view §13.3–13.4)
- **Correction manuelle de la découpe dans le produit** : LIFE-009 décrit les effets d'une fusion/scission, mais rien ne dit si l'utilisateur peut découper/fusionner à la main (déduit).
- **OCR, tableaux/équations comme objets, lecture à deux colonnes** : hors v1 de la vue document ; PDF entièrement image : OPEN-10.
- **Connecteur DOORS direct** non confirmé ; formats, mappings et aller-retour d'import/export à contractualiser. (OPEN-12 ; PLAT-004)
- **Légende des 16 codes système** à fournir. (DEC-032)

### Synthèse
- Quatre réglages de conversion avant la segmentation, avec une plage de pages qui *supprime* (pas qui filtre) ; leur modifiabilité après capture reste à trancher.
- Un bloc est Information, Heading ou Requirement ; seuls les Requirements ont un statut (DEC-073/074).
- Un bloc capturé ne se supprime jamais : il se reclasse en Information (DEC-094).
- Nouvelle piste à suivre sans la confondre avec la cible : la vue document sur PDF original (SPEC-document-view), qui remplacerait la vue Document si l'essai convainc.

## IA : modèles, confiance, relances, retour d'expérience
Où lire aujourd'hui : `docs/current/AI.md` (AI-001 à AI-014), `docs/current/ALLOCATION.md` (ALLOC-006/007, ALLOC-014/015, ALLOC-019, ALLOC-023), `docs/current/PLATFORM.md` (PLAT-003, PLAT-008 « Corrections IA »), `docs/current/OPEN-QUESTIONS.md` (DEC-020, 021, 027, 040 à 043, 050 à 056, 075, 077, 089, 091, 099, 117, 120) — au 8 sept. : `docs/specs/SPEC-backend-requirements.md` (FR10–13, FR22), `docs/tickets/TICKET-ai-uncertainty-display.md`, `docs/specs/SPEC-domain-model.md` §8.2–8.3, `docs/specs/SPEC-configuration.md` (AI feedback).

### Nouveau
- (R) **Frontière** : la conception et l'entretien des modèles relèvent du chantier IA, pas des specs fonctionnelles, qui ne décrivent que le comportement du produit face aux résultats (formats d'API et contrats avec les responsables techniques). (DEC-020 ; AI.md)
- (R) **Confiance de la caractérisation = niveau Low / Medium / High**, pas un pourcentage ; affiché à côté de la nature et de la classe tant que la valeur est celle de l'IA (un choix humain n'en porte pas) ; **Low** envoie l'exigence en To review, Medium et High non. **Les modèles d'allocation** (routage Turnkey vers un système, ABS / PBS / OBS) **gardent leurs pourcentages**. Une capture portant encore des nombres se lit < 75 Low, < 85 Medium, sinon High. (DEC-120 ; AI-014 ; `e5ee6e3`)
- (R) **Règles de comportement conservées** : résultat rattaché au bon projet/document/version/élément, propositions et corrections distinguées (AI-001) ; étapes enchaînées automatiquement, la validation humaine de l'allocation restant la borne (AI-009) ; pas de modèle applicable = état explicite et traitement manuel, jamais le modèle d'un autre type en silence (AI-010) ; consolidation et permissions calculées par règles métier, jamais par un LLM (AI-013) ; intégration : échec / en cours / résultat disponible distincts, reprise après incident sans doublon (AI-012, PROP).
- (R) **Relances d'allocation** (famille de décisions, détail : partie Allocation) : relance sur l'exigence entière en choisissant le modèle, appliquée directement, n'écrase qu'ABS/PBS/OBS (pas la personne), bloquée par une réponse ou un verdict enregistré mais plus par une question au client ; relance en masse ; résultat identique silencieux (journal « same result ») ; relance globale au changement de modèle qui écrase tout ; changer nature ou classe **propose** une relance, rien n'est relancé tout seul. (DEC-040 à 043, 050 à 053, 056, 075, 089, 091 ; ALLOC-014/015/019/023)
- (R) **La mesure de l'IA sort du tableau de bord** (qualité de dérivation, taux de correction) : elle reste dans Configuration › AI feedback. (DEC-117 ; PLAT-008)
- (R) **REX / Chat hors V1**, même si la maquette les représente ; un chat de recherche et une question officielle au client doivent rester distincts. (DEC-021 ; AI-008 ; QA-009)

### Modifié
- (R) **Affichage de la confiance** — Avant (TICKET-ai-uncertainty-display) : ne jamais montrer la gradation, seulement l'état qui en découle (To review sous le seuil) → Maintenant : niveau affiché pour la caractérisation, pourcentage pour l'allocation, y compris la certitude du routage Turnkey à côté de l'étiquette du système (couleur IA sous le seuil). (DEC-120 ; DEC-077)
- (R) **Ce que le retour IA capte** — Avant : toute correction en Allocation (réassignation de personne, changement d'activité), avec une raison demandée quand l'IA était très confiante → Maintenant : l'IA ne propose plus de personne (un OBS est une organisation) ; le retour ne porte que sur la nature/classe, le système et une dérivation faible validée telle quelle ; plus de raison demandée. Dénominateur et règles de la mesure à définir. (DEC-054 ; PLAT-008 ; `14e3059`)
- (R) **IA et nouvelle version** — Avant (FR12) : une « gap analysis » sans effet décrit sur les modèles → Maintenant : relance automatique ciblée des modèles sur les seules exigences modifiées. (DEC-027 ; AI-006 ; AI-011)
- (R) **Confirmation des valeurs IA** — Avant : confirmation champ par champ (bouton « ✓ Confirm AI activity » sur le système détecté ; entre le 23 et le 29 sept., mention « Detected by the AI, not confirmed yet » + Confirm sur nature/classe) → Maintenant : valider l'exigence confirme ce que l'IA a détecté, une seule validation. (DEC-099 ; `f85841f`) — détail : partie Allocation.

### Retiré / abandonné
- (X) **Proposition IA d'une personne** (carte de proposition et boîte « Why ») : l'IA dérive une organisation, la personne est affectée ensuite. (DEC-054 ; `14e3059`)
- (X) **Indicateurs IA du tableau de bord**. (DEC-117) — détail : partie Pilotage.

### Toujours ouvert
- **Calibration** des niveaux et pourcentages : les scores de démo (`seed_demo_confidence`) ne mesurent rien ; relève du chantier IA. (AI.md)
- **Traçabilité des appels de modèles** (modèle, coût, position dans la chaîne — ancien FR22) : rangée dans PLAT-003, rétention et périmètre ouverts (OPEN-11).
- **Mesure « Corrections IA »** : dénominateur, revue effective, corrections répétées. (PLAT-008)
- **Incohérence doc** : `TICKET-ai-uncertainty-display.md` (non modifié) dit encore « do not surface the graded confidence » — DEC-120 prime.

### Synthèse
- Caractérisation : Low / Medium / High, Low ⇒ To review ; allocation : pourcentages (DEC-120).
- Les specs ne conçoivent pas les modèles (DEC-020) : elles fixent le comportement autour (rattachement, absence de modèle, reprise, validation humaine finale).
- Les relances d'allocation forment désormais une famille de règles à lire dans ALLOCATION (ALLOC-014/015/019/023).
- Le retour IA ne capte plus que nature/classe, système et dérivation faible validée ; la mesure quitte le tableau de bord (DEC-117).

# Partie 6 — Accueil, création, tableau de bord, statistiques, configuration, casting

Référence de départ : specs du 8 sept. 2026 (`5e7ae6b`). Référence d'arrivée : `main` (`b675936`). Les `docs/specs/SPEC-home|project-creation|dashboard|dashboard-statistics|configuration|team-management.md` ne sont plus que des renvois vers `docs/current/` (texte d'origine dans `docs/archive/specs-2026-09-08/`) ; les trois tickets de la zone (`TICKET-casting-screen-redesign`, `TICKET-tender-creation-rework`, `TICKET-three-support-screens`) n'ont pas changé. Toutes les DEC citées sont dans `docs/current/OPEN-QUESTIONS.md` ; DEC-001 à DEC-026 datent de la consolidation du 8 sept. 16:43, donc postérieures à la base.

## Accueil (My tenders)
Où lire aujourd'hui : `docs/current/JOURNEYS.md` (JRN-001) ; aucune spec active ne décrit la nouvelle page — le comportement n'existe que dans `accueil.html` et dans `COMPONENTS.md` (Home Hero, Continue Card, Onboarding Line, Home Section Head, Tender Card, Product Line Badge, Role Chip, Tender Line) — au 8 sept. : `docs/specs/SPEC-home.md`

### Nouveau
- (R) **Page d'accueil = porte d'entrée de l'outil** — bandeau : salutation selon l'heure avec le prénom de l'utilisateur, une phrase sur ce que fait SRM, ligne de rôles (« You lead N tenders as project manager and contribute to M »), boutons « New tender » et « How SRM works ». Source : code seulement, pas de règle dans `docs/current` (b862a20, 6 oct.).
- (R) **Carte « Pick up where you left off »** — reprend un tender en cours (dans la démo : celui marqué `primary`, sinon le premier tender ouvert et navigable) ; montre sa ligne en miniature et l'étape suivante chiffrée (« N requirements still to allocate » tant que tout n'est pas alloué, puis « N still to answer in Compliance ») ; toute la carte ouvre le tender. (b862a20)
- (R) **Bloc d'onboarding « How a tender travels through SRM »** — quatre stations (Capture, Allocation, Compliance, Submission), une phrase et « qui le fait » pour chacune, puis la liste des écrans toujours ouverts (Documents & versions, Q&A, Risks, Team casting). Masquable (« Got it — hide »), réouvert par « How SRM works » ; l'état masqué est une préférence de l'utilisateur (déduit ; la démo la garde dans le shell). (b862a20, 58781b0)
- (R) **Carte de tender reconstruite** — rangée du haut : badge de ligne produit (Turnkey, SIG, autres lignes), référence, puce de rôle ; puis le nom ; puis la « ligne du tender » en miniature : quatre stations Capture → Allocation → Compliance → Submission, la station courante nommée avec son compteur (Capture : % de traitement ; Allocation : alloués/total ; Compliance : conformités internes renseignées/total ; Submission : coche). (41de42d, 8f87319)
- (R) **Deux libellés de rôle seulement : Project manager / Contributor** — un rôle par personne et par tender (DEC-030) ; mêmes couleurs de rôle partout sur la page (PM marine, contributeur bleu). (8f87319, 4953fea)

### Modifié
- (R) **Avancement d'un tender sur sa carte** — Avant : badge d'étape (Processing / Allocation / Expert review / Q&A & Versioning / Submitted) + barre « done/total validated | answered | resolved » → Maintenant : ligne à quatre stations ; deux compteurs seulement, allocation puis conformité interne, bascule automatique quand 100 % des exigences sont allouées, sans bascule manuelle. (2dd1fb4, 41de42d ; ticket de corrections consolidé §1.1–1.5, non versionné dans le dépôt)
- (R) **Sous-titre et rôle** — Avant : « Tenders you lead as Bid Director » (point ouvert §11 sur le vocabulaire) → Maintenant : « N tenders » sous « My tenders » + ligne de rôles PM / contributeur dans le bandeau (DEC-030).
- (P) **Tenders navigables** — Avant : seul STB-2026 (Energy Monitoring System) s'ouvre, les autres sont bloqués par un toast → Maintenant : deux tenders construits, STB-2026 (Turnkey) et RFP-2026-114 (« Line 4 Resignalling — ETCS L2 », SIG, produit Mainline Wayside — DEC-044, DEC-061) ; les trois autres restent « Demo project — list & status only ». JRN-001 : ces limitations et les temporisations de traitement ne font pas partie de la cible.
- (P) **Tender en traitement** — inchangé sur le fond (non ouvrable depuis l'accueil, toast) ; pied de carte « Processing — opens when it completes ».

### Retiré / abandonné
- (X) **Indicateur de santé par tender** (on track / at risk / behind + note, issu de l'ancienne §2.1 des statistiques) — retiré (2dd1fb4). PLATFORM : aucun indicateur composite de santé ni pourcentage global sans définition métier.
- (X) **Compte à rebours sur la carte** (« N days left », seuils urgent ≤ 10 j / soon ≤ 25 j, « overdue ») — retiré (2dd1fb4, « no days remaining ») ; les jours restants ne sont plus que dans le hero du dashboard.
- (X) **Badge d'étape de la carte** — retiré, la ligne porte l'étape (8f87319).
- (X) **« Words you'll meet » (glossaire) et « Next submissions » (frise des échéances de tous les tenders)** — ajoutés puis retirés le 6 oct. (c2bb430 ; 1ba9f3d : difficile à lire, échéances non comparables sur une même ligne). Ne pas réintroduire.
- (X) **Ligne du tender en grand** sur le dashboard — essayée puis retirée (voir Tableau de bord) ; elle ne subsiste qu'en miniature sur l'accueil.

### Toujours ouvert
- **Aucune spec de la page d'accueil** — bandeau, carte Continue, onboarding et ligne ne sont décrits que par le code et `COMPONENTS.md` (déduit : à spécifier si on les reprend).
- **Reprise d'un tender en traitement** — l'accueil bloque son ouverture alors que la création ouvre son dashboard ; JRN-001 renvoie à OPEN-05.
- **Qui peut créer un tender** — « politique globale à préciser » (JRN-001).
- **Vocabulaire « Bid Director »** — encore dans l'identité de démo et dans le hero du dashboard ; l'ancien point §11 n'est pas refermé par écrit (DEC-030 fixe PM / Contributor).
- **Vue VIP / Admin transverse aux tenders** — besoin historique non détaillé pour le pilote (ACCESS).

### Synthèse
- L'accueil est devenu une page d'entrée (bandeau, reprise, onboarding) sans spec écrite : la référence est le code.
- La carte ne montre plus santé, compte à rebours ni badge d'étape : ligne produit, rôle (PM / Contributor) et une ligne à quatre stations.
- L'avancement d'un tender se lit sur deux compteurs : alloués, puis conformité interne renseignée.
- Deux tenders de démo sont navigables (Turnkey et SIG) ; le blocage « demo-only » reste un artefact de démo.

## Création d'un tender (assistant)
Où lire aujourd'hui : `docs/current/LIFECYCLE.md` (LIFE-001 à LIFE-003), `docs/current/JOURNEYS.md` (JRN-001), `docs/current/TENDER-PROFILES.md` (§ Systèmes, produits et modèles, dont « Fait au 21 septembre 2026 » ; TYPE-T01 à T06), `docs/current/CAPTURE.md`, DEC-004, DEC-047 à DEC-049, DEC-059, DEC-061, DEC-095, DEC-096, DEC-110 — au 8 sept. : `docs/specs/SPEC-project-creation.md`, `docs/tickets/TICKET-tender-creation-rework.md`

### Nouveau
- (R) **Types de tender de référence : Turnkey, SIG, Mainline, RSC (DEC-004)**, « Mainline » étant un produit SIG et non un système (DEC-047). Le type sélectionne la configuration et les modèles (DEC-007) ; un test ou parcours annonce toujours son type (TYPE-T06). Premier pilote : de la création à la validation de l'allocation, pour les quatre (DEC-022).
- (R) **Produit, ou combinaison pour un Turnkey (DEC-049)** — le champ « System » devient « Product » pour un tender spécialisé, « Combination » pour un Turnkey. Seuls les produits SIG sont connus : Urban, Mainline Wayside, Mainline Onboard (DEC-047, DEC-061) ; Turnkey : placeholder explicite tant que la matrice des combinaisons manque (DEC-048) ; autres lignes : placeholder « produits non fournis ». Le produit décrit ce que le tender est, se fixe à la création, sélectionne le modèle ; le modèle reste réglable dans les paramètres (ALLOC-015).
- (R) **Le produit est transporté jusqu'au tender créé** — il était collecté puis perdu, si bien qu'un tender créé dans l'application ne pouvait jamais avoir de clés ; corrigé : un SIG Mainline Wayside créé ouvre Allocation sur ses clés (TENDER-PROFILES ; b3a195d).
- (R) **Ligne produit et mode d'assistance IA fixés à la création (DEC-095)** — les paramètres les montrent en lecture seule ; une erreur se corrige en recréant le tender. Ferme la question du ticket « le choix peut-il changer après l'allocation ? » (OPEN-05).
- (R) **Une seule langue source par tender (DEC-096)** — tous les documents de l'étape 2 portent la langue choisie à l'étape 1 ; traduction automatique vers l'anglais sans pause (LANG-001/002).
- (R) **Étapes IA enchaînées sans pause de validation (DEC-018, LIFE-003)** — la validation humaine finale de l'allocation reste requise (AI-009).
- (R) **Un tender naît sans stratégie d'écart (DEC-110)** — la liste s'écrit ensuite dans les paramètres (voir Configuration).

### Modifié
- (R) **Lignes produit proposées** — Avant : Turnkey / RCS / SIG / INFRA / Rolling Stock / Services → Maintenant : Turnkey / RSC / SIG / Services (orthographe RSC, DEC-059 ; INFRA et Rolling Stock retirés le 6 oct., 2169056 ; « Rolling Stock » n'est validé ni comme système ni comme code, DEC-059).
- (R) **Conséquence annoncée sous la ligne choisie** — Avant : Turnkey résout vers une « activité » séparée technique / non technique, toutes les autres lignes vers une personne → Maintenant : Turnkey route vers des systèmes, chacun dérive ABS / PBS / OBS et la personne ; SIG dérive ABS → PBS → OBS puis la personne de chaque OBS (DEC-008, ALLOC-003) ; les autres lignes n'ont pas de modèle fourni et s'allouent à la main (ALLOC-005, AI-010).
- (R) **Textes des étapes IA (étape 3)** — Characterisation : Avant « type et domaine du bloc » → Maintenant nature du bloc (Information / Heading / Requirement, DEC-074) et classe technique / non technique, avec un niveau de confiance Low / Medium / High (DEC-120, AI-014) ; Allocation : Avant « quelle activité » → Maintenant routage vers les systèmes (Turnkey) ou dérivation ABS / PBS / OBS (mono-système).
- (R) **Réversibilité du mode** — Avant : « rien n'est irréversible, on peut relancer chaque étape » → Maintenant : mode figé une fois le tender créé (DEC-095).
- (R) **Vocabulaire** — « activity » → « system » (DEC-045) ; « Casting screen » → « Team casting » ; « review screen » → « Allocation » (DEC-029) ; nouvelles versions ajoutées « dans Documents & versions », par document (DEC-069).
- (P) **Créateur du tender** — Avant : « Bid Director — you » écrit en dur → Maintenant : l'identité courante fournie par le shell ; il reste premier membre non retirable de l'équipe de gestion (ACC-001/002).

### Retiré / abandonné
- (X) **Champ « System »** (Mainline, Urban / Metro, Tramway, Monorail, Multiple systems) — même niveau que la ligne produit dit deux fois (DEC-049).
- (X) **Lignes INFRA et Rolling Stock** (2169056).
- (X) **Drapeau « allocation validée » et méta-projet partagé posés à la création** (ancienne §7.2) — plus de jalon de finalisation (DEC-084) ; seuls le mode et le tender sont transmis.

### Toujours ouvert
- **Ligne « Services »** — encore proposée, absente des types de DEC-004 ; aucune décision (déduit).
- **Matrice des combinaisons Turnkey** (DEC-048), **produits RSC** (DEC-047 ne donne que des exemples), **rapport RSC / RST** (DEC-059) ; Mainline / RSC : particularités non fournies (OPEN-15).
- **Codes région** — toujours des placeholders (question ouverte du ticket).
- **Toggles par étape IA et mode** — la question du ticket (les deux coexistent) n'est pas tranchée ; DEC-095 fige « le mode d'assistance IA » sans dire s'il inclut les toggles.
- **Réglages de capture** — figés à la création comme le produit, ou modifiables avec avertissement chiffré : à trancher (CAPTURE.md).
- **Qui peut créer** (JRN-001) ; **reprise d'un tender en traitement** (JRN-001 → OPEN-05).

### Synthèse
- Toujours quatre étapes ; l'étape identité porte désormais ligne produit + produit (ou combinaison Turnkey), tous deux figés à la création.
- Lignes proposées : Turnkey, RSC, SIG, Services ; types de référence DEC-004 : Turnkey, SIG, Mainline (= produit SIG), RSC.
- Le mode d'assistance IA est figé à la création (DEC-095) ; une seule langue source par tender (DEC-096).
- Le tender créé doit porter son produit (il sélectionne le modèle et les clés), et commence sans stratégie d'écart.

## Tableau de bord du tender
Où lire aujourd'hui : `docs/current/JOURNEYS.md` (JRN-007), `docs/current/PLATFORM.md` (PLAT-008, règle de la cloche, § « Carte Allocation du tableau de bord »), `docs/current/TENDER-PROFILES.md` (TYPE-T07, T08, T10), `docs/specs/SPEC-risks.md` §6 et §9, DEC-035, DEC-044, DEC-084, DEC-098, DEC-116, DEC-122 — au 8 sept. : `docs/specs/SPEC-dashboard.md`, `docs/tickets/TICKET-three-support-screens.md`

### Nouveau
- (R) **Carte Allocation « Done » quand toutes les exigences sont allouées (DEC-098)** — redevient « Current » dès qu'une ne l'est plus (nouvelle version, réouverture) ; lue sur la progression réelle d'Allocation, jamais sur un clic. Compteur « N / M requirements allocated ».
- (R) **Rail « Always open » à quatre écrans** — Team casting, Documents & versions, Risks (nouveau : nombre de risques du registre, SPEC-risks §6), Q&A ; aucun n'est une étape ni n'en bloque une (TICKET-three-support-screens).
- (R) **Cloche calculée (PLATFORM)** — contenu calculé depuis l'état réel de l'écran, résumé par nature avec son compte (jamais une ligne par affectation), « rien ne vous attend ici » sinon ; un élément unique nomme son exigence. Sur le dashboard : exigences à revoir, OBS faibles, affectations en retard, dernière version reçue. (b3a195d)
- (R) **Nouvelle version racontée depuis l'upload enregistré (DEC-122, LIFE-007)** — l'élément « What needs you now » et le fil d'activité disent document, version, écart (+ajouts ~modifs −suppressions) et nombre de réponses rouvertes dans Compliance, d'après ce que Documents & versions a enregistré pour ce tender ; rien tant qu'aucun upload. (8c748a3)
- (R) **Demandes de réaffectation en attente, au niveau tender** — carte affichée seulement s'il y en a, chaque ligne mène à Allocation où le PM tranche (DEC-011, ALLOC-013 ; f21b2b5).
- (R) **Colonne de droite : « Recent comments » et « Answers by system »** — le fil de commentaires remplace Project health ; « Answers by system » (par sous-système sur un tender SIG) remplace la liste nominative des experts (DEC-118).
- (R) **Le hero suit le tender ouvert** — nom, BO-ID, ligne produit puis produit (une seule fois si identiques), volume d'exigences, jours restants du tender (TYPE-T10 ; 376c6a5, e962c96).
- (R) **Tender SIG autonome réel (DEC-044)** — sur RFP-2026-114, cartes, éléments d'attention, statistiques et casting lisent le contenu propre du tender (TYPE-T07) ; ce qui compare des systèmes est masqué (un seul système, TYPE-T08).
- (R) **Élément « Not compliant »** — compte les verdicts Not compliant et ceux qui n'ont pas encore de risque ou de stratégie (DEC-108).
- (R) **Élément Q&A** — « N questions to send — mark them as sent once they're out », vers Q&A : le PM marque les questions envoyées à la main, l'outil n'envoie rien (DEC-116, QA-003).

### Modifié
- (R) **Navigation par étapes** — Avant (spec) : rail de trois cartes d'étape, toutes ouvertes (Allocation / Expert follow-up / Versions & Q&A), plus des cartes Team casting et Expert Space → Maintenant : deux étapes, Allocation et Compliance (DEC-029), en parallèle (DEC-035) ; les écrans de support sont dans le rail « Always open » (le code du 8 sept. avait déjà deux étapes et Team casting / Documents / Q&A en support). Une ligne à quatre stations a été essayée le 6 oct. puis abandonnée (2a42509 : Capture est automatique, Submission est la fin ; seules deux étapes s'ouvrent).
- (R) **Écran à deux états (pré / post finalisation)** — Avant : quatre éléments d'attention, Compliance, Experts et taux de réponse visibles seulement après « Finalize allocation » → Maintenant : plus de finalisation (DEC-035, DEC-084, ALLOC-022) ; tout le contenu Compliance est visible dès le premier jour ; seul l'élément « Requirements still to validate » disparaît quand tout est alloué (DEC-098).
- (R) **Carte Team casting** — Avant : managers ayant complété leur équipe / total → Maintenant : systèmes ayant au moins une personne / total (« N / M staffed », « K pending ») ; un système sans manager n'est pas un trou (DEC-124).
- (R) **Retards de réponse** — l'élément n'est plus réservé à l'après-finalisation ; il nomme la personne à relancer (nom autorisé pour une relance, DEC-118) et compte les retards.
- (R) **Vocabulaire** — Expert → Contributor (DEC-030), Follow-up → Compliance (DEC-029), activity → system (DEC-045).

### Retiré / abandonné
- (X) **« Finalize allocation »** — élément « Allocation not finalized » et état « finalized » de la carte (DEC-084).
- (X) **Carte Expert Space** — l'espace expert est fondu dans Compliance ; `SPEC-expert-space.md` est supprimé.
- (X) **Project health** (Requirements, « Managers assigned » à 100 % en dur, Validated, Response rate) — remplacé par « Recent comments » ; le volume d'exigences passe dans le hero (f21b2b5).
- (X) **Barre de conformité dans la colonne** — doublon de Statistics (633685b) ; segment « Partial / R&D » sans objet (DEC-031).
- (X) **Liste « Experts » par personne** (avancement nominatif) — DEC-118.
- (X) **Rangée de KPI au-dessus des étapes** — ajoutée le 13 sept., retirée le 16 (633685b) : elle répétait les compteurs des cartes d'étape.
- (X) **Élément « questions awaiting internal review / possible duplicate »** — pas de revue interne ni de détection de doublons (DEC-116).
- (X) **Lien « View all » et entrée « Allocation milestone reached »** du fil d'activité — pas de jalon (DEC-084).

### Toujours ouvert
- **Chiffres encore écrits à la main** — Documents & versions, Q&A et « uncertain segmentations » ; la cible les calcule depuis les données persistées (PLAT-001) (déduit).
- **Notifications** — déclencheurs, destinataires, regroupement et relances non finalisés (PLAT-005, OPEN-11).
- **« Bid Director »** dans le hero (voir Accueil).
- **Borne du pilote** — DEC-022 s'arrête à la validation de l'allocation : la partie Compliance du dashboard est spécifiée « pour la suite ».

### Synthèse
- Deux étapes (Allocation, Compliance) qui tournent en parallèle ; aucune finalisation ; Allocation « Done » se lit sur les données (DEC-098).
- Quatre écrans de support toujours ouverts, dont Risks.
- Les récits « nouvelle version » viennent de l'upload enregistré pour le tender (DEC-122), plus d'une histoire v2.2 fixe.
- Plus aucun avancement par personne sur le dashboard ; santé, KPI et barre de conformité retirés.
- La cloche suit une règle écrite (PLATFORM) : calculée, résumée par nature, honnête quand rien n'attend.

## Statistiques du tableau de bord
Où lire aujourd'hui : `docs/current/PLATFORM.md` (PLAT-008, tableau des mesures), DEC-117, DEC-118 (et DEC-106, DEC-108, DEC-113, DEC-124), `docs/specs/SPEC-risks.md` §9 (amendé par DEC-113) — au 8 sept. : `docs/specs/SPEC-dashboard-statistics.md`

### Nouveau
- (R) **Trois onglets : Project, Allocation, Compliance (DEC-117)** — purement métier ; chaque bloc s'ouvre sur une phrase calculée, puis le chiffre ; chaque ligne mène à l'écran concerné.
- (R) **Aucune statistique ne mesure une personne (DEC-118)** — activité et réponses comptées par système et sous-système, chaque action pour le système sur lequel elle porte, quel qu'en soit l'auteur ; « actif cette semaine » se dit d'un système. Les noms restent là où le travail l'exige : qui relancer, qui a renvoyé une exigence, qui a créé un risque, qui est staffé. Motif : information-consultation du CSE, codécision du Betriebsrat, RGPD.
- (R) **Project › Timeline** — dates clés (réception, cut-off Q&A, réponses client attendues, soumission, aujourd'hui) et courbe % alloué / % répondu dans le temps, avec projection au rythme des 7 derniers jours, dite « à ce rythme », jamais comme un plan (PLAT-008 « Trajectoire » ; exige un historique).
- (R) **Project › Most active this week** — par système et sous-système, 7 jours glissants : exigences validées en Allocation (une fois par exigence), réponses (une fois par affectation), commentaires et questions ; jamais les modifications de champ (PLAT-008 « Activité de la semaine »). Tender à un seul système : classement par sous-système.
- (R) **Project › The team** — équipe de gestion, managers de système (« pas de manager sur X — contributeurs seulement »), contributeurs, systèmes sans personne, systèmes actifs cette semaine.
- (R) **Allocation › Where the requirements are** (Incomplete / To review / To validate / Allocated), **By system, with who is on it** (charge par système et qui y est ; trou seulement si personne, DEC-124 ; masqué sur un tender à un seul système), **Sent back for reallocation** (réallouées / maintenues / à décider, par motif, par demandeur — PLAT-008 « Réallocations »), **Work invalidated by a new version** (réponses rouvertes, affiché seulement si non nul).
- (R) **Compliance › Progress to the client** — Assigned → Internal compliance → Not compliant logged → External compliance, ouvert sur « ce que le client recevra » (SPEC-risks §9 ; PLAT-008 « Profil de conformité »).
- (R) **Compliance › Answers by system** (par sous-système sur SIG) — confiées / répondues, retards (âge ≥ 5 jours) et le plus ancien ; le nom n'apparaît que sur la relance (PLAT-008).
- (R) **Compliance › What the open requirements are waiting on** — chaque exigence ouverte dans une seule file : renvoyée pour réallocation (décision du PM), puis client (Q&A), puis contributeur (en retard au-delà de 5 jours, le plus ancien et chez qui), sinon non affectée (PLAT-008 « Attente »).
- (R) **Compliance › Not compliant by gap strategy** (+ « Strategy missing », DEC-108) et **Risks** (nombre, liens, risques partagés, les plus liés avec leur créateur — DEC-113, DEC-114).

### Modifié
- (R) **Organisation** — Avant : deux audiences, PM (« For you ») et stakeholders VIP (« For stakeholders ») → Maintenant : Project + un onglet par étape (DEC-117). Une version intermédiaire « par étape » du 16 sept. (d2793d2 : entonnoir passe 1 → passe 2, qualité de dérivation, file par contributeur…) a été remplacée.
- (R) **Profil de conformité** — Avant : barre empilée Compliant / R&D needed / Not compliant / Pending → Maintenant : une phrase de « Progress to the client » (Compliant / Not compliant / pas encore réglé) ; deux verdicts internes (DEC-031) ; l'inconnu reste toujours montré.
- (R) **Bottlenecks by perimeter et Blocked on the client** → fusionnés dans « What the open requirements are waiting on » (DEC-117).
- (R) **Casting gaps** — Avant : activités sans manager → Maintenant : systèmes sans personne, dans « By system » (DEC-124).
- (R) **Trajectoire** — Avant : exigences restantes jusqu'à l'échéance → Maintenant : % alloué et % répondu, projection au rythme de la semaine.
- (R) **Mesure de l'IA** — Avant : « AI reliability — correction rate by field » côté stakeholders → Maintenant : hors du tableau de bord ; reste dans Configuration › AI feedback (DEC-117, PLAT-008 « Corrections IA »).

### Retiré / abandonné
- (X) **Vue stakeholders et santé comparable entre tenders** (ancienne §2.1) — aucun indicateur composite sans définition métier (PLATFORM).
- (X) **Mesures de l'IA** (qualité de dérivation, taux de correction) dans le dashboard (DEC-117).
- (X) **Classements nominatifs** — « late by contributor » (16 sept.), puis personnes les plus actives et réponses par personne (DEC-117, 6 oct.) : tous retirés par DEC-118 le 7 oct.
- (X) **« Internal vs declared to the client »** (bloc du 16 sept.) — la conformité externe est dérivée (DEC-106).
- (X) **Risques ouverts, risques par poids, matrice poids × stratégie** — prévus par SPEC-risks §9, abandonnés par DEC-113 (un risque n'a ni poids ni statut) : ne pas les construire d'après le texte de la spec.

### Toujours ouvert
- **Formules PLAT-008 « à compléter »** — dénominateurs, revue effective, corrections répétées ; trajectoire et activité de la semaine exigent des snapshots ou un historique exploitable.
- **Seuil de retard** — PLAT-008 fixe 5 jours ; le réglage « Overdue threshold » de Configuration n'est relié à rien.
- **« Sous-système » a deux sens** — DEC-118 appelle sous-systèmes les périmètres staffés du casting (OBS · team), alors que TENDER-PROFILES, DEC-046 et DEC-058 appellent sous-systèmes les 16 codes vers lesquels un Turnkey répartit — codes que l'écran affiche comme « systems » (déduit, non arbitré).
- **File « On the client » face à DEC-092 / DEC-125** — une exigence qui a une question au client est rangée « sur le client » avant « sur un contributeur », alors que la question ne bloque rien et que Compliance met désormais en avant ce que doit le contributeur (déduit ; la règle PLAT-008 date de DEC-117).

### Synthèse
- Trois onglets métier (Project, Allocation, Compliance), une phrase puis un chiffre par bloc, chaque ligne ouvre l'écran concerné.
- Unité = système ou sous-système, jamais la personne (DEC-118) : règle de conformité sociale, pas un choix d'affichage.
- L'IA ne se mesure plus dans le dashboard (Configuration › AI feedback seulement).
- Conformité : progression vers le client, stratégies d'écart et risques (SPEC-risks §9 sans poids).
- Plusieurs mesures exigent un historique que rien ne stocke encore (trajectoire, semaine).

## Configuration (paramètres du tender)
Où lire aujourd'hui : `docs/current/JOURNEYS.md` (JRN-007), `docs/current/ALLOCATION.md` (ALLOC-015, ALLOC-021, ALLOC-023, ALLOC-T16/T17), `docs/current/CAPTURE.md` (CAPT-T01 à T04), `docs/current/LIFECYCLE.md` (LANG-001), `docs/specs/SPEC-external-partners.md` §2, `docs/specs/SPEC-risks.md` §2.1, DEC-035, DEC-049, DEC-050, DEC-082, DEC-084, DEC-093, DEC-095, DEC-110, DEC-111, DEC-116, DEC-117 — au 8 sept. : `docs/specs/SPEC-configuration.md`

### Nouveau
- (R) **Section « Allocation model » (ALLOC-015 ; DEC-049, DEC-050)** — système et produit en lecture seule (figés à la création) ; modèle appliqué modifiable (SIG : Urban, Mainline Wayside, Mainline Onboard ; Turnkey : modèles par système fixés par la combinaison) ; « re-run everything » qui re-dérive toutes les exigences et détruit tout, réponses comprises, après une annonce chiffrée (exigences touchées, réponses et verdicts perdus — ALLOC-T16/T17). Distincte de la relance unitaire, jamais proposée en repli de celle-ci. Démo : affichage seulement, bouton désactivé.
- (R) **Partenaires externes dans la liste OBS Turnkey (DEC-082, ALLOC-021)** — Turnkey seulement : le PM ajoute une entreprise partenaire (son nom) ; couleur propre, jamais dans le jeu d'étiquettes du modèle, pas de passe 2, verdict saisi par le PM au niveau système (CONF-026) ; retrait seulement si aucune exigence ne lui est attribuée, sinon refus avec le nombre (DEC-093, ALLOC-023). Effet immédiat.
- (R) **Section « Compliance » : stratégies d'écart (SPEC-risks §2.1 ; DEC-110, DEC-111 ; CONF-029)** — par tender : nom + résultat externe (Compliant / Not compliant / Pending) ; liste vide à la création ; une stratégie utilisée se renomme mais ne se supprime pas ; changer le résultat d'une stratégie utilisée recalcule les exigences concernées après une confirmation qui dit combien changent, les corrections du PM étant conservées (DEC-106). Effet immédiat.
- (R) **Réglages avancés de capture (CAPTURE.md)** — Conversion range (toutes les pages / pages spécifiques, avec un champ pour dire lesquelles ; hors plage = aucune exigence, pas un filtre d'affichage), Default table conversion format (Image / Dataframe), Sentences in paragraphs (As source file / Split), Format of equations (images / formules) ; en tête de la section renommée « Capture & segmentation », juste avant la granularité des tableaux qui dépend du format. Démo seulement (CAPT-T04).
- (R) **Lecture seule par décision** — ligne produit (DEC-095) et produit (DEC-049), affichés « Not editable, by decision — not a missing control » ; langue de travail = anglais, non modifiable (LANG-001, DEC-019).

### Modifié
- (R) **Sections** — Avant (9) : General, Team & experts, Workflow & milestones, Appearance, AI & segmentation, AI feedback, Q&A & submission, Versions, Language → Maintenant (11) : General, Team & contributors, Reminders, Allocation model, Compliance, Appearance, Capture & segmentation, AI feedback, Q&A & submission, Versions, Language.
- (R) **General** — ligne produit : liste modifiable → valeur en lecture seule (DEC-095) ; « Source document » (fichier actif) → « Documents : gérés dans Documents & versions » (versions par document, DEC-069) ; l'échéance ne pilote plus que le compte à rebours.
- (R) **Workflow & milestones → Reminders** — ne restent que le seuil de retard et la cadence maximale de relance.
- (R) **Q&A & submission** — ne reste que le canal vers l'émetteur ; les questions sortent par export, l'outil n'envoie rien (QA-003, DEC-116).
- (R) **Language** — « Default translation target » (FR / DE / ES) → « Working language : English », non modifiable (LANG-001).
- (R) **AI feedback** — devient le seul lieu de mesure des corrections de l'IA (DEC-117).
- (R) **Ce qui agit vraiment** — Avant : thème et vue restreinte → Maintenant : thème, vue restreinte, partenaires, stratégies d'écart (tous immédiats ; pas de vraie sauvegarde).

### Retiré / abandonné
- (X) **Review milestone gate / « Enforce full validation before export » / « Allocation completeness gate »** — Finalize ne verrouille rien puis disparaît (DEC-035, DEC-084).
- (X) **Outdated-response re-flag (« substantive changes only »)** — contraire à DEC-026 (toute modification de texte ou de traduction repasse en revue) ; plus de statut « outdated » (DEC-078).
- (X) **AI duplicate detection et Internal review before sending** — DEC-116.
- (X) **Notification des contributeurs au changement de version** — retirée (14e3059), rien ne la réalise ; les notifications relèvent de PLAT-005.
- (X) **Default translation target** — LANG-001.
- (X) **Critère d'affectation « Discipline »** — retiré (14e3059) ; restent PBS / ABS / OBS.

### Toujours ouvert
- **Persistance et réglages réellement appliqués** — JRN-007 : distinguer ce qui est appliqué de ce qui est représenté ; « Save configuration » ne définit pas la cible (OPEN-05, OPEN-12).
- **Mode d'assistance IA** — DEC-095 veut qu'il soit affiché en lecture seule dans les paramètres ; il n'y figure pas.
- **Capture** — liste probablement incomplète ; réglages modifiables après capture ? ; granularité désactivée quand le format est « Image » ? (CAPTURE.md).
- **Modèle d'un Turnkey** — dépend de la matrice des combinaisons (DEC-048).
- **Vue restreinte (Redacted / Hidden)** — toujours présente et agissante, alors qu'ACC-007 (DEC-012) donne à un contributeur la lecture de tout le projet ; ACCESS note l'écart (« restreint certaines lectures ») et dit que la cible DEC prime (déduit : réglage appelé à disparaître, aucune DEC ne le dit explicitement).
- **Réglages restants sans câblage** — seuil de retard, cadence, critères d'affectation, rendu PDF / HTML, seuil d'incertitude de segmentation, re-segmentation, protection des corrections manuelles, canal Q&A, numérotation des versions, addendum : intention réelle, comportement cible non spécifié.

### Synthèse
- Onze sections ; deux nouvelles qui agissent vraiment : partenaires Turnkey (Allocation model) et stratégies d'écart (Compliance).
- Relance globale au changement de modèle : destructive par nature, annoncée en chiffres avant confirmation (ALLOC-015).
- Ligne produit, produit et langue de travail en lecture seule par décision ; le mode IA devrait l'être aussi (DEC-095).
- Réglages de capture ajoutés (affichage), réglages sans réalité retirés (re-flag, doublons, revue interne, notification, cible de traduction, Discipline).

## Team casting (équipes et droits de casting)
Où lire aujourd'hui : `docs/current/ACCESS.md` (ACC-001 à ACC-014, matrice métier, ACC-T01 à T10), `docs/current/JOURNEYS.md` (JRN-004), `docs/current/TENDER-PROFILES.md` (ligne « Casting » de la matrice), DEC-003, DEC-012, DEC-030, DEC-032, DEC-033, DEC-036, DEC-045, DEC-087, DEC-102, DEC-124 — au 8 sept. : `docs/specs/SPEC-team-management.md`, `docs/tickets/TICKET-casting-screen-redesign.md`

### Nouveau
- (R) **Systèmes = les 16 codes de la capture (DEC-032)** — Casting, Allocation, Compliance et Q&A partagent la même liste ; libellé = code tant que la légende n'est pas fournie. « + Add system » n'ajoute qu'un code de cette liste, jamais un système saisi ; impossible sur un tender SIG, émis sur un seul système (DEC-046, TYPE-T08).
- (R) **Périmètres = la liste OBS · team partagée (DEC-036)** — même liste pour tous les systèmes, choix fermé ; « pas de périmètre — staffé directement » reste un choix ordinaire. Le périmètre sert à affecter automatiquement depuis l'OBS et ne limite pas les droits (DEC-033).
- (R) **Manager de système facultatif (DEC-124, ACC-008, DEC-003)** — un système peut n'avoir que des contributeurs ; le PM y staffe directement ; un système n'est « non staffé » que s'il n'a personne.
- (R) **Une personne = un seul système (DEC-102, DEC-124, ACC-014)** — sur un ou plusieurs périmètres de ce système ; la recherche montre la personne déjà membre d'un autre système, avec ce système, et l'ajout est refusé avec la raison.
- (R) **Droits (DEC-003, DEC-012, ACC-007 à ACC-010)** — PM : casting de tout le projet ; contributeurs : rattachements de leur propre système, sans permission manager distincte (ACC-T06) ; pas de hiérarchie entre contributeurs d'un système ; lecture de tout le projet, modification de son seul système.
- (R) **Variantes de tender (DEC-005, TENDER-PROFILES)** — SIG autonome : PM + contributeurs SIG, un seul système, périmètres de DEC-036 ; SIG au sein d'un Turnkey : gestion de ses propres rattachements, pas du casting global.

### Modifié
- (R) **Hiérarchie** — Avant : Activity → Perimeter (optionnel) → Expert → Maintenant : Système → Périmètre (optionnel) → Personne (DEC-033, DEC-045).
- (R) **Système sans manager** — Avant : bloqué pour tous, y compris le PM (« garde d'intégrité ») → Maintenant : ordinaire, le PM le staffe (DEC-124).
- (R) **Couverture** — Avant : par activité ; complète si chaque périmètre propre est staffé, ou si l'activité est staffée directement → Maintenant : un système est un trou seulement s'il n'a personne (DEC-124) ; la carte du dashboard compte les systèmes ayant au moins une personne.
- (R) **Rôles** — « activity managers » → « system managers » ; « activity manager » est réservé à qui gère le casting d'un système (DEC-030).
- (R) **Retrait d'une personne qui a du travail** — inchangé (réaffectation d'abord) ; s'applique à la personne de chaque OBS, responsable de sa conformité (ACC-006, DEC-087).
- (R) **Points ouverts de l'ancien ticket** — droits propres au niveau activité : tranché, le périmètre ne limite pas les droits et le contributeur agit sur tout son système (DEC-033, DEC-002, DEC-012) ; liste de périmètres centrale ou par tender : liste partagée OBS · team (DEC-036).

### Retiré / abandonné
- (X) **Création libre de périmètre au clavier** — DEC-036.
- (X) **Listes inventées** (7 activités « Signalling & Urban, Mainline, Infrastructure… » et périmètres propres à chaque activité) — DEC-032, DEC-036.
- (X) **« No manager cast » comme état bloquant** — DEC-124.

### Toujours ouvert
- **Contributeur qui gère son système** — la maquette ne simule que PM et managers ; ACCESS : « Casting conserve managerId » (écart à DEC-003 / ACC-T06).
- **Légende des 16 codes** (DEC-032) ; **rapport RSC / RST** et **RST porteur d'un modèle** (hypothèse, DEC-059).
- **Périmètre = OBS · team (DEC-036) face à l'OBS-poste du modèle Mainline (DEC-062)** — sur RFP-2026-114 (Mainline Wayside) le casting garde des périmètres-équipes (déduit, non tranché).
- **« Ce que le document implique d'abord »** (ticket) — non construit.
- **Échelle et persistance** — 150 à 200 personnes décrites comme besoin, non mesurées (JRN-004) ; annuaire SSO et droits côté serveur (PLAT-001, PLAT-002).
- **« Sous-système »** — double sens (voir Statistiques).

### Synthèse
- Liste de systèmes fermée = 16 codes de la capture ; périmètres = liste OBS · team partagée, fermée.
- Manager de système facultatif : le PM staffe tout ; un système n'est non staffé que s'il n'a personne.
- Une personne appartient à un seul système, refus explicite sinon.
- Cible de droits : tout contributeur gère les rattachements de son système (DEC-003) — pas encore représenté.
