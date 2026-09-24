# Revue et conformité — spec pilote

## Objet et frontière

Permettre aux contributeurs de répondre et aux responsables projet de suivre la conformité. La conformité n'est pas une étape IA de création du projet : elle se construit au fil des réponses humaines. L'IA de recherche, si retenue, aide à documenter une réponse ; la consolidation est une règle métier.

## Décisions métier — DEC-001 et DEC-024, échelle interne et export client

| Surface | Verdicts observés | Consolidation observée |
|---|---|---|
| `compliance.html` | Compliant / Not Compliant ; R&D dans le commentaire Compliant | Branches → exigence, fonction `consolidate` |
| `revue-documentaire.html` | Compliant / R&D Needed / Not Compliant | Équipes → systèmes → exigence, fonctions `deriveActivityCompliance` et `deriveRequirementCompliance` |

Le ticket de fusion demande explicitement deux verdicts ; le ticket d'allocation à deux passes conserve une règle qui a été implémentée à trois valeurs dans Allocation. L’utilisateur a précisé le 8 septembre 2026 : **trois verdicts en interne (Compliant / R&D Needed / Not Compliant), deux à l’export client (Compliant / Not Compliant)**. L’écart entre écrans ne se résout donc pas en supprimant R&D partout. DEC-013 confirme une conversion automatique à l’export, avec warning interne uniquement. DEC-024 précise la destination : **Compliant**. Le verdict interne reste R&D Needed ; l’export ne le réécrit pas dans les données internes.

## Règles

| ID | Règle | Statut |
|---|---|---|
| CONF-001 | L'avancement et le verdict sont deux axes distincts. `awaiting_qa` n'est pas un verdict. | OBS/DOC |
| CONF-002 | Une réponse manquante maintient son agrégat en attente. Dans l'arbre à deux niveaux, cette attente remonte jusqu'à l'exigence. | OBS, mécanismes différents selon écran |
| CONF-003 | En interne, une fois toutes les réponses présentes : Not Compliant > R&D Needed > Compliant. La règle de priorité est observée dans Allocation ; DEC-001 confirme les trois valeurs internes. | DEC-014 confirme la priorité et la propagation de pending |
| CONF-004 | Le système est calculé depuis les équipes et l'exigence depuis les systèmes ; le système n'est pas un verdict saisi séparément. | DEC-014 ; dans SIG autonome, équipes → exigence |
| CONF-005 | Le verrou métier porte sur le verdict final de l'exigence. Les réponses et le résultat dérivé continuent d'évoluer dessous. | OBS Allocation / DOC |
| CONF-006 | Déverrouiller remet le verdict final en cohérence avec le résultat dérivé courant. | OBS Allocation |
| CONF-007 | Le PM peut saisir/modifier une réponse, remplacer et verrouiller le final. | DEC-013 ; contrôle serveur à construire |
| CONF-008 | Champs de la maquette : Compliant, commentaire facultatif ; Not Compliant, Category sélectionnée et Topic obligatoire (`v-submit-notcompliant`). R&D est conservé en interne ; pas de nouveaux champs inventés. | DEC-013 renvoie à la maquette ; liste Category marquée placeholder dans le code, OPEN-04 résiduel |
| CONF-009 | Le commentaire est accessible dans la table sans ouvrir le panneau. | OBS/DOC |
| CONF-010 | Tous les contributeurs du système peuvent répondre, même si une autre personne est affectée. La personne affectée reste responsable du suivi. | DEC-002 |
| CONF-011 | Les motifs de réaffectation sont mauvaise personne, mauvais système, système non applicable. La demande comporte une justification. | OBS |
| CONF-012 | Une réaffectation interne et une question au client sont deux processus distincts. | OBS/DOC |
| CONF-013 | Le dossier est complet quand toutes les réponses de conformité sont données ; le PM peut encore modifier. La complétude ne crée pas un verrou automatique. | DEC-014 |
| CONF-014 | Une version modifiant l’exigence déverrouille automatiquement son verdict final et le remet pending. | DEC-016 |
| CONF-015 | R&D est converti automatiquement pour l’export client ; warning visible en interne uniquement, jamais dans le livrable client. Destination : **Compliant** (DEC-024). | DEC-013 |

## Parcours de saisie

1. Accéder à Compliance avec le périmètre utilisateur.
2. Sélectionner une exigence et l'affectation concernée.
3. Lire le contexte Document. REX/Chat restent des éléments de maquette hors V1 (DEC-021).
4. Saisir le verdict et ses informations associées.
5. Enregistrer ; la réponse et les indicateurs se mettent à jour.

OBS : REX est alimenté par exemples, Chat est un stub, les rappels et exports ne prouvent pas une intégration réelle. Le formulaire actuel est conditionné par les branches de rendu ; cela ne limite pas le droit de modification PM confirmé par DEC-013.

## Lisibilité du panneau de détail

Revue UX du 21 septembre 2026, sur le cas le plus chargé : une exigence dont le verdict externe dévie de l'interne avec un risque accepté. Le panneau ouvrait sur **trois pastilles de verdict** — l'interne consolidée à côté de l'identifiant, l'externe, puis celle de l'affectation plus bas — sans qu'aucune ne dise laquelle fait foi. Sur une exigence à une seule affectation, la première et la troisième portaient **la même valeur**, à trois cents pixels d'écart et sous deux libellés différents. S'y ajoutaient une étiquette rouge « ≠ internal », un encadré ambre à triangle d'alerte autour d'une décision délibérée, et un gros bouton bleu « Escalate to client Q&A » — l'action la plus visible de l'écran, au moment précis où c'est la mauvaise.

Les règles qui en sortent :

| ID | Règle |
|---|---|
| CONF-016 | **Une seule pastille en tête : celle que le client reçoit.** C'est la question à laquelle le panneau existe pour répondre. Le verdict interne est énoncé **en toutes lettres** dessous, comme contexte, pas comme titre concurrent. |
| CONF-017 | **La déviation est une décision, pas une alerte.** Un liseré ambre et une phrase qui la nomme ; ni triangle d'avertissement, ni fond d'alerte. Le risque accepté se lit comme la justification enregistrée qu'il est. |
| CONF-018 | **Un verdict n'est affiché qu'une fois par portée.** Le verdict propre à une affectation n'apparaît que lorsqu'il y en a **plusieurs** — avec une seule, il répète celui de l'exigence. |
| CONF-019 | **Le panneau dit en une phrase ce qui est attendu**, dans tous ses états, y compris « rien ». Sans quoi l'absence d'action se déduit de l'absence de bouton, ce qui ne se distingue pas d'un écran incomplet. |
| CONF-020 | **La hiérarchie des actions suit cette phrase.** L'action nommée est primaire, les autres restent disponibles en secondaire. Une position déjà arbitrée avec son risque n'a **pas** d'action primaire : escalader n'y est plus la suite logique. |
| CONF-021 | Aucun écran ne propose à quelqu'un une action **adressée à lui-même** — pas de bouton de relance chez la personne dont on attend précisément la réponse. |
| CONF-022 | DEC-078 : **l'écran Compliance est allégé et suit la structure du document.** La table est par défaut en ordre du document, avec les titres de document et de section en lignes (les autres tris restent à plat). Plus de statut « overdue » ni « outdated version » (pastilles, marques, filtres, tri, fil d'activité), plus de bouton « Needs my action », plus d'onglet Document, plus de bloc « What the client receives » en tête du panneau — les colonnes External compliance et Risk accepted le portent, et le formulaire de déclaration s'ouvre toujours depuis l'action proposée. Un interrupteur « Wrap text » affiche le texte complet. **Remplace CONF-016** sur la pastille en tête. |
| CONF-023 | DEC-079 : **panneau de décision du contributeur** ([SPEC](../specs/SPEC-compliance-decision-panel.md)). Quand un contributeur ouvre une affectation qui attend son verdict : la file (« N left · this is k of N », Next), une ligne « Yours », le texte de l'exigence en entier et dominant, puis la décision — une seule action primaire, **Compliant en un geste, Not compliant en deux** (Category + Topic). Une phrase rappelle que le verdict interne est la vérité technique et que ce que reçoit le client relève du chef de projet. Deux actions secondaires plus discrètes : **Ask the client** et **Not mine — return it** (les trois motifs). Le reste est consultation, repliée : Document, Similar, REX, Chat. Le brouillon s'enregistre tout seul ; **Set aside** (icône, touche S) est un marqueur personnel. Le panneau peut s'élargir. Le panneau du chef de projet ne change pas. |

## Transitions

| État avant | Action | État/effet attendu | Base |
|---|---|---|---|
| En attente de réponse | Enregistrer une réponse valide | `answered`, consolidation recalculée | OBS |
| En attente de réponse | Demander réaffectation justifiée | `reassignment_needed` | OBS |
| Réaffectation demandée | Résolution autorisée | Retour à `awaiting_answer` pour la nouvelle affectation | OBS ; mécanisme de réallocation ALLOC-013 |
| Réponse requérant clarification | Créer une question client liée | `awaiting_qa` sur le travail lié | DOC/interaction simulée |
| `awaiting_qa` | Réponse client associée et validée | Retour au travail de revue, sans verdict automatique | DOC, QA-006 |
| Verdict final verrouillé | Modifier une réponse sous-jacente | Dérivé recalculé, final inchangé | OBS Allocation |
| Verdict final verrouillé | Déverrouiller | Final reprend le dérivé courant | OBS Allocation |

Le code permet certains chemins depuis `proposed` ; cela ne valide pas leur autorisation en production. La maquette demeure la référence d’interaction ; le PM peut modifier même après complétude du dossier (DEC-013/014).

## Scénarios d'acceptation

| Cas | Situation | Résultat |
|---|---|---|
| CONF-T01 | Deux équipes répondent Compliant | Système Compliant selon CONF-004 |
| CONF-T02 | Une répond Compliant, l'autre n'a pas répondu | Système puis exigence en attente |
| CONF-T03 | Toutes ont répondu, une Not Compliant | Verdict dérivé Not Compliant |
| CONF-T04 | Plusieurs systèmes complets, un Not Compliant | Exigence Not Compliant |
| CONF-T05 | Final verrouillé Compliant, une équipe passe Not Compliant | Dérivé Not Compliant ; final Compliant ; verrou visible |
| CONF-T06 | Déverrouillage de CONF-T05 | Final Not Compliant |
| CONF-T07 | Système hors périmètre | Lecture/action selon matrice ACCESS ; aucune extension des droits par filtre |
| CONF-T08 | Réponse à la question bloquante | Revue débloquée, aucun verdict créé automatiquement |
| CONF-T09 | Toutes les réponses présentes, une R&D Needed et aucune Not Compliant | Dérivé interne R&D Needed ; verdict client Compliant avec warning interne seulement, DEC-024 |
| CONF-T10 | Aucune affectation | Distinguer absence de responsable (validation autorisée DEC-025) et absence de réponse/affectation : aucune conformité acquise sans les réponses attendues |

Ces scénarios sont des critères proposés à partir des règles indiquées, pas des tests exécutés ni une recette utilisateur.

## Production — PROP

Distinguer le verrou métier d'une protection contre deux éditions simultanées. Présenter les erreurs d'enregistrement et conflits sans annoncer une réussite ni perdre la saisie. Auditer réponse, remplacement, verrou et déverrouillage. Ne pas synchroniser les écrans via des copies indépendantes de la même exigence.

## Sources

`compliance.html:CMP/CMP_ORDER/consolidate/canAnswer/renderPanel2`, `revue-documentaire.html:consolidateCompliance/deriveRequirementCompliance`, tickets fusion Compliance et allocation à deux passes.

## Cas complémentaires approuvés

CONF-T15 : le panneau n'affiche jamais deux pastilles de verdict portant la même valeur pour la même portée. CONF-T16 : dans chacun de ses états — en attente, sans réponse, bloqué sur le client, retourné, répondu, arbitré — le panneau porte exactement une phrase disant ce qui est attendu. CONF-T17 : sur une exigence dont la déclaration externe est arbitrée et justifiée, aucun bouton primaire n'est proposé. CONF-T18 : la vue du contributeur qui doit répondre ne lui propose pas de se relancer lui-même.

CONF-T11 : nouvelle version modifiant une exigence verrouillée → déverrouillage automatique et verdict pending. CONF-T12 : toutes réponses présentes → dossier complet, modification PM encore possible. CONF-T13 : export d’un R&D → conversion automatique en Compliant, warning interne absent du fichier client. CONF-T14 : contributeur d’un autre système consulte mais ne modifie pas ; le PM peut modifier.

Conformité et export client sont documentés pour la suite ; le premier pilote s’arrête à la validation d’allocation (DEC-022).

CONF-T15 : export d’un résultat interne R&D Needed produit Compliant côté client, laisse R&D Needed en interne et exclut le warning du fichier. Le warning automatique est distinct des commentaires saisis ; la politique des contributions en anglais reste LANG-003.
