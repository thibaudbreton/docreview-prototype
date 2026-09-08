# Modèle de tâche de développement

Les user stories peuvent résumer la valeur, mais ne remplacent pas les règles. Ce fichier est un modèle documentaire, pas une tâche lancée.

## Champs

- **Objectif utilisateur :** résultat observable.
- **Parcours et variante :** identifiant JRN, type Turnkey/SIG/Mainline/RSC, écran de référence. Pour SIG, ne pas extrapoler les éléments Turnkey.
- **Règles :** identifiants et liens ; ne pas recopier leurs définitions.
- **Décisions préalables :** OPEN concernés, tous résolus pour le périmètre dépendant.
- **Périmètre :** objets et actions modifiés ; exclusions.
- **Contrat technique :** lien vers API/données approuvées, quand disponibles.
- **Acceptation :** scénarios métier nominaux, limites, permissions et erreurs pertinents.
- **Vérification :** preuves nécessaires, pas une liste automatique de tests sans rapport.
- **Livraison :** changements, résultat des vérifications, limites restantes.

## Exemple de tâche à préparer pour le pilote

Objectif : valider l’allocation d’une exigence SIG, même sans responsable.
Parcours : JRN-002 et TYPE-T01/02. Règles : ALLOC-003/007/010/011 et ACC-007.
Critères : ABS → PBS → OBS ; aucune passe 1 ; détail SIG ; validation permise si seule la personne manque ; droits de validation conformes à ALLOC-012 ; absence visible après sauvegarde.
Préalables techniques : contrat de persistance et configuration SIG. Ne pas demander à l’agent de concevoir le modèle IA.

## Maintenance

Une modification métier met à jour sa règle unique, ses exemples et les parcours affectés dans le même changement. Une décision résolue est enregistrée dans OPEN-QUESTIONS. Une description d'écran ne doit pas redéfinir une règle commune. Les numéros de règle ne sont jamais réattribués à un autre sens.
