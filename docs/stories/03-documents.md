<!-- Généré depuis le backlog du 10 octobre 2026 ; voir README.md pour les conventions. -->
# Documents et versions (US-DOC)

L'écran « Documents & versions » rassemble les documents source du tender : leur ordre, leur état de traitement, leurs versions, leur retrait et leur export (JRN-005, LIFE-004). L'équipe de gestion du projet (le chef de projet) le gère ; un contributeur le consulte.
Termes : **version** = un état d'un document ; une version appartient à un document, jamais au tender entier (DEC-069) ; **écart** = ce qu'une nouvelle version ajoute, modifie et supprime par rapport à la précédente ; **réponse rouverte** = un verdict de Compliance remis en attente parce que la version a modifié l'exigence (DEC-016, DEC-122).
La lecture détaillée des changements se fait dans Allocation (colonne Changes : US-CHG ; onglet Changes de la vue Document : US-DOCV).

### US-DOC-01 — Voir les documents du tender dans leur ordre de lecture
**Carte :** En tant que chef de projet, je veux voir tous les documents du tender dans l'ordre où ils se lisent, avec leur état et leur poids, afin de savoir de quoi le tender est fait et ce qui reste à traiter.
**Conversation :** La liste suit l'ordre du tender, qui est aussi celui de la lecture dans Allocation et des exports. Chaque ligne dit la position, le document, son état de traitement, sa version en vigueur et son poids en exigences ; un bandeau résume l'ensemble. Une recherche et un filtre aident sur les gros tenders (une trentaine de documents). La cloche de l'écran (réponses rouvertes, documents non traités) suit la règle commune des notifications (voir US-X).
**Maquette :** Documents & versions — `documents.html` (route `#documents`), Document Summary Strip, Filter Toolbar, Document Table.
**Règles :** LIFE-004, JRN-005, DOM-002, DEC-069, DEC-012, PLAT-001  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Chaque ligne montre la position dans le tender, le nom et le fichier, l'état (« Ready », « Processing » ou « Not processed »), la version en vigueur avec sa date et, s'il y en a plusieurs, le nombre de versions, puis le poids : nombre d'exigences, barre et part du tender en %.
2. Le bandeau compte « Documents in this tender », « Requirements across them », « Still processing » et « Answers reopened by a new version » ; ces deux derniers passent en couleur d'alerte quand ils ne valent pas zéro.
3. Un document en cours de traitement montre une barre d'avancement et l'étape en cours.
4. La recherche « Search a document by name or filename… » et le filtre (« All documents », « Not fully processed », « Has several versions », « Has reopened answers ») réduisent la liste ; sans résultat, la liste dit « No document matches this filter. »
5. Dans une liste filtrée, le numéro reste la vraie position du document dans le tender, pas son rang dans le filtre.
6. Tous les chiffres sont calculés sur les données enregistrées du tender, et un contributeur voit la même liste (voir [US-DOC-08](#us-doc-08--réserver-la-gestion-des-documents-à-léquipe-de-gestion-du-projet)).
Écart maquette : la liste de démonstration est la même sur tous les tenders et ses compteurs sont écrits à la main.

### US-DOC-02 — Consulter l'historique des versions d'un document
**Carte :** En tant que chef de projet, je veux dérouler l'historique d'un document version par version, afin de savoir ce que chaque version a changé et ce qu'elle a rouvert.
**Conversation :** Chaque document avance à son rythme et son historique se lit document par document (DEC-069). Déplier une ligne montre ses versions, de la plus récente à la plus ancienne, avec l'écart de chacune par rapport à la précédente. Le détail mot à mot se lit dans Allocation (voir US-DOCV, onglet Changes).
**Maquette :** Documents & versions — `documents.html` (route `#documents`), Document Table (ligne dépliée), Version History Entry.
**Règles :** DEC-069, LIFE-012, DOM-002, JRN-005, DEC-122  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Un clic sur la ligne, ou Entrée / Espace au clavier, déplie l'historique ; un second clic le replie ; les boutons d'action de la ligne ne la déplient pas.
2. Chaque version montre son numéro, sa date et sa note ; la plus récente porte « Current ».
3. Chaque version après la première montre son écart : « +N added », « ~N modified », « −N removed ».
4. Une version qui a rouvert des réponses le dit (« N answers reopened by this version », verdicts revenus en attente, renvoi vers « Allocation › Document view › Changes ») avec le lien « Open Compliance → ».
5. Aucun écran n'affiche de version du tender entier : seules les versions de chaque document existent.
Point ouvert : la règle de numérotation des versions (automatique, alias, saisie libre) n'est pas décidée.

### US-DOC-03 — Réordonner les documents du tender
**Carte :** En tant que chef de projet, je veux déplacer un document plus tôt ou plus tard dans le tender, afin que le tender se lise dans le bon ordre.
**Conversation :** L'ordre des documents fait du tender un seul texte continu : il gouverne la lecture dans Allocation, l'ordre du document dans les tables et celui des exports (LIFE-004, LIFE-T03). Réordonner ne touche ni aux exigences ni au travail fait dessus.
**Maquette :** Documents & versions — `documents.html` (route `#documents`), boutons ↑ / ↓ de la Document Table.
**Règles :** LIFE-004, LIFE-T03, JRN-005, PLAT-001  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. « ↑ » (« Move earlier in the tender ») et « ↓ » (« Move later in the tender ») échangent le document avec son voisin ; ils sont inactifs au premier et au dernier rang.
2. Un message confirme « <document> moved — tender order updated ».
3. Le nouvel ordre est celui de la vue Document et de l'ordre du document dans Allocation et Compliance, pour toute l'équipe.
4. Un export du tender ou d'un document reprend les exigences dans ce même ordre (LIFE-T03).
5. Réordonner ne modifie aucune exigence, aucun statut ni aucune réponse.
Écart maquette : le nouvel ordre ne se propage pas aux autres écrans et se perd au rechargement.

### US-DOC-04 — Téléverser une nouvelle version d'un document
**Carte :** En tant que chef de projet, je veux remplacer un document par sa nouvelle version et voir aussitôt ce qu'elle change, afin que le travail touché soit repéré ici et non découvert plus tard.
**Conversation :** Une nouvelle version remplace le document sur place ; elle ne crée ni un autre document ni un autre tender (DOM-002). L'écart avec la version précédente se calcule seul. Ses effets sur le travail sont traités ailleurs et seulement comptés ici : exigences ajoutées ou modifiées remises « To review » (voir US-CHG), relance automatique des modèles sur les seules exigences modifiées (voir [US-CAP-12](04-capture-ia.md#us-cap-12--relancer-automatiquement-les-modèles-sur-les-seules-exigences-modifiées-par-une-nouvelle-version)), verdicts rouverts dans Compliance (voir [US-CMP-27](09-compliance.md#us-cmp-27--rouvrir-les-verdicts-dune-exigence-modifiée-par-une-nouvelle-version)). Le nombre de réponses rouvertes annoncé ici est exactement celui que Compliance rouvre (DEC-122).
**Maquette :** Documents & versions — `documents.html` (route `#documents`), bouton « Upload a new version — runs gap analysis » de la Document Table, Version History Entry, Toast.
**Règles :** DEC-069, DOM-002, LIFE-012, JRN-005, DEC-016, DEC-122, DEC-027, LIFE-011  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Le fichier téléversé devient la version en vigueur du document (« Current »), avec un numéro supérieur et la date du jour ; la version précédente reste dans l'historique.
2. L'écart est calculé et affiché sur la nouvelle version : « +N added », « ~N modified », « −N removed ».
3. Un message résume « <version> uploaded — gap analysis: +N ~N −N » et, s'il y a lieu, « N answers reopened » ; le même nombre paraît sur la version, sur la ligne du document et dans le bandeau.
4. Ce nombre est égal au nombre d'affectations que Compliance remet en attente pour ce document (DEC-122).
5. Seules les exigences de ce document peuvent changer ; les autres documents gardent leur version, leurs exigences et leur travail.
6. Sans autre action, Allocation (colonne et onglet Changes), Compliance et le tableau de bord reflètent la nouvelle version.
Écart maquette : l'écart et le choix des exigences « modifiées » sont simulés, aucun fichier n'est lu, et la version téléversée n'atteint pas Allocation.
Point ouvert : la manière de reconnaître qu'une exigence est la même, modifiée, fusionnée ou scindée d'une version à l'autre n'est pas spécifiée (OPEN-07, DOM-012) ; les réglages « Re-segmentation on new version », « Detect addendum-as-answer » et « Numbering » n'ont pas de règle ; le sort de la stratégie d'écart et des risques d'un verdict rouvert n'est pas décidé.

### US-DOC-05 — Retirer un document en annonçant ce qui sera perdu
**Carte :** En tant que chef de projet, je veux retirer un document joint par erreur en sachant avant d'agir ce qu'il emporte, afin de ne jamais perdre de travail sans l'avoir décidé.
**Conversation :** Retirer un document emporte ses exigences et tout le travail fait dessus ; l'écran le dit avant d'agir, pas après. C'est une action sur un document entier, distincte de l'interdiction de supprimer un bloc capturé (DEC-094, voir [US-CAP-06](04-capture-ia.md#us-cap-06--écarter-un-bloc-capturé-par-erreur-sans-le-supprimer)). Les documents restants gardent leur ordre.
**Maquette :** Documents & versions — `documents.html` (route `#documents`), bouton ✕ « Remove this document from the tender », Modal Dialog « Remove this document? ».
**Règles :** LIFE-004, JRN-005, DEC-094, PLAT-003  ·  **Périmètre :** Pilote 1 (à confirmer)  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. ✕ ouvre une confirmation qui nomme le document, sa version en vigueur et sa position (« … is position N of M in this tender. »).
2. Pour un document traité, elle annonce le nombre d'exigences retirées et la perte de « every characterisation, allocation and compliance verdict recorded against them » ; pour un document non traité, elle dit que seul le fichier est retiré.
3. « Cancel », ou un clic hors de la fenêtre, ne change rien ; « Remove the document » retire le document.
4. Après le retrait, les autres documents gardent leur ordre, le bandeau et la liste d'export sont à jour, et un message dit combien d'exigences sont parties avec lui.
5. Les exigences retirées disparaissent d'Allocation, de Compliance, des compteurs et des statistiques.
6. Le retrait est inscrit au journal d'audit avec son auteur et sa date (PLAT-003).
Écart maquette : le retrait n'agit que sur cet écran.
Point ouvert : la conservation ou la récupération d'un document retiré n'est pas décidée (LIFE-006, OPEN-07) ; la maquette annonce « This cannot be undone ».

### US-DOC-06 — Ajouter un document en cours de tender
**Carte :** En tant que chef de projet, je veux ajouter un document, un addendum par exemple, à un tender déjà en cours, afin qu'il rejoigne le matériel existant au lieu d'ouvrir un autre tender.
**Conversation :** Un document peut arriver à tout moment. Il s'ajoute à la fin du tender, dans la langue source du tender (DEC-096), et suit les mêmes étapes que la capture initiale, selon le mode du tender (voir [US-CAP-01](04-capture-ia.md#us-cap-01--enchaîner-automatiquement-les-étapes-ia-activées)). On peut quitter l'écran et revenir pendant le traitement.
**Maquette :** Documents & versions — `documents.html` (route `#documents`), Upload Dropzone (variante horizontale) « Add a document to this tender », bouton « ＋ Add a document ».
**Règles :** LIFE-004, JRN-005, DEC-096, DEC-018, LANG-002, AI-009  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Le document déposé s'ajoute en dernière position, à l'état « Processing », avec le message « <document> added — AI processing started ».
2. Sa ligne montre l'étape en cours : capture, puis traduction depuis la langue source si ce n'est pas l'anglais, puis caractérisation, puis allocation si le mode l'active.
3. Le texte de la zone d'ajout annonce la traduction quand la langue source n'est pas l'anglais.
4. Le traitement continue si la personne quitte l'écran ; à son retour, la ligne montre l'état réel.
5. À la fin, la ligne passe « Ready » avec son nombre d'exigences et le message « <document> processed — N requirements ready to review » ; ses exigences apparaissent dans Allocation à la place du document dans l'ordre du tender.
6. Le nouveau document est proposé dans l'export par document dès son ajout.
Écart maquette : le document est fictif (nom, fichier, nombre d'exigences), le traitement est minuté, n'inclut pas l'allocation et ses libellés parlent encore de « class, system and type ».
Point ouvert : l'état d'échec et la reprise d'un traitement interrompu sont traités par [US-CAP-11](04-capture-ia.md#us-cap-11--reprendre-un-traitement-interrompu-sans-doublon).

### US-DOC-07 — Exporter les exigences d'un seul document
**Carte :** En tant que chef de projet, je veux exporter les exigences d'un seul document, afin de transmettre une partie du tender sans exporter le tout.
**Conversation :** On choisit le document, ce qu'on inclut — capture (structure, blocs, tableaux), caractérisation, allocation — et le format ; l'export garde l'ordre du document. Les formats à prendre en charge sont DOORS (9 et NG) et Excel (PLAT-004). L'export du registre de conformité destiné au client est une autre fonction (voir US-CMP).
**Maquette :** Documents & versions — `documents.html` (route `#documents`), bouton « Export one document », Modal Dialog « Export one document » (Modal Field Group).
**Règles :** LIFE-004, LIFE-T03, PLAT-004, PLAT-002, DEC-074  ·  **Périmètre :** Pilote 1 (à confirmer)  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. La fenêtre propose le document (« Doc N — nom », dans l'ordre du tender), les parties à inclure et le format.
2. Les trois parties sont cochées par défaut ; sans aucune, « Generate export » refuse avec « Select at least one step to export ».
3. Le fichier produit ne contient que les exigences de ce document, dans l'ordre du document (LIFE-T03).
4. Un message confirme le format, le document et le nombre d'exigences exportées.
5. La caractérisation exportée donne la nature et la classe ; aucune valeur Functional, Performance, Security, Interface ou Regulatory n'y figure (DEC-074).
6. L'export ne contient que ce que la personne a le droit de lire, contrôlé par le serveur (PLAT-002).
Écart maquette : l'export est simulé ; la fenêtre propose aussi CSV et ReqIF et décrit la caractérisation comme « class, system and type ».
Point ouvert : formats, correspondances de champs et aller-retour DOORS sont à contractualiser (OPEN-10, OPEN-12) ; la langue du texte d'exigence dans cet export n'est pas décidée (LANG-003 vise l'export client) ; le droit d'un contributeur à lancer cet export n'est pas tranché (LIFE-004 réserve la gestion à l'équipe projet, DEC-012 lui ouvre la lecture de tout le tender).

### US-DOC-08 — Réserver la gestion des documents à l'équipe de gestion du projet
**Carte :** En tant que chef de projet, je veux que seule l'équipe de gestion du projet puisse ajouter, réordonner, versionner ou retirer les documents, afin qu'aucun contributeur ne change le contenu du tender.
**Conversation :** Gérer les documents est une gestion globale du tender, réservée à l'équipe de gestion du projet (LIFE-004). Un contributeur lit tout le tender, documents compris (DEC-012), mais ne les gère pas, même s'il est contributeur SIG au sein d'un Turnkey (DEC-005). Le refus est appliqué par le serveur, pas seulement masqué à l'écran.
**Maquette :** Documents & versions — `documents.html` (route `#documents`), Document Table et Upload Dropzone ; vue contributeur non maquettée.
**Règles :** LIFE-004, DEC-012, DEC-005, ACC-007, PLAT-002, TYPE-T03  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes ; Turnkey (contributeur du système SIG)
**Critères d'acceptation :**
1. Un membre de l'équipe de gestion dispose de l'ajout, de ↑ / ↓, de la nouvelle version et du retrait.
2. Un contributeur voit la liste, le bandeau, les historiques de versions et la cloche, sans aucune de ces quatre actions.
3. Un ajout, un réordonnancement, une nouvelle version ou un retrait demandé par un contributeur, y compris par requête directe, est refusé par le serveur et ne change rien.
4. Sur un Turnkey, être contributeur du système SIG ne donne aucun droit de gestion des documents (TYPE-T03).
5. Une personne qui n'est pas membre du tender n'accède pas à l'écran.
Écart maquette : l'écran n'a aucune notion de rôle ; toutes les actions sont ouvertes à tous.

## Couverture
- Règles couvertes : LIFE-004 → [US-DOC-01](#us-doc-01--voir-les-documents-du-tender-dans-leur-ordre-de-lecture), [US-DOC-03](#us-doc-03--réordonner-les-documents-du-tender), [US-DOC-05](#us-doc-05--retirer-un-document-en-annonçant-ce-qui-sera-perdu), [US-DOC-06](#us-doc-06--ajouter-un-document-en-cours-de-tender), [US-DOC-07](#us-doc-07--exporter-les-exigences-dun-seul-document), [US-DOC-08](#us-doc-08--réserver-la-gestion-des-documents-à-léquipe-de-gestion-du-projet) ; LIFE-T03 → [US-DOC-03](#us-doc-03--réordonner-les-documents-du-tender), [US-DOC-07](#us-doc-07--exporter-les-exigences-dun-seul-document) ; JRN-005 → [US-DOC-01](#us-doc-01--voir-les-documents-du-tender-dans-leur-ordre-de-lecture), [US-DOC-02](#us-doc-02--consulter-lhistorique-des-versions-dun-document), [US-DOC-03](#us-doc-03--réordonner-les-documents-du-tender), [US-DOC-04](#us-doc-04--téléverser-une-nouvelle-version-dun-document), [US-DOC-05](#us-doc-05--retirer-un-document-en-annonçant-ce-qui-sera-perdu), [US-DOC-06](#us-doc-06--ajouter-un-document-en-cours-de-tender) (relance automatique : [US-CAP-12](04-capture-ia.md#us-cap-12--relancer-automatiquement-les-modèles-sur-les-seules-exigences-modifiées-par-une-nouvelle-version)) ; DOM-002 → [US-DOC-01](#us-doc-01--voir-les-documents-du-tender-dans-leur-ordre-de-lecture), [US-DOC-02](#us-doc-02--consulter-lhistorique-des-versions-dun-document), [US-DOC-04](#us-doc-04--téléverser-une-nouvelle-version-dun-document) ; LIFE-011 → [US-DOC-04](#us-doc-04--téléverser-une-nouvelle-version-dun-document) (déclenchement ; la relance elle-même : [US-CAP-12](04-capture-ia.md#us-cap-12--relancer-automatiquement-les-modèles-sur-les-seules-exigences-modifiées-par-une-nouvelle-version)) ; LANG-002 → [US-DOC-06](#us-doc-06--ajouter-un-document-en-cours-de-tender) ; AI-009 → [US-DOC-06](#us-doc-06--ajouter-un-document-en-cours-de-tender) ; TYPE-T03 → [US-DOC-08](#us-doc-08--réserver-la-gestion-des-documents-à-léquipe-de-gestion-du-projet) (pouvoirs de gestion globale selon le rattachement).
- Non couvertes, avec la raison : LIFE-T05 (nouvelle version qui rouvre un verdict) — couverte par l'épopée US-CMP ([US-CMP-27](09-compliance.md#us-cmp-27--rouvrir-les-verdicts-dune-exigence-modifiée-par-une-nouvelle-version)) ; [US-DOC-04](#us-doc-04--téléverser-une-nouvelle-version-dun-document) n'en affiche que le compte ; LIFE-T06 (suppression visible seulement dans la comparaison) — couverte par l'épopée US-DOCV (onglet Changes) ; récupération d'un document retiré — point ouvert (LIFE-006, OPEN-07) ; JRN-005 « suppression manuelle » et « comparaison » — lignes en retard (DEC-094, DEC-119) : seule la suppression d'un document entier est ici, la comparaison est dans US-DOCV / US-CHG.
