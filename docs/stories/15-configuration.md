<!-- Généré depuis le backlog du 10 octobre 2026 ; voir README.md pour les conventions. -->
# Paramètres du tender (US-CFG)

L'écran Configuration réunit les réglages d'un tender en onze sections — General, Team & contributors, Reminders, Allocation model, Compliance, Appearance, Capture & segmentation, AI feedback, Q&A & submission, Versions, Language — et s'ouvre par la roue dentée de l'en-tête (route `#config`). Parcours JRN-007 : ne montrer que des réglages réellement appliqués. Certains choix sont figés à la création et seulement affichés : ligne produit, produit, mode d'assistance IA (DEC-049, DEC-095). Deux sections sont décrites ailleurs : la liste des stratégies d'écart (section Compliance) dans [US-RSK-01](10-risques.md#us-rsk-01--écrire-les-stratégies-décart-du-tender) à [US-RSK-03](10-risques.md#us-rsk-03--changer-le-résultat-dune-stratégie-déjà-utilisée), les réglages de conversion et le signal de découpe incertaine (section Capture & segmentation) dans [US-CAP-02](04-capture-ia.md#us-cap-02--régler-la-conversion-du-document-source) et [US-CAP-05](04-capture-ia.md#us-cap-05--signaler-une-découpe-incertaine). Termes : *modèle d'allocation* = ce qui dérive ABS → PBS → OBS pour un produit ; *partenaire externe* = entreprise ajoutée comme système à la liste OBS d'un Turnkey. Point ouvert commun : qui peut modifier quels paramètres (JRN-007, OPEN-05) — seuls les stratégies et les partenaires sont attribués au chef de projet par décision ; le thème est personnel.

### US-CFG-01 — Ouvrir les paramètres et n'y trouver que des réglages réels
**Carte :** En tant que chef de projet, je veux ouvrir les paramètres du tender et les parcourir par section, en sachant que chaque réglage affiché agit vraiment, afin de régler le tender sans me fier à des contrôles décoratifs.
**Conversation :** JRN-007 demande de distinguer les paramètres réellement appliqués de ceux seulement représentés : dans le produit, un réglage n'est livré que lorsque son effet est écrit. Un réglage enregistré est conservé (PLAT-001) et vaut pour tous les membres du tender, sauf le thème, personnel ([US-CFG-10](#us-cfg-10--choisir-son-thème-clair-ou-sombre)). Les sections Compliance et Capture & segmentation sont détaillées dans US-RSK et US-CAP. Les bandeaux « demo only » de la maquette ne font pas partie du produit.
**Maquette :** Configuration — `dashboard-et-config.html` (route `#config`), Config Sidebar Nav, Config Section, boutons « Save configuration » / « Discard changes ».
**Règles :** JRN-007, PLAT-001, PLAT-002, DEC-035, DEC-084  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. La roue dentée « Project configuration » de l'en-tête ouvre les paramètres du tender ouvert ; le bouton « Dashboard » ramène au tableau de bord.
2. La navigation liste, dans cet ordre, General, Team & contributors, Reminders, Allocation model, Compliance, Appearance, Capture & segmentation, AI feedback, Q&A & submission, Versions, Language ; cliquer une section l'affiche.
3. Aucun réglage n'est affiché s'il ne change rien au tender.
4. Un réglage enregistré est retrouvé à la réouverture, depuis un autre poste et par les autres membres du tender.
5. Aucun réglage de jalon ou de verrou n'existe : ni « Enforce full validation before export », ni « Allocation completeness gate ».
6. Une modification tentée sans le droit de modifier est refusée par le serveur, avec la raison à l'écran.
Écart maquette : la plupart des sections portent l'avertissement « TE2 — demo only » et « Save configuration » n'affiche qu'un message.
Point ouvert : qui peut modifier quels paramètres (JRN-007, OPEN-05) ; enregistrement immédiat réglage par réglage ou par « Save configuration » (JRN-007).

### US-CFG-02 — Consulter les informations générales du tender
**Carte :** En tant que chef de projet, je veux retrouver dans « General » l'identité du tender et les choix figés à sa création, afin de vérifier comment il a été créé.
**Conversation :** La ligne produit (Turnkey, SIG…) et le mode d'assistance IA sont fixés à la création : ils déterminent la structure d'allocation, et se tromper oblige à recréer le tender (DEC-095, comme le produit — DEC-049). Le refus de toute modification par le serveur est décrit avec leur choix dans l'assistant ([US-NEW-02](02-creation.md#us-new-02--choisir-la-ligne-produit-fixée-à-la-création), [US-NEW-06](02-creation.md#us-new-06--choisir-le-mode-dassistance-ia-fixé-à-la-création)). Les documents et leurs versions se gèrent dans Documents & versions, pas ici (DEC-069, voir US-DOC).
**Maquette :** Configuration — `dashboard-et-config.html` (route `#config`), section General (Config Field Row, Option Description Box).
**Règles :** DEC-095, DEC-049, DEC-069, LIFE-001, LIFE-002  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. La section affiche le nom du tender et son BO-ID.
2. « Product line » affiche la ligne du tender en lecture seule, avec « Not editable, by decision — not a missing control. ».
3. Le mode d'assistance IA choisi à la création (« AI-assisted », « AI segmentation only » ou les étapes personnalisées) s'affiche en lecture seule, avec la même mention.
4. « Documents » affiche « Managed in Documents & versions, not here. » et ne propose aucun fichier.
Écart maquette : le mode d'assistance IA n'apparaît pas dans les paramètres (c'est une valeur unique pour toute la démo) ; nom et BO-ID sont des champs de saisie sans effet.
Point ouvert : modifier le nom et le BO-ID après création (non décidé) ; les interrupteurs par étape IA font-ils partie du mode figé (DEC-095 ne le dit pas).

### US-CFG-03 — Régler l'échéance de soumission
**Carte :** En tant que chef de projet, je veux régler la date de soumission du tender, afin que le compte à rebours et la courbe de rythme disent juste.
**Conversation :** L'échéance ne pilote plus que le compte à rebours, aucun jalon (DEC-084) : les jours restants de l'en-tête du tableau de bord ([US-DASH-01](13-tableau-de-bord.md#us-dash-01--voir-lidentité-et-léchéance-du-tender-ouvert)) et le repère « Submission » des statistiques ([US-STAT-03](14-statistiques.md#us-stat-03--suivre-les-dates-clés-et-le-rythme-du-tender)).
**Maquette :** Configuration — `dashboard-et-config.html` (route `#config`), General › « Submission deadline ».
**Règles :** DEC-084, PLAT-001  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. « Submission deadline » affiche la date enregistrée et se modifie par un sélecteur de date.
2. Après enregistrement, « days to submission » du tableau de bord se calcule sur la nouvelle date.
3. Le repère « Submission » et la projection des statistiques utilisent la nouvelle date.
4. Changer l'échéance ne modifie aucun statut ni aucune exigence, et ne bloque rien.
Écart maquette : la date est un champ sans effet ; le compte à rebours est figé à la création.
Point ouvert : accepter ou non une échéance déjà passée (non écrit).

### US-CFG-04 — Voir les contributeurs du tender depuis les paramètres
**Carte :** En tant que chef de projet, je veux voir dans « Team & contributors » les contributeurs du tender avec leur système et leur charge, afin de vérifier l'équipe avant d'allouer.
**Conversation :** Une personne est choisie dans l'annuaire et rattachée à un seul système (ACC-004, DEC-102) : la section lit donc le même casting que Team casting (voir US-TEAM), sans liste à part. Un contributeur qui a du travail affecté ne se retire qu'après réaffectation (ACC-006). Le réglage « Restricted view » n'existe plus : un contributeur lit tout le tender (DEC-012).
**Maquette :** Configuration — `dashboard-et-config.html` (route `#config`), section Team & contributors (Team & Experts Config Editor : Expert Editor Row, Add Expert Form, Chip Group).
**Règles :** ACC-004, ACC-006, DEC-102, DEC-124, DEC-012, ACC-007  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. La section liste les contributeurs du tender avec leur système et « N requirements assigned ».
2. La liste est, au même moment, celle de Team casting.
3. Ajouter un contributeur passe par la recherche dans l'annuaire et le choix d'un système, avec les mêmes refus que Team casting (une personne déjà dans un autre système est refusée, raison affichée).
4. Retirer un contributeur qui a des exigences affectées est refusé avec « Cannot remove <nom> — N requirements still assigned ».
5. Aucun réglage « Restricted view » (Redacted / Hidden) n'est proposé.
Écart maquette : la liste est saisie au clavier (nom et équipe libres), indépendante du casting.
Point ouvert : garder cette section ou la réduire à un lien vers Team casting (doublon) ; effet des « Assignment criteria » (PBS, ABS, OBS), non spécifié.

### US-CFG-05 — Régler le seuil de retard et la cadence des relances
**Carte :** En tant que chef de projet, je veux régler au bout de combien de jours une réponse est en retard et à quelle fréquence maximale un contributeur peut être relancé, afin d'éviter à la fois les oublis et le harcèlement.
**Conversation :** La section « Reminders » remplace « Workflow & milestones » : il n'y a plus de jalon (DEC-084). La relance reste un geste humain unique dans Compliance, adressé à la personne de l'affectation (DEC-125, DEC-087, voir US-CMP). L'effet exact des deux réglages n'est pas écrit ; la story fixe ce qui est sûr — valeurs, défaut, conservation — et laisse le reste en point ouvert.
**Maquette :** Configuration — `dashboard-et-config.html` (route `#config`), section Reminders (Range Slider « Overdue threshold », Select Dropdown « Maximum reminder cadence »).
**Règles :** DEC-084, DEC-125, DEC-087, DEC-078, PLAT-005, PLAT-008  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. « Overdue threshold » se règle de 1 à 14 jours, 5 par défaut, et affiche la valeur choisie (« 5 days », « 1 day »).
2. « Maximum reminder cadence » propose « Once every 2 days », « Daily », « Once every 3 days » et « Manual only ».
3. Les deux valeurs sont enregistrées pour le tender et retrouvées à la réouverture.
4. Aucun de ces réglages ne crée de statut « overdue » dans Compliance.
Écart maquette : les deux réglages ne sont reliés à rien ; le tableau de bord compte les retards avec une règle fixe.
Point ouvert : le seuil remplace-t-il les 5 jours fixés par PLAT-008 pour le tableau de bord et les statistiques ; la cadence limite-t-elle les relances manuelles ou pilote-t-elle des relances automatiques (déclencheurs de PLAT-005, OPEN-11).

### US-CFG-06 — Consulter le système, le produit et le modèle appliqué
**Carte :** En tant que chef de projet, je veux voir sur quel système et quel produit le tender est émis et quel modèle d'allocation s'applique, afin de comprendre d'où viennent les dérivations ABS → PBS → OBS.
**Conversation :** Le produit décrit ce que le tender est et se fixe à la création ; le modèle qui en découle est la seule partie modifiable (DEC-049, ALLOC-015). SIG a trois produits connus — Urban, Mainline Wayside, Mainline Onboard (DEC-061) — et un tender « Mainline » est un tender SIG de produit Mainline (DEC-047). Un Turnkey n'a pas de produit propre : il porte une combinaison dont chaque système applique son modèle, et la matrice des combinaisons reste à fournir (DEC-048). Changer de modèle : [US-CFG-07](#us-cfg-07--changer-de-modèle-et-relancer-toute-la-dérivation) ; absence de modèle applicable dans Allocation : [US-CAP-10](04-capture-ia.md#us-cap-10--dire-quaucun-modèle-ne-sapplique-sans-en-emprunter-un-en-silence).
**Maquette :** Configuration — `dashboard-et-config.html` (route `#config`), section Allocation model (« System », « Product », « Model applied »).
**Règles :** DEC-049, DEC-047, DEC-048, DEC-061, DEC-095, ALLOC-015, AI-010, TYPE-T05  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. « System » affiche le système du tender en lecture seule.
2. « Product » affiche le produit en lecture seule avec « Not editable, by decision — not a missing control. » ; sur un Turnkey, il dit que la combinaison n'est pas renseignée tant que sa matrice manque, sans valeur inventée.
3. Sur un tender SIG (Mainline compris), « Model applied » propose « SIG Urban », « SIG Mainline Wayside » et « SIG Mainline Onboard », le modèle du produit étant présélectionné.
4. Sur un Turnkey, « Model applied » affiche « Per-system models — set by the tender's combination », sans choix possible.
5. Sur un tender dont le produit n'a pas de modèle fourni (RSC aujourd'hui), la section le dit et ne propose jamais le modèle d'un autre type de tender.
Écart maquette : sur un tender RSC ou « Services », le produit affiche le message de combinaison Turnkey.
Point ouvert : produits et modèles RSC non fournis (DEC-047, OPEN-15) ; maille de l'OBS du modèle Urban non tranchée.

### US-CFG-07 — Changer de modèle et relancer toute la dérivation
**Carte :** En tant que chef de projet, je veux changer le modèle d'allocation du tender en sachant exactement ce que la relance va détruire, afin de corriger un mauvais modèle sans perte de travail par surprise.
**Conversation :** Changer de modèle relance la dérivation sur toutes les exigences et écrase tout, réponses comprises : si le modèle était le mauvais, tout ce qui en découle l'est aussi (DEC-050, ALLOC-015), comme une nouvelle version de document (DEC-027). C'est l'inverse de la relance unitaire, interdite dès qu'une réponse existe (ALLOC-014, voir US-ALM) : les deux ne se remplacent pas et l'une n'est jamais proposée en repli de l'autre. Le produit, lui, ne change pas (DEC-049).
**Maquette :** Configuration — `dashboard-et-config.html` (route `#config`), Allocation model › « Re-run on all requirements » (encadré de danger, bouton « ↻ Change model and re-run everything »).
**Règles :** ALLOC-015, ALLOC-T16, ALLOC-T17, DEC-050, DEC-049, DEC-027, PLAT-003  ·  **Périmètre :** Pilote 1  ·  **Variantes :** SIG, Mainline
**Critères d'acceptation :**
1. Choisir un autre modèle affiche, avant toute confirmation, le nombre d'exigences qui seront re-dérivées, de réponses enregistrées et de verdicts internes qui seront détruits, y compris ceux déjà déclarés au client.
2. La confirmation reprend ces chiffres et demande un geste de plus qu'une confirmation ordinaire ; annuler ne change rien.
3. Après confirmation, aucune exigence ne garde de dérivation ABS / PBS / OBS issue de l'ancien modèle.
4. Le produit du tender reste inchangé et rien n'indique ensuite qu'il aurait changé.
5. La relance s'inscrit au journal de chaque exigence (avant → après, modèle utilisé).
6. Une exigence déjà répondue reste non relançable une par une : la relance globale n'est jamais proposée pour contourner ce blocage.
Écart maquette : la section n'est qu'un affichage — le sélecteur est sans effet, le bouton désactivé et les chiffres viennent d'une copie.
Point ouvert : statut des exigences après la relance (à revoir ou à valider) et sort des personnes affectées, des stratégies et des risques — non écrits ; forme du geste de confirmation renforcée ; changement de modèle sur un Turnkey (dépend de la matrice des combinaisons, DEC-048).

### US-CFG-08 — Ajouter un partenaire externe à la liste OBS Turnkey
**Carte :** En tant que chef de projet d'un tender Turnkey, je veux ajouter une entreprise partenaire comme système du tender, afin de lui attribuer la part du périmètre qu'elle prend en charge.
**Conversation :** La liste des systèmes attribuables en passe 1 (liste OBS Turnkey) appartient à la configuration du tender, alors que le jeu d'étiquettes du modèle est fermé : l'IA ne prédit jamais un partenaire (DEC-082, SPEC-external-partners). Un partenaire n'a ni modèle, ni équipe, ni personne ; son usage dans Allocation et la saisie de son verdict sont décrits dans US-ALM et US-RSK. Tenders Turnkey seulement ; liste propre au tender en v1.
**Maquette :** Configuration — `dashboard-et-config.html` (route `#config`), Allocation model › « Turnkey OBS list » (Turnkey OBS List Setting).
**Règles :** DEC-082, ALLOC-021, ALLOC-T29, CONF-026  ·  **Périmètre :** Pilote 1 (à confirmer)  ·  **Variantes :** Turnkey
**Critères d'acceptation :**
1. Sur un tender Turnkey, « Turnkey OBS list » affiche les systèmes du modèle, non modifiables, puis les partenaires ajoutés dans une couleur propre, avec une infobulle qui dit « added for this tender, not part of the model ».
2. Saisir le nom d'une entreprise puis « ＋ Add » (ou Entrée) l'ajoute avec un code court tiré de son nom, et le message « <nom> added to the Turnkey OBS list as <code> » s'affiche.
3. Un nom vide est refusé (« Type the partner's name ») ; un partenaire déjà présent est refusé (« That partner is already in the list »).
4. Le partenaire apparaît, dans sa couleur, partout où la liste sert : table et détail d'Allocation, filtres, « + Add system », Compliance.
5. Sur un tender SIG ou RSC, la ligne « Turnkey OBS list » n'existe pas.
Écart maquette : la couleur des partenaires est hors de l'échelle de jetons.

### US-CFG-09 — Retirer un partenaire externe
**Carte :** En tant que chef de projet d'un tender Turnkey, je veux retirer un partenaire ajouté à tort, afin de garder une liste juste sans rendre d'exigence orpheline.
**Conversation :** Le retrait n'est possible que tant qu'aucune exigence n'est attribuée au partenaire ; sinon il est refusé avec le nombre d'exigences à réattribuer d'abord — même règle que les options de colonnes personnalisées (DEC-093, DEC-065). L'usage compte Allocation et Compliance.
**Maquette :** Configuration — `dashboard-et-config.html` (route `#config`), Allocation model › « Turnkey OBS list », ✕ sur l'étiquette d'un partenaire.
**Règles :** DEC-093, ALLOC-023, DEC-065, PLAT-002  ·  **Périmètre :** Pilote 1 (à confirmer)  ·  **Variantes :** Turnkey
**Critères d'acceptation :**
1. Seuls les partenaires ajoutés portent un ✕ ; les systèmes du modèle n'en ont pas.
2. Retirer un partenaire sans exigence attribuée le supprime de la liste partout, avec « <nom> removed from the Turnkey OBS list ».
3. Retirer un partenaire encore attribué est refusé avec « Still assigned to N requirements — reassign them to another system first » ; rien ne change.
4. N compte les exigences attribuées dans Allocation comme les affectations de Compliance.
5. Le refus est aussi appliqué par le serveur à une requête directe.

### US-CFG-10 — Choisir son thème clair ou sombre
**Carte :** En tant que contributeur ou chef de projet, je veux choisir un thème clair ou sombre pour toute l'application, afin de travailler confortablement selon la salle et l'écran.
**Conversation :** Le thème est une préférence personnelle : il ne change rien pour les autres membres du tender. Le clair est le défaut. Les deux thèmes gardent les mêmes sens de couleur ([US-X-14](16-transverse.md#us-x-14--lire-des-couleurs-qui-gardent-toujours-le-même-sens)).
**Maquette :** Configuration — `dashboard-et-config.html` (route `#config`), section Appearance (Theme Picker).
**Règles :** DEC-063, PLAT-001  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. « Appearance » propose « Dark » et « Light », le thème en cours étant marqué.
2. Choisir un thème l'applique tout de suite à tous les écrans, avec « <Theme> theme applied ».
3. Le thème choisi est retrouvé à la connexion suivante, sur tout poste.
4. Le choix d'un utilisateur ne change pas le thème des autres.
5. Un utilisateur qui n'a jamais choisi voit le thème clair.
Écart maquette : le thème est une valeur de la session de démo, rangée dans les paramètres du tender bien qu'il soit personnel.
Point ouvert : place d'un réglage personnel dans les paramètres d'un tender (non décidé).

### US-CFG-11 — Capter chaque correction d'une proposition de l'IA
**Carte :** En tant que chef de projet, je veux que chaque correction d'une proposition de l'IA soit enregistrée sans geste supplémentaire, afin d'améliorer les prochains modèles sans ralentir l'équipe.
**Conversation :** Le retour porte sur ce que l'IA propose encore : nature et classe, système proposé par le routage Turnkey, dérivation faible validée telle quelle ; l'IA ne propose plus de personne, un OBS étant une organisation (DEC-054). Aucune raison n'est demandée. Le retour nourrit le modèle suivant et ne recalcule jamais le tender en cours ; proposition, valeur retenue et correction restent distinctes (DOM-013, [US-X-07](16-transverse.md#us-x-07--garder-séparées-la-proposition-de-lia-la-valeur-retenue-et-la-correction)). Les gestes de correction et leur versement au retour IA sont dans Allocation ([US-ALM-35](05-allocation.md#us-alm-35--inscrire-les-actions-dallocation-au-journal-de-lexigence)) ; cette story fixe ce que le retour contient.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), gestes de correction ; Configuration — `dashboard-et-config.html` (route `#config`), AI feedback › « This session » (Live Feedback Row).
**Règles :** DOM-013, PLAT-003, PLAT-008, DEC-054, DEC-120, DEC-117  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes (Turnkey : routage vers les systèmes)
**Critères d'acceptation :**
1. Changer une nature ou une classe proposée par l'IA enregistre un retour : exigence, champ, valeur proposée → valeur retenue, niveau de confiance de l'IA.
2. Retirer ou remplacer un système proposé par le routage Turnkey enregistre un retour avec le pourcentage de confiance du routage.
3. Valider telle quelle une dérivation sous le seuil de confiance enregistre un retour qui le dit, avec la confiance de chaque étape.
4. Aucune question, fenêtre ni geste supplémentaire n'est imposé au moment de la correction.
5. Le retour n'est jamais appliqué au tender en cours : aucune exigence n'est recalculée ni re-notée.
6. Le retour affiché ne nomme pas la personne qui a corrigé.
Écart maquette : le texte de la section promet encore une explication demandée quand l'IA était très confiante ; le retour n'est gardé que dans la session.
Point ouvert : destination et anonymisation des retours vers le chantier IA (DEC-020).

### US-CFG-12 — Consulter la qualité de l'IA dans « AI feedback »
**Carte :** En tant que chef de projet, je veux voir les taux d'acceptation des propositions de l'IA, les corrections récurrentes et les dernières corrections, afin de savoir où l'IA se trompe sur ce tender.
**Conversation :** C'est le seul endroit où l'IA est mesurée : le tableau de bord ne la mesure plus (DEC-117). Les mesures portent sur les étapes de l'IA, jamais sur les personnes (DEC-118). Rien ici ne change le tender en cours.
**Maquette :** Configuration — `dashboard-et-config.html` (route `#config`), section AI feedback (AI Feedback Panel (Config) : Stat Tile, AI Pattern Row, Live Feedback Row).
**Règles :** DEC-117, DEC-118, PLAT-008, DEC-020  ·  **Périmètre :** Pilote 1 (à confirmer)  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Un taux d'acceptation s'affiche par étape — « Segmentation », « System », « Characterization », « Assignment (OBS) » — en %, avec une barre.
2. « Recurring patterns » liste les corrections qui se répètent sur ce tender, avec leur nombre (« N× this tender »).
3. « This session » liste les dernières corrections captées (surface, exigence, avant → après), ou dit qu'aucune n'a encore été captée.
4. Les chiffres sont calculés sur les corrections enregistrées du tender, jamais écrits à la main.
5. Aucune mesure de l'IA n'apparaît ailleurs qu'ici.
Écart maquette : taux et motifs écrits à la main ; seule la liste de la session est réelle.
Point ouvert : formules — dénominateur, revue effective, corrections répétées (PLAT-008 « Corrections IA ») ; définition d'un motif récurrent ; période couverte au-delà de la session.

### US-CFG-13 — Choisir le canal de l'émetteur pour les questions
**Carte :** En tant que chef de projet, je veux indiquer par quel canal les questions partent vers l'émetteur du tender, afin que l'export des questions ait la forme attendue.
**Conversation :** L'outil n'envoie rien : les questions sortent par export et le chef de projet les marque envoyées à la main (QA-003, DEC-116). Il ne reste dans cette section que le canal ; la détection de doublons et la revue interne avant envoi sont retirées (DEC-116). L'export lui-même est dans US-QA.
**Maquette :** Configuration — `dashboard-et-config.html` (route `#config`), section Q&A & submission › « Issuer channel » (Segmented Control).
**Règles :** QA-003, DEC-116  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. « Issuer channel » propose « Buyer portal », « Standard form » et « Free document », chacun avec son explication.
2. Le canal choisi est enregistré pour le tender.
3. L'export des questions de Q&A prend la forme du canal choisi.
4. Aucun réglage « AI duplicate detection » ni « Internal review before sending » n'est proposé.
5. Aucun canal ne déclenche un envoi au client depuis SRM.
Écart maquette : le réglage n'agit pas sur l'écran Q&A.
Point ouvert : gabarit attendu pour « Buyer portal » et « Standard form », non fourni.

### US-CFG-14 — Régler la numérotation des versions et la détection d'addendum
**Carte :** En tant que chef de projet, je veux choisir comment les versions des documents sont numérotées et si l'IA propose de traiter un addendum comme une nouvelle version, afin que l'historique des documents reste lisible.
**Conversation :** Les versions appartiennent aux documents (DEC-069) et se gèrent dans Documents & versions (US-DOC). Aucune règle n'est écrite pour ces deux réglages : la story fixe leurs options, leurs effets restent ouverts. Le réglage de notification des contributeurs au changement de version est retiré (rien ne le réalisait ; notifications : PLAT-005).
**Maquette :** Configuration — `dashboard-et-config.html` (route `#config`), section Versions (« Numbering », « Detect addendum-as-answer »).
**Règles :** DEC-069, LIFE-012  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. « Numbering » propose « Auto-increment + alias » (recommandé) et « Free entry ».
2. « Detect addendum-as-answer » s'active ou se désactive (« AI suggests requalifying as a version »).
3. Les deux valeurs sont enregistrées pour le tender.
4. Aucun réglage ne crée de version du tender entier : les versions restent par document.
Écart maquette : réglages sans effet (« TE2 — demo only »).
Point ouvert : règle de numérotation (format, alias) ; ce que fait la détection d'addendum — où la proposition apparaît, qui la confirme (aucune règle écrite).

### US-CFG-15 — Voir la langue de travail et la langue source
**Carte :** En tant que chef de projet, je veux voir que la langue de travail du tender est l'anglais et dans quelle langue sont ses documents, afin de savoir ce qui est traduit et ce qui part au client.
**Conversation :** L'anglais est la langue de travail, fixe : un texte source dans une autre langue est traduit automatiquement en anglais et l'original est conservé (DEC-019, LANG-001 ; traduction : [US-CAP-07](04-capture-ia.md#us-cap-07--traduire-automatiquement-vers-langlais-de-travail)). Un tender n'a qu'une langue source, choisie à la création (DEC-096, [US-NEW-04](02-creation.md#us-new-04--déclarer-la-langue-source-unique-du-tender)). L'interface reste en anglais.
**Maquette :** Configuration — `dashboard-et-config.html` (route `#config`), section Language (« Working language », « Source document language »).
**Règles :** LANG-001, LANG-002, DEC-019, DEC-096  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. « Working language » affiche « English » en lecture seule, avec « Not editable — translation always goes into English. ».
2. La langue source du tender s'affiche telle que choisie à la création.
3. Aucun réglage « Default translation target » n'est proposé.
4. Aucun réglage ne permet de déclarer plusieurs langues sources pour un même tender.
Écart maquette : « Source document language » et « Interface language » sont des listes modifiables sans effet.
Point ouvert : modifier la langue source après la capture (non décidé) ; langue de l'interface (seul l'anglais existe, aucune décision produit).

## Couverture
- Règles couvertes : JRN-007 → [US-CFG-01](#us-cfg-01--ouvrir-les-paramètres-et-ny-trouver-que-des-réglages-réels), [US-CFG-02](#us-cfg-02--consulter-les-informations-générales-du-tender) ; PLAT-001 → [US-CFG-01](#us-cfg-01--ouvrir-les-paramètres-et-ny-trouver-que-des-réglages-réels), [US-CFG-03](#us-cfg-03--régler-léchéance-de-soumission), [US-CFG-10](#us-cfg-10--choisir-son-thème-clair-ou-sombre) ; PLAT-002 → [US-CFG-01](#us-cfg-01--ouvrir-les-paramètres-et-ny-trouver-que-des-réglages-réels), [US-CFG-09](#us-cfg-09--retirer-un-partenaire-externe) ; PLAT-003 → [US-CFG-07](#us-cfg-07--changer-de-modèle-et-relancer-toute-la-dérivation), [US-CFG-11](#us-cfg-11--capter-chaque-correction-dune-proposition-de-lia) ; PLAT-005 → [US-CFG-05](#us-cfg-05--régler-le-seuil-de-retard-et-la-cadence-des-relances) (lien avec les relances, point ouvert) ; PLAT-008 « Corrections IA » → [US-CFG-11](#us-cfg-11--capter-chaque-correction-dune-proposition-de-lia), [US-CFG-12](#us-cfg-12--consulter-la-qualité-de-lia-dans--ai-feedback-) ; DOM-013 → [US-CFG-11](#us-cfg-11--capter-chaque-correction-dune-proposition-de-lia).
- Autres règles mises en œuvre : ALLOC-015, AI-010, TYPE-T05 → [US-CFG-06](#us-cfg-06--consulter-le-système-le-produit-et-le-modèle-appliqué) ; ALLOC-015, ALLOC-T16, ALLOC-T17 → [US-CFG-07](#us-cfg-07--changer-de-modèle-et-relancer-toute-la-dérivation) ; ALLOC-021, ALLOC-T29, CONF-026 → [US-CFG-08](#us-cfg-08--ajouter-un-partenaire-externe-à-la-liste-obs-turnkey) ; ALLOC-023 → [US-CFG-09](#us-cfg-09--retirer-un-partenaire-externe) ; ACC-004, ACC-006, ACC-007 → [US-CFG-04](#us-cfg-04--voir-les-contributeurs-du-tender-depuis-les-paramètres) ; LIFE-001, LIFE-002 → [US-CFG-02](#us-cfg-02--consulter-les-informations-générales-du-tender) ; QA-003 → [US-CFG-13](#us-cfg-13--choisir-le-canal-de-lémetteur-pour-les-questions) ; LIFE-012 → [US-CFG-14](#us-cfg-14--régler-la-numérotation-des-versions-et-la-détection-daddendum) ; LANG-001, LANG-002 → [US-CFG-15](#us-cfg-15--voir-la-langue-de-travail-et-la-langue-source).
- Non couvertes, avec la raison : CAPT-T01, CAPT-T02, CAPT-T03 — couvertes par l'épopée US-CAP ([US-CAP-02](04-capture-ia.md#us-cap-02--régler-la-conversion-du-document-source), réglages de conversion de la section Capture & segmentation) ; CAPT-T04 — critère propre à la maquette (avertissement « demo only »), sans objet pour le produit ; réglage « Uncertainty threshold » — point ouvert (seuil réglable ou règles textuelles, [US-CAP-05](04-capture-ia.md#us-cap-05--signaler-une-découpe-incertaine)) ; liste des stratégies d'écart de la section Compliance (DEC-110, DEC-111) — couverte par l'épopée US-RSK ([US-RSK-01](10-risques.md#us-rsk-01--écrire-les-stratégies-décart-du-tender) à [US-RSK-03](10-risques.md#us-rsk-03--changer-le-résultat-dune-stratégie-déjà-utilisée)) ; PLAT-004, PLAT-006, PLAT-007, DOM-011 — couvertes par l'épopée US-X ; PLAT-008 (autres mesures) — couverte par l'épopée US-STAT ; réglages « Document rendering », « Re-segmentation on new version », « Never overwrite manual edits » (à concilier avec DOM-013), « Assignment criteria » — point ouvert, comportement cible non spécifié ; « Restricted view » — caduc (DEC-012) ; « Review milestone gate », « Outdated-response re-flag », « AI duplicate detection », « Internal review before sending », « Default translation target », critère « Discipline » — retirés (DEC-035, DEC-084, DEC-026, DEC-078, DEC-116, LANG-001).
