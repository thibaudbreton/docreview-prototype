<!-- Généré depuis le backlog du 10 octobre 2026 ; voir README.md pour les conventions. -->
# Transverse et plateforme (US-X)

Ce qui vaut pour tous les écrans et toutes les étapes : le journal d'activité de chaque exigence, partagé entre Allocation et Compliance ; la persistance, la connexion SSO et les droits contrôlés par le serveur ; l'audit des changements humains et machine ; les échanges Excel et DOORS ; les notifications ; la tenue à 100 000 lignes et 10 utilisateurs simultanés ; les états d'écran de production (chargement, vide, absence de droit, échec, conflit) ; le sens des couleurs. Stack communiquée : React et Azure, sans services arrêtés (PLATFORM). Termes : *journal d'activité* = la trace, par exigence, de qui a changé quoi, quand, avant → après ; *audit* = la même trace côté serveur pour toutes les données, traitements de l'IA compris. Décrits ailleurs : l'état personnel côté serveur — brouillons et mises de côté, DEC-090 — dans [US-CMP-13](09-compliance.md#us-cmp-13--retrouver-son-brouillon-de-verdict) et [US-CMP-14](09-compliance.md#us-cmp-14--mettre-une-affectation-de-côté) ; le traitement partiel et la reprise après incident dans [US-CAP-11](04-capture-ia.md#us-cap-11--reprendre-un-traitement-interrompu-sans-doublon) ; la recherche et le filtrage sur tout le jeu dans US-TAB. Les rôles Admin et VIP ne sont pas détaillés (OPEN-02) : aucune story ne les décrit.

### US-X-01 — Consulter le journal d'activité d'une exigence
**Carte :** En tant que contributeur, je veux voir tout ce qui est arrivé à une exigence — qui a changé quoi, quand, avant et après —, afin de comprendre une décision sans interroger mes collègues.
**Conversation :** Un seul journal par exigence, le même dans Allocation et dans Compliance (onglet « Activity » du panneau de détail). Ce qu'Allocation y écrit est fixé dans [US-ALM-35](05-allocation.md#us-alm-35--inscrire-les-actions-dallocation-au-journal-de-lexigence) (sous-systèmes, réassignations, relances avec le modèle utilisé — y compris un modèle emprunté, DEC-043 — et « same result », DEC-091, statuts, chaîne, personnes, type, classe) ; Compliance y écrit verdicts, stratégie, liens de risque, correction du tender manager, déclaration au client, question, renvoi, relance et réouverture par une version (voir US-CMP, US-RSK). Cette story fixe la lecture du journal. Aucune règle écrite ne va au-delà de DOM-011 et PLAT-003.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`) et Compliance — `compliance.html` (route `#compliance`), panneau de détail › onglet « Activity » (Activity Timeline, Activity Timeline Entry).
**Règles :** DOM-011, PLAT-003, ALLOC-014, DEC-043, DEC-091, DEC-122, DEC-125, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. L'onglet « Activity » d'une exigence affiche les mêmes entrées dans Allocation et dans Compliance, de la plus récente à la plus ancienne.
2. Chaque entrée indique son auteur — une personne, ou le traitement automatique (capture, nouvelle version, modèle) —, la date et l'heure, et ce qui a changé.
3. Une entrée qui modifie une valeur montre l'ancienne et la nouvelle (« avant → après »).
4. Les jalons « Captured », « Allocated », « Answered » et « Declared to the client » sont marqués comme tels quand ils arrivent.
5. Les filtres « All », « Status », « Allocation », « Compliance », « Comments » affichent le nombre d'entrées de chaque catégorie et ne gardent que la catégorie choisie ; une catégorie vide dit « Nothing in this category yet. ».
Écart maquette : l'auteur d'un changement détecté est la personne qui regarde (« View as » compris) ; les historiques de démonstration sont écrits à la main.
Point ouvert : liste exacte des événements tracés, rétention et droits de lecture du journal (DOM-011, PLAT-003, OPEN-11).

### US-X-02 — Commenter une exigence
**Carte :** En tant que contributeur, je veux laisser sur une exigence un commentaire visible de toute l'équipe dans les deux étapes, afin de partager une information au bon endroit plutôt que par e-mail.
**Conversation :** Le champ de commentaire est au bas de l'onglet « Activity » ; un commentaire entre au journal de l'exigence, catégorie Comments ([US-X-01](#us-x-01--consulter-le-journal-dactivité-dune-exigence)). Il alimente « Recent comments » du tableau de bord ([US-DASH-12](13-tableau-de-bord.md#us-dash-12--lire-les-derniers-commentaires-du-tender)) et compte pour le sous-système de l'exigence dans l'activité de la semaine ([US-STAT-04](14-statistiques.md#us-stat-04--voir-les-sous-systèmes-les-plus-actifs-de-la-semaine)), jamais pour son auteur (DEC-118). Taper « @ » propose les personnes du tender ; la personne mentionnée est prévenue, même hors de son sous-système (DEC-132, [US-X-17](#us-x-17--recevoir-tout-de-suite-ce-qui-mest-adressé-ou-que-jattends)).
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`) et Compliance — `compliance.html` (route `#compliance`), onglet « Activity » › champ « Comment… ».
**Règles :** DOM-011, PLAT-003, DEC-118, DEC-132, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Écrire un texte puis Entrée ou « ↑ » publie le commentaire et affiche « Comment posted » ; le champ se vide.
2. Le commentaire apparaît dans le journal avec son auteur, sa date et son texte, dans Allocation comme dans Compliance.
3. Un commentaire vide n'est pas publié.
4. Le nombre de commentaires de l'exigence, partout où il s'affiche, augmente de un.
5. Le commentaire apparaît dans « Recent comments » du tableau de bord à sa prochaine ouverture.
6. Taper « @ » propose les personnes du tender ; un commentaire publié avec une mention prévient la personne mentionnée ([US-X-17](#us-x-17--recevoir-tout-de-suite-ce-qui-mest-adressé-ou-que-jattends)).
Point ouvert : droit de commenter une exigence hors de son sous-système, que DEC-100 met en lecture seule ; modifier ou supprimer un commentaire.

### US-X-03 — Retrouver tout le travail après reconnexion
**Carte :** En tant que contributeur, je veux retrouver après une déconnexion ou un redémarrage tout ce qui a été saisi sur le tender, afin de ne jamais refaire un travail perdu.
**Conversation :** Tous les objets et états sont persistés : tenders, documents et versions, exigences, allocations, affectations, réponses, stratégies, risques, questions, colonnes personnalisées, paramètres et journal (PLAT-001). Un objet n'existe qu'une fois : tous les écrans le lisent à la même source, jamais dans des copies. La maquette garde tout en mémoire et perd tout au rechargement : ce mécanisme n'est pas à reproduire.
**Maquette :** non maquetté (la maquette n'a aucune persistance).
**Règles :** PLAT-001, JRN-001  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Une modification confirmée à l'écran est retrouvée identique après rechargement de la page, déconnexion ou redémarrage du serveur.
2. Une modification faite par une personne est vue par les autres membres du tender à leur chargement suivant.
3. Allocation, Compliance, le tableau de bord et les statistiques affichent la même valeur pour une même exigence au même moment.
4. Après reconnexion, l'utilisateur rouvre depuis « My tenders » le tender où il travaillait.
5. Le succès d'une modification n'est affiché qu'après confirmation de l'enregistrement par le serveur.
Écart maquette : rien n'est persisté ; chaque écran garde sa propre copie des données et les compteurs du tableau de bord sont écrits à la main.

### US-X-04 — Se connecter par SSO et n'accéder qu'à ses tenders
**Carte :** En tant que contributeur, je veux me connecter avec mon compte d'entreprise et ne voir que les tenders dont je suis membre, afin d'accéder à mon travail sans compte supplémentaire et sans voir les tenders des autres.
**Conversation :** SSO et droits par tender contrôlés côté serveur (PLAT-002). Être membre d'un tender — équipe de gestion ou staffing — ouvre la lecture de tout ce tender (DEC-012, ACC-007) ; aucun accès à un autre tender n'en est déduit (ACC-T09). Qui peut créer un tender reste à préciser (JRN-001).
**Maquette :** non maquetté (identité fournie par la démo ; avatar de l'en-tête — Header Avatar).
**Règles :** PLAT-002, ACC-007, ACC-T09, DEC-012, JRN-001  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. L'accès à Smart Req passe par l'authentification d'entreprise (SSO) ; aucun mot de passe propre à Smart Req n'est demandé.
2. L'avatar de l'en-tête affiche l'identité fournie par l'annuaire (nom, initiales).
3. « My tenders » ne liste que les tenders dont l'utilisateur est membre.
4. Ouvrir par son adresse un tender dont on n'est pas membre affiche un refus d'accès, sans aucun contenu ni compteur de ce tender.
5. Recherches, compteurs et exports ne renvoient jamais une donnée d'un tender dont l'utilisateur n'est pas membre.
Point ouvert : politique de création d'un tender (JRN-001) ; rôles Admin et VIP (OPEN-02) ; standards de sécurité (OPEN-11).

### US-X-05 — Faire respecter les droits du tender par le serveur
**Carte :** En tant que tender manager, je veux que les droits de chacun soient contrôlés par le serveur, pas seulement masqués à l'écran, afin qu'aucune modification interdite ne passe par un autre chemin.
**Conversation :** Un contributeur lit tout le tender mais ne modifie que son sous-système (DEC-012, ACC-007) ; il ne modifie ni le type ni la classe (DEC-086), ni rien sur une exigence dont aucun sous-système n'est le sien (DEC-100). La gestion globale — documents, relation client, validation de l'aiguillage Turnkey — appartient à l'équipe de gestion (ACCESS, DEC-104). Droits et consolidation se calculent par des règles métier, jamais par un modèle d'IA (AI-013). Le détail par écran est dans US-TEAM, US-ALM et US-CMP.
**Maquette :** non maquetté (la maquette ne contrôle les droits que dans l'écran ; « View as » est une démo).
**Règles :** PLAT-002, ACC-007, ACC-012, ACC-013, ACC-014, ACC-T04, ACC-T10, DEC-086, DEC-100, AI-013, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Une modification d'un autre sous-système envoyée par un contributeur en requête directe est refusée par le serveur avec un message de droit, et rien n'est enregistré.
2. Une modification de type ou de classe par un contributeur est refusée par le serveur, quel que soit le chemin (panneau, table, action groupée, vue Document, requête directe).
3. Les compteurs, la recherche et les exports d'un contributeur couvrent tout le tender en lecture, sans lui ouvrir d'action hors de son sous-système.
4. Une action groupée sur une sélection qui contient des exigences hors de son sous-système n'agit que sur les siennes et dit combien ont été écartées.
5. Chaque refus s'affiche avec sa raison, et l'action refusée n'apparaît jamais comme réussie.
Écart maquette : les refus ne sont simulés que dans l'interface.

### US-X-06 — Tracer tout changement, humain ou machine
**Carte :** En tant que tender manager, je veux que chaque changement de donnée, fait par une personne ou par un traitement automatique, soit tracé avec son auteur, sa date et ses valeurs avant et après, afin de pouvoir justifier une réponse au client et retrouver l'origine d'une erreur.
**Conversation :** Audit des changements humains et machine — identité, date, avant / après — et traçabilité des traitements de l'IA avec leur coût (PLAT-003, DOM-011). Le journal d'une exigence ([US-X-01](#us-x-01--consulter-le-journal-dactivité-dune-exigence)) en est la lecture fonctionnelle. Suivi de session, rétention et standards de sécurité sont à fournir (OPEN-11).
**Maquette :** non maquetté.
**Règles :** PLAT-003, DOM-011, AI-001, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Toute création, modification ou suppression d'une donnée métier enregistre l'auteur (personne ou traitement), la date et l'heure, l'objet concerné, l'ancienne et la nouvelle valeur.
2. Chaque traitement de l'IA (capture, traduction, caractérisation, dérivation, relance) enregistre le traitement ou modèle utilisé, l'élément traité (tender, document, version, exigence), l'heure et son coût.
3. Un changement fait par un traitement automatique se distingue, dans la trace, d'un changement humain.
4. La trace ne peut être ni modifiée ni supprimée depuis l'application.
5. Une relance ou une nouvelle version qui remplace des valeurs laisse les anciennes lisibles dans la trace.
Point ouvert : rétention, suivi de session et standards de sécurité (OPEN-11) ; unité et granularité du coût des traitements de l'IA.

### US-X-07 — Garder séparées la proposition de l'IA, la valeur retenue et la correction
**Carte :** En tant que tender manager, je veux que la proposition de l'IA, la valeur retenue par l'équipe et la correction restent distinctes, afin qu'un retraitement n'efface jamais en silence une décision humaine.
**Conversation :** DOM-013 (PROP) : conserver séparément la proposition IA, la valeur retenue et l'événement de correction ; une reprise de traitement ne doit pas effacer silencieusement une décision humaine (reprise après incident : [US-CAP-11](04-capture-ia.md#us-cap-11--reprendre-un-traitement-interrompu-sans-doublon)). Les relances voulues restent possibles : unitaire ou en masse (ALLOC-014, DEC-052), globale et annoncée (ALLOC-015), ciblée par une nouvelle version sur les exigences modifiées (LIFE-011). La confiance de l'IA ne s'affiche que tant que la valeur est la sienne (DEC-120).
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), panneau de détail (Confidence Level Badge, Derivation Chain).
**Règles :** DOM-013, AI-001, AI-011, DEC-120, LIFE-011, ALLOC-014, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Pour chaque champ proposé par l'IA (type, classe, sous-système routé, ABS, PBS, OBS), la proposition et sa confiance sont conservées à côté de la valeur retenue.
2. Corriger une valeur crée un événement de correction (qui, quand, proposition → valeur retenue) sans effacer la proposition.
3. Le niveau ou le pourcentage de confiance ne s'affiche que tant que la valeur affichée est celle de l'IA ; un choix humain n'en porte pas.
4. Une reprise automatique de traitement, par exemple après un incident, ne remplace aucune valeur retenue par un humain.
5. Seules une relance demandée par quelqu'un ou une nouvelle version qui modifie l'exigence renouvellent la proposition ; les anciennes valeurs restent au journal.
Point ouvert : modalités de reprise et de correspondance entre versions (OPEN-07, OPEN-09).

### US-X-08 — Exporter les exigences du tender
**Carte :** En tant que tender manager, je veux exporter les exigences d'un ou de tous les documents, avec les étapes et le format de mon choix, afin de les reprendre dans Excel ou dans DOORS.
**Conversation :** Le menu « Export ▾ » d'Allocation porte l'export du registre (DEC-084). L'export reprend ce que montrent les filtres de colonne et le filtre avancé, et l'annonce avant de produire le fichier. Le texte d'exigence part dans sa langue originale, les contributions en anglais (LANG-003) ; un contributeur exporte tout le tender en lecture, jamais au-delà (PLAT-002). Les colonnes personnalisées suivent [US-TAB-24](06-tables.md#us-tab-24--modifier-une-colonne-personnalisée) ; l'export de Compliance a ses propres options (US-CMP) ; l'export par document de Documents & versions est dans US-DOC.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), bouton « Export ▾ » › panneau « Export requirements » (Export Panel (header ad-hoc export)).
**Règles :** PLAT-004, PLAT-002, LANG-003, LIFE-004, DEC-084, UX-002, DEC-126  ·  **Périmètre :** Pilote 1 (à confirmer)  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Le panneau « Export requirements » propose le document (« All documents (N) » ou un seul) et annonce « N requirements — <filtres actifs> », ou « Nothing matches the current scope ».
2. « Include steps » propose « Capture », « Characterisation » et « Allocation » ; générer sans aucune étape est refusé (« Select at least one step to export »).
3. « Target format » propose Excel (.xlsx) et les formats DOORS 9 et DOORS Next retenus ; le fichier contient exactement les exigences annoncées, avec leur identifiant.
4. Générer quand rien ne correspond est refusé (« Nothing to export — the current filters match 0 requirements »).
5. Le texte d'exigence est exporté dans la langue originale du tender, ce que le panneau dit quand le tender n'est pas en anglais.
6. Les exigences sortent dans l'ordre du document, le même qu'à la lecture.
Écart maquette : aucun fichier n'est produit (message seulement) ; CSV et ReqIF sont proposés sans intégration.
Point ouvert : formats, correspondances et aller-retour DOORS à contractualiser (PLAT-004, OPEN-10, OPEN-12).

### US-X-09 — Importer un export DOORS comme document du tender
**Carte :** En tant que tender manager, je veux importer un module exporté de DOORS 9 ou de DOORS Next comme document du tender, afin de partir d'exigences déjà tenues dans DOORS.
**Conversation :** PLAT-004 prévoit l'import et l'export DOORS 9 et DOORS NG ; DEC-018 range les échanges DOORS parmi les formats pris en charge. L'ajout de document se fait à la création (US-NEW) ou dans Documents & versions (US-DOC) : cette story fixe ce que la plateforme accepte et garde. Il n'y a pas de connecteur direct à un serveur DOORS : son inclusion n'est pas confirmée (OPEN-12).
**Maquette :** non maquetté (la capture de démonstration est importée hors de l'application).
**Règles :** PLAT-004, DEC-018, DOM-012, AI-012, LANG-002, DEC-126  ·  **Périmètre :** Pilote 1 (à confirmer)  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Un fichier d'export DOORS 9 ou DOORS Next, dans un format convenu, est accepté là où l'on ajoute un document.
2. Le document importé suit la même chaîne que les autres : capture, traduction si besoin, caractérisation, allocation.
3. Chaque objet DOORS importé garde son identifiant DOORS comme référence de source, lisible depuis l'exigence.
4. Un fichier d'un format non pris en charge ou illisible est refusé avec un message qui cite les formats attendus, et rien n'est créé à moitié.
5. Aucune connexion directe à un serveur DOORS n'est proposée.
Point ouvert : formats exacts, correspondance des attributs DOORS et boucle aller-retour (OPEN-10, OPEN-12).

### US-X-10 — Recevoir les notifications dans l'application et par e-mail
**Carte :** En tant que contributeur ou tender manager, je veux être prévenu de ce qui change pour moi, et seulement de cela, afin de ne pas surveiller chaque écran sans être noyé sous les messages.
**Conversation :** Le [plan de notification](../current/NOTIFICATIONS.md) fait référence (DEC-127). Une notification est un événement adressé à une personne ; le travail en attente reste un état calculé, que montrent les écrans et le pied de la cloche ([US-DASH-15](13-tableau-de-bord.md#us-dash-15--lire-ce-qui-mattend-au-pied-de-la-cloche)). On ne prévient que la personne dont c'est le tour d'agir : la personne en charge (PIC) d'une affectation (DEC-087), tous les tender managers pour une décision qui leur revient (le premier qui tranche l'efface pour les autres), l'auteur d'une demande ou d'une question. Chaque événement du catalogue (NOTIFICATIONS, section 4) a un niveau : **A**, immédiat, envoyé par e-mail s'il n'est pas vu 10 minutes après ([US-X-17](#us-x-17--recevoir-tout-de-suite-ce-qui-mest-adressé-ou-que-jattends)) ; **B**, repris dans le résumé quotidien s'il n'est pas vu ([US-X-16](#us-x-16--recevoir-le-résumé-quotidien-par-e-mail)) ; **C**, dans la cloche seulement ([US-X-15](#us-x-15--ouvrir-ma-cloche-la-même-sur-tous-les-écrans)). Les réglages sont dans [US-X-18](#us-x-18--régler-mes-notifications). Le pilote ne sert que les événements de la création et de l'allocation (DEC-135) ; Compliance et Q&A ajoutent les leurs ensuite ([US-CMP-26](09-compliance.md#us-cmp-26--être-prévenu-de-ce-qui-bouge-dans-compliance), [US-CMP-24](09-compliance.md#us-cmp-24--relancer-le-contributeur-dune-affectation-due), [US-QA-09](11-qa.md#us-qa-09--lire-la-réponse-du-client-sous-sa-question)).
**Maquette :** intention dans `proposals/notifications/index.html` (matrice des événements, cloche, accueil, réglages) ; modèles d'e-mails dans `proposals/notifications/emails/`. Le prototype n'a encore qu'une cloche d'état par écran (Notifications Dropdown).
**Règles :** DEC-127, DEC-130, DEC-135, NOTIF-001 à NOTIF-005, NOTIF-009, NOTIF-023, NOTIF-024, PLAT-005, CONF-021, DEC-087, DEC-118, QA-003, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Chaque événement du catalogue crée une notification pour ses seuls destinataires, au niveau prévu ; dans le pilote : ajout à un tender, traitement terminé ou échoué, exigences à allouer, demande de réallocation ou sous-système manquant proposé, demande refusée ou approuvée, allocation complète, mention.
2. L'auteur d'une action n'en est jamais prévenu, même quand il agit pour un autre ; aucune notification ne propose à une personne une action qui lui est adressée à elle-même.
3. Un contributeur n'est prévenu que du travail de son sous-système, sauf d'une mention ; quand des exigences à allouer arrivent dans un sous-système, tous ses contributeurs le voient dans la cloche, et seuls ceux qui y sont staffés sans périmètre le retrouvent dans le résumé e-mail (DEC-130).
4. Quand un tender manager tranche une demande, la notification disparaît pour les autres tender managers, dans la cloche comme dans les e-mails pas encore partis.
5. Un retard, une échéance proche, une proposition de l'IA, un OBS faible ou une statistique ne créent jamais de notification ; Smart Req n'envoie jamais rien au client ni à un partenaire externe.
6. L'état « vu » d'une notification n'est montré à personne d'autre et n'entre dans aucune statistique ; aucun e-mail ne porte de pixel ni de lien de suivi.
Point ouvert : le mode d'envoi des e-mails (Microsoft Graph ou High Volume Email) et la boîte d'envoi, à fixer avec l'IT (DEC-136) ; la présentation du dispositif aux représentants du personnel avant le déploiement (DEC-118).

### US-X-11 — Travailler sur 100 000 lignes à dix en même temps
**Carte :** En tant que tender manager, je veux que les tables restent utilisables jusqu'à 100 000 lignes avec dix personnes connectées en même temps, afin de traiter les plus gros tenders sans attendre l'outil.
**Conversation :** Dimensionnement confirmé : jusqu'à 100 000 lignes, titres et blocs d'information compris, et 10 utilisateurs simultanés (DEC-023, PLAT-006). La rapidité est requise, mais l'ancienne cible P95 ≤ 300 ms n'est pas un engagement confirmé : les budgets mesurables (recherche, filtres, navigation, actions groupées) restent à fixer, les traitements de l'IA se mesurent à part (PLAT-007, OPEN-08). Recherche et filtres portent sur tout le jeu autorisé (UX-005, voir [US-TAB-02](06-tables.md#us-tab-02--déplier-une-exigence-en-lignes-par-sous-système-et-par-organisation) et [US-TAB-04](06-tables.md#us-tab-04--rechercher-une-exigence-par-son-identifiant-ou-son-texte)).
**Maquette :** non maquetté (la démo compte quelques centaines de lignes).
**Règles :** PLAT-006, PLAT-007, DEC-023, UX-005, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Un tender de 100 000 lignes s'ouvre dans Allocation et dans Compliance, et la table défile sans blocage.
2. Les compteurs d'un tender de 100 000 lignes (statuts, consolidation, statistiques) portent sur tout le jeu, pas sur la partie chargée.
3. Dix utilisateurs qui modifient le même tender en même temps voient chacun leurs modifications enregistrées, sans perte.
4. Un test de charge sur un jeu de 100 000 lignes et 10 sessions simultanées vérifie les budgets retenus avant la mise en service.
5. La durée des traitements de l'IA est mesurée et rapportée à part des temps d'écran.
Point ouvert : budgets chronométrés, portée exacte du jeu de 100 000 lignes et protocole de mesure (OPEN-08) ; sélection de toutes les pages et « Filter to Selection » à cette échelle (OPEN-13, UX-006).

### US-X-12 — Comprendre l'état d'un écran : chargement, vide, absence de droit
**Carte :** En tant que contributeur, je veux que chaque écran dise s'il charge, s'il n'a rien à montrer ou si je n'ai pas le droit d'y être, afin de ne jamais prendre un écran incomplet pour un résultat.
**Conversation :** États de production à concevoir pour chaque parcours (JOURNEYS, PROP) : chargement réel, aucun résultat, absence de droit ; la réussite n'est affichée qu'après confirmation réelle. Échec et conflit d'enregistrement : [US-X-13](#us-x-13--ne-rien-perdre-en-cas-déchec-ou-de-conflit-denregistrement) ; traitement partiel et reprise après incident : [US-CAP-11](04-capture-ia.md#us-cap-11--reprendre-un-traitement-interrompu-sans-doublon).
**Maquette :** non maquetté (quelques messages vides existent : Empty State Message, « Nothing waiting on you here. »).
**Règles :** JOURNEYS (états de production, PROP), PLAT-002, CONF-019  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Pendant un chargement, l'écran montre qu'il charge et n'affiche ni chiffre ni table vide comme s'ils étaient définitifs.
2. Une table ou une liste sans résultat le dit en une phrase et nomme les filtres actifs qui en sont la cause, avec un moyen de les retirer.
3. Un écran ou une action sans droit affiche un message qui le dit, sans montrer de contenu ni de compteur interdit.
4. Aucun message de réussite n'apparaît avant la confirmation du serveur.

### US-X-13 — Ne rien perdre en cas d'échec ou de conflit d'enregistrement
**Carte :** En tant que contributeur, je veux qu'un échec d'enregistrement ou une modification simultanée par un collègue ne fasse jamais disparaître ma saisie en silence, afin de ne pas perdre mon travail sans le savoir.
**Conversation :** Propositions de production : enregistrement concurrent sans perte silencieuse ; erreurs et conflits présentés sans annoncer une réussite ni perdre la saisie (PLATFORM, COMPLIANCE §Production, JOURNEYS). Le verrou métier du verdict n'existe plus (DEC-106) : ne pas le confondre avec la protection technique contre deux éditions simultanées.
**Maquette :** non maquetté.
**Règles :** JOURNEYS (PROP), PLATFORM (PROP), PLAT-001, DEC-106  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Quand un enregistrement échoue, un message le dit, la saisie reste dans le champ et l'utilisateur peut réessayer.
2. Après un échec, l'écran n'affiche pas la valeur comme enregistrée.
3. Quand une autre personne a modifié la même donnée depuis son ouverture, l'utilisateur en est averti avant que l'une des deux valeurs ne remplace l'autre, et voit les deux.
4. Aucune modification enregistrée n'est écrasée sans que son auteur et celui qui l'écrase le sachent.
5. Aucun verrou métier n'empêche de modifier un verdict : seule la protection contre les éditions simultanées s'applique.
Point ouvert : mode de résolution d'un conflit (dernière écriture avec avertissement, fusion, rechargement) non choisi.

### US-X-14 — Lire des couleurs qui gardent toujours le même sens
**Carte :** En tant que contributeur, je veux que le rouge et le vert gardent toujours le même sens et qu'aucun état ne repose sur la seule couleur, afin de ne jamais confondre une décoration avec un verdict.
**Conversation :** Le rouge de la marque est décoratif — la barre devant les titres de page — et jamais sur un élément cliquable ou porteur d'état, parce que le rouge signifie déjà « non conforme » (DEC-063). Vert et rouge sont réservés au verdict ; les statuts d'avancement ont d'autres couleurs. Les deux thèmes gardent ces sens ([US-CFG-10](15-configuration.md#us-cfg-10--choisir-son-thème-clair-ou-sombre)). Police de la marque, logo de l'entreprise dans l'en-tête et accent marine relèvent de la charte (DEC-063, DEC-115) et n'ont pas de story propre.
**Maquette :** tous les écrans — Page Title (barre rouge), Status Pill, colonne Compliance (✓ / ✕).
**Règles :** DEC-063, DEC-115  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Le rouge de la marque n'apparaît que comme marque décorative devant les titres de page, jamais sur un bouton, un lien, une pastille ou un statut.
2. Le vert et le rouge ne servent qu'aux verdicts Compliant et Not compliant ; « Answered » ou « Reassignment needed » ne sont ni verts ni rouges.
3. Chaque statut ou verdict porte aussi un libellé ou un symbole (✓ / ✕ dans la colonne Compliance), lisible sans la couleur.
4. Ces règles valent à l'identique en thème clair et en thème sombre.
Point ouvert : référentiel d'accessibilité à atteindre (contrastes, lecteur d'écran, navigation au clavier hors tables) — aucune règle écrite ; rouge exact de la marque à confirmer (DEC-063).

### US-X-15 — Ouvrir ma cloche, la même sur tous les écrans
**Carte :** En tant que contributeur ou tender manager, je veux une seule cloche qui me montre ce qui a changé pour moi, où que je sois dans Smart Req, afin de voir d'un coup d'œil s'il y a du nouveau sans faire le tour des écrans.
**Conversation :** Cette cloche remplace les cloches d'état de chaque écran (DEC-128) : son contenu dépend de la personne, jamais de l'écran. Elle est sur l'accueil, le tableau de bord, Allocation, Compliance, Documents & versions, Q&A et Risks ; l'assistant de création n'en a pas, c'est un parcours fermé. Son point ne signale que du nouveau, pas du travail en attente, sinon il resterait allumé en permanence sur un vrai tender ; ce qui attend tient en une ligne au pied du panneau ([US-DASH-15](13-tableau-de-bord.md#us-dash-15--lire-ce-qui-mattend-au-pied-de-la-cloche)). Le toast reste le retour de sa propre action : l'action d'un autre n'interrompt personne. La cloche garde 30 jours ; l'historique durable d'une exigence est son journal ([US-X-01](#us-x-01--consulter-le-journal-dactivité-dune-exigence)).
**Maquette :** intention dans `proposals/notifications/index.html` (« One bell, the same on every screen ») ; App Header › Icon Button cloche, Notification Dot, Notifications Dropdown, Notification Item.
**Règles :** DEC-128, DEC-127, NOTIF-010 à NOTIF-014, NOTIF-016, PLAT-008, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. La même cloche, à la même place, montre le même contenu sur tous les écrans d'un tender ; l'assistant de création n'en a pas.
2. Le point s'allume quand une notification n'a pas encore été vue et s'éteint à l'ouverture du panneau ; l'icône ne porte pas de compteur, et le bouton annonce « Notifications, N new » aux lecteurs d'écran.
3. Le panneau montre « New » (non lues) puis « Earlier » (lues, 30 jours), sur « this tender » dans un tender et sur « all my tenders » à l'accueil, avec un bouton pour passer de l'un à l'autre.
4. Une ligne réunit les notifications non lues d'un même tender, d'une même nature et d'une même cause, avec leur compte (« 12 new assignments in SIG ») ; elle nomme l'exigence quand elle est seule et passe en gris quand tout est traité.
5. Cliquer une ligne la marque lue et ouvre l'endroit exact : l'écran filtré, ou l'exigence quand elle est seule ; « Mark all as read » les marque toutes.
6. Le panneau se parcourt au clavier et se ferme avec Échap, le focus revenant au bouton ; un nouveau compte s'annonce poliment, sans déplacer le focus.
Écart maquette : chaque écran a sa propre cloche, calculée sur son seul contenu, dont le point reste allumé tant que quelque chose attend ; l'accueil et Risks n'en ont pas.

### US-X-16 — Recevoir le résumé quotidien par e-mail
**Carte :** En tant que contributeur ou tender manager, je veux un seul e-mail par jour qui rattrape ce que je n'ai pas vu dans Smart Req, tous tenders confondus, afin d'être au courant sans recevoir un message par événement.
**Conversation :** L'e-mail ne rattrape que ce qui n'a pas été vu (DEC-127) : une notification de niveau B vue dans l'application n'y figure pas. Le résumé part à 8:00 dans le fuseau de la personne, les jours ouvrés (DEC-131), et se construit au moment de partir, depuis l'état courant : ce qui a été fait, annulé ou tranché par un autre entre-temps disparaît, et s'il ne reste rien, rien ne part. C'est ce qui règle les rafales : valider 300 exigences d'un coup donne une ligne, pas 300 e-mails. Il est en anglais, texte d'abord, sans image ni suivi, avec une version texte complète, car Outlook peut forcer le texte brut. Les états qui attendent (seuil de retard dépassé, échéance à 7 jours ou moins, clôture des questions à 3 jours ou moins) ne s'y ajoutent qu'en gris, sous « Still waiting », dans un résumé qui part de toute façon.
**Maquette :** modèles `daily-summary-contributor`, `daily-summary-tender-manager` (pilote) et `daily-summary-compliance` (après pilote) dans `proposals/notifications/emails/` ; pas d'e-mail dans le prototype.
**Règles :** DEC-127, DEC-131, NOTIF-005 à NOTIF-008, NOTIF-017, NOTIF-018, NOTIF-025, DEC-118  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Un jour ouvré à 8:00, heure locale, la personne reçoit au plus un résumé, pour tous ses tenders, et seulement si une notification de niveau B n'a pas été vue.
2. Une notification vue, une action annulée ou une demande tranchée par un autre tender manager avant l'envoi ne figure pas dans le résumé.
3. L'objet commence par le tender et la chose la plus importante avec son compte, puis « and N more updates » ; la ligne d'aperçu dit la période et les tenders.
4. Le corps est groupé par tender puis par nature ; chaque ligne mène à l'endroit exact, derrière la connexion SSO, et aucun lien n'agit à l'ouverture.
5. Les lignes « Still waiting » sont en gris, en bas de leur tender, et ne déclenchent jamais un e-mail à elles seules.
6. La version texte porte les mêmes lignes et les mêmes liens ; le pied dit pourquoi la personne reçoit l'e-mail et mène à ses réglages.

### US-X-17 — Recevoir tout de suite ce qui m'est adressé ou que j'attends
**Carte :** En tant que contributeur ou tender manager, je veux un e-mail rapide quand quelqu'un s'adresse à moi ou quand arrive un résultat que j'attends, si je ne l'ai pas vu dans Smart Req, afin de réagir dans l'heure sans surveiller l'outil.
**Conversation :** Quatre cas seulement sont de niveau A (DEC-127) : une mention (DEC-132), l'ajout à un tender, la fin ou l'échec d'un traitement pour le tender manager qui l'a lancé, et, après le pilote, la relance d'un tender manager ([US-CMP-24](09-compliance.md#us-cmp-24--relancer-le-contributeur-dune-affectation-due)). La notification arrive tout de suite dans la cloche ; l'e-mail part 10 minutes plus tard, seulement si elle n'a pas été vue. L'ajout à un tender part même si la personne a coupé les e-mails : c'est souvent son premier contact avec le tender, et il dit ce qui l'attend (« Nothing to do yet » quand rien n'est encore à faire). Au-delà de trois e-mails immédiats dans la journée, les suivants attendent le résumé. Les e-mails partent d'une boîte interne « Smart Req », sans réponse (DEC-136).
**Maquette :** modèles `added-to-tender`, `processing-finished`, `processing-failed`, `mention` et `reminder` dans `proposals/notifications/emails/` ; pas d'e-mail dans le prototype.
**Règles :** DEC-127, DEC-132, DEC-136, NOTIF-005, NOTIF-006, NOTIF-017 à NOTIF-019, NOTIF-025  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Une mention, un ajout à un tender ou la fin d'un traitement, pour le tender manager qui l'a lancé, apparaît aussitôt dans la cloche ; s'il n'est pas vu 10 minutes plus tard, un e-mail part.
2. Vu dans l'application avant ces 10 minutes, il ne donne aucun e-mail ; les autres tender managers ne voient la fin d'un traitement que dans la cloche.
3. L'e-mail d'ajout part même quand la personne a coupé les e-mails ; il dit qui l'a ajoutée, à quel tender, pour quel sous-système, et ce qui l'attend.
4. Un échec dit quel document n'a pas pu être traité, pourquoi, et ce qui a été conservé ([US-CAP-11](04-capture-ia.md#us-cap-11--reprendre-un-traitement-interrompu-sans-doublon)).
5. Une personne ne reçoit pas plus de trois e-mails immédiats par jour ; au-delà, les notifications attendent le résumé quotidien.
6. Le pied de l'e-mail dit pourquoi la personne le reçoit et mène à ses réglages ; la boîte d'envoi ne reçoit pas de réponse.

### US-X-18 — Régler mes notifications
**Carte :** En tant que contributeur ou tender manager, je veux régler en quelques choix ce que je reçois par e-mail, afin de garder le résumé utile sans rien perdre dans l'application.
**Conversation :** Les réglages sont personnels et valent pour tous les tenders de la personne ; ils s'ouvrent depuis le menu de l'avatar (DEC-127). Peu de choix et des défauts sobres : la plupart des gens ne les ouvriront jamais. Rien ne se coupe dans l'application, qui reste la référence ; seul l'e-mail se règle. Le seuil de retard et le plafond des relances restent dans la Configuration du tender, parce qu'ils engagent toute l'équipe ([US-CFG-05](15-configuration.md#us-cfg-05--régler-le-seuil-de-retard-et-la-cadence-des-relances)).
**Maquette :** intention dans `proposals/notifications/index.html` (« Notification settings ») ; non maquetté dans le prototype.
**Règles :** DEC-127, DEC-131, NOTIF-021, NOTIF-022  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Le menu de l'avatar ouvre « Notification settings » sur tous les écrans où l'en-tête l'affiche.
2. Le résumé quotidien se règle sur « Working days at 8:00 » (par défaut), « Every day at 8:00 » ou « Off ».
3. L'e-mail d'une relance, d'une mention et d'un traitement que la personne a lancé se coupent chacun ; ils sont actifs par défaut.
4. Un tender peut être retiré des e-mails ; ses notifications restent dans la cloche.
5. L'ajout à un tender est toujours envoyé, et aucun réglage ne coupe la cloche.

## Couverture
- Règles couvertes : PLAT-001 → [US-X-03](#us-x-03--retrouver-tout-le-travail-après-reconnexion), [US-X-13](#us-x-13--ne-rien-perdre-en-cas-déchec-ou-de-conflit-denregistrement) ; PLAT-002 → [US-X-04](#us-x-04--se-connecter-par-sso-et-naccéder-quà-ses-tenders), [US-X-05](#us-x-05--faire-respecter-les-droits-du-tender-par-le-serveur), [US-X-08](#us-x-08--exporter-les-exigences-du-tender), [US-X-12](#us-x-12--comprendre-létat-dun-écran--chargement-vide-absence-de-droit) ; PLAT-003 → [US-X-01](#us-x-01--consulter-le-journal-dactivité-dune-exigence), [US-X-02](#us-x-02--commenter-une-exigence), [US-X-06](#us-x-06--tracer-tout-changement-humain-ou-machine) ; PLAT-004 → [US-X-08](#us-x-08--exporter-les-exigences-du-tender), [US-X-09](#us-x-09--importer-un-export-doors-comme-document-du-tender) ; PLAT-005 → [US-X-10](#us-x-10--recevoir-les-notifications-dans-lapplication-et-par-e-mail), [US-X-15](#us-x-15--ouvrir-ma-cloche-la-même-sur-tous-les-écrans), [US-X-16](#us-x-16--recevoir-le-résumé-quotidien-par-e-mail), [US-X-17](#us-x-17--recevoir-tout-de-suite-ce-qui-mest-adressé-ou-que-jattends), [US-X-18](#us-x-18--régler-mes-notifications) ; PLAT-006 → [US-X-11](#us-x-11--travailler-sur-100-000-lignes-à-dix-en-même-temps) ; PLAT-007 → [US-X-11](#us-x-11--travailler-sur-100-000-lignes-à-dix-en-même-temps) ; PLAT-008 (règle de la cloche) → [US-X-15](#us-x-15--ouvrir-ma-cloche-la-même-sur-tous-les-écrans), et pour ce qui attend [US-DASH-15](13-tableau-de-bord.md#us-dash-15--lire-ce-qui-mattend-au-pied-de-la-cloche) ; DOM-011 → [US-X-01](#us-x-01--consulter-le-journal-dactivité-dune-exigence), [US-X-02](#us-x-02--commenter-une-exigence), [US-X-06](#us-x-06--tracer-tout-changement-humain-ou-machine) ; DOM-013 → [US-X-07](#us-x-07--garder-séparées-la-proposition-de-lia-la-valeur-retenue-et-la-correction) ; NOTIF-001 à NOTIF-005, NOTIF-009, NOTIF-023, NOTIF-024 → [US-X-10](#us-x-10--recevoir-les-notifications-dans-lapplication-et-par-e-mail) ; NOTIF-010 à NOTIF-014, NOTIF-016 → [US-X-15](#us-x-15--ouvrir-ma-cloche-la-même-sur-tous-les-écrans) ; NOTIF-005 à NOTIF-008, NOTIF-017, NOTIF-018, NOTIF-025 → [US-X-16](#us-x-16--recevoir-le-résumé-quotidien-par-e-mail), [US-X-17](#us-x-17--recevoir-tout-de-suite-ce-qui-mest-adressé-ou-que-jattends) ; NOTIF-019 → [US-X-17](#us-x-17--recevoir-tout-de-suite-ce-qui-mest-adressé-ou-que-jattends) ; NOTIF-021, NOTIF-022 → [US-X-18](#us-x-18--régler-mes-notifications).
- Autres règles mises en œuvre : AI-001 → [US-X-06](#us-x-06--tracer-tout-changement-humain-ou-machine), [US-X-07](#us-x-07--garder-séparées-la-proposition-de-lia-la-valeur-retenue-et-la-correction) ; AI-011 → [US-X-07](#us-x-07--garder-séparées-la-proposition-de-lia-la-valeur-retenue-et-la-correction) ; AI-012 → [US-X-09](#us-x-09--importer-un-export-doors-comme-document-du-tender) ; AI-013 → [US-X-05](#us-x-05--faire-respecter-les-droits-du-tender-par-le-serveur) ; ALLOC-014 → [US-X-01](#us-x-01--consulter-le-journal-dactivité-dune-exigence), [US-X-07](#us-x-07--garder-séparées-la-proposition-de-lia-la-valeur-retenue-et-la-correction) ; ACC-007, ACC-012, ACC-013, ACC-014, ACC-T04, ACC-T09, ACC-T10 → [US-X-04](#us-x-04--se-connecter-par-sso-et-naccéder-quà-ses-tenders), [US-X-05](#us-x-05--faire-respecter-les-droits-du-tender-par-le-serveur) ; UX-002 → [US-X-08](#us-x-08--exporter-les-exigences-du-tender) ; UX-005 → [US-X-11](#us-x-11--travailler-sur-100-000-lignes-à-dix-en-même-temps) ; LANG-003, LIFE-004 → [US-X-08](#us-x-08--exporter-les-exigences-du-tender) ; DOM-012 → [US-X-09](#us-x-09--importer-un-export-doors-comme-document-du-tender) ; CONF-019 → [US-X-12](#us-x-12--comprendre-létat-dun-écran--chargement-vide-absence-de-droit) ; CONF-021 → [US-X-10](#us-x-10--recevoir-les-notifications-dans-lapplication-et-par-e-mail) ; JRN-001 → [US-X-03](#us-x-03--retrouver-tout-le-travail-après-reconnexion), [US-X-04](#us-x-04--se-connecter-par-sso-et-naccéder-quà-ses-tenders).
- Non couvertes, avec la raison : NOTIF-012 (pied de la cloche) — couverte par l'épopée US-DASH ([US-DASH-15](13-tableau-de-bord.md#us-dash-15--lire-ce-qui-mattend-au-pied-de-la-cloche)) ; NOTIF-015 — couverte par l'épopée US-HOME ([US-HOME-07](01-accueil.md#us-home-07--voir-ce-qui-a-changé-depuis-ma-dernière-visite)) ; NOTIF-020 — couverte par [US-CMP-24](09-compliance.md#us-cmp-24--relancer-le-contributeur-dune-affectation-due) et [US-CFG-05](15-configuration.md#us-cfg-05--régler-le-seuil-de-retard-et-la-cadence-des-relances) ; JRN-007 — couverte par les épopées US-DASH et US-CFG ; PLAT-008 (mesures) — couverte par l'épopée US-STAT ; PLAT-008 « Corrections IA » — couverte par [US-CFG-11](15-configuration.md#us-cfg-11--capter-chaque-correction-dune-proposition-de-lia) et [US-CFG-12](15-configuration.md#us-cfg-12--consulter-la-qualité-de-lia-dans--ai-feedback-) ; DEC-090 (état personnel côté serveur) — couvert par l'épopée US-CMP ([US-CMP-13](09-compliance.md#us-cmp-13--retrouver-son-brouillon-de-verdict), [US-CMP-14](09-compliance.md#us-cmp-14--mettre-une-affectation-de-côté)) ; état « traitement partiel » des parcours (JOURNEYS, PROP) et AI-012 côté reprise — couverts par [US-CAP-11](04-capture-ia.md#us-cap-11--reprendre-un-traitement-interrompu-sans-doublon) ; DEC-115 (police de marque) et logo de l'en-tête (commit `575fbbe`, sans décision) — charte sans besoin utilisateur propre, cités dans [US-X-14](#us-x-14--lire-des-couleurs-qui-gardent-toujours-le-même-sens) ; ligne « FR 5–6 » de PLATFORM (échelle à trois verdicts) — caduque (DEC-031, DEC-106).
