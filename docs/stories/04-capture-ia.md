<!-- Généré depuis le backlog du 10 octobre 2026 ; voir README.md pour les conventions. -->
# Capture, traduction et caractérisation IA (US-CAP)

Ces stories décrivent ce que fait le produit entre le dépôt des documents et l'arrivée des exigences dans Allocation : convertir et découper les documents, traduire, caractériser, enchaîner les étapes jusqu'à l'allocation, puis relancer les modèles quand une nouvelle version arrive (JRN-001, JRN-005). Le chef de projet lance, règle et corrige ; le contributeur lit le résultat.
Termes : **capture** = conversion du fichier source puis découpe en **blocs** ; **nature** d'un bloc = Heading (titre), Information ou Requirement (exigence) ; **classe** = technique / non technique ; **caractérisation** = nature et classe proposées par l'IA avec un **niveau de confiance** Low / Medium / High ; **relance** = faire tourner à nouveau un modèle.
La conception et l'entretien des modèles IA ne sont pas couverts ici (DEC-020) : seul le comportement du produit autour de leurs résultats l'est.

### US-CAP-01 — Enchaîner automatiquement les étapes IA activées
**Carte :** En tant que chef de projet, je veux que les étapes IA activées pour le tender s'enchaînent seules dès la création, afin de retrouver mes exigences prêtes à revoir sans valider chaque étape.
**Conversation :** Les étapes activées par le mode du tender tournent l'une après l'autre — capture, traduction si la langue source n'est pas l'anglais, caractérisation, allocation — sans pause de validation entre elles (DEC-018, LIFE-003). L'étape d'allocation dépend du type : aiguillage vers les systèmes puis modèle de chaque système sur un Turnkey, dérivation ABS → PBS → OBS sur un tender à un système, jamais de passe 1 Turnkey sur SIG (voir US-ALM). La seule borne humaine reste la validation de l'allocation, exigence par exigence. Un casting incomplet n'arrête rien.
**Maquette :** Nouveau tender — `creation-projet.html` (route `#new`), Processing Overlay ; Accueil — `accueil.html` (route `#home`), Tender Line (station Capture) ; Documents & versions — `documents.html` (route `#documents`), barre d'avancement de la Document Table.
**Règles :** DEC-018, LIFE-003, AI-009, LANG-002, AI-005, AI-001, LIFE-T02, ACC-003  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes (étape d'allocation selon le type)
**Critères d'acceptation :**
1. Après la création du tender ou l'ajout d'un document, chaque étape activée démarre dès que la précédente a fini, sans action ni validation de personne.
2. Une étape désactivée par le mode est sautée ; aucune proposition IA n'apparaît pour elle et son travail reste à faire à la main.
3. Pendant le traitement, l'étape en cours se lit sur la carte du tender et sur la ligne de chaque document (capture, traduction, caractérisation, allocation).
4. À la fin, les exigences portent des propositions mais aucune n'est « Allocated » sans validation humaine (voir [US-ALM-26](05-allocation.md#us-alm-26--valider-une-exigence-en-un-seul-geste)).
5. Un tender SIG ne passe jamais par l'aiguillage Turnkey ; un Turnkey le fait avant d'appliquer le modèle de chaque système.
6. Chaque résultat est rattaché au bon tender, document, version et bloc ; un tender dont aucun système n'est casté est traité de la même façon (LIFE-T02).
Écart maquette : le traitement est une temporisation simulée, et sa dernière étape s'intitule encore « Allocating to contributors… » alors que l'IA dérive des organisations, jamais des personnes (DEC-054).

### US-CAP-02 — Régler la conversion du document source
**Carte :** En tant que chef de projet, je veux régler ce qui sort du fichier source avant la découpe — pages, tableaux, phrases, équations —, afin que la capture produise les bons blocs.
**Conversation :** Les réglages de conversion décident de ce qui sort du fichier, avant la découpe en blocs ; ils ouvrent la section « Capture & segmentation » des paramètres. Une page hors de la plage capturée n'existe pas dans le tender : ce n'est pas un filtre d'affichage. Le format de tableau commande la granularité : seul un tableau converti en données (dataframe) a des lignes à transformer en exigences. Découper les paragraphes en phrases augmente le nombre d'exigences ; le défaut est « As source file ».
**Maquette :** Paramètres — `dashboard-et-config.html` (route `#config`), section « Capture & segmentation », Config Field Row, Segmented Control.
**Règles :** CAPT-T01, CAPT-T02, CAPT-T03  ·  **Périmètre :** Pilote 1 (à confirmer)  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. « Conversion range » propose « All pages » et « Specific pages » ; choisir « Specific pages » ouvre un champ pour dire lesquelles (par exemple « 1-12, 40, 55-58 »), et l'option n'existe pas sans ce champ (CAPT-T01).
2. L'écran dit qu'une page hors plage ne produit aucune exigence et ne la présente jamais comme un filtre d'Allocation ; après capture, aucun bloc ne vient d'une page hors plage (CAPT-T02).
3. « Default table conversion format » (« Image » / « Dataframe ») est suivi immédiatement de « Default table granularity » (« One requirement per row » / « Whole table »), qui dit ne valoir que pour un tableau converti en dataframe (CAPT-T03).
4. « Sentences in paragraphs » propose « As source file », par défaut, et « Split » ; « Format of equations » propose « As images » et « As formulas ».
5. Un tableau converti en image est capturé comme une image (voir [US-CAP-04](#us-cap-04--capturer-les-images-sans-en-lire-le-contenu)) ; converti en dataframe, ses lignes deviennent des blocs selon la granularité choisie.
Écart maquette : ces réglages sont affichés sans aucun effet (avertissement « demo only »).
Point ouvert : la liste des réglages est peut-être incomplète. Leur moment n'est pas décidé : figés à la création comme le produit, ou modifiables après capture avec un avertissement chiffré et une nouvelle capture — or la capture démarre dès la création, alors que ces réglages ne sont proposés que dans les paramètres. La granularité doit-elle être désactivée quand le format est « Image » ? Le libellé « Split » est à confirmer, et l'essai SPEC-document-view découpe par phrase par défaut. Le droit de modifier les paramètres n'est pas fixé (JRN-007, OPEN-05).

### US-CAP-03 — Découper chaque document en blocs Heading, Information ou Requirement
**Carte :** En tant que chef de projet, je veux que la capture découpe chaque document en blocs typés, chacun relié à son passage source, afin de travailler exigence par exigence sans perdre le fil du document.
**Conversation :** La capture découpe chaque document, dans l'ordre du tender, en blocs. La nature d'un bloc est Heading, Information ou Requirement, rien d'autre (DEC-074) ; seules les exigences sont caractérisées et allouées, titres et blocs d'information n'ont pas de statut (DEC-073, voir US-ALM). Chaque bloc a un identifiant stable, distinct du numéro de ligne affiché, et reste relié à son document, à sa version et à son passage source. Corriger la nature d'un bloc, droit du chef de projet (voir [US-ALM-04](05-allocation.md#us-alm-04--corriger-la-nature-et-la-classe-dune-exigence), [US-ALM-06](05-allocation.md#us-alm-06--réserver-la-nature-et-la-classe-au-chef-de-projet)), ne change pas son identité.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Document Reading View (Document Block, Type Chip), Requirement Table (Review Grid), Nature and Class Fields.
**Règles :** DOM-003, DOM-012, LIFE-005, LIFE-T04, DEC-074, DEC-073, AI-001, AI-002  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Chaque bloc capturé a pour nature Heading, Information ou Requirement, et aucune autre valeur n'est possible.
2. Les blocs paraissent dans l'ordre des documents du tender, puis dans l'ordre du texte ; un titre garde son niveau (2.1, 2.1.1…).
3. Le détail d'une exigence commence par son paragraphe source (« § numéro titre »), qui ouvre la vue Document à cet endroit.
4. L'identifiant d'un bloc ne change jamais : ni au tri, ni au filtrage, ni quand sa nature change, ni à l'arrivée d'une version qui ne le modifie pas (LIFE-T04).
5. Changer la nature d'un bloc conserve son texte original et son lien au passage source (LIFE-005).
6. Chaque bloc indique le document et la version dont il vient ; cette information est consultable et sort à l'export.
Point ouvert : la correspondance des identifiants d'une version à l'autre en cas de fusion ou de scission n'est pas spécifiée (OPEN-07, DOM-012) ; la correction de la découpe à la main n'est pas décidée (voir [US-CAP-05](#us-cap-05--signaler-une-découpe-incertaine)).

### US-CAP-04 — Capturer les images sans en lire le contenu
**Carte :** En tant que chef de projet, je veux que les figures du document soient capturées et affichées à leur place, sans que l'IA prétende les lire, afin de rattacher moi-même les exigences qu'elles portent.
**Conversation :** Une image est capturée et affichée, mais son contenu n'est ni lu ni caractérisé automatiquement ; le reste du document est traité normalement (DEC-018). La capture crée une ligne d'exigence rattachée à l'image ; si la figure porte plusieurs exigences, on duplique cette ligne. Seules ces lignes dupliquées se suppriment (DEC-094). Une figure détectée à tort se reclasse en Information.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Document Block (variante image), Requirement Row (ligne issue d'une image, « Duplicate », « Delete »), Detail / Assignment Panel (« Captured from … », « ← Image »).
**Règles :** DEC-018, AI-002, LIFE-T08, DEC-094, ALLOC-023  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Une image du document paraît dans la vue Document à sa place, avec sa légende.
2. Aucune nature, classe, système ni dérivation n'est proposé à partir du contenu de l'image ; le texte autour d'elle est traité comme le reste (LIFE-T08).
3. La capture crée une ligne d'exigence rattachée à l'image : la table montre un lien vers l'image au lieu d'un extrait, le détail dit « Captured from <image> » et « ← Image » ramène à la figure.
4. « Duplicate » crée une autre ligne rattachée à la même image, avec un nouvel identifiant, marquée « duplicate ».
5. Seule une ligne dupliquée se supprime, après confirmation ; la première ligne et l'image elle-même ne se suppriment jamais.
6. Une image détectée à tort se reclasse en Information par le chef de projet (voir [US-ALM-04](05-allocation.md#us-alm-04--corriger-la-nature-et-la-classe-dune-exigence)) ; son contenu n'est pas lu pour autant.
Écart maquette : les lignes issues d'images de la démonstration portent un texte et des valeurs pré-remplis.
Point ouvert : le texte de travail d'une ligne issue d'une image (vide, légende, saisie) et le droit d'un contributeur à dupliquer une ligne ne sont pas spécifiés ; un PDF fait uniquement d'images est une limite d'ingestion à préciser avec l'équipe technique (OPEN-10).

### US-CAP-05 — Signaler une découpe incertaine
**Carte :** En tant que chef de projet, je veux voir les blocs dont l'IA n'est pas sûre des limites, afin d'en vérifier le contenu avant de valider.
**Conversation :** La capture marque d'un drapeau les blocs dont la découpe est douteuse ; ce drapeau est distinct du statut et ne bloque rien. Le détail de l'exigence l'annonce avant la validation. Corriger la découpe à la main (scinder, fusionner) n'est pas décidé pour le produit : seuls les effets d'une fusion ou d'une scission sont écrits (LIFE-009, voir [US-CAP-13](#us-cap-13--repartir-de-zéro-sur-une-exigence-issue-dune-fusion-ou-dune-scission)).
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Document Block (« Check boundaries »), AI Suggestion Card (variante uncertain-segmentation), Block Badge du navigateur.
**Règles :** AI-001, ALLOC-006, DOM-007  ·  **Périmètre :** Pilote 1 (à confirmer)  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Un bloc à découpe incertaine porte « Check boundaries » dans la vue Document et une marque « Uncertain segmentation » dans le navigateur.
2. Son détail commence par « ⚠ Uncertain segmentation » et dit que l'IA n'est pas sûre des limites du bloc.
3. Le drapeau ne change pas le statut de l'exigence et n'empêche pas de la valider.
4. Le nombre de blocs à découpe incertaine du tender est disponible pour le tableau de bord (voir US-DASH).
Écart maquette : le réglage « Uncertainty threshold » des paramètres n'agit sur rien, et le mode « Edit segmentation » est masqué.
Point ouvert : la définition du drapeau n'est pas tranchée — seuil de confiance réglable (80 % par défaut dans la maquette) ou règles textuelles de l'essai SPEC-document-view (deux obligations dans des phrases différentes, exigence visiblement coupée) ; ce qui retire le drapeau n'est pas spécifié ; la correction manuelle de la découpe n'est pas décidée.

### US-CAP-06 — Écarter un bloc capturé par erreur sans le supprimer
**Carte :** En tant que chef de projet, je veux sortir du périmètre un bloc capturé à tort en le reclassant en Information, afin de garder le document intact tout en n'allouant que de vraies exigences.
**Conversation :** Un bloc capturé ne se supprime pas à la main : s'il n'est pas une exigence, on le reclasse en Information, ce qui le sort du périmètre — statut, allocation, compteurs (DEC-094). Le document reste donc complet et chaque bloc garde son identifiant. Seules les lignes dupliquées à la main depuis une image se suppriment (voir [US-CAP-04](#us-cap-04--capturer-les-images-sans-en-lire-le-contenu)). Le geste de reclassement, sa confirmation quand une réponse existe et le retour éventuel en Requirement sont décrits dans [US-ALM-04](05-allocation.md#us-alm-04--corriger-la-nature-et-la-classe-dune-exigence) et [US-ALM-06](05-allocation.md#us-alm-06--réserver-la-nature-et-la-classe-au-chef-de-projet) ; ici, la règle « jamais de suppression » et ce qu'elle implique.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Nature Picker, Nature and Class Fields, barre d'actions groupées (passage en Information) ; aucun bouton de suppression.
**Règles :** DEC-094, ALLOC-023, DEC-073, DEC-086, LIFE-005  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Aucune action ne supprime un bloc capturé — ni dans la table, ni dans le détail, ni dans la vue Document, ni par action groupée — et le serveur refuse une suppression demandée autrement.
2. Une exigence reclassée en Information perd son statut et sort des compteurs d'exigences : barre de statut d'Allocation, tableau de bord, statistiques et poids du document dans « Documents & versions ».
3. Le bloc reclassé reste visible à sa place dans la vue Document, avec son identifiant et son texte, et peut être reclassé plus tard.
4. Seul le chef de projet peut reclasser ; un contributeur n'a aucun moyen de sortir un bloc du périmètre (DEC-086, [US-ALM-06](05-allocation.md#us-alm-06--réserver-la-nature-et-la-classe-au-chef-de-projet)).
5. La seule suppression possible est celle d'une ligne dupliquée à la main depuis une image ([US-CAP-04](#us-cap-04--capturer-les-images-sans-en-lire-le-contenu)) ; la première ligne d'une image et tout autre bloc restent.
Point ouvert : la suppression et la restauration au niveau documentaire restent non confirmées (LIFE-006) ; elles sont distinctes de ce cas.

### US-CAP-07 — Traduire automatiquement vers l'anglais de travail
**Carte :** En tant que chef de projet d'un tender rédigé dans une autre langue, je veux que les blocs soient traduits automatiquement en anglais sans étape de relecture, afin que la caractérisation et l'allocation démarrent tout de suite.
**Conversation :** La langue de travail est l'anglais pour tous les tenders (LANG-001). Si la langue source n'est pas l'anglais, la traduction automatique tourne après la capture et avant la caractérisation, sans pause ni validation : elle est réputée fiable et se corrige ensuite (DEC-019, LANG-002, voir [US-CAP-08](#us-cap-08--corriger-une-traduction-ce-qui-remet-lexigence-en-revue)). L'original est conservé tel quel et reste lisible ; les modèles, les tables et la recherche travaillent sur le texte anglais. Un tender en anglais n'a pas d'étape de traduction.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Detail / Assignment Panel, onglet « Translation » et sélecteur « Read in » ; Paramètres — `dashboard-et-config.html` (route `#config`), section Language.
**Règles :** LANG-001, LANG-002, LANG-T01, LANG-T02, DEC-019, DEC-096, AI-003  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Sur un tender de langue source non anglaise, chaque titre, bloc d'information et exigence reçoit un texte anglais de travail, sans qu'aucune validation humaine ne soit demandée avant la caractérisation (LANG-T01).
2. Le texte original de chaque bloc est conservé à l'identique, et aucune action ne peut le modifier (LANG-T02).
3. L'onglet « Translation » montre « Original — <langue> » et « English — working text » ; le sélecteur « Read in » permet de lire l'un ou l'autre.
4. Sur un tender en anglais, aucune étape de traduction ne tourne et l'onglet « Translation » n'apparaît pas.
5. Les paramètres affichent « Working language » : « English », avec « Not editable — translation always goes into English. », sans contrôle pour la changer.
Écart maquette : la lecture dans une langue tierce (German, Spanish) est simulée.
Point ouvert : la langue affichée par défaut dans les panneaux n'est pas décidée (Allocation met l'original en tête, Compliance l'anglais) ; la lecture dans une langue tierce n'est pas redemandée par les règles actuelles ; la langue de l'export client relève d'US-CMP (LANG-003).

### US-CAP-08 — Corriger une traduction, ce qui remet l'exigence en revue
**Carte :** En tant que chef de projet, je veux corriger le texte anglais d'un bloc mal traduit, afin que tout le travail repose sur une traduction juste.
**Conversation :** La traduction se corrige à tout moment, même après caractérisation et allocation (LANG-004). Toute correction, même d'un mot, remet l'exigence en revue, sans seuil de gravité ni approbation préalable (DEC-026, LIFE-008). La correction est tracée et l'original ne bouge pas. Les autres modifications (personne d'une organisation, colonne personnalisée, réallocation…) passent par leur propre fonction et ne remettent pas l'exigence en revue (LIFE-010).
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Detail / Assignment Panel, onglet « Translation » (« Correct », « Save correction », « Correction history »).
**Règles :** LIFE-008, LANG-004, LANG-T03, DEC-026, LIFE-010, PLAT-003  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes (tenders de langue source non anglaise)
**Critères d'acceptation :**
1. « Correct » ouvre le texte anglais en édition ; « Save correction » enregistre, « Cancel » abandonne ; un texte vide est refusé avec « The English text can't be empty ».
2. Enregistrer un texte identique ne change rien : ni statut, ni trace (LANG-T03).
3. Enregistrer un texte différent, même d'un seul caractère, fait repasser l'exigence « To review », avec le motif en tête du détail ; un titre ou un bloc d'information corrigé ne prend aucun statut.
4. La correction s'inscrit dans « Correction history » et dans le journal du bloc — qui, quand, avant, après — et l'onglet porte une marque de correction.
5. Le verdict de conformité en place n'est jamais présenté comme revalidé après la correction sans action humaine (LANG-T03).
6. Changer la personne d'une organisation, une colonne personnalisée ou demander une réallocation ne remet pas l'exigence en revue (LIFE-010).
Écart maquette : enregistrer une correction ne change pas le statut de l'exigence.
Point ouvert : l'effet d'une correction sur une exigence déjà répondue (simple « To review », ou verdicts rouverts comme pour une version) n'est pas décidé ; le droit d'un contributeur à corriger la traduction d'une exigence de son système n'est pas écrit (DEC-100 lui interdit seulement toute modification hors de son système) ; la correction du texte de travail d'un tender en anglais n'est proposée nulle part, alors que LIFE-008 vise « toute correction du texte ou de la traduction ».

### US-CAP-09 — Caractériser chaque bloc avec un niveau de confiance Low, Medium ou High
**Carte :** En tant que chef de projet, je veux que l'IA propose la nature de chaque bloc et la classe de chaque exigence avec un niveau de confiance, afin de partir d'une caractérisation déjà faite et de savoir où regarder d'abord.
**Conversation :** Quand le mode l'active, l'étape de caractérisation propose la nature de chaque bloc et la classe (technique / non technique) de chaque exigence, selon la configuration du type de tender, sans transposer les règles Turnkey à SIG (AI-004). Chaque proposition porte un niveau — Low, Medium ou High —, pas un pourcentage (DEC-120) ; les modèles d'allocation gardent leurs pourcentages. Cette story couvre la production des propositions et de leurs niveaux ; leur affichage, le motif « To review » et la confirmation par la validation sont dans [US-ALM-05](05-allocation.md#us-alm-05--voir-le-niveau-de-confiance-de-lia-sur-la-nature-et-la-classe), [US-ALM-02](05-allocation.md#us-alm-02--savoir-pourquoi-une-exigence-est-à-revoir) et [US-ALM-26](05-allocation.md#us-alm-26--valider-une-exigence-en-un-seul-geste).
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Nature and Class Fields avec Confidence Level Badge ; Nature Picker (variante AI-typed) dans la vue Document ; Nouveau tender — `creation-projet.html` (route `#new`), étape 3 (description de Characterisation).
**Règles :** DEC-120, AI-014, AI-004, AI-001, DEC-074, ALLOC-006, ALLOC-007, DOM-007, DOM-013  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Après l'étape de caractérisation, chaque bloc a une nature proposée (Heading, Information ou Requirement) et chaque exigence une classe proposée, chacune avec un niveau Low, Medium ou High.
2. Aucune nature ni classe n'est proposée avec un pourcentage ; une capture qui fournit des nombres est convertie avec les seuils fixés : moins de 75 = Low, moins de 85 = Medium, sinon High.
3. Une proposition Low, sur la nature ou la classe d'une exigence, la fait passer « To review » ; Medium et High ne le font pas.
4. La proposition de l'IA, son niveau et la valeur retenue par une personne sont conservés séparément : une correction ne réécrit pas la proposition d'origine (DOM-013).
5. Le type du tender détermine les règles de caractérisation appliquées ; aucune règle propre au Turnkey n'est appliquée à un tender SIG (AI-004).
6. Si le mode désactive la caractérisation, aucune proposition ni aucun niveau n'apparaît : les exigences arrivent sans classe (« Off — every requirement starts unclassified. »).
Écart maquette : les niveaux de la démonstration sont générés et ne mesurent rien.
Point ouvert : la calibration des niveaux relève du chantier IA (DEC-020) ; la nature des blocs quand la caractérisation est désactivée (qui décide alors qu'un bloc est un titre, une information ou une exigence ?) n'est pas décrite.

### US-CAP-10 — Dire qu'aucun modèle ne s'applique, sans en emprunter un en silence
**Carte :** En tant que chef de projet d'un tender sans modèle fourni, RSC par exemple, je veux que l'outil dise clairement quand aucun modèle IA ne s'applique, afin de savoir que le travail se fera à la main plutôt que de recevoir des propositions fausses.
**Conversation :** Le type et le produit choisissent les modèles (DEC-007). Quand aucun modèle n'est fourni pour une étape de ce type de tender, l'étape le dit et le travail se fait à la main ; jamais le modèle d'un autre type n'est utilisé en silence (AI-010, TYPE-T05). Les autres étapes et les autres exigences avancent normalement. La saisie à la main d'un système sans modèle (y compris au sein d'un Turnkey) relève d'[US-ALM-20](05-allocation.md#us-alm-20--allouer-à-la-main-un-système-sans-modèle), l'emprunt explicite d'un modèle à la relance d'[US-ALM-22](05-allocation.md#us-alm-22--emprunter-le-modèle-dun-autre-système).
**Maquette :** Nouveau tender — `creation-projet.html` (route `#new`), note de ligne produit « No model supplied yet — allocated by hand. » ; état pendant le traitement non maquetté.
**Règles :** AI-010, TYPE-T05, DEC-007, ALLOC-005, ALLOC-009  ·  **Périmètre :** Pilote 1  ·  **Variantes :** RSC et toute ligne sans modèle fourni ; Turnkey pour ses systèmes sans modèle (voir [US-ALM-20](05-allocation.md#us-alm-20--allouer-à-la-main-un-système-sans-modèle))
**Critères d'acceptation :**
1. À la création, une ligne sans modèle fourni l'annonce sous le choix de ligne (« No model supplied yet — allocated by hand. »).
2. Pendant et après le traitement, l'étape sans modèle est montrée comme telle sur le tender, jamais comme une étape terminée ayant produit des propositions.
3. Un tender RSC ne reçoit aucune proposition d'un modèle SIG ou Turnkey ; ses exigences arrivent sans dérivation, « Incomplete », à allouer à la main ([US-ALM-20](05-allocation.md#us-alm-20--allouer-à-la-main-un-système-sans-modèle)).
4. Une étape qui dispose d'un modèle pour ce type tourne normalement ; seule l'étape sans modèle reste manuelle.
5. Les exigences en allocation manuelle n'empêchent pas les autres d'avancer (ALLOC-009).
Écart maquette : aucun état « sans modèle » n'est montré pendant le traitement.
Point ouvert : les particularités de configuration de RSC et de Mainline ne sont pas fournies (OPEN-15), ni les produits de RSC (DEC-047).

### US-CAP-11 — Reprendre un traitement interrompu sans doublon
**Carte :** En tant que chef de projet, je veux voir quand le traitement d'un document a échoué et pouvoir le reprendre, afin de ne perdre ni le document ni le travail déjà fait.
**Conversation :** Un traitement peut échouer (service IA indisponible, fichier illisible…). Le produit distingue trois états — en cours, en échec, résultat disponible — et permet de reprendre après incident sans créer de blocs en double (AI-012, proposition à valider). Une reprise n'efface jamais en silence une décision humaine déjà enregistrée (DOM-013). Le reste du tender reste utilisable pendant ce temps.
**Maquette :** non maquetté (« Documents & versions » — `documents.html`, route `#documents` — ne connaît que « Ready », « Processing » et « Not processed »).
**Règles :** AI-012, AI-001, DOM-013, ALLOC-009, PLAT-001  ·  **Périmètre :** Pilote 1 (à confirmer)  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Chaque document affiche un état distinct — en cours (avec l'étape), en échec, traité — et un échec n'est jamais présenté comme un résultat disponible.
2. En échec, la ligne du document dit à quelle étape le traitement s'est arrêté et propose de le reprendre.
3. La reprise ne duplique aucun bloc déjà capturé : chaque bloc garde un seul identifiant.
4. Une nature, une classe, une allocation ou une correction de traduction faite par une personne avant l'incident est intacte après la reprise.
5. Pendant l'échec d'un document, les exigences des autres documents restent consultables et traitables.
Point ouvert : AI-012 est une proposition à valider ; qui reprend le traitement, si la reprise est automatique et ce que l'on garde d'un résultat partiel ne sont pas décidés (DOM-013 renvoie à OPEN-07 et OPEN-09).

### US-CAP-12 — Relancer automatiquement les modèles sur les seules exigences modifiées par une nouvelle version
**Carte :** En tant que chef de projet, je veux qu'à l'arrivée d'une nouvelle version les modèles nécessaires se relancent seuls sur les exigences modifiées, et seulement elles, afin d'avoir des propositions à jour sans retraiter le reste du tender.
**Conversation :** Après la comparaison avec la nouvelle version d'un document, le produit relance automatiquement les modèles nécessaires, selon le changement et le type de tender, sur les exigences modifiées et elles seules (DEC-027, LIFE-011). Les nouvelles propositions restent à revoir et valider ; la relance ne rétablit ni les anciennes validations ni les verdicts (retour « To review » : voir US-CHG ; réouverture : voir US-CMP). L'historique des anciennes décisions est conservé pour l'audit, sans valeur courante. Le choix technique des modèles relève du chantier IA.
**Maquette :** non maquetté.
**Règles :** DEC-027, LIFE-011, LIFE-T09, LIFE-T10 (retraitement SIG), AI-006, AI-011, AI-004, AI-005, JRN-005  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes (SIG : jamais de passe 1 Turnkey)
**Critères d'acceptation :**
1. Une nouvelle version qui modifie 3 exigences sur 100 relance les modèles pour ces 3 exigences et pour aucune des 97 autres (LIFE-T09).
2. Les exigences inchangées gardent leurs propositions, leurs valeurs validées, leur statut et leurs réponses.
3. Les exigences relancées reçoivent des propositions issues du texte de la nouvelle version, à revoir et valider ; aucune ancienne validation ni aucun ancien verdict n'est réappliqué automatiquement.
4. Sur un tender SIG, la relance ne lance jamais l'aiguillage Turnkey ; sur un Turnkey, elle applique les modèles propres à ce type.
5. Les anciennes valeurs et décisions restent lisibles dans le journal de l'exigence, marquées comme antérieures à la version.
6. Une image, même modifiée, n'est toujours ni lue ni caractérisée (LIFE-T08).
Écart maquette : une version téléversée dans Documents n'atteint pas Allocation et aucune relance n'est simulée.
Point ouvert : ce que la relance fait de la personne déjà affectée à une organisation n'est pas écrit ; la détection d'une exigence « modifiée » dépend d'OPEN-07.

### US-CAP-13 — Repartir de zéro sur une exigence issue d'une fusion ou d'une scission
**Carte :** En tant que chef de projet, je veux que les exigences nées d'une fusion ou d'une scission dans une nouvelle version repartent sans aucune décision héritée, afin qu'aucun ancien verdict ne s'applique à un texte qui n'existait pas.
**Conversation :** Quand une nouvelle version fusionne deux exigences ou en scinde une, les exigences qui en résultent sont ajoutées au document en vigueur, leurs décisions sont remises à zéro et les modèles peuvent se relancer automatiquement pour elles (DEC-017, LIFE-009). Aucune ancienne décision ne se transfère. Les exigences d'origine quittent la vue courante et se lisent dans la comparaison (voir US-DOCV).
**Maquette :** non maquetté.
**Règles :** DEC-017, LIFE-009, LIFE-T07, AI-006, AI-011, DOM-012  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Chaque exigence issue d'une fusion ou d'une scission paraît dans le document en vigueur comme une nouvelle exigence.
2. Elle n'hérite d'aucune nature ou classe validée, d'aucune allocation, d'aucune personne ni d'aucun verdict de ses exigences d'origine (LIFE-T07).
3. Les modèles se relancent automatiquement pour elle ; ses propositions sont à revoir et valider comme toute proposition.
4. Les exigences d'origine sortent de la vue courante et restent lisibles, avec leur historique, dans la comparaison de versions.
5. Les exigences voisines, non touchées par la fusion ou la scission, gardent tout leur travail.
Écart maquette : le mode « Edit segmentation » (scinder, fusionner) est masqué et ne fait que remettre l'exigence en revue.
Point ouvert : la manière de reconnaître une fusion ou une scission et de relier les identifiants d'une version à l'autre n'est pas spécifiée (OPEN-07, DOM-012) ; une fusion ou une scission faite à la main par un utilisateur n'est pas décidée.

## Couverture
- Règles couvertes : LIFE-003 → [US-CAP-01](#us-cap-01--enchaîner-automatiquement-les-étapes-ia-activées) ; LIFE-005 → [US-CAP-03](#us-cap-03--découper-chaque-document-en-blocs-heading-information-ou-requirement), [US-CAP-06](#us-cap-06--écarter-un-bloc-capturé-par-erreur-sans-le-supprimer) ; LIFE-008 → [US-CAP-08](#us-cap-08--corriger-une-traduction-ce-qui-remet-lexigence-en-revue) ; LIFE-009 → [US-CAP-13](#us-cap-13--repartir-de-zéro-sur-une-exigence-issue-dune-fusion-ou-dune-scission) ; LIFE-010 → [US-CAP-08](#us-cap-08--corriger-une-traduction-ce-qui-remet-lexigence-en-revue) ; LIFE-011 → [US-CAP-12](#us-cap-12--relancer-automatiquement-les-modèles-sur-les-seules-exigences-modifiées-par-une-nouvelle-version) ; LIFE-T02 → [US-CAP-01](#us-cap-01--enchaîner-automatiquement-les-étapes-ia-activées) ; LIFE-T04 → [US-CAP-03](#us-cap-03--découper-chaque-document-en-blocs-heading-information-ou-requirement) ; LIFE-T07 → [US-CAP-13](#us-cap-13--repartir-de-zéro-sur-une-exigence-issue-dune-fusion-ou-dune-scission) ; LIFE-T08 → [US-CAP-04](#us-cap-04--capturer-les-images-sans-en-lire-le-contenu), [US-CAP-12](#us-cap-12--relancer-automatiquement-les-modèles-sur-les-seules-exigences-modifiées-par-une-nouvelle-version) ; LIFE-T09 → [US-CAP-12](#us-cap-12--relancer-automatiquement-les-modèles-sur-les-seules-exigences-modifiées-par-une-nouvelle-version) ; LANG-001 → [US-CAP-07](#us-cap-07--traduire-automatiquement-vers-langlais-de-travail) ; LANG-002 → [US-CAP-01](#us-cap-01--enchaîner-automatiquement-les-étapes-ia-activées), [US-CAP-07](#us-cap-07--traduire-automatiquement-vers-langlais-de-travail) ; LANG-004 → [US-CAP-08](#us-cap-08--corriger-une-traduction-ce-qui-remet-lexigence-en-revue) ; LANG-T01 → [US-CAP-07](#us-cap-07--traduire-automatiquement-vers-langlais-de-travail) ; LANG-T02 → [US-CAP-07](#us-cap-07--traduire-automatiquement-vers-langlais-de-travail) ; LANG-T03 → [US-CAP-08](#us-cap-08--corriger-une-traduction-ce-qui-remet-lexigence-en-revue) ; AI-001 → [US-CAP-01](#us-cap-01--enchaîner-automatiquement-les-étapes-ia-activées), [US-CAP-03](#us-cap-03--découper-chaque-document-en-blocs-heading-information-ou-requirement), [US-CAP-05](#us-cap-05--signaler-une-découpe-incertaine), [US-CAP-09](#us-cap-09--caractériser-chaque-bloc-avec-un-niveau-de-confiance-low-medium-ou-high), [US-CAP-11](#us-cap-11--reprendre-un-traitement-interrompu-sans-doublon) ; AI-002 → [US-CAP-03](#us-cap-03--découper-chaque-document-en-blocs-heading-information-ou-requirement), [US-CAP-04](#us-cap-04--capturer-les-images-sans-en-lire-le-contenu) ; AI-003 → [US-CAP-07](#us-cap-07--traduire-automatiquement-vers-langlais-de-travail) ; AI-004 → [US-CAP-09](#us-cap-09--caractériser-chaque-bloc-avec-un-niveau-de-confiance-low-medium-ou-high), [US-CAP-12](#us-cap-12--relancer-automatiquement-les-modèles-sur-les-seules-exigences-modifiées-par-une-nouvelle-version) ; AI-005 → [US-CAP-01](#us-cap-01--enchaîner-automatiquement-les-étapes-ia-activées), [US-CAP-12](#us-cap-12--relancer-automatiquement-les-modèles-sur-les-seules-exigences-modifiées-par-une-nouvelle-version) (détail de l'allocation : US-ALM) ; AI-006 → [US-CAP-12](#us-cap-12--relancer-automatiquement-les-modèles-sur-les-seules-exigences-modifiées-par-une-nouvelle-version), [US-CAP-13](#us-cap-13--repartir-de-zéro-sur-une-exigence-issue-dune-fusion-ou-dune-scission) ; AI-009 → [US-CAP-01](#us-cap-01--enchaîner-automatiquement-les-étapes-ia-activées) ; AI-010 → [US-CAP-10](#us-cap-10--dire-quaucun-modèle-ne-sapplique-sans-en-emprunter-un-en-silence) (système sans modèle : [US-ALM-20](05-allocation.md#us-alm-20--allouer-à-la-main-un-système-sans-modèle)) ; AI-011 → [US-CAP-12](#us-cap-12--relancer-automatiquement-les-modèles-sur-les-seules-exigences-modifiées-par-une-nouvelle-version), [US-CAP-13](#us-cap-13--repartir-de-zéro-sur-une-exigence-issue-dune-fusion-ou-dune-scission) ; AI-012 → [US-CAP-11](#us-cap-11--reprendre-un-traitement-interrompu-sans-doublon) ; AI-014 → [US-CAP-09](#us-cap-09--caractériser-chaque-bloc-avec-un-niveau-de-confiance-low-medium-ou-high) (affichage du niveau : [US-ALM-05](05-allocation.md#us-alm-05--voir-le-niveau-de-confiance-de-lia-sur-la-nature-et-la-classe)) ; CAPT-T01 → [US-CAP-02](#us-cap-02--régler-la-conversion-du-document-source) ; CAPT-T02 → [US-CAP-02](#us-cap-02--régler-la-conversion-du-document-source) ; CAPT-T03 → [US-CAP-02](#us-cap-02--régler-la-conversion-du-document-source) ; DOM-003 → [US-CAP-03](#us-cap-03--découper-chaque-document-en-blocs-heading-information-ou-requirement) ; DOM-012 → [US-CAP-03](#us-cap-03--découper-chaque-document-en-blocs-heading-information-ou-requirement), [US-CAP-13](#us-cap-13--repartir-de-zéro-sur-une-exigence-issue-dune-fusion-ou-dune-scission) ; JRN-005 → [US-CAP-12](#us-cap-12--relancer-automatiquement-les-modèles-sur-les-seules-exigences-modifiées-par-une-nouvelle-version) ; TYPE-T05 → [US-CAP-10](#us-cap-10--dire-quaucun-modèle-ne-sapplique-sans-en-emprunter-un-en-silence).
- Non couvertes, avec la raison : LANG-003 (langue de l'export client) — couverte par l'épopée US-CMP ([US-CMP-28](09-compliance.md#us-cmp-28--exporter-le-registre-de-conformité-avec-options)), langue par défaut en point ouvert ; LANG-005 — caduque (remplacée par DEC-096, une seule langue source par tender) ; AI-007 (même Q&A quel que soit le type) — couverte par l'épopée US-QA ([US-QA-02](11-qa.md#us-qa-02--parcourir-le-registre-en-deux-vues-par-statut), DEC-021) ; AI-008 (REX / Chat) — hors V1 (DEC-021), pas de story ; AI-013 (consolidation et droits calculés par les règles métier, jamais par un modèle) — couverte par l'épopée US-CMP ([US-CMP-20](09-compliance.md#us-cmp-20--consolider-les-verdicts-dune-exigence), consolidation) et US-X (droits côté serveur) ; CAPT-T04 (avertissement « demo only ») — critère propre à la maquette, sans objet dans le produit ; correction manuelle de la découpe — point ouvert (aucune décision).
