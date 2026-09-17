# Audit et traçabilité de la mise à jour

## Référence examinée

Dossier SRM-PROTO, HEAD `3ef09ba0f491ef9fe6dad248e2febc523cf0dddf`, fichiers de travail lus le 8 septembre 2026. Deux changements locaux étaient déjà présents : modification de `docs/archive/TICKETS-continuity-fixes.md` et suppression de `docs/specs/SPEC-expert-space.md`. Ils ne sont ni écrasés ni restaurés.

## Sources déterminantes

| Constat / règles | Preuve de code ou document |
|---|---|
| Sept écrans, anciennes pages retirées | `build_merge.py:SOURCES` |
| Deux verdicts et R&D en commentaire | `compliance.html:CMP/CMP_ORDER`, formulaire `v-submit-compliant`, ticket fusion |
| Trois verdicts et arbre à deux niveaux | `revue-documentaire.html:COMPLIANCE_DEFS/CMP_RANK/deriveActivityCompliance/deriveRequirementCompliance` |
| Réponse par activité | `compliance.html:canAnswer/passesB` |
| Casting encore lié à managerId | `dashboard-et-config.html:CAST_ACTIVITIES/castGroupHTML/PM_TEAM` |
| Création en quatre étapes et limites | `creation-projet.html`, spec création récente |
| Versions et gap simulés | `documents.html:uploadVersion` |
| Q&A synthétique | `qa.html:syntheticAnswer/buildDossier/runImport` |
| Confiance générée | `import_capture_doors.py:seed_demo_confidence` |
| Traduction et KPI souhaités | specs traduction et statistiques conservées en archive |
| Rôles et responsable unique | compte rendu USER-TEST-session-3 et ticket fusion |
| Exigences transverses conservées | tableau des 29 FR dans PLATFORM |

## Changements documentaires

Création d'une référence consolidée avec règles identifiées, statut de preuve, parcours, contrats IA, critères d'acceptation et registre d'arbitrages. Les anciennes specs sont conservées intégralement dans une archive datée ; leurs chemins habituels deviennent des points d'entrée vers les nouveaux domaines. Aucun HTML/CSS/JS ni script de prototype n'est modifié.

Le verdict R&D et les rôles ne sont pas harmonisés par supposition. Cette mise à jour corrige aussi l'impression donnée précédemment dans la conversation qu'une échelle à trois valeurs était déjà la règle commune : elle ne l'est pas dans le code actuel.

## Limites

Inspection documentaire et ciblée du code, sans session navigateur, appel modèle, test de charge ni test fonctionnel exécuté. Les anciens détails d'interface sont archivés, pas tous revalidés un par un. Les critères d'acceptation sont des cas à vérifier lors du développement. Les décisions utilisateur nouvelles doivent être intégrées avant d'appeler cette édition « approuvée pour implémentation ».

Les liens historiques internes aux copies d'archive sont conservés tels quels ; certains citaient déjà des fichiers absents. Les nouveaux points d'entrée et références actives sont contrôlés séparément. Les archives ne sont pas nettoyées au risque d'altérer leur valeur historique.

## Consolidation après réponses utilisateur

Les 30 réponses et les trois précisions suivantes sont intégrées dans DEC-004 à DEC-026. Ajout de TENDER-PROFILES, correction explicite de la chaîne SIG en ABS → PBS → OBS, responsable unique facultatif, droits de lecture globaux dans le projet, retour en revue pour tout changement de texte/traduction, conversion R&D → Compliant côté client, pilote allocation et charge 100k/10 simultanés.

Les anciens constats de code restent étiquetés OBS et les nouvelles décisions DEC priment. Vérifications ciblées supplémentaires : maquette de réallocation (`renderReassignForm`, `approveReassign`, `rejectReassign`) et validation de Topic dans Compliance (`v-submit-notcompliant`). Aucun test navigateur ni modification du prototype. Les anciens documents de référence sont conservés dans leur archive initiale, sans leur appliquer les nouvelles décisions.

## Précision DEC-027 — retraitement après nouvelle version

Ajout du retraitement automatique ciblé sur les exigences modifiées par une version. LIFE-011, AI-006/011 et JRN-005 explicitent la règle ; LIFE-T09/10 vérifient le ciblage et le respect du type de tender. Aucun appel modèle réel ni changement du prototype.
