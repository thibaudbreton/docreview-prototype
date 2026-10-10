<!-- Généré depuis le backlog du 10 octobre 2026 ; voir README.md pour les conventions. -->
# Statistiques du tender (US-STAT)

Les statistiques sont un panneau du tableau de bord, en trois onglets : **Project**, **Allocation**, **Compliance** (DEC-117). Elles sont purement métier : chaque bloc s'ouvre sur une phrase calculée — ce qu'un responsable dirait à voix haute —, puis le chiffre, et chaque ligne mène à l'écran concerné (parcours JRN-007). **Aucune statistique ne mesure une personne** : l'activité et les réponses se comptent par système et sous-système (DEC-118 — information-consultation du CSE, codécision du Betriebsrat, RGPD) ; la qualité de l'IA n'y figure pas et reste dans Configuration › AI feedback ([US-CFG-12](15-configuration.md#us-cfg-12--consulter-la-qualité-de-lia-dans--ai-feedback-)). Termes : *sous-système* = ici les périmètres staffés dans le casting (DEC-118, voir point ouvert) ; *affectation* = le travail de conformité confié à une organisation et à sa personne ; *conformité externe* = ce que le client recevra, dérivée de la stratégie d'écart (DEC-106). Points ouverts communs : les formules de PLAT-008 sont « à compléter », et la courbe de rythme comme l'activité de la semaine exigent un historique (snapshots) que rien ne stocke encore.

### US-STAT-01 — Lire les statistiques par onglet, une phrase puis le chiffre
**Carte :** En tant que chef de projet, je veux des statistiques rangées en trois onglets, où chaque bloc commence par une phrase calculée puis montre le chiffre, afin de comprendre la situation sans interpréter des graphiques.
**Conversation :** Project couvre le tender entier (dates, rythme, équipe) ; Allocation et Compliance suivent les deux cartes d'étape. Une mesure annonce toujours son unité — exigences, affectations, systèmes, réponses et risques ne sont pas interchangeables — et aucun indicateur composite de santé ni pourcentage global n'est affiché sans définition métier (PLATFORM). Les chiffres se calculent sur les données enregistrées du tender, les mêmes que celles des écrans d'origine.
**Maquette :** Tableau de bord — `dashboard-et-config.html` (route `#dashboard`), Statistics Panel › Tab Bar, Stat Block.
**Règles :** DEC-117, PLAT-008, JRN-007, PLAT-001  ·  **Périmètre :** Pilote 1 (à confirmer)  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Le panneau « Statistics » propose trois onglets « Project », « Allocation », « Compliance » ; « Project » est ouvert par défaut.
2. Chaque bloc commence par une phrase calculée, chiffres en gras, puis le graphique ou la liste qui la justifie.
3. Chaque chiffre est accompagné de son unité (requirements, assignments, systems, answers, risks…).
4. Cliquer une ligne ou un segment ouvre l'écran qui porte ce travail (Allocation, Compliance, Team casting, Q&A, Risks, Documents & versions).
5. Un bloc sans donnée affiche une phrase qui le dit (ex. « No Not compliant verdict yet. ») au lieu d'un graphique vide ou de valeurs d'exemple.
6. Aucun score de santé, feu tricolore ni pourcentage global unique n'apparaît.
Écart maquette : une partie des chiffres vient de copies écrites à la main ; sans visite préalable de Compliance, l'onglet Compliance affiche « Counted from Compliance — open it once… ».

### US-STAT-02 — Ne mesurer aucune personne
**Carte :** En tant que contributeur, je veux qu'aucune statistique ne compte, ne classe ni ne compare mon activité personnelle, afin que l'outil respecte le droit du travail et la protection des données.
**Conversation :** C'est une décision d'ordre social, pas un choix d'affichage (DEC-118) : un classement nominatif de l'activité des salariés relève de l'information-consultation du CSE (France), de la codécision du Betriebsrat (Allemagne) et du RGPD. Chaque action compte pour le système sur lequel elle porte, quel qu'en soit l'auteur. Les noms restent seulement là où le travail l'exige : qui relancer pour une réponse en retard, qui a renvoyé une exigence, qui a créé un risque, qui est staffé. Les mesures de l'IA ne sont pas non plus au tableau de bord (DEC-117).
**Maquette :** Tableau de bord — `dashboard-et-config.html` (route `#dashboard`), Statistics Panel (tous onglets) et carte « Answers by system ».
**Règles :** DEC-118, DEC-117, PLAT-008  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Aucun bloc des statistiques ni du tableau de bord n'affiche de compte, de classement, de taux ou de retard par personne.
2. L'activité et les réponses sont comptées par système, ou par sous-système sur un tender à un seul système.
3. « Active this week » se dit d'un système ou d'un sous-système, jamais d'une personne.
4. Un nom n'apparaît que dans quatre cas : la personne à relancer sur une réponse en retard, l'auteur d'un renvoi pour réallocation, le créateur d'un risque, la personne staffée dans l'équipe.
5. Aucun taux de correction ni mesure de qualité de l'IA n'apparaît au tableau de bord.
6. Aucune statistique par personne n'est calculée ni exposée par le serveur, y compris par requête directe.

### US-STAT-03 — Suivre les dates clés et le rythme du tender
**Carte :** En tant que chef de projet, je veux voir les dates clés du tender et la courbe des exigences allouées et répondues, avec ce que donne le rythme de la semaine, afin de savoir si l'on finira avant la soumission.
**Conversation :** La projection prolonge en ligne droite le rythme des 7 derniers jours ; elle se dit « à ce rythme », jamais comme un plan (PLAT-008 « Trajectoire »). Les dates : réception du tender, cut-off des questions, réponses attendues du client, soumission, aujourd'hui ; les deux dates du client sont facultatives (QA-008). La courbe exige un historique de l'avancement que la plateforme doit conserver.
**Maquette :** Tableau de bord — `dashboard-et-config.html` (route `#dashboard`), Statistics Panel › Project › « Timeline » (Key Dates List, Progress Trend Chart).
**Règles :** PLAT-008, DEC-117, QA-008, PLAT-001  ·  **Périmètre :** Pilote 1 (à confirmer)  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. La liste affiche dans l'ordre chronologique « Tender received », « Q&A cut-off », « Client answers expected », « Submission » et « Today » ; une date passée est marquée passée, une date à venir porte « in N days », une date facultative non renseignée n'apparaît pas.
2. La courbe trace le % d'exigences allouées et le % d'exigences répondues depuis la réception jusqu'à la soumission, avec les repères « Today » et « Submission ».
3. Une ligne pointillée prolonge chaque courbe au rythme des 7 derniers jours, jusqu'à 100 % ou jusqu'à la soumission.
4. La phrase dit, pour l'allocation puis pour les réponses, la date atteinte « At this week's pace », avec les jours d'avance ou de retard sur la soumission, « complete » à 100 % et « not moved this week » si le rythme est nul.
5. Aucun objectif, aucune ligne de plan ni date cible n'est tracé : seule la projection, nommée comme telle.
6. Les points passés de la courbe sont lus dans l'historique enregistré et restent identiques d'une ouverture à l'autre et pour tous les utilisateurs.
Écart maquette : l'historique est écrit à la main ; le point d'aujourd'hui vient d'une copie, pas des écrans.
Point ouvert : historique et formules (PLAT-008 « à compléter ») ; origine des dates de cut-off et de réponse du client (saisies à la création, dans les paramètres ou lues dans les documents — non tranché).

### US-STAT-04 — Voir les systèmes les plus actifs de la semaine
**Carte :** En tant que chef de projet, je veux voir quels systèmes ont fait avancer le tender ces 7 derniers jours, afin de repérer où le travail avance et où il stagne.
**Conversation :** L'activité compte, sur 7 jours glissants, les exigences validées dans Allocation (une fois par exigence), les réponses données (une fois par affectation), les commentaires et les questions, chacune pour le système sur lequel elle porte, quel qu'en soit l'auteur (DEC-118). Les modifications de champ ne comptent pas : un classement de clics récompenserait l'agitation, pas le travail. Sur un tender à un seul système (SIG), on classe ses sous-systèmes. Source : le journal d'activité ([US-X-01](16-transverse.md#us-x-01--consulter-le-journal-dactivité-dune-exigence)).
**Maquette :** Tableau de bord — `dashboard-et-config.html` (route `#dashboard`), Statistics Panel › Project › « Most active this week » (Leaderboard Row).
**Règles :** PLAT-008, DEC-117, DEC-118, DOM-011  ·  **Périmètre :** Pilote 1 (à confirmer)  ·  **Variantes :** Toutes (SIG : par sous-système)
**Critères d'acceptation :**
1. L'en-tête du bloc indique la période « last 7 days · <date> – <date> ».
2. La phrase dit le nombre total d'actions de la semaine, l'écart en % avec la semaine précédente et le système en tête, avec ses sous-systèmes les plus actifs.
3. Chaque ligne montre un système, son total et la part validations Allocation / réponses / commentaires et questions.
4. Une exigence validée deux fois ou une affectation répondue deux fois dans la semaine ne compte qu'une fois.
5. Modifier un champ (ABS, classe, personne…) ne change aucun compte.
6. Sur un tender SIG, les lignes sont les sous-systèmes du système unique et la phrase dit lequel est en tête.
Écart maquette : la semaine est écrite à la main ; seules les validations et les verdicts de la session s'y ajoutent.
Point ouvert : « sous-système » = périmètres staffés du casting (DEC-118) contre codes vers lesquels un Turnkey répartit (DEC-046, DEC-058) ; historique nécessaire (PLAT-008).

### US-STAT-05 — Voir l'équipe du tender
**Carte :** En tant que chef de projet, je veux voir en un bloc l'équipe de gestion, les managers de système, les contributeurs et les systèmes sans personne, afin de savoir si le tender est staffé.
**Conversation :** Un système sans manager est ordinaire (« contributors only ») ; un système n'est un trou que s'il n'a personne (DEC-124). Les noms y figurent parce que la personne staffée est l'une des exceptions de DEC-118. Le casting lui-même est décrit dans US-TEAM.
**Maquette :** Tableau de bord — `dashboard-et-config.html` (route `#dashboard`), Statistics Panel › Project › « The team » (Team Role Row, Avatar Stack), lien « Team casting → ».
**Règles :** DEC-124, DEC-118, DEC-102, ACC-001, ACC-008, PLAT-008  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes (SIG : par sous-système)
**Critères d'acceptation :**
1. La phrase dit combien de personnes travaillent sur le tender, sur combien de systèmes (de sous-systèmes sur un tender SIG), et sur combien d'entre eux le travail a bougé cette semaine.
2. Une ligne « Project management » nomme les membres de l'équipe de gestion.
3. Une ligne compte les managers de système et dit « no manager on <codes> — contributors only » pour les systèmes sans manager, sans le présenter comme un défaut.
4. Une ligne compte les contributeurs et les systèmes couverts, et signale « no contributor on <codes> yet » pour un système sans personne, en menant à Team casting.
5. Une jauge « Systems active this week » affiche N / M (« Sub-systems » sur un tender SIG).
6. « Team casting → » ouvre l'écran de casting.
Écart maquette : le casting n'est ni persisté ni partagé avec les autres écrans.

### US-STAT-06 — Voir où en sont les exigences dans Allocation
**Carte :** En tant que chef de projet, je veux voir la répartition des exigences entre Incomplete, To review, To validate et Allocated, afin de savoir combien de travail d'allocation reste.
**Conversation :** Ce sont les statuts d'Allocation (voir US-ALM). Les titres et blocs d'information n'ont pas de statut et n'entrent pas dans le compte (DEC-073). Un système sans modèle part vide, donc Incomplete (DEC-103).
**Maquette :** Tableau de bord — `dashboard-et-config.html` (route `#dashboard`), Statistics Panel › Allocation › « Where the requirements are » (Stacked Bar).
**Règles :** DEC-073, DEC-103, DEC-098, PLAT-008  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. La phrase dit « N of M requirements allocated » puis combien sont prêtes à valider, à revoir et encore incomplètes.
2. Une barre empilée montre les quatre statuts dans l'ordre Incomplete, To review, To validate, Allocated, avec une légende : nombre et %.
3. Le total M est celui de la carte Allocation et de l'en-tête du tableau de bord.
4. Aucun titre ni bloc d'information n'est compté.
5. Cliquer la barre ouvre Allocation.
Écart maquette : la barre lit une copie écrite à la main (14 exigences), qui peut différer de la carte Allocation.
Point ouvert : place du statut « Reassignment requested » d'un Turnkey (DEC-104) dans cette barre (non écrit).

### US-STAT-07 — Voir l'allocation par système, avec qui y est staffé
**Carte :** En tant que chef de projet, je veux voir pour chaque système combien de ses exigences sont allouées et qui y travaille, afin de repérer le système en retard ou sans personne.
**Conversation :** Le bloc réunit la charge par système et les trous de casting : la ligne montre le manager, ou le nombre de contributeurs quand il n'y en a pas ; seul un système sans personne est signalé (DEC-124). Un tender SIG n'a qu'un système : le bloc s'efface et « Sent back for reallocation » prend la largeur (TYPE-T08).
**Maquette :** Tableau de bord — `dashboard-et-config.html` (route `#dashboard`), Statistics Panel › Allocation › « By system, with who is on it » (System Manager Row).
**Règles :** DEC-124, DEC-118, TYPE-T08, PLAT-008  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Turnkey (masqué sur SIG)
**Critères d'acceptation :**
1. La phrase nomme le système qui a le plus d'exigences restant à allouer (« X of Y, with <manager ou N contributors> ») puis les systèmes sans personne.
2. Chaque ligne affiche le code du système, son manager, « N contributors » avec « no manager », ou « Nobody staffed yet », puis une barre allouées / à valider et « allouées/total ».
3. Les lignes sont triées du plus grand reste à allouer au plus petit.
4. Une ligne sans personne ouvre Team casting ; les autres ouvrent Allocation.
5. Une note compte les exigences pas encore routées vers un système (« N requirements not routed to a system yet »).
6. Sur un tender SIG, le bloc n'est pas affiché.

### US-STAT-08 — Voir les exigences renvoyées pour réallocation
**Carte :** En tant que chef de projet, je veux voir combien d'exigences les systèmes ont renvoyées, pourquoi et ce qui a été décidé, afin de juger la qualité de l'allocation et de trancher ce qui attend.
**Conversation :** Un renvoi (« not mine ») est le signe le plus clair qu'une allocation mérite un second regard. Trois motifs : bon système mais mauvaise personne, mauvais système, système non concerné (ALLOC-013). Le nom de qui a renvoyé reste affiché, exception prévue par DEC-118. La décision se prend dans Allocation (voir US-ALM).
**Maquette :** Tableau de bord — `dashboard-et-config.html` (route `#dashboard`), Statistics Panel › Allocation › « Sent back for reallocation » (Reallocation Breakdown).
**Règles :** ALLOC-013, CONF-011, PLAT-008, DEC-118  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. La phrase dit « N requirements sent back by a system so far » puis combien ont été réallouées, maintenues et attendent une décision.
2. Trois chiffres « reallocated », « kept as allocated », « to decide » ; « to decide » ouvre Allocation quand il n'est pas nul.
3. Une rubrique « Why » compte les renvois par motif : « Right system, wrong person », « Wrong system », « This system doesn't apply here ».
4. Une rubrique « Latest » montre les trois derniers renvois : exigence, système, personne qui l'a renvoyée, date et décision.
5. Sans aucun renvoi, le bloc affiche « Nothing sent back so far — every system kept what it was given. ».
Écart maquette : les renvois déjà décidés sont écrits à la main ; seuls ceux de la session sont réels.
Point ouvert : PLAT-008 demande aussi un compte « par demandeur », qui mesurerait des personnes, contraire à DEC-118 — à réarbitrer.

### US-STAT-09 — Voir le travail invalidé par une nouvelle version
**Carte :** En tant que chef de projet, je veux voir combien de réponses de contributeurs les nouvelles versions ont rouvertes, afin de mesurer le travail à refaire.
**Conversation :** Une nouvelle version qui modifie une exigence rouvre ses verdicts dans Compliance (DEC-016, DEC-122, LIFE-007). Le bloc n'existe que si ce nombre n'est pas nul.
**Maquette :** Tableau de bord — `dashboard-et-config.html` (route `#dashboard`), Statistics Panel › Allocation › « Work invalidated by a new version ».
**Règles :** DEC-122, DEC-016, LIFE-007, PLAT-008  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Le bloc n'apparaît que si au moins une réponse a été rouverte par une nouvelle version sur ce tender.
2. Il affiche « N contributor answers reopened by new versions » suivi des exigences concernées.
3. N est la somme des réponses rouvertes par toutes les versions téléversées, égale à ce que Compliance a rouvert.
4. Cliquer le bloc ouvre Documents & versions.
Point ouvert : PLAT-008 renvoie le « travail à revoir » à OPEN-07 (correspondance des exigences entre versions, fusion / scission).

### US-STAT-10 — Voir la progression vers le client
**Carte :** En tant que chef de projet, je veux voir ce que le client recevra à ce jour et où en est chaque étape qui y mène, afin de savoir combien d'exigences ne sont pas encore réglées.
**Conversation :** Quatre étapes : affectation, conformité interne, Not compliant documenté (lié à un risque), conformité externe (SPEC-risks §9 tel qu'amendé). La conformité externe est dérivée de la stratégie d'écart (DEC-106) ; ce qui n'est pas encore réglé est toujours montré, jamais omis (PLAT-008 « Profil de conformité »). Un risque est attendu sur tout Not compliant, SIG compris (DEC-109) ; un risque n'a ni poids ni statut (DEC-113).
**Maquette :** Tableau de bord — `dashboard-et-config.html` (route `#dashboard`), Statistics Panel › Compliance › « Progress to the client » (Progress Sequence).
**Règles :** PLAT-008, DEC-106, DEC-108, DEC-109, DEC-113, DEC-117, CONF-029  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. La phrase dit « So far the client will be told Compliant on N requirements and Not compliant on K — R of M are not settled yet ».
2. « Assigned » affiche le % et « X of Y assignments ».
3. « Internal compliance » affiche le % d'affectations répondues et le nombre de Not compliant.
4. « Not compliant logged » affiche le % de Not compliant liés à au moins un risque (« X of Y linked to a risk ») et reste signalé tant qu'il n'atteint pas 100 %.
5. « External compliance » affiche le % d'exigences réglées pour le client (Compliant ou Not compliant) et le nombre encore Pending.
6. Chaque étape ouvre l'écran qui la fait avancer : Allocation pour « Assigned », Compliance pour les autres.
Point ouvert : dénominateurs et formules (PLAT-008 « à compléter »).

### US-STAT-11 — Suivre les réponses par système et leurs retards
**Carte :** En tant que chef de projet, je veux voir pour chaque système les réponses confiées, rendues et en retard, afin de savoir où relancer.
**Conversation :** Une réponse est en retard quand l'affectation attend son contributeur depuis 5 jours ou plus (PLAT-008) ; c'est une statistique, pas un statut de Compliance, qui n'a plus d'« overdue » (DEC-078). Aucun nom dans ce bloc : la personne à relancer est nommée dans « What the open requirements are waiting on » ([US-STAT-12](#us-stat-12--voir-ce-quattendent-les-exigences-encore-ouvertes)) et dans « What needs you now » ([US-DASH-10](13-tableau-de-bord.md#us-dash-10--voir-les-réponses-en-retard-et-les-not-compliant-à-documenter)). Tender SIG : par sous-système.
**Maquette :** Tableau de bord — `dashboard-et-config.html` (route `#dashboard`), Statistics Panel › Compliance › « Answers by system » (System Answers Row).
**Règles :** PLAT-008, DEC-118, DEC-078, DEC-087, TYPE-T08  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes (SIG : par sous-système)
**Critères d'acceptation :**
1. La phrase dit « X of Y answers in » puis « N answers overdue, in <systèmes> » ou « none overdue ».
2. Chaque ligne affiche le système, une barre, « répondues/confiées », puis « N late · Dd » (D = âge du plus ancien retard), « ✓ all in » ou « N open ».
3. Les systèmes en retard viennent d'abord, du plus ancien retard au plus récent, puis les autres par taux de réponse.
4. Une affectation qui attend le client ou une décision de réallocation n'est jamais comptée en retard.
5. Aucun nom de personne n'apparaît dans le bloc ; une ligne ouvre Compliance.
6. Sur un tender SIG, le titre devient « Answers by sub-system » et les lignes sont les sous-systèmes.
Écart maquette : chiffres écrits à la main ; les retards sont une liste fixe, pas un calcul d'âge.
Point ouvert : borne « âge ≥ 5 jours » (Réponses par système) contre « au-delà de 5 jours » (Attente) dans PLAT-008, et lien avec le réglage « Overdue threshold » ([US-CFG-05](15-configuration.md#us-cfg-05--régler-le-seuil-de-retard-et-la-cadence-des-relances)) ; double sens de « sous-système ».

### US-STAT-12 — Voir ce qu'attendent les exigences encore ouvertes
**Carte :** En tant que chef de projet, je veux voir sur quoi attend chaque exigence sans réponse consolidée, chacune dans une seule file, afin de savoir qui doit agir : moi, le client ou un contributeur.
**Conversation :** Chaque exigence ouverte est rangée dans une seule file, dans cet ordre de priorité : renvoyée pour réallocation (décision du chef de projet), puis en attente du client (Q&A), puis chez un contributeur, sinon non affectée (PLAT-008 « Attente », DEC-117). Le nom du contributeur n'apparaît que pour le retard le plus ancien, à relancer (DEC-118).
**Maquette :** Tableau de bord — `dashboard-et-config.html` (route `#dashboard`), Statistics Panel › Compliance › « What the open requirements are waiting on » (Waiting Queue Row, Stacked Bar).
**Règles :** PLAT-008, DEC-117, DEC-118, DEC-092  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. La phrase dit « N requirements still open », puis combien de celles qui sont chez un contributeur sont en retard et combien attendent le client.
2. Quatre files au plus, chacune avec son compte — « On your decision », « On the client », « On a contributor », « Not assigned yet » ; une file vide n'est pas affichée.
3. Une exigence n'est comptée que dans une file, selon l'ordre réallocation → client → contributeur → non affectée ; la somme des files égale N.
4. « On a contributor » dit combien sont en retard, l'âge du plus ancien et le nom de sa personne ; « On the client » dit l'âge de la plus ancienne question et la date attendue des réponses du client.
5. « On your decision » cite chaque exigence avec son système et la personne qui l'a renvoyée ; « Not assigned yet » cite les exigences sans personne pour répondre.
6. Chaque file ouvre son écran (Allocation, Q&A ou Compliance) ; sans exigence ouverte, le bloc affiche « Every requirement has its answer. ».
Écart maquette : l'ancienneté des questions est écrite à la main.
Point ouvert : ranger « On the client » avant « On a contributor » alors qu'une question ne bloque rien (DEC-092) et que Compliance met d'abord en avant ce que doit le contributeur (DEC-125) — règle PLAT-008 antérieure, non réarbitrée.

### US-STAT-13 — Voir les Not compliant par stratégie d'écart
**Carte :** En tant que chef de projet, je veux voir comment les Not compliant se répartissent entre les stratégies d'écart, y compris ceux qui n'en ont pas encore, afin de savoir ce qui reste à documenter.
**Conversation :** Après un Not compliant, le responsable de l'affectation choisit une stratégie ; sans stratégie, l'affectation est signalée « Strategy missing » et l'externe reste Pending, sans blocage (DEC-108). Les stratégies sont celles du tender, écrites dans les paramètres ([US-RSK-01](10-risques.md#us-rsk-01--écrire-les-stratégies-décart-du-tender)) ; leur usage est décrit dans US-RSK.
**Maquette :** Tableau de bord — `dashboard-et-config.html` (route `#dashboard`), Statistics Panel › Compliance › « Not compliant by gap strategy » (Stacked Bar).
**Règles :** DEC-108, DEC-110, DEC-105, CONF-029  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. La phrase dit « N Not compliant answers » puis combien restent sans stratégie, ou « each with its strategy ».
2. Une barre empilée montre un segment par stratégie du tender, nommé comme dans les paramètres, plus « Strategy missing ».
3. Renommer une stratégie dans les paramètres renomme son segment.
4. Sans aucun Not compliant, le bloc affiche « No Not compliant verdict yet. ».
5. Cliquer la barre ouvre Compliance.

### US-STAT-14 — Voir les risques du tender et leur réutilisation
**Carte :** En tant que chef de projet, je veux voir combien de risques compte le tender, combien de fois ils sont liés et lesquels servent le plus, afin de vérifier que les risques sont réutilisés plutôt que recréés.
**Conversation :** Un risque n'est que sa justification (trois phrases) et ses liens ; il appartient au tender, pas à un système (DEC-113, DEC-114). Pas de poids, de statut ouvert / fermé ni de matrice poids × stratégie : ces statistiques de SPEC-risks §9 sont abandonnées. Le créateur d'un risque reste nommé, exception prévue par DEC-118.
**Maquette :** Tableau de bord — `dashboard-et-config.html` (route `#dashboard`), Statistics Panel › Compliance › « Risks » (Risk Summary Row).
**Règles :** DEC-113, DEC-114, DEC-105, DEC-118  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. La phrase dit « N risks in the list, linked K times to Not compliant answers », puis combien sont partagés par plusieurs exigences ou « none shared yet ».
2. Les quatre risques les plus liés s'affichent avec leur ID, le début de leur « There is a risk that… », leur créateur et « ×n ».
3. « + N more in the list » apparaît quand il y en a davantage ; une ligne ouvre la page Risks.
4. Aucun poids, statut, nombre de risques ouverts ni matrice n'apparaît.
5. Sans aucun risque, le bloc dit qu'il n'y en a pas encore et qu'ils se créent dans Compliance, sur chaque Not compliant.

## Couverture
- Règles couvertes : PLAT-008 → [US-STAT-01](#us-stat-01--lire-les-statistiques-par-onglet-une-phrase-puis-le-chiffre) à [US-STAT-14](#us-stat-14--voir-les-risques-du-tender-et-leur-réutilisation) (« Profil de conformité » → [US-STAT-10](#us-stat-10--voir-la-progression-vers-le-client) ; « Attente des exigences ouvertes » et « Blocage client » → [US-STAT-12](#us-stat-12--voir-ce-quattendent-les-exigences-encore-ouvertes) ; « Casting incomplet » → [US-STAT-05](#us-stat-05--voir-léquipe-du-tender), [US-STAT-07](#us-stat-07--voir-lallocation-par-système-avec-qui-y-est-staffé) ; « Travail à revoir » → [US-STAT-09](#us-stat-09--voir-le-travail-invalidé-par-une-nouvelle-version) ; « Trajectoire » → [US-STAT-03](#us-stat-03--suivre-les-dates-clés-et-le-rythme-du-tender) ; « Activité de la semaine » → [US-STAT-04](#us-stat-04--voir-les-systèmes-les-plus-actifs-de-la-semaine) ; « Réponses par système » → [US-STAT-11](#us-stat-11--suivre-les-réponses-par-système-et-leurs-retards) ; « Réallocations » → [US-STAT-08](#us-stat-08--voir-les-exigences-renvoyées-pour-réallocation) ; unité annoncée et refus d'un indicateur composite → [US-STAT-01](#us-stat-01--lire-les-statistiques-par-onglet-une-phrase-puis-le-chiffre)) ; JRN-007 → [US-STAT-01](#us-stat-01--lire-les-statistiques-par-onglet-une-phrase-puis-le-chiffre) ; PLAT-001 → [US-STAT-01](#us-stat-01--lire-les-statistiques-par-onglet-une-phrase-puis-le-chiffre), [US-STAT-03](#us-stat-03--suivre-les-dates-clés-et-le-rythme-du-tender) ; DOM-011 → [US-STAT-04](#us-stat-04--voir-les-systèmes-les-plus-actifs-de-la-semaine).
- Autres règles mises en œuvre : TYPE-T08 → [US-STAT-07](#us-stat-07--voir-lallocation-par-système-avec-qui-y-est-staffé), [US-STAT-11](#us-stat-11--suivre-les-réponses-par-système-et-leurs-retards) ; ALLOC-013, CONF-011 → [US-STAT-08](#us-stat-08--voir-les-exigences-renvoyées-pour-réallocation) ; LIFE-007 → [US-STAT-09](#us-stat-09--voir-le-travail-invalidé-par-une-nouvelle-version) ; CONF-029 → [US-STAT-10](#us-stat-10--voir-la-progression-vers-le-client), [US-STAT-13](#us-stat-13--voir-les-not-compliant-par-stratégie-décart) ; QA-008 → [US-STAT-03](#us-stat-03--suivre-les-dates-clés-et-le-rythme-du-tender) ; ACC-001, ACC-008 → [US-STAT-05](#us-stat-05--voir-léquipe-du-tender).
- Non couvertes, avec la raison : PLAT-008 « Corrections IA » — hors tableau de bord par DEC-117, couverte par [US-CFG-12](15-configuration.md#us-cfg-12--consulter-la-qualité-de-lia-dans--ai-feedback-) ; PLAT-008 « Réallocations… par demandeur » — point ouvert, contraire à DEC-118 ([US-STAT-08](#us-stat-08--voir-les-exigences-renvoyées-pour-réallocation)) ; SPEC-risks §9 « Open risks », « Risks by weight », « Weight × strategy » — caduques (DEC-113) ; vue VIP comparative entre tenders de l'ancienne spec — non reprise (VIP non détaillé, OPEN-02) ; PLAT-001 à PLAT-007, DOM-013 (hors usages cités) — couverts par l'épopée US-X.
