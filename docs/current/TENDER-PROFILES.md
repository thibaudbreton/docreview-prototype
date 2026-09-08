# Variantes par type de tender

## Décisions de référence

DEC-004 : les types à couvrir sont **Turnkey, SIG, Mainline, RSC** (réponse utilisateur 1).
DEC-005 : le modèle et les actions de SIG sont les mêmes en tender SIG autonome et dans l'activité SIG d'un Turnkey. Dans le second cas, les contributeurs SIG ne gèrent pas le projet global : documents, équipes au niveau projet et relation client (réponse 2). Cela n'enlève pas leur droit de gérer les rattachements de leur propre activité (DEC-003).
DEC-006 : SIG conserve tous les écrans ; retirer de l'interface tout ce qui concerne la passe 1 Turnkey, dont ses ABS/PBS/OBS spécifiques. Le panneau de détail s'ouvre directement dans la configuration SIG (réponses 3–4).
DEC-007 : le type sélectionne automatiquement la configuration/référentiels et modèles applicables. La réponse « oui » ne précise pas si le type reste modifiable après traitement : OPEN-05 reste limité à ce changement (réponse 5).

## Matrice d'applicabilité

| Fonction | Tender Turnkey | SIG au sein d'un Turnkey | Tender SIG autonome | Mainline / RSC autonomes |
|---|---|---|---|---|
| Passe de distribution Turnkey | Oui, au niveau global | Déjà issue de cette distribution | Non | Non, intention existante pour types non-Turnkey |
| Allocation d'activité | Modèle propre à l'activité | Modèle SIG | Même modèle SIG | Configuration propre, pas de paramètres SIG copiés implicitement |
| Écrans | Référence du prototype | Mêmes actions métier SIG ; gestion globale réservée à l'équipe projet | Tous conservés, adaptés à SIG | Parcours jusqu'à allocation inclus ; détails propres non documentés par le prototype |
| Champs ABS/PBS/OBS Turnkey | Visibles dans la passe 1 | Ne pas les confondre avec ceux de SIG | Absents, pas simplement vides | Absents dans la variante non-Turnkey ; valider détails particuliers |
| Détail d'allocation | Distribution puis détail d'activité | Configuration SIG pour le travail SIG | Directement configuration SIG | Configuration du type correspondant |
| Casting | Équipe projet + rattachements par activité | Gestion de ses rattachements, pas du casting global | PM + contributeurs SIG ; pas de hiérarchie interne | Même principe de droits ; vocabulaire propre à confirmer si différent |
| Conformité | Équipes → activités → exigence | Réponses SIG alimentent le projet global | Équipes → exigence | Règles communes, pas de distribution Turnkey |
| Documents / relation client | Équipe de gestion globale | Pas de gestion globale par simple rattachement SIG | Équipe projet SIG | Équipe du projet correspondant |

Les variantes Mainline/RSC font partie du périmètre, mais leurs particularités non fournies restent OPEN-15. L'absence de description ne signifie ni exclusion du pilote ni équivalence automatique avec SIG. Les alias historiques RCS/RST/Rolling Stock ne sont pas validés comme synonymes de RSC ; les nouvelles specs utilisent les quatre noms fournis.

## Critères d'acceptation

- TYPE-T01 : créer SIG conserve les écrans du produit et n'affiche aucun champ, filtre, étape ou action réservés à la distribution Turnkey.
- TYPE-T02 : le panneau de détail SIG ouvre directement sa configuration, sans passage par un panneau Turnkey vide.
- TYPE-T03 : un même cas SIG reçoit les mêmes règles d'allocation dans le projet autonome et dans la branche SIG Turnkey ; les pouvoirs de gestion globale diffèrent selon le rattachement.
- TYPE-T04 : créer Turnkey conserve les deux passes et la consolidation multi-activité.
- TYPE-T05 : Mainline et RSC chargent leur configuration ; aucune substitution silencieuse par SIG ou Turnkey si elle manque.
- TYPE-T06 : tous les parcours et tests annoncent leur type de tender ; un test Turnkey ne vaut pas recette SIG/Mainline/RSC.

## Périmètre de livraison

DEC-022 : premier parcours livré de la création jusqu'à la **validation de l'allocation**, pour les quatre types. Conformité, Q&A et export client restent spécifiés pour la suite du produit, sans être des conditions d'acceptation de ce premier parcours. REX/Chat sont hors V1 (DEC-021).
