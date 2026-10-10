<!-- Généré depuis le backlog du 10 octobre 2026 ; voir README.md pour les conventions. -->
# Changements de version côté Allocation (US-CHG)

Quand un document reçoit une nouvelle version (écran Documents, [US-DOC-04](03-documents.md#us-doc-04--téléverser-une-nouvelle-version-dun-document)), Allocation fait revoir les exigences qu'elle ajoute ou modifie. Le chef de projet — et le contributeur, sur son système — lit les changements dans la table et dans le détail, puis valide : cela suffit à les traiter (JRN-005, JRN-002). La relecture complète d'un document se fait dans la vue Document (US-DOCV).
- **Version en vigueur** : la dernière version d'un document ; les versions appartiennent aux documents, jamais au tender (DEC-069).
- **Diff mot à mot** : la même exigence, mots supprimés barrés et mots ajoutés surlignés, comme dans DOORS.
- **Exigence supprimée** : exigence d'une version antérieure qui n'existe plus dans la version en vigueur de son document.

### US-CHG-01 — Revoir une exigence ajoutée ou modifiée par une nouvelle version
**Carte :** En tant que chef de projet, je veux que chaque exigence ajoutée ou modifiée par la version en vigueur de son document repasse « To review », afin qu'aucune décision ne reste posée sur un texte qui a changé.
**Conversation :** Il n'y a pas d'état propre à un changement (DEC-072) : ni « New », ni « Reviewed, no impact », ni « Action required » ; l'exigence repasse To review et la valider est le traitement (validation : [US-ALM-26](05-allocation.md#us-alm-26--valider-une-exigence-en-un-seul-geste)). Le statut le plus restrictif continue de primer, et les exigences inchangées ne bougent pas. Côté Compliance, les verdicts d'une exigence modifiée sont rouverts (DEC-122, [US-CMP-27](09-compliance.md#us-cmp-27--rouvrir-les-verdicts-dune-exigence-modifiée-par-une-nouvelle-version)) ; les modèles nécessaires sont relancés automatiquement sur les seules exigences modifiées (DEC-027, [US-CAP-12](04-capture-ia.md#us-cap-12--relancer-automatiquement-les-modèles-sur-les-seules-exigences-modifiées-par-une-nouvelle-version)). Une exigence issue d'une fusion ou d'une scission arrive comme ajoutée, sans décision héritée (DEC-017 ; LIFE-009 dans [US-CAP-13](04-capture-ia.md#us-cap-13--repartir-de-zéro-sur-une-exigence-issue-dune-fusion-ou-dune-scission)).
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Status Pill (motif en tête du panneau) et pastille « changed in latest version » du Triage Bar.
**Règles :** DEC-072, DEC-069, DEC-017, DEC-073, LIFE-015, LIFE-012, LIFE-T12, LIFE-T13 · **Périmètre :** Après pilote · **Variantes :** Toutes
**Critères d'acceptation :**
1. Une exigence ajoutée ou modifiée dans la version en vigueur de son document passe « To review », avec le motif « Added in vX of its document — see the Versions tab » ou « Modified in vX of its document — see the Versions tab ».
2. Si un statut plus restrictif s'applique (par exemple Incomplete), c'est lui que montre la pastille de statut.
3. Une exigence inchangée garde son statut, même quand son document change de version ; un titre ou une information modifiés ne prennent aucun statut.
4. La pastille « N changed in latest version » de la barre de statut compte ces exigences et, cliquée, ne garde qu'elles dans la table.
5. Valider l'exigence suffit à traiter le changement : aucun autre bouton ni état ne le marque traité.
Écart maquette : les versions d'Allocation sont des données propres à l'écran ; une version téléversée dans Documents n'y arrive pas, et la relance automatique des modèles n'y est pas démontrée.
Point ouvert : la façon de reconnaître une même exigence d'une version à l'autre (modifiée, fusionnée, scindée) n'est pas spécifiée (OPEN-07, DOM-012).

### US-CHG-02 — Lire les changements dans la colonne Changes
**Carte :** En tant que chef de projet ou contributeur, je veux voir, à côté du texte en vigueur, la même exigence avec ses mots supprimés barrés et ajoutés surlignés, afin de comprendre ce qui a changé sans ouvrir chaque exigence.
**Conversation :** Les changements se lisent dans la table, sans mode dédié (DEC-119). La colonne « Changes » suit « Requirement », qui garde le texte en vigueur. Chaque cellule compare avec une version antérieure du document de l'exigence — la précédente par défaut ([US-CHG-03](#us-chg-03--choisir-la-version-de-comparaison-ligne-par-ligne-ou-pour-toutes) pour en choisir une autre). Aucune version de tender n'est affichée, chaque document a les siennes (DEC-069), et une exigence supprimée n'a pas de ligne ([US-CHG-06](#us-chg-06--consulter-une-exigence-supprimée-par-une-nouvelle-version)).
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Changes Cell (Change Type Tag, Version Picker Button) du Requirement Table (Review Grid).
**Règles :** DEC-119, DEC-069, LIFE-016, LIFE-012, LIFE-006, LIFE-T10, LIFE-T14 · **Périmètre :** Après pilote · **Variantes :** Toutes
**Critères d'acceptation :**
1. La colonne « Changes » se place juste après « Requirement » ; elle est visible par défaut dès qu'un document du tender a plusieurs versions, et masquée sinon.
2. Une exigence modifiée y montre son texte en vigueur, mots supprimés barrés et mots ajoutés surlignés (par exemple « once » barré et « twice » ajouté) ; sur une ligne, la cellule commence quelques mots avant le premier changement.
3. Avec « Wrap text », la cellule montre toute l'exigence et ses changements.
4. Une exigence ajoutée montre son texte entier surligné, avec l'étiquette « New ».
5. Une exigence sans changement affiche « No change » ; une exigence dont le document n'a qu'une version affiche « Single version ».
6. Aucune barre de l'écran n'affiche de version de tender (pas de pastille du type « v2.1 active »).

### US-CHG-03 — Choisir la version de comparaison, ligne par ligne ou pour toutes
**Carte :** En tant que chef de projet ou contributeur, je veux comparer une exigence, ou toutes, avec la version de mon choix de leur document, afin de voir soit le dernier changement, soit tout ce qui a changé depuis l'émission du tender.
**Conversation :** Chaque cellule a son propre sélecteur de version ; celui de l'en-tête change toutes les lignes d'un coup et remet à zéro les choix faits ligne par ligne (DEC-119). Les choix portent toujours sur les versions du document de chaque exigence, jamais sur une version de tender (DEC-069). « The first version » montre tout ce qui a changé depuis l'émission.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Version Picker Button et Version Picker Popover (cellule et en-tête « Changes »).
**Règles :** DEC-119, DEC-069, LIFE-016, LIFE-012, LIFE-T14 · **Périmètre :** Après pilote · **Variantes :** Toutes
**Critères d'acceptation :**
1. Chaque cellule porte un sélecteur « vs vX ▾ » qui liste les versions antérieures du document de l'exigence, avec date et note, et « — no change since » sous une version après laquelle l'exigence n'a plus changé.
2. Choisir une version pour une ligne ne change que cette ligne ; son sélecteur se distingue alors, et « Same as the column » la remet au choix de la colonne.
3. Le sélecteur de l'en-tête (« vs previous ▾ » / « vs first ▾ ») applique « The previous version » ou « The first version » de leur document à toutes les lignes.
4. Choisir pour toutes remet à zéro les choix faits ligne par ligne, ce que le sélecteur annonce avant (« N requirements have a version of their own — choosing here resets them. »).
5. Comparée à la première version, une exigence modifiée indique les versions où elle a changé (par exemple « v2.0 · v2.1 »).
6. Deux lignes de documents différents comparent chacune avec une version de leur propre document.

### US-CHG-04 — Filtrer sur les changements et afficher la colonne avec C
**Carte :** En tant que chef de projet ou contributeur, je veux ne garder que les exigences modifiées ou ajoutées, et faire apparaître ou disparaître la colonne Changes d'une touche, afin de traiter une réédition sans quitter la table.
**Conversation :** Le filtre de la colonne « Changes » suit la version que compare chaque ligne (DEC-119). La touche C fait aller et venir la colonne (DEC-085, DEC-119). Colonne masquée, un badge garde le changement visible sur la ligne.
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), entonnoir de l'en-tête « Changes » (Column Filter Section), Shortcut Help, Block Badge « Δ vX ».
**Règles :** DEC-119, DEC-085, LIFE-016, LIFE-T14, UX-002 · **Périmètre :** Après pilote · **Variantes :** Toutes
**Critères d'acceptation :**
1. L'entonnoir de « Changes » propose « Modified », « Added » et « No change », calculés contre la version que compare chaque ligne.
2. Ne garder que « Modified » ne laisse que les exigences modifiées dans la plage comparée.
3. La touche C affiche ou masque la colonne et l'annonce (« Changes column shown — C to hide it » / « Changes column hidden — C to show it ») ; « View » fait de même.
4. Si aucun document n'a plusieurs versions, C ne change rien et le dit (« Every document has a single version — no change to show »).
5. Colonne masquée, une exigence changée dans la version en vigueur porte un badge « Δ vX » sur sa ligne.
6. Le filtre avancé propose le champ « Changed in latest version » (Added, Modified, Unchanged).

### US-CHG-05 — Consulter l'onglet Versions d'une exigence changée
**Carte :** En tant que chef de projet ou contributeur, je veux voir dans le détail d'une exigence ce qui a changé, depuis quelle version, et son texte précédent, afin de décider en connaissance de cause avant de valider.
**Conversation :** L'onglet « Versions » n'existe que si l'exigence a changé dans la version en vigueur de son document (DEC-071). Il n'a pas d'état « revu » propre : il rappelle que la validation est le traitement (DEC-072). Il mène à la vue Document pour voir le changement dans son contexte ([US-DOCV-06](07-vue-document.md#us-docv-06--comparer-un-document-à-une-version-antérieure-onglet-changes)).
**Maquette :** Allocation — `revue-documentaire.html` (route `#review`), Versions Tab du panneau de détail (Word Diff).
**Règles :** DEC-071, DEC-072, DEC-119, LIFE-014, LIFE-T12 · **Périmètre :** Après pilote · **Variantes :** Toutes
**Critères d'acceptation :**
1. L'onglet « Versions » n'apparaît que sur une exigence ajoutée ou modifiée dans la version en vigueur de son document ; une exigence inchangée n'en a pas.
2. Il indique le type et la version du changement (« Modified in vX » ou « Added in vX »), la date et la note de cette version, et le document comparé (« <document> — compared with vA »).
3. Pour une modification, « What changed » montre le diff mot à mot et « Full text in vA » déplie le texte précédent complet ; pour un ajout, il dit qu'il n'y a pas de texte antérieur.
4. Les versions antérieures où l'exigence avait déjà changé sont listées sous « Earlier versions ».
5. Une phrase dit où en est le traitement : « Set back to To review by this change. Validate the requirement once the change has been checked. », puis « Checked since the change… » une fois l'exigence validée ; elle signale quand un statut plus restrictif s'affiche à la place.
6. « Show in the document → » ouvre la vue Document sur l'onglet « Changes », à ce document, à la version précédente et à cette exigence.

### US-CHG-06 — Consulter une exigence supprimée par une nouvelle version
**Carte :** En tant que chef de projet, je veux voir quelles exigences une nouvelle version a supprimées et ce qu'elles disaient, afin de m'assurer qu'aucun travail utile ne disparaît sans que je le sache.
**Conversation :** Une exigence supprimée n'est visible que dans l'onglet « Changes » de la vue Document (LIFE-006, DEC-017, DEC-119), jamais dans la table, le plan ni les compteurs. Son historique n'est pas effacé : ses anciennes décisions restent tracées pour l'audit, sans rester valides. Rien ne s'y modifie.
**Maquette :** Allocation, mode « Document » — `revue-documentaire.html` (route `#review`), Removed Requirement Panel et blocs supprimés du Document Reading View (onglet « Changes »).
**Règles :** LIFE-006, LIFE-T06, DEC-017, DEC-119, PLAT-003 · **Périmètre :** Après pilote · **Variantes :** Toutes
**Critères d'acceptation :**
1. Une exigence supprimée n'apparaît ni dans la table, ni dans le plan, ni dans les compteurs de statut, ni dans les résultats d'une recherche ou d'un filtre.
2. Dans l'onglet « Changes », sur une plage qui la couvre, elle apparaît à sa place dans le document (« Removed in vX — … ») et dans la liste des changements.
3. La sélectionner ouvre un panneau en lecture seule : « Removed in vX », le document et ses versions (« present in vA, gone from vB ») et son texte dans vA.
4. Le panneau dit qu'elle ne fait plus partie du tender (« No longer part of the tender… ») et n'offre aucune action.
5. Sa suppression n'efface pas son historique : ses décisions passées restent dans la trace d'audit.
Point ouvert : où et comment consulter l'historique d'une exigence supprimée n'est pas spécifié (LIFE-006, OPEN-07).

## Couverture
- Règles couvertes : LIFE-006 → [US-CHG-02](#us-chg-02--lire-les-changements-dans-la-colonne-changes), [US-CHG-06](#us-chg-06--consulter-une-exigence-supprimée-par-une-nouvelle-version) (et [US-DOCV-06](07-vue-document.md#us-docv-06--comparer-un-document-à-une-version-antérieure-onglet-changes)) ; LIFE-012 → [US-CHG-01](#us-chg-01--revoir-une-exigence-ajoutée-ou-modifiée-par-une-nouvelle-version), [US-CHG-02](#us-chg-02--lire-les-changements-dans-la-colonne-changes), [US-CHG-03](#us-chg-03--choisir-la-version-de-comparaison-ligne-par-ligne-ou-pour-toutes) (et [US-DOCV-06](07-vue-document.md#us-docv-06--comparer-un-document-à-une-version-antérieure-onglet-changes)) ; LIFE-014 → [US-CHG-05](#us-chg-05--consulter-longlet-versions-dune-exigence-changée) ; LIFE-015 → [US-CHG-01](#us-chg-01--revoir-une-exigence-ajoutée-ou-modifiée-par-une-nouvelle-version) ; LIFE-016 → [US-CHG-02](#us-chg-02--lire-les-changements-dans-la-colonne-changes), [US-CHG-03](#us-chg-03--choisir-la-version-de-comparaison-ligne-par-ligne-ou-pour-toutes), [US-CHG-04](#us-chg-04--filtrer-sur-les-changements-et-afficher-la-colonne-avec-c) ; LIFE-T10 (« la barre supérieure n'affiche aucune version de projet ») → [US-CHG-02](#us-chg-02--lire-les-changements-dans-la-colonne-changes) ; LIFE-T12 → [US-CHG-01](#us-chg-01--revoir-une-exigence-ajoutée-ou-modifiée-par-une-nouvelle-version), [US-CHG-05](#us-chg-05--consulter-longlet-versions-dune-exigence-changée) ; LIFE-T13 → [US-CHG-01](#us-chg-01--revoir-une-exigence-ajoutée-ou-modifiée-par-une-nouvelle-version) ; LIFE-T14 → [US-CHG-02](#us-chg-02--lire-les-changements-dans-la-colonne-changes), [US-CHG-03](#us-chg-03--choisir-la-version-de-comparaison-ligne-par-ligne-ou-pour-toutes), [US-CHG-04](#us-chg-04--filtrer-sur-les-changements-et-afficher-la-colonne-avec-c).
- Non couvertes, avec la raison : LIFE-013, LIFE-T11 — couvertes par l'épopée US-DOCV ; second LIFE-T10 (« un retraitement SIG ne lance pas la passe 1 Turnkey ») — couverte par l'épopée US-CAP ([US-CAP-12](04-capture-ia.md#us-cap-12--relancer-automatiquement-les-modèles-sur-les-seules-exigences-modifiées-par-une-nouvelle-version), LIFE-011), le numéro est en double dans LIFECYCLE.md ; LIFE-009 (fusion / scission) — couverte par l'épopée US-CAP ([US-CAP-13](04-capture-ia.md#us-cap-13--repartir-de-zéro-sur-une-exigence-issue-dune-fusion-ou-dune-scission)), rappelée dans [US-CHG-01](#us-chg-01--revoir-une-exigence-ajoutée-ou-modifiée-par-une-nouvelle-version) ; LIFE-007 (réouverture des verdicts) — couverte par l'épopée US-CMP ([US-CMP-27](09-compliance.md#us-cmp-27--rouvrir-les-verdicts-dune-exigence-modifiée-par-une-nouvelle-version)).
