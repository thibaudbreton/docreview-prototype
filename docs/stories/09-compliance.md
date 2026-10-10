<!-- Généré depuis le backlog du 10 octobre 2026 ; voir README.md pour les conventions. -->
# Compliance (US-CMP)
Compliance est l'étape où chaque contributeur rend le verdict technique de son système, exigence par exigence, et où le chef de projet suit la consolidation jusqu'à l'export (parcours JRN-003, écran `compliance.html`). Quelques termes, une ligne chacun :
- **affectation** : une organisation (OBS) d'un système à qui l'exigence est allouée, avec la personne qui en répond et que l'on relance (DEC-087) ; c'est l'unité de travail de Compliance.
- **verdict** : Compliant ou Not compliant, rien d'autre ; « R&D needed » n'est qu'une mention dans le commentaire d'un Compliant (DEC-031).
- **consolidation** : le verdict de l'exigence calculé depuis ses affectations ; le plus restrictif gagne, l'exigence reste en attente (pending) tant qu'une réponse manque.
- **conformité externe** : ce que le client reçoit, dérivée de la stratégie d'écart choisie sur un Not compliant (voir US-RSK).
Turnkey consolide organisations → système → exigence ; un tender SIG ou Mainline (un seul système) consolide organisations → exigence, sans axe système ; RSC suit les règles communes, ses particularités restent ouvertes (OPEN-15). Tout ce périmètre vient après le premier pilote (DEC-022 ; la borne reste à confirmer, docs/gap).

### US-CMP-01 — Créer les affectations quand l'allocation est validée
**Carte :** En tant que contributeur, je veux trouver dans Compliance une affectation pour chaque organisation de mon système dès que l'allocation est validée, afin de savoir sur quoi je dois répondre et qui en répond.
**Conversation :** Une affectation naît de l'allocation : une par organisation (entrée OBS), portée par la personne affectée à cette organisation ; il n'y a pas de responsable global de l'exigence (DEC-087). Sur Turnkey, chaque système est validé à part, par son contributeur ou le chef de projet (DEC-104), et ses organisations partent à ce moment ; sur SIG et Mainline, c'est la validation de l'exigence (DEC-099). Un partenaire externe (Turnkey) donne une affectation au niveau du système, sans organisation ni personne (voir [US-RSK-13](10-risques.md#us-rsk-13--saisir-le-verdict-dun-partenaire-et-documenter-son-écart)). Compliance lit l'allocation en vigueur, jamais une copie ; la validation et le choix des personnes sont décrits dans US-ALM.
**Maquette :** Compliance — `compliance.html` (route `#compliance`), Requirement Table (Review Grid), colonne « Assigned to » ; validation dans Allocation — `revue-documentaire.html` (route `#review`).
**Règles :** DEC-087, DEC-060, DEC-055, DEC-037, DEC-084, DEC-099, DEC-104, DEC-025, DEC-076, ALLOC-008, ALLOC-010, ALLOC-011, CONF-010, CONF-T10  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Valider l'allocation d'un système (Turnkey) ou d'une exigence (SIG, Mainline) fait de chaque organisation concernée une affectation « Awaiting answer », une ligne par organisation, portant la personne de cette organisation.
2. Avant cette validation, l'affectation existe à l'état « Proposed » : elle est visible de tous, mais rien n'est encore dû par personne.
3. Une organisation sans personne (validation permise, DEC-025) donne une affectation « — unassigned — » : tout contributeur du système peut y répondre, mais personne ne peut être relancé.
4. Une exigence n'a aucune conformité acquise tant que les réponses de toutes ses affectations ne sont pas données, y compris quand une affectation n'a pas de personne.
5. Changer la personne d'une organisation dans Allocation change la personne de l'affectation ; retirer une organisation retire son affectation (Allocation demande confirmation si elle a déjà une réponse).
6. La table, le panneau, la vue Document et l'export lisent les mêmes affectations, enregistrées côté serveur et retrouvées après reconnexion.
Écart maquette : la maquette porte une affectation par système (les organisations ne sont qu'affichées) et ses affectations sont des données de démonstration : valider dans Allocation ne crée ni ne modifie rien dans Compliance.
Point ouvert : un contributeur peut-il déjà répondre à une affectation « Proposed » ? La maquette le permet, aucune règle ne le dit (docs/gap SPECS, « Statuts d'une affectation », Toujours ouvert).

### US-CMP-02 — Suivre l'avancement d'une affectation par son statut
**Carte :** En tant que chef de projet, je veux lire où en est chaque affectation, séparément de son verdict, afin de savoir ce qui reste à faire sans confondre avancement et conformité.
**Conversation :** L'avancement et le verdict sont deux axes distincts (CONF-001) : le statut dit où en est le travail, le verdict ce qui a été jugé. Il y a cinq statuts : « Proposed », « Awaiting answer », « Awaiting Q&A » (une question au client est en cours : simple information, elle ne bloque rien, DEC-092), « Reassignment needed » et « Answered ». Les statuts « overdue » et « outdated version » n'existent plus (DEC-078) : l'âge reste une donnée. Le détail de chaque transition est dans la story de l'action qui la déclenche.
**Maquette :** Compliance — `compliance.html` (route `#compliance`), Progress Status Chip, colonne « Status ».
**Règles :** CONF-001, DEC-078, DEC-092, DEC-063, DEC-122  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Une affectation porte toujours un seul des cinq statuts ; aucun autre (ni « overdue », ni « outdated version ») n'apparaît en pastille, filtre, tri ou fil d'activité.
2. Transitions : validation de l'allocation → « Awaiting answer » ; verdict confirmé → « Answered » ; question au client posée sur une affectation « Awaiting answer » → « Awaiting Q&A » ; renvoi → « Reassignment needed » ; réaffectation ou réouverture par une nouvelle version → « Awaiting answer ».
3. « Awaiting Q&A » n'empêche pas de rendre le verdict : le confirmer passe l'affectation à « Answered ».
4. La pastille de statut n'affiche jamais un verdict, et la colonne Compliance n'affiche jamais un statut.
5. Aucun statut ne s'affiche en vert ni en rouge : ces deux couleurs sont réservées au verdict.
6. Chaque changement de statut s'inscrit au journal de l'exigence avec son auteur, sa date et l'avant → après (journal : voir US-X).
Point ouvert : le statut « Assigned » existe dans le vocabulaire mais aucun flux ne le produit ; le garder ou le retirer n'est pas décidé (docs/gap SPECS, « Statuts d'une affectation », Toujours ouvert).

### US-CMP-03 — Lire les colonnes de la table Compliance
**Carte :** En tant que chef de projet, je veux voir pour chaque exigence l'avancement, le verdict, son commentaire et ce que le client recevra, afin de piloter la conformité sans ouvrir chaque exigence.
**Conversation :** La table se lit de gauche à droite comme le raisonnement : avancement, verdict interne et son commentaire, puis, après un Not compliant, la stratégie d'écart et le risque, puis la conformité externe qui en découle (US-RSK). Les mécaniques communes (tri, filtres, colonnes masquables, redimensionnables, personnalisées) sont celles de US-TAB. Sur un tender SIG ou Mainline, l'axe système est absent, pas seulement masqué (TYPE-T08).
**Maquette :** Compliance — `compliance.html` (route `#compliance`), Requirement Table (Review Grid), Verdict Pill, Risk Chip, Column Visibility Menu.
**Règles :** CONF-001, CONF-009, CONF-025, DEC-031, DEC-063, DEC-078, DEC-082, DEC-087, TYPE-T08  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Les colonnes sont, dans l'ordre : « ID », « Requirement », « System », « Assigned to », « Status », « Compliance », « Compliance comment », « Gap strategy », « Risk », « External compliance », « Last follow-up », « Age », puis les colonnes personnalisées ; « System » et « Age » sont masquées par défaut et s'affichent depuis « View ».
2. Sur un tender SIG ou Mainline, la colonne « System » n'existe pas : ni dans la table, ni dans « View », ni dans les filtres.
3. « Compliance » montre « ✓ Compliant » en vert ou « ✕ Not compliant » en rouge une fois le verdict donné, « — » avant ; seules « Compliance » et « External compliance » utilisent le vert et le rouge.
4. « Compliance comment » affiche le commentaire du verdict (et, sur Turnkey, sa catégorie et son topic) sans ouvrir le panneau.
5. « Assigned to » montre une seule personne par affectation, « Multiple (N) » sur une ligne d'exigence qui a plusieurs affectations, « — unassigned — » sans personne, « PM · for partner » sur un partenaire.
6. « Last follow-up » donne la date de la dernière relance ; « Age » le nombre de jours depuis l'envoi de l'affectation, remis à zéro par une réaffectation ou une réouverture ; aucun âge ne déclenche de statut.

### US-CMP-04 — Déplier une exigence en systèmes et en organisations
**Carte :** En tant que chef de projet, je veux déplier une exigence pour voir chacune de ses affectations, afin de savoir quel système ou quelle organisation retient la consolidation.
**Conversation :** La ligne d'exigence est la synthèse, les lignes dessous sont le détail. Sur Turnkey : exigence → une ligne par système → une ligne par organisation quand un système en a plusieurs. Sur SIG et Mainline il n'y a qu'un système : l'exigence se déplie directement en organisations. La flèche est au même endroit que dans Allocation, dans la cellule du texte (DEC-081).
**Maquette :** Compliance — `compliance.html` (route `#compliance`), Requirement Row (Review Table Row), Branch / Allocated-Activity Sub-row, Disclosure / Expand Chevron.
**Règles :** DEC-037, DEC-055, DEC-060, DEC-081, DEC-087, CONF-004, CONF-025, TYPE-T08  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Une exigence à plusieurs affectations porte une flèche dans sa cellule « Requirement » ; les sous-lignes sont repliées par défaut, la flèche les déplie et les replie.
2. Sur Turnkey, le premier niveau donne une ligne par système ; sous un système à plusieurs organisations, une ligne par organisation.
3. Sur SIG et Mainline, l'exigence se déplie directement en une ligne par organisation, sans niveau système.
4. Chaque sous-ligne a sa propre personne, son statut et son verdict ; la ligne d'exigence montre le statut de l'affectation la plus due ([US-CMP-21](#us-cmp-21--mettre-en-avant-ce-qui-est-dû)), suivi de « · N assignments » quand plusieurs restent ouvertes, et le verdict consolidé ou « — ».
5. Cliquer une sous-ligne ouvre cette affectation dans le panneau de détail.
Écart maquette : la maquette n'affiche les organisations qu'en lecture, avec des valeurs écrites à la main ; le verdict s'y saisit au niveau du système et n'est jamais calculé depuis les organisations.

### US-CMP-05 — Lire la table dans l'ordre du document
**Carte :** En tant que contributeur, je veux parcourir les exigences dans l'ordre du document, avec ses titres, afin de répondre en suivant le texte du client.
**Conversation :** Compliance est allégé et structuré comme le document (DEC-078) : ordre du document par défaut, titres de document et de section en lignes. Trier par un en-tête met la table à plat ; « ↺ Document order » y revient (mécanique commune aux deux tables : [US-TAB-01](06-tables.md#us-tab-01--lire-la-table-dans-lordre-du-document), [US-TAB-05](06-tables.md#us-tab-05--trier-par-un-en-tête-de-colonne) ; « Wrap text » : [US-TAB-10](06-tables.md#us-tab-10--afficher-le-texte-complet-des-exigences)). L'ordre « action needed first », la liste « Sort: … », le bouton « Needs my action » et la bascule « By section / By contributor » ont disparu (DEC-081, DEC-083).
**Maquette :** Compliance — `compliance.html` (route `#compliance`), Requirement Table (Review Grid), Grid Section / Group Header, Left Navigator Panel.
**Règles :** DEC-078, DEC-081, DEC-083, CONF-022, CONF-025, CONF-027  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Sans tri actif, la table suit l'ordre du document et intercale une ligne par titre de document et par titre de section ; ces lignes n'ont ni statut ni case de sélection.
2. Un tri par en-tête met la table à plat, sans lignes de titre, et fait apparaître « ↺ Document order », qui rétablit l'ordre du document.
3. Le navigateur de gauche suit le même découpage (documents, sections, exigences) avec la couleur du verdict consolidé ; cliquer une exigence l'ouvre. Il n'a pas de mode « par contributeur ».
4. L'écran n'a ni liste « Sort: … », ni bouton « Needs my action », ni indicateur « overdue » ou « outdated version ».

### US-CMP-06 — Lire la conformité sur le document
**Carte :** En tant que chef de projet, je veux voir les verdicts posés sur le texte du document source, afin de lire la réponse du tender comme le client lira son document.
**Conversation :** La vue Document de Compliance montre chaque document source comme une feuille, avec le verdict consolidé de chaque exigence, en lecture seule. Elle remplace l'ancien onglet Document du panneau (DEC-078) ; on y arrive par la bascule « Table / Document » ou par « View in the document » depuis le panneau de décision ([US-CMP-10](#us-cmp-10--lire-lexigence-en-entier-dans-le-panneau-de-décision)). Elle montre tout le tender à tout lecteur (DEC-012).
**Maquette :** Compliance — `compliance.html` (route `#compliance`), Document Reading View, Document Block, Left Navigator Panel.
**Règles :** DEC-012, DEC-031, DEC-078, DEC-080  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. « Document » affiche une feuille par document source, sous son nom, sous-titrée « Compliance synthesis — consolidated verdicts over the source text · read-only ».
2. Une légende donne trois états, « Compliant », « Not compliant », « Pending » ; un bloc Not compliant est rouge, un Compliant vert, un bloc en attente neutre.
3. Chaque bloc montre l'ID de l'exigence et son verdict consolidé, ou, tant qu'elle est en attente, le statut de l'affectation la plus due.
4. Cliquer un bloc sélectionne l'exigence et ouvre son panneau ; rien ne se modifie depuis cette vue.
5. « View in the document » (ou le lien « § ») bascule sur cette vue à l'exigence en cours, mise en évidence, sans fermer le panneau de décision.

### US-CMP-07 — Suivre l'avancement de la consolidation
**Carte :** En tant que chef de projet, je veux voir combien d'exigences sont consolidées et combien d'affectations sont à chaque statut, afin de savoir d'un coup d'œil où en est la réponse au client.
**Conversation :** La barre d'état ouvre l'écran : titre, anneau « N/M consolidated » (en exigences), total des affectations, puis une pastille par statut qui filtre la table. Quand tout est consolidé, un bandeau propose l'export ; rien n'est verrouillé pour autant (CONF-013). Les comptes portent sur tout le tender pour tous (DEC-012) ; le contributeur a en plus les pastilles « set aside » ([US-CMP-14](#us-cmp-14--mettre-une-affectation-de-côté)) et « my system » ([US-CMP-08](#us-cmp-08--consulter-tout-le-tender-et-nagir-que-sur-son-système)).
**Maquette :** Compliance — `compliance.html` (route `#compliance`), Triage Bar, Filter Pill, Export Readiness Summary.
**Règles :** DEC-081, DEC-012, DEC-014, CONF-013, CONF-025, PLAT-002  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. La barre affiche « Compliance », un anneau avec « N/M consolidated » (exigences consolidées sur le total ; l'infobulle donne le pourcentage et les affectations répondues sur le total) et « N assignments ».
2. Les pastilles « answered », « awaiting answer », « awaiting Q&A » et « reassignment needed » comptent les affectations de chaque statut ; cliquer une pastille filtre la table sur ce statut, « ✕ Clear filter » retire le filtre.
3. Sous un filtre, la table annonce « N of M requirements · K assignments shown » ; sans filtre, cette ligne n'apparaît pas.
4. Quand toutes les exigences sont consolidées, un bandeau dit « Compliance matrix complete » et propose « Go to export → », qui ouvre l'export ([US-CMP-28](#us-cmp-28--exporter-le-registre-de-conformité-avec-options)) ; il disparaît dès qu'une exigence n'est plus consolidée.
5. Les comptes sont calculés côté serveur et sont les mêmes pour un chef de projet et pour un contributeur.

### US-CMP-08 — Consulter tout le tender et n'agir que sur son système
**Carte :** En tant que contributeur, je veux lire toutes les affectations du tender mais n'agir que sur celles de mon système, afin de m'appuyer sur le travail des autres sans risquer de le modifier.
**Conversation :** Un contributeur appartient à un seul système (DEC-102) et agit sur toutes ses affectations, y compris celles affectées à un collègue (DEC-002, CONF-010) ; il lit le reste du tender en lecture seule (DEC-012, DEC-100). « Mon système » se lit par l'appartenance, pas par l'affectation. La pastille « my system » resserre la table sur son système sans rien cacher par défaut, et un filtre ne change jamais les droits.
**Maquette :** Compliance — `compliance.html` (route `#compliance`), Triage Bar (pastille « my system »), Detail / Assignment Panel (lecture seule).
**Règles :** DEC-012, DEC-100, DEC-102, DEC-002, CONF-010, CONF-T07, CONF-T14, ACC-007, ACC-013, ACC-014, ACC-T04, ACC-T05, ACC-T09, PLAT-002  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Un contributeur voit toutes les exigences et affectations du tender dans la table, la vue Document, les compteurs et l'export.
2. Sur l'affectation d'un autre système, le panneau est en lecture seule et dit « Read only — <SYS>'s assignment. Only <SYS>'s contributors or the project team change it. » ; aucun verdict, question, renvoi, mise de côté ni relance n'y est proposé.
3. Les touches R, Q et S sur l'affectation d'un autre système sont refusées avec « Read only — <SYS>'s assignment ».
4. Sur une affectation de son système affectée à un collègue, il rend le verdict, pose une question ou la renvoie comme sur la sienne.
5. La pastille « my system », visible du seul contributeur et inactive par défaut, compte les affectations de son système et resserre la table sur elles ; elle se combine avec les pastilles de statut et ne change aucun droit.
6. Le serveur refuse toute modification d'une affectation d'un autre système, y compris par requête directe, et ne donne accès à aucun tender dont le contributeur n'est pas membre.

### US-CMP-09 — Arriver sur sa file et la parcourir
**Carte :** En tant que contributeur, je veux arriver directement sur la première affectation qui attend mon verdict et savoir combien il en reste, afin de juger si j'ai le temps de m'attarder sur un cas difficile.
**Conversation :** La file d'un contributeur, ce sont les affectations de son système qui attendent un verdict ; sans repère de progression, il ne peut pas juger s'il a dix minutes pour un cas (SPEC-compliance-decision-panel §5). Le panneau de décision affiche « N left · this is k of N » et « Next › » ; la touche N mène à la prochaine exigence qui attend le lecteur. Les affectations mises de côté ([US-CMP-14](#us-cmp-14--mettre-une-affectation-de-côté)) sont comptées mais sautées. Pour le chef de projet, N vise ce que lui seul peut faire.
**Maquette :** Compliance — `compliance.html` (route `#compliance`), Decision Panel (progression de la file, « Next › »), Shortcut Help.
**Règles :** DEC-079, DEC-085, DEC-102, DEC-108, CONF-023  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Un contributeur qui ouvre Compliance sans sélection en cours arrive, dans l'ordre de la table, sur la première exigence qui l'attend (une affectation de son système à décider, hors mises de côté, ou un Not compliant de son système à documenter), panneau ouvert ; une sélection déjà ouverte n'est jamais remplacée.
2. La file compte les affectations de son système qui ne sont ni « Answered » ni « Reassignment needed » ; le panneau affiche « N left · this is k of N », plus « · n set aside » s'il y en a, et une barre de progression des affectations répondues de son système.
3. « Next › » ouvre l'affectation suivante de la file dans l'ordre de la table, en sautant les mises de côté ; il n'apparaît pas quand il n'y en a pas d'autre.
4. Pour un contributeur, la touche N va à la prochaine exigence de la vue qui a une affectation de son système à décider (hors mises de côté) ou un Not compliant de son système sans stratégie ou sans risque ; sinon « Nothing left waiting on you in this view ».
5. Pour le chef de projet, N va à la prochaine exigence qui a une affectation renvoyée à réaffecter, ou un verdict ou une documentation d'écart de partenaire à saisir ; sinon « Nothing waiting on you in this view ».

### US-CMP-10 — Lire l'exigence en entier dans le panneau de décision
**Carte :** En tant que contributeur, je veux lire le texte complet de l'exigence, son contexte dans le document et sa version originale, afin de comprendre exactement ce que le client demande avant de juger.
**Conversation :** Le panneau de décision s'ouvre quand un contributeur ouvre une affectation de son système qui attend son verdict ; tout y est subordonné au texte, qui domine (SPEC-compliance-decision-panel §2, §4). Pas de bloc d'allocation ni de ligne « Yours » (DEC-080) : l'ID et la section suffisent pour se situer. L'interrupteur de langue originale n'existe que si le tender n'est pas en anglais ; un tender n'a qu'une langue source (DEC-096).
**Maquette :** Compliance — `compliance.html` (route `#compliance`), Decision Panel (en-tête, texte, « View in the document »), Toggle Switch « Original · … ».
**Règles :** DEC-079, DEC-080, DEC-081, DEC-096, LANG-001, CONF-023, CONF-024, CONF-025  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Sous le titre « Requirement », le texte de l'exigence s'affiche en entier, sans troncature, sur un fond teinté ; il ne se modifie pas depuis ce panneau.
2. Le lien « § <section> » et le bouton « View in the document » basculent sur la vue Document à cette exigence, mise en évidence, sans fermer le panneau.
3. Sur un tender dont la langue source n'est pas l'anglais, l'interrupteur « Original · <langue> » affiche le texte tel qu'écrit dans le tender, signalé « · original, <langue> », en lecture seule ; le désactiver revient à l'anglais. Sur un tender en anglais, l'interrupteur n'existe pas.
4. « ⇤ Widen panel » élargit le panneau pour un texte long, une figure ou une formule ; « ⇥ Narrow panel » le ramène à sa largeur normale.
5. Le panneau ne montre ni bloc d'allocation ni ligne « Yours » : l'ID et la section en tête, puis le texte, puis immédiatement la décision.

### US-CMP-11 — Rendre un verdict : choisir, puis confirmer
**Carte :** En tant que contributeur, je veux choisir Compliant ou Not compliant puis confirmer, afin de donner la vérité technique de mon système sur l'exigence.
**Conversation :** Deux verdicts seulement (DEC-031) ; « R&D needed » s'écrit dans le commentaire d'un Compliant. On choisit d'abord, puis seuls les champs de ce choix s'affichent, avec un seul bouton de confirmation : Compliant demande donc deux gestes (DEC-080, qui corrige la spec du panneau). Une phrase rappelle que le contributeur donne la vérité technique et que la stratégie choisie sur un Not compliant décide de ce que le client reçoit (DEC-106) ; le Not compliant s'enregistre même si sa stratégie ou son risque manque (DEC-108). Stratégie et risque : [US-RSK-04](10-risques.md#us-rsk-04--choisir-une-stratégie-décart-après-un-not-compliant) à -07 ; Category + Topic sur Turnkey : [US-CMP-12](#us-cmp-12--qualifier-un-not-compliant-par-category-et-topic-sur-un-tender-turnkey).
**Maquette :** Compliance — `compliance.html` (route `#compliance`), Decision Panel (« Your verdict »), Verdict Pill, Toast.
**Règles :** DEC-031, DEC-080, DEC-081, DEC-002, DEC-087, DEC-085, DEC-106, DEC-108, CONF-008, CONF-010, CONF-023, CONF-024, DOM-008, PLAT-003  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Sous « Your verdict », la phrase « Give the technical truth. On a Not compliant, the gap strategy you pick decides what the client is told, and the risk you link keeps it on record. » précède deux choix : « ✓ Compliant » (vert) et « ✕ Not compliant » (rouge).
2. Après un choix, le panneau affiche « Verdict: » avec la pastille et « Change », seulement les champs de ce choix, et un seul bouton « Confirm — Compliant » ou « Confirm — Not compliant » ; « Change » revient aux deux choix.
3. Sur Compliant, le commentaire est facultatif (« Comment — optional. Say so here if R&D work is needed. ») ; aucun écran ne propose de troisième verdict.
4. Confirmer passe l'affectation à « Answered » avec le verdict, le commentaire, la date et l'auteur ; la consolidation se recalcule ([US-CMP-20](#us-cmp-20--consolider-les-verdicts-dune-exigence)) et le verdict s'inscrit au journal de l'exigence.
5. Un message confirme « <ID> · <SYS> — Compliant » (ou « Not compliant ») ; « Undo » ou ⌘/Ctrl + Z rend l'état d'avant, brouillon compris (mécanique de l'annulation : US-TAB).
6. Tout contributeur du système de l'affectation peut confirmer, même si elle est affectée à un collègue ; le serveur refuse le verdict de toute autre personne que ces contributeurs et le chef de projet ([US-CMP-25](#us-cmp-25--saisir-ou-modifier-une-réponse-en-tant-que-chef-de-projet)).

### US-CMP-12 — Qualifier un Not compliant par Category et Topic sur un tender Turnkey
**Carte :** En tant que contributeur d'un tender Turnkey, je veux classer chaque Not compliant par une catégorie et un sujet, afin que le refus soit documenté de façon homogène.
**Conversation :** Category + Topic ne valent que sur Turnkey (DEC-107) ; ailleurs, ce sont la stratégie d'écart et le risque qui qualifient le Not compliant. Le métier n'a pas fourni la liste des catégories : elle reste un placeholder explicite à l'écran, jamais des valeurs plausibles (DEC-038). La friction est voulue : c'est là qu'un refus se documente.
**Maquette :** Compliance — `compliance.html` (route `#compliance`), Decision Panel (champs « Category » et « Topic »), Select Dropdown, Text Input.
**Règles :** DEC-107, DEC-038, DEC-031, CONF-008, CONF-023, OPEN-04  ·  **Périmètre :** Après pilote  ·  **Variantes :** Turnkey
**Critères d'acceptation :**
1. Sur un tender Turnkey, choisir « ✕ Not compliant » affiche « Category » (liste) et « Topic » (texte, requis) avant le commentaire.
2. La liste porte la mention « Placeholder list — the real categories aren't defined yet. » tant que les vraies valeurs ne sont pas fournies.
3. Confirmer sans Topic est refusé avec « Name the topic — a Not compliant verdict gets documented », et le curseur va au champ « Topic ».
4. La catégorie et le topic sont enregistrés avec la réponse et visibles dans la colonne « Compliance comment » et dans le panneau.
5. Sur un tender SIG, Mainline ou RSC, ni « Category » ni « Topic » n'apparaissent ; un Compliant ne les demande jamais.
Point ouvert : la liste réelle des catégories de non-conformité est à fournir par le métier avant la mise en production de Compliance (OPEN-04, DEC-038).

### US-CMP-13 — Retrouver son brouillon de verdict
**Carte :** En tant que contributeur, je veux que mon verdict en cours s'enregistre tout seul, afin de reprendre un cas difficile plus tard, sur un autre poste, sans rien perdre.
**Conversation :** Un verdict difficile peut s'étaler sur deux sessions ; sans brouillon, on pousse à conclure trop tôt (SPEC-compliance-decision-panel §6). Le brouillon (choix, commentaire, catégorie, topic) est enregistré côté serveur, privé à son auteur, et n'est jamais un statut partagé (DEC-090).
**Maquette :** Compliance — `compliance.html` (route `#compliance`), Decision Panel (« Drafts save themselves » / « Draft saved · HH:MM »), Requirement Row (marque ✎).
**Règles :** DEC-079, DEC-090, CONF-023, PLAT-001  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Le choix, le commentaire, la catégorie et le topic s'enregistrent à chaque saisie, sans bouton ; le panneau dit « Drafts save themselves », puis « Draft saved · HH:MM ».
2. Quitter le panneau ou l'écran puis revenir sur l'affectation rend le brouillon tel quel, y compris depuis un autre poste ou une autre session.
3. Le brouillon n'est visible que de son auteur : ni un collègue du système ni le chef de projet ne le voient, et il n'entre dans aucun compteur ni export.
4. La cellule ID de la ligne porte une marque « ✎ », pour son seul auteur, tant qu'un brouillon existe.
5. Confirmer le verdict supprime le brouillon ; annuler la confirmation le rétablit.
Écart maquette : le brouillon ne vit que dans la session de l'application (perdu au rechargement), pas sur le serveur.

### US-CMP-14 — Mettre une affectation de côté
**Carte :** En tant que contributeur, je veux marquer une affectation « à reprendre plus tard », afin de traiter d'abord le reste de ma file sans perdre ce cas de vue.
**Conversation :** « Set aside » est un marqueur personnel, pas un statut partagé (DEC-079, DEC-090) : seul son auteur le voit. Il est retrouvable par une pastille-filtre et visible sur la ligne (DEC-081, la décision la plus récente ; DEC-079 disait « ni filtre ni vue »). C'est, avec « Ask the client », une sortie pour ne pas trancher un cas difficile à la va-vite.
**Maquette :** Compliance — `compliance.html` (route `#compliance`), Decision Panel (« Set aside »), Triage Bar (pastille « set aside »), Requirement Row (cellule ID teintée).
**Règles :** DEC-079, DEC-081, DEC-085, DEC-090, CONF-023, CONF-025  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Le bouton « Set aside », au-dessus de l'ID, ou la touche S posent ou retirent le marqueur sur une affectation à décider ; un message dit « <ID> set aside — only you see this marker » ou « <ID> back in your queue », et le geste s'annule.
2. Une affectation mise de côté a sa cellule ID teintée, avec ⚑, pour son seul auteur ; personne d'autre, chef de projet compris, ne voit le marqueur.
3. La pastille « set aside », visible du seul contributeur, compte ses affectations mises de côté et filtre la table sur elles.
4. La file les compte (« · n set aside ») ; « Next › » et la touche N les sautent.
5. Rendre le verdict retire le marqueur ; le marqueur n'entre dans aucun autre compteur ni dans aucun export.
6. Le marqueur est enregistré côté serveur et retrouvé d'un poste et d'une session à l'autre.
Écart maquette : le marqueur ne vit que dans la session de l'application, pas sur le serveur.

### US-CMP-15 — Consulter les questions et les exigences similaires
**Carte :** En tant que contributeur, je veux voir sans quitter le panneau les questions déjà posées sur l'exigence et les exigences proches du tender, afin de ne pas re-décider ce qui a déjà été tranché.
**Conversation :** Les ressources sont de la consultation, pas des actions : des onglets repliés sous la décision, à un geste (SPEC-compliance-decision-panel §3). L'onglet Q&A remplace l'ancien onglet Document (DEC-080) : nos questions sur l'exigence et les réponses publiées par le client aux autres soumissionnaires. Similar montre les exigences les plus proches du tender avec leur verdict. REX et Chat sont hors V1 (DEC-021).
**Maquette :** Compliance — `compliance.html` (route `#compliance`), Decision Panel (onglets de ressources « Q&A » et « Similar »).
**Règles :** DEC-079, DEC-080, DEC-081, DEC-021, DEC-122, CONF-023, CONF-024, CONF-025  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Sous la décision, les onglets « Q&A » et « Similar » sont repliés et portent leur nombre d'éléments ; un clic en ouvre un, un second clic le replie.
2. « Q&A » liste d'abord « Our questions » sur l'exigence (ID, état « To send », « Sent », « Answer to confirm » ou « Answered », question, réponse du client ou « No answer yet », auteur et date), puis « Asked by other bidders » (questions des autres soumissionnaires liées à l'exigence, avec la réponse publiée).
3. Sans aucune question, l'onglet dit « No question on this requirement yet — neither ours nor another bidder's. »
4. « Similar » liste les exigences les plus proches du tender, chacune avec son verdict consolidé (ou « not answered yet ») et le commentaire de la réponse ; un clic ouvre cette exigence.
5. Aucune ressource ne déclenche d'action : on ne pose pas de question et on ne rend pas de verdict depuis ces onglets.
6. En V1, il n'y a ni onglet « REX » ni onglet « Chat ».
Écart maquette : la maquette affiche REX (exemples) et Chat (non construit) ; Similar y est un substitut par mots communs (les trois plus proches, à 25 % au moins).
Point ouvert : la capacité de similarité de la plateforme — source, classement, nombre d'exigences montrées — reste à spécifier (DEC-079, SPEC-compliance-decision-panel §8).

### US-CMP-16 — Poser une question au client depuis une affectation
**Carte :** En tant que contributeur, je veux écrire une question officielle au client depuis mon affectation, afin d'obtenir une précision sans bloquer mon verdict.
**Conversation :** « Ask the client » est une action secondaire, plus discrète que la décision ; le libellé ne change jamais, pour ne pas confondre une question officielle avec un chat (QA-009). La question entre dans le registre Q&A du tender à l'état « To send » ; c'est le chef de projet qui l'envoie hors de l'outil et la marque « Sent » (voir US-QA). Elle ne bloque rien : plusieurs questions peuvent être en cours sur une affectation, et le contributeur décide quand il veut (DEC-092). Une question est un échange externe, distinct d'un renvoi interne (CONF-012).
**Maquette :** Compliance — `compliance.html` (route `#compliance`), Decision Panel (« Ask the client »), Inline Form Shell, Toast ; registre : Q&A — `qa.html` (route `#qa`).
**Règles :** DEC-080, DEC-088, DEC-092, DEC-116, DEC-085, QA-001, QA-009, QA-010, CONF-012, CONF-024, CONF-028, DOM-010  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. « Ask the client » ouvre un formulaire qui rappelle « Official: it goes into the Q&A register, the project team sends it, and it doesn't hold anything up — you can give your verdict at any time. » ; la question est requise (« Write the question first ») et « Add to the Q&A register » l'enregistre.
2. La question entre dans le registre Q&A à l'état « To send », avec son auteur, sa date et le lien vers l'exigence et le système ; Compliance et Q&A la désignent par le même identifiant, et l'outil ne l'envoie jamais lui-même au client.
3. Une affectation « Awaiting answer » passe « Awaiting Q&A » ; une affectation « Proposed » ou « Reassignment needed » garde son statut.
4. Le contributeur peut poser d'autres questions sur la même affectation et rendre son verdict à tout moment, sans attendre la réponse du client.
5. Pour le contributeur qui décide, la touche Q ouvre ce formulaire.
6. « Undo » ou ⌘/Ctrl + Z retire la question du registre et rend à l'affectation son statut d'avant ; la question posée s'inscrit au journal de l'exigence.
Point ouvert : le chef de projet pose-t-il aussi des questions depuis Compliance ? La maquette ne lui donne qu'un raccourci Q qui crée une question générique, comportement de démonstration à ne pas reproduire (docs/gap CODE) ; rien n'est décidé.

### US-CMP-17 — Suivre dans Compliance l'état des questions et la réponse du client
**Carte :** En tant que contributeur, je veux voir où en est ma question et lire la réponse du client là où je travaille, afin de rendre mon verdict avec cette information sans changer d'écran.
**Conversation :** Compliance ne tient pas de registre à lui : il lit celui de Q&A (DEC-122). L'état d'une question et la réponse du client sont donc ceux du registre, avec les mêmes mots. Une réponse du client n'est jamais un verdict : c'est le contributeur qui décide (JRN-003). Le registre lui-même (marquer envoyé, importer, confirmer une réponse) est décrit dans US-QA.
**Maquette :** Compliance — `compliance.html` (route `#compliance`), Decision Panel (bandeau des questions, onglet « Q&A »), Detail / Assignment Panel (bloc « Question to the client »).
**Règles :** DEC-122, DEC-116, DEC-092, DEC-088, QA-010, CONF-028, CONF-T08, JRN-003  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. L'état de chaque question liée à une affectation est celui du registre Q&A : « To send », « Sent », « Answer to confirm » ou « Answered » ; un changement fait dans Q&A apparaît dans Compliance sans autre action.
2. Le panneau de décision affiche, quand des questions existent, « N questions in the Q&A register: <ID> <état> · … They don't hold your verdict up. »
3. Sur une affectation « Awaiting Q&A », le panneau du chef de projet montre le bloc « Question to the client » : chaque question avec son état « in the Q&A register » et, une fois « Answered », « Client's answer: … » ; « → Open the Q&A register » ouvre le registre.
4. L'arrivée de la réponse du client ne change ni le statut de l'affectation ni son verdict : aucun verdict n'est jamais créé automatiquement.
5. Une question posée depuis Compliance reste visible dans le registre et dans Compliance après navigation et reconnexion.
Point ouvert : ce que l'arrivée d'une réponse change à l'avancement de l'affectation (elle reste « Awaiting Q&A » ?) et si son contributeur en est prévenu ne sont pas spécifiés ; QA-006 parle encore de « débloquer » (docs/gap SPECS, « Q&A avec le client », Toujours ouvert ; PLAT-005).

### US-CMP-18 — Refuser une question sur une affectation déjà répondue
**Carte :** En tant que chef de projet, je veux qu'on ne puisse plus questionner le client sur une affectation dont le verdict est donné, afin qu'aucune question tardive ne rouvre un travail terminé.
**Conversation :** Une fois le verdict donné, il n'y a plus rien à demander sur cette affectation (DEC-121) ; auparavant, questionner une affectation répondue la rouvrait. Les questions posées avant le verdict restent au registre et lisibles. Une question ne change jamais le statut d'une affectation répondue (DEC-092).
**Maquette :** Compliance — `compliance.html` (route `#compliance`), Detail / Assignment Panel (« Ask the client » grisé).
**Règles :** DEC-121, DEC-092, CONF-028  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Sur une affectation « Answered », « Ask the client » est grisé, avec l'infobulle « The verdict is given — nothing left to ask on this assignment ».
2. La touche Q sur une affectation répondue est refusée avec le même message.
3. Le serveur refuse de créer une question liée à une affectation répondue, quelle que soit la voie.
4. Les questions posées avant le verdict restent dans le registre et dans les onglets Q&A, avec leur état et la réponse du client.
5. Si l'affectation redevient sans verdict (annulation, réouverture par une version), « Ask the client » est de nouveau disponible.

### US-CMP-19 — Renvoyer une affectation qui n'est pas la sienne
**Carte :** En tant que contributeur, je veux renvoyer une affectation mal allouée avec la raison et la bonne personne ou le bon système, afin qu'elle arrive vite chez qui doit y répondre.
**Conversation :** Une allocation erronée est un cas fréquent : le renvoi est une action secondaire visible, pas cachée dans un menu (SPEC-compliance-decision-panel §2). Il reprend le mécanisme de réallocation de la maquette (ALLOC-013) : trois motifs, une justification, une proposition ; la demande part dans la file d'approbation d'Allocation (voir US-ALM). C'est une boucle interne : rien ne part chez le client (CONF-012). La personne proposée appartient au même système (DEC-102).
**Maquette :** Compliance — `compliance.html` (route `#compliance`), Decision Panel (« ↩ Not mine — return it »), Reassignment Request Form.
**Règles :** ALLOC-013, DEC-011, DEC-080, DEC-085, DEC-102, DEC-104, CONF-011, CONF-012, CONF-023  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. « ↩ Not mine — return it » ouvre « Return it — why isn't it yours? » avec trois motifs : « Right system, wrong person » (par défaut), « Wrong system », « This system doesn't apply here ».
2. Pour « Right system, wrong person », « Who should take it » ne propose que les membres du même système, personne actuelle exclue ; s'il n'y en a aucun, la liste dit « Nobody else available » et le renvoi est refusé (« Nobody else is available to take this »). Pour les deux autres motifs, « Correct system » propose les autres systèmes du tender.
3. « Why » est requis : sans texte, « Return it » est refusé avec « A reason is required to return it ».
4. « Return it » passe l'affectation à « Reassignment needed », dépose la demande (motif, proposition, texte, auteur, date) dans la file d'approbation d'Allocation et l'inscrit au journal ; sur Turnkey, Allocation affiche « Reassignment requested » au niveau de l'aiguillage tant qu'elle attend.
5. « Undo » ou ⌘/Ctrl + Z retire la demande de la file et rend à l'affectation son statut d'avant.
6. Rien n'est envoyé au client : aucune question n'est créée et le registre Q&A ne change pas.
Point ouvert : sur un tender à un seul système (SIG, Mainline), ce que proposent « Wrong system » et « This system doesn't apply here » n'est pas défini ; ne pas inventer d'équivalent de la passe 1 (ALLOCATION, « Réallocation » ; OPEN-15).

### US-CMP-20 — Consolider les verdicts d'une exigence
**Carte :** En tant que chef de projet, je veux que le verdict de l'exigence se calcule depuis ceux de ses affectations, afin de connaître la position technique du tender sans arbitrer à la main.
**Conversation :** Chaque organisation rend son verdict ; le système et l'exigence sont calculés, jamais saisis (CONF-004, DEC-055) : le plus restrictif gagne et l'attente remonte (DEC-014, DEC-037). Sur Turnkey : organisations → système → exigence ; sur SIG et Mainline : organisations → exigence. Une question au client ne retient pas la consolidation (DEC-092) : seule une réponse manquante la retient. Un dossier complet ne verrouille rien (CONF-013) et il n'existe plus de verdict « final » verrouillé (DEC-028, DEC-106).
**Maquette :** Compliance — `compliance.html` (route `#compliance`), Requirement Row (colonne « Compliance »), Detail / Assignment Panel (« Pending consolidation »), Activity Timeline ; Allocation — `revue-documentaire.html` (route `#review`), Compliance Pill.
**Règles :** DEC-014, DEC-031, DEC-037, DEC-039, DEC-055, DEC-060, DEC-087, DEC-092, CONF-001, CONF-002, CONF-004, CONF-013, CONF-028, CONF-T01, CONF-T02, CONF-T03, CONF-T04, CONF-T10, CONF-T12, DOM-008, TYPE-T04, TYPE-T08  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Le verdict d'un système se calcule depuis ses organisations, celui de l'exigence depuis ses systèmes (Turnkey) ou directement depuis ses organisations (SIG, Mainline) ; aucun écran ne permet de le saisir à ces niveaux.
2. Tant qu'une affectation n'a pas de verdict, l'exigence est en attente — « — » dans la colonne « Compliance », « Pending consolidation » en tête du panneau —, quels que soient les autres verdicts.
3. Quand toutes les affectations ont un verdict, l'exigence est Not compliant si au moins une l'est, sinon Compliant : deux organisations Compliant donnent un système Compliant ; un système Not compliant parmi des Compliant donne une exigence Not compliant.
4. Une question au client en cours ne retient pas la consolidation : seule l'absence de verdict la retient.
5. Une exigence consolidée reste modifiable par le chef de projet ([US-CMP-25](#us-cmp-25--saisir-ou-modifier-une-réponse-en-tant-que-chef-de-projet)) ; toute modification ou réouverture recalcule la consolidation, et le journal note « Every system has answered — consolidated <verdict> » ou « No longer consolidated — a system is open again ».
6. Dans Allocation, la colonne Compliance montre la même valeur (Compliant, Not compliant ou Pending), en lecture seule ; un verdict ne se saisit que dans Compliance.
Écart maquette : la maquette saisit le verdict au niveau du système ; les organisations y sont affichées avec des valeurs écrites à la main et n'entrent pas dans le calcul.

### US-CMP-21 — Mettre en avant ce qui est dû
**Carte :** En tant que chef de projet, je veux qu'une exigence en attente nomme d'abord l'affectation dont on attend vraiment une réponse, afin de relancer la bonne personne plutôt que d'attendre le client.
**Conversation :** Une question au client ne bloque rien (DEC-092) ; ce qui retient une exigence, c'est une réponse due (DEC-125). L'ordre est donc : renvoi à réaffecter, puis réponse due par un contributeur, puis question chez le client, puis affectation pas encore envoyée. Cet ordre vaut pour le libellé de statut de l'exigence, le tri par statut et l'affectation ouverte par défaut.
**Maquette :** Compliance — `compliance.html` (route `#compliance`), Requirement Row (colonne « Status »), Detail / Assignment Panel (onglet « Requirement »).
**Règles :** DEC-125, DEC-092  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. La colonne « Status » d'une exigence en attente affiche le statut de l'affectation la plus due, dans l'ordre « Reassignment needed », « Awaiting answer », « Awaiting Q&A », « Proposed », suivi de « · N assignments » quand plusieurs restent ouvertes.
2. Une affectation « Awaiting answer » passe toujours avant une affectation « Awaiting Q&A » de la même exigence.
3. Trier la table sur « Status » range les exigences dans ce même ordre (mécanique du tri : US-TAB).
4. Le chef de projet qui ouvre une exigence en attente arrive sur l'affectation nommée en premier ; un contributeur arrive sur l'affectation de son système quand elle existe.
5. L'onglet « Requirement » dit « Pending — <SYS> not answered yet (<statut>) » en nommant cette même affectation.

### US-CMP-22 — Voir ce qui est attendu dans le panneau du chef de projet
**Carte :** En tant que chef de projet, je veux que le panneau de chaque affectation me dise en une phrase ce qui est attendu, et de qui, afin de savoir quoi faire sans le deviner d'après les boutons affichés.
**Conversation :** Le panneau du chef de projet — et de tout lecteur qui ne décide pas — se construit par état : en attente, question chez le client, renvoyée, partenaire, répondue, consolidée (CONF-019). L'action que nomme la phrase est la seule action primaire ; quand rien n'est attendu, la phrase le dit (CONF-020). Un verdict ne s'affiche qu'une fois par portée (CONF-018). Le bloc « What the client receives » et l'onglet Document ont disparu (DEC-078) : la conformité externe d'une affectation est un champ du panneau ([US-RSK-08](10-risques.md#us-rsk-08--dériver-la-conformité-externe-dune-affectation), [US-RSK-10](10-risques.md#us-rsk-10--corriger-la-conformité-externe-dune-affectation)).
**Maquette :** Compliance — `compliance.html` (route `#compliance`), Detail / Assignment Panel (onglets « Assignment », « Activity », « Requirement »).
**Règles :** CONF-018, CONF-019, CONF-020, CONF-022, CONF-T15, CONF-T16, DEC-078, DEC-021, DEC-125  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Dans chaque état, l'onglet « Assignment » porte exactement une phrase sur ce qui est attendu, par exemple « Waiting on <personne> — sent N days ago. Nothing is due from you but a reminder. », « Returned to you. Reallocate it and send it back out. », « Not dispatched yet. It leaves Allocation before anyone can answer it. », « Answered and consolidated. Nothing is waiting on you. »
2. L'action nommée par la phrase est la seule action primaire (« Send a reminder », « ↪ Reassign and send back out », saisie d'un verdict partenaire) ; quand la phrase n'en nomme aucune, il n'y a pas de bouton primaire, et « Ask the client » n'est jamais primaire.
3. L'en-tête montre l'ID et, seulement tant que l'exigence est en attente, « Pending consolidation » ; avec plusieurs affectations, un sélecteur montre chaque système avec son statut.
4. Sur une affectation répondue, le panneau montre la réponse et sa date ; le verdict propre à l'affectation n'apparaît que si l'exigence a plusieurs affectations : jamais deux pastilles de même valeur pour la même portée.
5. Les onglets sont « Assignment », « Activity » (journal de l'exigence, voir US-X) et « Requirement » (« The requirement text changes only through a new document version (Documents & versions). », affectations, consolidation, passage source, colonnes personnalisées) ; il n'y a ni onglet Document ni bloc « What the client receives ».
Écart maquette : la maquette affiche aussi les onglets REX (exemples) et Chat (non construit), hors V1 (DEC-021).

### US-CMP-23 — Réaffecter une affectation renvoyée
**Carte :** En tant que chef de projet, je veux réaffecter à une autre personne du système une affectation qu'un contributeur a renvoyée, afin qu'elle reparte aussitôt chez la bonne personne.
**Conversation :** Un renvoi arrive chez le chef de projet avec la raison du contributeur ([US-CMP-19](#us-cmp-19--renvoyer-une-affectation-qui-nest-pas-la-sienne)). Dans Compliance, il désigne une seule personne, membre du même système (DEC-087, DEC-102) ; c'est une action interne. Un renvoi « Wrong system » ou « This system doesn't apply here » change le système : il se tranche dans la file d'approbation d'Allocation (voir US-ALM). Il n'existe pas de réaffectation en masse.
**Maquette :** Compliance — `compliance.html` (route `#compliance`), Detail / Assignment Panel (« ↩ Returned by the contributor », « Reallocate to »), Bulk Selection Action Bar (« ↪ Reassign contributor »).
**Règles :** ALLOC-013, DEC-011, DEC-085, DEC-087, DEC-102, CONF-011, CONF-012  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Sur une affectation « Reassignment needed », le panneau montre « ↩ Returned by the contributor » avec sa raison, et la phrase « Reallocate it and send it back out. Internal action — nothing leaves the company here. »
2. « Reallocate to » ne propose que les membres du système de l'affectation ; « ↪ Reassign and send back out » sans personne choisie est refusé (« Pick someone before reassigning »).
3. Réaffecter remplace la personne, repasse l'affectation à « Awaiting answer » avec un âge de 0, marque la demande approuvée dans la file d'Allocation et s'inscrit au journal ; « Undo » ou ⌘/Ctrl + Z l'annule.
4. Seul le chef de projet réaffecte : un contributeur, même du système, ne voit pas ce formulaire, et le serveur refuse sa réaffectation.
5. Si la demande est refusée dans Allocation, l'affectation reprend son statut d'avant ; si un changement de système y est approuvé, l'affectation est remplacée par une affectation du nouveau système (voir US-ALM).
6. « ↪ Reassign contributor » de la barre de sélection ouvre la première exigence sélectionnée pour la réaffecter une à une : il n'y a pas de réaffectation en masse.
Écart maquette : le formulaire de réaffectation s'affiche aussi pour un contributeur du système de l'affectation.

### US-CMP-24 — Relancer le contributeur d'une affectation due
**Carte :** En tant que chef de projet, je veux relancer en une action la personne d'une affectation qui attend encore sa réponse, afin que la consolidation n'avance pas en silence.
**Conversation :** La relance est une seule action, quel que soit le chemin — bouton du panneau, touche R, action groupée — qui date « Last follow-up » et s'inscrit au journal (DEC-125). Elle vise la personne d'une affectation encore due (DEC-087) et n'est jamais proposée à ce contributeur lui-même (CONF-021). Un partenaire travaille hors de l'outil : on le suit directement.
**Maquette :** Compliance — `compliance.html` (route `#compliance`), Detail / Assignment Panel (« Send a reminder »), Bulk Selection Action Bar (« Send reminder »), Shortcut Help (R).
**Règles :** DEC-125, DEC-087, DEC-078, CONF-021, CONF-T18, PLAT-005  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. « Send a reminder » (panneau), la touche R et « Send reminder » (barre de sélection) ont le même effet : « Last follow-up » prend la date du jour et le journal note « <SYS> — reminder sent to <personne> ».
2. La relance n'est possible que sur une affectation « Awaiting answer » ou « Awaiting Q&A » qui a une personne ; ailleurs le bouton n'apparaît pas et R est refusé avec la raison (« Already answered — nobody owes anything on it », « Not dispatched yet — nobody owes an answer », « Returned to the project team — reallocate it instead », « Nobody assigned yet on this assignment »).
3. Sur un partenaire, R est refusé avec « <partenaire> works outside the tool — follow up with them directly ».
4. Un contributeur ne relance jamais : sur son système, R dit « It's waiting on your system — answer it rather than remind yourself », et l'action groupée lui est masquée.
5. En groupe, seules les affectations éligibles sont relancées ; le message compte les relancées et les ignorées (« … skipped — answered, not dispatched, returned or unassigned »).
Point ouvert : le canal de la relance (notification interne, e-mail) et son contenu ne sont pas définis ; la maquette ne fait que dater et journaliser (PLAT-005, OPEN-11).

### US-CMP-25 — Saisir ou modifier une réponse en tant que chef de projet
**Carte :** En tant que chef de projet, je veux saisir ou corriger le verdict d'une affectation, même quand le dossier est complet, afin de garder la main sur la réponse du tender.
**Conversation :** Le chef de projet peut répondre et modifier une réponse (DEC-013, ACC-011), même quand toutes les réponses sont reçues (DEC-014, OPEN-14) ; rien ne se verrouille. Il ne remplace pas un verdict « final », qui n'existe plus (DEC-028, DEC-106) : il change le verdict d'une affectation, et la consolidation suit. Le verdict d'un partenaire est décrit dans [US-RSK-13](10-risques.md#us-rsk-13--saisir-le-verdict-dun-partenaire-et-documenter-son-écart).
**Maquette :** non maquetté (parcours le plus proche : Partner Verdict Entry — `compliance.html`, route `#compliance`).
**Règles :** DEC-013, DEC-014, ACC-011, ACC-T08, CONF-007, CONF-013, CONF-T12, CONF-T14, OPEN-14, PLAT-003  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Sur toute affectation, le chef de projet peut rendre le verdict avec le même parcours « choisir puis confirmer » que le contributeur, Category + Topic compris sur Turnkey.
2. Sur une affectation déjà répondue, il peut changer le verdict et le commentaire, y compris quand toutes les exigences sont consolidées.
3. Chaque saisie ou modification s'inscrit au journal de l'exigence avec son auteur, sa date et l'avant → après.
4. La consolidation de l'exigence et sa conformité externe se recalculent aussitôt.
5. Un contributeur ne peut pas modifier la réponse d'un autre système ; le serveur le refuse.
Écart maquette : la maquette ne permet au chef de projet de saisir que le verdict d'un partenaire ; personne n'y révise un verdict donné, hors annulation (⌘/Ctrl + Z) et réouverture par une version.
Point ouvert : un contributeur peut-il réviser son propre verdict une fois donné ? Qui documente la stratégie et le risque d'un Not compliant saisi par le chef de projet sur l'affectation d'un contributeur ? Rien ne le décide (docs/gap SPECS, « Modèle de conformité », Toujours ouvert ; SPEC-risks §1).

### US-CMP-26 — Voir dans la cloche ce qui attend
**Carte :** En tant que chef de projet, je veux que la cloche de Compliance résume ce qui attend, par nature et avec un compte, afin d'aller droit au travail sans parcourir toute la table.
**Conversation :** Une cloche se calcule depuis l'état réel de l'écran, résume par nature avec un compte (jamais une ligne par affectation) et dit quand rien n'attend (règle des notifications, PLATFORM). Dans Compliance : affectations renvoyées à réaffecter, questions chez le client (pour information, elles ne bloquent rien), réponses rouvertes par une nouvelle version. Les canaux de notification (e-mail, déclencheurs) relèvent de US-X.
**Maquette :** Compliance — `compliance.html` (route `#compliance`), Notifications Dropdown, Notification Item, Notification Dot.
**Règles :** PLAT-005, DEC-092, DEC-122, DEC-125  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. La cloche liste une ligne par nature, avec son compte : « N assignments returned by contributors — reallocate them », « N assignments have a question with the client » (« nothing due from you »), « N answers reopened by a new document version — the requirements changed ».
2. Une nature qui ne concerne qu'une affectation nomme son exigence, et cliquer l'ouvre ; cliquer une nature à plusieurs éléments filtre la table sur eux.
3. Quand rien n'attend, la cloche dit « Nothing waiting on you here. » et son point disparaît.
4. Pour un contributeur, la cloche ne compte que les affectations de son système.
5. Le contenu se recalcule à chaque ouverture et à chaque changement : il ne montre jamais un état périmé.

### US-CMP-27 — Rouvrir les verdicts d'une exigence modifiée par une nouvelle version
**Carte :** En tant que chef de projet, je veux que les verdicts d'une exigence dont le texte a changé dans une nouvelle version repassent en attente, afin qu'aucun verdict ne reste posé sur un texte qui n'existe plus.
**Conversation :** Une nouvelle version d'un document qui modifie une exigence rouvre ses verdicts dans Compliance (DEC-016, DEC-122, LIFE-007) : chaque affectation répondue redemande un verdict, et la mention « Reopened by … » dit pourquoi. Les exigences inchangées ne bougent pas du seul fait du téléversement. Le nombre de réponses rouvertes annoncé par Documents & versions est exactement celui que Compliance rouvre. Le téléversement et l'écart entre versions sont dans US-DOC ; le retour en To review côté Allocation dans US-CHG.
**Maquette :** Compliance — `compliance.html` (route `#compliance`), Decision Panel (bandeau « Reopened by »), Detail / Assignment Panel, Notifications Dropdown ; Documents & versions — `documents.html` (route `#documents`).
**Règles :** LIFE-007, LIFE-T05, LIFE-T09, DEC-016, DEC-122, CONF-014  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Quand une nouvelle version modifie une exigence, chacune de ses affectations « Answered » repasse « Awaiting answer », sans verdict ni commentaire, avec un âge de 0 ; l'exigence n'est plus consolidée.
2. Les affectations encore sans verdict et les exigences inchangées ne changent pas.
3. L'affectation rouverte porte « Reopened by <document> <version> » : bandeau du panneau de décision (« … — the requirement changed, so the verdict went back to pending. Give it again. ») et phrase du panneau du chef de projet.
4. Chaque réouverture s'inscrit au journal de l'exigence (auteur « Documents & versions », verdict d'avant → « Awaiting answer »), et la cloche compte les réponses rouvertes.
5. Le nombre « N answers reopened by this version » annoncé par Documents & versions est égal au nombre d'affectations rouvertes dans Compliance.
Écart maquette : la maquette choisit elle-même les exigences « modifiées » et rejoue la réouverture à chaque ouverture de l'écran.
Point ouvert : le sort de la stratégie d'écart, des risques liés et de la correction du chef de projet d'une affectation rouverte n'est pas décidé (voir [US-RSK-09](10-risques.md#us-rsk-09--consolider-la-conformité-externe-dune-exigence)) ; l'effet d'une correction de traduction sur une exigence déjà répondue (To review seulement, ou verdicts rouverts ?) non plus (LIFE-008 ; docs/gap README).

### US-CMP-28 — Exporter le registre de conformité avec options
**Carte :** En tant que chef de projet, je veux exporter le registre de conformité en choisissant le format, les lignes, les colonnes et la langue du texte, afin de produire le bon fichier, pour le client ou pour un partenaire.
**Conversation :** L'export à options remplace le registre fixe d'autrefois (DEC-081). « What the filters show » sert aussi à envoyer à un partenaire la part qui le concerne : le filtre appliqué y est dit en clair (CONF-026). Les colonnes personnalisées sont internes : décochées par défaut et marquées comme telles (DEC-068, DEC-097). Le texte d'exigence peut sortir en langue originale ou en anglais ; commentaires et catégories restent en anglais (LANG-003). Tout lecteur du tender peut exporter ce qu'il a le droit de lire (DEC-012).
**Maquette :** Compliance — `compliance.html` (route `#compliance`), Export Options Modal (bouton « Export »).
**Règles :** DEC-081, DEC-082, DEC-068, DEC-097, DEC-012, CONF-025, CONF-026, LANG-003, LIFE-004, PLAT-002, PLAT-004  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. « Export » ouvre « Export the compliance register » : format « Excel (.xlsx) », « CSV » ou « PDF » ; lignes « All requirements (N) », « What the filters show — N requirements (<filtre en clair>) » ou « Selected rows (N) », ce dernier inactif sans sélection.
2. Par défaut, les lignes sont la sélection s'il y en a une, sinon la vue filtrée si un filtre est actif, sinon tout ; les colonnes cochées sont celles visibles dans la table, avec « All » et « As in the table ».
3. Les colonnes personnalisées portent la marque « internal » et sont décochées par défaut ; une note dit « Custom columns are internal: leave them unticked for the file that goes to the client. », et les inclure fait avertir que le fichier n'est pas pour le client en l'état.
4. Sur un tender dont la langue source n'est pas l'anglais, « Requirement text » propose « Original (<langue>) » ou « English translation » ; commentaires et catégories restent en anglais dans les deux cas.
5. Exporter sans aucune colonne est refusé (« Tick at least one column ») ; le fichier contient exactement les lignes et colonnes choisies, dans l'ordre du document.
6. Le serveur produit le fichier à partir des seules données que le demandeur a le droit de lire.
Écart maquette : la génération n'est qu'un message ; l'anglais y est coché par défaut, alors que LANG-003 veut le texte original.
Point ouvert : la langue par défaut de l'export (LANG-003 : originale ; maquette : anglais) ; ce qui part au client — la conformité externe seule ou aussi l'interne, quelles colonnes — n'est pas défini, et « colonnes personnalisées hors export client » reste un défaut à confirmer (DEC-068 ; docs/gap SPECS, « Écran Compliance », Toujours ouvert).

## Couverture
- Règles couvertes :
  - CONF-001 → [US-CMP-02](#us-cmp-02--suivre-lavancement-dune-affectation-par-son-statut), [US-CMP-03](#us-cmp-03--lire-les-colonnes-de-la-table-compliance), [US-CMP-20](#us-cmp-20--consolider-les-verdicts-dune-exigence)
  - CONF-002 → [US-CMP-20](#us-cmp-20--consolider-les-verdicts-dune-exigence)
  - CONF-004 → [US-CMP-04](#us-cmp-04--déplier-une-exigence-en-systèmes-et-en-organisations), [US-CMP-20](#us-cmp-20--consolider-les-verdicts-dune-exigence) (verdict par organisation ; la maquette le porte au système)
  - CONF-007 (saisie et modification par le chef de projet ; « remplacer et verrouiller le final » est caduc, DEC-028/DEC-106) → [US-CMP-25](#us-cmp-25--saisir-ou-modifier-une-réponse-en-tant-que-chef-de-projet)
  - CONF-008 (Category + Topic sur Turnkey seulement depuis DEC-107 ; « R&D conservé en interne » caduc, DEC-031) → [US-CMP-11](#us-cmp-11--rendre-un-verdict--choisir-puis-confirmer), [US-CMP-12](#us-cmp-12--qualifier-un-not-compliant-par-category-et-topic-sur-un-tender-turnkey)
  - CONF-009 → [US-CMP-03](#us-cmp-03--lire-les-colonnes-de-la-table-compliance)
  - CONF-010 (la personne « affectée » est celle de l'OBS, DEC-087) → [US-CMP-01](#us-cmp-01--créer-les-affectations-quand-lallocation-est-validée), [US-CMP-08](#us-cmp-08--consulter-tout-le-tender-et-nagir-que-sur-son-système), [US-CMP-11](#us-cmp-11--rendre-un-verdict--choisir-puis-confirmer)
  - CONF-011 → [US-CMP-19](#us-cmp-19--renvoyer-une-affectation-qui-nest-pas-la-sienne), [US-CMP-23](#us-cmp-23--réaffecter-une-affectation-renvoyée)
  - CONF-012 → [US-CMP-16](#us-cmp-16--poser-une-question-au-client-depuis-une-affectation), [US-CMP-19](#us-cmp-19--renvoyer-une-affectation-qui-nest-pas-la-sienne), [US-CMP-23](#us-cmp-23--réaffecter-une-affectation-renvoyée)
  - CONF-013 → [US-CMP-07](#us-cmp-07--suivre-lavancement-de-la-consolidation), [US-CMP-20](#us-cmp-20--consolider-les-verdicts-dune-exigence), [US-CMP-25](#us-cmp-25--saisir-ou-modifier-une-réponse-en-tant-que-chef-de-projet)
  - CONF-018 → [US-CMP-22](#us-cmp-22--voir-ce-qui-est-attendu-dans-le-panneau-du-chef-de-projet)
  - CONF-019 → [US-CMP-22](#us-cmp-22--voir-ce-qui-est-attendu-dans-le-panneau-du-chef-de-projet)
  - CONF-020 (1ʳᵉ phrase : l'action nommée est primaire ; la seconde, sur une position arbitrée avec son risque, relève du modèle de déclaration caduc, DEC-106) → [US-CMP-22](#us-cmp-22--voir-ce-qui-est-attendu-dans-le-panneau-du-chef-de-projet)
  - CONF-021 → [US-CMP-24](#us-cmp-24--relancer-le-contributeur-dune-affectation-due)
  - CONF-022 (sauf « Risk accepted » et le formulaire de déclaration, caducs depuis DEC-106) → [US-CMP-05](#us-cmp-05--lire-la-table-dans-lordre-du-document), [US-CMP-22](#us-cmp-22--voir-ce-qui-est-attendu-dans-le-panneau-du-chef-de-projet)
  - CONF-023 (sauf « Compliant en un geste » et la ligne « Yours », remplacés par DEC-080 ; Category + Topic : Turnkey seulement, DEC-107) → [US-CMP-09](#us-cmp-09--arriver-sur-sa-file-et-la-parcourir) à [US-CMP-15](#us-cmp-15--consulter-les-questions-et-les-exigences-similaires), [US-CMP-19](#us-cmp-19--renvoyer-une-affectation-qui-nest-pas-la-sienne)
  - CONF-024 → [US-CMP-10](#us-cmp-10--lire-lexigence-en-entier-dans-le-panneau-de-décision), [US-CMP-11](#us-cmp-11--rendre-un-verdict--choisir-puis-confirmer), [US-CMP-15](#us-cmp-15--consulter-les-questions-et-les-exigences-similaires), [US-CMP-16](#us-cmp-16--poser-une-question-au-client-depuis-une-affectation)
  - CONF-025 (sauf les colonnes « propres à Compliance », devenues communes par DEC-097 → US-TAB) → [US-CMP-04](#us-cmp-04--déplier-une-exigence-en-systèmes-et-en-organisations), [US-CMP-05](#us-cmp-05--lire-la-table-dans-lordre-du-document), [US-CMP-07](#us-cmp-07--suivre-lavancement-de-la-consolidation), [US-CMP-10](#us-cmp-10--lire-lexigence-en-entier-dans-le-panneau-de-décision), [US-CMP-14](#us-cmp-14--mettre-une-affectation-de-côté), [US-CMP-28](#us-cmp-28--exporter-le-registre-de-conformité-avec-options)
  - CONF-026 → [US-RSK-13](10-risques.md#us-rsk-13--saisir-le-verdict-dun-partenaire-et-documenter-son-écart) (saisie du verdict partenaire), [US-CMP-28](#us-cmp-28--exporter-le-registre-de-conformité-avec-options) (export « What the filters show » qui dit le filtre)
  - CONF-027 (ordre du document sans tri ; le tri par en-têtes lui-même → US-TAB) → [US-CMP-05](#us-cmp-05--lire-la-table-dans-lordre-du-document)
  - CONF-028 → [US-CMP-16](#us-cmp-16--poser-une-question-au-client-depuis-une-affectation), [US-CMP-17](#us-cmp-17--suivre-dans-compliance-létat-des-questions-et-la-réponse-du-client), [US-CMP-18](#us-cmp-18--refuser-une-question-sur-une-affectation-déjà-répondue), [US-CMP-20](#us-cmp-20--consolider-les-verdicts-dune-exigence)
  - CONF-029 → [US-RSK-01](10-risques.md#us-rsk-01--écrire-les-stratégies-décart-du-tender) à [US-RSK-12](10-risques.md#us-rsk-12--passer-dun-risque-à-ses-exigences-et-inversement)
  - CONF-T01, CONF-T02, CONF-T03, CONF-T04 → [US-CMP-20](#us-cmp-20--consolider-les-verdicts-dune-exigence)
  - CONF-T07 → [US-CMP-08](#us-cmp-08--consulter-tout-le-tender-et-nagir-que-sur-son-système)
  - CONF-T08 (sans la notion de question « bloquante », caduque par DEC-092) → [US-CMP-17](#us-cmp-17--suivre-dans-compliance-létat-des-questions-et-la-réponse-du-client)
  - CONF-T10 → [US-CMP-01](#us-cmp-01--créer-les-affectations-quand-lallocation-est-validée), [US-CMP-20](#us-cmp-20--consolider-les-verdicts-dune-exigence)
  - CONF-T12 → [US-CMP-20](#us-cmp-20--consolider-les-verdicts-dune-exigence), [US-CMP-25](#us-cmp-25--saisir-ou-modifier-une-réponse-en-tant-que-chef-de-projet)
  - CONF-T14 → [US-CMP-08](#us-cmp-08--consulter-tout-le-tender-et-nagir-que-sur-son-système), [US-CMP-25](#us-cmp-25--saisir-ou-modifier-une-réponse-en-tant-que-chef-de-projet)
  - CONF-T15 (premier énoncé : jamais deux pastilles de même valeur pour une même portée) → [US-CMP-22](#us-cmp-22--voir-ce-qui-est-attendu-dans-le-panneau-du-chef-de-projet)
  - CONF-T16 → [US-CMP-22](#us-cmp-22--voir-ce-qui-est-attendu-dans-le-panneau-du-chef-de-projet)
  - CONF-T18 → [US-CMP-24](#us-cmp-24--relancer-le-contributeur-dune-affectation-due)
  - DOM-008 (sans le « responsable unique de suivi », remplacé par DEC-087) → [US-CMP-11](#us-cmp-11--rendre-un-verdict--choisir-puis-confirmer), [US-CMP-12](#us-cmp-12--qualifier-un-not-compliant-par-category-et-topic-sur-un-tender-turnkey), [US-CMP-20](#us-cmp-20--consolider-les-verdicts-dune-exigence)
  - DOM-010 (côté Compliance : lien question ↔ exigence et système ; l'objet question lui-même → US-QA ; le « travail bloqué » est caduc, DEC-092) → [US-CMP-16](#us-cmp-16--poser-une-question-au-client-depuis-une-affectation), [US-CMP-17](#us-cmp-17--suivre-dans-compliance-létat-des-questions-et-la-réponse-du-client)
  - LIFE-007 (« déverrouiller » se lit « rouvrir », DEC-122) → [US-CMP-27](#us-cmp-27--rouvrir-les-verdicts-dune-exigence-modifiée-par-une-nouvelle-version)
  - JRN-003 (« détail Document » caduc depuis DEC-078) → [US-CMP-08](#us-cmp-08--consulter-tout-le-tender-et-nagir-que-sur-son-système) à [US-CMP-28](#us-cmp-28--exporter-le-registre-de-conformité-avec-options), et [US-RSK-04](10-risques.md#us-rsk-04--choisir-une-stratégie-décart-après-un-not-compliant) à [US-RSK-10](10-risques.md#us-rsk-10--corriger-la-conformité-externe-dune-affectation)
- Non couvertes, avec la raison :
  - CONF-003 — caduque (DEC-031 : deux verdicts ; « le plus restrictif gagne » et la propagation de pending, à deux valeurs, sont couverts par [US-CMP-20](#us-cmp-20--consolider-les-verdicts-dune-exigence)).
  - CONF-005, CONF-006 — caduques (DEC-028 puis DEC-106 : plus de verrou ni de verdict final).
  - CONF-014 — caduque dans sa forme (déverrouillage, DEC-028) ; le retour à pending est repris par LIFE-007 / DEC-122 dans [US-CMP-27](#us-cmp-27--rouvrir-les-verdicts-dune-exigence-modifiée-par-une-nouvelle-version).
  - CONF-015 — caduque (DEC-031 ; DEC-024 sans objet : plus de conversion R&D à l'export).
  - CONF-016 — caduque (remplacée par DEC-078, puis DEC-106).
  - CONF-017 — caduque (DEC-106 : plus de déclaration externe ni de « Risk accepted »).
  - CONF-T05, CONF-T06 — caduques (DEC-028, DEC-106 : plus de verrou).
  - CONF-T09 — caduque (DEC-031 : R&D n'est plus un verdict).
  - CONF-T11 — caduque dans sa forme (verrou, DEC-028) ; la réouverture est couverte par [US-CMP-27](#us-cmp-27--rouvrir-les-verdicts-dune-exigence-modifiée-par-une-nouvelle-version).
  - CONF-T13 — caduque (DEC-031).
  - CONF-T15 (second énoncé, R&D à l'export) — caduque (DEC-031). L'identifiant CONF-T15 est attribué deux fois dans COMPLIANCE.md.
  - CONF-T17 — caduque (DEC-106 : plus de déclaration externe arbitrée).
  - DOM-009 — caduque pour le verdict « final » et le verrou (DEC-028, DEC-106) ; le verdict dérivé est le verdict consolidé de [US-CMP-20](#us-cmp-20--consolider-les-verdicts-dune-exigence).
