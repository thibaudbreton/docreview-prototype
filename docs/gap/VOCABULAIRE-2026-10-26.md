# Écart de vocabulaire du 26 octobre 2026 (DEC-126)

**Pour qui.** Le développeur qui refait le front, et toute personne qui lit les specs ou les user stories. Ce document liste ce qui a changé de nom ou de forme le 26 octobre 2026. La décision est **DEC-126**, dans [docs/current/OPEN-QUESTIONS.md](../current/OPEN-QUESTIONS.md).

**Point de départ.** L'état décrit par [INTERFACE.md](INTERFACE.md), au 10 octobre, plus le nom « Smart Req » donné depuis.

> **Règle de lecture.** Les documents datés d'avant le 26 octobre gardent l'ancien vocabulaire : INTERFACE.md, CODE.md, SPECS.md, DECISIONS.md, les décisions DEC-001 à DEC-125 et les archives. Dans ces documents :
> - « Project manager », « System », « Nature », « Assigned to » et « Team casting » se lisent avec les nouveaux termes ci-dessous ;
> - l'ancien niveau « sous-système » placé sous un système SIG n'existe plus.

## Les renommages

| Avant | Maintenant | Où on le voit (exemples de libellés) |
|---|---|---|
| « Project » (le tender) | « Tender » | « ＋ New tender », « Create a tender », « Tender created », « Tender identity », « Tender configuration », « Back to the tender dashboard ». Le surtitre du tableau de bord passe de « Tender project » à « Tender ». |
| « Project name » | « Tender name » | Création (étape 1) et Configuration › General. |
| « Project manager » / « PM » | « Tender manager » / « TM » | Cartes d'accueil, « You lead N tenders as tender manager », « Tender management team », sélecteur de démo, « TM · for partner » (affectation d'un partenaire), « corrected by the TM ». |
| « Team casting » | « Users » | Écran `#team` (« Users — overview »), carte du rail « Always open », bouton de l'en-tête, bas de l'accueil, statistiques (« Users → »). |
| « Assigned to » | « PIC » (person in charge) | Colonne et filtre d'Allocation et de Compliance, champ du panneau (« PIC · responsible for its compliance »), barre d'actions groupées, raccourci clavier « Go to the selected row's PIC ». |
| « System » | « Sub-system » | Colonne, filtres et vue d'Allocation et de Compliance. Exemples : « + Add sub-system », « + Missing sub-system », « No sub-system yet », « ✓ Validate & send to the sub-systems », « My sub-system », « Right sub-system, wrong person », « Answers by sub-system », « By sub-system, with who is on it ». |
| « Nature » | « Type » | Champ du panneau (Heading / Information / Requirement), puce de la vue Document, « Type proposed by the AI with low confidence », « Type and class are set by the tender manager », « Characterisation — type, class, sub-system and status ». |

## Les changements de forme

- **Un seul niveau, le sous-système.** Le niveau qui s'appelait « sous-système » sous un système SIG disparaît. Il découpait les statistiques d'un tender SIG en Design, Wayside, V&V… Désormais, un tender SIG montre son unique sous-système comme n'importe quel autre, dans :
  - « Most active this week » ;
  - « The team » ;
  - « Answers by sub-system ».

  Sur chaque ligne de « Most active this week », la sous-ligne indique maintenant « N validated · N answers · N comments ».
- **Nouveau champ « Region ».**
  - **Valeurs :** NAM — North America, LAM — Latin America, FR — France. La liste reste à compléter.
  - **À la création :** il se choisit à l'étape 1 de l'assistant. Il remplace la liste provisoire EUR / MEA / APAC / AME / AFR, et apparaît dans le récapitulatif.
  - **Configuration › General :** il s'affiche en liste déroulante.
  - **Carte de tender à l'accueil :** le code apparaît à côté de la référence, le nom complet en infobulle.
  - **Tableau de bord :** il apparaît dans la ligne d'identité du tender (« FR — France »).
- **Champ « Combination » supprimé.**
  - **Création :** sur un tender Turnkey, la ligne « Product » ne s'affiche plus. Il n'y a plus de champ « Combination » ni de ligne correspondante dans le récapitulatif.
  - **Configuration › Allocation model :** la ligne « Product » est masquée sur un Turnkey, et la liste des modèles dit « Per-sub-system models — each sub-system's own ».

## Ce qui ne change pas

- **Identifiants :** SRM-00001…, RSK-…, QA-…, DEC-…, numéros de règle et de story.
- **Noms internes :** fonctions, variables, classes CSS (`getCurrentProject`, `crumb-project`, `typology`…). Les noms de composants de [COMPONENTS.md](../../COMPONENTS.md) restent aussi : « Nature Picker », « Team Casting Screen », « System Answers Row »…
- **Contenus :** textes d'exigence (« The system SHALL… »), noms de tenders et de documents (« Energy Monitoring System »), intitulés de postes du classeur de clés (« Project Manager », « Project Safety Engineer »…), commentaires du fil de démo.
- **Le titre « Bid Director »** de l'utilisateur de démo.

## Documents mis à jour

- **Maquette :** les 8 écrans, le shell (`build_merge.py`) et le chat masqué. Environ 630 libellés sont touchés : 172 « project », 395 « system », 19 « nature », 21 « Assigned to », 16 « Team casting », 6 « PM ».
- **Composants :** [COMPONENTS.md](../../COMPONENTS.md), avec 31 fiches datées du 26 octobre.
- **Specs :** `docs/current/*.md`, sauf AUDIT.md (relevé daté) et les décisions historiques. DEC-126 est cité dans les règles modifiées. Ajouts :
  - LIFE-001 et LIFE-T15 (Region et fin de Combination à la création) ;
  - TYPE-T12 ;
  - JRN-001, à qui s'ajoute la région ;
  - JRN-004, renommé « Maintenir les utilisateurs (écran Users) ».
- **User stories :** les 16 épopées, README, COUVERTURE et POINTS-OUVERTS ; DEC-126 est cité dans les stories concernées.
  - L'épopée 12 devient « Users et droits ».
  - Nouveaux critères Region : US-NEW-01, US-HOME-04, US-CFG-02.
  - US-NEW-03 devient « Choisir le produit du tender ».
  - Les statistiques n'ont plus qu'un niveau.
  - Les liens internes sont recalculés.
- **README et HANDOVER :** une note de vocabulaire seulement.

## Points à vérifier

- **Le haut de la hiérarchie dans TENDER-PROFILES.md.** Turnkey, SIG et RSC étaient appelés « système ». Ils sont devenus **« type de tender »**, pour ne pas les confondre avec les sous-systèmes (SIG, TRK, SEN…). C'est une interprétation de DEC-126 à confirmer.
- **Le niveau intermédiaire du PBS** dans le classeur de clés (`2.1` IXL…) s'appelait « sous-système ». Il est renommé **« sous-ensemble »** dans KEYS.md et dans la story US-ALM concernée. Ce nom est un choix de rédaction, pas un terme du classeur.
- **« Staffing ».** Là où « casting » désignait l'ensemble des personnes staffées, les specs disent maintenant « staffing ». C'est le cas par exemple de « Staffing incomplet » dans PLATFORM.md.
- **Les régions de démo** des cinq tenders (FR, NAM, LAM…) sont arbitraires.
- **La région dans Configuration.** Elle est modifiable dans la maquette, mais non branchée, comme les autres champs de General. La règle (modifiable ou fixée à la création) reste à décider.
- **« PIC » dans les phrases.** Le verbe « assigned » reste dans les phrases (« No one assigned yet », « {ID} assigned to {nom} »). Seul le libellé du champ devient « PIC ».
