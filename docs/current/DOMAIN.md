# Modèle métier et vocabulaire

## Objets fonctionnels

| ID | Objet | Définition et statut |
|---|---|---|
| DOM-001 | Projet / tender | Dossier de travail contenant identité, documents ordonnés, mode de traitement et équipe projet. OBS |
| DOM-002 | Document / version | Un document possède plusieurs versions ; une nouvelle version ne constitue pas un autre projet. OBS/DOC |
| DOM-003 | Élément capturé | Titre, information ou exigence. L'identifiant doit rester stable lors d'une correction de type. DOC, test utilisateur session 3 |
| DOM-004 | Exigence | Élément qui peut être caractérisé, alloué et faire l'objet de réponses de conformité ; un responsable de suivi au maximum, absence permise DEC-010/025 |
| DOM-005 | Branche d'activité | Une activité associée à une exigence ; peut contenir plusieurs équipes. OBS dans Allocation |
| DOM-006 | Affectation d'équipe | Feuille de l'arbre d'allocation. Ne pas confondre équipe/service, personne responsable et rôle d'accès. DEC-010 : responsable unique au niveau exigence ; affectations multiples distinctes |
| DOM-007 | Proposition IA | Valeur proposée pour une étape ou un champ. Sa confiance ne constitue pas une validation humaine. OBS/DOC |
| DOM-008 | Réponse | Réponse de conformité, commentaire et, selon verdict, catégorie/topic. Consolidation par équipes/activités distincte du responsable unique de suivi ; DEC-014 confirme le calcul |
| DOM-009 | Verdict dérivé / final | Résultat calculé et résultat retenu au niveau exigence ; un verrou peut les rendre différents. OBS dans Allocation |
| DOM-010 | Question / réponse client | Objets identifiés avec liens vers questions, exigences et travail bloqué. DOC |
| DOM-011 | Événement d'audit | Changement avec auteur humain/machine, date, objet et ancienne/nouvelle valeur. DOC, pas de stockage réel dans le prototype |

## Axes à ne pas fusionner

- Caractérisation/allocation : Incomplete, To review, To validate, Allocated dans la spec historique et le code concerné. Les labels de toutes les surfaces doivent être vérifiés avant harmonisation (OPEN-13).
- Avancement de revue : `proposed`, `assigned`, `awaiting_answer`, `awaiting_qa`, `reassignment_needed`, `answered` dans Compliance.
- Conformité : **trois valeurs internes, deux à l’export client (DEC-001)**. Les écrans ne sont pas encore alignés. R&D Needed devient Compliant à l’export, avec warning interne uniquement (DEC-024). Pending représente l’absence de résultat complet, pas un avis de conformité.
- Obsolescence après changement documentaire : état distinct de la réponse et du verdict (LIFE-007).
- Incertitude IA : attachée à un champ/étape, distincte de l'avancement.

## Vocabulaire de rôles

Le ticket de fusion et le test utilisateur remplacent manager/expert par Contributor dans le travail de conformité. Project Manager conserve un périmètre projet. VIP/Admin sont décrits par les exigences backend, sans implémentation réelle démontrée. Les clés historiques `manager`, `expert` et `byRole:"expert"` ne prouvent pas l'existence de permissions métier distinctes.

## Identité et traçabilité pour la production — PROP

DOM-012 : relier chaque exigence à son document, sa version et son passage source ; distinguer identifiant stable et numéro de ligne affiché. La correspondance entre deux versions, notamment fusion/scission, demande OPEN-07.

DOM-013 : conserver séparément la proposition IA, la valeur retenue et l'événement de correction. Une reprise de traitement ne doit pas effacer silencieusement une décision humaine ; modalités OPEN-07/09.

## Sources

`build_merge.py:SOURCES`, `revue-documentaire.html:deriveActivityCompliance/deriveRequirementCompliance`, `compliance.html:BST/CMP`, test utilisateur session 3, ticket d'allocation à deux passes. Voir [AUDIT](AUDIT.md).

## Applicabilité et responsabilité

[Variantes de tender](TENDER-PROFILES.md) : le type n’est pas un simple libellé, il sélectionne parcours et configuration. Un tender SIG autonome n’est pas un Turnkey filtré.

DEC-010/025 : au plus un responsable de suivi par exigence, même si plusieurs équipes/activités contribuent ; l’absence de responsable ne bloque pas la validation d’allocation. Les réponses et allocations multiples ne créent pas autant de responsables. DEC-012 : tous les contributeurs d’une activité sont au même niveau ; ils consultent les autres activités sans les modifier.

La séquence historique PBS → ABS → OBS est corrigée pour SIG par DEC-008 : **ABS → PBS → OBS → personne**.

## OBS — ce que c'est, et ce que ce n'est pas

DEC-054. **OBS = Organisation Breakdown Structure.** C'est une **organisation**, jamais une personne. Dériver un OBS, c'est dire « c'est cette équipe-là qui s'en occupe » — pas « c'est cette personne qui répond ».

**Deux granularités, une même structure.** Ce ne sont pas deux notions différentes, c'est le même axe lu à deux niveaux de l'entreprise (ce qui fonde DEC-034, qui interdit de les confondre) :

| | Ce que l'OBS désigne | Où |
|---|---|---|
| **TK OBS** | Un **système ou sous-système** — une très grande équipe | Passe 1, distribution Turnkey |
| **OBS · team** | Une **équipe** au sein d'un système ou sous-système | Passe 2, modèle du système |

**La personne vient après, et séparément.** On assigne ensuite, le plus souvent, au responsable de cette équipe **dans la région où se joue le tender**. Au moment de la dérivation, l'organisation n'est pas encore rattachée à une région : la chaîne s'arrête sur une équipe, l'affectation d'une personne est une étape distincte.

**Cardinalité (DEC-055).** ABS et PBS sont **uniques** pour une exigence ; l'**OBS peut être multiple**. Une exigence concerne parfois plusieurs équipes, et chacune doit vérifier si elle est conforme : chaque organisation porte donc **sa** personne qui vérifie et **son** verdict, consolidés ensuite au niveau exigence (DEC-037, le plus restrictif gagne). Ne jamais dupliquer un ABS ou un PBS par équipe — deux équipes qui ne partageraient pas le même ABS décriraient deux exigences, pas une.

**Conséquences à tenir partout.**

- Une chaîne de dérivation se termine sur une **organisation**. Afficher un nom de personne sous un libellé OBS est l'amalgame hérité de la première version de l'application ; il est à supprimer partout où il subsiste.
- « OBS » et « affectation » ne sont pas synonymes dans les libellés, infobulles et motifs de revue. Un OBS faible veut dire que **l'organisation proposée** est peut-être la mauvaise, pas que la personne l'est.
- DEC-036 tient : ce que la passe 2 dérive est un périmètre, et un périmètre est une organisation.
- La relance porte sur l'**exigence entière** (DEC-056) : elle re-dérive ABS, PBS et l'ensemble des organisations. Relancer une organisation seule n'a pas de sens puisqu'elle partage ABS et PBS avec ses sœurs.
- **Précision de DEC-042** : la relance re-dérive bien l'OBS — c'est ce qu'un modèle d'allocation produit. Ce qu'elle ne touche pas, c'est la **personne** affectée en aval. La protection portait sur l'affectation nominative, pas sur l'organisation.
