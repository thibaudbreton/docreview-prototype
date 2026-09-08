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

Une correction des métadonnées n’est pas assimilée par défaut à une modification du texte source/de travail. Toute modification du texte/traduction entraîne une revue selon LIFE-008 ; les modifications structurelles d'allocation suivent la réallocation.
