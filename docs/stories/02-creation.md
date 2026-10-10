<!-- Généré depuis le backlog du 10 octobre 2026 ; voir README.md pour les conventions. -->
# Création d'un tender (US-NEW)

Le chef de projet crée un tender avec un assistant en quatre étapes — identité, documents, mode de traitement, équipe de gestion — puis arrive sur le tender au travail (JRN-001, LIFE-001).
Ce qui s'y décide structure tout le reste et ne se corrige pas ensuite : la **ligne produit** (le système sur lequel le tender est émis : Turnkey, SIG, RSC), le **produit** (la déclinaison du système qui choisit le modèle d'allocation) ou, pour un Turnkey, la **combinaison** de produits, et le **mode d'assistance IA** (DEC-049, DEC-095). Un tender **Mainline** est un tender SIG de produit Mainline (DEC-047).
Une seule **langue source** par tender ; la langue de travail est toujours l'anglais (DEC-096, LANG-001). Le casting des systèmes ne se fait pas ici, mais dans Team casting (voir US-TEAM).

### US-NEW-01 — Décrire l'identité du tender
**Carte :** En tant que chef de projet, je veux saisir l'identité d'un nouveau tender en une seule fois, afin que tous les écrans portent le même nom et la même référence.
**Conversation :** L'étape 1 « Project identity » demande le nom et la référence BO-ID, obligatoires, puis la région, l'émetteur et la date de soumission, facultatifs ; la date de soumission alimente le compte à rebours du tender. La ligne produit, le produit et la langue source, sur la même étape, sont traités par [US-NEW-02](#us-new-02--choisir-la-ligne-produit-fixée-à-la-création) à [US-NEW-04](#us-new-04--déclarer-la-langue-source-unique-du-tender). On avance par « Continue → » et on revient par « ← Back » ou par la colonne d'étapes.
**Maquette :** Nouveau tender — `creation-projet.html` (route `#new`), étape 1, Wizard Stepper Panel, Wizard Step Item, Form Field Row.
**Règles :** LIFE-001, LIFE-T01, JRN-001, DOM-001  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Sans nom ou sans BO-ID, « Continue → » n'avance pas et affiche « Project name and BO-ID are required ».
2. Le serveur refuse aussi de créer un tender sans nom ou sans BO-ID, quel que soit le chemin pris dans l'assistant (LIFE-T01).
3. Région, émetteur (« Tender issuer ») et date de soumission (« Submission deadline ») sont facultatifs ; un champ vide apparaît « — » au récapitulatif.
4. On peut revenir à toute étape précédente ; on n'avance vers une étape suivante, par bouton ou par la colonne d'étapes, que si l'étape courante est valide ; « Step N of 4 » indique où l'on est.
5. « Cancel » quitte l'assistant sans rien créer et ramène à l'accueil.
Écart maquette : la date de soumission a une valeur par défaut fixe, et ni la région, ni l'émetteur, ni la date ne sont conservés sur le tender créé (seul un nombre de jours l'est).
Point ouvert : la liste réelle des régions n'est pas fournie (acronymes provisoires) ; l'unicité du BO-ID n'est décidée nulle part ; qui peut créer un tender n'est pas fixé (JRN-001, « politique globale à préciser »).

### US-NEW-02 — Choisir la ligne produit, fixée à la création
**Carte :** En tant que chef de projet, je veux choisir la ligne produit du tender en voyant ce qu'elle implique, afin que l'allocation suive le bon modèle dès la capture.
**Conversation :** La ligne produit sélectionne seule la configuration, les référentiels et les modèles applicables (DEC-007). Les types à couvrir sont Turnkey, SIG, Mainline et RSC (DEC-004) ; Mainline n'est pas une ligne mais un produit de SIG (DEC-047, voir [US-NEW-03](#us-new-03--choisir-le-produit-ou-la-combinaison-dun-turnkey)). Sous la ligne choisie, une phrase dit sa conséquence sur l'allocation. Une erreur de ligne ne se corrige qu'en recréant le tender (DEC-095).
**Maquette :** Nouveau tender — `creation-projet.html` (route `#new`), étape 1, sélecteur « Product line » et sa note, Form Field Row.
**Règles :** DEC-004, DEC-007, DEC-047, DEC-059, DEC-095, LIFE-001, LIFE-002, TYPE-T05  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Turnkey, SIG (dont Mainline), RSC
**Critères d'acceptation :**
1. « Product line » est obligatoire et propose Turnkey, SIG et RSC, Turnkey étant sélectionné par défaut.
2. Sous la ligne choisie s'affiche sa conséquence : Turnkey « Routes to systems; each derives its ABS / PBS / OBS and person. », SIG « Derives ABS, PBS and OBS, then the person for each OBS. », une ligne sans modèle « No model supplied yet — allocated by hand. »
3. Le libellé est « RSC » partout (assistant, paramètres, cartes) ; ni « RCS », ni « INFRA », ni « Rolling Stock » ne sont proposés.
4. Une fois le tender créé, aucune action ne change la ligne produit : les paramètres l'affichent en lecture seule avec « Not editable, by decision — not a missing control. » (voir US-CFG), et le serveur refuse toute modification.
5. Une ligne sans modèle fourni ne reçoit jamais en silence la configuration de SIG ou de Turnkey (TYPE-T05, voir [US-CAP-10](04-capture-ia.md#us-cap-10--dire-quaucun-modèle-ne-sapplique-sans-en-emprunter-un-en-silence)).
Écart maquette : la ligne « Services » est encore proposée.
Point ouvert : « Services » ne fait pas partie des types de DEC-004 — à garder ou retirer, non tranché. L'orthographe RSC (DEC-059) est une déduction à confirmer et le rapport RSC / RST reste ouvert ; les particularités de RSC ne sont pas fournies (OPEN-15).

### US-NEW-03 — Choisir le produit, ou la combinaison d'un Turnkey
**Carte :** En tant que chef de projet, je veux indiquer le produit du tender, ou sa combinaison s'il est Turnkey, afin que le bon modèle d'allocation et les bonnes clés s'appliquent.
**Conversation :** Le produit décrit ce que le tender est et sélectionne le modèle d'allocation ; il se choisit à la création et ne se corrige plus (DEC-049). Pour SIG, les produits connus sont Urban, Mainline Wayside et Mainline Onboard (DEC-047, DEC-061). Un Turnkey n'a pas de produit propre mais une combinaison de produits de plusieurs systèmes, dont la matrice n'est pas fournie (DEC-048). Le modèle qui découle du produit reste réglable ensuite dans les paramètres (voir US-CFG).
**Maquette :** Nouveau tender — `creation-projet.html` (route `#new`), étape 1, champ « Product » / « Combination » et sa note, Form Field Row.
**Règles :** DEC-047, DEC-048, DEC-049, DEC-061, DEC-007, LIFE-002  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Turnkey (combinaison), SIG (dont Mainline), RSC
**Critères d'acceptation :**
1. Sur SIG, le champ s'appelle « Product » et propose Urban, Mainline Wayside et Mainline Onboard.
2. Pour Mainline Wayside ou Mainline Onboard, une note dit que l'ABS, le PBS et l'OBS seront dérivés des clés de ce produit ; pour Urban, elle dit que ce produit n'est pas sur les clés.
3. Sur Turnkey, le champ s'appelle « Combination », n'offre aucune valeur (« — Not available — ») et sa note « Placeholder. » dit que la matrice des combinaisons n'a pas été fournie ; aucune liste plausible n'est inventée.
4. Sur une ligne dont les produits ne sont pas fournis (RSC…), le champ « Product » est inactif et sa note le dit.
5. Le produit choisi est enregistré sur le tender : un tender SIG Mainline Wayside ouvre Allocation sur les clés Mainline Wayside.
6. Après création, le produit n'est modifiable nulle part : les paramètres l'affichent en lecture seule et le serveur refuse le changement.
Point ouvert : la matrice des combinaisons Turnkey (DEC-048) et les produits de RSC (DEC-047) sont à fournir ; la maille de l'OBS du modèle Urban n'est pas tranchée.

### US-NEW-04 — Déclarer la langue source unique du tender
**Carte :** En tant que chef de projet, je veux indiquer la langue dans laquelle les documents du tender sont écrits, afin que la traduction vers l'anglais se fasse seule quand il le faut.
**Conversation :** Un tender n'a qu'une langue source : tous ses documents sont dans cette langue, il n'y a pas de dossier multilingue (DEC-096). Si c'est l'anglais, aucune traduction ne tourne ; sinon, la traduction automatique vers l'anglais s'insère entre la capture et la caractérisation (voir [US-CAP-07](04-capture-ia.md#us-cap-07--traduire-automatiquement-vers-langlais-de-travail)). La langue de travail de l'outil reste l'anglais pour tous les tenders (LANG-001).
**Maquette :** Nouveau tender — `creation-projet.html` (route `#new`), étape 1, champ « Source language » ; étape 2, langue affichée sur chaque Document / File Card.
**Règles :** DEC-096, DEC-019, LANG-001, LANG-002  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. L'étape 1 propose un seul champ « Source language », anglais par défaut ; aucun choix de langue n'existe par document.
2. À l'étape 2, chaque document joint affiche cette langue ; changer la langue à l'étape 1 met la liste de l'étape 2 à jour.
3. Le récapitulatif affiche la langue source et le tender créé la conserve.
4. Avec une langue source autre que l'anglais, le traitement du tender comprend l'étape de traduction ; avec l'anglais, il ne la comprend pas.
5. Aucun écran, à la création ou après, ne propose une langue de travail autre que l'anglais.
Point ouvert : la liste des langues proposées n'est pas décidée (la maquette offre English, French, German, Spanish) ; un changement de langue source après création n'est pas décidé.

### US-NEW-05 — Joindre et ordonner les documents source
**Carte :** En tant que chef de projet, je veux joindre tous les documents du tender dans leur ordre de lecture, afin qu'ils soient capturés comme un seul tender continu.
**Conversation :** Un tender arrive souvent en plusieurs documents : on les joint tous et on les ordonne, ils se lisent bout à bout dans cet ordre. Les formats à prendre en charge sont le PDF texte ou scanné, Word, Excel et les échanges DOORS (DEC-018). On peut créer le tender sans document et en ajouter plus tard ; les nouvelles versions d'un document s'ajoutent ensuite dans Documents & versions (voir US-DOC).
**Maquette :** Nouveau tender — `creation-projet.html` (route `#new`), étape 2 « Source documents », Upload Dropzone, Document / File Card, Warning / Notice Box.
**Règles :** LIFE-001, LIFE-004, DEC-018, DEC-069, DOM-001, DOM-002  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. On peut déposer ou choisir plusieurs fichiers ; chaque document joint montre son nom, son nombre de pages, sa taille et la langue source du tender.
2. ▲ / ▼ (« Move up » / « Move down ») changent la position ; le numéro affiché est la position de lecture, et cet ordre devient celui des documents du tender créé.
3. ✕ retire un document de la liste avant création, sans autre effet.
4. Sans document, la création reste possible ; un avertissement dit qu'Allocation reste vide tant qu'aucun document n'est joint.
5. Chaque document joint devient un document du tender avec sa première version ; aucune version n'est attachée au tender entier (DEC-069).
6. Un fichier dans un format non pris en charge est refusé avec un message qui le dit.
Écart maquette : seuls des PDF sont annoncés, et les documents sont fictifs (pas de vrai choix de fichier, rien n'est conservé sur le tender créé).
Point ouvert : la liste exacte des formats et contrats d'import (DOORS, Excel) et le cas d'un PDF fait uniquement d'images sont à préciser avec l'équipe technique (OPEN-10, OPEN-12) ; aucune limite de taille n'est décidée.

### US-NEW-06 — Choisir le mode d'assistance IA, fixé à la création
**Carte :** En tant que chef de projet, je veux choisir ce que l'IA fait sur ce tender avant que la capture démarre, afin qu'elle ne fasse que les étapes en lesquelles j'ai confiance.
**Conversation :** L'étape 3 « Processing mode » propose deux modes, « AI-assisted » (recommandé) et « AI segmentation only », et le détail des trois étapes IA (Capture, Characterisation, Allocation), chacune décrite allumée ou éteinte. Le mode détermine la structure du travail : il est fixé à la création, affiché en lecture seule ensuite, et se tromper oblige à recréer le tender (DEC-095). Les étapes activées s'enchaîneront sans pause de validation (voir [US-CAP-01](04-capture-ia.md#us-cap-01--enchaîner-automatiquement-les-étapes-ia-activées)).
**Maquette :** Nouveau tender — `creation-projet.html` (route `#new`), étape 3, Selectable Preset Card, Toggle Setting Row, Warning / Notice Box (« Manual mode »).
**Règles :** DEC-095, DEC-018, LIFE-002, LIFE-003, AI-009, DOM-001  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. « AI-assisted » est sélectionné par défaut et active les trois étapes ; « AI segmentation only » n'active que la capture.
2. Chaque étape affiche ce qu'elle fait quand elle est allumée et ce qui reste à faire à la main quand elle est éteinte (par exemple « Off — every requirement starts unclassified. ») ; modifier une étape hors d'un mode affiche « Custom », retrouver la combinaison d'un mode le resélectionne.
3. Characterisation annonce la nature et la classe avec une confiance Low / Medium / High ; Allocation annonce le routage vers les systèmes (Turnkey) ou la dérivation ABS / PBS / OBS (tender à un système).
4. Tout éteindre affiche « No AI processing. The project opens immediately — you build every requirement by hand. »
5. L'écran dit « This mode is fixed once the tender is created » ; après création, le mode est affiché en lecture seule dans les paramètres, aucune action ne le change et le serveur refuse toute modification.
Écart maquette : le mode est une seule valeur pour toute la démonstration, pas une propriété du tender, et les paramètres ne l'affichent pas. La phrase « The AI never overwrites a manual correction » contredit les relances qui écrasent les dérivations (ALLOC-015, DEC-027).
Point ouvert : DEC-095 fige « le mode d'assistance IA » sans dire si les réglages par étape en font partie. En mode tout manuel, la manière de créer les exigences à la main n'est pas spécifiée (« Edit segmentation » est masqué dans la maquette). L'estimation de durée affichée n'a pas de règle.

### US-NEW-07 — Constituer l'équipe de gestion du projet
**Carte :** En tant que chef de projet, je veux nommer dès la création les autres personnes qui géreront le tender avec moi, afin que l'équipe de gestion existe dès le premier jour.
**Conversation :** Le créateur est automatiquement le premier membre de l'équipe de gestion, sur tout le tender, et ne peut pas être retiré ici. Ajouter d'autres chefs de projet est facultatif et ne bloque jamais la création. Le casting des systèmes (contributeurs, périmètres) et la gestion ultérieure de l'équipe se font dans Team casting (voir [US-TEAM-03](12-casting-droits.md#us-team-03--composer-léquipe-de-gestion-du-projet)), et l'absence de casting n'arrête pas la capture (LIFE-T02).
**Maquette :** Nouveau tender — `creation-projet.html` (route `#new`), étape 4, Project Management Team Section, Team Member Row, Search-to-Add Combobox.
**Règles :** LIFE-001, LIFE-003, LIFE-T02, ACC-001, ACC-002, ACC-003, DEC-009  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. La personne connectée apparaît en premier, identifiée par l'annuaire (SSO), avec « Never removed — created the project » et sans bouton de retrait.
2. Le champ « Search a person via SSO to add another project manager… » propose des personnes de l'annuaire ; sans résultat, il affiche « No match in the directory. »
3. Choisir une personne l'ajoute comme « Project manager », vide le champ et le laisse prêt pour l'ajout suivant ; une personne déjà membre n'est plus proposée.
4. Un membre ajouté se retire par ✕ avant la création.
5. Après création, chaque membre voit le tender dans « My tenders » avec le rôle « Project manager » et le retrouve dans l'équipe de gestion de Team casting.
Écart maquette : l'équipe saisie ici est stockée sur le tender mais Team casting ne la lit pas ; l'annuaire est une liste locale de démonstration.

### US-NEW-08 — Vérifier le récapitulatif et créer le tender
**Carte :** En tant que chef de projet, je veux relire tout ce que j'ai saisi puis créer le tender, afin d'arriver directement sur un tender au travail.
**Conversation :** L'étape 4 se termine par un récapitulatif de tout le tender et par « ✓ Create project ». La création ferme l'assistant et lance le traitement : avec une étape IA active, on arrive sur le tableau de bord pendant que la capture tourne en arrière-plan ; en mode tout manuel, on arrive directement dans Allocation (JRN-001). Le tender apparaît aussitôt dans « My tenders ».
**Maquette :** Nouveau tender — `creation-projet.html` (route `#new`), « Summary » de l'étape 4 (Key-Value Summary Row), Processing Overlay ; puis Tableau de bord (route `#dashboard`) ou Allocation (route `#review`).
**Règles :** JRN-001, LIFE-001, LIFE-003, LIFE-T01, AI-009, PLAT-001  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Le récapitulatif liste nom, BO-ID, ligne produit, produit ou combinaison, région, langue source, émetteur, échéance, documents, mode de traitement et équipe de gestion ; un nom, un BO-ID ou un produit manquant y paraît « Not set », l'absence de document « None attached ».
2. « ✓ Create project » ne crée le tender que si le nom et le BO-ID sont présents ; sinon l'assistant revient à l'étape 1 avec le message d'[US-NEW-01](#us-new-01--décrire-lidentité-du-tender).
3. Avec au moins une étape IA active, une confirmation « Project created » dit que la capture a démarré en arrière-plan, puis le tableau de bord du nouveau tender s'ouvre.
4. En mode tout manuel, le tender s'ouvre directement dans Allocation.
5. Le nouveau tender figure en tête de « My tenders » pour chaque membre de l'équipe de gestion, en traitement s'il a une étape IA, et il survit à une déconnexion (PLAT-001).
6. Si l'enregistrement échoue, aucun succès n'est affiché, aucun tender incomplet n'apparaît et la saisie de l'assistant est conservée.

### US-NEW-09 — Retrouver dans le tender créé tout ce que l'assistant a fixé
**Carte :** En tant que chef de projet, je veux que le tender créé porte exactement ce que l'assistant a fixé, afin que chaque écran applique la bonne configuration sans réglage supplémentaire.
**Conversation :** Un tender est un dossier de travail : identité, documents ordonnés, mode de traitement et équipe de gestion (DOM-001). Son type choisit seul la configuration et les modèles (DEC-007) : un Turnkey garde ses deux passes, un SIG n'a rien de la passe 1 Turnkey, Mainline et RSC chargent leur propre configuration. Il naît sans stratégie d'écart (DEC-110) et sans casting de système.
**Maquette :** Paramètres — `dashboard-et-config.html` (route `#config`), sections General et Allocation model (Config Field Row) ; Allocation — `revue-documentaire.html` (route `#review`).
**Règles :** DOM-001, DEC-007, DEC-049, DEC-095, DEC-110, LIFE-002, TYPE-T01, TYPE-T04, TYPE-T05, PLAT-001  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Turnkey, SIG (dont Mainline), RSC
**Critères d'acceptation :**
1. Le tender créé conserve nom, BO-ID, ligne produit, produit ou combinaison, langue source, mode, documents dans leur ordre et équipe de gestion ; les paramètres les relisent tels quels, ligne produit et produit en lecture seule.
2. Un tender Turnkey créé présente l'aiguillage vers les systèmes, puis le modèle de chaque système (TYPE-T04).
3. Un tender SIG créé n'affiche aucun champ, filtre, étape ni action de la passe 1 Turnkey (TYPE-T01).
4. Un tender Mainline ou RSC charge sa propre configuration ; si elle manque, l'écran le dit et ne lui substitue ni celle de SIG ni celle de Turnkey (TYPE-T05).
5. La liste des stratégies d'écart du tender est vide à la création (voir US-RSK pour l'écrire).
6. Aucun système n'a de contributeur tant que le casting n'est pas fait, et la capture tourne quand même (LIFE-T02).
Écart maquette : un tender créé dans la maquette réutilise le contenu du tender de référence (bandeau « Prototype scope ») ; ni l'émetteur, ni l'échéance, ni les documents, ni le mode ne sont conservés sur lui.
Point ouvert : la possibilité de modifier les autres réglages de traitement après le démarrage n'est pas décidée (LIFE-002, OPEN-05 résiduel).

## Couverture
- Règles couvertes : LIFE-001 → [US-NEW-01](#us-new-01--décrire-lidentité-du-tender), [US-NEW-02](#us-new-02--choisir-la-ligne-produit-fixée-à-la-création), [US-NEW-05](#us-new-05--joindre-et-ordonner-les-documents-source), [US-NEW-07](#us-new-07--constituer-léquipe-de-gestion-du-projet), [US-NEW-08](#us-new-08--vérifier-le-récapitulatif-et-créer-le-tender) ; LIFE-002 → [US-NEW-02](#us-new-02--choisir-la-ligne-produit-fixée-à-la-création), [US-NEW-03](#us-new-03--choisir-le-produit-ou-la-combinaison-dun-turnkey), [US-NEW-06](#us-new-06--choisir-le-mode-dassistance-ia-fixé-à-la-création), [US-NEW-09](#us-new-09--retrouver-dans-le-tender-créé-tout-ce-que-lassistant-a-fixé) ; LIFE-003 → [US-NEW-06](#us-new-06--choisir-le-mode-dassistance-ia-fixé-à-la-création), [US-NEW-07](#us-new-07--constituer-léquipe-de-gestion-du-projet), [US-NEW-08](#us-new-08--vérifier-le-récapitulatif-et-créer-le-tender) (enchaînement : [US-CAP-01](04-capture-ia.md#us-cap-01--enchaîner-automatiquement-les-étapes-ia-activées)) ; LIFE-004 → [US-NEW-05](#us-new-05--joindre-et-ordonner-les-documents-source) (suite : US-DOC) ; LIFE-T01 → [US-NEW-01](#us-new-01--décrire-lidentité-du-tender), [US-NEW-08](#us-new-08--vérifier-le-récapitulatif-et-créer-le-tender) ; LIFE-T02 → [US-NEW-07](#us-new-07--constituer-léquipe-de-gestion-du-projet), [US-NEW-09](#us-new-09--retrouver-dans-le-tender-créé-tout-ce-que-lassistant-a-fixé) ; LANG-001 → [US-NEW-04](#us-new-04--déclarer-la-langue-source-unique-du-tender) ; LANG-002 → [US-NEW-04](#us-new-04--déclarer-la-langue-source-unique-du-tender) ; AI-009 → [US-NEW-06](#us-new-06--choisir-le-mode-dassistance-ia-fixé-à-la-création), [US-NEW-08](#us-new-08--vérifier-le-récapitulatif-et-créer-le-tender) ; JRN-001 → [US-NEW-01](#us-new-01--décrire-lidentité-du-tender), [US-NEW-08](#us-new-08--vérifier-le-récapitulatif-et-créer-le-tender) ; DOM-001 → [US-NEW-01](#us-new-01--décrire-lidentité-du-tender), [US-NEW-05](#us-new-05--joindre-et-ordonner-les-documents-source), [US-NEW-06](#us-new-06--choisir-le-mode-dassistance-ia-fixé-à-la-création), [US-NEW-09](#us-new-09--retrouver-dans-le-tender-créé-tout-ce-que-lassistant-a-fixé) ; DOM-002 → [US-NEW-05](#us-new-05--joindre-et-ordonner-les-documents-source) ; TYPE-T01 → [US-NEW-09](#us-new-09--retrouver-dans-le-tender-créé-tout-ce-que-lassistant-a-fixé) ; TYPE-T04 → [US-NEW-09](#us-new-09--retrouver-dans-le-tender-créé-tout-ce-que-lassistant-a-fixé) ; TYPE-T05 → [US-NEW-02](#us-new-02--choisir-la-ligne-produit-fixée-à-la-création), [US-NEW-09](#us-new-09--retrouver-dans-le-tender-créé-tout-ce-que-lassistant-a-fixé).
- Non couvertes, avec la raison : TYPE-T02 (détail SIG ouvert directement) — couverte par l'épopée US-ALM ([US-ALM-13](05-allocation.md#us-alm-13--allouer-sur-un-tender-sig-autonome-sans-axe-système)) ; TYPE-T03 — partie « mêmes règles d'allocation » couverte par US-ALM ([US-ALM-12](05-allocation.md#us-alm-12--travailler-dans-le-détail-dun-système-dun-turnkey)), partie « pouvoirs de gestion globale » par [US-DOC-08](03-documents.md#us-doc-08--réserver-la-gestion-des-documents-à-léquipe-de-gestion-du-projet) et US-TEAM ; TYPE-T06 — couverte par [US-HOME-04](01-accueil.md#us-home-04--voir-la-liste-de-mes-tenders) et par le champ « Variantes » de chaque story (règle de recette, sans comportement propre) ; ligne « Services » — point ouvert (absente de DEC-004).
