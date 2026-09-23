# Allocation et validation humaine

Applicabilité : [variantes de tender](TENDER-PROFILES.md). Le prototype est la référence Turnkey ; ne pas en reproduire la passe 1 dans un tender SIG.

## Règles

| ID | Règle | Statut et portée |
|---|---|---|
| ALLOC-001 | Turnkey distribue entre systèmes, puis applique leur modèle. Un tender SIG commence directement dans SIG. | DEC-005/006, DOC autres non-Turnkey |
| ALLOC-002 | Passe 1 Turnkey : classe technique vers PBS, non technique vers ABS, puis système TK OBS — affiché dans la colonne System, avec la certitude du routage à côté (DEC-077 ; il n'y a plus de colonne TK OBS). Cette distinction ne s'applique pas à l'allocation SIG. | DOC passe 1, DEC-008 exclusion SIG |
| ALLOC-003 | Allocation SIG : **ABS → PBS → OBS → personne**. Aucune différence de chaîne technique/non technique. Corriger un champ invalide les propositions qui en dépendent ; les corrections de décisions déjà validées suivent LIFE-008. | DEC-008 prime sur l'ancien PBS → ABS → OBS |
| ALLOC-004 | Distribution multiple entre systèmes en Turnkey, puis affectations d'équipes ; ne pas dupliquer l'exigence pour représenter les branches. | DOC, consolidation confirmée DEC-014 |
| ALLOC-005 | Système sans modèle : allocation manuelle, identifiée et filtrable, sans bloquer les autres systèmes. | DOC ; contenu/gestion des modèles hors spec fonctionnelle |
| ALLOC-006 | Incertitude affichée par champ/étape applicable ; aucun indicateur de passe 1 en SIG. | DOC/DEC-006 |
| ALLOC-007 | La confiance IA ne remplace pas la validation humaine de l'allocation. | DOC, borne du pilote DEC-022 |
| ALLOC-008 | La validation d'allocation rend le travail disponible pour la suite de conformité ; pas de construction de Compliance exigée dans le premier pilote. | DOC + DEC-022 |
| ALLOC-009 | Les exigences progressent indépendamment. Un cas incomplet n'arrête pas les autres. | DOC |
| ALLOC-010 | L’allocation peut être validée sans responsable. L’absence reste visible, sans bloquer cette exigence ni les autres. | DEC-025 |
| ALLOC-011 | **Au plus une personne responsable du suivi par exigence**, pas une par système ou équipe. Tous les contributeurs du système peuvent répondre. | DEC-010 + DEC-002 |
| ALLOC-012 | La validation relève de l'équipe de gestion du projet, composée de bid managers et requirement managers de SIG selon la réponse utilisateur. Ces fonctions ne créent pas une hiérarchie des contributeurs. | DEC-009 ; portée générale aux autres types OPEN-15 |

## Absence de responsable — décision

DEC-025 : absence autorisée, y compris après validation d’allocation. Afficher « Non désigné » et permettre d’isoler ces exigences avec le filtre de champ vide existant ; ne pas ajouter de validation bloquante. Les contributeurs gardent leurs droits dans leur système. Un responsable peut être désigné ensuite ; il devient l’unique responsable du suivi. La proposition de blocage formulée précédemment a été refusée.

## Réallocation — référence vérifiée dans la maquette

ALLOC-013 — DEC-011 : conserver le mécanisme de demande de réallocation de la maquette, pas inventer une nouvelle interaction.

- Motifs : bon système/mauvaise personne ; mauvais système ; système non applicable.
- Justification requise ; proposer une personne de remplacement pour le premier, un système de remplacement pour les deux autres dans le parcours Turnkey.
- La demande passe à `reassignment_needed`. La maquette offre approbation/refus.
- Approbation personne : remplacement du responsable, travail remis à disposition. Le code historique utilise des identifiants équipe/personne incohérents par écran ; ne pas reproduire cette duplication avec DEC-010.
- Approbation système : remplacement de la branche, état proposé/en attente et nouvelle allocation. La maquette remplace au lieu de laisser zéro système.
- Refus : retour à l'état antérieur.
- La gestion projet reçoit les demandes au niveau global ; les anciens rôles manager/expert du code ne recréent pas une hiérarchie métier après DEC-003/012.

Dans un tender SIG, les actions de distribution Turnkey sont absentes (DEC-006). Ne pas laisser un menu de changement de système qui lancerait la passe 1. Les cas hors système en standalone devront être explicités si nécessaires (OPEN-15), sans inventer leur équivalent.

Sources : `revue-documentaire.html:renderReassignForm/submitReassignRequest/approveReassign/rejectReassign`, `compliance.html:reassign-submit`. Inspection du code ; pas de recette navigateur.

## Relance d'une passe d'allocation

ALLOC-014 — DEC-040 à DEC-043 : rejouer un modèle d'allocation sur une exigence déjà traitée, en choisissant lequel. Mécanisme distinct de la réallocation (ALLOC-013) : la réallocation change **qui** répond, la relance recalcule **ce que le modèle dérive**. Les deux ne se remplacent pas.

**Granularité (DEC-056, remplace DEC-040 sur ce point).** La relance porte sur l'**exigence** au sein de son système : elle re-dérive **ABS, PBS et l'ensemble des organisations**. La granularité « équipe » de DEC-040 reposait sur l'idée que les ABS/PBS/OBS vivaient à la feuille ; DEC-055 établit que seuls les OBS s'y trouvent — ABS et PBS sont uniques pour l'exigence. Relancer une organisation isolément n'a donc pas de sens : elle partage son ABS et son PBS avec ses sœurs. Elle est bloquée dès qu'**une seule** de ses organisations l'est, puisqu'elle les réécrit toutes.

**Deux cas d'entrée.**

- Cas A — le système a un modèle : la relance rejoue ce modèle. C'est le cas d'une exigence déjà dérivée automatiquement, dont on veut recalculer le résultat.
- Cas B — le système n'a pas de modèle : la relance reste possible en **empruntant** le modèle d'un autre système, désigné explicitement. ALLOC-005 n'est pas remplacée — l'allocation manuelle reste le fonctionnement par défaut d'un système sans modèle ; l'emprunt est une action délibérée, jamais une substitution automatique.

**Choix du modèle.** Proposé à chaque relance, dans les deux cas, et présenté en deux temps (DEC-047) :

1. **Les produits du système concerné**, d'abord — pour SIG, choisir entre le modèle *Urban* et le modèle *Mainline*. Ce n'est pas un emprunt : les deux sont des modèles légitimes du même système, et c'est le cas d'usage principal. Le produit du tender présélectionne le sien.
2. **Le modèle d'un autre système**, ensuite et distinctement — le cas B, l'exception. La liste doit dire laquelle des deux natures elle propose ; sans quoi emprunter devient aussi banal que choisir.

Choisir l'autre produit à la relance **ne change pas le produit du tender**, qui est figé à la création (DEC-049). La relance reste ponctuelle.

**Effet.** La relance **applique directement** son résultat : ni aperçu, ni validation intermédiaire, ni proposition soumise. Elle écrase **l'ABS, le PBS et l'ensemble des OBS de l'exigence, et rien d'autre**. L'équipe et la personne affectées ne sont pas touchées : re-dériver n'est pas réaffecter — pour cela il y a la réallocation. L'ordre produit est celui d'ALLOC-003, ABS → PBS → OBS.

**Condition.** La relance est **interdite dès qu'une réponse est enregistrée** sur l'une quelconque de ses organisations. Le contrôle est alors visible mais inactif, avec le motif affiché — pas masqué, sinon l'absence s'interprète comme un défaut. Cette règle est ce qui rend l'application directe sans risque : rien en aval ne peut être détruit, puisque rien en aval n'existe encore.

**Emprunt ponctuel.** Le modèle emprunté au cas B ne laisse **aucun marqueur persistant** : ni sur l'exigence, ni dans les filtres, ni à l'export. L'emprunt vaut pour cette relance seulement et ne devient pas la configuration du système.

**Trace.** La relance écrit dans l'historique de branche comme toute autre action — qui, quand, quel modèle, cas A ou B. C'est le seul endroit où la provenance subsiste, et c'est voulu : l'emprunt est silencieux dans l'interface courante, pas effacé de l'historique.

**Droits.** L'équipe de gestion du projet et les contributeurs du système concerné (DEC-003, DEC-012). La relance n'ouvre aucun droit nouveau et n'en retire aucun.

**Où se trouve le contrôle.** En tête du bloc de qualification pour le PM sur un tender à un système ; **sur chaque carte système** dans la vue PM d'un Turnkey, puisque chaque système a son propre modèle ; en tête de la vue contributeur. Un contrôle réservé au détail d'un système, un clic plus loin, n'a pas été trouvé à l'usage (23 septembre 2026). La relance **en masse** ne touche que les exigences : blocs d'information et titres sont écartés et comptés à part.

**Confiance.** Les scores issus d'une relance suivent ALLOC-006 et ALLOC-007 : affichés par champ, et sans jamais dispenser de la validation humaine. Une relance ne vaut pas validation.

## Titres et blocs d'information

ALLOC-018 — DEC-073 : **un titre ou un bloc d'information n'a pas de statut.** Seules les exigences portent Incomplete / To review / To validate / Allocated. Si l'IA n'est pas sûre qu'un bloc soit un titre, une information ou une exigence, c'est la puce de type qui le dit (bordure en pointillés) ; choisir le type en place le confirme, en choisir un autre le reclasse. Critère : ALLOC-T24 — aucun titre ni bloc d'information n'affiche de pastille de statut, dans aucune vue.

## Dérivation sur les clés

ALLOC-017 — DEC-061/062 : sur un tender dont le produit a des clés ([KEYS](KEYS.md)), la chaîne ABS → PBS → OBS se choisit dans les listes cochées pour ce produit, jamais en texte libre. L'OBS proposé en premier est celui rangé sous l'ABS de l'exigence, comme dans le classeur ; les autres restent accessibles. La relance dérive de même l'OBS sous l'ABS qu'elle vient de dériver. Le PBS est un élément produit (DEC-062). Les valeurs Functional / Performance / Security / Interface / Regulatory, que le prototype affichait d'abord sous « PBS » puis sous « Nature », **ne font plus partie d'Allocation** (DEC-074).

**Nature et classe (DEC-074).** La **nature** d'un bloc, c'est ce qu'il est : **Information, Heading ou Requirement** — rien d'autre. Elle se lit et se corrige dans le détail, en tête, et **n'a pas de colonne dans la table**. La **classe** (technique / non technique) s'affiche dans le détail de toute exigence, juste en dessous — elle n'y figurait que dans la vue du chef de projet Turnkey, si bien qu'un tender SIG ne la montrait pas. Une nature ou une classe détectée par l'IA le dit, avec un bouton pour la confirmer. Critères : ALLOC-T25 — le détail d'une exigence montre Nature (trois valeurs) et Class, sur tout tender ; ALLOC-T26 — aucune colonne Nature dans la table, et aucune valeur Functional / Performance / Security / Interface / Regulatory dans Allocation.

ALLOC-019 — DEC-075 : **changer la nature ou la classe propose de relancer le modèle.** Une ligne colorée « ↻ Re-run the model » s'affiche au-dessus d'ABS, PBS et OBS, avec la raison (nature changed / class changed). Rien n'est relancé tout seul. Elle disparaît quand la caractérisation revient à celle de la dérivation, ou après une relance, quelle que soit sa voie. Relance bloquée : la même ligne le dit, sans bouton. Critère : ALLOC-T27 — basculer la classe d'une exigence SIG non répondue affiche le bouton ; le cliquer re-dérive ABS / PBS / OBS et le bouton disparaît ; sur une exigence répondue, la ligne dit « re-run blocked ».

ALLOC-020 — DEC-076 : **tout OBS et tout système se supprime, jusqu'à zéro.** Le ✕ est sur chaque ligne de la liste OBS (SIG comme Turnkey) et de la liste System du Turnkey. Plus rien : la liste le dit (« No role yet », « No system yet ») et l'exigence est Incomplete. Une entrée déjà répondue demande confirmation. Critère : ALLOC-T28 — sur une exigence SIG à un seul OBS, le ✕ est présent et le retire ; sur une exigence Turnkey à deux systèmes, les deux se retirent et l'exigence passe Incomplete. Le chef de projet ajoute un système directement (« + Add system », recherche sur le code et le nom), y compris sur une exigence qui n'en a plus ; seul le contributeur passe par une proposition (« + Missing system »).

## Une allocation par organisation

ALLOC-016 — DEC-060 : **une allocation est une organisation et la personne qui y répond.** Une exigence qui atteint trois organisations est **trois allocations à faire**, et le compte affiché est celui des organisations, pas celui des systèmes.

Il y avait auparavant deux blocs disant la même chose : la liste des organisations d'un côté, un bloc « qui vérifie » de l'autre, qui reprenait la même liste pour y accrocher une personne. **DEC-060 remplace DEC-057** : il n'y a pas de bloc d'affectations séparé, c'est l'allocation elle-même qui porte sa personne.

Ce que cela implique :

- Le libellé de chaque allocation est **l'organisation**, pas le système. Le système reste affiché en étiquette là où il distingue quelque chose — un Turnkey, ou une exigence qui atteint plusieurs systèmes — et disparaît là où il serait le même code sur toutes les cartes.
- Le statut et le verdict se lisent **par organisation**, puisque chacune répond pour elle-même et que les verdicts se consolident ensuite (DEC-055, DEC-037).
- L'étape OBS de la chaîne de dérivation **reste** : elle est la lecture de ce que le modèle a dérivé, avec ses scores de confiance et ses ajouts/retraits. L'allocation, elle, est le travail qui en découle. Les deux se ressemblent parce que l'une décrit ce que l'autre traite ; elles ne se dupliquent pas.
- Sur une exigence à **une seule** organisation dans **un seul** système, la personne affectée à l'allocation est aussi la personne de l'exigence : les deux champs ne peuvent pas diverger sans que l'un des deux mente.

## Relance globale au changement de modèle

ALLOC-015 — DEC-050 : les paramètres du projet permettent de **changer le modèle appliqué**, indépendamment du produit qui reste figé (DEC-049). Ce changement relance la dérivation sur **toutes les exigences du tender**.

**Elle écrase tout, réponses comprises.** C'est l'inverse exact de la relance unitaire, et c'est voulu : si le modèle du projet était le mauvais, alors toutes les dérivations produites jusque-là sont fausses, et les réponses qui s'appuient dessus le sont aussi. Même logique qu'une nouvelle version de document (DEC-027), appliquée à la cause plutôt qu'au texte.

**Conséquences à assumer à l'écran.** L'action est destructrice et doit se présenter comme telle : annoncer le nombre d'exigences touchées **et le nombre de réponses perdues** avant de confirmer, pas après. Une confirmation ordinaire ne suffit pas pour une action qui efface le travail des contributeurs.

**Les deux relances ne se remplacent pas.** L'unitaire est chirurgicale, donc protégée (ALLOC-014, interdite si réponse). La globale est un changement de prémisse du projet, donc totale. Ne pas offrir l'une comme repli de l'autre, et ne pas fusionner leurs contrôles.

**Ce qui bloque, précisément** (DEC-051). Une réponse enregistrée, et **aussi l'attente d'une réponse du client** (`awaiting_qa`). Une question en vol suppose que le client a été interrogé sur la dérivation actuelle ; la changer sous la question rendrait sa réponse inexploitable. Les états qui ne bloquent pas : proposé, assigné, en attente de réponse du contributeur, réallocation demandée.

**Relance en masse** (DEC-052). Disponible depuis la barre d'actions groupées de la table, sur une sélection. Même règle de blocage feuille par feuille : les feuilles bloquées sont sautées et comptées, jamais relancées de force. Couvre le cas « dix exigences mal dérivées » sans passer par un changement de modèle global, qui lui est destructeur.

**Résultat identique** (DEC-053). Aucun traitement particulier : même retour que toute relance. La trace dans l'historique suffit à établir qu'elle a eu lieu.

## États et acceptation

Conserver la distinction Incomplete / To review / To validate / Allocated ; ne pas assimiler validation de l'allocation et conformité finale.

- ALLOC-T01 : Turnkey multi-système garde une exigence et plusieurs branches.
- ALLOC-T02 : en SIG, corriger ABS invalide ses propositions PBS/OBS dépendantes ; corriger PBS invalide OBS. Ancien ordre interdit pour SIG.
- ALLOC-T03 : système sans modèle : travail manuel possible, autres exigences indépendantes.
- ALLOC-T04 : résultat IA complet reste à valider explicitement.
- ALLOC-T05 : personne responsable unique malgré plusieurs systèmes/équipes.
- ALLOC-T06 : validation sans responsable autorisée, absence affichée ; aucun blocage de validation lié au seul responsable manquant.
- ALLOC-T07 : demande sans motif explicatif refusée ; refus d'une demande restaure l'état précédent.
- ALLOC-T08 : aucune colonne/section de passe 1 dans le parcours SIG ; détail SIG direct.
- ALLOC-T09 : relancer une exigence recalcule ses seuls ABS/PBS/OBS ; les personnes affectées à chacune de ses organisations sont inchangées après la relance.
- ALLOC-T10 : une exigence dont une organisation a enregistré sa réponse n'est pas relançable ; le contrôle reste visible et inactif, avec son motif.
- ALLOC-T11 : relancer une exigence ne modifie aucune autre exigence ; à l'intérieur, elle re-dérive bien toutes ses organisations, jamais une seule.
- ALLOC-T12 : un système sans modèle peut être relancé avec le modèle d'un autre, choisi explicitement ; le système reste sans modèle après coup et les exigences suivantes restent en allocation manuelle.
- ALLOC-T13 : après un emprunt, aucune trace du modèle emprunté n'apparaît sur l'exigence ni à l'export ; l'historique de branche, lui, la porte.
- ALLOC-T14 : le sélecteur de relance distingue les produits du système concerné de l'emprunt à un autre système ; le produit du tender y est présélectionné.
- ALLOC-T15 : relancer avec l'autre produit laisse le produit du tender inchangé ; rien dans le projet n'indique ensuite qu'il aurait changé.
- ALLOC-T16 : changer le modèle dans les paramètres annonce, avant confirmation, le nombre d'exigences touchées et le nombre de réponses détruites.
- ALLOC-T17 : après une relance globale, aucune exigence ne conserve de dérivation issue du modèle précédent.
- ALLOC-T18 : le nombre d'allocations affiché égale le nombre d'organisations de l'exigence, et non celui de ses systèmes.
- ALLOC-T19 : aucun écran ne propose deux endroits pour désigner la personne d'une même organisation.
- ALLOC-T20 : affecter une personne sur une exigence à organisation unique donne la même personne partout où l'exigence l'affiche — table comprise.
- ALLOC-T21 : supprimer des organisations jusqu'à n'en garder qu'une rend à la table la personne de celle qui reste.
- ALLOC-T22 : une relance en masse ne dérive rien sur un bloc qui n'est pas une exigence.
- ALLOC-T23 : le contrôle de relance est visible sans navigation supplémentaire pour le PM (y compris sur un Turnkey) comme pour le contributeur du système.

Une correction des métadonnées n’est pas assimilée par défaut à une modification du texte source/de travail. Toute modification du texte/traduction entraîne une revue selon LIFE-008 ; les modifications structurelles d'allocation suivent la réallocation.
