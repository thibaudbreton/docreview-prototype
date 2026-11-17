<!-- Généré depuis le backlog du 10 octobre 2026 ; voir README.md pour les conventions. -->
# Allocation — modèle et panneau (US-ALM)

L'écran Allocation est le cœur du premier pilote (DEC-022) : le tender manager, puis les contributeurs de chaque sous-système, y corrigent ce que l'IA a proposé pour chaque exigence et la valident, ce qui l'envoie vers Compliance. Parcours JRN-002 : ouvrir Allocation → isoler ce qui est à revoir → inspecter la source et les propositions → corriger → valider → retrouver le travail dans Compliance. Écran `revue-documentaire.html` (route `#review`) ; la mécanique de table (filtres, clavier, sélection, colonnes, recherche, annulation) est dans US-TAB, la vue Document dans US-DOCV, les changements de version dans US-CHG, la caractérisation par l'IA dans US-CAP, les paramètres du tender dans US-CFG, le journal d'activité dans US-X.

- **Type** : ce qu'est un bloc capturé — Information, Heading (titre) ou Requirement (exigence) ; seules les exigences s'allouent.
- **Classe** : technique ou non technique (« Class » à l'écran).
- **Sous-système** : ce qui porte le travail (« Sub-system » à l'écran) ; un tender est émis sur un seul sous-système, et un Turnkey répartit ses exigences vers des sous-systèmes. Il n'existe qu'un niveau : plus de « sous-système » sous un sous-système (DEC-126).
- **Aiguillage** : sur un Turnkey, la première passe de l'IA, qui envoie l'exigence vers un ou plusieurs sous-systèmes (concept « TK OBS »).
- **Modèle** : ce qu'applique le produit d'un sous-système (SIG : Urban, Mainline Wayside, Mainline Onboard) pour dériver la chaîne ; un sous-système peut ne pas en avoir.
- **ABS → PBS → OBS** : l'activité (Activity Breakdown Structure), l'élément du produit (Product Breakdown Structure), puis l'organisation qui traite l'exigence (Organisation Breakdown Structure) — une organisation, jamais une personne.
- **Allocation** : une organisation (une entrée OBS) et la personne qui en répond, la personne en charge (PIC) — colonne et champ « PIC » à l'écran (DEC-126).
- **Relance** : rejouer un modèle sur une exigence déjà dérivée ; **réallocation** : changer qui répond, ou quel sous-système.
- **Clés** : le classeur de référence PBS / OBS / ABS des produits SIG Mainline.
- **Partenaire externe** : entreprise ajoutée comme sous-système sur un Turnkey, qui travaille hors de l'outil.

### US-ALM-01 — Lire le statut d'une exigence
**Carte :** En tant que tender manager, je veux voir où en est chaque exigence entre caractérisation et allocation, afin de savoir ce qu'il reste à faire avant de l'envoyer vers Compliance.
**Conversation :** Quatre statuts disent l'avancement : Incomplete (il manque une information), To review (l'IA doute, ou un changement l'exige), To validate (tout est rempli, reste la validation humaine), Allocated (validée par une personne). Le statut affiché est le plus restrictif entre caractérisation et allocation ; les titres et blocs d'information n'en ont pas. Sur un Turnkey, le tender manager lit le statut du niveau Turnkey (type, classe, aiguillage), qui peut aussi valoir « Reassignment requested », et chaque sous-système porte le sien ([US-ALM-27](#us-alm-27--valider-laiguillage-dune-exigence-turnkey), [US-ALM-28](#us-alm-28--valider-lallocation-dun-sous-système-dun-turnkey)). Filtrer par statut : voir US-TAB.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Status Pill (Requirement Workflow State) dans la colonne Status et l'en-tête du Detail / Assignment Panel.
**Règles :** DEC-073, DEC-103, DEC-104, DEC-025, DEC-072, ALLOC-007, ALLOC-018, ALLOC-T04, ALLOC-T24, LIFE-015, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Chaque exigence porte un et un seul statut parmi « Incomplete », « To review », « To validate » et « Allocated » (plus « Reassignment requested » au niveau Turnkey), le même dans la ligne de la table, l'en-tête du panneau, la vue Document et le navigateur.
2. Aucun titre ni bloc d'information n'affiche de statut, dans aucune vue, et aucun n'entre dans un compteur de statut.
3. Une exigence est « Incomplete » tant que sa classe manque, qu'elle n'a aucun sous-système ou que son allocation est vide (aucune organisation, sous-système sans modèle pas encore rempli) ; l'absence de personne ne la rend jamais « Incomplete ».
4. Le statut affiché est le moins avancé des deux axes : une caractérisation « To validate » avec une allocation « Incomplete » s'affiche « Incomplete ».
5. Un résultat de l'IA complet et sûr reste « To validate » : seule une validation humaine fait passer une exigence à « Allocated ».
6. Il n'existe ni statut, ni pastille, ni filtre « Awaiting manual allocation ».
Point ouvert : libellés exacts des états à harmoniser entre écrans (OPEN-13) ; allocation partiellement remplie : voir [US-ALM-14](#us-alm-14--corriger-la-chaîne-abs--pbs--obs).

### US-ALM-02 — Savoir pourquoi une exigence est à revoir
**Carte :** En tant que tender manager, je veux lire le motif qui a mis une exigence « To review », afin de vérifier le bon champ sans tout relire.
**Conversation :** Une exigence passe « To review » pour un motif précis : type ou classe proposés par l'IA au niveau Low ; sous-système détecté par l'IA sous le seuil de certitude (Turnkey) ; ABS, PBS ou OBS dérivé sous le seuil ; exigence ajoutée ou modifiée par la version en vigueur de son document (US-CHG) ; texte ou traduction corrigé (LIFE-008, US-CAP) ; marquage manuel. Le motif s'affiche en tête du panneau et dans l'infobulle de la pastille. Il dit quoi regarder sans bloquer : valider confirme ce que l'IA a proposé ([US-ALM-26](#us-alm-26--valider-une-exigence-en-un-seul-geste)).
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), ligne « ⚠ » en tête du Detail / Assignment Panel, infobulle de la Status Pill, « Mark to review » de la Bulk Selection Action Bar.
**Règles :** DEC-120, DEC-072, DEC-026, DEC-054, DEC-099, ALLOC-006, AI-014, LIFE-015, LIFE-008, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes (motif « Sub-system » : Turnkey)
**Critères d'acceptation :**
1. Une exigence « To review » affiche son motif en tête du panneau (« ⚠ » suivi du motif, par ex. « Class proposed by the AI with low confidence ») et dans l'infobulle de sa pastille de statut.
2. Un type ou une classe proposés au niveau Low envoient en « To review » ; Medium et High n'y envoient pas.
3. Un ABS, un PBS ou une organisation dérivé sous 75 % envoie en « To review » avec le maillon et son score (« Weak OBS derivation (61%) — the proposed organisation may be wrong ») ; le motif parle d'organisation, jamais de personne.
4. Sur un Turnkey, une certitude d'aiguillage sous le seuil envoie en « To review » avec « Sub-system is AI-detected, unconfirmed » ; ce motif n'existe pas sur un tender SIG.
5. « Mark to review » passe les exigences sélectionnées « To review » avec « Flagged for review in bulk » ; un contributeur ne marque que celles de son sous-système.
6. Corriger le champ en cause ou valider l'exigence retire le motif.
Écart maquette : le motif de dérivation faible dit encore « the proposed assignment may be wrong » (DEC-054 : une organisation) ; une correction de traduction ne repasse pas l'exigence en revue (LIFE-008).
Point ouvert : le seuil de 75 % est celui de la maquette ; sa calibration relève du chantier IA (AI.md).

### US-ALM-03 — Suivre l'avancement dans la barre de statut
**Carte :** En tant que tender manager, je veux voir combien d'exigences sont dans chaque statut et la part déjà allouée, afin de savoir où porter l'effort.
**Conversation :** La barre en tête d'Allocation compte les exigences du tender par statut et donne la part allouée ; elle porte sur tout le tender, pour tout lecteur (DEC-012). La pastille des demandes de réallocation n'apparaît que s'il y en a. Cliquer un compteur filtre la table (US-TAB) ; la pastille « changed in latest version » relève de US-CHG et la carte Allocation du tableau de bord (DEC-098) de US-DASH.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Triage Bar (« % allocated », pastilles de statut, « pending reassignment »).
**Règles :** DEC-012, DEC-073, DEC-103, DEC-104, ALLOC-022, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. La barre affiche le nombre d'exigences du tender puis un compteur par statut (« incomplete », « to review », « to validate », « allocated ») ; titres et blocs d'information ne sont comptés nulle part.
2. « N% allocated » vaut les exigences allouées divisées par toutes les exigences du tender, arrondi à l'entier.
3. « N pending reassignment » n'apparaît qu'avec au moins une demande de réallocation en attente et disparaît quand la dernière est traitée.
4. Aucune pastille « awaiting manual allocation » n'existe : ces exigences comptent dans « incomplete ».
5. Un contributeur voit les compteurs de tout le tender ; sur un Turnkey, les exigences de son sous-système y comptent avec le statut de son sous-système.
Point ouvert : sur un Turnkey, « allocated » veut-il dire aiguillage validé (statut du niveau Turnkey, DEC-104) ou tous les sous-systèmes validés (carte du tableau de bord, DEC-098) ? La maquette compte le premier dans la barre et transmet le second au tableau de bord, alors que l'infobulle de la barre annonce le second.

### US-ALM-04 — Corriger le type et la classe d'une exigence
**Carte :** En tant que tender manager, je veux corriger le type d'un bloc et la classe d'une exigence dans son détail, afin que l'allocation parte d'une caractérisation juste.
**Conversation :** Le type dit ce qu'est un bloc — Information, Heading ou Requirement, rien d'autre ; il se corrige en tête du détail (et dans la vue Document, US-DOCV) et n'a pas de colonne dans la table. La classe (Technical / Non-technical) s'affiche juste en dessous, dans le détail de toute exigence, SIG compris, et se bascule aussi dans la colonne Class ou par l'action groupée « Classify ». Les valeurs Functional / Performance / Security / Interface / Regulatory ont quitté Allocation. Un bloc capturé ne se supprime jamais : on le reclasse en Information. Changer le type ou la classe propose une relance ([US-ALM-25](#us-alm-25--relancer-après-un-changement-de-type-ou-de-classe)).
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Nature and Class Fields du Detail / Assignment Panel, colonne Class, « Classify » de la Bulk Selection Action Bar.
**Règles :** DEC-074, DEC-073, DEC-094, DEC-075, ALLOC-017, ALLOC-023, ALLOC-T25, ALLOC-T26, KEY-T04, LIFE-005, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Le détail d'une exigence montre « Type » (Information, Heading, Requirement — trois valeurs seulement) puis « Class », sur tout tender ; un titre ou un bloc d'information ne montre que « Type ».
2. Allocation n'a aucune colonne Type et n'affiche nulle part (table, détail, filtres, recherche, actions groupées) les valeurs Functional, Performance, Security, Interface ou Regulatory.
3. Reclasser un bloc conserve son identifiant ; un bloc d'information reclassé en Requirement entre « Incomplete », et reçoit le sous-système SIG sur un tender SIG.
4. Reclasser une exigence en Information efface son allocation (sous-systèmes, ABS, PBS, organisations, personnes) et la sort des statuts et compteurs ; si une réponse est enregistrée, une confirmation annonce la suppression définitive de ce travail, et refuser ne change rien.
5. Aucune action ne supprime un bloc capturé ; seules les lignes dupliquées à la main depuis une image restent supprimables (US-CAP).
6. Changer la classe depuis le détail, la colonne Class ou « Classify » donne la même valeur partout et retire le niveau de confiance de l'IA sur ce champ.
Écart maquette : la recherche plein texte et des puces de la vue Document lisent encore les valeurs Functional / Performance (ALLOC-T26).

### US-ALM-05 — Voir le niveau de confiance de l'IA sur le type et la classe
**Carte :** En tant que tender manager, je veux voir si l'IA est peu, moyennement ou très sûre du type et de la classe qu'elle propose, afin de concentrer ma relecture sur les appels incertains.
**Conversation :** Le modèle de caractérisation donne un niveau Low, Medium ou High, pas un pourcentage ; les modèles d'allocation gardent leurs pourcentages ([US-ALM-07](#us-alm-07--voir-vers-quels-sous-systèmes-un-turnkey-a-aiguillé-une-exigence), [US-ALM-14](#us-alm-14--corriger-la-chaîne-abs--pbs--obs)). Le niveau s'affiche à côté du libellé tant que la valeur est celle de l'IA ; Low est l'appel incertain qui envoie en « To review ». Il n'y a pas de bouton « Confirm » : valider l'exigence confirme ce que l'IA a détecté (DEC-099) — ALLOC-017 décrit encore un tel bouton, caduc. La production des niveaux par l'IA relève de US-CAP.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Confidence Level Badge dans les Nature and Class Fields ; Nature Picker en pointillés dans la vue Document.
**Règles :** DEC-120, DEC-099, DEC-073, AI-014, ALLOC-006, ALLOC-007, DOM-007, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. À côté de « Type » et de « Class », un badge « Low », « Medium » ou « High » s'affiche tant que la valeur est celle proposée par l'IA ; aucun pourcentage n'est montré pour ces deux champs.
2. Une valeur changée par une personne ne porte plus de badge.
3. « Low » est mis en évidence et met l'exigence « To review » avec le motif du champ ; « Medium » et « High » ne changent pas le statut.
4. Valider l'exigence retire badges et marques de doute ; il n'existe ni bouton « Confirm » ni mention « Detected by the AI, not confirmed yet ».
5. Sur un titre ou un bloc d'information dont l'IA doute, la puce de type est en pointillés, sans statut ; choisir le type déjà en place le confirme, en choisir un autre reclasse le bloc.
6. Une capture qui porte encore des scores numériques est lue avec les mêmes seuils : moins de 75 = Low, moins de 85 = Medium, sinon High.

### US-ALM-06 — Réserver le type et la classe au tender manager
**Carte :** En tant que tender manager, je veux être le seul à pouvoir changer le type et la classe, afin qu'un sous-système ne modifie pas ce qui décide de la dérivation de tous les autres.
**Conversation :** Type et classe déterminent ce que le modèle dérive pour chaque sous-système : elles appartiennent à l'équipe de gestion du tender, tous tender managers confondus. Un contributeur les voit partout, sans pouvoir les modifier — ni dans le détail, ni dans la table, ni par action groupée, ni dans la vue Document. Le refus vaut aussi hors de l'écran, côté serveur.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Nature and Class Fields (variante lecture seule), colonne Class, Bulk Selection Action Bar.
**Règles :** DEC-086, ACC-012, ACC-001, PLAT-002, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Pour un contributeur, Type et Class s'affichent en texte suivi de « Set by the tender manager », sans liste de choix.
2. La bascule de la colonne Class est désactivée pour un contributeur, avec l'infobulle « Set by the tender manager ».
3. L'action groupée « Classify » n'est pas proposée à un contributeur.
4. Le sélecteur de type de la vue Document est inactif pour un contributeur (US-DOCV).
5. Toute tentative d'un contributeur de changer le type ou la classe par un autre chemin est refusée par le serveur avec « Type and class are set by the tender manager », sans rien modifier.
6. Chaque tender manager du tender garde ce droit.

### US-ALM-07 — Voir vers quels sous-systèmes un Turnkey a aiguillé une exigence
**Carte :** En tant que tender manager d'un tender Turnkey, je veux voir vers quel(s) sous-système(s) l'IA a aiguillé chaque exigence et avec quelle certitude, afin de repérer les aiguillages douteux.
**Conversation :** Sur un Turnkey, la première passe lit une seule dimension selon la classe — le PBS d'une exigence technique, l'ABS d'une non technique — puis route l'exigence vers un ou plusieurs sous-systèmes. Ce routage (le concept « TK OBS ») s'affiche dans la colonne Sub-system, avec sa certitude en pourcentage à côté de chaque étiquette ; il n'y a plus de colonne « TK OBS ». Le détail du tender manager reprend, dans l'ordre : Type, Class, la dimension lue, puis la liste Sub-system. Rien de cela n'existe sur un tender SIG ([US-ALM-13](#us-alm-13--allouer-sur-un-tender-sig-autonome-sans-axe-sous-système)).
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Activity / Requirement Tag avec certitude (`.sys-conf`) dans la colonne Sub-system, Derivation Chain (variante « Turnkey pass 1 ») du Detail / Assignment Panel.
**Règles :** DEC-077, DEC-034, DEC-046, DEC-120, ALLOC-001, ALLOC-002, ALLOC-006, TYPE-T04, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Turnkey
**Critères d'acceptation :**
1. La cellule Sub-system montre l'étiquette de chaque sous-système ; sur une exigence à un sous-système, et sur chaque sous-ligne de sous-système, la certitude du routage s'affiche en % à côté (jamais sur la ligne parente d'une exigence multi-sous-systèmes).
2. Une certitude sous le seuil (75 %) s'affiche en couleur IA, avec une infobulle qui dit que le sous-système est peut-être le mauvais.
3. Aucune colonne « TK OBS » n'existe.
4. Le détail affiche Type, Class, puis « PBS » si l'exigence est technique ou « ABS » sinon, avec la mention que la passe ne lit que cette dimension, puis la liste Sub-system.
5. Dans la liste Sub-system, chaque sous-système porte soit le % de l'IA, soit « manual » s'il a été ajouté à la main, et « has a model » quand il a son propre modèle d'allocation.
6. Seuls Type et Class portent un niveau Low / Medium / High ; la dimension lue et chaque sous-système gardent un pourcentage.

### US-ALM-08 — Ajouter ou retirer un sous-système
**Carte :** En tant que tender manager d'un tender Turnkey, je veux ajouter directement un sous-système à une exigence ou en retirer, jusqu'à n'en laisser aucun, afin de corriger l'aiguillage sans passer par une demande.
**Conversation :** Le tender manager ne se propose rien à lui-même : « + Add sub-system » ajoute le sous-système tout de suite, par une recherche sur le code et le nom, y compris sur une exigence qui n'en a plus. Chaque sous-système porte un ✕, le dernier compris ; une exigence sans sous-système est « Incomplete » jusqu'à un nouvel ajout. Retirer un sous-système efface son allocation, et si une réponse y est déjà enregistrée, la perte est annoncée avant. Un contributeur passe par une proposition ([US-ALM-10](#us-alm-10--proposer-un-sous-système-manquant)).
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), liste Sub-system de la Derivation Chain (« + Add sub-system », recherche `.obs-pick`), cellule Sub-system de la table, « Assign › Sub-system » de la Bulk Selection Action Bar.
**Règles :** DEC-076, DEC-046, ALLOC-020, ALLOC-T28, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Turnkey
**Critères d'acceptation :**
1. « + Add sub-system » ouvre une recherche (« Search a sub-system… ») sur le code et le nom, limitée aux sous-systèmes absents de l'exigence ; un clic ou Entrée ajoute le sous-système, marqué « manual ».
2. Le sous-système ajouté arrive avec sa propre allocation, vide, et son propre statut.
3. Retirer les deux sous-systèmes d'une exigence qui en a deux affiche « No sub-system yet » et la passe « Incomplete ».
4. Retirer un sous-système qui porte une réponse enregistrée demande d'abord une confirmation annonçant la suppression définitive de ce travail ; refuser ne change rien.
5. Seul un tender manager ajoute ou retire directement un sous-système, depuis le détail, la cellule Sub-system ou l'action groupée ; la même action est refusée à un contributeur, y compris par le serveur.
6. Chaque ajout ou retrait s'inscrit au journal de l'exigence ([US-ALM-35](#us-alm-35--inscrire-les-actions-dallocation-au-journal-de-lexigence)).
Écart maquette : la cellule Sub-system et « Assign › Sub-system » ne vérifient pas que l'utilisateur est tender manager, et retirer un sous-système depuis la cellule ne supprime pas son allocation (seul le ✕ du détail le fait).
Point ouvert : faut-il dériver automatiquement l'allocation d'un sous-système à modèle ajouté à la main ? Non dit ; la maquette l'ajoute vide (une relance peut la dériver, [US-ALM-21](#us-alm-21--relancer-le-modèle-dallocation-sur-une-exigence)).

### US-ALM-09 — Attribuer une exigence à un partenaire externe
**Carte :** En tant que tender manager d'un tender Turnkey, je veux attribuer une exigence à une entreprise partenaire ajoutée au tender, afin que la part du périmètre qu'elle tient soit suivie comme un sous-système.
**Conversation :** Un partenaire est un sous-système de la liste Turnkey, ajouté par le tender manager dans les paramètres (US-CFG), jamais prédit par le modèle. Il apparaît partout où la liste sert, dans sa couleur propre, avec une infobulle qui dit qu'il a été ajouté pour ce tender. Il n'a pas de seconde passe — ni ABS, PBS, OBS, ni équipe, ni personne : sa branche est allouée dès l'attribution et le tender manager en répond (« TM · for partner »). L'envoi au partenaire passe par l'export filtré, et son verdict se saisit dans Compliance (US-CMP).
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Activity / Requirement Tag variante `.partner`, liste Sub-system et « + Add sub-system » (groupe « Added for this tender — not in the model »), détail partenaire (`.partner-box`) ; Turnkey OBS List Setting dans Configuration (`dashboard-et-config.html`, route `#config`).
**Règles :** DEC-082, DEC-093, ALLOC-021, ALLOC-023, ALLOC-T29, DEC-126  ·  **Périmètre :** Pilote 1 (à confirmer)  ·  **Variantes :** Turnkey
**Critères d'acceptation :**
1. Un partenaire ajouté dans les paramètres apparaît dans sa couleur propre dans la cellule Sub-system, la liste Sub-system du détail, le filtre Sub-system et « + Add sub-system », où il est listé à part sous « Added for this tender — not in the model ».
2. Son infobulle dit qu'il est ajouté pour ce tender, hors du modèle Turnkey, jamais prédit par l'IA et qu'il travaille hors de l'outil ; il ne porte jamais de certitude en %.
3. Attribuer une exigence à un partenaire rend sa branche « Allocated » aussitôt, sans ABS, PBS, organisation ni personne, et sans relance possible.
4. La colonne « PIC » affiche « TM · for partner » pour cette branche, et son filtre propose cette valeur.
5. Le détail du partenaire explique qu'il n'y a rien à allouer et indique de filtrer la table sur son code puis d'exporter ce que montre le filtre.
6. Le nombre d'exigences attribuées au partenaire dans Allocation est celui que les paramètres annoncent pour refuser son retrait.

### US-ALM-10 — Proposer un sous-système manquant
**Carte :** En tant que contributeur d'un tender Turnkey, je veux signaler au tender manager qu'un sous-système manque sur une exigence, afin que le bon sous-système y travaille sans que je modifie l'aiguillage moi-même.
**Conversation :** Le contributeur ne change pas les sous-systèmes d'une exigence : il propose, avec une raison, et le tender manager approuve ou refuse. La proposition suit le mécanisme de réallocation de la maquette (DEC-011) : tant qu'elle attend, elle compte comme une demande en attente. Sur un tender SIG il n'y a pas d'axe sous-système, donc pas de proposition ([US-ALM-13](#us-alm-13--allouer-sur-un-tender-sig-autonome-sans-axe-sous-système)).
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Propose / Reassign Form (« Propose a change », « + Missing sub-system »), Activity / Requirement Tag variante `.proposed`, carte de proposition avec « ✓ Approve » / « ✕ Reject ».
**Règles :** DEC-076, DEC-011, DEC-104, ALLOC-020, ALLOC-013, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Turnkey
**Critères d'acceptation :**
1. « + Missing sub-system » propose seulement les sous-systèmes absents de l'exigence, avec le champ « Why do you think this sub-system is missing? ».
2. Envoyer sans raison est refusé avec « Add a short reason before submitting » ; rien n'est créé.
3. Une proposition envoyée apparaît comme sous-système proposé (étiquette distincte) dans la cellule Sub-system et le détail ; son auteur la voit « awaiting tender-manager review ».
4. Tant qu'elle attend, l'exigence compte dans « pending reassignment » et son niveau Turnkey affiche « Reassignment requested ».
5. Le tender manager voit l'auteur, le sous-système et la raison, avec « ✓ Approve » et « ✕ Reject » ; approuver ajoute le sous-système avec une allocation à faire, refuser le retire et rend l'exigence à son état antérieur.
6. La proposition et la décision s'inscrivent au journal de l'exigence.

### US-ALM-11 — Suivre une exigence répartie sur plusieurs sous-systèmes
**Carte :** En tant que tender manager d'un tender Turnkey, je veux voir une exigence aiguillée vers plusieurs sous-systèmes comme une seule exigence avec une branche par sous-système, afin de suivre chaque sous-système sans dupliquer l'exigence.
**Conversation :** Une exigence reste une seule exigence ; chaque sous-système auquel elle va est une branche avec son allocation, son statut et sa conformité, et les branches progressent indépendamment. Dans la table, la ligne se déplie en une sous-ligne par sous-système, puis par organisation quand un sous-système en a plusieurs (mécanique de dépliage : US-TAB). Dans le détail, « Sub-systems (N) » donne une carte par sous-système. Un cas incomplet n'arrête pas les autres.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Branch / Allocated-Activity Sub-row, Turnkey System Card (« Sub-systems (N) »), Block Badge (variante « branch count »).
**Règles :** ALLOC-004, ALLOC-009, ALLOC-T01, DEC-103, DEC-104, DOM-005, TYPE-T04, JRN-002, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Turnkey
**Critères d'acceptation :**
1. Une exigence aiguillée vers deux sous-systèmes reste une seule ligne, sous un seul identifiant, avec un badge du nombre de branches ; elle n'est jamais dupliquée.
2. Déplier la ligne montre une sous-ligne par sous-système avec son ABS, son PBS, son OBS, sa personne et sa conformité ; un sous-système à plusieurs organisations se déplie en une sous-ligne par organisation.
3. Chaque carte de « Sub-systems (N) » montre une ligne par organisation (organisation à gauche, personne à droite, manquants en gris : « No organisation yet », « Unassigned »), la conformité du sous-système et « Open sub-system detail → ».
4. Compléter, valider ou bloquer un sous-système ne change pas le statut des autres sous-systèmes de la même exigence.
5. La sous-ligne d'un sous-système sans modèle porte l'étiquette « no model ».
6. Pour le tender manager, les sous-lignes de sous-système n'affichent pas de statut d'allocation : la ligne porte le statut du niveau Turnkey.
Point ouvert : DEC-104 dit que le tender manager ne voit pas le statut des sous-systèmes sur la vue Turnkey, mais chaque carte de « Sub-systems (N) » l'affiche en coin — à préciser.

### US-ALM-12 — Travailler dans le détail d'un sous-système d'un Turnkey
**Carte :** En tant que tender manager d'un tender Turnkey, je veux ouvrir le détail d'un des sous-systèmes d'une exigence et y travailler comme sur un tender SIG, afin de corriger et valider ce sous-système sans toucher aux autres.
**Conversation :** Le détail d'un sous-système est le même panneau que sur SIG — type, classe, le modèle du sous-système (ABS / PBS / OBS modifiables, relance), la personne de chaque organisation, la validation — plus les boutons de réallocation. Les modifications ne portent que sur le sous-système ouvert. Un même cas SIG suit les mêmes règles dans un Turnkey et dans un tender SIG autonome ; seule la gestion globale du tender diffère. Un partenaire ouvre un détail explicatif ([US-ALM-09](#us-alm-09--attribuer-une-exigence-à-un-partenaire-externe)).
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Detail / Assignment Panel (« Open sub-system detail → », « ← All sub-systems »), Derivation Chain, Allocated-Activity Detail Card, Validate Zone, Propose / Reassign Form.
**Règles :** DEC-101, DEC-005, ALLOC-024, ALLOC-T31, TYPE-T03, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Turnkey
**Critères d'acceptation :**
1. « Open sub-system detail → » ouvre le détail du sous-système ; « ← All sub-systems » revient à la vue d'ensemble sans perdre l'exigence sélectionnée.
2. Le détail montre, dans l'ordre : Type, Class, le modèle du sous-système (ABS, PBS, liste OBS, « ↻ Re-run ▾ »), « Allocations (N) », la validation du sous-système, puis « Propose a change ».
3. Modifier le PBS dans le détail d'un sous-système ne change que ce sous-système ; les autres sous-systèmes de l'exigence gardent le leur.
4. La validation de ce détail ne valide que ce sous-système ([US-ALM-28](#us-alm-28--valider-lallocation-dun-sous-système-dun-turnkey)).
5. Une exigence d'un sous-système SIG reçoit dans un Turnkey les mêmes champs, contrôles et règles d'allocation que dans un tender SIG autonome.
Point ouvert : DEC-101 met les boutons de réallocation dans ce détail, y compris pour le tender manager, qui peut déjà ajouter ou retirer un sous-système lui-même : l'usage d'une demande qu'il s'adresserait n'est pas précisé.

### US-ALM-13 — Allouer sur un tender SIG autonome, sans axe sous-système
**Carte :** En tant que tender manager d'un tender SIG, je veux un écran d'allocation sans aucune notion de sous-système ni d'aiguillage, afin de travailler directement la chaîne ABS → PBS → OBS de SIG.
**Conversation :** Un tender SIG autonome n'est pas un Turnkey filtré : il est émis sur SIG, chaque exigence est SIG et n'a qu'une dérivation. Tout ce qui relève de l'aiguillage Turnkey est absent, pas simplement vide, et le détail s'ouvre directement sur la configuration SIG. Un tender Mainline est un tender SIG de produit Mainline (clés : [US-ALM-16](#us-alm-16--choisir-abs-pbs-et-rôle-dans-les-listes-des-clés)). Les particularités des tenders RSC ne sont pas fournies.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`) sur un tender SIG : Requirement Table sans colonne Sub-system, Detail / Assignment Panel (modèle « SIG's model »).
**Règles :** DEC-006, DEC-044, DEC-005, DEC-075, ALLOC-001, ALLOC-006, ALLOC-T08, TYPE-T01, TYPE-T02, TYPE-T08, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** SIG (Mainline compris)
**Critères d'acceptation :**
1. La table n'a pas de colonne Sub-system, le menu View ne la propose pas, et ni les filtres ni le regroupement n'offrent de champ Sub-system.
2. Le détail d'une exigence s'ouvre directement sur Type, Class, le modèle SIG (ABS, PBS, OBS), « Allocations (N) » et la validation, sans panneau Turnkey intermédiaire ni champ Sub-system.
3. Aucune certitude de routage, mention « has a model », « + Add sub-system », « + Missing sub-system » ni bouton « Validate & send to the sub-systems » n'apparaît.
4. Aucune exigence ne porte plus d'un sous-système ; un bloc reclassé en Requirement reçoit SIG.
5. La validation est « ✓ Validate & send to Compliance », une par exigence ([US-ALM-26](#us-alm-26--valider-une-exigence-en-un-seul-geste)).
Point ouvert : configuration et écrans propres aux tenders RSC (et à Mainline au-delà des clés) non fournis — ne pas les déduire de SIG (OPEN-15).

### US-ALM-14 — Corriger la chaîne ABS → PBS → OBS
**Carte :** En tant que tender manager ou contributeur du sous-système, je veux corriger l'ABS, le PBS et l'OBS d'une exigence dans leur ordre de dérivation, afin que chaque étape reste cohérente avec celle dont elle découle.
**Conversation :** La chaîne se lit et se dérive ABS, puis PBS, puis OBS ; la personne vient après, séparément ([US-ALM-18](#us-alm-18--désigner-la-personne-de-chaque-organisation)). L'ABS et le PBS sont uniques pour l'exigence dans son sous-système ; seule l'OBS peut compter plusieurs organisations ([US-ALM-15](#us-alm-15--gérer-les-organisations-obs-dun-sous-système)). Corriger une étape efface ce qui en découle, et l'écran le dit. Chaque étape proposée par l'IA porte sa propre certitude en % ; hors tender à clés, ABS et PBS se saisissent en texte (sur clés : [US-ALM-16](#us-alm-16--choisir-abs-pbs-et-rôle-dans-les-listes-des-clés)).
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Derivation Chain (Derivation Step) du Detail / Assignment Panel, colonnes ABS et PBS, sous-lignes de sous-système.
**Règles :** DEC-008, DEC-055, ALLOC-003, ALLOC-006, ALLOC-T02, TYPE-T09, KEY-T03, JRN-002, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes (Turnkey : dans le détail de chaque sous-système)
**Critères d'acceptation :**
1. Le détail et la table présentent toujours ABS, puis PBS, puis OBS, dans cet ordre, sur tout tender.
2. Changer l'ABS efface le PBS et l'OBS de ce sous-système, avec le message « ABS changed — PBS and OBS cleared, they were derived from it ».
3. Changer le PBS efface l'OBS ; changer l'OBS ne touche ni l'ABS ni le PBS.
4. Chaque étape proposée par l'IA affiche sa certitude en %, en couleur IA sous 75 % (y compris sur les sous-lignes de la table) ; une valeur saisie par une personne n'en a pas.
5. Une exigence a un seul ABS et un seul PBS par sous-système, quel que soit son nombre d'organisations ; aucune organisation ne porte son propre ABS ou PBS.
6. Hors tender à clés, l'ABS se saisit en texte dans la table et le détail, le PBS en texte dans le détail ; la colonne PBS de la table est alors en lecture seule.
Écart maquette : la maquette n'exige qu'une organisation (OBS) pour sortir d'« Incomplete » (retirer la dernière l'y renvoie, DEC-076) ; un ABS ou un PBS manquant n'y retient pas l'exigence.
Point ouvert : faut-il aussi un ABS et un PBS pour sortir d'« Incomplete » ? ALLOC-T32 le suggère sans le dire. Effet d'une correction de la chaîne sur une exigence déjà « Allocated » : la maquette la laisse « Allocated » ; ALLOC-003 renvoie à LIFE-008 sans dire si le statut change.

### US-ALM-15 — Gérer les organisations (OBS) d'un sous-système
**Carte :** En tant que tender manager ou contributeur du sous-système, je veux ajouter ou retirer les organisations qui traitent une exigence, afin que chaque équipe concernée ait son allocation.
**Conversation :** Une OBS est une organisation — une équipe ou un service du sous-système (colonne « OBS · team »), un poste sur un tender Mainline à clés (« OBS · role ») — jamais une personne. Un sous-système peut compter plusieurs organisations : chacune répond pour elle-même et les verdicts se consolident (le plus restrictif l'emporte). Toutes se retirent, la dernière comprise, et l'exigence redevient alors « Incomplete ». La personne de chaque organisation se désigne ensuite ([US-ALM-18](#us-alm-18--désigner-la-personne-de-chaque-organisation)).
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), OBS List (« + Add organisation », ✕ sur chaque ligne, recherche `.obs-pick`).
**Règles :** DEC-054, DEC-055, DEC-076, DEC-034, ALLOC-020, ALLOC-T21, ALLOC-T28, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. « + Add organisation » ouvre une recherche ; un clic ou Entrée ajoute l'organisation choisie, Échap annule.
2. Chaque organisation a son ✕, la dernière comprise ; retirer la dernière vide l'allocation du sous-système (organisation et personne), affiche « No organisation yet » et passe l'exigence « Incomplete ».
3. Sur une exigence SIG à une seule organisation, le ✕ est présent et la retire.
4. Retirer une organisation qui porte une réponse enregistrée demande une confirmation annonçant la suppression définitive de ce travail.
5. Retirer des organisations jusqu'à n'en garder qu'une fait afficher, dans la colonne « PIC » de la table, la personne de celle qui reste.
6. Une entrée sans organisation s'affiche « — No organisation derived yet — », jamais avec le nom d'une personne ; avec plusieurs organisations, une mention rappelle que chacune a son verdict à consolider.
Point ouvert : liste proposée hors clés — DEC-036 fait des OBS · team et des périmètres du casting une même liste fermée, alors que la maquette propose les organisations déjà utilisées et un nom libre (« Add “…” »). DEC-087 (plusieurs personnes d'un même périmètre = plusieurs entrées OBS) face à une maquette qui refuse la même organisation deux fois sur un sous-système : traduction exacte à préciser.

### US-ALM-16 — Choisir ABS, PBS et rôle dans les listes des clés
**Carte :** En tant que tender manager ou contributeur SIG d'un tender Mainline, je veux choisir l'ABS, le PBS et le rôle dans les listes du produit, afin qu'aucune dérivation ne repose sur une valeur inventée.
**Conversation :** Sur un tender SIG de produit Mainline (Wayside ou Onboard), les trois axes viennent du classeur de clés ([US-ALM-17](#us-alm-17--alimenter-les-listes-depuis-le-classeur-de-clés-de-référence)). L'OBS y est un poste, rangé sous une catégorie ABS : choisir l'ABS met en tête les rôles qui en dépendent. Le PBS est un élément du produit, groupé par famille. Un tender Turnkey ou SIG Urban n'a aucune liste de clés et garde la saisie libre.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`) sur un tender Mainline : listes ABS / PBS de la Derivation Chain et de la table, OBS List variante « keyed » (« + Add role »), en-tête « OBS · role ».
**Règles :** DEC-061, DEC-062, ALLOC-017, KEY-T02, KEY-T03, KEY-T05, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Mainline (Wayside, Onboard)
**Critères d'acceptation :**
1. L'ABS se choisit dans la liste des catégories du produit et le PBS dans ses éléments groupés par famille, dans le détail comme dans la table ; aucun champ n'accepte une valeur hors liste.
2. La colonne et l'étape OBS s'intitulent « OBS · role » ; « + Add role » cherche sur l'intitulé du poste et ses codes (« Search a role, or a code… »).
3. Les rôles rangés sous l'ABS de l'exigence sont proposés en premier (« Under <ABS> »), les autres ensuite (« Other roles on this product »).
4. Changer l'ABS efface le PBS et les rôles de ce sous-système.
5. Une valeur produite par le modèle d'un autre produit et absente de la liste reste affichée, sous « From another product's model ».
6. Sur un tender Turnkey ou SIG Urban, aucun sélecteur de clé n'apparaît et le comportement est inchangé.

### US-ALM-17 — Alimenter les listes depuis le classeur de clés de référence
**Carte :** En tant que tender manager d'un tender Mainline, je veux que les listes ABS, PBS et OBS soient exactement celles du classeur de référence pour mon produit, afin que deux tenders du même produit allouent sur le même vocabulaire.
**Conversation :** Le classeur « PBS / OBS / ABS Keys » (v260720) porte les trois axes, chacun coché par produit (Urban, Mainline Wayside, Mainline Onboard) : le modèle d'un produit est ce qui est coché pour lui. Mainline Wayside et Mainline Onboard sont deux produits SIG distincts. Le fichier est chargé tel quel, anomalies comprises : leur correction appartient au fichier. Le PBS y est un élément produit, pas une catégorie d'exigence.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), listes de la Derivation Chain ; le chargement du classeur n'est pas maquetté (fait à la construction du prototype).
**Règles :** DEC-061, DEC-062, DEC-047, KEY-T01, KEY-T04, TYPE-T11, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Mainline (Wayside, Onboard)
**Critères d'acceptation :**
1. Les listes d'un tender Mainline Wayside sont exactement les entrées cochées Mainline Wayside du classeur (de même pour Onboard) ; aucune valeur n'est saisie ailleurs que dans le classeur.
2. Remplacer le classeur par une nouvelle version met à jour les listes sans rien ressaisir.
3. Toutes les dérivations d'un tender Mainline, proposées par l'IA ou par une relance avec le modèle du tender, prennent leurs valeurs dans ces listes ; aucune valeur inventée ne subsiste.
4. La colonne PBS montre un élément produit (famille › sous-ensemble › élément), jamais Functional, Performance ni une autre catégorie d'exigence.
5. Les anomalies du fichier (doublons, lignes sans identifiant, casse mélangée) sont chargées telles quelles, sans correction par l'outil.
Point ouvert : qui charge ou remplace le classeur, et ce que deviennent les dérivations existantes quand une valeur disparaît d'une nouvelle version (rôle Admin non détaillé, OPEN-02) ; modèles Urban et RSC sans clés réelles.

### US-ALM-18 — Désigner la personne de chaque organisation
**Carte :** En tant que tender manager ou contributeur du sous-système, je veux désigner pour chaque organisation la personne qui en répond, choisie parmi les membres du sous-système, afin que chaque allocation ait un responsable de sa conformité.
**Conversation :** Une allocation est une organisation et la personne qui en répond : une exigence qui atteint trois organisations, ce sont trois allocations. Cette personne est responsable de la conformité de son organisation — elle répond et c'est elle qu'on relance ; il n'y a pas de responsable global de l'exigence. Une personne appartient à un seul sous-système (US-TEAM) et n'est proposée que là ; un manager de sous-système, s'il existe, n'a pas de droit de plus. La personne se désigne à un seul endroit, l'allocation, que la cellule « PIC » de la table reflète.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Allocated-Activity Detail Card (« Allocations (N) », « PIC »), colonne « PIC » du Requirement Row, « Assign » de la Bulk Selection Action Bar.
**Règles :** DEC-060, DEC-087, DEC-102, DEC-123, DEC-124, ALLOC-011, ALLOC-016, ALLOC-025, ALLOC-T05, ALLOC-T18, ALLOC-T19, ALLOC-T20, ALLOC-T32, DOM-004, DOM-006, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. « Allocations (N) » compte les organisations de l'exigence, pas ses sous-systèmes ; chaque carte porte l'organisation (avec l'étiquette du sous-système seulement sur un Turnkey ou une exigence multi-sous-systèmes), son avancement et un seul champ « PIC ».
2. La liste « PIC » ne propose que les membres du sous-système de l'organisation, plus la personne déjà en place ; un membre d'un autre sous-système n'y figure jamais.
3. Sur une exigence à une organisation dans un sous-système, la personne choisie est la même partout où l'exigence l'affiche, table comprise, et la cellule de la table modifie ce même champ.
4. Avec plusieurs organisations, la cellule « PIC » résume (prénoms, « n/m assigned » ou « Unassigned ») sans liste de choix ; une exigence multi-sous-systèmes n'est jamais « Unassigned » si une de ses organisations a une personne.
5. Aucun champ « responsable » n'existe au niveau de l'exigence, et aucun écran n'offre deux endroits pour désigner la personne d'une même organisation.
6. « Assign » (action groupée) écrit la personne sur les organisations de son propre sous-système dans chaque exigence choisie — remplace une entrée unique, ne remplit que les entrées vides s'il y en a plusieurs — et dit combien d'exigences sont laissées telles quelles.
Point ouvert : une exigence sans sous-système n'a pas d'organisation ; la maquette y garde une recherche dans l'annuaire au niveau de l'exigence, que DEC-087 et DEC-102 ne prévoient pas.

### US-ALM-19 — Valider sans avoir désigné de personne
**Carte :** En tant que tender manager, je veux pouvoir valider une allocation dont une organisation n'a encore personne, afin que le manque de staffing ne bloque pas le travail.
**Conversation :** L'absence de personne est permise, y compris après validation : elle reste visible, mais ne rend pas l'exigence « Incomplete » et ne désactive jamais la validation. Les contributeurs du sous-système gardent leurs droits et peuvent répondre. Une personne peut être désignée ensuite et devient responsable de sa conformité. Isoler ces exigences passe par le filtre de champ vide de « PIC » (US-TAB).
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), note sous le bouton de la Validate Zone, colonne « PIC », Role Recap Row (« To assign — k of m ») de l'onglet Activity.
**Règles :** DEC-025, DEC-087, ALLOC-010, ALLOC-T06, ACC-T10, DOM-004, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Une exigence complète dont aucune organisation n'a de personne est « To validate » et son bouton de validation est actif.
2. Sous le bouton, une note informe : « No one assigned yet — you can still validate; the sub-system's contributors can answer. », ou « k of m organisations with no one assigned — you can still validate » si seules certaines manquent.
3. Après validation, l'exigence est « Allocated » et la table affiche toujours « Unassigned » ou « n/m assigned ».
4. Le filtre de champ vide de « PIC » isole les exigences dont au moins une organisation n'a personne.
5. Désigner une personne après validation laisse l'exigence « Allocated » et s'inscrit au journal.
6. L'onglet Activity affiche « To assign — k of m organisations » tant qu'une entrée est vide.

### US-ALM-20 — Allouer à la main un sous-système sans modèle
**Carte :** En tant que contributeur d'un sous-système sans modèle d'allocation, je veux remplir moi-même l'ABS, le PBS et l'OBS des exigences de mon sous-système, afin de les faire avancer sans attendre de modèle.
**Conversation :** Un sous-système sans modèle n'est pas dérivé : ABS, PBS, OBS et personne arrivent vides, donc « Incomplete », jusqu'à ce que ses contributeurs les remplissent (puis « To validate », puis « Allocated »). C'est un mode de travail normal, pas un défaut : il n'y a pas de statut « Awaiting manual allocation ». L'outil n'applique jamais en silence le modèle d'un autre sous-système ; l'emprunt est un geste délibéré ([US-ALM-22](#us-alm-22--emprunter-le-modèle-dun-autre-sous-système)). Les sous-systèmes et exigences qui ont un modèle avancent sans attendre.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), vue contributeur (Derivation Chain, champs « Fill in by hand »), Branch / Allocated-Activity Sub-row (étiquette « no model »).
**Règles :** DEC-103, DEC-043, ALLOC-005, ALLOC-009, ALLOC-025, ALLOC-T03, ALLOC-T32, AI-010, TYPE-T05, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Turnkey (sous-systèmes sans modèle) ; RSC selon sa configuration
**Critères d'acceptation :**
1. Une exigence aiguillée vers un sous-système sans modèle arrive avec ABS, PBS et OBS vides pour ce sous-système, au statut « Incomplete », sans autre statut ni étiquette d'attente.
2. La sous-ligne de ce sous-système porte « no model », avec une infobulle qui dit qu'on y alloue à la main.
3. Le contributeur saisit l'ABS et le PBS et ajoute ses organisations ; une fois remplis, le sous-système passe « To validate », même sans personne désignée.
4. Le contributeur valide son sous-système, qui passe « Allocated ».
5. Aucun modèle d'un autre sous-système n'est appliqué automatiquement ; le sous-système reste sans modèle pour les exigences suivantes.
6. Les autres sous-systèmes de la même exigence et les autres exigences avancent sans attendre ; Status « Incomplete » et le code du sous-système suffisent à isoler ce travail (US-TAB).
Point ouvert : quels sous-systèmes ont un modèle — SIG et RSC selon une déduction à confirmer (DEC-058) ; RST est marqué « avec modèle » dans la maquette par hypothèse (DEC-059).

### US-ALM-21 — Relancer le modèle d'allocation sur une exigence
**Carte :** En tant que tender manager ou contributeur du sous-système, je veux rejouer un modèle d'allocation sur une exigence déjà dérivée en choisissant lequel, afin de recalculer une dérivation que je juge fausse.
**Conversation :** La relance recalcule ce que le modèle dérive ; elle ne change pas qui répond, ce qui relève de la réallocation ([US-ALM-29](#us-alm-29--demander-une-réallocation)). Elle porte sur l'exigence entière dans son sous-système — ABS, PBS et toutes ses organisations, rien d'autre, jamais les personnes — et s'applique directement, sans aperçu, ce qui n'est sûr que parce qu'elle est interdite dès qu'une réponse existe ([US-ALM-23](#us-alm-23--comprendre-pourquoi-une-relance-est-bloquée)). Le choix montre d'abord les modèles du sous-système (pour SIG : Urban, Mainline Wayside, Mainline Onboard), puis à part l'emprunt ([US-ALM-22](#us-alm-22--emprunter-le-modèle-dun-autre-sous-système)). La relance globale au changement de modèle est un autre geste, destructeur, dans les paramètres (US-CFG).
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Re-run Control (« ↻ Re-run ▾ », « This sub-system's models ») en tête du bloc de modèle, de la vue contributeur et du détail de sous-système ; Toast.
**Règles :** DEC-040, DEC-042, DEC-047, DEC-049, DEC-053, DEC-054, DEC-056, DEC-091, ALLOC-014, ALLOC-023, ALLOC-T09, ALLOC-T11, ALLOC-T14, ALLOC-T15, ALLOC-T23, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes (Turnkey : par sous-système)
**Critères d'acceptation :**
1. « ↻ Re-run ▾ » est visible sans navigation supplémentaire en tête du bloc de modèle (tender manager, tender à un sous-système) et en tête de la vue du contributeur ; son menu liste d'abord « This sub-system's models », le produit du tender en premier.
2. Choisir un modèle réécrit aussitôt l'ABS, le PBS et toutes les organisations du sous-système, avec leurs nouvelles certitudes ; les personnes, les autres sous-systèmes et les autres exigences ne changent pas.
3. Si le résultat diffère, le message « <ID> — re-derived with <modèle> » s'affiche ; s'il est identique, rien ne s'affiche et seul le journal note « same result ».
4. Relancer avec l'autre produit du sous-système ne change pas le produit du tender, et rien n'indique ensuite qu'il aurait changé.
5. Une relance ne fait jamais passer une exigence à « Allocated ».
6. Seuls le tender manager et les contributeurs du sous-système voient le contrôle ; il est absent de la lecture seule ([US-ALM-32](#us-alm-32--lire-en-lecture-seule-une-exigence-dun-autre-sous-système)) et le serveur refuse la relance à tout autre.
Point ouvert : emplacement du contrôle pour le tender manager sur un Turnkey — ALLOC-014 et ALLOC-T23 le veulent sur chaque carte sous-système, la maquette ne l'a que dans le détail du sous-système (retiré des cartes le 23 sept. à la demande de l'utilisateur) : à arbitrer. Statut après une relance (recalcul selon les nouvelles certitudes, retour d'une exigence « Allocated ») : la maquette ne touche pas au statut. Un modèle peut-il ajouter ou retirer une organisation à la relance : non tranché (la maquette garde leur nombre).

### US-ALM-22 — Emprunter le modèle d'un autre sous-système
**Carte :** En tant que contributeur d'un sous-système sans modèle, je veux relancer une exigence avec le modèle d'un autre sous-système, désigné explicitement, afin d'obtenir une dérivation de départ plutôt que de tout saisir.
**Conversation :** L'emprunt est l'exception : il se choisit dans une section distincte du menu, pour qu'emprunter ne soit jamais aussi banal que choisir un produit du sous-système. Il vaut pour cette relance seulement : le sous-système reste sans modèle et l'allocation manuelle reste son fonctionnement par défaut. Il ne laisse aucune trace sur l'exigence, dans les filtres ni à l'export ; seul le journal la garde. Mêmes règles que toute relance, blocage compris ; le tender manager peut aussi emprunter.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Re-run Control (section « Borrow another sub-system's model »).
**Règles :** DEC-043, DEC-047, ALLOC-005, ALLOC-014, ALLOC-T12, ALLOC-T13, ALLOC-T14, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes (cas principal : sous-systèmes sans modèle d'un Turnkey)
**Critères d'acceptation :**
1. Le menu de relance sépare les modèles du sous-système (« This sub-system's models ») de ceux des autres sous-systèmes (« Borrow another sub-system's model »), sous deux titres distincts.
2. Sur un sous-système sans modèle, seule la section d'emprunt est proposée.
3. Une relance empruntée dérive ABS, PBS et organisations comme une relance ordinaire ; le sous-système reste ensuite sans modèle et ses exigences suivantes restent en allocation manuelle.
4. Après un emprunt, rien sur l'exigence, dans la table, les filtres ni l'export n'indique le modèle emprunté.
5. Le journal de l'exigence garde qui, quand et quel modèle a été emprunté (« … (borrowed — this sub-system has no model of its own) »).
6. Un emprunt sur une exigence bloquée (réponse ou verdict enregistré) est refusé comme toute relance.

### US-ALM-23 — Comprendre pourquoi une relance est bloquée
**Carte :** En tant que tender manager ou contributeur du sous-système, je veux voir que la relance est impossible et pourquoi, afin de ne pas croire à une fonction manquante et de ne jamais écraser un travail déjà répondu.
**Conversation :** Une relance s'applique sans aperçu ; ce qui la rend sûre, c'est qu'elle est interdite dès qu'une réponse ou un verdict est enregistré sur l'une quelconque des organisations de l'exigence. Une question en attente du client ne bloque pas : rien n'est encore répondu. Le contrôle reste visible et inactif, avec le motif — jamais masqué. Les réponses n'existant qu'avec Compliance, ce blocage n'a d'objet qu'après le premier pilote ; la relance globale des paramètres, elle, écrase tout (US-CFG).
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Re-run Control (variante « blocked »), Re-run Prompt (variante « blocked »).
**Règles :** DEC-041, DEC-051, DEC-056, DEC-089, DEC-050, ALLOC-014, ALLOC-T10, DEC-126  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Dès qu'une organisation de l'exigence a une réponse enregistrée, « ↻ Re-run » est grisé avec « Cannot re-run — an answer has been recorded. ».
2. Un verdict enregistré bloque de même, avec « Cannot re-run — a verdict has been recorded. ».
3. Une seule organisation bloquée bloque la relance de toute l'exigence dans ce sous-système.
4. Une affectation proposée, en attente de réponse du contributeur, en attente du client (« Awaiting Q&A ») ou en réallocation demandée ne bloque pas.
5. Une relance bloquée tentée par un autre chemin (action groupée, requête directe) est refusée avec le même motif, sans rien modifier.
6. La ligne de proposition qui suit un changement de type ou de classe dit « re-run blocked » à la place du bouton.

### US-ALM-24 — Relancer le modèle sur une sélection d'exigences
**Carte :** En tant que tender manager, je veux relancer un modèle sur plusieurs exigences sélectionnées, afin de corriger d'un coup une série d'exigences mal dérivées sans changer le modèle de tout le tender.
**Conversation :** La relance en masse est la même relance, appliquée à une sélection depuis la barre d'actions groupées (sélection : US-TAB). Les règles s'appliquent exigence par exigence : celles qui sont bloquées sont sautées et comptées, jamais relancées de force. Titres et blocs d'information n'ont rien à dériver et sont comptés à part ; seules les exigences dont la dérivation a changé comptent comme relancées. C'est le recours pour une série d'erreurs, distinct de la relance globale des paramètres (US-CFG).
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), « Re-run ▾ » de la Bulk Selection Action Bar, Toast.
**Règles :** DEC-052, DEC-091, DEC-056, ALLOC-014, ALLOC-T22, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. « Re-run ▾ » de la barre d'actions groupées propose les modèles ; en choisir un relance chaque exigence sélectionnée selon les règles de la relance unitaire.
2. Les exigences bloquées sont laissées telles quelles et comptées (« N left alone — already answered »).
3. Aucun titre ni bloc d'information ne reçoit d'ABS, de PBS ou d'OBS ; ils sont comptés à part (« N not requirements — nothing to derive »).
4. Le message ne compte comme relancées que les exigences dont la dérivation a changé ; les résultats identiques n'y figurent pas, mais le journal de chacune note « same result ».
5. Un contributeur ne relance que les exigences de son sous-système ; les autres sont retirées de la sélection et comptées (« … not on your sub-system — left as is »).
Point ouvert : exigence à plusieurs sous-systèmes dans une relance groupée — la maquette les écarte et les compte (« re-run those from the panel »), aucune décision ne le dit.

### US-ALM-25 — Relancer après un changement de type ou de classe
**Carte :** En tant que tender manager ou contributeur du sous-système, je veux qu'on me propose de relancer le modèle quand le type ou la classe d'une exigence a changé, afin que la dérivation affichée corresponde à la caractérisation actuelle.
**Conversation :** La dérivation ABS / PBS / OBS a été faite pour la caractérisation d'alors : si un bloc devient une exigence ou si la classe change, une ligne colorée « ↻ Re-run the model » apparaît au-dessus de l'ABS, avec la raison. Rien n'est relancé tout seul. La ligne disparaît quand la caractérisation revient à celle de la dérivation, ou après une relance par n'importe quelle voie. Si la relance est bloquée ou impossible, la même ligne le dit, en neutre.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Re-run Prompt (variantes « action », « blocked », « no model ») dans la Derivation Chain.
**Règles :** DEC-075, DEC-089, ALLOC-019, ALLOC-T27, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Basculer la classe d'une exigence non répondue affiche « ↻ Re-run the model » avec « class changed » au-dessus de l'ABS ; reclasser un bloc en Requirement l'affiche avec « type changed ».
2. Aucun modèle n'est relancé tant que personne ne clique.
3. Cliquer relance le modèle du sous-système (le produit du tender présélectionné) : ABS, PBS et OBS sont re-dérivés et la ligne disparaît.
4. Revenir à la classe d'origine, ou relancer par « ↻ Re-run ▾ » ou l'action groupée, fait aussi disparaître la ligne.
5. Sur une exigence dont une organisation a une réponse enregistrée, la ligne dit « … · re-run blocked », sans bouton.
6. Sur un sous-système sans modèle, la ligne dit « … · check ABS / PBS / OBS by hand », sans bouton.

### US-ALM-26 — Valider une exigence en un seul geste
**Carte :** En tant que tender manager, je veux valider en une fois la caractérisation et l'allocation d'une exigence, afin de l'envoyer vers Compliance sans étape intermédiaire.
**Conversation :** Une seule validation par exigence confirme le type, la classe, l'allocation et ce que l'IA avait détecté ; elle rend les allocations disponibles pour Compliance, dont la construction n'est pas exigée au premier pilote. Le bouton est toujours dans le panneau, juste après les données qu'il confirme, et grisé avec sa raison quand la validation est impossible ; il n'y a plus de « Finalize allocation ». Le tender manager valide toute exigence, un contributeur celles de son sous-système ([US-ALM-31](#us-alm-31--travailler-sur-son-sous-système-vue-du-contributeur)) : ALLOC-012, qui réserve encore la validation à l'équipe de gestion, cède devant DEC-104. Sur un Turnkey, la validation a deux niveaux ([US-ALM-27](#us-alm-27--valider-laiguillage-dune-exigence-turnkey), [US-ALM-28](#us-alm-28--valider-lallocation-dun-sous-système-dun-turnkey)) ; ALLOC-T30 décrit encore deux gestes, caducs depuis DEC-099.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Validate Zone (« ✓ Validate & send to Compliance »), Status Pill (clic), « Validate » de la Bulk Selection Action Bar, Toast.
**Règles :** DEC-099, DEC-084, DEC-009, DEC-104, DEC-067, ALLOC-007, ALLOC-008, ALLOC-012, ALLOC-022, ALLOC-024, ALLOC-T04, ALLOC-T30, ALLOC-T31, DOM-007, JRN-002, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** SIG (Mainline compris), RSC ; Turnkey : [US-ALM-27](#us-alm-27--valider-laiguillage-dune-exigence-turnkey) et [US-ALM-28](#us-alm-28--valider-lallocation-dun-sous-système-dun-turnkey)
**Critères d'acceptation :**
1. Sur une exigence « To review » ou « To validate », « ✓ Validate & send to Compliance » la passe « Allocated » en un geste ; le bouton devient « ✓ Allocated — sent to Compliance » et le message dit « <ID> allocated — sent to Compliance ».
2. La validation retire les niveaux de confiance et les marques IA du type, de la classe et du sous-système ; aucun bouton « Confirm » séparé n'existe.
3. Une exigence « Incomplete » garde le bouton visible mais grisé, avec sa raison : « Characterisation incomplete — set its type and class first. » ou « Allocation incomplete — complete ABS / PBS / OBS first. ».
4. Cliquer la pastille d'une exigence « To review » ou « To validate », ou appuyer sur V (US-TAB), produit la même validation ; l'action groupée ne valide que les exigences prêtes et dit combien ne l'étaient pas.
5. La validation s'annule depuis le message ou par ⌘/Ctrl+Z (US-TAB) et rend l'exigence à son état antérieur.
6. Aucun bouton, fenêtre, lien ni réglage « Finalize allocation » n'existe, et une colonne personnalisée vide n'empêche jamais la validation.

### US-ALM-27 — Valider l'aiguillage d'une exigence Turnkey
**Carte :** En tant que tender manager d'un tender Turnkey, je veux valider en un geste le type, la classe et les sous-systèmes vers lesquels une exigence est aiguillée, afin de l'envoyer aux sous-systèmes qui la traiteront.
**Conversation :** Sur un Turnkey, la validation a deux niveaux : le tender manager valide l'aiguillage (niveau Turnkey), puis chaque sous-système est validé à part ([US-ALM-28](#us-alm-28--valider-lallocation-dun-sous-système-dun-turnkey)). Une fois validé, l'aiguillage reste « Allocated », sauf pendant une demande de réallocation : le niveau Turnkey passe alors « Reassignment requested » et sa validation est bloquée jusqu'à la décision. Seul le tender manager valide l'aiguillage.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Validate Zone (variante « Turnkey routing », sous la liste Sub-system), Status Pill (« Reassignment requested »).
**Règles :** DEC-104, DEC-099, DEC-009, ALLOC-012, ALLOC-025, ALLOC-T32, ACC-014, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Turnkey
**Critères d'acceptation :**
1. Dans la vue Turnkey, « ✓ Validate & send to the sub-systems » passe le niveau Turnkey à « Allocated » et devient « ✓ Routing validated — sent to the sub-systems » ; le message dit « <ID> routing validated — sent to its sub-systems ».
2. Sans classe ou sans sous-système, le bouton est grisé avec sa raison.
3. Tant qu'une demande de réallocation attend sur un des sous-systèmes, le niveau Turnkey affiche « Reassignment requested » et le bouton est grisé avec « A sub-system asked for a reassignment — approve or reject it first. ».
4. Approuver ou refuser la demande rend au niveau Turnkey son statut antérieur, « Allocated » s'il avait été validé.
5. Valider l'aiguillage ne valide aucun sous-système.
6. Un contributeur ne voit pas ce bouton : sa pastille et sa touche V visent son seul sous-système.
Écart maquette : quand c'est le sous-système qui manque, la raison affichée parle encore de type et de classe (« Characterisation incomplete — set its type and class first. »).
Point ouvert : DEC-099 dit que valider un sous-système valide aussi la caractérisation, DEC-104 sépare les deux niveaux ; la maquette laisse valider un sous-système avant l'aiguillage sans valider la caractérisation — ordre et dépendance à confirmer.

### US-ALM-28 — Valider l'allocation d'un sous-système d'un Turnkey
**Carte :** En tant que contributeur d'un sous-système, je veux valider l'allocation de mon sous-système sur une exigence Turnkey, afin d'envoyer ses organisations vers Compliance sans attendre les autres sous-systèmes.
**Conversation :** Chaque sous-système d'une exigence porte son propre statut et se valide à part, par son contributeur ou par le tender manager. Le tender manager le fait depuis le détail du sous-système ([US-ALM-12](#us-alm-12--travailler-dans-le-détail-dun-sous-système-dun-turnkey)), le contributeur depuis sa vue ([US-ALM-31](#us-alm-31--travailler-sur-son-sous-système-vue-du-contributeur)) ou la pastille de la sous-ligne de son sous-système. Un sous-système à qui il manque des données est « Incomplete » et son bouton est grisé avec la raison. Les autres sous-systèmes avancent indépendamment.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Validate Zone (variantes « contributor's own system », « disabled with its reason »), pastille du Branch / Allocated-Activity Sub-row.
**Règles :** DEC-104, DEC-103, DEC-099, ALLOC-009, ALLOC-025, ALLOC-T30, ALLOC-T32, ACC-014, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Turnkey
**Critères d'acceptation :**
1. Dans le détail d'un sous-système ou la vue du contributeur, « ✓ Validate & send to Compliance » passe ce sous-système à « Allocated » et devient « ✓ Allocated — sent to Compliance ».
2. Un sous-système « Incomplete » garde le bouton grisé avec « Allocation incomplete — complete ABS / PBS / OBS first. ».
3. Valider un sous-système ne change ni le statut des autres sous-systèmes ni celui du niveau Turnkey.
4. Un contributeur ne valide que son sous-système ; le tender manager peut valider tout sous-système ; le serveur refuse le reste.
5. Un partenaire n'a rien à valider : sa branche est « Allocated » dès l'attribution ([US-ALM-09](#us-alm-09--attribuer-une-exigence-à-un-partenaire-externe)).
6. La validation d'un sous-système s'inscrit au journal et s'annule comme celle d'une exigence ([US-ALM-26](#us-alm-26--valider-une-exigence-en-un-seul-geste)).

### US-ALM-29 — Demander une réallocation
**Carte :** En tant que contributeur, je veux demander au tender manager de réallouer une exigence de mon sous-système, avec un motif et un remplaçant, afin que la bonne personne ou le bon sous-système la traite.
**Conversation :** Le mécanisme est celui de la maquette (DEC-011) : trois motifs, « Right sub-system, wrong person » (proposer une personne du même sous-système), « Wrong sub-system » et « This sub-system doesn't apply here » (proposer un sous-système de remplacement), et une justification obligatoire. La demande part au tender manager, qui seul tranche ([US-ALM-30](#us-alm-30--traiter-une-demande-de-réallocation)). Elle se fait depuis le détail dans Allocation ou depuis Compliance (« Not mine — return it », US-CMP), et c'est la même demande des deux côtés. Une demande remplace toujours : elle ne retire jamais un sous-système sans le remplacer.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Propose / Reassign Form (« ↩ Request reassignment », trois motifs), Block Badge (« ⚠ Blocked »), pastille « pending reassignment » de la Triage Bar.
**Règles :** DEC-011, DEC-102, DEC-104, ALLOC-013, ALLOC-T07, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes (motifs « sous-système » : Turnkey)
**Critères d'acceptation :**
1. « ↩ Request reassignment » ouvre les trois motifs ; « Right sub-system, wrong person » demande une personne de remplacement, les deux autres un sous-système de remplacement.
2. La personne de remplacement se choisit parmi les seuls membres du même sous-système.
3. Envoyer sans justification est refusé avec « Add a short reason before submitting » ; rien n'est créé.
4. Une demande envoyée passe ce sous-système en « Reassignment needed », affiche « ⚠ Blocked » sur la ligne, compte dans « pending reassignment » et, sur un Turnkey, met le niveau Turnkey en « Reassignment requested ».
5. Tant qu'une demande attend sur ce sous-système, le bouton est grisé (« Already flagged for reassignment ») et son auteur la voit « awaiting tender-manager review ».
6. Une demande faite depuis Compliance apparaît à l'identique dans Allocation, et inversement.
Écart maquette : la personne de remplacement est choisie parmi tous les contributeurs, pas seulement ceux du sous-système (DEC-102).
Point ouvert : sur un tender SIG autonome, « Wrong sub-system » et « This sub-system doesn't apply here » n'ont pas de sous-système de remplacement possible ; la maquette les propose — les cas hors sous-système en autonome restent à expliciter (ALLOCATION.md, OPEN-15).

### US-ALM-30 — Traiter une demande de réallocation
**Carte :** En tant que tender manager, je veux approuver ou refuser une demande de réallocation en voyant son motif et le remplaçant proposé, afin de corriger l'allocation sans perdre la trace de la décision.
**Conversation :** Le tender manager voit, dans le détail de l'exigence, qui demande, le motif, la justification et le remplaçant proposé. Approuver remplace : la personne sur les organisations que tenait le demandeur, ou le sous-système entier par celui proposé, dont l'allocation reste à faire ; refuser rend l'état antérieur. Les demandes en attente remontent aussi au tableau de bord (US-DASH), et les statistiques comptent les réallocations par motif (US-STAT).
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Allocated-Activity Detail Card (variante « with pending reassignment request »), Toast.
**Règles :** DEC-011, DEC-076, DEC-102, DEC-104, ALLOC-013, ALLOC-T07, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Le détail montre « ↩ Reassignment requested by <nom> », le motif, la justification, « Proposed: reassign to <personne> » ou « Proposed: replace with <sous-système> », puis « ✓ Approve » et « ✕ Reject ».
2. Approuver « Right sub-system, wrong person » met la personne proposée sur les organisations que tenait le demandeur et remet l'affectation « Awaiting answer ».
3. Approuver « Wrong sub-system » ou « This sub-system doesn't apply here » remplace le sous-système par celui proposé, sans personne et avec une allocation à faire ; l'exigence ne se retrouve jamais sans sous-système.
4. Refuser rend au sous-système son état antérieur, avec le message « Reassignment rejected — reverted to the prior state ».
5. Seul un tender manager approuve ou refuse : un contributeur ne voit pas ces boutons, et le serveur refuse l'action.
6. La décision met à jour la demande vue depuis Compliance et s'inscrit au journal de l'exigence (qui, quand, quoi).
Écart maquette : un contributeur qui tient une organisation voit encore « ✓ Approve » / « ✕ Reject » sur une demande venue de Compliance (hiérarchie manager / expert héritée, abandonnée par DEC-003 et DEC-012).

### US-ALM-31 — Travailler sur son sous-système (vue du contributeur)
**Carte :** En tant que contributeur, je veux un détail centré sur l'allocation de mon sous-système, afin de corriger, compléter et valider ce qui me revient.
**Conversation :** Un contributeur appartient à un seul sous-système ; « son » sous-système se lit par l'appartenance, pas par l'affectation (US-TEAM). Sur une exigence qui touche son sous-système, il voit dans un ordre fixe le type et la classe (lecture seule), le modèle de son sous-système avec la relance, l'ABS, le PBS, l'OBS, ses allocations avec leurs personnes, la validation, les colonnes personnalisées (US-TAB) et « Propose a change ». Tous les contributeurs du sous-système sont au même niveau ; un manager de sous-système éventuel n'a pas de droit de plus.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Detail / Assignment Panel (vue contributeur), Allocated-Activity Detail Card, Validate Zone, Propose / Reassign Form.
**Règles :** DEC-012, DEC-102, DEC-104, DEC-124, DEC-086, ALLOC-024, ALLOC-025, ACC-007, ACC-010, ACC-014, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Sur une exigence de son sous-système, le détail montre, dans cet ordre : Type, Class (« Set by the tender manager »), « <sous-système>'s model » avec « ↻ Re-run ▾ », ABS, PBS, OBS, « Allocations (N) », la validation, puis « Propose a change ».
2. La pastille en tête du panneau est le statut de son sous-système (« Your status on this sub-system »), pas celui de l'exigence entière.
3. Il modifie l'ABS, le PBS, les organisations et les personnes de son sous-système, choisies parmi les membres de ce sous-système.
4. Il valide son sous-système ([US-ALM-28](#us-alm-28--valider-lallocation-dun-sous-système-dun-turnkey)), jamais le niveau Turnkey, le type ni la classe.
5. Sur une exigence multi-sous-systèmes, ce détail ne montre que la branche de son sous-système ; il n'y a pas de bloc « Distribution across sub-systems ».
6. Tout contributeur du sous-système a les mêmes droits sur l'exigence, qu'il soit ou non la personne désignée.

### US-ALM-32 — Lire en lecture seule une exigence d'un autre sous-système
**Carte :** En tant que contributeur, je veux lire l'allocation complète d'une exigence qui n'est pas à mon sous-système, sans pouvoir la modifier, afin de comprendre le contexte sans risquer de changer le travail des autres.
**Conversation :** Un contributeur lit tout le tender ([US-ALM-33](#us-alm-33--lire-tout-le-tender)) mais ne modifie rien sur une exigence dont aucun sous-système n'est le sien. Le panneau est alors en lecture seule : type, classe, puis chaque sous-système avec son ABS, son PBS, ses organisations et leurs personnes. Dans la table, les cellules de la ligne sont verrouillées. Le serveur refuse toute modification tentée autrement.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Detail / Assignment Panel (variante lecture seule, `.ro-note`), Requirement Row verrouillée (`is-ro`).
**Règles :** DEC-100, DEC-012, ALLOC-024, ALLOC-T31, ACC-013, ACC-T04, PLAT-002, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Le panneau commence par « Not assigned to you — read only. », puis Type, Class et un bloc par sous-système avec ABS, PBS et chaque organisation suivie de sa personne (« — nobody yet — » si vide) ; un partenaire y est dit « answered outside the tool ».
2. Aucun contrôle actif : ni sélecteur de sous-système, ni champ ABS / PBS / OBS, ni personne, ni relance, ni proposition, ni validation.
3. Dans la table, les contrôles de la ligne sont désactivés (infobulle « Not assigned to you — read only ») ; seules la case de sélection et la flèche de dépliage restent actives.
4. V, la pastille de statut ou une action groupée sur cette exigence ne changent rien et le disent (« Not your sub-system — read only », « … not on your sub-system — left as is »).
5. Une modification envoyée directement au serveur sur cette exigence est refusée.

### US-ALM-33 — Lire tout le tender
**Carte :** En tant que contributeur, je veux voir toutes les exigences du tender, pas seulement celles de mon sous-système, afin de lire chaque exigence dans son contexte.
**Conversation :** Un contributeur consulte tout son tender : table, vue Document, compteurs, filtres et export portent sur tout le tender, sans masquage ni caviardage. Il ne modifie que son sous-système ([US-ALM-31](#us-alm-31--travailler-sur-son-sous-système-vue-du-contributeur), [US-ALM-32](#us-alm-32--lire-en-lecture-seule-une-exigence-dun-autre-sous-système)). Cette lecture ne donne aucun accès aux tenders dont il n'est pas membre (US-TEAM).
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Requirement Table, Triage Bar, vue Document ; la bannière « Viewing as … » est un outil de démonstration, à ne pas reproduire.
**Règles :** DEC-012, ACC-007, ACC-T09, PLAT-002, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. La table d'un contributeur liste toutes les exigences du tender, celles des autres sous-systèmes comprises, ces dernières en lecture seule.
2. La vue Document montre tous les blocs en clair ; aucun passage n'est masqué ni caviardé.
3. Les compteurs de la barre, le filtre avancé et l'export portent sur tout le tender.
4. Aucun réglage du tender ne restreint cette lecture.
5. Un contributeur ne voit aucune exigence d'un tender dont il n'est pas membre, y compris par requête directe.

### US-ALM-34 — Lire la conformité dans Allocation sans la saisir
**Carte :** En tant que tender manager, je veux voir dans Allocation où en est la conformité de chaque exigence et de chaque sous-système, afin de suivre le résultat sans changer d'écran.
**Conversation :** La colonne Compliance d'Allocation est en lecture seule : un verdict ne se saisit que dans Compliance (US-CMP). Elle suit l'échelle à deux verdicts — Compliant, Not Compliant, et Pending tant qu'un verdict manque — sans aucun verrou du verdict final. La valeur d'un sous-système se calcule depuis ses organisations, celle de l'exigence depuis ses sous-systèmes : le plus restrictif l'emporte.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Compliance Pill de la colonne Compliance, Branch / Allocated-Activity Sub-row, ligne Compliance de la Turnkey System Card.
**Règles :** DEC-039, DEC-031, DEC-014, DEC-037, DEC-055, DEC-028, DEC-126  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. La colonne Compliance n'offre aucun contrôle de saisie, sur les lignes d'exigence, de sous-système ou d'organisation ; l'infobulle dit « Set on Compliance — read-only here. ».
2. Les seules valeurs sont « Compliant », « Not Compliant » et « Pending » ; ni R&D Needed, ni verrou.
3. Une exigence est « Pending » tant qu'une de ses organisations n'a pas de verdict, sinon « Not Compliant » si l'une l'est, sinon « Compliant ».
4. Chaque sous-ligne de sous-système et chaque carte de « Sub-systems (N) » affiche la conformité de ce sous-système.
5. Un verdict saisi dans Compliance apparaît dans Allocation sans autre geste.
Écart maquette : sur une exigence à un seul sous-système, la cellule Compliance de la ligne affiche « — » au lieu de la valeur (déduit du code).

### US-ALM-35 — Inscrire les actions d'allocation au journal de l'exigence
**Carte :** En tant que tender manager, je veux que chaque changement fait dans Allocation s'inscrive au journal de l'exigence avec qui, quand et avant → après, afin de pouvoir expliquer chaque allocation.
**Conversation :** Le journal est commun à Allocation et Compliance ; son affichage, ses filtres et ses commentaires relèvent de US-X. Cette story fixe ce qu'Allocation y écrit : caractérisation, statuts, chaîne et personnes par sous-système, sous-systèmes ajoutés ou retirés, propositions et réallocations, relances, jalon « Allocated ». C'est la seule trace de l'emprunt d'un modèle ([US-ALM-22](#us-alm-22--emprunter-le-modèle-dun-autre-sous-système)). Une correction d'une valeur proposée par l'IA alimente aussi le retour IA (Configuration › AI feedback, US-CFG).
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), onglet Activity du Detail / Assignment Panel (Activity Timeline).
**Règles :** PLAT-003, DOM-011, DOM-007, ALLOC-014, DEC-043, DEC-091, DEC-126  ·  **Périmètre :** Pilote 1 (à confirmer)  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Tout changement de type, de classe, de statut, d'ABS, de PBS, d'organisation ou de personne, depuis le détail, la table, une action groupée ou le clavier, crée une entrée : auteur, date et heure, champ, valeur avant → après.
2. Ajouter ou retirer un sous-système, proposer un sous-système manquant, demander, approuver ou refuser une réallocation crée une entrée qui nomme le sous-système et, le cas échéant, le motif et la justification.
3. Chaque relance crée une entrée avec le modèle utilisé, la mention de l'emprunt le cas échéant et « same result » quand rien n'a changé.
4. La validation d'une exigence ou d'un sous-système inscrit le jalon « Allocated — sent to Compliance ».
5. Valider telle quelle une dérivation faible, ou corriger un type, une classe ou un sous-système proposés par l'IA, est versé au retour IA sans rien demander à l'utilisateur.
6. Les entrées écrites par Allocation se lisent dans le journal de la même exigence depuis Compliance.
Point ouvert : contenu exact, rétention et droits de lecture du journal non spécifiés (OPEN-11, PLAT-003).

## Couverture
- Règles couvertes : ALLOC-001 → [US-ALM-07](#us-alm-07--voir-vers-quels-sous-systèmes-un-turnkey-a-aiguillé-une-exigence), [US-ALM-13](#us-alm-13--allouer-sur-un-tender-sig-autonome-sans-axe-sous-système) ; ALLOC-002 → [US-ALM-07](#us-alm-07--voir-vers-quels-sous-systèmes-un-turnkey-a-aiguillé-une-exigence) ; ALLOC-003 → [US-ALM-14](#us-alm-14--corriger-la-chaîne-abs--pbs--obs) ; ALLOC-004 → [US-ALM-11](#us-alm-11--suivre-une-exigence-répartie-sur-plusieurs-sous-systèmes) ; ALLOC-005 → [US-ALM-20](#us-alm-20--allouer-à-la-main-un-sous-système-sans-modèle), [US-ALM-22](#us-alm-22--emprunter-le-modèle-dun-autre-sous-système) ; ALLOC-006 → [US-ALM-02](#us-alm-02--savoir-pourquoi-une-exigence-est-à-revoir), [US-ALM-05](#us-alm-05--voir-le-niveau-de-confiance-de-lia-sur-le-type-et-la-classe), [US-ALM-07](#us-alm-07--voir-vers-quels-sous-systèmes-un-turnkey-a-aiguillé-une-exigence), [US-ALM-13](#us-alm-13--allouer-sur-un-tender-sig-autonome-sans-axe-sous-système), [US-ALM-14](#us-alm-14--corriger-la-chaîne-abs--pbs--obs) ; ALLOC-007 → [US-ALM-01](#us-alm-01--lire-le-statut-dune-exigence), [US-ALM-05](#us-alm-05--voir-le-niveau-de-confiance-de-lia-sur-le-type-et-la-classe), [US-ALM-26](#us-alm-26--valider-une-exigence-en-un-seul-geste) ; ALLOC-008 → [US-ALM-26](#us-alm-26--valider-une-exigence-en-un-seul-geste) ; ALLOC-009 → [US-ALM-11](#us-alm-11--suivre-une-exigence-répartie-sur-plusieurs-sous-systèmes), [US-ALM-20](#us-alm-20--allouer-à-la-main-un-sous-système-sans-modèle), [US-ALM-28](#us-alm-28--valider-lallocation-dun-sous-système-dun-turnkey) ; ALLOC-010 → [US-ALM-19](#us-alm-19--valider-sans-avoir-désigné-de-personne) ; ALLOC-011 → [US-ALM-18](#us-alm-18--désigner-la-personne-de-chaque-organisation) ; ALLOC-012 → [US-ALM-26](#us-alm-26--valider-une-exigence-en-un-seul-geste), [US-ALM-27](#us-alm-27--valider-laiguillage-dune-exigence-turnkey) (lue selon DEC-104 : un sous-système est aussi validé par son contributeur) ; ALLOC-013 → [US-ALM-10](#us-alm-10--proposer-un-sous-système-manquant), [US-ALM-29](#us-alm-29--demander-une-réallocation), [US-ALM-30](#us-alm-30--traiter-une-demande-de-réallocation) ; ALLOC-014 → [US-ALM-21](#us-alm-21--relancer-le-modèle-dallocation-sur-une-exigence), [US-ALM-22](#us-alm-22--emprunter-le-modèle-dun-autre-sous-système), [US-ALM-23](#us-alm-23--comprendre-pourquoi-une-relance-est-bloquée), [US-ALM-24](#us-alm-24--relancer-le-modèle-sur-une-sélection-dexigences), [US-ALM-35](#us-alm-35--inscrire-les-actions-dallocation-au-journal-de-lexigence) ; ALLOC-016 → [US-ALM-18](#us-alm-18--désigner-la-personne-de-chaque-organisation) ; ALLOC-017 → [US-ALM-04](#us-alm-04--corriger-le-type-et-la-classe-dune-exigence), [US-ALM-16](#us-alm-16--choisir-abs-pbs-et-rôle-dans-les-listes-des-clés) (sans le bouton de confirmation, caduc depuis DEC-099) ; ALLOC-018 → [US-ALM-01](#us-alm-01--lire-le-statut-dune-exigence) ; ALLOC-019 → [US-ALM-25](#us-alm-25--relancer-après-un-changement-de-type-ou-de-classe) ; ALLOC-020 → [US-ALM-08](#us-alm-08--ajouter-ou-retirer-un-sous-système), [US-ALM-10](#us-alm-10--proposer-un-sous-système-manquant), [US-ALM-15](#us-alm-15--gérer-les-organisations-obs-dun-sous-système) ; ALLOC-021 → [US-ALM-09](#us-alm-09--attribuer-une-exigence-à-un-partenaire-externe) ; ALLOC-022 → [US-ALM-03](#us-alm-03--suivre-lavancement-dans-la-barre-de-statut), [US-ALM-26](#us-alm-26--valider-une-exigence-en-un-seul-geste) ; ALLOC-023 → [US-ALM-04](#us-alm-04--corriger-le-type-et-la-classe-dune-exigence) (DEC-094), [US-ALM-09](#us-alm-09--attribuer-une-exigence-à-un-partenaire-externe) (DEC-093), [US-ALM-21](#us-alm-21--relancer-le-modèle-dallocation-sur-une-exigence) (DEC-091) ; ALLOC-024 → [US-ALM-12](#us-alm-12--travailler-dans-le-détail-dun-sous-système-dun-turnkey), [US-ALM-26](#us-alm-26--valider-une-exigence-en-un-seul-geste), [US-ALM-32](#us-alm-32--lire-en-lecture-seule-une-exigence-dun-autre-sous-système) ; ALLOC-025 → [US-ALM-18](#us-alm-18--désigner-la-personne-de-chaque-organisation), [US-ALM-20](#us-alm-20--allouer-à-la-main-un-sous-système-sans-modèle), [US-ALM-27](#us-alm-27--valider-laiguillage-dune-exigence-turnkey), [US-ALM-28](#us-alm-28--valider-lallocation-dun-sous-système-dun-turnkey) ; ALLOC-T01 → [US-ALM-11](#us-alm-11--suivre-une-exigence-répartie-sur-plusieurs-sous-systèmes) ; ALLOC-T02 → [US-ALM-14](#us-alm-14--corriger-la-chaîne-abs--pbs--obs) ; ALLOC-T03 → [US-ALM-20](#us-alm-20--allouer-à-la-main-un-sous-système-sans-modèle) ; ALLOC-T04 → [US-ALM-01](#us-alm-01--lire-le-statut-dune-exigence), [US-ALM-26](#us-alm-26--valider-une-exigence-en-un-seul-geste) ; ALLOC-T05 → [US-ALM-18](#us-alm-18--désigner-la-personne-de-chaque-organisation) ; ALLOC-T06 → [US-ALM-19](#us-alm-19--valider-sans-avoir-désigné-de-personne) ; ALLOC-T07 → [US-ALM-29](#us-alm-29--demander-une-réallocation), [US-ALM-30](#us-alm-30--traiter-une-demande-de-réallocation) ; ALLOC-T08 → [US-ALM-13](#us-alm-13--allouer-sur-un-tender-sig-autonome-sans-axe-sous-système) ; ALLOC-T09 → [US-ALM-21](#us-alm-21--relancer-le-modèle-dallocation-sur-une-exigence) ; ALLOC-T10 → [US-ALM-23](#us-alm-23--comprendre-pourquoi-une-relance-est-bloquée) ; ALLOC-T11 → [US-ALM-21](#us-alm-21--relancer-le-modèle-dallocation-sur-une-exigence) ; ALLOC-T12 → [US-ALM-22](#us-alm-22--emprunter-le-modèle-dun-autre-sous-système) ; ALLOC-T13 → [US-ALM-22](#us-alm-22--emprunter-le-modèle-dun-autre-sous-système) ; ALLOC-T14 → [US-ALM-21](#us-alm-21--relancer-le-modèle-dallocation-sur-une-exigence), [US-ALM-22](#us-alm-22--emprunter-le-modèle-dun-autre-sous-système) ; ALLOC-T15 → [US-ALM-21](#us-alm-21--relancer-le-modèle-dallocation-sur-une-exigence) ; ALLOC-T18 → [US-ALM-18](#us-alm-18--désigner-la-personne-de-chaque-organisation) ; ALLOC-T19 → [US-ALM-18](#us-alm-18--désigner-la-personne-de-chaque-organisation) ; ALLOC-T20 → [US-ALM-18](#us-alm-18--désigner-la-personne-de-chaque-organisation) ; ALLOC-T21 → [US-ALM-15](#us-alm-15--gérer-les-organisations-obs-dun-sous-système) ; ALLOC-T22 → [US-ALM-24](#us-alm-24--relancer-le-modèle-sur-une-sélection-dexigences) ; ALLOC-T23 → [US-ALM-21](#us-alm-21--relancer-le-modèle-dallocation-sur-une-exigence) (Turnkey : point ouvert) ; ALLOC-T24 → [US-ALM-01](#us-alm-01--lire-le-statut-dune-exigence) ; ALLOC-T25 → [US-ALM-04](#us-alm-04--corriger-le-type-et-la-classe-dune-exigence) ; ALLOC-T26 → [US-ALM-04](#us-alm-04--corriger-le-type-et-la-classe-dune-exigence) ; ALLOC-T27 → [US-ALM-25](#us-alm-25--relancer-après-un-changement-de-type-ou-de-classe) ; ALLOC-T28 → [US-ALM-08](#us-alm-08--ajouter-ou-retirer-un-sous-système), [US-ALM-15](#us-alm-15--gérer-les-organisations-obs-dun-sous-système) ; ALLOC-T29 → [US-ALM-09](#us-alm-09--attribuer-une-exigence-à-un-partenaire-externe) ; ALLOC-T30 → [US-ALM-26](#us-alm-26--valider-une-exigence-en-un-seul-geste), [US-ALM-28](#us-alm-28--valider-lallocation-dun-sous-système-dun-turnkey) (sans les « deux gestes », caducs depuis DEC-099 ; la « ligne par sous-système » d'un Turnkey devient la validation de chaque sous-système, DEC-104) ; ALLOC-T31 → [US-ALM-12](#us-alm-12--travailler-dans-le-détail-dun-sous-système-dun-turnkey), [US-ALM-26](#us-alm-26--valider-une-exigence-en-un-seul-geste), [US-ALM-32](#us-alm-32--lire-en-lecture-seule-une-exigence-dun-autre-sous-système) ; ALLOC-T32 → [US-ALM-18](#us-alm-18--désigner-la-personne-de-chaque-organisation), [US-ALM-20](#us-alm-20--allouer-à-la-main-un-sous-système-sans-modèle), [US-ALM-27](#us-alm-27--valider-laiguillage-dune-exigence-turnkey) ; KEY-T01 → [US-ALM-17](#us-alm-17--alimenter-les-listes-depuis-le-classeur-de-clés-de-référence) ; KEY-T02 → [US-ALM-16](#us-alm-16--choisir-abs-pbs-et-rôle-dans-les-listes-des-clés) ; KEY-T03 → [US-ALM-14](#us-alm-14--corriger-la-chaîne-abs--pbs--obs), [US-ALM-16](#us-alm-16--choisir-abs-pbs-et-rôle-dans-les-listes-des-clés) ; KEY-T04 → [US-ALM-04](#us-alm-04--corriger-le-type-et-la-classe-dune-exigence), [US-ALM-17](#us-alm-17--alimenter-les-listes-depuis-le-classeur-de-clés-de-référence) ; KEY-T05 → [US-ALM-16](#us-alm-16--choisir-abs-pbs-et-rôle-dans-les-listes-des-clés) ; TYPE-T01 → [US-ALM-13](#us-alm-13--allouer-sur-un-tender-sig-autonome-sans-axe-sous-système) ; TYPE-T02 → [US-ALM-13](#us-alm-13--allouer-sur-un-tender-sig-autonome-sans-axe-sous-système) ; TYPE-T03 → [US-ALM-12](#us-alm-12--travailler-dans-le-détail-dun-sous-système-dun-turnkey) ; TYPE-T04 → [US-ALM-07](#us-alm-07--voir-vers-quels-sous-systèmes-un-turnkey-a-aiguillé-une-exigence), [US-ALM-11](#us-alm-11--suivre-une-exigence-répartie-sur-plusieurs-sous-systèmes) ; TYPE-T05 → [US-ALM-20](#us-alm-20--allouer-à-la-main-un-sous-système-sans-modèle) ; TYPE-T08 → [US-ALM-13](#us-alm-13--allouer-sur-un-tender-sig-autonome-sans-axe-sous-système) ; TYPE-T09 → [US-ALM-14](#us-alm-14--corriger-la-chaîne-abs--pbs--obs) ; TYPE-T11 → [US-ALM-17](#us-alm-17--alimenter-les-listes-depuis-le-classeur-de-clés-de-référence) (généralisée à tout tender Mainline) ; DOM-004 → [US-ALM-18](#us-alm-18--désigner-la-personne-de-chaque-organisation), [US-ALM-19](#us-alm-19--valider-sans-avoir-désigné-de-personne) ; DOM-005 → [US-ALM-11](#us-alm-11--suivre-une-exigence-répartie-sur-plusieurs-sous-systèmes) ; DOM-006 → [US-ALM-18](#us-alm-18--désigner-la-personne-de-chaque-organisation) ; DOM-007 → [US-ALM-05](#us-alm-05--voir-le-niveau-de-confiance-de-lia-sur-le-type-et-la-classe), [US-ALM-26](#us-alm-26--valider-une-exigence-en-un-seul-geste), [US-ALM-35](#us-alm-35--inscrire-les-actions-dallocation-au-journal-de-lexigence) ; JRN-002 → parcours de toute l'épopée, critères de recette dans [US-ALM-04](#us-alm-04--corriger-le-type-et-la-classe-dune-exigence) (identité conservée), [US-ALM-11](#us-alm-11--suivre-une-exigence-répartie-sur-plusieurs-sous-systèmes) (branches indépendantes), [US-ALM-14](#us-alm-14--corriger-la-chaîne-abs--pbs--obs) (dépendances invalidées), [US-ALM-26](#us-alm-26--valider-une-exigence-en-un-seul-geste) (validation).
- Non couvertes, avec la raison : ALLOC-015, ALLOC-T16, ALLOC-T17 — couvertes par l'épopée US-CFG (relance globale au changement de modèle, dans les paramètres ; référencée par [US-ALM-21](#us-alm-21--relancer-le-modèle-dallocation-sur-une-exigence), 23, 24) ; TYPE-T06 — règle de recette, appliquée par le champ Variantes de chaque story ; TYPE-T07 — contenu de démonstration du tender SIG de référence (DEC-044), pas un comportement ; TYPE-T10 — couverte par l'épopée US-DASH (ligne produit du tableau de bord).
