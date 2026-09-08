# Exigences transverses et correspondance backend

La stack communiquée par l'utilisateur est React côté front et Azure côté backend. Le choix des services, frameworks et schémas API n'est pas approuvé par cette mise à jour fonctionnelle.

## Besoins conservés

- PLAT-001 — DOC : persistance des projets, documents, exigences, affectations, réponses et états ; accès après redémarrage.
- PLAT-002 — DOC : SSO et droits projet/activité contrôlés côté serveur. La séparation entre projets et les droits de modification doivent couvrir requêtes directes, compteurs, recherche et exports. Dans un projet, lecture de toutes les activités autorisée aux contributeurs par DEC-012.
- PLAT-003 — DOC : audit des changements humains et machines, identité, date, avant/après ; traçabilité des traitements IA et coût. Le suivi de session et sa rétention doivent être précisés (OPEN-11).
- PLAT-004 — DOC : import/export DOORS 9 et DOORS NG, export Excel. Les menus CSV/ReqIF de démonstration ne prouvent pas une intégration. Formats, mappings et boucle aller-retour à contractualiser (OPEN-10/12).
- PLAT-005 — DOC : notifications internes et email ; déclencheurs, destinataires, regroupement et relances non finalisés. L'envoi client Q&A reste hors outil (QA-003).
- PLAT-006 — DEC-023 : tableaux jusqu’à **100 000 lignes**, jusqu’à **10 utilisateurs simultanés**. Ces cibles remplacent les anciens 30 000 éléments/10 000 utilisateurs comme hypothèse de dimensionnement. 100 000 lignes ne signifie pas nécessairement 100 000 exigences : titres et informations comptent aussi. La portée exacte projet/table sera précisée pour le test de charge ; ne pas réduire le maximum à une page affichée.
- PLAT-007 — DEC-023 : rapidité requise. Ancienne cible P95 ≤ 300 ms et < 3 s pour 10 000 lignes : références historiques, **pas SLA confirmé à 100 000 lignes**. Spécifier ensuite budgets mesurables sur recherche, filtres, navigation et actions groupées ; transfert/traitement IA mesurés séparément.

## Métriques — PLAT-008 (DOC, formules à compléter)

| Mesure | Unité et règle |
|---|---|
| Profil de conformité | Exigences : verdict final ou en attente ; ne pas omettre les inconnus ; échelle interne DEC-001 et conversion client DEC-024 |
| Attente interne | Affectations en attente de réponse, âge de la plus ancienne par périmètre ; distinguer Q&A client |
| Blocage client | Affectations `awaiting_qa`, ancienneté de la question liée |
| Casting incomplet | Périmètres/activités utiles au dossier sans personne ; responsable facultatif unique DEC-010/025 ; absence non bloquante |
| Travail à revoir | Réponses affectées par une nouvelle version, selon OPEN-07 |
| Trajectoire | Historique du travail restant et échéance ; nécessite snapshots ou historique exploitable |
| Corrections IA | Propositions modifiées par champ ; définir dénominateur, revue effective et corrections répétées |

Une métrique doit annoncer son unité : exigences, activités, équipes, réponses et personnes ne sont pas interchangeables. Aucun indicateur composite santé ni pourcentage global unique n'est adopté sans définition métier. Les valeurs de démo ne constituent pas une mesure réelle.

## Correspondance avec les 29 FR historiques

| FR anciens | Référence actuelle | État |
|---|---|---|
| 1 | Stack React/Azure, ci-dessus | Besoin utilisateur ; détails techniques ouverts |
| 2–3 | LIFE-004/005, AI-002 | Capture image et suppression : OPEN-07/10 |
| 4 | LIFE-002 | Contradiction immutabilité OPEN-05 |
| 5–6 | CONF-001 à CONF-008, PLAT-003 | Verrous distincts ; échelle interne DEC-001 et conversion client DEC-024 |
| 7 | PLAT-005 | Déclencheurs OPEN-11 |
| 8–9 | PLAT-007 | Charge et définition OPEN-08 |
| 10–13 | AI-001 à AI-013 | Confiance, gap analysis, humain ; OPEN-07/10 |
| 14–15 | ALLOC-004, PLAT-001 | Arbre Turnkey et variante SIG ; responsable unique DEC-010 |
| 16–18 | LIFE-004/007, PLAT-006, UX-005 | Versions, ordre, filtrage global ; limites à confirmer |
| 19–20 | QA-001 à QA-009 | Deux flux, pas un chat générique |
| 21 | PLAT-006/007 | DEC-023 : 10 utilisateurs simultanés, 100 000 lignes |
| 22–23 | PLAT-003 | Périmètre audit et conservation OPEN-11 |
| 24–26 | ACC-001 à ACC-007, PLAT-002 | DEC-012/013 : lecture projet, édition activité, actions PM |
| 27 | OPEN-11 | Standards et contraintes à fournir |
| 28–29 | PLAT-004 | Contrats d'échange et priorité OPEN-10/12 |

Le critère historique « pipeline sans intervention » ne supprime pas les validations humaines. Distinguer exécution technique des étapes et validation métier de leurs résultats (AI-009).

## Acceptation de production à préparer — PROP

Persistance après reconnexion ; droits sur requêtes directes ; enregistrement concurrent sans perte silencieuse ; audit vérifiable ; export comparé aux données visibles ; reprise de traitement après incident ; test de charge selon profil approuvé ; aller-retour DOORS avec données représentatives. Aucun de ces tests n'a été exécuté dans le cadre de la mise à jour documentaire.

## Borne de pilote et recette

DEC-022 : Turnkey, SIG, Mainline et RSC jusqu’à validation de l’allocation. Le pilote vérifie création, documents, traitements enchaînés, interfaces adaptées au type, corrections/réallocation, responsable facultatif unique et validation finale. La conformité complète, Q&A et l’export client restent au-delà de cette borne. L’inclusion d’un connecteur DOORS direct n’est pas déduite du support des fichiers DOORS.

Charge : constituer un jeu de 100 000 lignes et 10 sessions concurrentes ; vérifier recherche/filtrage sur le jeu complet, fluidité de la navigation et conservation des modifications. Les seuils chronométrés restent OPEN-08. Sécurité confirmée comme exigence ; règles internes spécifiques/rétention à fournir via le chantier technique, pas inventées ici.
