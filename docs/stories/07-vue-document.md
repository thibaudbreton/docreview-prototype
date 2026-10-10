<!-- Généré depuis le backlog du 10 octobre 2026 ; voir README.md pour les conventions. -->
# Vue Document d'Allocation (US-DOCV)

La vue Document d'Allocation montre le tender comme un document : chaque bloc à sa place, avec sa nature et, pour une exigence, son statut. Le chef de projet y vérifie la lecture de l'IA dans son contexte et y relit une nouvelle version ; un contributeur y lit tout le tender (JRN-002 ; JRN-005 pour les versions, téléversées depuis l'écran Documents — [US-DOC-04](03-documents.md#us-doc-04--téléverser-une-nouvelle-version-dun-document)).
- **Bloc** : un morceau du texte capturé — un titre, une information ou une exigence.
- **Nature** : ce qu'est un bloc, « Heading », « Information » ou « Requirement », rien d'autre (DEC-074).
- **Plan** (« Outline ») : l'arbre documents → sections → titres → exigences, dans le navigateur de gauche.
- **Version en vigueur** : la dernière version d'un document ; l'onglet « Changes » la compare à une version antérieure du même document.

### US-DOCV-01 — Lire le tender sous forme de document
**Carte :** En tant que chef de projet ou contributeur, je veux lire le tender comme un document, chaque bloc à sa place avec son état, afin de vérifier le travail dans le contexte du texte.
**Conversation :** « Review » et « Document », en tête d'Allocation, basculent entre la table et le document. Une feuille par document, dans l'ordre des documents, avec ses titres, informations, figures, tableaux et exigences à leur place. Une exigence porte son statut ; un titre ou une information n'en a jamais (DEC-073). Une figure s'affiche avec le nombre d'exigences capturées depuis elle, sans que son contenu soit lu (DEC-018, [US-CAP-04](04-capture-ia.md#us-cap-04--capturer-les-images-sans-en-lire-le-contenu)) ; la découpe des blocs relève de [US-CAP-03](04-capture-ia.md#us-cap-03--découper-chaque-document-en-blocs-heading-information-ou-requirement). Un contributeur lit tout le tender (DEC-012).
**Maquette :** Allocation, mode « Document » — `revue-documentaire.html` (route `#review`), Document Reading View, Document Block, Type Chip.
**Règles :** DEC-073, DEC-012, DEC-123, DEC-069, DEC-018, JRN-002 · **Périmètre :** Pilote 1 · **Variantes :** Toutes
**Critères d'acceptation :**
1. « Document » affiche les documents du tender en feuilles, dans leur ordre ; la première porte le nom et la référence du tender ouvert, et chaque feuille indique en pied son rang et sa version en vigueur.
2. Chaque exigence montre son identifiant, son texte et l'étiquette « Requirement · <statut> » (Incomplete, To review, To validate ou Allocated).
3. Aucun titre ni bloc d'information ne porte de statut.
4. Une exigence dont une entrée OBS n'a personne porte la marque « Unassigned », ou « n/m assigned » quand seules certaines ont une personne (DEC-123) ; la marque disparaît quand toutes en ont une.
5. Les blocs que la recherche ou les filtres écartent restent à leur place, estompés.
6. La même exigence reste sélectionnée et visible quand on passe de « Review » à « Document », et inversement.

### US-DOCV-02 — Naviguer dans le plan du tender
**Carte :** En tant que chef de projet ou contributeur, je veux un plan repliable du tender, afin d'aller à un passage sans faire défiler des centaines de pages.
**Conversation :** Le plan est l'onglet « Outline » du navigateur de gauche ; l'onglet « Changes » le rejoint quand un document a plusieurs versions ([US-DOCV-06](#us-docv-06--comparer-un-document-à-une-version-antérieure-onglet-changes)). Tout est replié au départ, car un vrai tender compte des dizaines de sections. Les informations et les figures restent dans le document, pas dans le plan. « Add a document » mène à l'écran Documents ([US-DOC-06](03-documents.md#us-doc-06--ajouter-un-document-en-cours-de-tender)).
**Maquette :** Allocation, mode « Document » — `revue-documentaire.html` (route `#review`), Left Navigator Panel (Nav Tree Section Header, Nav Tree Item, Search Box).
**Règles :** DEC-073, DEC-123, UX-001, JRN-002 · **Périmètre :** Pilote 1 · **Variantes :** Toutes
**Critères d'acceptation :**
1. Le plan liste les documents, leurs sections, leurs sous-titres et leurs exigences, avec le nombre d'exigences par document et par section ; tout est replié à l'ouverture.
2. Cliquer un document ou une section le déplie ou le replie ; cliquer une exigence ou un sous-titre fait défiler le document jusqu'à lui et l'ouvre dans le panneau de détail.
3. Chaque exigence du plan a un point de la couleur de son statut, et une pastille quand elle est To review, a une entrée sans personne, a des commentaires ou une découpe douteuse.
4. Une recherche ou un filtre actif déplie tout, estompe ce qui ne correspond pas, et le pied affiche « N results — filter active » ; sinon « N requirements · M sections ».
5. La recherche du plan et celle de la table sont un seul champ : taper dans l'une remplit l'autre.
6. Le navigateur se replie en un rail fin et se rouvre d'un clic.

### US-DOCV-03 — Ouvrir le détail d'un bloc depuis le document
**Carte :** En tant que chef de projet ou contributeur, je veux cliquer un bloc du document pour voir son détail à droite, afin de corriger ou valider sans quitter le texte.
**Conversation :** Le panneau de détail est le même que depuis la table (US-ALM). Un titre ou une information l'ouvre aussi, avec sa nature et sans statut (DEC-073). À l'inverse, la référence de paragraphe du détail ouvre le document à l'endroit du bloc ; Compliance a sa propre vue Document ([US-CMP-06](09-compliance.md#us-cmp-06--lire-la-conformité-sur-le-document)).
**Maquette :** Allocation, mode « Document » — `revue-documentaire.html` (route `#review`), Document Block, Detail / Assignment Panel, Paragraph Reference.
**Règles :** DEC-073, DEC-012, DEC-100 · **Périmètre :** Pilote 1 · **Variantes :** Toutes
**Critères d'acceptation :**
1. Cliquer une exigence dans le document l'encadre et ouvre son détail dans le panneau de droite.
2. Cliquer un titre ou une information ouvre le panneau avec sa nature, sans statut ni allocation.
3. Cliquer une figure fait seulement défiler jusqu'à elle, sans ouvrir de panneau.
4. Dans le détail d'une exigence, la référence « § n° titre » (le titre le plus proche au-dessus d'elle) ouvre la vue Document centrée sur ce bloc.
5. Pour un contributeur, le détail d'une exigence d'un autre système s'ouvre en lecture seule (DEC-100, voir [US-ALM-32](05-allocation.md#us-alm-32--lire-en-lecture-seule-une-exigence-dun-autre-système)).

### US-DOCV-04 — Voir la nature de chaque bloc et le doute de l'IA
**Carte :** En tant que chef de projet, je veux voir sur chaque bloc s'il est titre, information ou exigence, et quand l'IA n'en est pas sûre, afin de repérer vite les erreurs de lecture.
**Conversation :** La nature vaut « Heading », « Information » ou « Requirement », rien d'autre (DEC-074) ; elle n'a pas de colonne dans la table et se lit ici, sur une puce, ou dans le détail. Quand l'IA a proposé la nature sans en être sûre, la puce est en pointillés et son infobulle donne le niveau de confiance (DEC-120, [US-ALM-05](05-allocation.md#us-alm-05--voir-le-niveau-de-confiance-de-lia-sur-la-nature-et-la-classe)). Titres et informations n'ayant pas de statut, c'est là que leur doute se voit (DEC-073).
**Maquette :** Allocation, mode « Document » — `revue-documentaire.html` (route `#review`), Nature Picker sur Document Block.
**Règles :** DEC-073, DEC-074, DEC-120, ALLOC-018, ALLOC-T26 · **Périmètre :** Pilote 1 · **Variantes :** Toutes
**Critères d'acceptation :**
1. Chaque titre, information et exigence porte une puce de nature (« Heading ▾ », « Information ▾ » ou « Requirement ▾ »).
2. Une nature proposée par l'IA et pas encore confirmée a une puce en pointillés, dont l'infobulle donne le niveau (Low, Medium ou High) et invite à la confirmer ou à la changer.
3. Une nature choisie ou confirmée par une personne a une puce pleine, sans niveau.
4. Aucune puce ni étiquette du document ne montre Functional, Performance, Security, Interface ou Regulatory (DEC-074).
Écart maquette : dans un tableau du document, l'étiquette d'une ligne affiche encore l'ancien type (« Interface · … ») au lieu de « Requirement ».

### US-DOCV-05 — Reclasser ou confirmer un bloc sur place
**Carte :** En tant que chef de projet, je veux changer la nature d'un bloc, ou confirmer celle de l'IA, directement dans le document, afin de corriger la lecture là où je la vois.
**Conversation :** Seul le chef de projet change la nature (DEC-086, ACC-012, [US-ALM-06](05-allocation.md#us-alm-06--réserver-la-nature-et-la-classe-au-chef-de-projet)) ; pour un contributeur, la puce est inactive. Choisir la nature déjà en place confirme celle de l'IA (DEC-073). Un bloc capturé par erreur se reclasse en Information au lieu d'être supprimé (DEC-094). Ce qu'entraîne un reclassement — allocation effacée vers Information, Incomplete vers Requirement, proposition de relancer le modèle — est décrit dans [US-ALM-04](05-allocation.md#us-alm-04--corriger-la-nature-et-la-classe-dune-exigence) et [US-ALM-25](05-allocation.md#us-alm-25--relancer-après-un-changement-de-nature-ou-de-classe).
**Maquette :** Allocation, mode « Document » — `revue-documentaire.html` (route `#review`), Nature Picker (menu de reclassement).
**Règles :** DEC-086, ACC-012, DEC-073, DEC-074, DEC-094, PLAT-002 · **Périmètre :** Pilote 1 · **Variantes :** Toutes
**Critères d'acceptation :**
1. Cliquer la puce ouvre un menu des trois natures, l'actuelle marquée ; en choisir une autre reclasse le bloc aussitôt et l'annonce (« <ID> reclassified as <nature> »).
2. Choisir la nature déjà en place sur une puce en pointillés la confirme : la puce devient pleine et un message le dit (« <ID> — nature confirmed: <nature> »).
3. Sur une figure, seul « Information » est proposé.
4. Pour un contributeur, la puce est inactive avec l'infobulle « Set by the project manager », et le serveur refuse un reclassement tenté par un autre chemin.
5. Le nouveau classement se voit aussitôt dans le document, le plan, la table et le panneau.

### US-DOCV-06 — Comparer un document à une version antérieure (onglet Changes)
**Carte :** En tant que chef de projet, je veux choisir un document et une version antérieure pour voir, dans le document lui-même, tout ce que la version en vigueur a changé, afin de relire une nouvelle version en entier.
**Conversation :** Il n'y a plus de mode Compare (DEC-119) : la revue complète d'une nouvelle version se fait dans la vue Document, dont le navigateur a deux onglets, « Outline » et « Changes ». Les versions appartiennent aux documents : on compare un document à la fois, une version antérieure contre celle en vigueur (DEC-069, DEC-070). Le document montre chaque changement à sa place : mots supprimés barrés, mots ajoutés surlignés, exigences supprimées là où elles étaient (LIFE-006). Le panneau de droite reste celui de l'exigence sélectionnée.
**Maquette :** Allocation, mode « Document » — `revue-documentaire.html` (route `#review`), Changes Navigator (onglet « Changes » du Left Navigator Panel), Document Reading View, Word Diff.
**Règles :** DEC-119, DEC-069, DEC-070, DEC-017, LIFE-012, LIFE-013, LIFE-006, LIFE-T11 · **Périmètre :** Après pilote · **Variantes :** Toutes
**Critères d'acceptation :**
1. L'onglet « Changes » n'apparaît à côté de « Outline » que si au moins un document a plusieurs versions ; navigateur replié, son rail affiche le nombre de changements et rouvre cet onglet.
2. L'onglet propose les documents du tender ; un document à une seule version est grisé (« · one version »).
3. Pour le document choisi, l'onglet propose ses versions antérieures, avec leur date, à comparer avec « vX · in force » ; par défaut, la précédente.
4. Le document n'affiche que ce document, titré « vA → vB » : chaque exigence modifiée en mots barrés et surlignés, chaque ajout marqué « Added in vX », chaque exigence supprimée à sa place (« Removed in vX — … »).
5. Chaque section annonce ses changements (« +a · ~m · -r changes in this section »).
6. Un document à une seule version le dit (« Only one version of this document — nothing to compare yet. »), une plage sans changement aussi (« No change between vA and vB in this document. »), sans jamais afficher de comparaison vide.
Écart maquette : les versions et leurs changements sont des données propres à Allocation ; une version téléversée dans Documents n'y arrive pas.

### US-DOCV-07 — Lire chaque changement et son effet sur le travail déjà fait
**Carte :** En tant que chef de projet, je veux savoir, pour chaque changement, ce qu'il fait au travail déjà fait sur l'exigence, afin de traiter d'abord ce qui rouvre une réponse.
**Conversation :** L'onglet liste chaque changement du document et de la plage choisis, avec son effet : réponse rouverte, allocation à faire, travail archivé (DEC-119). Une exigence modifiée repasse To review ([US-CHG-01](08-changements.md#us-chg-01--revoir-une-exigence-ajoutée-ou-modifiée-par-une-nouvelle-version)) et ses verdicts sont rouverts dans Compliance (DEC-122, [US-CMP-27](09-compliance.md#us-cmp-27--rouvrir-les-verdicts-dune-exigence-modifiée-par-une-nouvelle-version)). Le panneau de droite montre l'exigence sur son onglet « Versions » ([US-CHG-05](08-changements.md#us-chg-05--consulter-longlet-versions-dune-exigence-changée)).
**Maquette :** Allocation, mode « Document » — `revue-documentaire.html` (route `#review`), Changes Navigator (Compare Summary Chip, Change List Card).
**Règles :** DEC-119, DEC-122, LIFE-013, LIFE-015, LIFE-006 · **Périmètre :** Après pilote · **Variantes :** Toutes
**Critères d'acceptation :**
1. L'onglet compte les changements par type (« +N added », « ~N modified », « −N removed »).
2. Chaque changement a sa carte : type, identifiant, « § » de son paragraphe, ce qui a changé, et son effet.
3. L'effet affiché est l'un de : « ↺ Was answered — back to To review » (mis en avant), « Awaiting its answer — the contributor answers the new text », « Back to To review », « New — needs allocation », « New — allocated since », « Removed — its work stays archived with vA ».
4. Cliquer une carte sélectionne l'exigence, fait défiler le document jusqu'à elle et ouvre son détail sur l'onglet « Versions ».
5. Cliquer un changement dans le document en fait le changement courant de la liste.
6. Une exigence supprimée s'ouvre dans un panneau en lecture seule ([US-CHG-06](08-changements.md#us-chg-06--consulter-une-exigence-supprimée-par-une-nouvelle-version)).

### US-DOCV-08 — Filtrer les changements et les parcourir au clavier
**Carte :** En tant que chef de projet, je veux ne garder qu'un type de changement, ou ceux qui rouvrent une réponse, et passer de l'un à l'autre au clavier, afin de traiter une réédition de plusieurs centaines de changements.
**Conversation :** Une réédition peut apporter des centaines de changements (DEC-119 : plus de 400 sur un document de 1 000 exigences). Les comptes par type et la ligne des réponses rouvertes filtrent la liste et ce que parcourent ] et [. Le parcours tourne en boucle.
**Maquette :** Allocation, mode « Document » — `revue-documentaire.html` (route `#review`), Changes Navigator (« Change k of n », ‹ ›).
**Règles :** DEC-119, DEC-023, LIFE-013 · **Périmètre :** Après pilote · **Variantes :** Toutes
**Critères d'acceptation :**
1. Cliquer un compte par type ne garde que ce type dans la liste ; le recliquer rend toute la liste.
2. Quand des changements rouvrent une réponse déjà donnée, « ↺ N changes reopen answers already given » les isole d'un clic.
3. « Change k of n » situe le changement courant ; ‹ et ›, ou [ et ] au clavier, passent au précédent ou au suivant dans la liste filtrée, en boucle.
4. Sous un filtre, « show all N » rend tous les changements ; un filtre qui ne garde plus rien est levé de lui-même.
5. La liste garde sa position quand elle se met à jour et ramène la carte courante en vue.
Point ouvert : temps de réponse attendu sur un document de plusieurs milliers d'exigences (OPEN-08).

### US-DOCV-09 — Lire le document sur le PDF original
**Carte :** En tant que chef de projet, je veux voir le PDF du client tel quel, avec les blocs capturés dessinés par-dessus, afin de vérifier d'un coup d'œil que l'outil a bien lu et découpé le texte.
**Conversation :** SPEC-document-view décrit un prototype séparé, non construit : les pages du PDF rendues intactes, chaque bloc dessiné en cadre sur le vrai texte avec sa nature, et le texte lu affiché sous le cadre sélectionné. La confiance vient de là : on compare la capture à la source, pas à une recomposition faite par l'outil. Hors périmètre : statuts, allocation, découpe à la main, comparaison de versions (qui garderait une forme texte, à concevoir). Dans le produit, le reclassement resterait réservé au chef de projet (DEC-086).
**Maquette :** non maquetté (spec `docs/specs/SPEC-document-view.md`, prototype autonome non construit).
**Règles :** SPEC-document-view (DV-T01, DV-T02, DV-T03, DV-T04, DV-T09, DV-T10, DV-T11, DV-T12), DEC-074, DEC-086 · **Périmètre :** Après pilote · **Variantes :** Toutes
**Critères d'acceptation :**
1. Chaque page s'affiche comme dans un lecteur PDF — mise en page, polices, tableaux, figures — sans rien recomposer.
2. Chaque cadre couvre exactement le texte de son bloc, à tout zoom de 50 % à 300 % ; un paragraphe coupé par un saut de page a deux cadres qui s'allument ensemble.
3. Les en-têtes, pieds et numéros de page répétés ne donnent aucun bloc et s'affichent en zones hachurées (« Ignored — running header »…).
4. Sélectionner un bloc ouvre sous son cadre le texte capturé ; Échap le referme.
5. Reclasser un bloc change son cadre aussitôt, avec « Undo » ; aucun contrôle ne permet de couper, fusionner ou redimensionner un bloc.
6. Une page scannée, sans texte, s'affiche avec le bandeau « No text on this page — it needs OCR, nothing was captured here. » et sans cadre.
Point ouvert : remplacerait la vue Document si l'essai convainc (SPEC-document-view §13.4) ; la forme de la comparaison de versions serait alors à concevoir.

## Couverture
- Règles couvertes : LIFE-006 → [US-DOCV-06](#us-docv-06--comparer-un-document-à-une-version-antérieure-onglet-changes), [US-DOCV-07](#us-docv-07--lire-chaque-changement-et-son-effet-sur-le-travail-déjà-fait) (et [US-CHG-06](08-changements.md#us-chg-06--consulter-une-exigence-supprimée-par-une-nouvelle-version)) ; LIFE-012 → [US-DOCV-06](#us-docv-06--comparer-un-document-à-une-version-antérieure-onglet-changes) ; LIFE-013 → [US-DOCV-06](#us-docv-06--comparer-un-document-à-une-version-antérieure-onglet-changes), [US-DOCV-07](#us-docv-07--lire-chaque-changement-et-son-effet-sur-le-travail-déjà-fait), [US-DOCV-08](#us-docv-08--filtrer-les-changements-et-les-parcourir-au-clavier) ; LIFE-T11 → [US-DOCV-06](#us-docv-06--comparer-un-document-à-une-version-antérieure-onglet-changes) ; JRN-002 (lecture du document) → [US-DOCV-01](#us-docv-01--lire-le-tender-sous-forme-de-document), [US-DOCV-02](#us-docv-02--naviguer-dans-le-plan-du-tender), [US-DOCV-03](#us-docv-03--ouvrir-le-détail-dun-bloc-depuis-le-document).
- Non couvertes, avec la raison : LIFE-014, LIFE-015, LIFE-016, LIFE-T10, LIFE-T12, LIFE-T13, LIFE-T14 — couvertes par l'épopée US-CHG ; la découpe des blocs (scission, fusion, granularité des tableaux) — couverte par l'épopée US-CAP ; les effets d'un reclassement sur l'allocation — couverts par l'épopée US-ALM ([US-ALM-04](05-allocation.md#us-alm-04--corriger-la-nature-et-la-classe-dune-exigence)).
