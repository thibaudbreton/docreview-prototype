# Équipes, utilisateurs et accès

## Règles approuvées

| ID | Règle | Statut |
|---|---|---|
| ACC-001 | Plusieurs TM peuvent gérer le tender ; le créateur en fait initialement partie. | DOC/OBS |
| ACC-002 | Il reste au moins un membre de l'équipe de gestion du tender. | DOC/OBS |
| ACC-003 | Staffing permanent (écran Users), après création ; absence de staffing ne bloque pas globalement la capture. | DOC/OBS |
| ACC-004 | Personne choisie dans l'annuaire, rattachée à un sous-système et à un périmètre optionnel. | Maquette, DEC-003 |
| ACC-005 | Même personne/sous-système/périmètre non ajouté deux fois ; rattachements multiples possibles. | OBS |
| ACC-006 | Retrait d'une personne avec travail assigné exige une réaffectation préalable dans la maquette. S'applique à la personne en charge (PIC) de chaque OBS, responsable de sa conformité. | OBS + DEC-087, DEC-126 |
| ACC-007 | Un contributeur peut **tout consulter dans son tender**, mais ne peut pas modifier les autres sous-systèmes. Aucun accès aux tenders dont il n'est pas membre n'est déduit. | DEC-012 |
| ACC-008 | TM : staffing du tender, sur l'écran Users. Contributeurs : gestion des rattachements dans leur sous-système. Aucun manager de sous-système obligatoire. | DEC-003, DEC-126 |
| ACC-009 | Tous les contributeurs du sous-système peuvent répondre ; la personne responsable de l'exigence, si désignée, garde le suivi. | DEC-002/010 |
| ACC-010 | Pas de hiérarchie de permissions entre contributeurs d'un sous-système ; hiérarchie organisationnelle hors SRM. | DEC-012 |
| ACC-011 | Le TM peut saisir et modifier directement des réponses. Il ne verrouille plus rien ; il peut **corriger la conformité externe dérivée**, motif obligatoire et visible (DEC-106). | DEC-013/106 |
| ACC-012 | **Le type et la classe d'une exigence appartiennent au tender manager.** Un contributeur (le responsable d'un sous-système) les voit mais ne peut pas les modifier — ni dans le détail, ni dans la table, ni par l'action groupée « Classify », ni dans la vue Document. Ils déterminent ce que le modèle dérive pour chaque sous-système. | DEC-086, DEC-126 |
| ACC-013 | **Un contributeur ne modifie rien sur une exigence dont aucun sous-système ne lui est assigné** : il la lit (type, classe, allocation de chaque sous-système), sans aucun contrôle actif, dans le panneau comme dans la table. | DEC-100 |
| ACC-014 | **Une personne appartient à un seul sous-système.** « Son » sous-système est celui dont elle est membre (plus celui où elle est affectée) : c'est ce qui décide ACC-013. Elle n'est proposée comme PIC d'un OBS que sur ce sous-système. Un sous-système est validé par son contributeur ou par le TM ; l'aiguillage Turnkey, par le TM seul. | DEC-102/104 |

## Matrice métier

| Action | Équipe de gestion du tender / TM | Contributeur de sous-système |
|---|---|---|
| Consulter le tender | Tout le tender | Tout le tender, y compris autres sous-systèmes en lecture |
| Modifier le travail d'un sous-système | Oui au titre de gestion du tender | Seulement son ou ses sous-systèmes |
| Répondre à la conformité | Oui | Oui, dans son sous-système, même si un autre responsable est affecté |
| Remplacer/verrouiller le verdict final | Oui | Non au titre du seul rôle Contributor |
| Gérer les utilisateurs (écran Users) | Tender entier | Rattachements de son sous-système |
| Gérer documents et relation client globaux | Oui | Non au titre du simple rattachement à un sous-système |
| Valider la distribution/allocation du tender | Équipe de gestion selon DEC-009 | Ne pas déduire de la permission de répondre un droit de validation globale |

SIG dans Turnkey suit le même modèle de travail que SIG autonome, mais la gestion globale appartient à l'équipe du tender global. Un simple rattachement SIG ne donne pas les pouvoirs de TM Turnkey.

Admin/VIP restent des besoins historiques non détaillés pour le pilote ; un rôle technique Admin n'ajoute pas implicitement une autorité métier. Les anciennes restrictions de lecture entre sous-systèmes et hiérarchies manager/expert sont dépassées par les décisions utilisateur.

## Critères d'acceptation

ACC-T01 : suppression du dernier TM refusée. ACC-T02 : rattachement en double refusé. ACC-T03 : réaffecter le travail avant suppression de son responsable. ACC-T04 : contributeur SIG consulte un autre sous-système du même tender mais ne le modifie pas, y compris par requête directe. ACC-T05 : contributeur SIG peut répondre à une exigence SIG dont un collègue porte le suivi. ACC-T06 : il peut ajouter un contributeur SIG sans permission manager distincte. ACC-T07 : TM peut amorcer un sous-système vide. ACC-T08 : TM saisit/modifie une réponse. ACC-T09 : aucune fuite inter-tenders par la règle « tout voir ».

## Écart avec la maquette

Depuis le 9 octobre 2026, la maquette suit ACC-007 : un contributeur voit toutes les exigences et affectations du tender (table, vue Document, Compliance, compteurs, export), en lecture seule hors de son sous-système (ACC-013) ; « View as » ne masque ni ne caviarde plus rien et le réglage « Restricted view » est retiré. Un filtre « My sub-system », désactivé par défaut, ramène Compliance à son sous-système (DEC-126). Reste : l'écran Users conserve managerId (ACC-T06 non simulé).

ACC-T10 : le droit de valider l’allocation n’est pas conditionné à la présence d’un responsable (DEC-025). Le droit de modifier hors sous-système reste interdit au contributeur malgré la lecture globale.
