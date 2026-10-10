# User stories de SRM

Backlog complet du produit, réécrit le 10 octobre 2026 à partir des décisions DEC-001 à DEC-125 et des règles de `docs/current/`, avec la maquette comme référence visuelle (`main` du 10 octobre). Il remplace le backlog extrait de la maquette le 17 septembre, archivé dans [docs/archive/stories-2026-09-17/](../archive/stories-2026-09-17/STORIES-extracted-from-prototype.md).

## Comment lire une story

Chaque story suit les « 3 C » — **Carte** (qui, quoi, pourquoi), **Conversation** (l'intention, le contexte, les cas limites), **Confirmation** (les critères d'acceptation) — et les critères INVEST : indépendante, négociable, utile, estimable, petite (un sprint), testable.

```
### US-XXX-NN — titre
**Carte :** En tant que <rôle>, je veux <action>, afin de <bénéfice>.
**Conversation :** intention, contexte, inclus / exclu, cas limites, différence Turnkey / SIG.
**Maquette :** l'écran et la zone de la maquette (fichier, route, composant de COMPONENTS.md), ou « non maquetté ».
**Règles :** les décisions et règles que la story met en œuvre  ·  **Périmètre :** Pilote 1 | Après pilote  ·  **Variantes :** Toutes | Turnkey | SIG…
**Critères d'acceptation :** 4 à 6 faits observables et testables.
Écart maquette : ce que la maquette fait autrement ou simule (la story décrit la cible, pas la maquette).
Point ouvert : ce qui n'est pas décidé (la story ne le tranche pas).
```

- **Autorité.** Une story résume la valeur et rend la règle testable ; en cas de doute, la règle de `docs/current/` et la décision la plus récente (`docs/current/OPEN-QUESTIONS.md`) font foi. Les lignes de `docs/current/` restées en retard sur les décisions sont listées dans [POINTS-OUVERTS.md](POINTS-OUVERTS.md).
- **Rôles.** *Chef de projet* : membre de l'équipe de gestion du tender (plusieurs par tender). *Contributeur* : personne rattachée à **un** système, qui lit tout le tender et ne modifie que son système. Admin et VIP ne sont pas détaillés (OPEN-02).
- **Vocabulaire.** *Système* (jamais « activité ») ; *organisation (OBS)* ; *allocation* = une organisation + la personne qui en répond ; *affectation* (Compliance) ; libellés d'écran en anglais, entre guillemets, tels qu'affichés.
- **Périmètre.** *Pilote 1* : de la création à la validation de l'allocation, pour Turnkey, SIG, Mainline et RSC (DEC-022). *Après pilote* : Compliance, versions, Q&A, risques, statistiques de conformité. « (à confirmer) » quand la borne n'est pas dite.
- **Variantes.** Turnkey, SIG (autonome), Mainline (tender SIG de produit Mainline), RSC. Un tender SIG n'est pas un Turnkey filtré.

## Épopées

| # | Épopée | Fichier | Stories | Pilote 1 | Après pilote |
|---|---|---|---|---|---|
| 1 | Accueil (My tenders) (`US-HOME`) | [01-accueil.md](01-accueil.md) | 6 | 6 | 0 |
| 2 | Création d'un tender (`US-NEW`) | [02-creation.md](02-creation.md) | 9 | 9 | 0 |
| 3 | Documents et versions (`US-DOC`) | [03-documents.md](03-documents.md) | 8 | 6 | 2 |
| 4 | Capture, segmentation, traduction et IA (`US-CAP`) | [04-capture-ia.md](04-capture-ia.md) | 13 | 11 | 2 |
| 5 | Allocation — modèle et panneau (`US-ALM`) | [05-allocation.md](05-allocation.md) | 35 | 33 | 2 |
| 6 | Tables communes Allocation et Compliance (`US-TAB`) | [06-tables.md](06-tables.md) | 26 | 25 | 1 |
| 7 | Vue Document d'Allocation (`US-DOCV`) | [07-vue-document.md](07-vue-document.md) | 9 | 5 | 4 |
| 8 | Changements de version côté Allocation (`US-CHG`) | [08-changements.md](08-changements.md) | 6 | 0 | 6 |
| 9 | Compliance (`US-CMP`) | [09-compliance.md](09-compliance.md) | 28 | 0 | 28 |
| 10 | Stratégies d'écart, conformité externe et risques (`US-RSK`) | [10-risques.md](10-risques.md) | 13 | 0 | 13 |
| 11 | Registre Q&A avec le client (`US-QA`) | [11-qa.md](11-qa.md) | 11 | 0 | 11 |
| 12 | Team casting et droits (`US-TEAM`) | [12-casting-droits.md](12-casting-droits.md) | 17 | 15 | 2 |
| 13 | Tableau de bord du tender (`US-DASH`) | [13-tableau-de-bord.md](13-tableau-de-bord.md) | 15 | 8 | 7 |
| 14 | Statistiques (`US-STAT`) | [14-statistiques.md](14-statistiques.md) | 14 | 8 | 6 |
| 15 | Configuration du tender (`US-CFG`) | [15-configuration.md](15-configuration.md) | 15 | 12 | 3 |
| 16 | Transverse : journal, notifications, plateforme (`US-X`) | [16-transverse.md](16-transverse.md) | 14 | 14 | 0 |
| | **Total** | | **239** | **152** | **87** |

Les stories marquées « Pilote 1 » mais dont une partie (Compliance) vient après le pilote sont comptées en Pilote 1. Matrice règle → stories : [COUVERTURE.md](COUVERTURE.md). Points non décidés et écarts de la maquette : [POINTS-OUVERTS.md](POINTS-OUVERTS.md).

## Index

### Accueil (My tenders)

| Story | Titre | Périmètre | Variantes |
|---|---|---|---|
| [US-HOME-01](01-accueil.md#us-home-01--être-accueilli-et-orienté-dès-larrivée) | Être accueilli et orienté dès l'arrivée | Pilote 1 (à confirmer) | Toutes |
| [US-HOME-02](01-accueil.md#us-home-02--reprendre-le-tender-en-cours) | Reprendre le tender en cours | Pilote 1 (à confirmer) | Toutes |
| [US-HOME-03](01-accueil.md#us-home-03--comprendre-comment-un-tender-traverse-srm) | Comprendre comment un tender traverse SRM | Pilote 1 (à confirmer) | Toutes |
| [US-HOME-04](01-accueil.md#us-home-04--voir-la-liste-de-mes-tenders) | Voir la liste de mes tenders | Pilote 1 | Toutes |
| [US-HOME-05](01-accueil.md#us-home-05--lire-lavancement-dun-tender-sur-sa-ligne) | Lire l'avancement d'un tender sur sa ligne | Pilote 1 (à confirmer) | Toutes |
| [US-HOME-06](01-accueil.md#us-home-06--ouvrir-un-tender-depuis-laccueil) | Ouvrir un tender depuis l'accueil | Pilote 1 | Toutes |

### Création d'un tender

| Story | Titre | Périmètre | Variantes |
|---|---|---|---|
| [US-NEW-01](02-creation.md#us-new-01--décrire-lidentité-du-tender) | Décrire l'identité du tender | Pilote 1 | Toutes |
| [US-NEW-02](02-creation.md#us-new-02--choisir-la-ligne-produit-fixée-à-la-création) | Choisir la ligne produit, fixée à la création | Pilote 1 | Turnkey, SIG (dont Mainline), RSC |
| [US-NEW-03](02-creation.md#us-new-03--choisir-le-produit-ou-la-combinaison-dun-turnkey) | Choisir le produit, ou la combinaison d'un Turnkey | Pilote 1 | Turnkey (combinaison), SIG (dont Mainline), RSC |
| [US-NEW-04](02-creation.md#us-new-04--déclarer-la-langue-source-unique-du-tender) | Déclarer la langue source unique du tender | Pilote 1 | Toutes |
| [US-NEW-05](02-creation.md#us-new-05--joindre-et-ordonner-les-documents-source) | Joindre et ordonner les documents source | Pilote 1 | Toutes |
| [US-NEW-06](02-creation.md#us-new-06--choisir-le-mode-dassistance-ia-fixé-à-la-création) | Choisir le mode d'assistance IA, fixé à la création | Pilote 1 | Toutes |
| [US-NEW-07](02-creation.md#us-new-07--constituer-léquipe-de-gestion-du-projet) | Constituer l'équipe de gestion du projet | Pilote 1 | Toutes |
| [US-NEW-08](02-creation.md#us-new-08--vérifier-le-récapitulatif-et-créer-le-tender) | Vérifier le récapitulatif et créer le tender | Pilote 1 | Toutes |
| [US-NEW-09](02-creation.md#us-new-09--retrouver-dans-le-tender-créé-tout-ce-que-lassistant-a-fixé) | Retrouver dans le tender créé tout ce que l'assistant a fixé | Pilote 1 | Turnkey, SIG (dont Mainline), RSC |

### Documents et versions

| Story | Titre | Périmètre | Variantes |
|---|---|---|---|
| [US-DOC-01](03-documents.md#us-doc-01--voir-les-documents-du-tender-dans-leur-ordre-de-lecture) | Voir les documents du tender dans leur ordre de lecture | Pilote 1 | Toutes |
| [US-DOC-02](03-documents.md#us-doc-02--consulter-lhistorique-des-versions-dun-document) | Consulter l'historique des versions d'un document | Après pilote | Toutes |
| [US-DOC-03](03-documents.md#us-doc-03--réordonner-les-documents-du-tender) | Réordonner les documents du tender | Pilote 1 | Toutes |
| [US-DOC-04](03-documents.md#us-doc-04--téléverser-une-nouvelle-version-dun-document) | Téléverser une nouvelle version d'un document | Après pilote | Toutes |
| [US-DOC-05](03-documents.md#us-doc-05--retirer-un-document-en-annonçant-ce-qui-sera-perdu) | Retirer un document en annonçant ce qui sera perdu | Pilote 1 (à confirmer) | Toutes |
| [US-DOC-06](03-documents.md#us-doc-06--ajouter-un-document-en-cours-de-tender) | Ajouter un document en cours de tender | Pilote 1 | Toutes |
| [US-DOC-07](03-documents.md#us-doc-07--exporter-les-exigences-dun-seul-document) | Exporter les exigences d'un seul document | Pilote 1 (à confirmer) | Toutes |
| [US-DOC-08](03-documents.md#us-doc-08--réserver-la-gestion-des-documents-à-léquipe-de-gestion-du-projet) | Réserver la gestion des documents à l'équipe de gestion du projet | Pilote 1 | Toutes ; Turnkey (contributeur du système SIG) |

### Capture, segmentation, traduction et IA

| Story | Titre | Périmètre | Variantes |
|---|---|---|---|
| [US-CAP-01](04-capture-ia.md#us-cap-01--enchaîner-automatiquement-les-étapes-ia-activées) | Enchaîner automatiquement les étapes IA activées | Pilote 1 | Toutes (étape d'allocation selon le type) |
| [US-CAP-02](04-capture-ia.md#us-cap-02--régler-la-conversion-du-document-source) | Régler la conversion du document source | Pilote 1 (à confirmer) | Toutes |
| [US-CAP-03](04-capture-ia.md#us-cap-03--découper-chaque-document-en-blocs-heading-information-ou-requirement) | Découper chaque document en blocs Heading, Information ou Requirement | Pilote 1 | Toutes |
| [US-CAP-04](04-capture-ia.md#us-cap-04--capturer-les-images-sans-en-lire-le-contenu) | Capturer les images sans en lire le contenu | Pilote 1 | Toutes |
| [US-CAP-05](04-capture-ia.md#us-cap-05--signaler-une-découpe-incertaine) | Signaler une découpe incertaine | Pilote 1 (à confirmer) | Toutes |
| [US-CAP-06](04-capture-ia.md#us-cap-06--écarter-un-bloc-capturé-par-erreur-sans-le-supprimer) | Écarter un bloc capturé par erreur sans le supprimer | Pilote 1 | Toutes |
| [US-CAP-07](04-capture-ia.md#us-cap-07--traduire-automatiquement-vers-langlais-de-travail) | Traduire automatiquement vers l'anglais de travail | Pilote 1 | Toutes |
| [US-CAP-08](04-capture-ia.md#us-cap-08--corriger-une-traduction-ce-qui-remet-lexigence-en-revue) | Corriger une traduction, ce qui remet l'exigence en revue | Pilote 1 | Toutes (tenders de langue source non anglaise) |
| [US-CAP-09](04-capture-ia.md#us-cap-09--caractériser-chaque-bloc-avec-un-niveau-de-confiance-low-medium-ou-high) | Caractériser chaque bloc avec un niveau de confiance Low, Medium ou High | Pilote 1 | Toutes |
| [US-CAP-10](04-capture-ia.md#us-cap-10--dire-quaucun-modèle-ne-sapplique-sans-en-emprunter-un-en-silence) | Dire qu'aucun modèle ne s'applique, sans en emprunter un en silence | Pilote 1 | RSC et toute ligne sans modèle fourni ; Turnkey pour ses systèmes sans modèle (voir US-ALM-20) |
| [US-CAP-11](04-capture-ia.md#us-cap-11--reprendre-un-traitement-interrompu-sans-doublon) | Reprendre un traitement interrompu sans doublon | Pilote 1 (à confirmer) | Toutes |
| [US-CAP-12](04-capture-ia.md#us-cap-12--relancer-automatiquement-les-modèles-sur-les-seules-exigences-modifiées-par-une-nouvelle-version) | Relancer automatiquement les modèles sur les seules exigences modifiées par une nouvelle version | Après pilote | Toutes (SIG : jamais de passe 1 Turnkey) |
| [US-CAP-13](04-capture-ia.md#us-cap-13--repartir-de-zéro-sur-une-exigence-issue-dune-fusion-ou-dune-scission) | Repartir de zéro sur une exigence issue d'une fusion ou d'une scission | Après pilote | Toutes |

### Allocation — modèle et panneau

| Story | Titre | Périmètre | Variantes |
|---|---|---|---|
| [US-ALM-01](05-allocation.md#us-alm-01--lire-le-statut-dune-exigence) | Lire le statut d'une exigence | Pilote 1 | Toutes |
| [US-ALM-02](05-allocation.md#us-alm-02--savoir-pourquoi-une-exigence-est-à-revoir) | Savoir pourquoi une exigence est à revoir | Pilote 1 | Toutes (motif « System » : Turnkey) |
| [US-ALM-03](05-allocation.md#us-alm-03--suivre-lavancement-dans-la-barre-de-statut) | Suivre l'avancement dans la barre de statut | Pilote 1 | Toutes |
| [US-ALM-04](05-allocation.md#us-alm-04--corriger-la-nature-et-la-classe-dune-exigence) | Corriger la nature et la classe d'une exigence | Pilote 1 | Toutes |
| [US-ALM-05](05-allocation.md#us-alm-05--voir-le-niveau-de-confiance-de-lia-sur-la-nature-et-la-classe) | Voir le niveau de confiance de l'IA sur la nature et la classe | Pilote 1 | Toutes |
| [US-ALM-06](05-allocation.md#us-alm-06--réserver-la-nature-et-la-classe-au-chef-de-projet) | Réserver la nature et la classe au chef de projet | Pilote 1 | Toutes |
| [US-ALM-07](05-allocation.md#us-alm-07--voir-vers-quels-systèmes-un-turnkey-a-aiguillé-une-exigence) | Voir vers quels systèmes un Turnkey a aiguillé une exigence | Pilote 1 | Turnkey |
| [US-ALM-08](05-allocation.md#us-alm-08--ajouter-ou-retirer-un-système) | Ajouter ou retirer un système | Pilote 1 | Turnkey |
| [US-ALM-09](05-allocation.md#us-alm-09--attribuer-une-exigence-à-un-partenaire-externe) | Attribuer une exigence à un partenaire externe | Pilote 1 (à confirmer) | Turnkey |
| [US-ALM-10](05-allocation.md#us-alm-10--proposer-un-système-manquant) | Proposer un système manquant | Pilote 1 | Turnkey |
| [US-ALM-11](05-allocation.md#us-alm-11--suivre-une-exigence-répartie-sur-plusieurs-systèmes) | Suivre une exigence répartie sur plusieurs systèmes | Pilote 1 | Turnkey |
| [US-ALM-12](05-allocation.md#us-alm-12--travailler-dans-le-détail-dun-système-dun-turnkey) | Travailler dans le détail d'un système d'un Turnkey | Pilote 1 | Turnkey |
| [US-ALM-13](05-allocation.md#us-alm-13--allouer-sur-un-tender-sig-autonome-sans-axe-système) | Allouer sur un tender SIG autonome, sans axe système | Pilote 1 | SIG (Mainline compris) |
| [US-ALM-14](05-allocation.md#us-alm-14--corriger-la-chaîne-abs--pbs--obs) | Corriger la chaîne ABS → PBS → OBS | Pilote 1 | Toutes (Turnkey : dans le détail de chaque système) |
| [US-ALM-15](05-allocation.md#us-alm-15--gérer-les-organisations-obs-dun-système) | Gérer les organisations (OBS) d'un système | Pilote 1 | Toutes |
| [US-ALM-16](05-allocation.md#us-alm-16--choisir-abs-pbs-et-rôle-dans-les-listes-des-clés) | Choisir ABS, PBS et rôle dans les listes des clés | Pilote 1 | Mainline (Wayside, Onboard) |
| [US-ALM-17](05-allocation.md#us-alm-17--alimenter-les-listes-depuis-le-classeur-de-clés-de-référence) | Alimenter les listes depuis le classeur de clés de référence | Pilote 1 | Mainline (Wayside, Onboard) |
| [US-ALM-18](05-allocation.md#us-alm-18--désigner-la-personne-de-chaque-organisation) | Désigner la personne de chaque organisation | Pilote 1 | Toutes |
| [US-ALM-19](05-allocation.md#us-alm-19--valider-sans-avoir-désigné-de-personne) | Valider sans avoir désigné de personne | Pilote 1 | Toutes |
| [US-ALM-20](05-allocation.md#us-alm-20--allouer-à-la-main-un-système-sans-modèle) | Allouer à la main un système sans modèle | Pilote 1 | Turnkey (systèmes sans modèle) ; RSC selon sa configuration |
| [US-ALM-21](05-allocation.md#us-alm-21--relancer-le-modèle-dallocation-sur-une-exigence) | Relancer le modèle d'allocation sur une exigence | Pilote 1 | Toutes (Turnkey : par système) |
| [US-ALM-22](05-allocation.md#us-alm-22--emprunter-le-modèle-dun-autre-système) | Emprunter le modèle d'un autre système | Pilote 1 | Toutes (cas principal : systèmes sans modèle d'un Turnkey) |
| [US-ALM-23](05-allocation.md#us-alm-23--comprendre-pourquoi-une-relance-est-bloquée) | Comprendre pourquoi une relance est bloquée | Après pilote | Toutes |
| [US-ALM-24](05-allocation.md#us-alm-24--relancer-le-modèle-sur-une-sélection-dexigences) | Relancer le modèle sur une sélection d'exigences | Pilote 1 | Toutes |
| [US-ALM-25](05-allocation.md#us-alm-25--relancer-après-un-changement-de-nature-ou-de-classe) | Relancer après un changement de nature ou de classe | Pilote 1 | Toutes |
| [US-ALM-26](05-allocation.md#us-alm-26--valider-une-exigence-en-un-seul-geste) | Valider une exigence en un seul geste | Pilote 1 | SIG (Mainline compris), RSC ; Turnkey : US-ALM-27 et US-ALM-28 |
| [US-ALM-27](05-allocation.md#us-alm-27--valider-laiguillage-dune-exigence-turnkey) | Valider l'aiguillage d'une exigence Turnkey | Pilote 1 | Turnkey |
| [US-ALM-28](05-allocation.md#us-alm-28--valider-lallocation-dun-système-dun-turnkey) | Valider l'allocation d'un système d'un Turnkey | Pilote 1 | Turnkey |
| [US-ALM-29](05-allocation.md#us-alm-29--demander-une-réallocation) | Demander une réallocation | Pilote 1 | Toutes (motifs « système » : Turnkey) |
| [US-ALM-30](05-allocation.md#us-alm-30--traiter-une-demande-de-réallocation) | Traiter une demande de réallocation | Pilote 1 | Toutes |
| [US-ALM-31](05-allocation.md#us-alm-31--travailler-sur-son-système-vue-du-contributeur) | Travailler sur son système (vue du contributeur) | Pilote 1 | Toutes |
| [US-ALM-32](05-allocation.md#us-alm-32--lire-en-lecture-seule-une-exigence-dun-autre-système) | Lire en lecture seule une exigence d'un autre système | Pilote 1 | Toutes |
| [US-ALM-33](05-allocation.md#us-alm-33--lire-tout-le-tender) | Lire tout le tender | Pilote 1 | Toutes |
| [US-ALM-34](05-allocation.md#us-alm-34--lire-la-conformité-dans-allocation-sans-la-saisir) | Lire la conformité dans Allocation sans la saisir | Après pilote | Toutes |
| [US-ALM-35](05-allocation.md#us-alm-35--inscrire-les-actions-dallocation-au-journal-de-lexigence) | Inscrire les actions d'allocation au journal de l'exigence | Pilote 1 (à confirmer) | Toutes |

### Tables communes Allocation et Compliance

| Story | Titre | Périmètre | Variantes |
|---|---|---|---|
| [US-TAB-01](06-tables.md#us-tab-01--lire-la-table-dans-lordre-du-document) | Lire la table dans l'ordre du document | Pilote 1 (Allocation) ; Compliance : après pilote | Toutes |
| [US-TAB-02](06-tables.md#us-tab-02--déplier-une-exigence-en-lignes-par-système-et-par-organisation) | Déplier une exigence en lignes par système et par organisation | Pilote 1 (Allocation) ; Compliance : après pilote | Toutes |
| [US-TAB-03](06-tables.md#us-tab-03--filtrer-dun-clic-sur-un-compteur-de-statut) | Filtrer d'un clic sur un compteur de statut | Pilote 1 (Allocation) ; Compliance : après pilote | Toutes |
| [US-TAB-04](06-tables.md#us-tab-04--rechercher-une-exigence-par-son-identifiant-ou-son-texte) | Rechercher une exigence par son identifiant ou son texte | Pilote 1 (Allocation) ; Compliance : après pilote | Toutes |
| [US-TAB-05](06-tables.md#us-tab-05--trier-par-un-en-tête-de-colonne) | Trier par un en-tête de colonne | Pilote 1 (Allocation) ; Compliance : après pilote | Toutes |
| [US-TAB-06](06-tables.md#us-tab-06--filtrer-une-colonne-comme-dans-excel) | Filtrer une colonne comme dans Excel | Pilote 1 (Allocation) ; Compliance : après pilote | Toutes (sur SIG, pas de filtre System) |
| [US-TAB-07](06-tables.md#us-tab-07--construire-un-filtre-avancé) | Construire un filtre avancé | Pilote 1 (Allocation) ; Compliance : après pilote | Toutes |
| [US-TAB-08](06-tables.md#us-tab-08--lire-en-clair-ce-qui-filtre-la-table-et-tout-effacer) | Lire en clair ce qui filtre la table et tout effacer | Pilote 1 (Allocation) ; Compliance : après pilote | Toutes |
| [US-TAB-09](06-tables.md#us-tab-09--enregistrer-un-filtre-et-le-réutiliser-sur-un-autre-tender) | Enregistrer un filtre et le réutiliser sur un autre tender | Pilote 1 (Allocation) ; Compliance : après pilote | Toutes |
| [US-TAB-10](06-tables.md#us-tab-10--afficher-le-texte-complet-des-exigences) | Afficher le texte complet des exigences | Pilote 1 (Allocation) ; Compliance : après pilote | Toutes |
| [US-TAB-11](06-tables.md#us-tab-11--choisir-masquer-et-réordonner-les-colonnes) | Choisir, masquer et réordonner les colonnes | Pilote 1 (Allocation) ; Compliance : après pilote | Toutes (sur SIG, pas de « Group by » System) |
| [US-TAB-12](06-tables.md#us-tab-12--redimensionner-les-colonnes) | Redimensionner les colonnes | Pilote 1 (Allocation) ; Compliance : après pilote | Toutes |
| [US-TAB-13](06-tables.md#us-tab-13--sélectionner-plusieurs-lignes-et-agir-en-une-fois) | Sélectionner plusieurs lignes et agir en une fois | Pilote 1 (Allocation) ; Compliance : après pilote | Toutes |
| [US-TAB-14](06-tables.md#us-tab-14--ne-montrer-que-les-lignes-sélectionnées) | Ne montrer que les lignes sélectionnées | Pilote 1 (Allocation) ; Compliance : après pilote | Toutes |
| [US-TAB-15](06-tables.md#us-tab-15--se-déplacer-et-sélectionner-au-clavier) | Se déplacer et sélectionner au clavier | Pilote 1 (Allocation) ; Compliance : après pilote | Toutes |
| [US-TAB-16](06-tables.md#us-tab-16--éditer-une-cellule-au-clavier) | Éditer une cellule au clavier | Pilote 1 (Allocation) ; Compliance : après pilote | Toutes |
| [US-TAB-17](06-tables.md#us-tab-17--aller-à-la-prochaine-exigence-qui-mattend-et-valider-au-clavier) | Aller à la prochaine exigence qui m'attend et valider au clavier | Pilote 1 (Allocation) ; Compliance : après pilote | Toutes |
| [US-TAB-18](06-tables.md#us-tab-18--annuler-la-dernière-action-même-après-le-message) | Annuler la dernière action, même après le message | Pilote 1 (Allocation) ; Compliance : après pilote | Toutes |
| [US-TAB-19](06-tables.md#us-tab-19--consulter-laide-clavier-au-survol) | Consulter l'aide clavier au survol | Pilote 1 (Allocation) ; Compliance : après pilote | Toutes |
| [US-TAB-20](06-tables.md#us-tab-20--créer-une-colonne-personnalisée) | Créer une colonne personnalisée | Pilote 1 (à confirmer) ; Compliance : après pilote | Toutes |
| [US-TAB-21](06-tables.md#us-tab-21--remplir-une-colonne-personnalisée) | Remplir une colonne personnalisée | Pilote 1 (à confirmer) ; Compliance : après pilote | Toutes |
| [US-TAB-22](06-tables.md#us-tab-22--retrouver-une-colonne-personnalisée-sur-lautre-écran) | Retrouver une colonne personnalisée sur l'autre écran | Après pilote | Toutes |
| [US-TAB-23](06-tables.md#us-tab-23--filtrer-et-trier-sur-une-colonne-personnalisée) | Filtrer et trier sur une colonne personnalisée | Pilote 1 (à confirmer) ; Compliance : après pilote | Toutes |
| [US-TAB-24](06-tables.md#us-tab-24--modifier-une-colonne-personnalisée) | Modifier une colonne personnalisée | Pilote 1 (à confirmer) ; Compliance : après pilote | Toutes |
| [US-TAB-25](06-tables.md#us-tab-25--supprimer-une-colonne-personnalisée) | Supprimer une colonne personnalisée | Pilote 1 (à confirmer) ; Compliance : après pilote | Toutes |
| [US-TAB-26](06-tables.md#us-tab-26--garder-les-colonnes-personnalisées-hors-de-lexport-client) | Garder les colonnes personnalisées hors de l'export client | Pilote 1 (à confirmer) ; Compliance : après pilote | Toutes |

### Vue Document d'Allocation

| Story | Titre | Périmètre | Variantes |
|---|---|---|---|
| [US-DOCV-01](07-vue-document.md#us-docv-01--lire-le-tender-sous-forme-de-document) | Lire le tender sous forme de document | Pilote 1 | Toutes |
| [US-DOCV-02](07-vue-document.md#us-docv-02--naviguer-dans-le-plan-du-tender) | Naviguer dans le plan du tender | Pilote 1 | Toutes |
| [US-DOCV-03](07-vue-document.md#us-docv-03--ouvrir-le-détail-dun-bloc-depuis-le-document) | Ouvrir le détail d'un bloc depuis le document | Pilote 1 | Toutes |
| [US-DOCV-04](07-vue-document.md#us-docv-04--voir-la-nature-de-chaque-bloc-et-le-doute-de-lia) | Voir la nature de chaque bloc et le doute de l'IA | Pilote 1 | Toutes |
| [US-DOCV-05](07-vue-document.md#us-docv-05--reclasser-ou-confirmer-un-bloc-sur-place) | Reclasser ou confirmer un bloc sur place | Pilote 1 | Toutes |
| [US-DOCV-06](07-vue-document.md#us-docv-06--comparer-un-document-à-une-version-antérieure-onglet-changes) | Comparer un document à une version antérieure (onglet Changes) | Après pilote | Toutes |
| [US-DOCV-07](07-vue-document.md#us-docv-07--lire-chaque-changement-et-son-effet-sur-le-travail-déjà-fait) | Lire chaque changement et son effet sur le travail déjà fait | Après pilote | Toutes |
| [US-DOCV-08](07-vue-document.md#us-docv-08--filtrer-les-changements-et-les-parcourir-au-clavier) | Filtrer les changements et les parcourir au clavier | Après pilote | Toutes |
| [US-DOCV-09](07-vue-document.md#us-docv-09--lire-le-document-sur-le-pdf-original) | Lire le document sur le PDF original | Après pilote | Toutes |

### Changements de version côté Allocation

| Story | Titre | Périmètre | Variantes |
|---|---|---|---|
| [US-CHG-01](08-changements.md#us-chg-01--revoir-une-exigence-ajoutée-ou-modifiée-par-une-nouvelle-version) | Revoir une exigence ajoutée ou modifiée par une nouvelle version | Après pilote | Toutes |
| [US-CHG-02](08-changements.md#us-chg-02--lire-les-changements-dans-la-colonne-changes) | Lire les changements dans la colonne Changes | Après pilote | Toutes |
| [US-CHG-03](08-changements.md#us-chg-03--choisir-la-version-de-comparaison-ligne-par-ligne-ou-pour-toutes) | Choisir la version de comparaison, ligne par ligne ou pour toutes | Après pilote | Toutes |
| [US-CHG-04](08-changements.md#us-chg-04--filtrer-sur-les-changements-et-afficher-la-colonne-avec-c) | Filtrer sur les changements et afficher la colonne avec C | Après pilote | Toutes |
| [US-CHG-05](08-changements.md#us-chg-05--consulter-longlet-versions-dune-exigence-changée) | Consulter l'onglet Versions d'une exigence changée | Après pilote | Toutes |
| [US-CHG-06](08-changements.md#us-chg-06--consulter-une-exigence-supprimée-par-une-nouvelle-version) | Consulter une exigence supprimée par une nouvelle version | Après pilote | Toutes |

### Compliance

| Story | Titre | Périmètre | Variantes |
|---|---|---|---|
| [US-CMP-01](09-compliance.md#us-cmp-01--créer-les-affectations-quand-lallocation-est-validée) | Créer les affectations quand l'allocation est validée | Après pilote | Toutes |
| [US-CMP-02](09-compliance.md#us-cmp-02--suivre-lavancement-dune-affectation-par-son-statut) | Suivre l'avancement d'une affectation par son statut | Après pilote | Toutes |
| [US-CMP-03](09-compliance.md#us-cmp-03--lire-les-colonnes-de-la-table-compliance) | Lire les colonnes de la table Compliance | Après pilote | Toutes |
| [US-CMP-04](09-compliance.md#us-cmp-04--déplier-une-exigence-en-systèmes-et-en-organisations) | Déplier une exigence en systèmes et en organisations | Après pilote | Toutes |
| [US-CMP-05](09-compliance.md#us-cmp-05--lire-la-table-dans-lordre-du-document) | Lire la table dans l'ordre du document | Après pilote | Toutes |
| [US-CMP-06](09-compliance.md#us-cmp-06--lire-la-conformité-sur-le-document) | Lire la conformité sur le document | Après pilote | Toutes |
| [US-CMP-07](09-compliance.md#us-cmp-07--suivre-lavancement-de-la-consolidation) | Suivre l'avancement de la consolidation | Après pilote | Toutes |
| [US-CMP-08](09-compliance.md#us-cmp-08--consulter-tout-le-tender-et-nagir-que-sur-son-système) | Consulter tout le tender et n'agir que sur son système | Après pilote | Toutes |
| [US-CMP-09](09-compliance.md#us-cmp-09--arriver-sur-sa-file-et-la-parcourir) | Arriver sur sa file et la parcourir | Après pilote | Toutes |
| [US-CMP-10](09-compliance.md#us-cmp-10--lire-lexigence-en-entier-dans-le-panneau-de-décision) | Lire l'exigence en entier dans le panneau de décision | Après pilote | Toutes |
| [US-CMP-11](09-compliance.md#us-cmp-11--rendre-un-verdict--choisir-puis-confirmer) | Rendre un verdict : choisir, puis confirmer | Après pilote | Toutes |
| [US-CMP-12](09-compliance.md#us-cmp-12--qualifier-un-not-compliant-par-category-et-topic-sur-un-tender-turnkey) | Qualifier un Not compliant par Category et Topic sur un tender Turnkey | Après pilote | Turnkey |
| [US-CMP-13](09-compliance.md#us-cmp-13--retrouver-son-brouillon-de-verdict) | Retrouver son brouillon de verdict | Après pilote | Toutes |
| [US-CMP-14](09-compliance.md#us-cmp-14--mettre-une-affectation-de-côté) | Mettre une affectation de côté | Après pilote | Toutes |
| [US-CMP-15](09-compliance.md#us-cmp-15--consulter-les-questions-et-les-exigences-similaires) | Consulter les questions et les exigences similaires | Après pilote | Toutes |
| [US-CMP-16](09-compliance.md#us-cmp-16--poser-une-question-au-client-depuis-une-affectation) | Poser une question au client depuis une affectation | Après pilote | Toutes |
| [US-CMP-17](09-compliance.md#us-cmp-17--suivre-dans-compliance-létat-des-questions-et-la-réponse-du-client) | Suivre dans Compliance l'état des questions et la réponse du client | Après pilote | Toutes |
| [US-CMP-18](09-compliance.md#us-cmp-18--refuser-une-question-sur-une-affectation-déjà-répondue) | Refuser une question sur une affectation déjà répondue | Après pilote | Toutes |
| [US-CMP-19](09-compliance.md#us-cmp-19--renvoyer-une-affectation-qui-nest-pas-la-sienne) | Renvoyer une affectation qui n'est pas la sienne | Après pilote | Toutes |
| [US-CMP-20](09-compliance.md#us-cmp-20--consolider-les-verdicts-dune-exigence) | Consolider les verdicts d'une exigence | Après pilote | Toutes |
| [US-CMP-21](09-compliance.md#us-cmp-21--mettre-en-avant-ce-qui-est-dû) | Mettre en avant ce qui est dû | Après pilote | Toutes |
| [US-CMP-22](09-compliance.md#us-cmp-22--voir-ce-qui-est-attendu-dans-le-panneau-du-chef-de-projet) | Voir ce qui est attendu dans le panneau du chef de projet | Après pilote | Toutes |
| [US-CMP-23](09-compliance.md#us-cmp-23--réaffecter-une-affectation-renvoyée) | Réaffecter une affectation renvoyée | Après pilote | Toutes |
| [US-CMP-24](09-compliance.md#us-cmp-24--relancer-le-contributeur-dune-affectation-due) | Relancer le contributeur d'une affectation due | Après pilote | Toutes |
| [US-CMP-25](09-compliance.md#us-cmp-25--saisir-ou-modifier-une-réponse-en-tant-que-chef-de-projet) | Saisir ou modifier une réponse en tant que chef de projet | Après pilote | Toutes |
| [US-CMP-26](09-compliance.md#us-cmp-26--voir-dans-la-cloche-ce-qui-attend) | Voir dans la cloche ce qui attend | Après pilote | Toutes |
| [US-CMP-27](09-compliance.md#us-cmp-27--rouvrir-les-verdicts-dune-exigence-modifiée-par-une-nouvelle-version) | Rouvrir les verdicts d'une exigence modifiée par une nouvelle version | Après pilote | Toutes |
| [US-CMP-28](09-compliance.md#us-cmp-28--exporter-le-registre-de-conformité-avec-options) | Exporter le registre de conformité avec options | Après pilote | Toutes |

### Stratégies d'écart, conformité externe et risques

| Story | Titre | Périmètre | Variantes |
|---|---|---|---|
| [US-RSK-01](10-risques.md#us-rsk-01--écrire-les-stratégies-décart-du-tender) | Écrire les stratégies d'écart du tender | Après pilote | Toutes |
| [US-RSK-02](10-risques.md#us-rsk-02--renommer-ou-supprimer-une-stratégie-décart) | Renommer ou supprimer une stratégie d'écart | Après pilote | Toutes |
| [US-RSK-03](10-risques.md#us-rsk-03--changer-le-résultat-dune-stratégie-déjà-utilisée) | Changer le résultat d'une stratégie déjà utilisée | Après pilote | Toutes |
| [US-RSK-04](10-risques.md#us-rsk-04--choisir-une-stratégie-décart-après-un-not-compliant) | Choisir une stratégie d'écart après un Not compliant | Après pilote | Toutes |
| [US-RSK-05](10-risques.md#us-rsk-05--lier-un-risque-existant-à-un-not-compliant) | Lier un risque existant à un Not compliant | Après pilote | Toutes |
| [US-RSK-06](10-risques.md#us-rsk-06--créer-un-risque-quand-aucun-ne-convient) | Créer un risque quand aucun ne convient | Après pilote | Toutes |
| [US-RSK-07](10-risques.md#us-rsk-07--enregistrer-un-not-compliant-sans-stratégie-ni-risque-en-le-signalant) | Enregistrer un Not compliant sans stratégie ni risque, en le signalant | Après pilote | Toutes |
| [US-RSK-08](10-risques.md#us-rsk-08--dériver-la-conformité-externe-dune-affectation) | Dériver la conformité externe d'une affectation | Après pilote | Toutes |
| [US-RSK-09](10-risques.md#us-rsk-09--consolider-la-conformité-externe-dune-exigence) | Consolider la conformité externe d'une exigence | Après pilote | Toutes |
| [US-RSK-10](10-risques.md#us-rsk-10--corriger-la-conformité-externe-dune-affectation) | Corriger la conformité externe d'une affectation | Après pilote | Toutes |
| [US-RSK-11](10-risques.md#us-rsk-11--consulter-la-liste-des-risques-du-tender) | Consulter la liste des risques du tender | Après pilote | Toutes |
| [US-RSK-12](10-risques.md#us-rsk-12--passer-dun-risque-à-ses-exigences-et-inversement) | Passer d'un risque à ses exigences, et inversement | Après pilote | Toutes |
| [US-RSK-13](10-risques.md#us-rsk-13--saisir-le-verdict-dun-partenaire-et-documenter-son-écart) | Saisir le verdict d'un partenaire et documenter son écart | Après pilote | Turnkey |

### Registre Q&A avec le client

| Story | Titre | Périmètre | Variantes |
|---|---|---|---|
| [US-QA-01](11-qa.md#us-qa-01--recevoir-dans-le-registre-une-question-posée-depuis-compliance) | Recevoir dans le registre une question posée depuis Compliance | Après pilote | Toutes |
| [US-QA-02](11-qa.md#us-qa-02--parcourir-le-registre-en-deux-vues-par-statut) | Parcourir le registre en deux vues, par statut | Après pilote | Toutes |
| [US-QA-03](11-qa.md#us-qa-03--rechercher-une-question-et-filtrer-par-système) | Rechercher une question et filtrer par système | Après pilote | Toutes |
| [US-QA-04](11-qa.md#us-qa-04--voir-les-dates-de-clôture-des-questions-et-de-retour-des-réponses) | Voir les dates de clôture des questions et de retour des réponses | Après pilote | Toutes |
| [US-QA-05](11-qa.md#us-qa-05--exporter-vers-excel-les-questions-à-envoyer) | Exporter vers Excel les questions à envoyer | Après pilote | Toutes |
| [US-QA-06](11-qa.md#us-qa-06--marquer-des-questions-envoyées-une-ou-plusieurs-et-revenir-en-arrière) | Marquer des questions envoyées, une ou plusieurs, et revenir en arrière | Après pilote | Toutes |
| [US-QA-07](11-qa.md#us-qa-07--importer-le-dossier-de-réponses-du-client) | Importer le dossier de réponses du client | Après pilote | Toutes |
| [US-QA-08](11-qa.md#us-qa-08--confirmer-ou-écarter-une-réponse-incertaine) | Confirmer ou écarter une réponse incertaine | Après pilote | Toutes |
| [US-QA-09](11-qa.md#us-qa-09--lire-la-réponse-du-client-sous-sa-question) | Lire la réponse du client sous sa question | Après pilote | Toutes |
| [US-QA-10](11-qa.md#us-qa-10--consulter-les-questions-réponses-des-autres-soumissionnaires) | Consulter les questions-réponses des autres soumissionnaires | Après pilote | Toutes |
| [US-QA-11](11-qa.md#us-qa-11--réserver-à-léquipe-de-gestion-le-marquage-des-questions-envoyées) | Réserver à l'équipe de gestion le marquage des questions envoyées | Après pilote | Toutes |

### Team casting et droits

| Story | Titre | Périmètre | Variantes |
|---|---|---|---|
| [US-TEAM-01](12-casting-droits.md#us-team-01--ouvrir-le-team-casting-là-où-lon-a-à-agir) | Ouvrir le Team casting là où l'on a à agir | Pilote 1 | Toutes |
| [US-TEAM-02](12-casting-droits.md#us-team-02--repérer-les-systèmes-sans-personne-et-les-staffer) | Repérer les systèmes sans personne et les staffer | Pilote 1 | Toutes |
| [US-TEAM-03](12-casting-droits.md#us-team-03--composer-léquipe-de-gestion-du-projet) | Composer l'équipe de gestion du projet | Pilote 1 | Toutes |
| [US-TEAM-04](12-casting-droits.md#us-team-04--ajouter-un-système-au-tender-depuis-la-liste-de-référence) | Ajouter un système au tender depuis la liste de référence | Pilote 1 | Turnkey (absent sur SIG et Mainline) |
| [US-TEAM-05](12-casting-droits.md#us-team-05--staffer-une-personne-sur-un-système-avec-ou-sans-périmètre) | Staffer une personne sur un système, avec ou sans périmètre | Pilote 1 | Toutes |
| [US-TEAM-06](12-casting-droits.md#us-team-06--refuser-quune-personne-appartienne-à-deux-systèmes) | Refuser qu'une personne appartienne à deux systèmes | Pilote 1 | Toutes |
| [US-TEAM-07](12-casting-droits.md#us-team-07--staffer-une-personne-sur-plusieurs-périmètres-sans-doublon) | Staffer une personne sur plusieurs périmètres, sans doublon | Pilote 1 | Toutes |
| [US-TEAM-08](12-casting-droits.md#us-team-08--retrouver-une-personne-dans-un-casting-de-200-personnes) | Retrouver une personne dans un casting de 200 personnes | Pilote 1 | Toutes |
| [US-TEAM-09](12-casting-droits.md#us-team-09--retirer-une-personne-après-réaffectation-de-son-travail) | Retirer une personne, après réaffectation de son travail | Pilote 1 | Toutes |
| [US-TEAM-10](12-casting-droits.md#us-team-10--laisser-les-contributeurs-dun-système-gérer-ses-rattachements) | Laisser les contributeurs d'un système gérer ses rattachements | Pilote 1 | Toutes |
| [US-TEAM-11](12-casting-droits.md#us-team-11--désigner-automatiquement-la-personne-dune-allocation-depuis-son-périmètre) | Désigner automatiquement la personne d'une allocation depuis son périmètre | Pilote 1 | Toutes |
| [US-TEAM-12](12-casting-droits.md#us-team-12--avancer-sans-attendre-que-le-casting-soit-complet) | Avancer sans attendre que le casting soit complet | Pilote 1 | Toutes |
| [US-TEAM-13](12-casting-droits.md#us-team-13--lire-tout-son-tender-et-aucun-autre) | Lire tout son tender, et aucun autre | Pilote 1 | Toutes |
| [US-TEAM-14](12-casting-droits.md#us-team-14--ne-modifier-que-le-travail-de-son-système) | Ne modifier que le travail de son système | Pilote 1 | Toutes |
| [US-TEAM-15](12-casting-droits.md#us-team-15--répondre-pour-un-collègue-de-son-système) | Répondre pour un collègue de son système | Après pilote | Toutes |
| [US-TEAM-16](12-casting-droits.md#us-team-16--réserver-la-nature-et-la-classe-au-chef-de-projet) | Réserver la nature et la classe au chef de projet | Pilote 1 | Toutes |
| [US-TEAM-17](12-casting-droits.md#us-team-17--laisser-le-chef-de-projet-saisir-ou-corriger-toute-réponse) | Laisser le chef de projet saisir ou corriger toute réponse | Après pilote | Toutes |

### Tableau de bord du tender

| Story | Titre | Périmètre | Variantes |
|---|---|---|---|
| [US-DASH-01](13-tableau-de-bord.md#us-dash-01--voir-lidentité-et-léchéance-du-tender-ouvert) | Voir l'identité et l'échéance du tender ouvert | Pilote 1 | Toutes |
| [US-DASH-02](13-tableau-de-bord.md#us-dash-02--suivre-létape-allocation-sur-sa-carte) | Suivre l'étape Allocation sur sa carte | Pilote 1 | Toutes |
| [US-DASH-03](13-tableau-de-bord.md#us-dash-03--suivre-létape-compliance-en-parallèle) | Suivre l'étape Compliance en parallèle | Après pilote | Toutes |
| [US-DASH-04](13-tableau-de-bord.md#us-dash-04--ouvrir-team-casting-et-documents--versions-depuis-le-rail--always-open-) | Ouvrir Team casting et Documents & versions depuis le rail « Always open » | Pilote 1 | Toutes |
| [US-DASH-05](13-tableau-de-bord.md#us-dash-05--voir-les-risques-et-les-questions-au-client-dans-le-rail) | Voir les risques et les questions au client dans le rail | Après pilote | Toutes |
| [US-DASH-06](13-tableau-de-bord.md#us-dash-06--voir-les-demandes-de-réallocation-en-attente) | Voir les demandes de réallocation en attente | Pilote 1 | Toutes |
| [US-DASH-07](13-tableau-de-bord.md#us-dash-07--voir-ce-qui-mattend-dans--what-needs-you-now-) | Voir ce qui m'attend dans « What needs you now » | Pilote 1 | Toutes |
| [US-DASH-08](13-tableau-de-bord.md#us-dash-08--voir-le-travail-dallocation-qui-mattend) | Voir le travail d'allocation qui m'attend | Pilote 1 | Toutes |
| [US-DASH-09](13-tableau-de-bord.md#us-dash-09--voir-larrivée-dune-nouvelle-version-et-ses-effets) | Voir l'arrivée d'une nouvelle version et ses effets | Après pilote | Toutes |
| [US-DASH-10](13-tableau-de-bord.md#us-dash-10--voir-les-réponses-en-retard-et-les-not-compliant-à-documenter) | Voir les réponses en retard et les Not compliant à documenter | Après pilote | Toutes |
| [US-DASH-11](13-tableau-de-bord.md#us-dash-11--voir-les-questions-à-envoyer-au-client) | Voir les questions à envoyer au client | Après pilote | Toutes |
| [US-DASH-12](13-tableau-de-bord.md#us-dash-12--lire-les-derniers-commentaires-du-tender) | Lire les derniers commentaires du tender | Pilote 1 (à confirmer) | Toutes |
| [US-DASH-13](13-tableau-de-bord.md#us-dash-13--suivre-les-réponses-par-système) | Suivre les réponses par système | Après pilote | Toutes (SIG : par sous-système) |
| [US-DASH-14](13-tableau-de-bord.md#us-dash-14--suivre-lactivité-récente-du-tender) | Suivre l'activité récente du tender | Après pilote | Toutes |
| [US-DASH-15](13-tableau-de-bord.md#us-dash-15--ouvrir-la-cloche-du-tableau-de-bord) | Ouvrir la cloche du tableau de bord | Pilote 1 | Toutes |

### Statistiques

| Story | Titre | Périmètre | Variantes |
|---|---|---|---|
| [US-STAT-01](14-statistiques.md#us-stat-01--lire-les-statistiques-par-onglet-une-phrase-puis-le-chiffre) | Lire les statistiques par onglet, une phrase puis le chiffre | Pilote 1 (à confirmer) | Toutes |
| [US-STAT-02](14-statistiques.md#us-stat-02--ne-mesurer-aucune-personne) | Ne mesurer aucune personne | Pilote 1 | Toutes |
| [US-STAT-03](14-statistiques.md#us-stat-03--suivre-les-dates-clés-et-le-rythme-du-tender) | Suivre les dates clés et le rythme du tender | Pilote 1 (à confirmer) | Toutes |
| [US-STAT-04](14-statistiques.md#us-stat-04--voir-les-systèmes-les-plus-actifs-de-la-semaine) | Voir les systèmes les plus actifs de la semaine | Pilote 1 (à confirmer) | Toutes (SIG : par sous-système) |
| [US-STAT-05](14-statistiques.md#us-stat-05--voir-léquipe-du-tender) | Voir l'équipe du tender | Pilote 1 | Toutes (SIG : par sous-système) |
| [US-STAT-06](14-statistiques.md#us-stat-06--voir-où-en-sont-les-exigences-dans-allocation) | Voir où en sont les exigences dans Allocation | Pilote 1 | Toutes |
| [US-STAT-07](14-statistiques.md#us-stat-07--voir-lallocation-par-système-avec-qui-y-est-staffé) | Voir l'allocation par système, avec qui y est staffé | Pilote 1 | Turnkey (masqué sur SIG) |
| [US-STAT-08](14-statistiques.md#us-stat-08--voir-les-exigences-renvoyées-pour-réallocation) | Voir les exigences renvoyées pour réallocation | Pilote 1 | Toutes |
| [US-STAT-09](14-statistiques.md#us-stat-09--voir-le-travail-invalidé-par-une-nouvelle-version) | Voir le travail invalidé par une nouvelle version | Après pilote | Toutes |
| [US-STAT-10](14-statistiques.md#us-stat-10--voir-la-progression-vers-le-client) | Voir la progression vers le client | Après pilote | Toutes |
| [US-STAT-11](14-statistiques.md#us-stat-11--suivre-les-réponses-par-système-et-leurs-retards) | Suivre les réponses par système et leurs retards | Après pilote | Toutes (SIG : par sous-système) |
| [US-STAT-12](14-statistiques.md#us-stat-12--voir-ce-quattendent-les-exigences-encore-ouvertes) | Voir ce qu'attendent les exigences encore ouvertes | Après pilote | Toutes |
| [US-STAT-13](14-statistiques.md#us-stat-13--voir-les-not-compliant-par-stratégie-décart) | Voir les Not compliant par stratégie d'écart | Après pilote | Toutes |
| [US-STAT-14](14-statistiques.md#us-stat-14--voir-les-risques-du-tender-et-leur-réutilisation) | Voir les risques du tender et leur réutilisation | Après pilote | Toutes |

### Configuration du tender

| Story | Titre | Périmètre | Variantes |
|---|---|---|---|
| [US-CFG-01](15-configuration.md#us-cfg-01--ouvrir-les-paramètres-et-ny-trouver-que-des-réglages-réels) | Ouvrir les paramètres et n'y trouver que des réglages réels | Pilote 1 | Toutes |
| [US-CFG-02](15-configuration.md#us-cfg-02--consulter-les-informations-générales-du-tender) | Consulter les informations générales du tender | Pilote 1 | Toutes |
| [US-CFG-03](15-configuration.md#us-cfg-03--régler-léchéance-de-soumission) | Régler l'échéance de soumission | Pilote 1 | Toutes |
| [US-CFG-04](15-configuration.md#us-cfg-04--voir-les-contributeurs-du-tender-depuis-les-paramètres) | Voir les contributeurs du tender depuis les paramètres | Pilote 1 | Toutes |
| [US-CFG-05](15-configuration.md#us-cfg-05--régler-le-seuil-de-retard-et-la-cadence-des-relances) | Régler le seuil de retard et la cadence des relances | Après pilote | Toutes |
| [US-CFG-06](15-configuration.md#us-cfg-06--consulter-le-système-le-produit-et-le-modèle-appliqué) | Consulter le système, le produit et le modèle appliqué | Pilote 1 | Toutes |
| [US-CFG-07](15-configuration.md#us-cfg-07--changer-de-modèle-et-relancer-toute-la-dérivation) | Changer de modèle et relancer toute la dérivation | Pilote 1 | SIG, Mainline |
| [US-CFG-08](15-configuration.md#us-cfg-08--ajouter-un-partenaire-externe-à-la-liste-obs-turnkey) | Ajouter un partenaire externe à la liste OBS Turnkey | Pilote 1 (à confirmer) | Turnkey |
| [US-CFG-09](15-configuration.md#us-cfg-09--retirer-un-partenaire-externe) | Retirer un partenaire externe | Pilote 1 (à confirmer) | Turnkey |
| [US-CFG-10](15-configuration.md#us-cfg-10--choisir-son-thème-clair-ou-sombre) | Choisir son thème clair ou sombre | Pilote 1 | Toutes |
| [US-CFG-11](15-configuration.md#us-cfg-11--capter-chaque-correction-dune-proposition-de-lia) | Capter chaque correction d'une proposition de l'IA | Pilote 1 | Toutes (Turnkey : routage vers les systèmes) |
| [US-CFG-12](15-configuration.md#us-cfg-12--consulter-la-qualité-de-lia-dans--ai-feedback-) | Consulter la qualité de l'IA dans « AI feedback » | Pilote 1 (à confirmer) | Toutes |
| [US-CFG-13](15-configuration.md#us-cfg-13--choisir-le-canal-de-lémetteur-pour-les-questions) | Choisir le canal de l'émetteur pour les questions | Après pilote | Toutes |
| [US-CFG-14](15-configuration.md#us-cfg-14--régler-la-numérotation-des-versions-et-la-détection-daddendum) | Régler la numérotation des versions et la détection d'addendum | Après pilote | Toutes |
| [US-CFG-15](15-configuration.md#us-cfg-15--voir-la-langue-de-travail-et-la-langue-source) | Voir la langue de travail et la langue source | Pilote 1 | Toutes |

### Transverse : journal, notifications, plateforme

| Story | Titre | Périmètre | Variantes |
|---|---|---|---|
| [US-X-01](16-transverse.md#us-x-01--consulter-le-journal-dactivité-dune-exigence) | Consulter le journal d'activité d'une exigence | Pilote 1 | Toutes |
| [US-X-02](16-transverse.md#us-x-02--commenter-une-exigence) | Commenter une exigence | Pilote 1 | Toutes |
| [US-X-03](16-transverse.md#us-x-03--retrouver-tout-le-travail-après-reconnexion) | Retrouver tout le travail après reconnexion | Pilote 1 | Toutes |
| [US-X-04](16-transverse.md#us-x-04--se-connecter-par-sso-et-naccéder-quà-ses-tenders) | Se connecter par SSO et n'accéder qu'à ses tenders | Pilote 1 | Toutes |
| [US-X-05](16-transverse.md#us-x-05--faire-respecter-les-droits-du-tender-par-le-serveur) | Faire respecter les droits du tender par le serveur | Pilote 1 | Toutes |
| [US-X-06](16-transverse.md#us-x-06--tracer-tout-changement-humain-ou-machine) | Tracer tout changement, humain ou machine | Pilote 1 | Toutes |
| [US-X-07](16-transverse.md#us-x-07--garder-séparées-la-proposition-de-lia-la-valeur-retenue-et-la-correction) | Garder séparées la proposition de l'IA, la valeur retenue et la correction | Pilote 1 | Toutes |
| [US-X-08](16-transverse.md#us-x-08--exporter-les-exigences-du-tender) | Exporter les exigences du tender | Pilote 1 (à confirmer) | Toutes |
| [US-X-09](16-transverse.md#us-x-09--importer-un-export-doors-comme-document-du-tender) | Importer un export DOORS comme document du tender | Pilote 1 (à confirmer) | Toutes |
| [US-X-10](16-transverse.md#us-x-10--recevoir-les-notifications-dans-lapplication-et-par-e-mail) | Recevoir les notifications dans l'application et par e-mail | Pilote 1 (à confirmer) | Toutes |
| [US-X-11](16-transverse.md#us-x-11--travailler-sur-100-000-lignes-à-dix-en-même-temps) | Travailler sur 100 000 lignes à dix en même temps | Pilote 1 | Toutes |
| [US-X-12](16-transverse.md#us-x-12--comprendre-létat-dun-écran--chargement-vide-absence-de-droit) | Comprendre l'état d'un écran : chargement, vide, absence de droit | Pilote 1 | Toutes |
| [US-X-13](16-transverse.md#us-x-13--ne-rien-perdre-en-cas-déchec-ou-de-conflit-denregistrement) | Ne rien perdre en cas d'échec ou de conflit d'enregistrement | Pilote 1 | Toutes |
| [US-X-14](16-transverse.md#us-x-14--lire-des-couleurs-qui-gardent-toujours-le-même-sens) | Lire des couleurs qui gardent toujours le même sens | Pilote 1 | Toutes |
