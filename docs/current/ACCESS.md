# Équipes, casting et accès

## Règles approuvées

| ID | Règle | Statut |
|---|---|---|
| ACC-001 | Plusieurs PM peuvent gérer le projet ; le créateur en fait initialement partie. | DOC/OBS |
| ACC-002 | Il reste au moins un membre de l'équipe de gestion projet. | DOC/OBS |
| ACC-003 | Casting permanent, après création ; absence de staffing ne bloque pas globalement la capture. | DOC/OBS |
| ACC-004 | Personne choisie dans l'annuaire, rattachée à un système et à un périmètre optionnel. | Maquette, DEC-003 |
| ACC-005 | Même personne/système/périmètre non ajouté deux fois ; rattachements multiples possibles. | OBS |
| ACC-006 | Retrait d'une personne avec travail assigné exige une réaffectation préalable dans la maquette. Appliquer au responsable unique de l'exigence. | OBS + DEC-010 |
| ACC-007 | Un contributeur peut **tout consulter dans son projet**, mais ne peut pas modifier les autres systèmes. Aucun accès aux projets dont il n'est pas membre n'est déduit. | DEC-012 |
| ACC-008 | PM : casting du projet. Contributeurs : gestion des rattachements dans leur système. Aucun manager de système obligatoire. | DEC-003 |
| ACC-009 | Tous les contributeurs du système peuvent répondre ; la personne responsable de l'exigence, si désignée, garde le suivi. | DEC-002/010 |
| ACC-010 | Pas de hiérarchie de permissions entre contributeurs d'un système ; hiérarchie organisationnelle hors SRM. | DEC-012 |
| ACC-011 | Le PM peut saisir et modifier directement des réponses, en plus de remplacer/verrouiller le verdict final. | DEC-013 |

## Matrice métier

| Action | Équipe de gestion du projet / PM | Contributeur de système |
|---|---|---|
| Consulter le projet | Tout le projet | Tout le projet, y compris autres systèmes en lecture |
| Modifier le travail d'un système | Oui au titre de gestion du projet | Seulement son ou ses systèmes |
| Répondre à la conformité | Oui | Oui, dans son système, même si un autre responsable est affecté |
| Remplacer/verrouiller le verdict final | Oui | Non au titre du seul rôle Contributor |
| Gérer le casting | Projet entier | Rattachements de son système |
| Gérer documents et relation client globaux | Oui | Non au titre du simple rattachement à un système |
| Valider la distribution/allocation projet | Équipe de gestion selon DEC-009 | Ne pas déduire de la permission de répondre un droit de validation globale |

SIG dans Turnkey suit le même modèle de travail que SIG autonome, mais la gestion globale appartient à l'équipe du projet global. Un simple rattachement SIG ne donne pas les pouvoirs de PM Turnkey.

Admin/VIP restent des besoins historiques non détaillés pour le pilote ; un rôle technique Admin n'ajoute pas implicitement une autorité métier. Les anciennes restrictions de lecture entre systèmes et hiérarchies manager/expert sont dépassées par les décisions utilisateur.

## Critères d'acceptation

ACC-T01 : suppression du dernier PM refusée. ACC-T02 : rattachement en double refusé. ACC-T03 : réaffecter le travail avant suppression de son responsable. ACC-T04 : contributeur SIG consulte un autre système du même projet mais ne le modifie pas, y compris par requête directe. ACC-T05 : contributeur SIG peut répondre à une exigence SIG dont un collègue porte le suivi. ACC-T06 : il peut ajouter un contributeur SIG sans permission manager distincte. ACC-T07 : PM peut amorcer un système vide. ACC-T08 : PM saisit/modifie une réponse. ACC-T09 : aucune fuite inter-projets par la règle « tout voir ».

## Écart avec la maquette

`canAnswer/passesB` restreint actuellement certaines lectures ; Casting conserve managerId. La cible DEC ci-dessus prime ; le code reste inchangé dans cette tâche.

ACC-T10 : le droit de valider l’allocation n’est pas conditionné à la présence d’un responsable (DEC-025). Le droit de modifier hors système reste interdit au contributeur malgré la lecture globale.
