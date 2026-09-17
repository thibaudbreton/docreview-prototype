# Allocation et validation humaine

Applicabilité : [variantes de tender](TENDER-PROFILES.md). Le prototype est la référence Turnkey ; ne pas en reproduire la passe 1 dans un tender SIG.

## Règles

| ID | Règle | Statut et portée |
|---|---|---|
| ALLOC-001 | Turnkey distribue entre activités, puis applique leur modèle. Un tender SIG commence directement dans SIG. | DEC-005/006, DOC autres non-Turnkey |
| ALLOC-002 | Passe 1 Turnkey : classe technique vers PBS, non technique vers ABS, puis activité TK OBS. Cette distinction ne s'applique pas à l'allocation SIG. | DOC passe 1, DEC-008 exclusion SIG |
| ALLOC-003 | Allocation SIG : **ABS → PBS → OBS → personne**. Aucune différence de chaîne technique/non technique. Corriger un champ invalide les propositions qui en dépendent ; les corrections de décisions déjà validées suivent LIFE-008. | DEC-008 prime sur l'ancien PBS → ABS → OBS |
| ALLOC-004 | Distribution multiple entre activités en Turnkey, puis affectations d'équipes ; ne pas dupliquer l'exigence pour représenter les branches. | DOC, consolidation confirmée DEC-014 |
| ALLOC-005 | Activité sans modèle : allocation manuelle, identifiée et filtrable, sans bloquer les autres activités. | DOC ; contenu/gestion des modèles hors spec fonctionnelle |
| ALLOC-006 | Incertitude affichée par champ/étape applicable ; aucun indicateur de passe 1 en SIG. | DOC/DEC-006 |
| ALLOC-007 | La confiance IA ne remplace pas la validation humaine de l'allocation. | DOC, borne du pilote DEC-022 |
| ALLOC-008 | La validation d'allocation rend le travail disponible pour la suite de conformité ; pas de construction de Compliance exigée dans le premier pilote. | DOC + DEC-022 |
| ALLOC-009 | Les exigences progressent indépendamment. Un cas incomplet n'arrête pas les autres. | DOC |
| ALLOC-010 | L’allocation peut être validée sans responsable. L’absence reste visible, sans bloquer cette exigence ni les autres. | DEC-025 |
| ALLOC-011 | **Au plus une personne responsable du suivi par exigence**, pas une par activité ou équipe. Tous les contributeurs de l'activité peuvent répondre. | DEC-010 + DEC-002 |
| ALLOC-012 | La validation relève de l'équipe de gestion du projet, composée de bid managers et requirement managers de SIG selon la réponse utilisateur. Ces fonctions ne créent pas une hiérarchie des contributeurs. | DEC-009 ; portée générale aux autres types OPEN-15 |

## Absence de responsable — décision

DEC-025 : absence autorisée, y compris après validation d’allocation. Afficher « Non désigné » et permettre d’isoler ces exigences avec le filtre de champ vide existant ; ne pas ajouter de validation bloquante. Les contributeurs gardent leurs droits dans leur activité. Un responsable peut être désigné ensuite ; il devient l’unique responsable du suivi. La proposition de blocage formulée précédemment a été refusée.

## Réallocation — référence vérifiée dans la maquette

ALLOC-013 — DEC-011 : conserver le mécanisme de demande de réallocation de la maquette, pas inventer une nouvelle interaction.

- Motifs : bonne activité/mauvaise personne ; mauvaise activité ; activité non applicable.
- Justification requise ; proposer une personne de remplacement pour le premier, une activité de remplacement pour les deux autres dans le parcours Turnkey.
- La demande passe à `reassignment_needed`. La maquette offre approbation/refus.
- Approbation personne : remplacement du responsable, travail remis à disposition. Le code historique utilise des identifiants équipe/personne incohérents par écran ; ne pas reproduire cette duplication avec DEC-010.
- Approbation activité : remplacement de la branche, état proposé/en attente et nouvelle allocation. La maquette remplace au lieu de laisser zéro activité.
- Refus : retour à l'état antérieur.
- La gestion projet reçoit les demandes au niveau global ; les anciens rôles manager/expert du code ne recréent pas une hiérarchie métier après DEC-003/012.

Dans un tender SIG, les actions de distribution Turnkey sont absentes (DEC-006). Ne pas laisser un menu de changement d'activité qui lancerait la passe 1. Les cas hors activité en standalone devront être explicités si nécessaires (OPEN-15), sans inventer leur équivalent.

Sources : `revue-documentaire.html:renderReassignForm/submitReassignRequest/approveReassign/rejectReassign`, `compliance.html:reassign-submit`. Inspection du code ; pas de recette navigateur.

## Relance d'une passe d'allocation

ALLOC-014 — DEC-040 à DEC-043 : rejouer un modèle d'allocation sur une exigence déjà traitée, en choisissant lequel. Mécanisme distinct de la réallocation (ALLOC-013) : la réallocation change **qui** répond, la relance recalcule **ce que le modèle dérive**. Les deux ne se remplacent pas.

**Granularité.** La relance porte sur une **équipe** — la feuille de l'arbre exigence → activité → équipe, c'est-à-dire le niveau exact où le verdict se saisit et où vivent les ABS/PBS/OBS. Pas de relance au niveau d'une exigence entière ni d'une activité : chaque feuille se relance pour elle-même, et les feuilles voisines ne bougent pas.

**Deux cas d'entrée.**

- Cas A — le système a un modèle : la relance rejoue ce modèle. C'est le cas d'une exigence déjà dérivée automatiquement, dont on veut recalculer le résultat.
- Cas B — le système n'a pas de modèle : la relance reste possible en **empruntant** le modèle d'un autre système, désigné explicitement. ALLOC-005 n'est pas remplacée — l'allocation manuelle reste le fonctionnement par défaut d'un système sans modèle ; l'emprunt est une action délibérée, jamais une substitution automatique.

**Choix du modèle.** Proposé à chaque relance, dans les deux cas, et présenté en deux temps (DEC-047) :

1. **Les produits du système concerné**, d'abord — pour SIG, choisir entre le modèle *Urban* et le modèle *Mainline*. Ce n'est pas un emprunt : les deux sont des modèles légitimes du même système, et c'est le cas d'usage principal. Le produit du tender présélectionne le sien.
2. **Le modèle d'un autre système**, ensuite et distinctement — le cas B, l'exception. La liste doit dire laquelle des deux natures elle propose ; sans quoi emprunter devient aussi banal que choisir.

Choisir l'autre produit à la relance **ne change pas le produit du tender**, qui est figé à la création (DEC-049). La relance reste ponctuelle.

**Effet.** La relance **applique directement** son résultat : ni aperçu, ni validation intermédiaire, ni proposition soumise. Elle écrase **ABS, PBS et OBS de cette feuille, et rien d'autre**. L'équipe et la personne affectées ne sont pas touchées : re-dériver n'est pas réaffecter — pour cela il y a la réallocation. L'ordre produit est celui d'ALLOC-003, ABS → PBS → OBS.

**Condition.** La relance est **interdite dès qu'une réponse est enregistrée** sur cette feuille. Le contrôle est alors visible mais inactif, avec le motif affiché — pas masqué, sinon l'absence s'interprète comme un défaut. Cette règle est ce qui rend l'application directe sans risque : rien en aval ne peut être détruit, puisque rien en aval n'existe encore.

**Emprunt ponctuel.** Le modèle emprunté au cas B ne laisse **aucun marqueur persistant** : ni sur l'exigence, ni dans les filtres, ni à l'export. L'emprunt vaut pour cette relance seulement et ne devient pas la configuration de l'activité.

**Trace.** La relance écrit dans l'historique de branche comme toute autre action — qui, quand, quel modèle, cas A ou B. C'est le seul endroit où la provenance subsiste, et c'est voulu : l'emprunt est silencieux dans l'interface courante, pas effacé de l'historique.

**Droits.** L'équipe de gestion du projet et les contributeurs de l'activité concernée (DEC-003, DEC-012). La relance n'ouvre aucun droit nouveau et n'en retire aucun.

**Confiance.** Les scores issus d'une relance suivent ALLOC-006 et ALLOC-007 : affichés par champ, et sans jamais dispenser de la validation humaine. Une relance ne vaut pas validation.

## Relance globale au changement de modèle

ALLOC-015 — DEC-050 : les paramètres du projet permettent de **changer le modèle appliqué**, indépendamment du produit qui reste figé (DEC-049). Ce changement relance la dérivation sur **toutes les exigences du tender**.

**Elle écrase tout, réponses comprises.** C'est l'inverse exact de la relance unitaire, et c'est voulu : si le modèle du projet était le mauvais, alors toutes les dérivations produites jusque-là sont fausses, et les réponses qui s'appuient dessus le sont aussi. Même logique qu'une nouvelle version de document (DEC-027), appliquée à la cause plutôt qu'au texte.

**Conséquences à assumer à l'écran.** L'action est destructrice et doit se présenter comme telle : annoncer le nombre d'exigences touchées **et le nombre de réponses perdues** avant de confirmer, pas après. Une confirmation ordinaire ne suffit pas pour une action qui efface le travail des contributeurs.

**Les deux relances ne se remplacent pas.** L'unitaire est chirurgicale, donc protégée (ALLOC-014, interdite si réponse). La globale est un changement de prémisse du projet, donc totale. Ne pas offrir l'une comme repli de l'autre, et ne pas fusionner leurs contrôles.

À préciser avant construction, non tranché à ce stade :

- Quels états bloquent exactement. La règle dit « réponse enregistrée » ; reste à confirmer si `awaiting_qa` (question partie chez le client, aucune réponse encore) bloque ou non. Proposition : ne bloque pas.
- Relance en masse sur une sélection. Hors périmètre proposé : une feuille à la fois, conformément à la demande d'origine.
- Comportement quand le résultat est identique au précédent. Proposition : le dire explicitement plutôt que de ne rien afficher.

## États et acceptation

Conserver la distinction Incomplete / To review / To validate / Allocated ; ne pas assimiler validation de l'allocation et conformité finale.

- ALLOC-T01 : Turnkey multi-activité garde une exigence et plusieurs branches.
- ALLOC-T02 : en SIG, corriger ABS invalide ses propositions PBS/OBS dépendantes ; corriger PBS invalide OBS. Ancien ordre interdit pour SIG.
- ALLOC-T03 : activité sans modèle : travail manuel possible, autres exigences indépendantes.
- ALLOC-T04 : résultat IA complet reste à valider explicitement.
- ALLOC-T05 : personne responsable unique malgré plusieurs activités/équipes.
- ALLOC-T06 : validation sans responsable autorisée, absence affichée ; aucun blocage de validation lié au seul responsable manquant.
- ALLOC-T07 : demande sans motif explicatif refusée ; refus d'une demande restaure l'état précédent.
- ALLOC-T08 : aucune colonne/section de passe 1 dans le parcours SIG ; détail SIG direct.
- ALLOC-T09 : relancer une feuille recalcule ses seuls ABS/PBS/OBS ; l'équipe et la personne affectées sont inchangées après la relance.
- ALLOC-T10 : une feuille dont la réponse est enregistrée n'est pas relançable ; le contrôle reste visible et inactif, avec son motif.
- ALLOC-T11 : relancer une feuille ne modifie aucune feuille voisine de la même exigence.
- ALLOC-T12 : une activité sans modèle peut être relancée avec le modèle d'une autre, choisi explicitement ; l'activité reste sans modèle après coup et les exigences suivantes restent en allocation manuelle.
- ALLOC-T13 : après un emprunt, aucune trace du modèle emprunté n'apparaît sur l'exigence ni à l'export ; l'historique de branche, lui, la porte.
- ALLOC-T14 : le sélecteur de relance distingue les produits du système concerné de l'emprunt à un autre système ; le produit du tender y est présélectionné.
- ALLOC-T15 : relancer avec l'autre produit laisse le produit du tender inchangé ; rien dans le projet n'indique ensuite qu'il aurait changé.
- ALLOC-T16 : changer le modèle dans les paramètres annonce, avant confirmation, le nombre d'exigences touchées et le nombre de réponses détruites.
- ALLOC-T17 : après une relance globale, aucune exigence ne conserve de dérivation issue du modèle précédent.

Une correction des métadonnées n’est pas assimilée par défaut à une modification du texte source/de travail. Toute modification du texte/traduction entraîne une revue selon LIFE-008 ; les modifications structurelles d'allocation suivent la réallocation.
