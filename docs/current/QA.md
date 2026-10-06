# Q&A — questions et réponses client

DEC-021 : même fonctionnement Q&A pour Turnkey et SIG. Fonction décrite pour la suite ; premier pilote limité à l’allocation.

## Règles

| ID | Règle | Statut |
|---|---|---|
| QA-001 | Une question est identifiée, attribuée à son auteur et liée aux exigences/affectations concernées. | DOC/OBS simulé |
| QA-002 | ~~Le PM prépare le lot, fusionne les doublons ou exclut une question de l'export sans la supprimer du registre.~~ **Remplacée par DEC-116** : plus de lot, de fusion ni d'exclusion ; chaque question a un statut À envoyer / Envoyée / Répondue, et le PM la **marque « envoyée » à la main**, une par une ou par sélection. | DOC/OBS |
| QA-003 | L'export prévu est Excel avec identifiant de l'exigence. L'envoi client est réalisé hors SRM. Depuis DEC-116, l'export ne marque rien : c'est le PM qui marque « envoyée ». | DOC ; export simulé |
| QA-004 | La cible actuelle décrit un seul cycle par tender ; les lots multiples ne sont pas implicitement acquis. | DOC |
| QA-005 | Importer fichier ou contenu, extraire les paires Q/R et proposer des liens avec questions propres ou exigences pour les réponses à d'autres soumissionnaires. | DOC ; extraction/matching simulés |
| QA-006 | Réponse validée à notre question : débloquer le travail associé sans inventer une conformité. Une réponse à un concurrent ajoute du contexte sans changement d'état. | DOC |
| QA-007 | ~~Les associations incertaines sont arbitrées par le PM dans une file.~~ **Remplacée par DEC-116** : pas de file d'arbitrage. Une réponse incertaine à notre question s'affiche « à confirmer » sur la question (un clic pour l'accepter ou l'écarter) ; une question-réponse d'un autre soumissionnaire sans lien sûr reste dans la liste, « No requirement linked ». | DOC/OBS |
| QA-008 | Dates de clôture des questions et de retour prévu optionnelles ; retard visible, sans blocage absolu des questions tardives. | DOC/OBS |
| QA-009 | Chat de recherche et question officielle au client doivent rester distincts. | DOC |
| QA-010 | **Une question posée depuis Compliance entre dans le registre Q&A du tender en brouillon** (DEC-088). Le chef de projet la relit et la marque « envoyée » à la main (DEC-116 : plus de fusion de doublons ni de lot) ; le contributeur ne l'envoie pas lui-même. **Elle ne bloque pas la conformité** (DEC-092) : l'affectation se consolide sur le verdict du contributeur, pas sur la réponse du client, et **plusieurs questions** peuvent être en cours sur une même affectation. Annuler la question (Undo) la retire du registre. | DEC-088 |

## Points de vigilance fonctionnels

OBS : `qa.html` possède ses données et une génération de réponses fictives (`syntheticAnswer/buildDossier`). La continuité complète avec les branches bloquées de Compliance n'est pas une intégration backend démontrée. Depuis DEC-116, « Sent » est marqué à la main par le PM et l'export ne marque rien ; cela ne prouve pas l'envoi effectif hors outil : OPEN-06.

~~La fusion doit préserver tous les liens de travail bloqué ; aucune action supplémentaire lors de l’exclusion (DEC-021).~~ Sans objet depuis DEC-116 : fusion, doublons et exclusion sont retirés. DEC-012 permet la consultation des autres systèmes du même projet. Les détails non répondus (plusieurs questions bloquantes, lots successifs) conservent le comportement de maquette sans élargissement implicite ; OPEN-06 résiduel.

## Acceptation

QA-T01 et QA-T02 (fusion, exclusion) : sans objet depuis DEC-116. QA-T03 : une réponse à notre question débloque uniquement les affectations liées. QA-T04 : une réponse concurrente ne change pas l'état de revue. QA-T05 : écarter une réponse « à confirmer » la laisse consultable ; aucun lien forcé. QA-T06 : dates absentes n'empêchent pas de travailler. QA-T07 : export ne déclenche aucun envoi automatique.

## Sources

`qa.html:oursHTML/othersHTML/cardHTML/runImport/markSent`, ancienne SPEC-qa-screen, ticket des trois écrans support.
