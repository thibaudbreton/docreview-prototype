<!-- Généré depuis le backlog du 10 octobre 2026 ; voir README.md pour les conventions. -->
# Tables communes Allocation et Compliance (US-TAB)

Le chef de projet et les contributeurs passent l'essentiel de leur temps dans les tables d'Allocation et de Compliance : isoler ce qui reste à faire, inspecter, corriger, valider en série (JRN-002 ; JRN-003 sur Compliance). Les deux écrans partagent une seule mécanique de table (UX-001) : chaque comportement est écrit une fois ici, avec ses différences par écran ; les actions métier des barres d'actions sont dans US-ALM et US-CMP. Allocation est dans le premier pilote, Compliance vient après (DEC-022).
- **Ligne de titre** : ligne qui reprend un document, une section ou un sous-titre du tender, pour garder le fil du texte.
- **Filtre de colonne** : liste de valeurs à cocher, ouverte depuis l'entonnoir d'un en-tête, comme dans Excel ; **filtre avancé** : des conditions combinées par ET / OU.
- **Cellule active** : la case où se trouve le clavier, comme dans un tableur ; **sélection** : les lignes cochées, sur lesquelles agit la barre d'actions groupées.
- **Colonne personnalisée** : colonne ajoutée au tender par un chef de projet, remplie par des personnes, jamais par l'IA.

### US-TAB-01 — Lire la table dans l'ordre du document
**Carte :** En tant que chef de projet ou contributeur, je veux voir les exigences dans l'ordre du document, sous leurs titres, afin de suivre le fil du tender tel que le client l'a écrit.
**Conversation :** C'est l'ordre par défaut des deux tables, et celui auquel on revient toujours (DEC-078, DEC-083). Les exigences d'un même sujet se suivent dans le document, ce qui rend utiles les sélections de plages et les actions en série. Allocation montre des lignes de document, de section et de sous-titre, puis les exigences et les blocs d'information à leur place ; Compliance montre les lignes de document et de section, et chaque exigence y porte ses lignes par système derrière une flèche ([US-TAB-02](#us-tab-02--déplier-une-exigence-en-lignes-par-système-et-par-organisation) ; voir aussi [US-CMP-05](09-compliance.md#us-cmp-05--lire-la-table-dans-lordre-du-document)). Un tri par colonne met la table à plat ([US-TAB-05](#us-tab-05--trier-par-un-en-tête-de-colonne)) ; dans Allocation, le menu « View » peut limiter la table à un seul document ([US-TAB-11](#us-tab-11--choisir-masquer-et-réordonner-les-colonnes)).
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Requirement Table (Review Grid), Grid Section / Group Header ; Compliance — `compliance.html` (route `#compliance`), mêmes composants.
**Règles :** DEC-078, DEC-083, CONF-022, DEC-073, UX-001, JRN-002 · **Périmètre :** Pilote 1 (Allocation) ; Compliance : après pilote · **Variantes :** Toutes
**Critères d'acceptation :**
1. Sans tri, sur les deux écrans, chaque exigence s'affiche sous la ligne de son document puis de sa section, dans l'ordre des documents puis du texte.
2. Une ligne de section affiche son numéro, son titre et le nombre d'exigences qu'elle contient.
3. Les lignes de document, de section et de sous-titre n'ont ni case de sélection ni statut, et ↑/↓ passent par-dessus.
4. Dans Allocation, un bloc d'information a une ligne réduite, sans statut, sans système ni allocation (DEC-073), et aucun filtre de statut ne le retient.
5. Une section dont aucune ligne ne passe la recherche et les filtres en cours n'affiche pas sa ligne de titre.

### US-TAB-02 — Déplier une exigence en lignes par système et par organisation
**Carte :** En tant que chef de projet ou contributeur, je veux déplier une exigence répartie sur plusieurs systèmes ou organisations, afin de voir chaque part sous la ligne de l'exigence, sans la dupliquer.
**Conversation :** Une exigence reste une seule ligne ; ses parts se lisent dessous, à la demande (ALLOC-004). La flèche est dans la cellule du texte, au même endroit sur les deux écrans (DEC-081). Ce que montre chaque sous-ligne est décrit dans [US-ALM-11](05-allocation.md#us-alm-11--suivre-une-exigence-répartie-sur-plusieurs-systèmes) (Allocation) et [US-CMP-04](09-compliance.md#us-cmp-04--déplier-une-exigence-en-systèmes-et-en-organisations) (Compliance) ; cette story ne décrit que la mécanique commune.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Disclosure / Expand Chevron et Branch / Allocated-Activity Sub-row ; Compliance — `compliance.html` (route `#compliance`), mêmes composants.
**Règles :** ALLOC-004, DEC-055, DEC-060, DEC-081, CONF-025, UX-001 · **Périmètre :** Pilote 1 (Allocation) ; Compliance : après pilote · **Variantes :** Toutes
**Critères d'acceptation :**
1. Dans Allocation, une exigence à plusieurs systèmes porte une flèche dans sa cellule « Requirement » ; dans Compliance, toute exigence à plusieurs affectations ; les sous-lignes sont repliées par défaut et la flèche les déplie ou les replie.
2. Un système qui compte plusieurs organisations a sa propre flèche, qui déplie un second niveau d'une ligne par organisation.
3. Une exigence dépliée le reste quand on trie, filtre ou passe par la vue Document, et ses sous-lignes restent toujours juste sous elle.
4. Les sous-lignes n'ont pas de case de sélection : X sur une sous-ligne coche son exigence, et une action groupée porte sur l'exigence entière.
5. ↑/↓ passent aussi par les sous-lignes affichées.
6. Sur une sous-ligne, les cellules qui ne valent que pour l'exigence entière (Changes, colonnes personnalisées) restent vides.

### US-TAB-03 — Filtrer d'un clic sur un compteur de statut
**Carte :** En tant que chef de projet ou contributeur, je veux cliquer sur un compteur de la barre de statut pour ne garder que ce statut, afin d'isoler d'un geste ce qui reste à revoir ou à valider.
**Conversation :** C'est le premier geste du parcours : isoler ce qui attend une décision (JRN-002). Les compteurs et ce qu'ils comptent sont décrits dans [US-ALM-03](05-allocation.md#us-alm-03--suivre-lavancement-dans-la-barre-de-statut) (Allocation) et [US-CMP-07](09-compliance.md#us-cmp-07--suivre-lavancement-de-la-consolidation) (Compliance) ; la pastille « changed in latest version » dans [US-CHG-01](08-changements.md#us-chg-01--revoir-une-exigence-ajoutée-ou-modifiée-par-une-nouvelle-version), les pastilles « set aside » et « my system » du contributeur dans [US-CMP-14](09-compliance.md#us-cmp-14--mettre-une-affectation-de-côté) et [US-CMP-08](09-compliance.md#us-cmp-08--consulter-tout-le-tender-et-nagir-que-sur-son-système). Un seul compteur filtre à la fois, en plus de la recherche et des autres filtres. Dans Allocation, il agit aussi sur le plan et la vue Document.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Triage Bar (pastilles de statut, « ✕ Clear filter ») ; Compliance — `compliance.html` (route `#compliance`), Triage Bar, Filter Pill.
**Règles :** UX-002, JRN-002, DEC-073, DEC-012 · **Périmètre :** Pilote 1 (Allocation) ; Compliance : après pilote · **Variantes :** Toutes
**Critères d'acceptation :**
1. Cliquer un compteur de statut ne garde que les exigences (dans Compliance, les affectations) de ce statut, et le compteur actif est mis en évidence.
2. Un seul compteur est actif à la fois : en cliquer un autre remplace le premier ; recliquer le compteur actif retire le filtre.
3. Tant qu'un compteur filtre, « ✕ Clear filter » est visible et le retire.
4. Le filtre de statut se combine avec la recherche, les filtres de colonne et le filtre avancé.
5. Dans Allocation, un filtre de statut écarte les titres et les blocs d'information, qui n'ont pas de statut (DEC-073), et estompe dans le plan et la vue Document les exigences qu'il écarte.
6. Les compteurs restent ceux de tout le tender, quel que soit le filtre posé.

### US-TAB-04 — Rechercher une exigence par son identifiant ou son texte
**Carte :** En tant que chef de projet ou contributeur, je veux taper un identifiant ou un mot, afin de retrouver tout de suite les exigences qui en parlent.
**Conversation :** Le champ « Search requirement, ID… » est en tête de la barre d'outils et ne bouge jamais. Il cherche dans l'identifiant et le texte de l'exigence ; sur Compliance, il trouve aussi le système et la personne d'une affectation. Dans Allocation, la recherche de la table et celle du plan de la vue Document sont un seul champ ([US-DOCV-02](07-vue-document.md#us-docv-02--naviguer-dans-le-plan-du-tender)). Un contributeur cherche dans tout le tender, qu'il lit en entier (DEC-012).
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Search Box du Filter Toolbar ; Compliance — `compliance.html` (route `#compliance`), même composant.
**Règles :** UX-001, UX-005, DEC-012, DEC-023, PLAT-002 · **Périmètre :** Pilote 1 (Allocation) ; Compliance : après pilote · **Variantes :** Toutes
**Critères d'acceptation :**
1. Taper dans « Search requirement, ID… » ne garde que les exigences dont l'identifiant ou le texte contient la saisie, sans tenir compte des majuscules.
2. La recherche se combine avec les filtres : une ligne affichée satisfait les deux.
3. Sur Compliance, une saisie contenue dans le code d'un système ou dans le nom d'une personne affectée retient aussi l'exigence.
4. La recherche porte sur toutes les exigences du tender ouvert, y compris celles qui ne sont pas encore affichées (jusqu'à 100 000 lignes), et jamais sur un autre tender.
5. Vider le champ rend la table telle que la laissent les seuls filtres actifs.
Écart maquette : la recherche d'Allocation trouve encore les valeurs Functional / Performance…, sorties d'Allocation (ALLOC-T26) ; elle tourne dans le navigateur, sur les lignes chargées.
Point ouvert : temps de réponse attendu à 100 000 lignes (OPEN-08, PLAT-007).

### US-TAB-05 — Trier par un en-tête de colonne
**Carte :** En tant que chef de projet ou contributeur, je veux trier la table d'un clic sur un en-tête, afin de rapprocher ce qui se ressemble (même statut, même personne, même système) le temps d'un passage.
**Conversation :** Comme dans un tableur : ordre croissant, décroissant, puis retour à l'ordre du document. Compliance n'a plus de liste « Sort: … » ni d'ordre « action needed first » (DEC-083). Un tri est une vue à plat, sans lignes de titre. Dans Allocation, les colonnes ID, Class, System, ABS, PBS, OBS, Assigned to et Status se trient ; dans Compliance, toutes les colonnes ; les colonnes personnalisées se trient sur les deux écrans.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), en-têtes du Requirement Table (Review Grid) et « ↺ Document order » du Filter Toolbar ; Compliance — `compliance.html` (route `#compliance`), mêmes zones.
**Règles :** DEC-083, CONF-027, DEC-078, UX-001, UX-005, DEC-023 · **Périmètre :** Pilote 1 (Allocation) ; Compliance : après pilote · **Variantes :** Toutes
**Critères d'acceptation :**
1. Un premier clic sur l'en-tête d'une colonne triable trie en ordre croissant (▲), un deuxième en ordre décroissant (▼), un troisième rend l'ordre du document.
2. Tant qu'un tri est actif, la table est à plat et « ↺ Document order » est visible ; ce bouton rend l'ordre du document avec ses lignes de titre.
3. Un seul tri à la fois : trier une autre colonne remplace le tri précédent.
4. Le tri porte sur toutes les lignes que les filtres retiennent dans le tender, y compris celles qui ne sont pas encore affichées (UX-005).
5. Un clic sur un en-tête ne masque jamais la colonne ; le masquage passe par « View » ([US-TAB-11](#us-tab-11--choisir-masquer-et-réordonner-les-colonnes)).
Écart maquette : le tri se fait dans le navigateur, sur les lignes chargées.

### US-TAB-06 — Filtrer une colonne comme dans Excel
**Carte :** En tant que chef de projet ou contributeur, je veux cocher, depuis l'en-tête d'une colonne, les valeurs à garder, afin d'isoler vite un statut, un système ou une personne.
**Conversation :** La plupart des filtrages portent sur une seule colonne : l'entonnoir de l'en-tête suffit (UX-002). Allocation en propose sur Changes, Class, System, Assigned to, Status et les colonnes personnalisées de type liste ; Compliance sur System et Assigned to, où une exigence reste si l'une de ses affectations passe. « Assigned to » a une valeur par entrée OBS : une exigence correspond à une personne si l'une de ses entrées est à elle, et à « Unassigned » si l'une n'a personne (DEC-123) ; un Turnkey avec partenaire ajoute « PM · for partner » (DEC-082). Filtrer ne modifie aucune donnée.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Column Filter Section (entonnoir d'en-tête) ; Compliance — `compliance.html` (route `#compliance`), même composant.
**Règles :** UX-001, UX-002, UX-005, DEC-023, DEC-123, DEC-082, TYPE-T08, JRN-002 · **Périmètre :** Pilote 1 (Allocation) ; Compliance : après pilote · **Variantes :** Toutes (sur SIG, pas de filtre System)
**Critères d'acceptation :**
1. L'entonnoir d'un en-tête ouvre la liste des valeurs de la colonne, toutes cochées au départ, avec « All » et « None ».
2. Décocher une valeur retire aussitôt les lignes qui n'ont que des valeurs décochées ; le pied affiche « k of n shown » et « Clear ».
3. L'entonnoir d'une colonne filtrée reste en évidence, avec l'infobulle « Filtered — <colonne> ».
4. Des filtres posés sur plusieurs colonnes se cumulent : une ligne doit les passer tous.
5. Le filtre porte sur toutes les lignes du tender, pas seulement celles déjà affichées, jusqu'à 100 000 lignes (UX-005).
6. Sur un tender SIG, la colonne System n'existe pas et aucun filtre ne la propose (TYPE-T08).
Écart maquette : le filtrage tourne dans le navigateur, sur les lignes chargées, sans serveur.
Point ouvert : temps de réponse attendu à 100 000 lignes et comportement d'une table servie par pages (OPEN-08, OPEN-13).

### US-TAB-07 — Construire un filtre avancé
**Carte :** En tant que chef de projet ou contributeur, je veux combiner plusieurs conditions avec ET / OU, afin de poser une question précise à la table et de travailler exactement sur ses réponses.
**Conversation :** Le filtre avancé sert à ce qu'un entonnoir ne sait pas dire (UX-003), par exemple « Status is To review AND System is any of SIG, SEN ». Les conditions se lient par « Match all / any of » ; un seul niveau de groupes, chacun avec son propre ET / OU, sans imbrication plus profonde. Les champs sont ceux de l'écran, rangés par usage — Allocation : Progress, Characterisation, Allocation, Content & source ; Compliance : Progress, Assignment, Content & source ; plus « Custom columns » ([US-TAB-23](#us-tab-23--filtrer-et-trier-sur-une-colonne-personnalisée)). Un champ sans objet sur l'écran n'est pas proposé, comme System sur un tender SIG.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), bouton « Filter ▾ » et Advanced Filter Builder (Advanced Filter Condition Row) ; Compliance — `compliance.html` (route `#compliance`), même constructeur.
**Règles :** UX-003, UX-005, DEC-066, DEC-023, JRN-002 · **Périmètre :** Pilote 1 (Allocation) ; Compliance : après pilote · **Variantes :** Toutes
**Critères d'acceptation :**
1. « + Add condition » et « + Add group » ajoutent une condition ou un groupe ; le haut de la liste et chaque groupe ont leur choix « Match all / any of ».
2. Les opérateurs suivent le type du champ : texte (« contains », « does not contain », « is », « is not », « starts with », « is empty », « is not empty »), liste (« is », « is not », « is any of », « is none of », « is empty »), date (« before », « after », « between », « in the last N days », « is empty »).
3. Pendant la construction, « N of M requirements » se met à jour et compte sur tout le tender, pas seulement sur les lignes chargées.
4. Quand rien ne correspond, le constructeur affiche « Nothing matches » et, s'il peut la trouver, la condition qui à elle seule ne garde rien.
5. Rien ne change dans la table avant « Apply » ; « Cancel » referme sans rien appliquer.
6. Une condition sans valeur est marquée « needs a value », et « Apply » reste inactif tant qu'elle n'est pas complétée ou retirée.

### US-TAB-08 — Lire en clair ce qui filtre la table et tout effacer
**Carte :** En tant que chef de projet ou contributeur, je veux lire en une phrase tout ce qui réduit la table et l'effacer d'un geste, afin de toujours savoir ce que je ne vois pas.
**Conversation :** Les filtres de colonne et le filtre avancé forment un seul état actif, pas deux indicateurs concurrents (UX-002). Une phrase en clair le dit dans la barre d'outils, juste après la recherche : un filtre qu'on ne peut pas relire n'inspire pas confiance. Le constructeur part des filtres de colonne actifs, pour ne pas refaire ce qu'on vient de faire. Filtrer sélectionne ; seules les actions groupées modifient.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Filter Toolbar (phrase du filtre actif et son ✕) ; Compliance — `compliance.html` (route `#compliance`), même zone.
**Règles :** UX-002, UX-003 · **Périmètre :** Pilote 1 (Allocation) ; Compliance : après pilote · **Variantes :** Toutes
**Critères d'acceptation :**
1. Dès qu'un filtre de colonne ou un filtre avancé est actif, une phrase en clair s'affiche après la recherche (par exemple « System is not TRK AND Status is any of To review »), entière au survol.
2. Le ✕ de cette phrase efface d'un coup les filtres de colonne et le filtre avancé.
3. Le bouton « Filter » porte le nombre de conditions du filtre avancé en cours.
4. Dès qu'un filtre ou la recherche réduit la table, le compte s'affiche (Allocation : « N of M shown » ; Compliance : « N of M requirements · K assignments shown ») ; une table vide le dit (« No requirement matches the current view. » / « No assignment matches the current view. »).
5. Ouvert sans filtre avancé, le constructeur reprend les filtres de colonne actifs comme premières conditions et l'annonce (« Started from your N active column filters… »).
6. Aucun filtre, aucune recherche et aucun tri ne modifie une donnée.

### US-TAB-09 — Enregistrer un filtre et le réutiliser sur un autre tender
**Carte :** En tant que chef de projet ou contributeur, je veux nommer un filtre avancé et le retrouver sur mes autres tenders, afin de refaire mes passages habituels sans le reconstruire.
**Conversation :** La vraie valeur du filtre avancé, c'est la répétition : les mêmes passages reviennent à chaque tender (UX-004). Un filtre enregistré est personnel, sans partage implicite, et propre à une table : un filtre d'Allocation n'est proposé que dans Allocation, un filtre de Compliance que dans Compliance. Ce que devient une condition sur un champ absent du tender ouvert (colonne personnalisée d'un autre tender, System sur un SIG) n'est pas décidé.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), section « Saved filters » de l'Advanced Filter Builder ; Compliance — `compliance.html` (route `#compliance`), même section.
**Règles :** UX-004 · **Périmètre :** Pilote 1 (Allocation) ; Compliance : après pilote · **Variantes :** Toutes
**Critères d'acceptation :**
1. Dès qu'une condition complète existe, « Save current as… » puis « Save » enregistrent le filtre sous un nom ; sans nom, l'enregistrement est refusé (« Name the filter before saving »).
2. « Saved filters » liste les filtres de la personne pour cette table, avec leur nombre (« N saved · reusable on any tender »).
3. Cliquer un filtre enregistré le charge dans le constructeur ; il ne s'applique qu'avec « Apply ».
4. Le ✕ d'un filtre enregistré le supprime.
5. Un filtre enregistré sur un tender est proposé sur tout autre tender, pour la même table.
6. Les filtres enregistrés d'une personne ne sont visibles par aucune autre.
Écart maquette : les filtres sont gardés dans le navigateur, pas rattachés au compte de la personne.
Point ouvert : condition portant sur un champ absent du tender ouvert (UX-004, OPEN-13).

### US-TAB-10 — Afficher le texte complet des exigences
**Carte :** En tant que chef de projet ou contributeur, je veux basculer entre un extrait d'une ligne et le texte complet, afin de lire sans ouvrir le détail, ou de voir plus de lignes à la fois.
**Conversation :** Par défaut, chaque ligne montre un extrait d'une ligne. L'interrupteur « Wrap text » affiche le texte entier, sur les deux écrans (DEC-078). Dans Allocation, il déplie aussi les cellules qui résument : System et Changes.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Toggle Switch « Wrap text » du Filter Toolbar ; Compliance — `compliance.html` (route `#compliance`), même interrupteur.
**Règles :** DEC-078, CONF-022, DEC-119 · **Périmètre :** Pilote 1 (Allocation) ; Compliance : après pilote · **Variantes :** Toutes
**Critères d'acceptation :**
1. « Wrap text » activé, chaque exigence montre son texte complet ; désactivé, un extrait d'une ligne terminé par « … ».
2. Basculer garde la cellule active, la sélection, les filtres et le tri.
3. Dans Allocation, avec « Wrap text », la cellule System montre toutes les étiquettes de systèmes au lieu de « +N ».
4. Dans Allocation, avec « Wrap text », la cellule Changes montre toute l'exigence avec ses changements ([US-CHG-02](08-changements.md#us-chg-02--lire-les-changements-dans-la-colonne-changes)).

### US-TAB-11 — Choisir, masquer et réordonner les colonnes
**Carte :** En tant que chef de projet ou contributeur, je veux choisir les colonnes affichées et leur ordre, afin d'adapter la table à la tâche du moment.
**Conversation :** Le menu « View » liste les colonnes facultatives sous « Table columns » : une case pour afficher ou masquer, une poignée pour glisser (UX-001). ID et Requirement restent en tête, toujours visibles ; un clic sur un en-tête trie et ne masque plus. Dans Allocation, « View » porte aussi le choix du document et le regroupement « Group by » ; sur un Turnkey, les colonnes par défaut de la vue chef de projet et de la vue système relèvent de US-ALM.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Columns Panel (« View ▾ », Reorderable Column Row) ; Compliance — `compliance.html` (route `#compliance`), Column Visibility Menu.
**Règles :** UX-001, DEC-097, TYPE-T08 · **Périmètre :** Pilote 1 (Allocation) ; Compliance : après pilote · **Variantes :** Toutes (sur SIG, pas de « Group by » System)
**Critères d'acceptation :**
1. « View ▾ » liste les colonnes facultatives de l'écran, colonnes personnalisées comprises (marquées « custom »), cochées si elles sont affichées.
2. Décocher une colonne la retire de la table ; la recocher la remet à sa place.
3. Glisser une colonne dans la liste change sa place dans la table, et ←/→ suivent ce nouvel ordre.
4. ID et Requirement ne sont pas dans la liste et restent toujours en tête.
5. Dans Allocation, « Document » limite la table et la vue Document à un seul document (« All documents » pour revenir) et vide la sélection.
6. Dans Allocation, « Group by » « System » range les exigences sous un en-tête par système ; un tri par colonne remet « None ».
Point ouvert : rien ne dit si l'affichage et l'ordre des colonnes sont retenus d'une visite à l'autre, ni pour qui ; seul l'affichage d'une colonne personnalisée est retenu par écran (DEC-097).

### US-TAB-12 — Redimensionner les colonnes
**Carte :** En tant que chef de projet ou contributeur, je veux élargir ou réduire une colonne, afin de lire ce qui compte sans perdre de place.
**Conversation :** Ajouté sans décision dédiée, sur les deux tables : une poignée au bord droit de chaque en-tête, sauf la colonne des cases. La table se pilote au clavier, sa mise en page aussi. Les largeurs sont retenues pour ce tender et cette table.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Column Resize Handle et « Reset column widths » du Columns Panel ; Compliance — `compliance.html` (route `#compliance`), mêmes composants.
**Règles :** UX-001 (comportement sans DEC) · **Périmètre :** Pilote 1 (Allocation) ; Compliance : après pilote · **Variantes :** Toutes
**Critères d'acceptation :**
1. Glisser la poignée d'un en-tête change la largeur de la colonne en direct, sans descendre sous une largeur minimale lisible.
2. Un double-clic sur la poignée rend la largeur par défaut.
3. La poignée prend le focus clavier ; ← et → réduisent ou élargissent alors la colonne par petits pas.
4. Les largeurs choisies sont retrouvées en revenant sur la même table du même tender, et seulement là.
5. « Reset column widths » apparaît dans « View » dès qu'une largeur a changé et remet toutes les colonnes par défaut (« Column widths back to default »).
Écart maquette : les largeurs sont perdues au rechargement de la page.
Point ouvert : largeurs propres à chaque personne ou communes au tender — non décidé.

### US-TAB-13 — Sélectionner plusieurs lignes et agir en une fois
**Carte :** En tant que chef de projet ou contributeur, je veux sélectionner plusieurs lignes d'un geste et agir sur elles depuis une barre, afin d'appliquer une même correction à toute une série.
**Conversation :** Les exigences d'un même sujet se suivent : une plage sélectionnée d'un geste puis une action remplacent douze gestes (UX-001). Cette story décrit la mécanique ; les actions sont dans US-ALM (« Assign », « Re-run », « Classify », « Mark to review », « Validate ») et US-CMP (« ↪ Reassign contributor », « Send reminder »). Un contributeur sélectionne dans tout le tender, qu'il lit en entier (DEC-012), mais n'agit que sur son système (DEC-100). La barre n'existe que sur la table, pas dans la vue Document.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Checkbox de ligne et Bulk Selection Action Bar ; Compliance — `compliance.html` (route `#compliance`), mêmes composants.
**Règles :** UX-001, DEC-012, DEC-100, PLAT-002, JRN-002 · **Périmètre :** Pilote 1 (Allocation) ; Compliance : après pilote · **Variantes :** Toutes
**Critères d'acceptation :**
1. Cocher la case d'une ligne la sélectionne ; dans Allocation, Maj+clic sur une autre case sélectionne toute la plage entre les deux.
2. Appuyer dans la colonne des cases puis glisser sélectionne (ou désélectionne) toutes les lignes parcourues, sans toucher au reste de la sélection.
3. La case de l'en-tête sélectionne toutes les lignes que les filtres montrent.
4. Dès qu'une ligne est sélectionnée, la barre d'actions apparaît en bas avec « N selected » et un ✕ qui vide la sélection ; dans Allocation, « Select all N » l'étend à tout ce que les filtres montrent.
5. Pour un contributeur, une action groupée ne modifie que les exigences de son système ; les autres restent telles quelles, le message les compte (« k selected requirements are not on your system — left as is »), et le serveur refuse lui aussi de les modifier.
6. Après une action groupée, un message dit combien de lignes ont changé et combien ont été laissées, avec la raison (par exemple « 8 of 10 validated — 2 were not ready »), puis la sélection est vidée.
Écart maquette : Compliance n'a ni Maj+clic ni « Select all N ».
Point ouvert : sélectionner tout ce que montrent les filtres quand la table est servie par pages, à 100 000 lignes (UX-006, OPEN-13).

### US-TAB-14 — Ne montrer que les lignes sélectionnées
**Carte :** En tant que chef de projet ou contributeur, je veux ne garder à l'écran que ma sélection, afin de travailler sur ce lot sans le reste de la table.
**Conversation :** « Show only these » dans Allocation, « Show only selected » dans Compliance, depuis la barre d'actions. Le mode remplace la barre d'outils par un bandeau ; la recherche et les filtres de colonne sont suspendus, pas perdus (UX-006). Sa composition avec le filtre avancé et avec une sélection sur plusieurs pages reste à définir.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Bulk Selection Action Bar et bandeau « Show all » ; Compliance — `compliance.html` (route `#compliance`), mêmes composants.
**Règles :** UX-006, UX-002, UX-001 · **Périmètre :** Pilote 1 (Allocation) ; Compliance : après pilote · **Variantes :** Toutes
**Critères d'acceptation :**
1. « Show only these » (Allocation) ou « Show only selected » (Compliance) ne laisse dans la table que les lignes sélectionnées.
2. Un bandeau « Showing N of M requirements — selected » remplace la barre d'outils, avec « Show all ».
3. Pendant ce mode, la recherche et les filtres de colonne ne s'appliquent pas, sans être effacés.
4. « Show all » rend la table avec exactement la recherche et les filtres de colonne d'avant.
5. Les actions groupées restent disponibles sur la sélection pendant ce mode.
Point ouvert : composition avec le filtre avancé et la sélection de toutes les pages (UX-006, OPEN-13).

### US-TAB-15 — Se déplacer et sélectionner au clavier
**Carte :** En tant que chef de projet ou contributeur, je veux parcourir la table et composer ma sélection sans la souris, afin de garder la vitesse d'un tableur.
**Conversation :** La table se pilote comme un tableur : une cellule active, visible, que les flèches déplacent (UX-001). Les touches de sélection sont les mêmes sur les deux écrans (DEC-085). Dans Allocation, ces touches agissent sur la table (« Review »), pas dans la vue Document. Dans un champ de saisie, les touches gardent leur comportement habituel.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Requirement Table (Review Grid), cellule active ; Compliance — `compliance.html` (route `#compliance`), même table.
**Règles :** DEC-085, UX-001, CUST-T10 · **Périmètre :** Pilote 1 (Allocation) ; Compliance : après pilote · **Variantes :** Toutes
**Critères d'acceptation :**
1. Un clic dans une cellule en fait la cellule active, encadrée ; ↑/↓ (ou J/K) changent de ligne, ←/→ de colonne dans l'ordre affiché, colonnes réordonnées et personnalisées comprises.
2. La table défile pour garder la cellule active visible, en hauteur comme en largeur.
3. X coche ou décoche la ligne active, depuis n'importe quelle colonne ; Espace fait de même sur la colonne des cases.
4. Maj+↑/↓ (ou Maj+J/K) étend la sélection ligne par ligne depuis la ligne active.
5. ⌘/Ctrl+A sélectionne toutes les lignes que les filtres montrent et l'annonce (« N selected — everything in view ») ; Échap vide la sélection.
6. Dans un champ de saisie, ⌘/Ctrl+A et ⌘/Ctrl+Z agissent sur le texte du champ, pas sur la table.
Écart maquette : sur Compliance, ←/→ suivent un ordre de colonnes figé, pas l'ordre affiché.

### US-TAB-16 — Éditer une cellule au clavier
**Carte :** En tant que chef de projet ou contributeur, je veux ouvrir, valider ou annuler l'édition d'une cellule au clavier, afin de remplir une colonne en descendant, comme dans Excel.
**Conversation :** Toute cellule modifiable s'édite au clavier, colonnes personnalisées comprises (CUST-T10) : champ texte, liste ou sélecteur à choix multiple. Entrée valide et descend, ce qui permet de saisir une colonne d'affilée. Ce qu'un utilisateur peut modifier dépend de son rôle et de son système (US-ALM, US-CMP) ; une cellule en lecture seule ne s'ouvre pas, comme la bascule Class pour un contributeur (DEC-086, [US-ALM-06](05-allocation.md#us-alm-06--réserver-la-nature-et-la-classe-au-chef-de-projet)).
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Requirement Row et Custom Column Cell ; Compliance — `compliance.html` (route `#compliance`), Custom Column Cell.
**Règles :** CUST-T10, DEC-085, DEC-100, UX-001 · **Périmètre :** Pilote 1 (Allocation) ; Compliance : après pilote · **Variantes :** Toutes
**Critères d'acceptation :**
1. Entrée ou F2 sur la cellule active ouvre son édition ; sur une cellule qui ne se modifie pas, la touche ne fait rien.
2. En édition, Entrée valide la valeur et descend d'une ligne dans la même colonne.
3. En édition, Échap remet la valeur d'avant et sort de l'édition.
4. Dans un sélecteur à choix multiple, ↑/↓ passent d'une option à l'autre, Espace coche ou décoche, Entrée valide et descend, Échap remet les valeurs d'avant.
5. Dans Allocation, A place le curseur dans « Assigned to » de la ligne sélectionnée.
6. Une cellule verrouillée pour le lecteur (exigence d'un autre système pour un contributeur, DEC-100) ne s'ouvre pas en édition.
Écart maquette : sur Compliance, Entrée ou F2 n'ouvre pas l'édition d'une cellule ; seules Entrée (valider) et Échap (rétablir) y fonctionnent, une fois dans le champ.

### US-TAB-17 — Aller à la prochaine exigence qui m'attend et valider au clavier
**Carte :** En tant que chef de projet ou contributeur, je veux sauter d'une touche à la prochaine exigence qui m'attend, et valider sans la souris, afin d'enchaîner les décisions sans chercher.
**Conversation :** N cherche, après la ligne active et dans ce que les filtres montrent, la prochaine exigence qui attend une action du lecteur (DEC-085). Ce qui « attend » dépend de l'écran : dans Allocation, To review ou To validate ; dans Compliance, pour le contributeur ses affectations à décider hors mises de côté, pour le chef de projet une réaffectation, un verdict partenaire à saisir ou un Not compliant sans déclaration (états décrits dans US-CMP). V, dans Allocation, déclenche la validation décrite dans [US-ALM-26](05-allocation.md#us-alm-26--valider-une-exigence-en-un-seul-geste). Les touches R, Q et S de Compliance sont dans US-CMP.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Requirement Table (Review Grid) ; Compliance — `compliance.html` (route `#compliance`), même table.
**Règles :** DEC-085, DEC-099, DEC-102, JRN-002 · **Périmètre :** Pilote 1 (Allocation) ; Compliance : après pilote · **Variantes :** Toutes
**Critères d'acceptation :**
1. Dans Allocation, N sélectionne la prochaine exigence To review ou To validate (sur elle-même ou sur l'un de ses systèmes) après la ligne active, en boucle dans ce que les filtres montrent, et y place la cellule active.
2. Pour un contributeur, N ne s'arrête que sur des exigences de son système (DEC-102).
3. Dans Compliance, N s'arrête sur la prochaine exigence qui attend le lecteur, selon son rôle.
4. Quand rien n'attend, N le dit (« Nothing left to review or validate in this view ») et ne déplace rien.
5. Dans Allocation, V valide les lignes sélectionnées s'il y en a, sinon l'exigence active ; une ligne qui n'est pas prête reste telle quelle et le message la compte.
Point ouvert : « un Not compliant sans déclaration » (DEC-085) date d'avant la conformité externe dérivée (DEC-106) et les manques signalés (DEC-108) ; la maquette arrête N, pour le contributeur, sur ses Not compliant sans stratégie ou sans risque — à confirmer.

### US-TAB-18 — Annuler la dernière action, même après le message
**Carte :** En tant que chef de projet ou contributeur, je veux annuler ma dernière action avec ⌘/Ctrl+Z, même quand son message a disparu, afin de réparer une erreur sans la refaire à la main.
**Conversation :** Toute action annulable affiche un message avec « Undo » ; le bouton et le raccourci annulent la même action, une seule fois, de la plus récente à la plus ancienne (DEC-085). Sont annulables : dans Allocation, l'assignation d'une personne et la validation, unitaire et groupée (US-ALM) ; dans Compliance, le verdict, le verdict partenaire, la question au client, le renvoi, la réaffectation et la mise de côté (US-CMP). Dans un champ texte, ⌘/Ctrl+Z annule la frappe, comme d'habitude.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Toast (bouton « Undo ») ; Compliance — `compliance.html` (route `#compliance`), même composant.
**Règles :** DEC-085 · **Périmètre :** Pilote 1 (Allocation) ; Compliance : après pilote · **Variantes :** Toutes
**Critères d'acceptation :**
1. Une action annulable affiche un message avec « Undo » ; le cliquer rend exactement l'état d'avant l'action.
2. ⌘/Ctrl+Z annule la dernière action annulable même après la disparition de son message, et l'annonce (« Undone — … »).
3. Des ⌘/Ctrl+Z successifs annulent les actions de la plus récente à la plus ancienne ; une action déjà annulée par le bouton ne l'est pas une seconde fois.
4. Sans action à annuler, ⌘/Ctrl+Z affiche « Nothing to undo » et ne change rien.
5. Annuler une action groupée la défait sur toutes les lignes concernées en une fois.
6. Le curseur dans un champ texte, ⌘/Ctrl+Z annule la saisie du champ et aucune action de la table.
Écart maquette : dans Allocation, seule l'assignation faite dans la cellule « Assigned to » d'une ligne s'annule, pas l'assignation groupée ni celle du panneau ; les annulations possibles sont perdues en quittant l'écran.
Point ouvert : portée de l'annulation côté serveur — après un rechargement, ou quand une autre personne a modifié la même exigence entre-temps (DEC-085 décrit le geste, pas sa portée).

### US-TAB-19 — Consulter l'aide clavier au survol
**Carte :** En tant que chef de projet ou contributeur, je veux voir les raccourcis de l'écran quand j'en ai besoin, afin de les apprendre sans qu'ils encombrent la barre d'outils.
**Conversation :** Les raccourcis ne sont plus affichés en permanence (DEC-081) : une icône ⌨ en bout de barre d'outils les montre sur demande. Chaque écran liste ses propres touches.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Shortcut Help (Kbd Key) ; Compliance — `compliance.html` (route `#compliance`), même composant.
**Règles :** DEC-085, DEC-081, DEC-119 · **Périmètre :** Pilote 1 (Allocation) ; Compliance : après pilote · **Variantes :** Toutes
**Critères d'acceptation :**
1. L'icône ⌨ en bout de barre d'outils ouvre la liste des raccourcis au survol et quand elle reçoit le focus clavier.
2. La liste range les touches par usage (par exemple « Move », « Select ») et ne montre que celles de l'écran ouvert.
3. Allocation y liste notamment V, N, C et A ; Compliance, N, R, Q, S et l'édition des colonnes personnalisées.
4. Chaque touche listée fonctionne sur l'écran, et chaque raccourci de l'écran est listé.
5. Aucune bande de raccourcis n'est affichée en permanence.

### US-TAB-20 — Créer une colonne personnalisée
**Carte :** En tant que chef de projet, je veux ajouter à mon tender une colonne à moi, en texte libre ou en liste, afin de suivre une information propre au tender sans repartir dans Excel.
**Conversation :** L'intention : la souplesse d'un tableur sans perdre le modèle dessous (DEC-064). Deux types : « Free text », ou « List » — un ensemble fermé d'options, à choix unique ou multiple (« Allow several values per requirement », DEC-066). Une colonne appartient à son tender et à lui seul ; elle est commune à Allocation et Compliance ([US-TAB-22](#us-tab-22--retrouver-une-colonne-personnalisée-sur-lautre-écran)). Seuls les chefs de projet créent, modifient et suppriment.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), bouton « ＋ Column » et Custom Column Editor ; Compliance — `compliance.html` (route `#compliance`), mêmes composants.
**Règles :** DEC-064, DEC-066, DEC-097, CUST-T01 (partie « autre tender »), CUST-T02, PLAT-002 · **Périmètre :** Pilote 1 (à confirmer) ; Compliance : après pilote · **Variantes :** Toutes
**Critères d'acceptation :**
1. « ＋ Column » ouvre « New column » : un nom, un type (« Free text » ou « List ») et, pour une liste, ses options et « Allow several values per requirement ».
2. « Create column » refuse un nom vide (« Give the column a name ») ou déjà porté par une autre colonne, native ou personnalisée, sans tenir compte des majuscules (« A column called “…” already exists »).
3. Une liste sans option est refusée (« A list needs at least one option »), une option en double aussi.
4. La colonne créée s'ajoute en fin de table, visible sur l'écran où elle a été créée et vide sur toutes les exigences.
5. Elle n'apparaît sur aucun autre tender et n'alimente aucune statistique.
6. Un contributeur ne voit ni « ＋ Column » ni le ✎ des en-têtes, et le serveur refuse une création ou une modification qu'il tenterait par un autre chemin.

### US-TAB-21 — Remplir une colonne personnalisée
**Carte :** En tant que contributeur ou chef de projet, je veux saisir la valeur d'une colonne personnalisée dans la table ou dans le détail, afin de tenir l'information à jour là où je travaille.
**Conversation :** Une colonne personnalisée se remplit comme un champ natif : dans la cellule (champ texte, liste déroulante ou sélecteur à cases) ou dans le panneau de détail. Ce sont des données humaines : l'IA ne les remplit jamais, sans confiance ni doute, et elles ne mettent jamais une exigence « à revoir » ; toujours facultatives, elles ne bloquent jamais la validation (DEC-067, comme l'absence de personne, DEC-025). Le contributeur remplit sur les exigences de son système (DEC-100). Les lignes de système, d'équipe et d'information ont une cellule vide.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Custom Column Cell et Custom Fields Panel Section ; Compliance — `compliance.html` (route `#compliance`), mêmes composants.
**Règles :** DEC-067, DEC-068, DEC-097, DEC-100, CUST-T02, CUST-T03, CUST-T09, PLAT-002 · **Périmètre :** Pilote 1 (à confirmer) ; Compliance : après pilote · **Variantes :** Toutes
**Critères d'acceptation :**
1. Une valeur saisie dans la cellule ou dans le panneau s'enregistre et apparaît aussitôt aux deux endroits.
2. Le panneau rappelle : « Custom columns — entered by people. The AI never fills them, and they never put a requirement into review. »
3. Aucune valeur n'est proposée par l'IA ni ne porte de niveau de confiance, et modifier une valeur ne change jamais le statut de l'exigence.
4. Une exigence dont une colonne personnalisée est vide se valide normalement.
5. Sur une exigence qui n'est pas de son système, le contributeur voit la valeur en lecture seule, et le serveur refuse toute modification.
6. Une valeur survit à la navigation entre écrans et à la remise à zéro de l'exigence par une nouvelle version de son document.
Point ouvert : la survie des valeurs à une nouvelle version est un défaut « à confirmer » (DEC-068).

### US-TAB-22 — Retrouver une colonne personnalisée sur l'autre écran
**Carte :** En tant que chef de projet ou contributeur, je veux retrouver dans Compliance une colonne créée dans Allocation, et l'inverse, avec les mêmes valeurs, afin de ne jamais saisir deux fois la même information.
**Conversation :** DEC-097 remplace la portée « une phase » : une colonne est commune aux deux étapes, avec les mêmes valeurs. Elle est visible par défaut sur l'écran où elle a été créée, masquée par défaut sur l'autre, où « View » l'affiche ; ce choix est retenu par écran. CUST-T01 (« ni dans Compliance ») et CUST-T11 (« n'apparaît que dans Compliance ») sont caducs sur ce point.
**Maquette :** Compliance — `compliance.html` (route `#compliance`), Column Visibility Menu (Custom Column Tag) ; Allocation — `revue-documentaire.html` (route `#review`), Columns Panel.
**Règles :** DEC-097, CUST-T12 · **Périmètre :** Après pilote · **Variantes :** Toutes
**Critères d'acceptation :**
1. Une colonne créée dans Allocation existe dans Compliance, masquée, avec exactement les mêmes valeurs ; et inversement.
2. Sur l'autre écran, elle figure dans « View » sous « Table columns », marquée « custom », décochée.
3. La cocher l'affiche ; ce choix est retrouvé à la visite suivante de cet écran et ne change rien sur l'autre.
4. Une valeur saisie sur un écran est la même sur l'autre.
5. La supprimer depuis l'un des deux écrans la retire des deux ([US-TAB-25](#us-tab-25--supprimer-une-colonne-personnalisée)).
Point ouvert : le choix d'affichage vaut-il pour chaque personne ou pour tout le tender ? La maquette le garde sur la colonne, donc pour tous.

### US-TAB-23 — Filtrer et trier sur une colonne personnalisée
**Carte :** En tant que chef de projet ou contributeur, je veux filtrer et trier sur une colonne personnalisée comme sur une colonne native, afin d'isoler les exigences selon l'information qu'on y suit.
**Conversation :** Une colonne personnalisée vaut une colonne native partout : tri, entonnoir pour les listes, filtre avancé avec les opérateurs de son type (CUST-T07). Les listes à choix multiple ont leurs propres opérateurs (DEC-066). La valeur vide se cherche aussi.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Custom Column Header Cell et groupe « Custom columns » de l'Advanced Filter Builder ; Compliance — `compliance.html` (route `#compliance`), mêmes composants.
**Règles :** CUST-T07, DEC-066, UX-003 · **Périmètre :** Pilote 1 (à confirmer) ; Compliance : après pilote · **Variantes :** Toutes
**Critères d'acceptation :**
1. Le filtre avancé propose un groupe « Custom columns » ; une colonne texte y a « contains », « does not contain », « is », « is not », « starts with », « is empty », « is not empty ».
2. Une liste à choix unique y a « is », « is not », « is any of », « is none of », « is empty ».
3. Une liste à choix multiple y a « is any of » (au moins une des valeurs), « is none of », « is empty », « is not empty ».
4. L'en-tête d'une colonne de type liste porte un entonnoir avec ses options et « — empty — » ([US-TAB-06](#us-tab-06--filtrer-une-colonne-comme-dans-excel)).
5. Un clic sur son en-tête la trie comme toute colonne ([US-TAB-05](#us-tab-05--trier-par-un-en-tête-de-colonne)).
6. Une colonne supprimée disparaît aussitôt des filtres, des tris et des conditions du filtre avancé en cours, sans laisser de condition qui ne filtre plus rien.
Écart maquette : sur Compliance, une colonne de type liste n'a pas d'entonnoir d'en-tête ; seul le filtre avancé la filtre.

### US-TAB-24 — Modifier une colonne personnalisée
**Carte :** En tant que chef de projet, je veux renommer une colonne personnalisée et faire évoluer ses options, afin de l'adapter sans perdre les valeurs déjà saisies.
**Conversation :** Aucune valeur ne doit être perdue ni rendue orpheline en silence (DEC-065). Renommer est toujours permis ; changer le type est bloqué dès qu'une valeur existe (DEC-068, défaut à confirmer). Passer d'un choix unique à un choix multiple est sans perte ; l'inverse est bloqué tant qu'une exigence tient plusieurs valeurs. Chaque verrou s'explique dans l'éditeur au lieu de griser sans raison.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), ✎ du Custom Column Header Cell et Custom Column Editor (« Edit column ») ; Compliance — `compliance.html` (route `#compliance`), mêmes composants.
**Règles :** DEC-065, DEC-066, DEC-068, CUST-T05, CUST-T06, CUST-T02 · **Périmètre :** Pilote 1 (à confirmer) ; Compliance : après pilote · **Variantes :** Toutes
**Critères d'acceptation :**
1. Le ✎ d'un en-tête ouvre « Edit column » ; renommer est accepté même quand des valeurs existent.
2. Dès qu'une exigence a une valeur, l'autre type est inactif et l'éditeur dit pourquoi, avec le nombre d'exigences concernées.
3. Une option utilisée affiche « used by N » ; la retirer est refusé avec ce nombre (« … is used by N requirements — clear those values before removing it »).
4. Une option inutilisée se retire, et une nouvelle option s'ajoute à tout moment.
5. Cocher « Allow several values per requirement » garde chaque valeur existante, qui devient une liste d'un élément.
6. Le décocher est impossible tant qu'une exigence tient plusieurs valeurs ; l'éditeur dit combien.
Point ouvert : renommer une option existante n'est ni fait ni décidé ; le verrou du type est un défaut « à confirmer » (DEC-068).

### US-TAB-25 — Supprimer une colonne personnalisée
**Carte :** En tant que chef de projet, je veux supprimer une colonne personnalisée en sachant combien de valeurs je perds, afin de ne rien détruire sans le savoir.
**Conversation :** Supprimer une colonne supprime toutes ses valeurs, sans retour : « supprimer cette colonne » et « supprimer 340 valeurs » sont la même action, et c'est la seconde que l'utilisateur doit lire. La colonne disparaît des deux écrans (DEC-097).
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Custom Column Editor (confirmation de suppression) ; Compliance — `compliance.html` (route `#compliance`), même composant.
**Règles :** CUST-T04, CUST-T12, CUST-T02, DEC-097, PLAT-002 · **Périmètre :** Pilote 1 (à confirmer) ; Compliance : après pilote · **Variantes :** Toutes
**Critères d'acceptation :**
1. « Delete column… » ouvre une confirmation qui dit, avant d'agir, combien d'exigences ont une valeur (« N requirements hold a value in this column… This cannot be undone. »).
2. Le bouton nomme ce qui part (« Delete column and N values ») ; « Keep it » revient sans rien changer.
3. Sans aucune valeur, la confirmation le dit (« No requirement holds a value yet — only the column itself goes. »).
4. Confirmer retire la colonne et toutes ses valeurs d'Allocation et de Compliance, définitivement.
5. Seul un chef de projet peut supprimer ; le serveur refuse la demande d'un contributeur.

### US-TAB-26 — Garder les colonnes personnalisées hors de l'export client
**Carte :** En tant que chef de projet, je veux que mes colonnes personnalisées ne partent jamais au client par défaut, afin qu'une note interne ne se retrouve pas dans la matrice de conformité.
**Conversation :** Une colonne libre finit tôt ou tard par servir de note interne : un doute sur un fournisseur, une réserve commerciale. Défaut retenu : incluses dans les exports internes, jamais dans la matrice de conformité client (DEC-068, à confirmer). À l'export de Compliance, elles sont proposées décochées et marquées « internal », et les cocher avertit (DEC-081 ; fenêtre d'export dans [US-CMP-28](09-compliance.md#us-cmp-28--exporter-le-registre-de-conformité-avec-options)). L'export générique d'Allocation est décrit dans US-X.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Export Panel (« Export ▾ ») ; Compliance — `compliance.html` (route `#compliance`), Export Options Modal (Custom Column Tag « internal »).
**Règles :** DEC-068, DEC-081, CUST-T08, CUST-T11 (partie export) · **Périmètre :** Pilote 1 (à confirmer) ; Compliance : après pilote · **Variantes :** Toutes
**Critères d'acceptation :**
1. L'export interne d'Allocation inclut les colonnes personnalisées et le dit (« N custom columns included — internal exports only. Never sent in the client compliance matrix. »).
2. Dans les options d'export de Compliance, chaque colonne personnalisée est décochée par défaut et étiquetée « internal ».
3. Cocher une colonne personnalisée à l'export affiche un avertissement.
4. Une matrice de conformité client ne contient aucune colonne personnalisée que personne n'a cochée.
Point ouvert : le défaut « hors export client » est à confirmer (DEC-068) ; ce qui distingue un export client d'un export interne n'est pas spécifié (voir [US-CMP-28](09-compliance.md#us-cmp-28--exporter-le-registre-de-conformité-avec-options)).

## Couverture
- Règles couvertes : UX-001 → [US-TAB-01](#us-tab-01--lire-la-table-dans-lordre-du-document), [US-TAB-02](#us-tab-02--déplier-une-exigence-en-lignes-par-système-et-par-organisation), [US-TAB-04](#us-tab-04--rechercher-une-exigence-par-son-identifiant-ou-son-texte), [US-TAB-05](#us-tab-05--trier-par-un-en-tête-de-colonne), [US-TAB-06](#us-tab-06--filtrer-une-colonne-comme-dans-excel), [US-TAB-11](#us-tab-11--choisir-masquer-et-réordonner-les-colonnes), [US-TAB-12](#us-tab-12--redimensionner-les-colonnes), [US-TAB-13](#us-tab-13--sélectionner-plusieurs-lignes-et-agir-en-une-fois), [US-TAB-15](#us-tab-15--se-déplacer-et-sélectionner-au-clavier), [US-TAB-16](#us-tab-16--éditer-une-cellule-au-clavier) ; UX-002 → [US-TAB-03](#us-tab-03--filtrer-dun-clic-sur-un-compteur-de-statut), [US-TAB-06](#us-tab-06--filtrer-une-colonne-comme-dans-excel), [US-TAB-08](#us-tab-08--lire-en-clair-ce-qui-filtre-la-table-et-tout-effacer), [US-TAB-14](#us-tab-14--ne-montrer-que-les-lignes-sélectionnées) ; UX-003 → [US-TAB-07](#us-tab-07--construire-un-filtre-avancé), [US-TAB-08](#us-tab-08--lire-en-clair-ce-qui-filtre-la-table-et-tout-effacer), [US-TAB-23](#us-tab-23--filtrer-et-trier-sur-une-colonne-personnalisée) ; UX-004 → [US-TAB-09](#us-tab-09--enregistrer-un-filtre-et-le-réutiliser-sur-un-autre-tender) ; UX-005 → [US-TAB-04](#us-tab-04--rechercher-une-exigence-par-son-identifiant-ou-son-texte), [US-TAB-05](#us-tab-05--trier-par-un-en-tête-de-colonne), [US-TAB-06](#us-tab-06--filtrer-une-colonne-comme-dans-excel), [US-TAB-07](#us-tab-07--construire-un-filtre-avancé) ; UX-006 → [US-TAB-14](#us-tab-14--ne-montrer-que-les-lignes-sélectionnées) (partie décidée) ; CUST-T01 → [US-TAB-20](#us-tab-20--créer-une-colonne-personnalisée) (partie « autre tender ») ; CUST-T02 → [US-TAB-20](#us-tab-20--créer-une-colonne-personnalisée), [US-TAB-21](#us-tab-21--remplir-une-colonne-personnalisée), [US-TAB-24](#us-tab-24--modifier-une-colonne-personnalisée), [US-TAB-25](#us-tab-25--supprimer-une-colonne-personnalisée) ; CUST-T03 → [US-TAB-21](#us-tab-21--remplir-une-colonne-personnalisée) ; CUST-T04 → [US-TAB-25](#us-tab-25--supprimer-une-colonne-personnalisée) ; CUST-T05 → [US-TAB-24](#us-tab-24--modifier-une-colonne-personnalisée) ; CUST-T06 → [US-TAB-24](#us-tab-24--modifier-une-colonne-personnalisée) ; CUST-T07 → [US-TAB-23](#us-tab-23--filtrer-et-trier-sur-une-colonne-personnalisée) ; CUST-T08 → [US-TAB-26](#us-tab-26--garder-les-colonnes-personnalisées-hors-de-lexport-client) ; CUST-T09 → [US-TAB-21](#us-tab-21--remplir-une-colonne-personnalisée) ; CUST-T10 → [US-TAB-15](#us-tab-15--se-déplacer-et-sélectionner-au-clavier), [US-TAB-16](#us-tab-16--éditer-une-cellule-au-clavier) ; CUST-T11 → [US-TAB-26](#us-tab-26--garder-les-colonnes-personnalisées-hors-de-lexport-client) (partie export) ; CUST-T12 → [US-TAB-22](#us-tab-22--retrouver-une-colonne-personnalisée-sur-lautre-écran), [US-TAB-25](#us-tab-25--supprimer-une-colonne-personnalisée) ; JRN-002 (parties table) → [US-TAB-01](#us-tab-01--lire-la-table-dans-lordre-du-document), [US-TAB-03](#us-tab-03--filtrer-dun-clic-sur-un-compteur-de-statut), [US-TAB-06](#us-tab-06--filtrer-une-colonne-comme-dans-excel), [US-TAB-07](#us-tab-07--construire-un-filtre-avancé), [US-TAB-13](#us-tab-13--sélectionner-plusieurs-lignes-et-agir-en-une-fois), [US-TAB-17](#us-tab-17--aller-à-la-prochaine-exigence-qui-mattend-et-valider-au-clavier).
- Non couvertes, avec la raison : CUST-T01, partie « ni dans Compliance » — caduque (remplacée par DEC-097) ; CUST-T11, partie « n'apparaît que dans Compliance » — caduque (remplacée par DEC-097) ; UX-006, composition avec le filtre avancé et la sélection de toutes les pages — point ouvert (OPEN-13) ; JRN-002 hors table (inspecter, corriger, valider une exigence) — couverte par l'épopée US-ALM.
