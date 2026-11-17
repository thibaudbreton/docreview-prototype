<!-- Généré depuis le backlog du 10 octobre 2026 ; voir README.md pour les conventions. -->
# Users et droits (US-TEAM)

L'écran Users dit qui travaille sur le tender, dans quel sous-système et sur quel périmètre. Le tender manager y compose l'équipe de gestion du tender et staffe les sous-systèmes ; chaque contributeur gère les rattachements de son propre sous-système (parcours JRN-004). Le staffing est permanent : il se complète tout au long du tender et ne bloque jamais le travail (ACC-003). Les droits qui en découlent — tout lire dans son tender, ne modifier que son sous-système — sont posés ici une fois pour tous les écrans.
- **Sous-système** : un code de la liste de référence de la capture (SIG, TRK, SEN…), dont le libellé est encore égal au code.
- **Périmètre** : une équipe de la liste OBS · team, facultative, qui sert à désigner automatiquement la personne quand le modèle dérive cette équipe.
- **Rattachement** : une personne + son sous-système + son périmètre éventuel ; un sous-système est **staffé** dès qu'il a au moins une personne.

### US-TEAM-01 — Ouvrir l'écran Users là où l'on a à agir
**Carte :** En tant que tender manager ou contributeur, je veux arriver sur l'écran Users au bon endroit — la vue d'ensemble pour le tender manager, mon sous-système déplié pour un contributeur —, afin d'agir tout de suite sans parcourir 200 lignes.
**Conversation :** Users est un écran permanent de gestion des personnes, pas une étape de la création (ACC-003). On y arrive par l'icône « Team management » de l'en-tête ou par la carte « Users » du tableau de bord (voir US-DASH). Chaque sous-système est un groupe repliable : son code, son manager s'il en a un, sa couverture, puis ses périmètres et ses personnes. Tout membre du tender lit tout le staffing, équipe de gestion comprise (ACC-007) ; seuls les contrôles changent selon les droits ([US-TEAM-10](#us-team-10--laisser-les-contributeurs-dun-sous-système-gérer-ses-rattachements)).
**Maquette :** Users — `dashboard-et-config.html` (route `#team`), Team Casting Screen, Cast Activity Group, Cast Perimeter Group, Cast Person Row.
**Règles :** ACC-003, ACC-007, ACC-008, JRN-004, DEC-045, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Un tender manager arrive sur « Users — overview » : la couverture par sous-système, l'équipe de gestion du tender, puis tous les sous-systèmes repliés.
2. Un contributeur arrive sur « Users — your scope » : son sous-système déplié, la zone d'ajout prête ; les autres sous-systèmes restent visibles, repliés.
3. Chaque sous-système montre son code, « model » s'il a un modèle d'allocation ou « manual » sinon, et le nom de son manager ou « No manager — contributors only ».
4. Dans un sous-système, les personnes sont rangées par périmètre ; celles staffées sans périmètre sont réunies sous « Staffed directly (no perimeter) ».
5. Chaque personne montre qui l'a ajoutée et quand (« Added by <nom> · <date> »), et le nombre d'exigences qu'elle tient déjà.
6. Un sous-système que l'on ne peut pas modifier s'affiche en lecture seule, avec la raison écrite en clair.
Écart maquette : l'arrivée dépend du sélecteur de démonstration « Viewing as » (tender manager ou manager, aucun contributeur simple) ; l'équipe de gestion n'est affichée qu'aux tender managers.

### US-TEAM-02 — Repérer les sous-systèmes sans personne et les staffer
**Carte :** En tant que tender manager, je veux voir d'un coup d'œil quels sous-systèmes n'ont encore personne et y ajouter la première personne, afin que l'allocation trouve quelqu'un dans chaque sous-système concerné.
**Conversation :** Un sous-système n'a pas besoin de manager : il est staffé dès qu'une personne y est rattachée, sur un périmètre ou directement (DEC-124). Un périmètre vide n'est donc pas un manque. Le tender manager amorce seul un sous-système vide, sans attendre qu'un manager existe (ACC-T07). La carte « Users » du tableau de bord compte les mêmes sous-systèmes staffés (voir US-DASH).
**Maquette :** Users — `dashboard-et-config.html` (route `#team`), Cast Coverage Card, Chip Toggle (« ⚠ Unstaffed only »).
**Règles :** DEC-124, ACC-008, ACC-T07, JRN-004, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. La bande de couverture montre une carte par sous-système du tender, avec son code et son état.
2. Un sous-système sans aucune personne est marqué « Nothing staffed » ; un sous-système qui a au moins une personne n'est jamais marqué non staffé, même si des périmètres restent vides.
3. Un sous-système sans manager n'est jamais signalé comme un manque.
4. Cliquer une carte déplie ce sous-système et l'amène à l'écran.
5. Le tender manager ajoute la première personne d'un sous-système vide et sans manager depuis ce sous-système ; sa carte passe aussitôt à staffé.
6. « ⚠ Unstaffed only » ne garde que les sous-systèmes sans personne.
Écart maquette : la couverture compte encore six périmètres plus « staffé directement » (« n/7 staffed », « Fully staffed » seulement quand les sept sont pourvus), chaque périmètre vide porte « ⚠ Unstaffed » et le filtre garde les périmètres vides.

### US-TEAM-03 — Composer l'équipe de gestion du tender
**Carte :** En tant que tender manager, je veux ajouter et retirer des membres de l'équipe de gestion du tender, afin de partager la conduite du tender sans jamais le laisser sans tender manager.
**Conversation :** Plusieurs personnes ont le statut de tender manager, chacune sur tout le tender, sans restriction de sous-système (ACC-001) : bid managers, et requirement managers SIG sur un tender SIG (DEC-009). Le créateur du tender en est le premier membre (l'équipe saisie à la création : voir US-NEW). On ajoute un membre par la recherche dans l'annuaire, sans étape de périmètre. Un tender manager n'a pas besoin d'être staffé dans un sous-système pour y travailler.
**Maquette :** Users — `dashboard-et-config.html` (route `#team`), groupe « Tender management team » (Cast Activity Group, variante TM-team), Add-Person Flow (variante TM-team), Cast Person Row.
**Règles :** ACC-001, ACC-002, ACC-T01, ACC-008, DEC-009, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Le groupe « Tender management team » montre chaque membre ; le créateur porte « On the tender since <date> — created it », les autres « Added by <nom> · <date> ».
2. Choisir une personne dans l'annuaire l'ajoute à l'équipe sans choix de périmètre ; le champ se vide, prêt pour l'ajout suivant.
3. Ajouter une personne déjà membre est refusé avec « <nom> is already on the tender management team ».
4. Retirer un membre alors qu'il en reste au moins un autre le sort de l'équipe et lui retire les droits de tender manager sur ce tender.
5. Le dernier membre porte « Last member » ; son retrait est refusé avec « A tender always keeps at least one tender manager », y compris par une requête directe au serveur.
6. Un contributeur ne peut ni ajouter ni retirer un membre de l'équipe de gestion, ni à l'écran ni par une requête directe.
Point ouvert : le créateur reste-t-il impossible à retirer une fois le tender créé ? L'assistant de création l'affiche « Never removed — created the tender », alors que l'écran Users permet de le retirer s'il reste un autre tender manager ; ACC-001 dit seulement qu'il est le premier membre.

### US-TEAM-04 — Ajouter un sous-système au tender depuis la liste de référence
**Carte :** En tant que tender manager, je veux ajouter au tender un sous-système de la liste de référence qui n'y figure pas encore, afin de pouvoir le staffer quand l'allocation en a besoin.
**Conversation :** La liste de référence est celle de la capture : les 16 codes sous-système présents dans le document, communs à Allocation, Compliance, Q&A et Users (DEC-032). On n'ajoute qu'un code de cette liste, jamais un sous-système saisi au clavier. Un tender SIG (Mainline compris) est émis sur un seul sous-système et n'en gagne pas un second (DEC-046, DEC-047). Le sous-système ajouté n'a pas de manager, ce qui n'est pas un manque (DEC-124).
**Maquette :** Users — `dashboard-et-config.html` (route `#team`), bouton « + Add sub-system » et sa fenêtre « Add sub-system ».
**Règles :** DEC-032, DEC-045, DEC-046, DEC-124, ACC-008, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Turnkey (absent sur SIG et Mainline)
**Critères d'acceptation :**
1. « + Add sub-system » n'est proposé qu'à un tender manager.
2. La fenêtre ne propose que les codes de la liste de référence absents du tender ; aucune saisie libre n'est possible.
3. Quand tous les codes sont déjà sur le tender, la fenêtre l'écrit : « Every sub-system in the reference list is already on this tender. ».
4. Le sous-système ajouté s'affiche déplié, sans manager, la zone d'ajout prête, avec le message « <code> added — staff it below ».
5. Sur un tender SIG ou Mainline, « + Add sub-system » n'existe pas et un ajout de sous-système demandé directement au serveur est refusé.
Point ouvert : la légende métier des 16 codes reste à fournir (DEC-032) ; retirer un sous-système du tender n'est pas spécifié ; le staffing d'un tender RSC n'est pas décrit (OPEN-15).

### US-TEAM-05 — Staffer une personne sur un sous-système, avec ou sans périmètre
**Carte :** En tant que tender manager ou contributeur d'un sous-système, je veux trouver une personne dans l'annuaire de l'entreprise et la rattacher à ce sous-système, sur un périmètre ou directement, afin qu'elle puisse y travailler et y recevoir des allocations.
**Conversation :** C'est le geste répété 150 à 200 fois par tender (JRN-004) : il doit être rapide et se faire au clavier. La personne vient de l'annuaire SSO, rien n'est saisi à la main (ACC-004, PLAT-002). Le périmètre est facultatif : « — No perimeter — staffed directly — » est un choix ordinaire, pas une étape sautée. Les périmètres forment une liste fermée, la liste OBS · team, la même pour tous les sous-systèmes (DEC-036) ; l'écran Users n'en crée pas. Qui peut staffer quel sous-système est décrit dans [US-TEAM-10](#us-team-10--laisser-les-contributeurs-dun-sous-système-gérer-ses-rattachements), la règle « une personne, un sous-système » dans [US-TEAM-06](#us-team-06--refuser-quune-personne-appartienne-à-deux-sous-systèmes).
**Maquette :** Users — `dashboard-et-config.html` (route `#team`), Add-Person Flow, Search-to-Add Combobox, Cast Person Row.
**Règles :** ACC-004, DEC-033, DEC-036, DEC-045, JRN-004, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Un nom tapé dans « Search a person via SSO… » propose les personnes de l'annuaire qui correspondent ; flèches et Entrée suffisent pour en choisir une ; « No match in the directory. » quand personne ne correspond.
2. Après le choix, le périmètre se prend dans la liste fermée ou reste sur « — No perimeter — staffed directly — » ; aucun périmètre ne peut être saisi.
3. « Add » enregistre le rattachement et le confirme : « <nom> added — <périmètre> » ou « <nom> added — staffed directly ».
4. Après l'ajout, le champ de recherche est vide et actif, dans le même sous-système : l'ajout suivant s'enchaîne sans naviguer.
5. La ligne ajoutée porte son auteur et sa date ; le nom et l'identité viennent de l'annuaire.
6. La personne ajoutée est aussitôt proposée comme personne des OBS de son sous-système dans Allocation (voir US-ALM).
Écart maquette : annuaire SSO simulé ; le staffing reste local à son écran (perdu au changement d'écran, lu ni par Allocation ni par Compliance) ; Configuration › « Team & contributors » garde une seconde liste de contributeurs saisie à la main (nom libre et « Team / domain »), sans lien avec l'écran Users.

### US-TEAM-06 — Refuser qu'une personne appartienne à deux sous-systèmes
**Carte :** En tant que tender manager, je veux qu'une personne ne puisse être staffée que dans un seul sous-système, et le voir dès la recherche, afin que « son sous-système » — celui qu'elle peut modifier — soit toujours sans ambiguïté.
**Conversation :** Une personne appartient à un seul sous-système, sur un ou plusieurs de ses périmètres (DEC-102, DEC-124, ACC-014). Cette appartenance décide ce qu'elle peut modifier ([US-TEAM-14](#us-team-14--ne-modifier-que-le-travail-de-son-sous-système)) et sur quels OBS on peut la désigner : seulement ceux de son sous-système (voir US-ALM). Le refus s'explique au moment du choix, pas après coup.
**Maquette :** Users — `dashboard-et-config.html` (route `#team`), Add-Person Flow (option grisée « In <code> — one sub-system per person »).
**Règles :** DEC-102, DEC-124, ACC-014, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Dans la recherche d'un sous-système, une personne déjà membre d'un autre sous-système reste listée, grisée, avec « In <code> — one sub-system per person ».
2. La choisir est refusé avec « <nom> already belongs to <code> — a person is staffed on one sub-system only » ; l'étape du périmètre ne s'ouvre pas.
3. Une personne déjà membre de ce sous-système est listée avec « Already in <code> » et reste sélectionnable pour un autre périmètre.
4. Un rattachement à un second sous-système demandé directement au serveur est refusé avec la même raison.
5. Une personne dont tous les rattachements ont été retirés peut être staffée dans un autre sous-système.

### US-TEAM-07 — Staffer une personne sur plusieurs périmètres, sans doublon
**Carte :** En tant que tender manager ou contributeur d'un sous-système, je veux rattacher une même personne à plusieurs périmètres de son sous-système sans pouvoir la rattacher deux fois au même endroit, afin de refléter ce qu'elle couvre réellement.
**Conversation :** Les rattachements multiples sont permis dans un même sous-système (ACC-005, DEC-124) : une personne peut couvrir deux équipes. Le même trio personne + sous-système + périmètre ne s'enregistre qu'une fois (ACC-T02). Après un ajout, l'écran propose de rattacher la même personne à un autre périmètre.
**Maquette :** Users — `dashboard-et-config.html` (route `#team`), Add-Person Flow, bandeau « Just added ».
**Règles :** ACC-005, ACC-T02, DEC-124, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Rattacher une personne déjà membre du sous-système à un autre périmètre crée une seconde ligne, sous ce périmètre.
2. Rattacher la même personne au même sous-système et au même périmètre est refusé avec « <nom> is already staffed here — pick a different perimeter, or search someone else » ; aucune ligne n'est créée.
3. Le même refus s'applique à une requête directe au serveur.
4. Après un ajout, le bandeau « Just added <nom> » propose de la staffer sur un autre périmètre du même sous-système ; « Dismiss » le ferme.
5. Une personne staffée sur plusieurs périmètres apparaît sous chacun d'eux.

### US-TEAM-08 — Retrouver une personne parmi 200 personnes staffées
**Carte :** En tant que tender manager ou contributeur, je veux chercher une personne dans tout le staffing et voir où elle est staffée, afin de vérifier avant d'ajouter plutôt qu'après.
**Conversation :** Un tender réel staffe 150 à 200 personnes (JRN-004). L'écran reste groupé par sous-système puis par périmètre, jamais une liste plate. La recherche porte sur tout le staffing, sous-systèmes repliés compris.
**Maquette :** Users — `dashboard-et-config.html` (route `#team`), Search Box (« Search the roster — is this person already staffed, and where? »).
**Règles :** JRN-004, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Un nom saisi dans « Search the roster — is this person already staffed, and where? » ne garde, à chaque frappe, que les personnes qui correspondent, dans tous les sous-systèmes et tous les périmètres.
2. Une personne trouvée apparaît sous son sous-système et sous chacun de ses périmètres.
3. Effacer la recherche rend la liste complète.
4. Avec 200 personnes staffées, la liste reste groupée par sous-système et par périmètre, chaque sous-système repliable.
5. Avec 200 personnes staffées, l'ajout garde le même comportement qu'avec trois : résultats de l'annuaire à chaque frappe, champ prêt après chaque ajout.
Écart maquette : l'échelle n'est montrée que par la commande de démonstration « Simulate 200 roster ».
Point ouvert : les budgets de temps de réponse restent à fixer (PLAT-007, OPEN-08).

### US-TEAM-09 — Retirer une personne, après réaffectation de son travail
**Carte :** En tant que tender manager ou contributeur d'un sous-système, je veux retirer une personne du staffing, et être arrêté tant qu'elle tient encore du travail, afin qu'aucune allocation ne perde sa personne à l'insu de tous.
**Conversation :** Retirer est simple tant que rien ne dépend de la personne. Si elle est encore la personne d'au moins une allocation (OBS) du tender, donc responsable de sa conformité (DEC-087), il faut d'abord réaffecter ce travail (ACC-006, ACC-T03), dans Allocation ou dans Compliance (voir US-ALM, US-CMP). Le refus le dit au moment du clic.
**Maquette :** Users — `dashboard-et-config.html` (route `#team`), Cast Person Row (bouton ✕).
**Règles :** ACC-006, ACC-T03, DEC-087, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Le ✕ d'une personne n'apparaît que pour qui peut modifier ce sous-système.
2. Une personne sans travail sur le tender est retirée de ce rattachement, avec le message « <nom> removed ».
3. Le retrait d'une personne encore désignée sur au moins une allocation est refusé, avec le nombre d'exigences à réaffecter d'abord.
4. Une fois tout son travail réaffecté, son retrait devient possible.
5. Le même refus s'applique à une requête directe au serveur.
6. Retirer l'un des rattachements d'une personne laisse ses autres rattachements intacts.

### US-TEAM-10 — Laisser les contributeurs d'un sous-système gérer ses rattachements
**Carte :** En tant que contributeur d'un sous-système, je veux ajouter et retirer moi-même les personnes de mon sous-système, sans manager ni tender manager, afin de staffer mon sous-système à mon rythme.
**Conversation :** Le tender manager gère le staffing de tout le tender ; chaque contributeur d'un sous-système gère les rattachements de ce sous-système (DEC-003, ACC-008). Un sous-système n'a pas besoin de manager, et le manager éventuel n'a aucun droit de plus que ses collègues (DEC-124, ACC-010). Sur un Turnkey, un contributeur SIG gère les rattachements de SIG, pas le staffing global (DEC-005). Sur un tender SIG autonome, le staffing réunit le tender manager et les contributeurs SIG, sans hiérarchie.
**Maquette :** Users — `dashboard-et-config.html` (route `#team`), Cast Activity Group (variantes modifiable et lecture seule).
**Règles :** DEC-003, DEC-005, DEC-124, ACC-008, ACC-010, ACC-T06, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Tout contributeur d'un sous-système voit la zone d'ajout et les ✕ de son sous-système, qu'il y ait un manager ou non.
2. Un contributeur ajoute un collègue à son sous-système sans aucune permission de manager.
3. Les autres sous-systèmes s'affichent pour lui en lecture seule, avec la raison.
4. Il ne peut ni ajouter un sous-système au tender ni modifier l'équipe de gestion du tender.
5. Le tender manager modifie les rattachements de tous les sous-systèmes.
6. Une modification d'un rattachement hors de son sous-système, demandée directement au serveur, est refusée.
Écart maquette : seuls le tender manager et des managers de sous-système semés sont simulés — un contributeur sans rôle de manager ne staffe rien —, et la raison affichée parle du manager (« Read-only — <nom> manages this sub-system, not you. »).
Point ouvert : la façon de désigner le manager facultatif d'un sous-système n'est spécifiée nulle part ; la maquette les sème, aucun écran ne permet d'en nommer un (DEC-030, DEC-124).

### US-TEAM-11 — Désigner automatiquement la personne d'une allocation depuis son périmètre
**Carte :** En tant que tender manager, je veux que la personne staffée sur un périmètre soit désignée d'elle-même sur les allocations qui portent cette équipe, afin de ne pas affecter à la main des centaines d'exigences.
**Conversation :** Le périmètre et l'OBS · team sont la même liste : ce que le modèle d'un sous-système dérive est un périmètre, et l'affectation est une correspondance directe (DEC-033, DEC-036). Plusieurs personnes sur un même périmètre sont toutes responsables : une allocation chacune (DEC-037, DEC-087). Le périmètre ne donne aucun droit : un contributeur agit sur tout son sous-système (DEC-033). L'affichage de la personne dans le panneau d'allocation est décrit dans US-ALM.
**Maquette :** non maquetté (le staffing n'est pas lu par Allocation) ; résultat visible dans Allocation — `revue-documentaire.html` (route `#review`), Detail / Assignment Panel.
**Règles :** DEC-033, DEC-036, DEC-037, DEC-087, DEC-025, ACC-004, ACC-014, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Quand une allocation d'un sous-système reçoit un OBS · team — dérivé par le modèle ou choisi à la main —, la personne staffée sur ce périmètre de ce sous-système en devient la personne.
2. Quand plusieurs personnes sont staffées sur ce périmètre, l'exigence reçoit une allocation par personne.
3. Quand personne n'est staffé sur ce périmètre, l'allocation reste sans personne, affichée « Unassigned », et sa validation reste possible (DEC-025).
4. Une personne staffée directement sur le sous-système, sans périmètre, n'est jamais désignée automatiquement ; elle reste proposée à la main sur les OBS de son sous-système.
5. Aucune personne n'est désignée automatiquement sur une allocation d'un autre sous-système que le sien.
Écart maquette : Allocation ne lit pas le staffing ; les personnes des OBS y sont semées à la main.
Point ouvert : sur le modèle Mainline, l'OBS est un poste et non une équipe (DEC-062) — sa correspondance avec les périmètres du staffing n'est pas tranchée ; l'effet d'un rattachement ajouté ou retiré après la dérivation sur les allocations déjà faites n'est pas spécifié.

### US-TEAM-12 — Avancer sans attendre que le staffing soit complet
**Carte :** En tant que tender manager, je veux capturer, caractériser, allouer et valider même quand le staffing est incomplet, afin qu'un staffing en retard ralentisse le tender sans jamais l'arrêter.
**Conversation :** Le staffing est permanent : ouvert dès la création, complété au fil du tender (ACC-003). La capture et la caractérisation n'en ont pas besoin ; l'allocation n'en a besoin que pour désigner les personnes. Ce qu'aucun contributeur ne couvre revient à l'équipe de gestion, qui n'a pas de restriction de sous-système. La validation elle-même est décrite dans US-ALM.
**Maquette :** Users — `dashboard-et-config.html` (route `#team`) ; Allocation — `revue-documentaire.html` (route `#review`), Validate Zone (« No one assigned yet — you can still validate »).
**Règles :** ACC-003, ACC-T10, DEC-025, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. L'écran Users est accessible dès la création du tender, puis à tout moment.
2. Un tender sans aucune personne staffée peut être capturé, caractérisé et alloué.
3. Une allocation sans personne se valide ; le manque reste affiché (« Unassigned »).
4. Aucun écran n'impose une étape « staffing terminé » avant d'allouer ou de valider.
5. Un staffing incomplet n'élargit aucun droit : un contributeur ne modifie toujours que son sous-système.

### US-TEAM-13 — Lire tout son tender, et aucun autre
**Carte :** En tant que contributeur, je veux lire tout le tender — exigences, allocations et réponses de tous les sous-systèmes —, afin de comprendre le contexte de mon travail, sans jamais voir un tender dont je ne suis pas membre.
**Conversation :** Un contributeur consulte tout son tender, autres sous-systèmes compris, sans masquage ni caviardage (DEC-012, ACC-007). Ce droit ne s'étend jamais à un autre tender (ACC-T09). Il est contrôlé par le serveur, requêtes directes, compteurs, recherche et exports compris (PLAT-002, plateforme : voir US-X). Le filtre « My sub-system » de Compliance, désactivé par défaut, n'est qu'une commodité (voir US-CMP).
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Requirement Table (Review Grid), Document Reading View ; Compliance — `compliance.html` (route `#compliance`).
**Règles :** DEC-012, ACC-007, ACC-T09, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Dans la table et la vue Document d'Allocation, un contributeur voit toutes les exigences du tender, quel que soit leur sous-système.
2. Il voit de même, dès que ces écrans sont livrés, toutes les affectations et leurs réponses dans Compliance, le registre Q&A et l'écran Users.
3. Les compteurs, la recherche et les exports qu'il lance portent sur tout le tender, sans ligne masquée ni texte caviardé.
4. Un tender dont il n'est pas membre n'apparaît pas dans sa liste de tenders.
5. Une requête directe vers un tender dont il n'est pas membre est refusée et ne révèle rien : ni contenu, ni compteur, ni résultat de recherche, ni export.

### US-TEAM-14 — Ne modifier que le travail de son sous-système
**Carte :** En tant que contributeur, je veux pouvoir modifier tout le travail de mon sous-système et rien en dehors, afin que chaque sous-système reste maître de ses allocations et de ses réponses.
**Conversation :** « Mon sous-système » est celui dont je suis membre dans le staffing, et non celui où une allocation me désigne (DEC-102, ACC-014). Sur une exigence dont aucun sous-système n'est le mien, tout est en lecture seule (DEC-100, ACC-013). L'affichage en lecture seule propre à chaque écran est décrit dans US-ALM, US-CMP et US-TAB ; ici, la règle commune et son contrôle par le serveur.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Detail / Assignment Panel en lecture seule ; Compliance — `compliance.html` (route `#compliance`), Decision Panel en lecture seule.
**Règles :** DEC-012, DEC-100, DEC-102, ACC-007, ACC-013, ACC-014, ACC-T04, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Sur une exigence de son sous-système, un contributeur dispose des actions de modification de ce sous-système, quelle que soit la personne désignée.
2. Sur une exigence dont aucun sous-système n'est le sien, il n'a aucune action de modification, ni dans le panneau, ni dans la table, ni dans la vue Document.
3. Sur une exigence à plusieurs sous-systèmes, il ne modifie que la partie de son sous-système ; les autres restent en lecture.
4. Une action groupée ignore les lignes hors de son sous-système (voir US-TAB).
5. Une modification hors de son sous-système demandée directement au serveur est refusée et ne change rien — par exemple un contributeur SIG sur un autre sous-système du même tender (ACC-T04).
6. Changer son rattachement dans le staffing change aussitôt ce qu'il peut modifier.

### US-TEAM-15 — Répondre pour un collègue de son sous-système
**Carte :** En tant que contributeur, je veux pouvoir répondre à une affectation de mon sous-système même quand elle désigne un collègue, afin que l'absence d'une personne ne bloque pas mon sous-système.
**Conversation :** Tous les contributeurs d'un sous-système sont au même niveau : pas de hiérarchie dans l'outil, et le manager éventuel n'a aucun droit de plus (DEC-012, ACC-010, DEC-124). Tous peuvent répondre pour leur sous-système, même quand la personne désignée est un collègue (DEC-002, ACC-T05). La personne de chaque allocation reste responsable de sa conformité : c'est elle qu'on relance (DEC-087). L'ancien « responsable du suivi » par exigence (ACC-009, DEC-010) n'existe plus.
**Maquette :** Compliance — `compliance.html` (route `#compliance`), Decision Panel.
**Règles :** DEC-002, DEC-012, DEC-087, DEC-124, ACC-009, ACC-010, ACC-T05, DEC-126  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Un contributeur peut rendre le verdict d'une affectation de son sous-système dont la personne désignée est un collègue.
2. La réponse garde qui l'a réellement donnée, visible dans le journal de l'exigence (voir US-X).
3. La personne désignée reste celle de l'allocation : répondre à sa place ne la remplace pas.
4. Le manager du sous-système, s'il y en a un, n'a aucune action de plus que les autres contributeurs.
5. Un contributeur d'un autre sous-système ne peut pas répondre à cette affectation.

### US-TEAM-16 — Réserver le type et la classe au tender manager
**Carte :** En tant que tender manager, je veux être le seul à pouvoir changer le type et la classe d'une exigence, afin que ce qui oriente la dérivation de chaque sous-système reste sous mon contrôle.
**Conversation :** Le type (Information, Heading, Requirement) et la classe (technique / non technique) déterminent ce que le modèle dérive pour chaque sous-système (ACC-012, DEC-086). Un contributeur les lit partout mais ne les modifie nulle part. Les contrôles de chaque écran sont décrits dans US-ALM (panneau, relance proposée), US-TAB (bascule Class, action « Classify ») et US-DOCV (vue Document) ; ici, la règle commune et son contrôle par le serveur.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Detail / Assignment Panel (« Set by the tender manager »), Requirement Table (Review Grid), Document Reading View.
**Règles :** ACC-012, DEC-086, DEC-126  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Pour un contributeur, le type et la classe s'affichent en texte, avec « Set by the tender manager », sans sélecteur.
2. Pour un contributeur, la bascule Class de la table est inactive et l'action groupée « Classify » n'est pas proposée.
3. Pour un contributeur, le sélecteur de type de la vue Document est inactif.
4. Une modification de type ou de classe demandée directement au serveur par un contributeur est refusée et ne change rien.
5. Tout membre de l'équipe de gestion du tender modifie le type et la classe, partout.

### US-TEAM-17 — Laisser le tender manager saisir ou corriger toute réponse
**Carte :** En tant que tender manager, je veux pouvoir saisir ou corriger la réponse de conformité de n'importe quelle affectation, afin de couvrir un sous-système sans personne ou de rectifier une réponse avant la remise.
**Conversation :** L'équipe de gestion du tender n'a aucune restriction de sous-système (ACC-008) : elle peut saisir et modifier des réponses (DEC-013, ACC-011), même quand toutes les réponses sont reçues (DEC-014, OPEN-14). Elle ne verrouille plus rien (DEC-028, DEC-106). La correction de la conformité externe, motif obligatoire, est décrite dans US-RSK ; le panneau du tender manager dans US-CMP.
**Maquette :** Compliance — `compliance.html` (route `#compliance`), Detail / Assignment Panel et Decision Panel (vue tender manager).
**Règles :** ACC-011, ACC-T08, DEC-013, DEC-014, DEC-126  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Un tender manager peut saisir le verdict d'une affectation de n'importe quel sous-système, qu'une personne y soit désignée ou non.
2. Il peut modifier un verdict déjà donné par un contributeur, y compris quand toutes les réponses de l'exigence sont reçues.
3. Le verdict saisi ou modifié garde son auteur et sa date, visibles dans le journal de l'exigence (voir US-X).
4. La consolidation de l'exigence se recalcule aussitôt avec ce verdict (voir US-CMP).
5. Aucune réponse n'est verrouillée : il n'existe ni action ni état « locked ».
Écart maquette : la maquette ne laisse le tender manager saisir un verdict que pour un partenaire externe (« TM · for partner », DEC-082).

## Couverture
- Règles couvertes : ACC-001 → [US-TEAM-03](#us-team-03--composer-léquipe-de-gestion-du-tender) ; ACC-002 → [US-TEAM-03](#us-team-03--composer-léquipe-de-gestion-du-tender) ; ACC-003 → [US-TEAM-01](#us-team-01--ouvrir-lécran-users-là-où-lon-a-à-agir), [US-TEAM-12](#us-team-12--avancer-sans-attendre-que-le-staffing-soit-complet) ; ACC-004 → [US-TEAM-05](#us-team-05--staffer-une-personne-sur-un-sous-système-avec-ou-sans-périmètre), [US-TEAM-11](#us-team-11--désigner-automatiquement-la-personne-dune-allocation-depuis-son-périmètre) ; ACC-005 → [US-TEAM-07](#us-team-07--staffer-une-personne-sur-plusieurs-périmètres-sans-doublon) ; ACC-006 → [US-TEAM-09](#us-team-09--retirer-une-personne-après-réaffectation-de-son-travail) ; ACC-007 → [US-TEAM-01](#us-team-01--ouvrir-lécran-users-là-où-lon-a-à-agir), [US-TEAM-13](#us-team-13--lire-tout-son-tender-et-aucun-autre), [US-TEAM-14](#us-team-14--ne-modifier-que-le-travail-de-son-sous-système) ; ACC-008 → [US-TEAM-02](#us-team-02--repérer-les-sous-systèmes-sans-personne-et-les-staffer), [US-TEAM-03](#us-team-03--composer-léquipe-de-gestion-du-tender), [US-TEAM-04](#us-team-04--ajouter-un-sous-système-au-tender-depuis-la-liste-de-référence), [US-TEAM-10](#us-team-10--laisser-les-contributeurs-dun-sous-système-gérer-ses-rattachements) ; ACC-009 (tous les contributeurs du sous-système peuvent répondre) → [US-TEAM-15](#us-team-15--répondre-pour-un-collègue-de-son-sous-système) ; ACC-010 → [US-TEAM-10](#us-team-10--laisser-les-contributeurs-dun-sous-système-gérer-ses-rattachements), [US-TEAM-15](#us-team-15--répondre-pour-un-collègue-de-son-sous-système) ; ACC-011 (saisie et modification des réponses par le tender manager) → [US-TEAM-17](#us-team-17--laisser-le-tender-manager-saisir-ou-corriger-toute-réponse) ; ACC-012 → [US-TEAM-16](#us-team-16--réserver-le-type-et-la-classe-au-tender-manager) ; ACC-013 → [US-TEAM-14](#us-team-14--ne-modifier-que-le-travail-de-son-sous-système) ; ACC-014 (une personne, un sous-système ; « mon sous-système » par appartenance ; personne d'un OBS seulement sur son sous-système) → [US-TEAM-06](#us-team-06--refuser-quune-personne-appartienne-à-deux-sous-systèmes), [US-TEAM-11](#us-team-11--désigner-automatiquement-la-personne-dune-allocation-depuis-son-périmètre), [US-TEAM-14](#us-team-14--ne-modifier-que-le-travail-de-son-sous-système) ; ACC-T01 → [US-TEAM-03](#us-team-03--composer-léquipe-de-gestion-du-tender) ; ACC-T02 → [US-TEAM-07](#us-team-07--staffer-une-personne-sur-plusieurs-périmètres-sans-doublon) ; ACC-T03 → [US-TEAM-09](#us-team-09--retirer-une-personne-après-réaffectation-de-son-travail) ; ACC-T04 → [US-TEAM-14](#us-team-14--ne-modifier-que-le-travail-de-son-sous-système) ; ACC-T05 → [US-TEAM-15](#us-team-15--répondre-pour-un-collègue-de-son-sous-système) ; ACC-T06 → [US-TEAM-10](#us-team-10--laisser-les-contributeurs-dun-sous-système-gérer-ses-rattachements) ; ACC-T07 → [US-TEAM-02](#us-team-02--repérer-les-sous-systèmes-sans-personne-et-les-staffer) ; ACC-T08 → [US-TEAM-17](#us-team-17--laisser-le-tender-manager-saisir-ou-corriger-toute-réponse) ; ACC-T09 → [US-TEAM-13](#us-team-13--lire-tout-son-tender-et-aucun-autre) ; ACC-T10 → [US-TEAM-12](#us-team-12--avancer-sans-attendre-que-le-staffing-soit-complet) ; JRN-004 → [US-TEAM-01](#us-team-01--ouvrir-lécran-users-là-où-lon-a-à-agir), [US-TEAM-02](#us-team-02--repérer-les-sous-systèmes-sans-personne-et-les-staffer), [US-TEAM-05](#us-team-05--staffer-une-personne-sur-un-sous-système-avec-ou-sans-périmètre), [US-TEAM-08](#us-team-08--retrouver-une-personne-parmi-200-personnes-staffées).
- Non couvertes, avec la raison : ACC-009, partie « la personne responsable de l'exigence garde le suivi » — caduque (remplacée par DEC-087) ; ACC-011, partie « corriger la conformité externe dérivée, motif obligatoire » — couverte par l'épopée US-RSK ; ACC-014, partie « un sous-système est validé par son contributeur ou par le TM, l'aiguillage Turnkey par le TM seul » — couverte par l'épopée US-ALM ; matrice d'ACCESS, ligne « Remplacer/verrouiller le verdict final » — caduque (plus de verrou, DEC-028 puis DEC-106) ; matrice d'ACCESS, ligne « Valider la distribution/allocation » — couverte par l'épopée US-ALM ; matrice d'ACCESS, ligne « Gérer documents et relation client globaux » — couverte par [US-QA-11](11-qa.md#us-qa-11--réserver-à-léquipe-de-gestion-le-marquage-des-questions-envoyées) (relation client) et par l'épopée US-DOC (documents).
