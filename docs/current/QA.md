# Q&A — questions et réponses client

DEC-021 : même fonctionnement Q&A pour Turnkey et SIG. Fonction décrite pour la suite ; premier pilote limité à l’allocation.

## Règles

| ID | Règle | Statut |
|---|---|---|
| QA-001 | Une question est identifiée, attribuée à son auteur et liée aux exigences/affectations concernées. | DOC/OBS simulé |
| QA-002 | Le PM prépare le lot, fusionne les doublons ou exclut une question de l'export sans la supprimer du registre. | DOC/OBS |
| QA-003 | L'export prévu est Excel avec identifiant de l'exigence. L'envoi client est réalisé hors SRM. | DOC ; export simulé |
| QA-004 | La cible actuelle décrit un seul cycle par tender ; les lots multiples ne sont pas implicitement acquis. | DOC |
| QA-005 | Importer fichier ou contenu, extraire les paires Q/R et proposer des liens avec questions propres ou exigences pour les réponses à d'autres soumissionnaires. | DOC ; extraction/matching simulés |
| QA-006 | Réponse validée à notre question : débloquer le travail associé sans inventer une conformité. Une réponse à un concurrent ajoute du contexte sans changement d'état. | DOC |
| QA-007 | Les associations incertaines sont arbitrées par le PM dans une file ; passer et « aucune exigence correspondante » sont des issues valides. | DOC/OBS |
| QA-008 | Dates de clôture des questions et de retour prévu optionnelles ; retard visible, sans blocage absolu des questions tardives. | DOC/OBS |
| QA-009 | Chat de recherche et question officielle au client doivent rester distincts. | DOC |

## Points de vigilance fonctionnels

OBS : `qa.html` possède ses données et une génération de réponses fictives (`syntheticAnswer/buildDossier`). La continuité complète avec les branches bloquées de Compliance n'est pas une intégration backend démontrée. « Sent » dans le prototype après export ne prouve pas l'envoi effectif hors outil : OPEN-06.

La fusion doit préserver tous les liens de travail bloqué (DOC). DEC-021 : aucune action supplémentaire lors de l’exclusion (« rien ») : conserver l’exclusion, sans notification ni déblocage ajouté. DEC-012 permet la consultation des autres systèmes du même projet. Les détails non répondus (plusieurs questions bloquantes, lots successifs) conservent le comportement de maquette sans élargissement implicite ; OPEN-06 résiduel.

## Acceptation

QA-T01 : fusionner deux questions conserve les liens aux deux affectations. QA-T02 : exclure laisse la question consultable et la retire du lot. QA-T03 : une réponse à notre question débloque uniquement les affectations liées. QA-T04 : une réponse concurrente ne change pas l'état de revue. QA-T05 : passer un arbitrage le garde disponible ; aucun lien forcé. QA-T06 : dates absentes n'empêchent pas de travailler. QA-T07 : export ne déclenche aucun envoi automatique.

## Sources

`qa.html:renderQuestions/buildDossier/decideArb/skipArb/runImport`, ancienne SPEC-qa-screen, ticket des trois écrans support.
