<!-- Généré depuis le backlog du 10 octobre 2026 ; voir README.md pour les conventions. -->
# Tableau de bord du tender (US-DASH)

Le tableau de bord est la page d'un tender ouvert : le chef de projet y voit où en est le tender et ce qui l'attend, et chaque indicateur ouvre l'écran où se fait le travail, sans jamais bloquer une étape (parcours JRN-007). Deux étapes tournent en parallèle : **Allocation** (router chaque exigence vers son système et son organisation, puis valider) et **Compliance** (dire si chaque exigence est respectée et ce que reçoit le client) ; il n'y a plus de « Finalize » (DEC-084). À côté, quatre écrans « toujours ouverts » : Team casting, Documents & versions, Risks, Q&A. Termes : *OBS* = l'organisation (équipe) qui répond pour une exigence, jamais une personne ; *OBS faible* = organisation proposée par l'IA sous le seuil de confiance ; *affectation* = le travail de conformité confié à une organisation et à sa personne. Sur un tender SIG (un seul système), le tableau de bord lit son propre contenu et masque ce qui compare des systèmes (TYPE-T07, TYPE-T08). Les statistiques du même écran sont dans US-STAT.

### US-DASH-01 — Voir l'identité et l'échéance du tender ouvert
**Carte :** En tant que chef de projet, je veux voir en tête du tableau de bord le nom, le BO-ID, la ligne produit, le produit, le volume d'exigences et les jours restants du tender ouvert, afin de savoir d'un coup d'œil sur quel tender je travaille et combien de temps il reste.
**Conversation :** L'en-tête (hero) suit toujours le tender réellement ouvert : passer d'un tender Turnkey à un tender SIG change l'affichage et le comportement ensemble (TYPE-T10). La ligne produit (Turnkey, SIG…) est suivie du produit (ex. « Mainline Wayside ») quand il en a un, une seule fois si les deux sont identiques ; un Turnkey porte une combinaison de produits dont la matrice reste à fournir (DEC-048). Le volume compte les exigences, pas les titres ni les blocs d'information (DEC-073, DEC-074). Les jours restants se calculent sur l'échéance de soumission réglée dans les paramètres (voir [US-CFG-03](15-configuration.md#us-cfg-03--régler-léchéance-de-soumission)).
**Maquette :** Tableau de bord — `dashboard-et-config.html` (route `#dashboard`), en-tête « Tender project » (hero), au-dessus du Phase Rail.
**Règles :** TYPE-T10, TYPE-T07, DEC-044, DEC-047, DEC-048, DEC-049, DEC-073, DEC-074, PLAT-001  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. L'en-tête affiche le nom du tender, « BO-ID » suivi de sa référence, la ligne produit, puis le produit quand il existe et diffère de la ligne.
2. Ouvrir un autre tender remplace toutes ces valeurs par les siennes ; aucune valeur d'un autre tender ne reste affichée.
3. « N requirements » compte les seules exigences (nature Requirement) du tender et vaut le même total que le dénominateur de la carte Allocation.
4. « days to submission » vaut le nombre de jours entre aujourd'hui et l'échéance de soumission enregistrée pour ce tender.
5. Sur un tender Turnkey sans combinaison renseignée, seule la ligne produit s'affiche, sans produit inventé.
Écart maquette : le volume vient d'une copie écrite à la main (14 exigences) et peut différer de la carte Allocation ; l'en-tête affiche « Bid Director: » suivi d'un nom écrit en dur.
Point ouvert : mention « Bid Director » et place de l'équipe de gestion dans l'en-tête — vocabulaire non refermé par écrit, DEC-030 ne retient que Project manager / Contributor ; affichage une fois l'échéance passée, non décrit.

### US-DASH-02 — Suivre l'étape Allocation sur sa carte
**Carte :** En tant que chef de projet, je veux une carte Allocation qui dit combien d'exigences sont allouées et qui passe à « Done » quand tout l'est, afin de savoir où en est l'allocation sans ouvrir l'écran.
**Conversation :** La carte lit la progression réelle d'Allocation : elle passe à « Done » quand toutes les exigences sont allouées et redevient « Current » dès qu'une ne l'est plus, par exemple après une nouvelle version ou une réouverture (DEC-098). Il n'y a plus de jalon « Finalize allocation » : l'état se lit sur les données, jamais sur un clic, et rien côté Compliance n'attend ce moment (DEC-035, DEC-084). La validation se fait exigence par exigence dans Allocation (voir US-ALM).
**Maquette :** Tableau de bord — `dashboard-et-config.html` (route `#dashboard`), Phase Rail › Phase Card (variante step) « Allocation ».
**Règles :** DEC-098, DEC-084, DEC-035, ALLOC-022, JRN-007  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. La carte affiche « N / M requirements allocated », N comptant les exigences au statut Allocated et M toutes les exigences du tender, avec une barre proportionnelle.
2. Quand N = M (M > 0), le badge passe à « Done », le texte devient « / M allocated · done » et la barre est pleine.
3. Dès qu'une exigence n'est plus Allocated (nouvelle version, réouverture, retrait d'un système), la carte repasse « Current » avec le nouveau compte, sans action de quiconque.
4. Aucun bouton, lien ni fenêtre « Finalize » n'existe sur le tableau de bord.
5. Cliquer la carte ouvre Allocation.
6. L'état « Done » ne masque ni ne verrouille rien de Compliance : sa carte et ses éléments restent les mêmes avant et après.
Écart maquette : tant qu'Allocation n'a pas été ouvert dans la session, la carte lit une copie écrite à la main.

### US-DASH-03 — Suivre l'étape Compliance en parallèle
**Carte :** En tant que chef de projet, je veux une carte Compliance ouverte dès le premier jour avec le nombre d'exigences répondues, afin de suivre les réponses sans attendre la fin de l'allocation.
**Conversation :** Les deux étapes tournent en parallèle : une exigence part vers son contributeur dès qu'elle est validée, et Compliance n'attend aucun jalon (DEC-035, DEC-084). La carte lit les verdicts réels de Compliance et ajoute les retards quand il y en a (règle de retard : voir [US-STAT-11](14-statistiques.md#us-stat-11--suivre-les-réponses-par-système-et-leurs-retards)). Une seule des deux cartes porte la mise en avant « current » : Allocation tant que tout n'est pas alloué, Compliance ensuite.
**Maquette :** Tableau de bord — `dashboard-et-config.html` (route `#dashboard`), Phase Rail › Phase Card (variante step) « Compliance ».
**Règles :** DEC-035, DEC-084, DEC-098, DEC-029, JRN-007, PLAT-008  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. La carte porte le badge « Open » et s'ouvre dès la création du tender, quel que soit l'avancement d'Allocation.
2. Elle affiche « N / M answered », N comptant les exigences dont le verdict interne est consolidé, avec une barre proportionnelle.
3. Quand des réponses sont en retard, le texte ajoute « · K overdue » ; sans retard, rien n'est ajouté.
4. Cliquer la carte ouvre Compliance.
5. La mise en avant « current » passe de la carte Allocation à la carte Compliance quand toutes les exigences sont allouées, et revient à Allocation si une exigence ne l'est plus.
Écart maquette : les chiffres viennent d'une copie de Compliance écrite à la main.
Point ouvert : dénominateur M — toutes les exigences du tender ou seulement celles déjà affectées (non écrit).

### US-DASH-04 — Ouvrir Team casting et Documents & versions depuis le rail « Always open »
**Carte :** En tant que chef de projet, je veux un rail « Always open » qui montre l'état du casting et des documents, afin d'aller staffer un système ou ajouter un document à tout moment.
**Conversation :** Les écrans de support ne sont pas des étapes : ouverts dès le premier jour, ils tournent à côté d'Allocation et de Compliance et n'en bloquent aucune. La carte Team casting compte les systèmes qui ont au moins une personne : un système sans manager n'est pas un trou, seul un système sans personne l'est (DEC-124). Le casting est décrit dans US-TEAM, Documents & versions dans US-DOC.
**Maquette :** Tableau de bord — `dashboard-et-config.html` (route `#dashboard`), Support Rail › Phase Card (variante support) « Team casting » et « Documents & versions ».
**Règles :** DEC-124, DEC-102, ACC-003, ACC-008, PLAT-008, JRN-007, TYPE-T08  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Le rail « Always open » s'affiche sous les deux étapes, sans numéro d'ordre, et aucune de ses cartes ne conditionne l'accès à une étape.
2. La carte Team casting affiche « N / M staffed », N comptant les systèmes du tender qui ont au moins une personne, et un badge « K pending » (systèmes sans personne) ou « Complete ».
3. Après une modification du casting, la carte affiche le nouveau compte au retour sur le tableau de bord.
4. La carte Documents & versions affiche le nombre de documents du tender et combien sont encore en traitement, lus sur les données enregistrées.
5. Cliquer une carte ouvre l'écran correspondant.
6. Sur un tender SIG, la carte Team casting compte son seul système (« 1 / 1 staffed » dès qu'une personne y est).
Écart maquette : le chiffre Documents (« 3 docs · 1 processing ») est écrit à la main ; le casting n'est ni persisté ni partagé avec les autres écrans.

### US-DASH-05 — Voir les risques et les questions au client dans le rail
**Carte :** En tant que chef de projet, je veux que le rail « Always open » montre aussi le nombre de risques et l'état des questions au client, afin d'ouvrir Risks ou Q&A sans passer par Compliance.
**Conversation :** Risks est la liste des risques du tender, alimentée depuis Compliance (voir US-RSK) ; Q&A est le registre des questions au client (voir US-QA). Ces deux cartes arrivent avec leurs modules, après le pilote. Elles ne sont pas des étapes et ne bloquent rien.
**Maquette :** Tableau de bord — `dashboard-et-config.html` (route `#dashboard`), Support Rail › Phase Card (variante support) « Risks » et « Q&A ».
**Règles :** DEC-105, DEC-113, DEC-114, DEC-116, DEC-122, QA-003  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. La carte Risks affiche le nombre de risques de la liste du tender (« N in the list ») et ouvre la page Risks.
2. Sur un tender neuf, la carte Risks affiche « 0 in the list », sans valeur d'exemple.
3. La carte Q&A affiche le nombre de questions du registre et combien ont une réponse du client, lus sur le registre Q&A.
4. Cliquer la carte Q&A ouvre Q&A.
5. Un risque créé ou une question qui change d'état est pris en compte à la prochaine ouverture du tableau de bord.
Écart maquette : le chiffre Q&A (« 5 questions · 1 answered ») est écrit à la main et ne lit pas le registre.

### US-DASH-06 — Voir les demandes de réallocation en attente
**Carte :** En tant que chef de projet, je veux voir sur le tableau de bord les demandes de réallocation encore en attente, afin qu'aucune ne reste oubliée dans une table.
**Conversation :** Un contributeur peut renvoyer une exigence (bon système mais mauvaise personne, mauvais système, système non concerné) avec une justification ; l'équipe de gestion du projet tranche dans Allocation (DEC-011, ALLOC-013 ; décision : voir US-ALM). La carte regroupe ces demandes au niveau du tender et n'existe que s'il y en a. Sur un Turnkey, l'exigence concernée porte le statut « Reassignment requested » tant que la demande attend (DEC-104).
**Maquette :** Tableau de bord — `dashboard-et-config.html` (route `#dashboard`), carte « Pending reassignment requests » › Attention List Item.
**Règles :** DEC-011, ALLOC-013, DEC-104, PLAT-008, JRN-007  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. La carte « Pending reassignment requests » n'apparaît que si au moins une demande du tender est en attente, avec leur nombre à côté du titre.
2. Chaque ligne affiche « <ID> — reassignment requested », le nom de la personne qui a demandé et le début de sa justification.
3. « Review → » ouvre Allocation sur l'exigence concernée.
4. Une demande approuvée, refusée ou retirée quitte la carte ; la carte disparaît quand il n'en reste aucune.
5. Seules les demandes du tender ouvert y figurent, jamais celles d'un autre tender.
Écart maquette : la boîte de demandes n'est pas propre au tender (filtrage par préfixe d'identifiant) ; « Review → » ouvre Allocation sans sélectionner l'exigence.

### US-DASH-07 — Voir ce qui m'attend dans « What needs you now »
**Carte :** En tant que chef de projet, je veux une liste « What needs you now » calculée sur l'état réel du tender, afin de savoir ce qui attend une action de ma part et d'y aller en un clic.
**Conversation :** Chaque élément se calcule depuis les données enregistrées, jamais depuis un fil figé, et mène à l'écran où l'action se fait ; un élément disparaît quand il n'a plus d'objet. Le contenu des éléments est décrit par famille dans [US-DASH-08](#us-dash-08--voir-le-travail-dallocation-qui-mattend) à [US-DASH-11](#us-dash-11--voir-les-questions-à-envoyer-au-client). Aucun élément ne transforme le processus en phases bloquantes (JRN-007).
**Maquette :** Tableau de bord — `dashboard-et-config.html` (route `#dashboard`), Dashboard Attention Panel « What needs you now » › Attention List Item, Count Badge.
**Règles :** JRN-007, PLAT-008, PLAT-001, DEC-098  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Seuls les éléments qui ont au moins une chose à traiter s'affichent.
2. Le compte à côté du titre égale le nombre d'éléments affichés.
3. Chaque élément porte un titre chiffré, une ligne d'explication et un lien d'action (« Open Allocation → », « See verdict → »…) qui ouvre l'écran concerné.
4. Quand le travail est fait (par exemple la dernière exigence validée), l'élément disparaît à la prochaine ouverture du tableau de bord.
5. Les chiffres d'un élément sont ceux de l'écran qu'il ouvre au même moment.
6. Quand rien n'attend, la liste le dit en une phrase au lieu de rester vide.
Écart maquette : la liste ne dit rien quand elle est vide.
Point ouvert : ce que voit un contributeur sur ce tableau de bord (ACC-007 lui ouvre la lecture, aucun texte ne décrit sa vue).

### US-DASH-08 — Voir le travail d'allocation qui m'attend
**Carte :** En tant que chef de projet, je veux voir combien d'exigences restent à valider, combien d'OBS faibles et de découpes incertaines sont à vérifier, afin de prioriser mon travail dans Allocation.
**Conversation :** « Requirements still to validate » compte les exigences qui ne sont pas encore Allocated ; l'élément disparaît quand tout est alloué (DEC-098). Un OBS faible est une organisation proposée par le modèle d'allocation avec une confiance sous le seuil — les modèles d'allocation gardent leurs pourcentages (DEC-120) — : c'est l'organisation qui est peut-être la mauvaise, pas la personne (DEC-054). Une découpe incertaine est un bloc dont l'IA n'est pas sûre des limites (signal décrit dans [US-CAP-05](04-capture-ia.md#us-cap-05--signaler-une-découpe-incertaine)). Titres et blocs d'information n'entrent dans aucun compte d'exigences (DEC-073).
**Maquette :** Tableau de bord — `dashboard-et-config.html` (route `#dashboard`), Attention List Item « Requirements still to validate » et « N uncertain segmentations » (« Fix in Allocation → ») ; OBS faibles : non maquetté dans cette liste (présent dans la cloche).
**Règles :** DEC-098, DEC-099, DEC-120, DEC-054, DEC-073, ALLOC-006, ALLOC-007  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. L'élément « Requirements still to validate » affiche « N requirements still to validate », N comptant les exigences du tender qui ne sont pas Allocated.
2. « Open Allocation → » ouvre Allocation.
3. L'élément disparaît dès que toutes les exigences sont Allocated et revient si l'une ne l'est plus.
4. Un élément compte les exigences dont au moins un OBS proposé par l'IA est sous le seuil de confiance, et ouvre Allocation.
5. L'élément « N uncertain segmentations » compte les blocs du tender signalés à découpe incertaine et ouvre Allocation ; il disparaît quand aucun bloc n'est signalé.
6. Quand un seul cas est concerné, l'élément nomme l'exigence ou le bloc au lieu d'afficher un compte.
Écart maquette : les OBS faibles ne figurent que dans la cloche, pas dans cette liste ; « 2 uncertain segmentations » est écrit à la main.
Point ouvert : valeur du seuil de confiance des modèles d'allocation (75 % dans la maquette, sans règle écrite ni réglage) ; compter encore un OBS faible sur une exigence déjà validée ou non ; ce qui retire le signal de découpe incertaine et la correction manuelle de la découpe ([US-CAP-05](04-capture-ia.md#us-cap-05--signaler-une-découpe-incertaine)).

### US-DASH-09 — Voir l'arrivée d'une nouvelle version et ses effets
**Carte :** En tant que chef de projet, je veux que le tableau de bord signale la dernière version téléversée d'un document, avec son écart et les réponses rouvertes, afin de lancer la revue des changements au bon moment.
**Conversation :** Les versions appartiennent aux documents (DEC-069). Le récit vient de ce que Documents & versions a enregistré pour ce tender : document, version, écart (ajouts, modifications, suppressions) et nombre de réponses rouvertes dans Compliance — le même nombre que Compliance rouvre (DEC-122, LIFE-007). Rien ne s'affiche tant qu'aucune nouvelle version n'a été téléversée. La revue des changements se fait dans Allocation (voir US-CHG, US-DOCV).
**Maquette :** Tableau de bord — `dashboard-et-config.html` (route `#dashboard`), Attention List Item « … ready for review » (« Review changes → ») et Activity Feed Panel « Recent activity ».
**Règles :** DEC-122, DEC-069, DEC-016, LIFE-007, LIFE-012, DEC-098  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Après le téléversement d'une nouvelle version, un élément « <document> <version> ready for review » apparaît avec « +a ~m −r » et « N answers reopened in Compliance » (ou « no answer reopened »).
2. « Review changes → » ouvre Documents & versions.
3. N égale le nombre d'affectations rouvertes par cette version dans Compliance.
4. Le fil « Recent activity » ajoute « <document> <version> uploaded — gap analysis ready (+a ~m −r) » et, seulement si N > 0, une ligne qui dit les réponses rouvertes et cite les exigences concernées.
5. Sur un tender où aucune version n'a été téléversée, ni l'élément ni ces lignes n'apparaissent.
6. Si des exigences modifiées ne sont plus allouées, la carte Allocation repasse « Current » ([US-DASH-02](#us-dash-02--suivre-létape-allocation-sur-sa-carte)).
Écart maquette : l'écart est simulé par Documents et seul le dernier téléversement est raconté.
Point ouvert : plusieurs versions téléversées à la suite — raconter seulement la dernière ou chacune (non écrit).

### US-DASH-10 — Voir les réponses en retard et les Not compliant à documenter
**Carte :** En tant que chef de projet, je veux voir les réponses de contributeurs en retard, avec la personne à relancer, et les verdicts Not compliant encore sans risque ou sans stratégie, afin d'agir là où la conformité piétine.
**Conversation :** Une réponse est en retard quand l'affectation attend son contributeur depuis au moins 5 jours (PLAT-008) ; une affectation qui attend le client ou une décision de réallocation n'est pas en retard. Le nom n'apparaît ici que parce qu'il faut relancer cette personne, responsable de son affectation (DEC-118, DEC-087) ; la relance elle-même se fait dans Compliance (DEC-125, voir US-CMP). Une stratégie ou un risque manquant ne bloque rien mais se signale (DEC-108).
**Maquette :** Tableau de bord — `dashboard-et-config.html` (route `#dashboard`), Attention List Item « N contributor responses overdue » (« Remind → ») et « N Not compliant verdicts » (« See verdict → »).
**Règles :** PLAT-008, DEC-118, DEC-087, DEC-125, DEC-108, DEC-105, DEC-092  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. L'élément « N contributor responses overdue » compte les affectations qui attendent leur contributeur depuis 5 jours ou plus, sans celles qui attendent le client ou une décision de réallocation.
2. Sa ligne d'explication nomme la personne et l'exigence du retard le plus ancien, avec son âge en jours, puis « +K more » s'il y en a d'autres.
3. « Remind → » ouvre Compliance ; l'élément disparaît quand plus aucune affectation n'est en retard.
4. L'élément « N Not compliant verdicts » dit combien ne sont pas encore liés à un risque et combien n'ont pas de stratégie d'écart, ou « All documented — strategy and risk on each ».
5. Cet élément n'apparaît pas tant qu'aucun verdict Not compliant n'existe ; « See verdict → » ouvre Compliance.
Écart maquette : les retards sont une liste fixe, pas un calcul d'âge ; le libellé dit « unopened for N days » alors que la règle compte l'âge sans réponse.
Point ouvert : seuil de 5 jours fixé par PLAT-008 face au réglage « Overdue threshold » des paramètres, relié à rien ([US-CFG-05](15-configuration.md#us-cfg-05--régler-le-seuil-de-retard-et-la-cadence-des-relances)).

### US-DASH-11 — Voir les questions à envoyer au client
**Carte :** En tant que chef de projet, je veux voir combien de questions au client restent à envoyer, afin de penser à les marquer envoyées une fois parties.
**Conversation :** L'outil n'envoie rien au client : le chef de projet envoie hors outil, puis marque les questions « envoyées » à la main dans Q&A (DEC-116, QA-003). Une question posée depuis Compliance entre dans le registre au statut To send (DEC-088). L'élément lit le registre Q&A (voir US-QA).
**Maquette :** Tableau de bord — `dashboard-et-config.html` (route `#dashboard`), Attention List Item « N questions to send » (« Open Q&A → »).
**Règles :** DEC-116, DEC-088, DEC-122, QA-003, QA-010  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. L'élément affiche « N questions to send » avec « Mark them as sent once they're out », N comptant les questions du registre au statut To send.
2. « Open Q&A → » ouvre Q&A.
3. Marquer une question envoyée dans Q&A diminue N à la prochaine ouverture du tableau de bord ; à zéro, l'élément disparaît.
4. Une question posée depuis Compliance augmente N dès qu'elle est enregistrée ; annulée, elle n'est plus comptée.
5. Quand N = 1, l'élément nomme la question et son exigence.
Écart maquette : « 2 questions to send » est écrit à la main et ne lit pas le registre.

### US-DASH-12 — Lire les derniers commentaires du tender
**Carte :** En tant que chef de projet, je veux un fil « Recent comments » qui rassemble les derniers commentaires du tender, afin de repérer une note de risque ou un renvoi sans fouiller chaque exigence.
**Conversation :** Le fil lit le journal d'activité des exigences ([US-X-01](16-transverse.md#us-x-01--consulter-le-journal-dactivité-dune-exigence), [US-X-02](16-transverse.md#us-x-02--commenter-une-exigence)) : commentaires, demandes de réallocation avec leur justification, questions posées au client, risques liés à un Not compliant. Il remplace l'ancien bloc « Project health ». Les noms y figurent comme auteurs, là où le travail l'exige (DEC-118) : le fil ne compte ni ne classe personne.
**Maquette :** Tableau de bord — `dashboard-et-config.html` (route `#dashboard`), colonne de droite « Recent comments » › Activity Feed Item.
**Règles :** DOM-011, PLAT-003, ALLOC-013, DEC-118  ·  **Périmètre :** Pilote 1 (à confirmer)  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Le fil affiche les six éléments les plus récents du tender, du plus récent au plus ancien.
2. Chaque élément montre son auteur, l'exigence citée, un extrait et la date.
3. Un commentaire posté sur une exigence apparaît dans le fil à la prochaine ouverture du tableau de bord.
4. Une demande de réallocation apparaît avec son auteur et le début de sa justification.
5. Cliquer un élément ouvre l'exigence citée.
6. Sans aucun commentaire sur le tender, le fil affiche « No comments yet. ».
Écart maquette : seules les demandes de réallocation sont réelles ; les autres lignes sont écrites à la main, le fil ne lit pas le journal et ses éléments ne sont pas cliquables.
Point ouvert : liste exacte des événements qui comptent comme commentaire dans ce fil (non écrite).

### US-DASH-13 — Suivre les réponses par système
**Carte :** En tant que chef de projet, je veux voir, pour les systèmes qui portent le plus d'affectations, combien de réponses sont rendues et combien sont en retard, afin de savoir où relancer sans classer les personnes.
**Conversation :** La carte « Answers by system » remplace l'ancienne liste nominative des experts : aucune statistique ne mesure une personne (DEC-118). Sur un tender à un seul système (SIG), elle se lit par sous-système. Elle montre les mêmes chiffres que Statistiques › Compliance › Answers by system ([US-STAT-11](14-statistiques.md#us-stat-11--suivre-les-réponses-par-système-et-leurs-retards)).
**Maquette :** Tableau de bord — `dashboard-et-config.html` (route `#dashboard`), colonne de droite « Answers by system » › Compact Expert Line.
**Règles :** DEC-118, DEC-117, PLAT-008, TYPE-T08  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes (SIG : par sous-système)
**Critères d'acceptation :**
1. La carte liste les trois systèmes qui ont le plus d'affectations confiées, chacun avec une barre et « répondues/confiées ».
2. Un système qui a des réponses en retard affiche « N late » à la place du ratio, avec une barre de couleur distincte.
3. Aucun nom de personne n'apparaît dans la carte.
4. Sur un tender SIG, la carte s'intitule « Answers by sub-system » et liste les sous-systèmes.
5. Les chiffres sont identiques, au même moment, à ceux du bloc « Answers by system » des statistiques.
Écart maquette : les chiffres sont écrits à la main.
Point ouvert : « sous-système » désigne ici les périmètres staffés du casting (DEC-118), alors que DEC-046 et DEC-058 appellent sous-systèmes les codes vers lesquels un Turnkey répartit.

### US-DASH-14 — Suivre l'activité récente du tender
**Carte :** En tant que chef de projet, je veux un fil « Recent activity » des derniers faits marquants du tender, afin de savoir ce qui a bougé depuis ma dernière visite.
**Conversation :** Le fil raconte des faits enregistrés : nouvelle version téléversée et réponses rouvertes ([US-DASH-09](#us-dash-09--voir-larrivée-dune-nouvelle-version-et-ses-effets)), dernière réponse donnée, question marquée envoyée. Il n'y a plus de jalon « Allocation milestone reached » ni de lien « View all » vers nulle part (DEC-084).
**Maquette :** Tableau de bord — `dashboard-et-config.html` (route `#dashboard`), Activity Feed Panel « Recent activity » (bas de page).
**Règles :** DEC-084, DEC-122, DEC-116, DOM-011  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Chaque ligne décrit un fait enregistré du tender, avec sa date, du plus récent au plus ancien.
2. La dernière réponse donnée apparaît sous la forme « <ID> answered — internal verdict Compliant » (ou « Not compliant »).
3. Une question marquée envoyée apparaît sous la forme « <QA-ID> marked as sent ».
4. Aucune ligne « Allocation milestone reached » ni aucun lien « View all » n'existe.
5. Sur un tender sans activité, le fil le dit au lieu d'afficher des exemples.
Écart maquette : deux lignes sont écrites à la main (une question posée par une personne nommée, « QA-01 marked as sent »).
Point ouvert : liste des faits qui entrent dans ce fil et sa profondeur (non écrites).

### US-DASH-15 — Ouvrir la cloche du tableau de bord
**Carte :** En tant que chef de projet, je veux une cloche qui résume ce qui m'attend, par nature et avec un compte, afin de voir d'un coup d'œil s'il y a quelque chose à faire sans lire une liste interminable.
**Conversation :** Règle commune à toutes les cloches de SRM (PLATFORM, PLAT-008) : le contenu se calcule depuis l'état réel, se résume par nature avec son compte — une ligne par affectation donnerait des dizaines de lignes, un tableau et non une notification —, nomme l'exigence quand il n'y en a qu'une et dit explicitement quand rien n'attend. Sur le tableau de bord : exigences à revoir dans Allocation, OBS faibles à vérifier, affectations au-delà du seuil de retard, dernière version d'un document arrivée. Les cloches de Compliance, Documents & versions, Q&A et Allocation appliquent la même règle à leur propre contenu (voir US-CMP, US-DOC, US-QA, US-ALM) ; l'envoi par e-mail relève d'[US-X-10](16-transverse.md#us-x-10--recevoir-les-notifications-dans-lapplication-et-par-e-mail).
**Maquette :** Tableau de bord — `dashboard-et-config.html` (route `#dashboard`), App Header › Icon Button cloche, Notification Dot, Notifications Dropdown.
**Règles :** PLAT-008, PLAT-005, CONF-021, DEC-087  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Le point sur la cloche n'apparaît que si au moins un élément attend.
2. Ouverte, la cloche affiche « Notifications · N » puis une ligne par nature avec son compte (ex. « 3 requirements waiting to be reviewed in Allocation »), jamais une ligne par exigence ou par affectation.
3. Quand une nature ne compte qu'un élément, sa ligne nomme l'exigence concernée.
4. Quand rien n'attend, la cloche affiche « Nothing waiting on you here. ».
5. Cliquer une ligne ferme la cloche et ouvre l'écran concerné, sur l'exigence quand il n'y en a qu'une.
6. Le contenu est recalculé à chaque ouverture : un élément traité entre-temps n'y figure plus.
Écart maquette : la cloche du tableau de bord ne nomme pas l'exigence quand il n'y en a qu'une ; celle d'Allocation affiche encore une liste figée (mention, version v2.1, rappel), contraire à la règle.
Point ouvert : déclencheurs, destinataires et regroupement des notifications (PLAT-005, OPEN-11).

## Couverture
- Règles couvertes : PLAT-008 → [US-DASH-03](#us-dash-03--suivre-létape-compliance-en-parallèle), [US-DASH-04](#us-dash-04--ouvrir-team-casting-et-documents--versions-depuis-le-rail--always-open-), [US-DASH-06](#us-dash-06--voir-les-demandes-de-réallocation-en-attente), [US-DASH-07](#us-dash-07--voir-ce-qui-mattend-dans--what-needs-you-now-), [US-DASH-10](#us-dash-10--voir-les-réponses-en-retard-et-les-not-compliant-à-documenter), [US-DASH-13](#us-dash-13--suivre-les-réponses-par-système), [US-DASH-15](#us-dash-15--ouvrir-la-cloche-du-tableau-de-bord) (règle de la cloche, mesures « Casting incomplet », « Attente », « Réponses par système », « Réallocations ») ; JRN-007 → [US-DASH-02](#us-dash-02--suivre-létape-allocation-sur-sa-carte), [US-DASH-03](#us-dash-03--suivre-létape-compliance-en-parallèle), [US-DASH-04](#us-dash-04--ouvrir-team-casting-et-documents--versions-depuis-le-rail--always-open-), [US-DASH-06](#us-dash-06--voir-les-demandes-de-réallocation-en-attente), [US-DASH-07](#us-dash-07--voir-ce-qui-mattend-dans--what-needs-you-now-) ; PLAT-005 → [US-DASH-15](#us-dash-15--ouvrir-la-cloche-du-tableau-de-bord) (notification dans l'application) ; PLAT-001 → [US-DASH-01](#us-dash-01--voir-lidentité-et-léchéance-du-tender-ouvert), [US-DASH-07](#us-dash-07--voir-ce-qui-mattend-dans--what-needs-you-now-) ; DOM-011 → [US-DASH-12](#us-dash-12--lire-les-derniers-commentaires-du-tender), [US-DASH-14](#us-dash-14--suivre-lactivité-récente-du-tender) ; PLAT-003 → [US-DASH-12](#us-dash-12--lire-les-derniers-commentaires-du-tender).
- Autres règles mises en œuvre (familles d'autres épopées) : TYPE-T07, TYPE-T10 → [US-DASH-01](#us-dash-01--voir-lidentité-et-léchéance-du-tender-ouvert) ; TYPE-T08 → [US-DASH-04](#us-dash-04--ouvrir-team-casting-et-documents--versions-depuis-le-rail--always-open-), [US-DASH-13](#us-dash-13--suivre-les-réponses-par-système) ; ALLOC-022 → [US-DASH-02](#us-dash-02--suivre-létape-allocation-sur-sa-carte) ; ALLOC-013 → [US-DASH-06](#us-dash-06--voir-les-demandes-de-réallocation-en-attente), [US-DASH-12](#us-dash-12--lire-les-derniers-commentaires-du-tender) ; ALLOC-006, ALLOC-007 → [US-DASH-08](#us-dash-08--voir-le-travail-dallocation-qui-mattend) ; LIFE-007, LIFE-012 → [US-DASH-09](#us-dash-09--voir-larrivée-dune-nouvelle-version-et-ses-effets) ; QA-003 → [US-DASH-05](#us-dash-05--voir-les-risques-et-les-questions-au-client-dans-le-rail), [US-DASH-11](#us-dash-11--voir-les-questions-à-envoyer-au-client) ; QA-010 → [US-DASH-11](#us-dash-11--voir-les-questions-à-envoyer-au-client) ; CONF-021 → [US-DASH-15](#us-dash-15--ouvrir-la-cloche-du-tableau-de-bord).
- Non couvertes, avec la raison : PLAT-002, PLAT-004, PLAT-006, PLAT-007, DOM-013 — couvertes par l'épopée US-X ; PLAT-008 (mesures détaillées des statistiques) — couverte par l'épopée US-STAT ; PLAT-008 « Corrections IA » — hors tableau de bord par DEC-117, couverte par [US-CFG-12](15-configuration.md#us-cfg-12--consulter-la-qualité-de-lia-dans--ai-feedback-) ; DEC-115 (police de marque) et logo de l'en-tête — charte sans comportement propre (voir [US-X-14](16-transverse.md#us-x-14--lire-des-couleurs-qui-gardent-toujours-le-même-sens)).
