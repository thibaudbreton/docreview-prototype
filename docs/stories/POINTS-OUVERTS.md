# Points ouverts et écarts de la maquette

Tout ce que les stories ne tranchent pas, et tout ce que la maquette fait autrement que la cible. Les stories décrivent la cible ; ces listes servent à arbitrer et à planifier.

## Incohérences dans la documentation de référence

Lignes de `docs/current/` ou de décisions qui se contredisent ; la décision la plus récente prime, ces lignes sont à réaligner.

- **Conformité** : `COMPLIANCE.md` (CONF-003, CONF-005, CONF-006, CONF-014 à CONF-017, CONF-T05, CONF-T06, CONF-T09, CONF-T11, CONF-T13, CONF-T17) et `DOMAIN.md` (DOM-009) décrivent encore trois verdicts, le verrou du verdict final ou la déclaration externe — remplacés par DEC-031 et DEC-106. CONF-T15 est utilisé deux fois, pour deux critères différents.
- **Grain de la conformité externe** : DEC-106 et CONF-029 disent « par système », alors que DEC-055, DEC-060 et DEC-087 portent le verdict par organisation (OBS).
- **Allocation** : ALLOC-017 décrit encore un bouton « Confirm » (retiré par DEC-099) ; ALLOC-T30 décrit deux gestes de validation (DEC-099 : un seul) ; ALLOC-012 réserve la validation à l'équipe de gestion (DEC-104 : un contributeur valide son système) ; ALLOC-014 et ALLOC-T23 placent le contrôle de relance sur les cartes système Turnkey, d'où la maquette l'a retiré à la demande de l'utilisateur.
- **Validation Turnkey** : DEC-104 dit que le chef de projet ne voit pas le statut des systèmes sur la vue Turnkey, mais les cartes système l'affichent ; l'ordre entre validation de l'aiguillage et validation d'un système (DEC-099 contre DEC-104) n'est pas dit.
- **Raccourci N du chef de projet dans Compliance** : DEC-085 vise « un Not compliant sans déclaration », notion remplacée par DEC-106 et DEC-108.
- **Set aside** : DEC-079 (« ni filtre ni vue ») contre DEC-081 (une pastille de filtre) — DEC-081 s'applique.
- **Q&A** : QA-010, DEC-088 (« fusionne… lot »), JRN-006 (« lot… arbitre ») et QA-T05 (« arbitrage ») précèdent DEC-116 ; QA-006 et QA-T03 parlent encore de « débloquer » (rien n'est bloqué depuis DEC-092).
- **Versions** : LIFE-007 parle de « déverrouiller » (plus de verrou) ; JRN-003 cite un « détail Document » retiré ; JRN-005 parle de « comparaison » et de « suppression manuelle » (DEC-119, DEC-094) ; `LIFECYCLE.md` a deux critères numérotés LIFE-T10 ; LANG-005 précède DEC-096.
- **Colonnes personnalisées** : `CUSTOM-COLUMNS.md` (CUST-T01, CUST-T11, « créée deux fois », paragraphe export) contredit DEC-097 et CUST-T12.
- **Statistiques** : PLAT-008 compte les réallocations « par demandeur » (une mesure de personne, contraire à DEC-118), parle de retard « au-delà de 5 jours » et « âge ≥ 5 jours », et range « On the client » avant « On a contributor » alors que DEC-092 et DEC-125 font passer ce que doit le contributeur en premier.
- **« Sous-système »** : DEC-118 appelle ainsi les périmètres staffés, DEC-046 et DEC-058 les codes vers lesquels un Turnkey répartit.
- **Équipe de gestion** : l'assistant de création dit du créateur « Never removed », le casting permet de le retirer s'il reste un autre chef de projet ; ACC-001 ne dit rien.
- **Assistant et paramètres** : « The AI never overwrites a manual correction » et le réglage « Never overwrite manual edits » contredisent les relances qui écrasent les dérivations (ALLOC-015, DEC-027) et DOM-013.

## Points ouverts, par story

### Accueil (My tenders)

- [US-HOME-01](01-accueil.md#us-home-01--être-accueilli-et-orienté-dès-larrivée) — pas de règle écrite, comportement tiré de la maquette.
- [US-HOME-01](01-accueil.md#us-home-01--être-accueilli-et-orienté-dès-larrivée) — qui a le droit de créer un tender n'est pas fixé (JRN-001, « politique globale à préciser ») ; l'affichage de « ＋ New tender » à tous ne doit pas être lu comme une décision.
- [US-HOME-02](01-accueil.md#us-home-02--reprendre-le-tender-en-cours) — pas de règle écrite, comportement tiré de la maquette ; la règle de choix du tender à reprendre (le dernier ouvert par la personne ?) n'est pas décidée. Le compte « still to answer in Compliance » relève de l'après-pilote (DEC-022).
- [US-HOME-03](01-accueil.md#us-home-03--comprendre-comment-un-tender-traverse-srm) — pas de règle écrite, comportement tiré de la maquette ; la conservation de l'état masqué comme préférence personnelle est une déduction.
- [US-HOME-04](01-accueil.md#us-home-04--voir-la-liste-de-mes-tenders) — pas de règle écrite pour la carte, comportement tiré de la maquette ; ce qui fait passer un tender à « Submitted » n'est décrit nulle part.
- [US-HOME-05](01-accueil.md#us-home-05--lire-lavancement-dun-tender-sur-sa-ligne) — pas de règle écrite, comportement tiré de la maquette ; le passage à Submission n'est pas spécifié ; le compteur Compliance relève de l'après-pilote (DEC-022).
- [US-HOME-06](01-accueil.md#us-home-06--ouvrir-un-tender-depuis-laccueil) — ouverture d'un tender en traitement depuis l'accueil (« Still processing — it will open when the models finish » dans la maquette) — reprise non décidée (JRN-001 → OPEN-05).

### Création d'un tender

- [US-NEW-01](02-creation.md#us-new-01--décrire-lidentité-du-tender) — la liste réelle des régions n'est pas fournie (acronymes provisoires) ; l'unicité du BO-ID n'est décidée nulle part ; qui peut créer un tender n'est pas fixé (JRN-001, « politique globale à préciser »).
- [US-NEW-02](02-creation.md#us-new-02--choisir-la-ligne-produit-fixée-à-la-création) — « Services » ne fait pas partie des types de DEC-004 — à garder ou retirer, non tranché. L'orthographe RSC (DEC-059) est une déduction à confirmer et le rapport RSC / RST reste ouvert ; les particularités de RSC ne sont pas fournies (OPEN-15).
- [US-NEW-03](02-creation.md#us-new-03--choisir-le-produit-ou-la-combinaison-dun-turnkey) — la matrice des combinaisons Turnkey (DEC-048) et les produits de RSC (DEC-047) sont à fournir ; la maille de l'OBS du modèle Urban n'est pas tranchée.
- [US-NEW-04](02-creation.md#us-new-04--déclarer-la-langue-source-unique-du-tender) — la liste des langues proposées n'est pas décidée (la maquette offre English, French, German, Spanish) ; un changement de langue source après création n'est pas décidé.
- [US-NEW-05](02-creation.md#us-new-05--joindre-et-ordonner-les-documents-source) — la liste exacte des formats et contrats d'import (DOORS, Excel) et le cas d'un PDF fait uniquement d'images sont à préciser avec l'équipe technique (OPEN-10, OPEN-12) ; aucune limite de taille n'est décidée.
- [US-NEW-06](02-creation.md#us-new-06--choisir-le-mode-dassistance-ia-fixé-à-la-création) — DEC-095 fige « le mode d'assistance IA » sans dire si les réglages par étape en font partie. En mode tout manuel, la manière de créer les exigences à la main n'est pas spécifiée (« Edit segmentation » est masqué dans la maquette). L'estimation de durée affichée n'a pas de règle.
- [US-NEW-09](02-creation.md#us-new-09--retrouver-dans-le-tender-créé-tout-ce-que-lassistant-a-fixé) — la possibilité de modifier les autres réglages de traitement après le démarrage n'est pas décidée (LIFE-002, OPEN-05 résiduel).

### Documents et versions

- [US-DOC-02](03-documents.md#us-doc-02--consulter-lhistorique-des-versions-dun-document) — la règle de numérotation des versions (automatique, alias, saisie libre) n'est pas décidée.
- [US-DOC-04](03-documents.md#us-doc-04--téléverser-une-nouvelle-version-dun-document) — la manière de reconnaître qu'une exigence est la même, modifiée, fusionnée ou scindée d'une version à l'autre n'est pas spécifiée (OPEN-07, DOM-012) ; les réglages « Re-segmentation on new version », « Detect addendum-as-answer » et « Numbering » n'ont pas de règle ; le sort de la stratégie d'écart et des risques d'un verdict rouvert n'est pas décidé.
- [US-DOC-05](03-documents.md#us-doc-05--retirer-un-document-en-annonçant-ce-qui-sera-perdu) — la conservation ou la récupération d'un document retiré n'est pas décidée (LIFE-006, OPEN-07) ; la maquette annonce « This cannot be undone ».
- [US-DOC-06](03-documents.md#us-doc-06--ajouter-un-document-en-cours-de-tender) — l'état d'échec et la reprise d'un traitement interrompu sont traités par US-CAP-11.
- [US-DOC-07](03-documents.md#us-doc-07--exporter-les-exigences-dun-seul-document) — formats, correspondances de champs et aller-retour DOORS sont à contractualiser (OPEN-10, OPEN-12) ; la langue du texte d'exigence dans cet export n'est pas décidée (LANG-003 vise l'export client) ; le droit d'un contributeur à lancer cet export n'est pas tranché (LIFE-004 réserve la gestion à l'équipe projet, DEC-012 lui ouvre la lecture de tout le tender).

### Capture, segmentation, traduction et IA

- [US-CAP-02](04-capture-ia.md#us-cap-02--régler-la-conversion-du-document-source) — la liste des réglages est peut-être incomplète. Leur moment n'est pas décidé : figés à la création comme le produit, ou modifiables après capture avec un avertissement chiffré et une nouvelle capture — or la capture démarre dès la création, alors que ces réglages ne sont proposés que dans les paramètres. La granularité doit-elle être désactivée quand le format est « Image » ? Le libellé « Split » est à confirmer, et l'essai SPEC-document-view découpe par phrase par défaut. Le droit de modifier les paramètres n'est pas fixé (JRN-007, OPEN-05).
- [US-CAP-03](04-capture-ia.md#us-cap-03--découper-chaque-document-en-blocs-heading-information-ou-requirement) — la correspondance des identifiants d'une version à l'autre en cas de fusion ou de scission n'est pas spécifiée (OPEN-07, DOM-012) ; la correction de la découpe à la main n'est pas décidée (voir US-CAP-05).
- [US-CAP-04](04-capture-ia.md#us-cap-04--capturer-les-images-sans-en-lire-le-contenu) — le texte de travail d'une ligne issue d'une image (vide, légende, saisie) et le droit d'un contributeur à dupliquer une ligne ne sont pas spécifiés ; un PDF fait uniquement d'images est une limite d'ingestion à préciser avec l'équipe technique (OPEN-10).
- [US-CAP-05](04-capture-ia.md#us-cap-05--signaler-une-découpe-incertaine) — la définition du drapeau n'est pas tranchée — seuil de confiance réglable (80 % par défaut dans la maquette) ou règles textuelles de l'essai SPEC-document-view (deux obligations dans des phrases différentes, exigence visiblement coupée) ; ce qui retire le drapeau n'est pas spécifié ; la correction manuelle de la découpe n'est pas décidée.
- [US-CAP-06](04-capture-ia.md#us-cap-06--écarter-un-bloc-capturé-par-erreur-sans-le-supprimer) — la suppression et la restauration au niveau documentaire restent non confirmées (LIFE-006) ; elles sont distinctes de ce cas.
- [US-CAP-07](04-capture-ia.md#us-cap-07--traduire-automatiquement-vers-langlais-de-travail) — la langue affichée par défaut dans les panneaux n'est pas décidée (Allocation met l'original en tête, Compliance l'anglais) ; la lecture dans une langue tierce n'est pas redemandée par les règles actuelles ; la langue de l'export client relève d'US-CMP (LANG-003).
- [US-CAP-08](04-capture-ia.md#us-cap-08--corriger-une-traduction-ce-qui-remet-lexigence-en-revue) — l'effet d'une correction sur une exigence déjà répondue (simple « To review », ou verdicts rouverts comme pour une version) n'est pas décidé ; le droit d'un contributeur à corriger la traduction d'une exigence de son système n'est pas écrit (DEC-100 lui interdit seulement toute modification hors de son système) ; la correction du texte de travail d'un tender en anglais n'est proposée nulle part, alors que LIFE-008 vise « toute correction du texte ou de la traduction ».
- [US-CAP-09](04-capture-ia.md#us-cap-09--caractériser-chaque-bloc-avec-un-niveau-de-confiance-low-medium-ou-high) — la calibration des niveaux relève du chantier IA (DEC-020) ; la nature des blocs quand la caractérisation est désactivée (qui décide alors qu'un bloc est un titre, une information ou une exigence ?) n'est pas décrite.
- [US-CAP-10](04-capture-ia.md#us-cap-10--dire-quaucun-modèle-ne-sapplique-sans-en-emprunter-un-en-silence) — les particularités de configuration de RSC et de Mainline ne sont pas fournies (OPEN-15), ni les produits de RSC (DEC-047).
- [US-CAP-11](04-capture-ia.md#us-cap-11--reprendre-un-traitement-interrompu-sans-doublon) — AI-012 est une proposition à valider ; qui reprend le traitement, si la reprise est automatique et ce que l'on garde d'un résultat partiel ne sont pas décidés (DOM-013 renvoie à OPEN-07 et OPEN-09).
- [US-CAP-12](04-capture-ia.md#us-cap-12--relancer-automatiquement-les-modèles-sur-les-seules-exigences-modifiées-par-une-nouvelle-version) — ce que la relance fait de la personne déjà affectée à une organisation n'est pas écrit ; la détection d'une exigence « modifiée » dépend d'OPEN-07.
- [US-CAP-13](04-capture-ia.md#us-cap-13--repartir-de-zéro-sur-une-exigence-issue-dune-fusion-ou-dune-scission) — la manière de reconnaître une fusion ou une scission et de relier les identifiants d'une version à l'autre n'est pas spécifiée (OPEN-07, DOM-012) ; une fusion ou une scission faite à la main par un utilisateur n'est pas décidée.

### Allocation — modèle et panneau

- [US-ALM-01](05-allocation.md#us-alm-01--lire-le-statut-dune-exigence) — libellés exacts des états à harmoniser entre écrans (OPEN-13) ; allocation partiellement remplie : voir US-ALM-14.
- [US-ALM-02](05-allocation.md#us-alm-02--savoir-pourquoi-une-exigence-est-à-revoir) — le seuil de 75 % est celui de la maquette ; sa calibration relève du chantier IA (AI.md).
- [US-ALM-03](05-allocation.md#us-alm-03--suivre-lavancement-dans-la-barre-de-statut) — sur un Turnkey, « allocated » veut-il dire aiguillage validé (statut du niveau Turnkey, DEC-104) ou tous les systèmes validés (carte du tableau de bord, DEC-098) ? La maquette compte le premier dans la barre et transmet le second au tableau de bord, alors que l'infobulle de la barre annonce le second.
- [US-ALM-08](05-allocation.md#us-alm-08--ajouter-ou-retirer-un-système) — faut-il dériver automatiquement l'allocation d'un système à modèle ajouté à la main ? Non dit ; la maquette l'ajoute vide (une relance peut la dériver, US-ALM-21).
- [US-ALM-11](05-allocation.md#us-alm-11--suivre-une-exigence-répartie-sur-plusieurs-systèmes) — DEC-104 dit que le chef de projet ne voit pas le statut des systèmes sur la vue Turnkey, mais chaque carte de « Systems (N) » l'affiche en coin — à préciser.
- [US-ALM-12](05-allocation.md#us-alm-12--travailler-dans-le-détail-dun-système-dun-turnkey) — DEC-101 met les boutons de réallocation dans ce détail, y compris pour le chef de projet, qui peut déjà ajouter ou retirer un système lui-même : l'usage d'une demande qu'il s'adresserait n'est pas précisé.
- [US-ALM-13](05-allocation.md#us-alm-13--allouer-sur-un-tender-sig-autonome-sans-axe-système) — configuration et écrans propres aux tenders RSC (et à Mainline au-delà des clés) non fournis — ne pas les déduire de SIG (OPEN-15).
- [US-ALM-14](05-allocation.md#us-alm-14--corriger-la-chaîne-abs--pbs--obs) — faut-il aussi un ABS et un PBS pour sortir d'« Incomplete » ? ALLOC-T32 le suggère sans le dire. Effet d'une correction de la chaîne sur une exigence déjà « Allocated » : la maquette la laisse « Allocated » ; ALLOC-003 renvoie à LIFE-008 sans dire si le statut change.
- [US-ALM-15](05-allocation.md#us-alm-15--gérer-les-organisations-obs-dun-système) — liste proposée hors clés — DEC-036 fait des OBS · team et des périmètres du casting une même liste fermée, alors que la maquette propose les organisations déjà utilisées et un nom libre (« Add “…” »). DEC-087 (plusieurs personnes d'un même périmètre = plusieurs entrées OBS) face à une maquette qui refuse la même organisation deux fois sur un système : traduction exacte à préciser.
- [US-ALM-17](05-allocation.md#us-alm-17--alimenter-les-listes-depuis-le-classeur-de-clés-de-référence) — qui charge ou remplace le classeur, et ce que deviennent les dérivations existantes quand une valeur disparaît d'une nouvelle version (rôle Admin non détaillé, OPEN-02) ; modèles Urban et RSC sans clés réelles.
- [US-ALM-18](05-allocation.md#us-alm-18--désigner-la-personne-de-chaque-organisation) — une exigence sans système n'a pas d'organisation ; la maquette y garde une recherche dans l'annuaire au niveau de l'exigence, que DEC-087 et DEC-102 ne prévoient pas.
- [US-ALM-20](05-allocation.md#us-alm-20--allouer-à-la-main-un-système-sans-modèle) — quels systèmes ont un modèle — SIG et RSC selon une déduction à confirmer (DEC-058) ; RST est marqué « avec modèle » dans la maquette par hypothèse (DEC-059).
- [US-ALM-21](05-allocation.md#us-alm-21--relancer-le-modèle-dallocation-sur-une-exigence) — emplacement du contrôle pour le chef de projet sur un Turnkey — ALLOC-014 et ALLOC-T23 le veulent sur chaque carte système, la maquette ne l'a que dans le détail du système (retiré des cartes le 23 sept. à la demande de l'utilisateur) : à arbitrer. Statut après une relance (recalcul selon les nouvelles certitudes, retour d'une exigence « Allocated ») : la maquette ne touche pas au statut. Un modèle peut-il ajouter ou retirer une organisation à la relance : non tranché (la maquette garde leur nombre).
- [US-ALM-24](05-allocation.md#us-alm-24--relancer-le-modèle-sur-une-sélection-dexigences) — exigence à plusieurs systèmes dans une relance groupée — la maquette les écarte et les compte (« re-run those from the panel »), aucune décision ne le dit.
- [US-ALM-27](05-allocation.md#us-alm-27--valider-laiguillage-dune-exigence-turnkey) — DEC-099 dit que valider un système valide aussi la caractérisation, DEC-104 sépare les deux niveaux ; la maquette laisse valider un système avant l'aiguillage sans valider la caractérisation — ordre et dépendance à confirmer.
- [US-ALM-29](05-allocation.md#us-alm-29--demander-une-réallocation) — sur un tender SIG autonome, « Wrong system » et « This system doesn't apply here » n'ont pas de système de remplacement possible ; la maquette les propose — les cas hors système en autonome restent à expliciter (ALLOCATION.md, OPEN-15).
- [US-ALM-35](05-allocation.md#us-alm-35--inscrire-les-actions-dallocation-au-journal-de-lexigence) — contenu exact, rétention et droits de lecture du journal non spécifiés (OPEN-11, PLAT-003).

### Tables communes Allocation et Compliance

- [US-TAB-04](06-tables.md#us-tab-04--rechercher-une-exigence-par-son-identifiant-ou-son-texte) — temps de réponse attendu à 100 000 lignes (OPEN-08, PLAT-007).
- [US-TAB-06](06-tables.md#us-tab-06--filtrer-une-colonne-comme-dans-excel) — temps de réponse attendu à 100 000 lignes et comportement d'une table servie par pages (OPEN-08, OPEN-13).
- [US-TAB-09](06-tables.md#us-tab-09--enregistrer-un-filtre-et-le-réutiliser-sur-un-autre-tender) — condition portant sur un champ absent du tender ouvert (UX-004, OPEN-13).
- [US-TAB-11](06-tables.md#us-tab-11--choisir-masquer-et-réordonner-les-colonnes) — rien ne dit si l'affichage et l'ordre des colonnes sont retenus d'une visite à l'autre, ni pour qui ; seul l'affichage d'une colonne personnalisée est retenu par écran (DEC-097).
- [US-TAB-12](06-tables.md#us-tab-12--redimensionner-les-colonnes) — largeurs propres à chaque personne ou communes au tender — non décidé.
- [US-TAB-13](06-tables.md#us-tab-13--sélectionner-plusieurs-lignes-et-agir-en-une-fois) — sélectionner tout ce que montrent les filtres quand la table est servie par pages, à 100 000 lignes (UX-006, OPEN-13).
- [US-TAB-14](06-tables.md#us-tab-14--ne-montrer-que-les-lignes-sélectionnées) — composition avec le filtre avancé et la sélection de toutes les pages (UX-006, OPEN-13).
- [US-TAB-17](06-tables.md#us-tab-17--aller-à-la-prochaine-exigence-qui-mattend-et-valider-au-clavier) — « un Not compliant sans déclaration » (DEC-085) date d'avant la conformité externe dérivée (DEC-106) et les manques signalés (DEC-108) ; la maquette arrête N, pour le contributeur, sur ses Not compliant sans stratégie ou sans risque — à confirmer.
- [US-TAB-18](06-tables.md#us-tab-18--annuler-la-dernière-action-même-après-le-message) — portée de l'annulation côté serveur — après un rechargement, ou quand une autre personne a modifié la même exigence entre-temps (DEC-085 décrit le geste, pas sa portée).
- [US-TAB-21](06-tables.md#us-tab-21--remplir-une-colonne-personnalisée) — la survie des valeurs à une nouvelle version est un défaut « à confirmer » (DEC-068).
- [US-TAB-22](06-tables.md#us-tab-22--retrouver-une-colonne-personnalisée-sur-lautre-écran) — le choix d'affichage vaut-il pour chaque personne ou pour tout le tender ? La maquette le garde sur la colonne, donc pour tous.
- [US-TAB-24](06-tables.md#us-tab-24--modifier-une-colonne-personnalisée) — renommer une option existante n'est ni fait ni décidé ; le verrou du type est un défaut « à confirmer » (DEC-068).
- [US-TAB-26](06-tables.md#us-tab-26--garder-les-colonnes-personnalisées-hors-de-lexport-client) — le défaut « hors export client » est à confirmer (DEC-068) ; ce qui distingue un export client d'un export interne n'est pas spécifié (voir US-CMP-28).

### Vue Document d'Allocation

- [US-DOCV-08](07-vue-document.md#us-docv-08--filtrer-les-changements-et-les-parcourir-au-clavier) — temps de réponse attendu sur un document de plusieurs milliers d'exigences (OPEN-08).
- [US-DOCV-09](07-vue-document.md#us-docv-09--lire-le-document-sur-le-pdf-original) — remplacerait la vue Document si l'essai convainc (SPEC-document-view §13.4) ; la forme de la comparaison de versions serait alors à concevoir.

### Changements de version côté Allocation

- [US-CHG-01](08-changements.md#us-chg-01--revoir-une-exigence-ajoutée-ou-modifiée-par-une-nouvelle-version) — la façon de reconnaître une même exigence d'une version à l'autre (modifiée, fusionnée, scindée) n'est pas spécifiée (OPEN-07, DOM-012).
- [US-CHG-06](08-changements.md#us-chg-06--consulter-une-exigence-supprimée-par-une-nouvelle-version) — où et comment consulter l'historique d'une exigence supprimée n'est pas spécifié (LIFE-006, OPEN-07).

### Compliance

- [US-CMP-01](09-compliance.md#us-cmp-01--créer-les-affectations-quand-lallocation-est-validée) — un contributeur peut-il déjà répondre à une affectation « Proposed » ? La maquette le permet, aucune règle ne le dit (docs/gap SPECS, « Statuts d'une affectation », Toujours ouvert).
- [US-CMP-02](09-compliance.md#us-cmp-02--suivre-lavancement-dune-affectation-par-son-statut) — le statut « Assigned » existe dans le vocabulaire mais aucun flux ne le produit ; le garder ou le retirer n'est pas décidé (docs/gap SPECS, « Statuts d'une affectation », Toujours ouvert).
- [US-CMP-12](09-compliance.md#us-cmp-12--qualifier-un-not-compliant-par-category-et-topic-sur-un-tender-turnkey) — la liste réelle des catégories de non-conformité est à fournir par le métier avant la mise en production de Compliance (OPEN-04, DEC-038).
- [US-CMP-15](09-compliance.md#us-cmp-15--consulter-les-questions-et-les-exigences-similaires) — la capacité de similarité de la plateforme — source, classement, nombre d'exigences montrées — reste à spécifier (DEC-079, SPEC-compliance-decision-panel §8).
- [US-CMP-16](09-compliance.md#us-cmp-16--poser-une-question-au-client-depuis-une-affectation) — le chef de projet pose-t-il aussi des questions depuis Compliance ? La maquette ne lui donne qu'un raccourci Q qui crée une question générique, comportement de démonstration à ne pas reproduire (docs/gap CODE) ; rien n'est décidé.
- [US-CMP-17](09-compliance.md#us-cmp-17--suivre-dans-compliance-létat-des-questions-et-la-réponse-du-client) — ce que l'arrivée d'une réponse change à l'avancement de l'affectation (elle reste « Awaiting Q&A » ?) et si son contributeur en est prévenu ne sont pas spécifiés ; QA-006 parle encore de « débloquer » (docs/gap SPECS, « Q&A avec le client », Toujours ouvert ; PLAT-005).
- [US-CMP-19](09-compliance.md#us-cmp-19--renvoyer-une-affectation-qui-nest-pas-la-sienne) — sur un tender à un seul système (SIG, Mainline), ce que proposent « Wrong system » et « This system doesn't apply here » n'est pas défini ; ne pas inventer d'équivalent de la passe 1 (ALLOCATION, « Réallocation » ; OPEN-15).
- [US-CMP-24](09-compliance.md#us-cmp-24--relancer-le-contributeur-dune-affectation-due) — le canal de la relance (notification interne, e-mail) et son contenu ne sont pas définis ; la maquette ne fait que dater et journaliser (PLAT-005, OPEN-11).
- [US-CMP-25](09-compliance.md#us-cmp-25--saisir-ou-modifier-une-réponse-en-tant-que-chef-de-projet) — un contributeur peut-il réviser son propre verdict une fois donné ? Qui documente la stratégie et le risque d'un Not compliant saisi par le chef de projet sur l'affectation d'un contributeur ? Rien ne le décide (docs/gap SPECS, « Modèle de conformité », Toujours ouvert ; SPEC-risks §1).
- [US-CMP-27](09-compliance.md#us-cmp-27--rouvrir-les-verdicts-dune-exigence-modifiée-par-une-nouvelle-version) — le sort de la stratégie d'écart, des risques liés et de la correction du chef de projet d'une affectation rouverte n'est pas décidé (voir US-RSK-09) ; l'effet d'une correction de traduction sur une exigence déjà répondue (To review seulement, ou verdicts rouverts ?) non plus (LIFE-008 ; docs/gap README).
- [US-CMP-28](09-compliance.md#us-cmp-28--exporter-le-registre-de-conformité-avec-options) — la langue par défaut de l'export (LANG-003 : originale ; maquette : anglais) ; ce qui part au client — la conformité externe seule ou aussi l'interne, quelles colonnes — n'est pas défini, et « colonnes personnalisées hors export client » reste un défaut à confirmer (DEC-068 ; docs/gap SPECS, « Écran Compliance », Toujours ouvert).

### Stratégies d'écart, conformité externe et risques

- [US-RSK-04](10-risques.md#us-rsk-04--choisir-une-stratégie-décart-après-un-not-compliant) — quand un Not compliant redevient Compliant, ce que deviennent sa stratégie, ses liens de risque et une éventuelle correction du chef de projet n'est pas décidé — la maquette efface stratégie et risques et garde la correction (docs/gap SPECS, « Statuts d'une affectation », Toujours ouvert).
- [US-RSK-08](10-risques.md#us-rsk-08--dériver-la-conformité-externe-dune-affectation) — DEC-106 et CONF-029 disent « par système » alors que le verdict se donne par organisation (DEC-087, DEC-055) ; le grain de la stratégie et de la conformité externe (organisation ou système) est à confirmer — la maquette porte tout au système.
- [US-RSK-09](10-risques.md#us-rsk-09--consolider-la-conformité-externe-dune-exigence) — ce que deviennent la stratégie, les risques liés et la correction du chef de projet d'une affectation rouverte par une version n'est pas décidé ; la maquette les garde, et la page Risks compte encore l'exigence comme liée (docs/gap SPECS, « Stratégies d'écart », Toujours ouvert).
- [US-RSK-11](10-risques.md#us-rsk-11--consulter-la-liste-des-risques-du-tender) — modifier la justification d'un risque, ou supprimer un risque devenu inutile, n'est pas spécifié depuis DEC-113 ; filtres avancés et export filtré « comme sur toute table » non plus (SPEC-risks §5, §6.2 ; docs/gap SPECS, « Page Risks », Toujours ouvert).

### Registre Q&A avec le client

- [US-QA-01](11-qa.md#us-qa-01--recevoir-dans-le-registre-une-question-posée-depuis-compliance) — créer une question directement dans le registre, hors d'une affectation, n'est pas spécifié (la maquette ne le permet pas) ; annuler depuis Compliance une question déjà marquée « Sent » n'est pas spécifié.
- [US-QA-03](11-qa.md#us-qa-03--rechercher-une-question-et-filtrer-par-système) — le filtre système d'un tender SIG — un seul système, axe système absent des autres écrans (TYPE-T08) — n'est pas précisé, la maquette y propose les 16 codes ; la légende des codes reste à fournir (DEC-032).
- [US-QA-04](11-qa.md#us-qa-04--voir-les-dates-de-clôture-des-questions-et-de-retour-des-réponses) — l'origine des deux dates n'est pas tranchée — saisies à la création, dans les paramètres, ou lues dans les documents du tender (ancienne SPEC-qa-screen §7.1).
- [US-QA-05](11-qa.md#us-qa-05--exporter-vers-excel-les-questions-à-envoyer) — le droit d'exporter n'est pas précisé (déduit : chef de projet, au titre de la relation client) ; le format attendu par le client (réglage « Issuer channel », voir US-CFG) n'est pas fixé.
- [US-QA-07](11-qa.md#us-qa-07--importer-le-dossier-de-réponses-du-client) — format réel du dossier du client, à obtenir avant de construire l'extraction (OPEN-10) ; plusieurs vagues ou plusieurs dossiers par tender (QA-004, OPEN-06) ; seuil de certitude d'un rapprochement ; réponse importée pour une question encore To send (la maquette ne rapproche que les Sent) ; droit d'importer (déduit : chef de projet).
- [US-QA-08](11-qa.md#us-qa-08--confirmer-ou-écarter-une-réponse-incertaine) — ce que devient une réponse écartée (rangée parmi les autres soumissionnaires ou abandonnée) n'est pas précisé, la maquette l'abandonne ; qui peut confirmer ou écarter n'est pas précisé (déduit : chef de projet).
- [US-QA-09](11-qa.md#us-qa-09--lire-la-réponse-du-client-sous-sa-question) — l'état d'avancement de l'affectation après la réponse (QA-006 et QA-T03 parlent encore de « débloquer », alors que rien n'est bloqué depuis DEC-092) et la notification du contributeur à l'arrivée de la réponse (PLAT-005) ne sont pas spécifiés.
- [US-QA-10](11-qa.md#us-qa-10--consulter-les-questions-réponses-des-autres-soumissionnaires) — rattacher à la main une question-réponse « No requirement linked » à une exigence n'est pas spécifié.
- [US-QA-11](11-qa.md#us-qa-11--réserver-à-léquipe-de-gestion-le-marquage-des-questions-envoyées) — les droits d'importer, d'exporter et de confirmer ou écarter une réponse ne sont pas précisés (déduit : chef de projet, « relation client globale » de la matrice d'ACCESS).

### Team casting et droits

- [US-TEAM-03](12-casting-droits.md#us-team-03--composer-léquipe-de-gestion-du-projet) — le créateur reste-t-il impossible à retirer une fois le tender créé ? L'assistant de création l'affiche « Never removed — created the project », alors que le Team casting permet de le retirer s'il reste un autre chef de projet ; ACC-001 dit seulement qu'il est le premier membre.
- [US-TEAM-04](12-casting-droits.md#us-team-04--ajouter-un-système-au-tender-depuis-la-liste-de-référence) — la légende métier des 16 codes reste à fournir (DEC-032) ; retirer un système du casting n'est pas spécifié ; le casting d'un tender RSC n'est pas décrit (OPEN-15).
- [US-TEAM-08](12-casting-droits.md#us-team-08--retrouver-une-personne-dans-un-casting-de-200-personnes) — les budgets de temps de réponse restent à fixer (PLAT-007, OPEN-08).
- [US-TEAM-10](12-casting-droits.md#us-team-10--laisser-les-contributeurs-dun-système-gérer-ses-rattachements) — la façon de désigner le manager facultatif d'un système n'est spécifiée nulle part ; la maquette les sème, aucun écran ne permet d'en nommer un (DEC-030, DEC-124).
- [US-TEAM-11](12-casting-droits.md#us-team-11--désigner-automatiquement-la-personne-dune-allocation-depuis-son-périmètre) — sur le modèle Mainline, l'OBS est un poste et non une équipe (DEC-062) — sa correspondance avec les périmètres du casting n'est pas tranchée ; l'effet d'un rattachement ajouté ou retiré après la dérivation sur les allocations déjà faites n'est pas spécifié.

### Tableau de bord du tender

- [US-DASH-01](13-tableau-de-bord.md#us-dash-01--voir-lidentité-et-léchéance-du-tender-ouvert) — mention « Bid Director » et place de l'équipe de gestion dans l'en-tête — vocabulaire non refermé par écrit, DEC-030 ne retient que Project manager / Contributor ; affichage une fois l'échéance passée, non décrit.
- [US-DASH-03](13-tableau-de-bord.md#us-dash-03--suivre-létape-compliance-en-parallèle) — dénominateur M — toutes les exigences du tender ou seulement celles déjà affectées (non écrit).
- [US-DASH-07](13-tableau-de-bord.md#us-dash-07--voir-ce-qui-mattend-dans--what-needs-you-now-) — ce que voit un contributeur sur ce tableau de bord (ACC-007 lui ouvre la lecture, aucun texte ne décrit sa vue).
- [US-DASH-08](13-tableau-de-bord.md#us-dash-08--voir-le-travail-dallocation-qui-mattend) — valeur du seuil de confiance des modèles d'allocation (75 % dans la maquette, sans règle écrite ni réglage) ; compter encore un OBS faible sur une exigence déjà validée ou non ; ce qui retire le signal de découpe incertaine et la correction manuelle de la découpe (US-CAP-05).
- [US-DASH-09](13-tableau-de-bord.md#us-dash-09--voir-larrivée-dune-nouvelle-version-et-ses-effets) — plusieurs versions téléversées à la suite — raconter seulement la dernière ou chacune (non écrit).
- [US-DASH-10](13-tableau-de-bord.md#us-dash-10--voir-les-réponses-en-retard-et-les-not-compliant-à-documenter) — seuil de 5 jours fixé par PLAT-008 face au réglage « Overdue threshold » des paramètres, relié à rien (US-CFG-05).
- [US-DASH-12](13-tableau-de-bord.md#us-dash-12--lire-les-derniers-commentaires-du-tender) — liste exacte des événements qui comptent comme commentaire dans ce fil (non écrite).
- [US-DASH-13](13-tableau-de-bord.md#us-dash-13--suivre-les-réponses-par-système) — « sous-système » désigne ici les périmètres staffés du casting (DEC-118), alors que DEC-046 et DEC-058 appellent sous-systèmes les codes vers lesquels un Turnkey répartit.
- [US-DASH-14](13-tableau-de-bord.md#us-dash-14--suivre-lactivité-récente-du-tender) — liste des faits qui entrent dans ce fil et sa profondeur (non écrites).
- [US-DASH-15](13-tableau-de-bord.md#us-dash-15--ouvrir-la-cloche-du-tableau-de-bord) — déclencheurs, destinataires et regroupement des notifications (PLAT-005, OPEN-11).

### Statistiques

- [US-STAT-03](14-statistiques.md#us-stat-03--suivre-les-dates-clés-et-le-rythme-du-tender) — historique et formules (PLAT-008 « à compléter ») ; origine des dates de cut-off et de réponse du client (saisies à la création, dans les paramètres ou lues dans les documents — non tranché).
- [US-STAT-04](14-statistiques.md#us-stat-04--voir-les-systèmes-les-plus-actifs-de-la-semaine) — « sous-système » = périmètres staffés du casting (DEC-118) contre codes vers lesquels un Turnkey répartit (DEC-046, DEC-058) ; historique nécessaire (PLAT-008).
- [US-STAT-06](14-statistiques.md#us-stat-06--voir-où-en-sont-les-exigences-dans-allocation) — place du statut « Reassignment requested » d'un Turnkey (DEC-104) dans cette barre (non écrit).
- [US-STAT-08](14-statistiques.md#us-stat-08--voir-les-exigences-renvoyées-pour-réallocation) — PLAT-008 demande aussi un compte « par demandeur », qui mesurerait des personnes, contraire à DEC-118 — à réarbitrer.
- [US-STAT-09](14-statistiques.md#us-stat-09--voir-le-travail-invalidé-par-une-nouvelle-version) — PLAT-008 renvoie le « travail à revoir » à OPEN-07 (correspondance des exigences entre versions, fusion / scission).
- [US-STAT-10](14-statistiques.md#us-stat-10--voir-la-progression-vers-le-client) — dénominateurs et formules (PLAT-008 « à compléter »).
- [US-STAT-11](14-statistiques.md#us-stat-11--suivre-les-réponses-par-système-et-leurs-retards) — borne « âge ≥ 5 jours » (Réponses par système) contre « au-delà de 5 jours » (Attente) dans PLAT-008, et lien avec le réglage « Overdue threshold » (US-CFG-05) ; double sens de « sous-système ».
- [US-STAT-12](14-statistiques.md#us-stat-12--voir-ce-quattendent-les-exigences-encore-ouvertes) — ranger « On the client » avant « On a contributor » alors qu'une question ne bloque rien (DEC-092) et que Compliance met d'abord en avant ce que doit le contributeur (DEC-125) — règle PLAT-008 antérieure, non réarbitrée.

### Configuration du tender

- [US-CFG-01](15-configuration.md#us-cfg-01--ouvrir-les-paramètres-et-ny-trouver-que-des-réglages-réels) — qui peut modifier quels paramètres (JRN-007, OPEN-05) ; enregistrement immédiat réglage par réglage ou par « Save configuration » (JRN-007).
- [US-CFG-02](15-configuration.md#us-cfg-02--consulter-les-informations-générales-du-tender) — modifier le nom et le BO-ID après création (non décidé) ; les interrupteurs par étape IA font-ils partie du mode figé (DEC-095 ne le dit pas).
- [US-CFG-03](15-configuration.md#us-cfg-03--régler-léchéance-de-soumission) — accepter ou non une échéance déjà passée (non écrit).
- [US-CFG-04](15-configuration.md#us-cfg-04--voir-les-contributeurs-du-tender-depuis-les-paramètres) — garder cette section ou la réduire à un lien vers Team casting (doublon) ; effet des « Assignment criteria » (PBS, ABS, OBS), non spécifié.
- [US-CFG-05](15-configuration.md#us-cfg-05--régler-le-seuil-de-retard-et-la-cadence-des-relances) — le seuil remplace-t-il les 5 jours fixés par PLAT-008 pour le tableau de bord et les statistiques ; la cadence limite-t-elle les relances manuelles ou pilote-t-elle des relances automatiques (déclencheurs de PLAT-005, OPEN-11).
- [US-CFG-06](15-configuration.md#us-cfg-06--consulter-le-système-le-produit-et-le-modèle-appliqué) — produits et modèles RSC non fournis (DEC-047, OPEN-15) ; maille de l'OBS du modèle Urban non tranchée.
- [US-CFG-07](15-configuration.md#us-cfg-07--changer-de-modèle-et-relancer-toute-la-dérivation) — statut des exigences après la relance (à revoir ou à valider) et sort des personnes affectées, des stratégies et des risques — non écrits ; forme du geste de confirmation renforcée ; changement de modèle sur un Turnkey (dépend de la matrice des combinaisons, DEC-048).
- [US-CFG-10](15-configuration.md#us-cfg-10--choisir-son-thème-clair-ou-sombre) — place d'un réglage personnel dans les paramètres d'un tender (non décidé).
- [US-CFG-11](15-configuration.md#us-cfg-11--capter-chaque-correction-dune-proposition-de-lia) — destination et anonymisation des retours vers le chantier IA (DEC-020).
- [US-CFG-12](15-configuration.md#us-cfg-12--consulter-la-qualité-de-lia-dans--ai-feedback-) — formules — dénominateur, revue effective, corrections répétées (PLAT-008 « Corrections IA ») ; définition d'un motif récurrent ; période couverte au-delà de la session.
- [US-CFG-13](15-configuration.md#us-cfg-13--choisir-le-canal-de-lémetteur-pour-les-questions) — gabarit attendu pour « Buyer portal » et « Standard form », non fourni.
- [US-CFG-14](15-configuration.md#us-cfg-14--régler-la-numérotation-des-versions-et-la-détection-daddendum) — règle de numérotation (format, alias) ; ce que fait la détection d'addendum — où la proposition apparaît, qui la confirme (aucune règle écrite).
- [US-CFG-15](15-configuration.md#us-cfg-15--voir-la-langue-de-travail-et-la-langue-source) — modifier la langue source après la capture (non décidé) ; langue de l'interface (seul l'anglais existe, aucune décision produit).

### Transverse : journal, notifications, plateforme

- [US-X-01](16-transverse.md#us-x-01--consulter-le-journal-dactivité-dune-exigence) — liste exacte des événements tracés, rétention et droits de lecture du journal (DOM-011, PLAT-003, OPEN-11).
- [US-X-02](16-transverse.md#us-x-02--commenter-une-exigence) — mentions « @ » (le champ les annonce, aucune règle) ; droit de commenter une exigence hors de son système, que DEC-100 met en lecture seule ; modifier ou supprimer un commentaire.
- [US-X-04](16-transverse.md#us-x-04--se-connecter-par-sso-et-naccéder-quà-ses-tenders) — politique de création d'un tender (JRN-001) ; rôles Admin et VIP (OPEN-02) ; standards de sécurité (OPEN-11).
- [US-X-06](16-transverse.md#us-x-06--tracer-tout-changement-humain-ou-machine) — rétention, suivi de session et standards de sécurité (OPEN-11) ; unité et granularité du coût des traitements de l'IA.
- [US-X-07](16-transverse.md#us-x-07--garder-séparées-la-proposition-de-lia-la-valeur-retenue-et-la-correction) — modalités de reprise et de correspondance entre versions (OPEN-07, OPEN-09).
- [US-X-08](16-transverse.md#us-x-08--exporter-les-exigences-du-tender) — formats, correspondances et aller-retour DOORS à contractualiser (PLAT-004, OPEN-10, OPEN-12).
- [US-X-09](16-transverse.md#us-x-09--importer-un-export-doors-comme-document-du-tender) — formats exacts, correspondance des attributs DOORS et boucle aller-retour (OPEN-10, OPEN-12).
- [US-X-10](16-transverse.md#us-x-10--recevoir-les-notifications-dans-lapplication-et-par-e-mail) — déclencheurs, destinataires, regroupement, fréquence et relances (PLAT-005, OPEN-11) ; lien avec « Maximum reminder cadence » (US-CFG-05) ; la relance de Compliance (DEC-125) envoie-t-elle un e-mail.
- [US-X-11](16-transverse.md#us-x-11--travailler-sur-100-000-lignes-à-dix-en-même-temps) — budgets chronométrés, portée exacte du jeu de 100 000 lignes et protocole de mesure (OPEN-08) ; sélection de toutes les pages et « Filter to Selection » à cette échelle (OPEN-13, UX-006).
- [US-X-13](16-transverse.md#us-x-13--ne-rien-perdre-en-cas-déchec-ou-de-conflit-denregistrement) — mode de résolution d'un conflit (dernière écriture avec avertissement, fusion, rechargement) non choisi.
- [US-X-14](16-transverse.md#us-x-14--lire-des-couleurs-qui-gardent-toujours-le-même-sens) — référentiel d'accessibilité à atteindre (contrastes, lecteur d'écran, navigation au clavier hors tables) — aucune règle écrite ; rouge exact de la marque à confirmer (DEC-063).

## Écarts de la maquette, par story

La maquette simule ou diffère ; à corriger dans la maquette ou à ignorer, jamais à reproduire.

### Accueil (My tenders)

- [US-HOME-02](01-accueil.md#us-home-02--reprendre-le-tender-en-cours) — le tender proposé est choisi par un marquage de démonstration, pas d'après l'usage de la personne.
- [US-HOME-03](01-accueil.md#us-home-03--comprendre-comment-un-tender-traverse-srm) — l'état masqué n'est gardé qu'en mémoire et revient à chaque réinitialisation.
- [US-HOME-04](01-accueil.md#us-home-04--voir-la-liste-de-mes-tenders) — la liste montre des tenders de démonstration non ouvrables (« Demo project — list & status only ») et déduit le rôle d'un texte libre ; rien de cela n'existe dans le produit.
- [US-HOME-05](01-accueil.md#us-home-05--lire-lavancement-dun-tender-sur-sa-ligne) — les compteurs de démonstration ne concordent pas avec ceux du tableau de bord ; dans le produit, ce sont les mêmes données.
- [US-HOME-06](01-accueil.md#us-home-06--ouvrir-un-tender-depuis-laccueil) — l'ouverture des tenders de démonstration non construits est bloquée par un message ; sans objet dans le produit.

### Création d'un tender

- [US-NEW-01](02-creation.md#us-new-01--décrire-lidentité-du-tender) — la date de soumission a une valeur par défaut fixe, et ni la région, ni l'émetteur, ni la date ne sont conservés sur le tender créé (seul un nombre de jours l'est).
- [US-NEW-02](02-creation.md#us-new-02--choisir-la-ligne-produit-fixée-à-la-création) — la ligne « Services » est encore proposée.
- [US-NEW-05](02-creation.md#us-new-05--joindre-et-ordonner-les-documents-source) — seuls des PDF sont annoncés, et les documents sont fictifs (pas de vrai choix de fichier, rien n'est conservé sur le tender créé).
- [US-NEW-06](02-creation.md#us-new-06--choisir-le-mode-dassistance-ia-fixé-à-la-création) — le mode est une seule valeur pour toute la démonstration, pas une propriété du tender, et les paramètres ne l'affichent pas. La phrase « The AI never overwrites a manual correction » contredit les relances qui écrasent les dérivations (ALLOC-015, DEC-027).
- [US-NEW-07](02-creation.md#us-new-07--constituer-léquipe-de-gestion-du-projet) — l'équipe saisie ici est stockée sur le tender mais Team casting ne la lit pas ; l'annuaire est une liste locale de démonstration.
- [US-NEW-09](02-creation.md#us-new-09--retrouver-dans-le-tender-créé-tout-ce-que-lassistant-a-fixé) — un tender créé dans la maquette réutilise le contenu du tender de référence (bandeau « Prototype scope ») ; ni l'émetteur, ni l'échéance, ni les documents, ni le mode ne sont conservés sur lui.

### Documents et versions

- [US-DOC-01](03-documents.md#us-doc-01--voir-les-documents-du-tender-dans-leur-ordre-de-lecture) — la liste de démonstration est la même sur tous les tenders et ses compteurs sont écrits à la main.
- [US-DOC-03](03-documents.md#us-doc-03--réordonner-les-documents-du-tender) — le nouvel ordre ne se propage pas aux autres écrans et se perd au rechargement.
- [US-DOC-04](03-documents.md#us-doc-04--téléverser-une-nouvelle-version-dun-document) — l'écart et le choix des exigences « modifiées » sont simulés, aucun fichier n'est lu, et la version téléversée n'atteint pas Allocation.
- [US-DOC-05](03-documents.md#us-doc-05--retirer-un-document-en-annonçant-ce-qui-sera-perdu) — le retrait n'agit que sur cet écran.
- [US-DOC-06](03-documents.md#us-doc-06--ajouter-un-document-en-cours-de-tender) — le document est fictif (nom, fichier, nombre d'exigences), le traitement est minuté, n'inclut pas l'allocation et ses libellés parlent encore de « class, system and type ».
- [US-DOC-07](03-documents.md#us-doc-07--exporter-les-exigences-dun-seul-document) — l'export est simulé ; la fenêtre propose aussi CSV et ReqIF et décrit la caractérisation comme « class, system and type ».
- [US-DOC-08](03-documents.md#us-doc-08--réserver-la-gestion-des-documents-à-léquipe-de-gestion-du-projet) — l'écran n'a aucune notion de rôle ; toutes les actions sont ouvertes à tous.

### Capture, segmentation, traduction et IA

- [US-CAP-01](04-capture-ia.md#us-cap-01--enchaîner-automatiquement-les-étapes-ia-activées) — le traitement est une temporisation simulée, et sa dernière étape s'intitule encore « Allocating to contributors… » alors que l'IA dérive des organisations, jamais des personnes (DEC-054).
- [US-CAP-02](04-capture-ia.md#us-cap-02--régler-la-conversion-du-document-source) — ces réglages sont affichés sans aucun effet (avertissement « demo only »).
- [US-CAP-04](04-capture-ia.md#us-cap-04--capturer-les-images-sans-en-lire-le-contenu) — les lignes issues d'images de la démonstration portent un texte et des valeurs pré-remplis.
- [US-CAP-05](04-capture-ia.md#us-cap-05--signaler-une-découpe-incertaine) — le réglage « Uncertainty threshold » des paramètres n'agit sur rien, et le mode « Edit segmentation » est masqué.
- [US-CAP-07](04-capture-ia.md#us-cap-07--traduire-automatiquement-vers-langlais-de-travail) — la lecture dans une langue tierce (German, Spanish) est simulée.
- [US-CAP-08](04-capture-ia.md#us-cap-08--corriger-une-traduction-ce-qui-remet-lexigence-en-revue) — enregistrer une correction ne change pas le statut de l'exigence.
- [US-CAP-09](04-capture-ia.md#us-cap-09--caractériser-chaque-bloc-avec-un-niveau-de-confiance-low-medium-ou-high) — les niveaux de la démonstration sont générés et ne mesurent rien.
- [US-CAP-10](04-capture-ia.md#us-cap-10--dire-quaucun-modèle-ne-sapplique-sans-en-emprunter-un-en-silence) — aucun état « sans modèle » n'est montré pendant le traitement.
- [US-CAP-12](04-capture-ia.md#us-cap-12--relancer-automatiquement-les-modèles-sur-les-seules-exigences-modifiées-par-une-nouvelle-version) — une version téléversée dans Documents n'atteint pas Allocation et aucune relance n'est simulée.
- [US-CAP-13](04-capture-ia.md#us-cap-13--repartir-de-zéro-sur-une-exigence-issue-dune-fusion-ou-dune-scission) — le mode « Edit segmentation » (scinder, fusionner) est masqué et ne fait que remettre l'exigence en revue.

### Allocation — modèle et panneau

- [US-ALM-02](05-allocation.md#us-alm-02--savoir-pourquoi-une-exigence-est-à-revoir) — le motif de dérivation faible dit encore « the proposed assignment may be wrong » (DEC-054 : une organisation) ; une correction de traduction ne repasse pas l'exigence en revue (LIFE-008).
- [US-ALM-04](05-allocation.md#us-alm-04--corriger-la-nature-et-la-classe-dune-exigence) — la recherche plein texte et des puces de la vue Document lisent encore les valeurs Functional / Performance (ALLOC-T26).
- [US-ALM-08](05-allocation.md#us-alm-08--ajouter-ou-retirer-un-système) — la cellule System et « Assign › System » ne vérifient pas que l'utilisateur est chef de projet, et retirer un système depuis la cellule ne supprime pas son allocation (seul le ✕ du détail le fait).
- [US-ALM-14](05-allocation.md#us-alm-14--corriger-la-chaîne-abs--pbs--obs) — la maquette n'exige qu'une organisation (OBS) pour sortir d'« Incomplete » (retirer la dernière l'y renvoie, DEC-076) ; un ABS ou un PBS manquant n'y retient pas l'exigence.
- [US-ALM-27](05-allocation.md#us-alm-27--valider-laiguillage-dune-exigence-turnkey) — quand c'est le système qui manque, la raison affichée parle encore de nature et de classe (« Characterisation incomplete — set its nature and class first. »).
- [US-ALM-29](05-allocation.md#us-alm-29--demander-une-réallocation) — la personne de remplacement est choisie parmi tous les contributeurs, pas seulement ceux du système (DEC-102).
- [US-ALM-30](05-allocation.md#us-alm-30--traiter-une-demande-de-réallocation) — un contributeur qui tient une organisation voit encore « ✓ Approve » / « ✕ Reject » sur une demande venue de Compliance (hiérarchie manager / expert héritée, abandonnée par DEC-003 et DEC-012).
- [US-ALM-34](05-allocation.md#us-alm-34--lire-la-conformité-dans-allocation-sans-la-saisir) — sur une exigence à un seul système, la cellule Compliance de la ligne affiche « — » au lieu de la valeur (déduit du code).

### Tables communes Allocation et Compliance

- [US-TAB-04](06-tables.md#us-tab-04--rechercher-une-exigence-par-son-identifiant-ou-son-texte) — la recherche d'Allocation trouve encore les valeurs Functional / Performance…, sorties d'Allocation (ALLOC-T26) ; elle tourne dans le navigateur, sur les lignes chargées.
- [US-TAB-05](06-tables.md#us-tab-05--trier-par-un-en-tête-de-colonne) — le tri se fait dans le navigateur, sur les lignes chargées.
- [US-TAB-06](06-tables.md#us-tab-06--filtrer-une-colonne-comme-dans-excel) — le filtrage tourne dans le navigateur, sur les lignes chargées, sans serveur.
- [US-TAB-09](06-tables.md#us-tab-09--enregistrer-un-filtre-et-le-réutiliser-sur-un-autre-tender) — les filtres sont gardés dans le navigateur, pas rattachés au compte de la personne.
- [US-TAB-12](06-tables.md#us-tab-12--redimensionner-les-colonnes) — les largeurs sont perdues au rechargement de la page.
- [US-TAB-13](06-tables.md#us-tab-13--sélectionner-plusieurs-lignes-et-agir-en-une-fois) — Compliance n'a ni Maj+clic ni « Select all N ».
- [US-TAB-15](06-tables.md#us-tab-15--se-déplacer-et-sélectionner-au-clavier) — sur Compliance, ←/→ suivent un ordre de colonnes figé, pas l'ordre affiché.
- [US-TAB-16](06-tables.md#us-tab-16--éditer-une-cellule-au-clavier) — sur Compliance, Entrée ou F2 n'ouvre pas l'édition d'une cellule ; seules Entrée (valider) et Échap (rétablir) y fonctionnent, une fois dans le champ.
- [US-TAB-18](06-tables.md#us-tab-18--annuler-la-dernière-action-même-après-le-message) — dans Allocation, seule l'assignation faite dans la cellule « Assigned to » d'une ligne s'annule, pas l'assignation groupée ni celle du panneau ; les annulations possibles sont perdues en quittant l'écran.
- [US-TAB-23](06-tables.md#us-tab-23--filtrer-et-trier-sur-une-colonne-personnalisée) — sur Compliance, une colonne de type liste n'a pas d'entonnoir d'en-tête ; seul le filtre avancé la filtre.

### Vue Document d'Allocation

- [US-DOCV-04](07-vue-document.md#us-docv-04--voir-la-nature-de-chaque-bloc-et-le-doute-de-lia) — dans un tableau du document, l'étiquette d'une ligne affiche encore l'ancien type (« Interface · … ») au lieu de « Requirement ».
- [US-DOCV-06](07-vue-document.md#us-docv-06--comparer-un-document-à-une-version-antérieure-onglet-changes) — les versions et leurs changements sont des données propres à Allocation ; une version téléversée dans Documents n'y arrive pas.

### Changements de version côté Allocation

- [US-CHG-01](08-changements.md#us-chg-01--revoir-une-exigence-ajoutée-ou-modifiée-par-une-nouvelle-version) — les versions d'Allocation sont des données propres à l'écran ; une version téléversée dans Documents n'y arrive pas, et la relance automatique des modèles n'y est pas démontrée.

### Compliance

- [US-CMP-01](09-compliance.md#us-cmp-01--créer-les-affectations-quand-lallocation-est-validée) — la maquette porte une affectation par système (les organisations ne sont qu'affichées) et ses affectations sont des données de démonstration : valider dans Allocation ne crée ni ne modifie rien dans Compliance.
- [US-CMP-04](09-compliance.md#us-cmp-04--déplier-une-exigence-en-systèmes-et-en-organisations) — la maquette n'affiche les organisations qu'en lecture, avec des valeurs écrites à la main ; le verdict s'y saisit au niveau du système et n'est jamais calculé depuis les organisations.
- [US-CMP-13](09-compliance.md#us-cmp-13--retrouver-son-brouillon-de-verdict) — le brouillon ne vit que dans la session de l'application (perdu au rechargement), pas sur le serveur.
- [US-CMP-14](09-compliance.md#us-cmp-14--mettre-une-affectation-de-côté) — le marqueur ne vit que dans la session de l'application, pas sur le serveur.
- [US-CMP-15](09-compliance.md#us-cmp-15--consulter-les-questions-et-les-exigences-similaires) — la maquette affiche REX (exemples) et Chat (non construit) ; Similar y est un substitut par mots communs (les trois plus proches, à 25 % au moins).
- [US-CMP-20](09-compliance.md#us-cmp-20--consolider-les-verdicts-dune-exigence) — la maquette saisit le verdict au niveau du système ; les organisations y sont affichées avec des valeurs écrites à la main et n'entrent pas dans le calcul.
- [US-CMP-22](09-compliance.md#us-cmp-22--voir-ce-qui-est-attendu-dans-le-panneau-du-chef-de-projet) — la maquette affiche aussi les onglets REX (exemples) et Chat (non construit), hors V1 (DEC-021).
- [US-CMP-23](09-compliance.md#us-cmp-23--réaffecter-une-affectation-renvoyée) — le formulaire de réaffectation s'affiche aussi pour un contributeur du système de l'affectation.
- [US-CMP-25](09-compliance.md#us-cmp-25--saisir-ou-modifier-une-réponse-en-tant-que-chef-de-projet) — la maquette ne permet au chef de projet de saisir que le verdict d'un partenaire ; personne n'y révise un verdict donné, hors annulation (⌘/Ctrl + Z) et réouverture par une version.
- [US-CMP-27](09-compliance.md#us-cmp-27--rouvrir-les-verdicts-dune-exigence-modifiée-par-une-nouvelle-version) — la maquette choisit elle-même les exigences « modifiées » et rejoue la réouverture à chaque ouverture de l'écran.
- [US-CMP-28](09-compliance.md#us-cmp-28--exporter-le-registre-de-conformité-avec-options) — la génération n'est qu'un message ; l'anglais y est coché par défaut, alors que LANG-003 veut le texte original.

### Stratégies d'écart, conformité externe et risques

- [US-RSK-01](10-risques.md#us-rsk-01--écrire-les-stratégies-décart-du-tender) — les tenders de démonstration arrivent avec quatre stratégies déjà écrites.
- [US-RSK-11](10-risques.md#us-rsk-11--consulter-la-liste-des-risques-du-tender) — l'export n'est qu'un message, sans options.

### Registre Q&A avec le client

- [US-QA-01](11-qa.md#us-qa-01--recevoir-dans-le-registre-une-question-posée-depuis-compliance) — Compliance et le registre échangent les questions par une boîte aux lettres en mémoire, perdue au rechargement de la page ; les mêmes questions de démonstration s'affichent sur tous les tenders.
- [US-QA-04](11-qa.md#us-qa-04--voir-les-dates-de-clôture-des-questions-et-de-retour-des-réponses) — les deux dates sont écrites en dur, identiques sur tous les tenders, et « passed » / « overdue » ne sont pas calculés.
- [US-QA-05](11-qa.md#us-qa-05--exporter-vers-excel-les-questions-à-envoyer) — l'export est simulé — un message, aucun fichier.
- [US-QA-06](11-qa.md#us-qa-06--marquer-des-questions-envoyées-une-ou-plusieurs-et-revenir-en-arrière) — aucun contrôle de rôle — n'importe qui marque « Sent » ; la date d'envoi est le mot « Today ».
- [US-QA-07](11-qa.md#us-qa-07--importer-le-dossier-de-réponses-du-client) — extraction et rapprochement sont simulés (réponses écrites à la main, certitude fixe, une seule réponse à confirmer au premier import) ; l'écran n'offre pas le choix entre fichier et texte collé.
- [US-QA-11](11-qa.md#us-qa-11--réserver-à-léquipe-de-gestion-le-marquage-des-questions-envoyées) — le registre n'applique aucun rôle — tout le monde peut marquer, confirmer, exporter et importer.

### Team casting et droits

- [US-TEAM-01](12-casting-droits.md#us-team-01--ouvrir-le-team-casting-là-où-lon-a-à-agir) — l'arrivée dépend du sélecteur de démonstration « Viewing as » (chef de projet ou manager, aucun contributeur simple) ; l'équipe de gestion n'est affichée qu'aux chefs de projet.
- [US-TEAM-02](12-casting-droits.md#us-team-02--repérer-les-systèmes-sans-personne-et-les-staffer) — la couverture compte encore six périmètres plus « staffé directement » (« n/7 staffed », « Fully staffed » seulement quand les sept sont pourvus), chaque périmètre vide porte « ⚠ Unstaffed » et le filtre garde les périmètres vides.
- [US-TEAM-05](12-casting-droits.md#us-team-05--staffer-une-personne-sur-un-système-avec-ou-sans-périmètre) — annuaire SSO simulé ; le casting reste local à son écran (perdu au changement d'écran, lu ni par Allocation ni par Compliance) ; Configuration › « Team & contributors » garde une seconde liste de contributeurs saisie à la main (nom libre et « Team / domain »), sans lien avec le casting.
- [US-TEAM-08](12-casting-droits.md#us-team-08--retrouver-une-personne-dans-un-casting-de-200-personnes) — l'échelle n'est montrée que par la commande de démonstration « Simulate 200 roster ».
- [US-TEAM-10](12-casting-droits.md#us-team-10--laisser-les-contributeurs-dun-système-gérer-ses-rattachements) — seuls le chef de projet et des managers de système semés sont simulés — un contributeur sans rôle de manager ne staffe rien —, et la raison affichée parle du manager (« Read-only — <nom> manages this system, not you. »).
- [US-TEAM-11](12-casting-droits.md#us-team-11--désigner-automatiquement-la-personne-dune-allocation-depuis-son-périmètre) — Allocation ne lit pas le casting ; les personnes des OBS y sont semées à la main.
- [US-TEAM-17](12-casting-droits.md#us-team-17--laisser-le-chef-de-projet-saisir-ou-corriger-toute-réponse) — la maquette ne laisse le chef de projet saisir un verdict que pour un partenaire externe (« PM · for partner », DEC-082).

### Tableau de bord du tender

- [US-DASH-01](13-tableau-de-bord.md#us-dash-01--voir-lidentité-et-léchéance-du-tender-ouvert) — le volume vient d'une copie écrite à la main (14 exigences) et peut différer de la carte Allocation ; l'en-tête affiche « Bid Director: » suivi d'un nom écrit en dur.
- [US-DASH-02](13-tableau-de-bord.md#us-dash-02--suivre-létape-allocation-sur-sa-carte) — tant qu'Allocation n'a pas été ouvert dans la session, la carte lit une copie écrite à la main.
- [US-DASH-03](13-tableau-de-bord.md#us-dash-03--suivre-létape-compliance-en-parallèle) — les chiffres viennent d'une copie de Compliance écrite à la main.
- [US-DASH-04](13-tableau-de-bord.md#us-dash-04--ouvrir-team-casting-et-documents--versions-depuis-le-rail--always-open-) — le chiffre Documents (« 3 docs · 1 processing ») est écrit à la main ; le casting n'est ni persisté ni partagé avec les autres écrans.
- [US-DASH-05](13-tableau-de-bord.md#us-dash-05--voir-les-risques-et-les-questions-au-client-dans-le-rail) — le chiffre Q&A (« 5 questions · 1 answered ») est écrit à la main et ne lit pas le registre.
- [US-DASH-06](13-tableau-de-bord.md#us-dash-06--voir-les-demandes-de-réallocation-en-attente) — la boîte de demandes n'est pas propre au tender (filtrage par préfixe d'identifiant) ; « Review → » ouvre Allocation sans sélectionner l'exigence.
- [US-DASH-07](13-tableau-de-bord.md#us-dash-07--voir-ce-qui-mattend-dans--what-needs-you-now-) — la liste ne dit rien quand elle est vide.
- [US-DASH-08](13-tableau-de-bord.md#us-dash-08--voir-le-travail-dallocation-qui-mattend) — les OBS faibles ne figurent que dans la cloche, pas dans cette liste ; « 2 uncertain segmentations » est écrit à la main.
- [US-DASH-09](13-tableau-de-bord.md#us-dash-09--voir-larrivée-dune-nouvelle-version-et-ses-effets) — l'écart est simulé par Documents et seul le dernier téléversement est raconté.
- [US-DASH-10](13-tableau-de-bord.md#us-dash-10--voir-les-réponses-en-retard-et-les-not-compliant-à-documenter) — les retards sont une liste fixe, pas un calcul d'âge ; le libellé dit « unopened for N days » alors que la règle compte l'âge sans réponse.
- [US-DASH-11](13-tableau-de-bord.md#us-dash-11--voir-les-questions-à-envoyer-au-client) — « 2 questions to send » est écrit à la main et ne lit pas le registre.
- [US-DASH-12](13-tableau-de-bord.md#us-dash-12--lire-les-derniers-commentaires-du-tender) — seules les demandes de réallocation sont réelles ; les autres lignes sont écrites à la main, le fil ne lit pas le journal et ses éléments ne sont pas cliquables.
- [US-DASH-13](13-tableau-de-bord.md#us-dash-13--suivre-les-réponses-par-système) — les chiffres sont écrits à la main.
- [US-DASH-14](13-tableau-de-bord.md#us-dash-14--suivre-lactivité-récente-du-tender) — deux lignes sont écrites à la main (une question posée par une personne nommée, « QA-01 marked as sent »).
- [US-DASH-15](13-tableau-de-bord.md#us-dash-15--ouvrir-la-cloche-du-tableau-de-bord) — la cloche du tableau de bord ne nomme pas l'exigence quand il n'y en a qu'une ; celle d'Allocation affiche encore une liste figée (mention, version v2.1, rappel), contraire à la règle.

### Statistiques

- [US-STAT-01](14-statistiques.md#us-stat-01--lire-les-statistiques-par-onglet-une-phrase-puis-le-chiffre) — une partie des chiffres vient de copies écrites à la main ; sans visite préalable de Compliance, l'onglet Compliance affiche « Counted from Compliance — open it once… ».
- [US-STAT-03](14-statistiques.md#us-stat-03--suivre-les-dates-clés-et-le-rythme-du-tender) — l'historique est écrit à la main ; le point d'aujourd'hui vient d'une copie, pas des écrans.
- [US-STAT-04](14-statistiques.md#us-stat-04--voir-les-systèmes-les-plus-actifs-de-la-semaine) — la semaine est écrite à la main ; seules les validations et les verdicts de la session s'y ajoutent.
- [US-STAT-05](14-statistiques.md#us-stat-05--voir-léquipe-du-tender) — le casting n'est ni persisté ni partagé avec les autres écrans.
- [US-STAT-06](14-statistiques.md#us-stat-06--voir-où-en-sont-les-exigences-dans-allocation) — la barre lit une copie écrite à la main (14 exigences), qui peut différer de la carte Allocation.
- [US-STAT-08](14-statistiques.md#us-stat-08--voir-les-exigences-renvoyées-pour-réallocation) — les renvois déjà décidés sont écrits à la main ; seuls ceux de la session sont réels.
- [US-STAT-11](14-statistiques.md#us-stat-11--suivre-les-réponses-par-système-et-leurs-retards) — chiffres écrits à la main ; les retards sont une liste fixe, pas un calcul d'âge.
- [US-STAT-12](14-statistiques.md#us-stat-12--voir-ce-quattendent-les-exigences-encore-ouvertes) — l'ancienneté des questions est écrite à la main.

### Configuration du tender

- [US-CFG-01](15-configuration.md#us-cfg-01--ouvrir-les-paramètres-et-ny-trouver-que-des-réglages-réels) — la plupart des sections portent l'avertissement « TE2 — demo only » et « Save configuration » n'affiche qu'un message.
- [US-CFG-02](15-configuration.md#us-cfg-02--consulter-les-informations-générales-du-tender) — le mode d'assistance IA n'apparaît pas dans les paramètres (c'est une valeur unique pour toute la démo) ; nom et BO-ID sont des champs de saisie sans effet.
- [US-CFG-03](15-configuration.md#us-cfg-03--régler-léchéance-de-soumission) — la date est un champ sans effet ; le compte à rebours est figé à la création.
- [US-CFG-04](15-configuration.md#us-cfg-04--voir-les-contributeurs-du-tender-depuis-les-paramètres) — la liste est saisie au clavier (nom et équipe libres), indépendante du casting.
- [US-CFG-05](15-configuration.md#us-cfg-05--régler-le-seuil-de-retard-et-la-cadence-des-relances) — les deux réglages ne sont reliés à rien ; le tableau de bord compte les retards avec une règle fixe.
- [US-CFG-06](15-configuration.md#us-cfg-06--consulter-le-système-le-produit-et-le-modèle-appliqué) — sur un tender RSC ou « Services », le produit affiche le message de combinaison Turnkey.
- [US-CFG-07](15-configuration.md#us-cfg-07--changer-de-modèle-et-relancer-toute-la-dérivation) — la section n'est qu'un affichage — le sélecteur est sans effet, le bouton désactivé et les chiffres viennent d'une copie.
- [US-CFG-08](15-configuration.md#us-cfg-08--ajouter-un-partenaire-externe-à-la-liste-obs-turnkey) — la couleur des partenaires est hors de l'échelle de jetons.
- [US-CFG-10](15-configuration.md#us-cfg-10--choisir-son-thème-clair-ou-sombre) — le thème est une valeur de la session de démo, rangée dans les paramètres du tender bien qu'il soit personnel.
- [US-CFG-11](15-configuration.md#us-cfg-11--capter-chaque-correction-dune-proposition-de-lia) — le texte de la section promet encore une explication demandée quand l'IA était très confiante ; le retour n'est gardé que dans la session.
- [US-CFG-12](15-configuration.md#us-cfg-12--consulter-la-qualité-de-lia-dans--ai-feedback-) — taux et motifs écrits à la main ; seule la liste de la session est réelle.
- [US-CFG-13](15-configuration.md#us-cfg-13--choisir-le-canal-de-lémetteur-pour-les-questions) — le réglage n'agit pas sur l'écran Q&A.
- [US-CFG-14](15-configuration.md#us-cfg-14--régler-la-numérotation-des-versions-et-la-détection-daddendum) — réglages sans effet (« TE2 — demo only »).
- [US-CFG-15](15-configuration.md#us-cfg-15--voir-la-langue-de-travail-et-la-langue-source) — « Source document language » et « Interface language » sont des listes modifiables sans effet.

### Transverse : journal, notifications, plateforme

- [US-X-01](16-transverse.md#us-x-01--consulter-le-journal-dactivité-dune-exigence) — l'auteur d'un changement détecté est la personne qui regarde (« View as » compris) ; les historiques de démonstration sont écrits à la main.
- [US-X-03](16-transverse.md#us-x-03--retrouver-tout-le-travail-après-reconnexion) — rien n'est persisté ; chaque écran garde sa propre copie des données et les compteurs du tableau de bord sont écrits à la main.
- [US-X-05](16-transverse.md#us-x-05--faire-respecter-les-droits-du-tender-par-le-serveur) — les refus ne sont simulés que dans l'interface.
- [US-X-08](16-transverse.md#us-x-08--exporter-les-exigences-du-tender) — aucun fichier n'est produit (message seulement) ; CSV et ReqIF sont proposés sans intégration.

