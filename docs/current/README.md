# SRM — Référence fonctionnelle consolidée

Édition du 8 septembre 2026. Mise à jour documentaire ; aucun changement du prototype.

## Lecture et autorité

Cette édition sépare les comportements constatés, les besoins décrits et les décisions encore ouvertes. Elle ne prétend pas que tous les comportements du prototype ont été validés par les utilisateurs. Les divergences entre écrans restent visibles. Les décisions DEC ci-dessous priment sur les comportements OBS contradictoires ; elles ne signifient pas que le prototype a déjà été corrigé.

- **DEC** : décision explicite de l’utilisateur dans cette session ; référence métier pour les nouvelles implémentations.
- **OBS** : constat dans le code actuel, sans présumer de sa validation métier.
- **DOC** : intention explicite dans une spec, un ticket ou un compte rendu ; pas une preuve d'implémentation.
- **PROP** : proposition de conception pour la production, à valider.
- **OPEN** : contradiction ou décision manquante ; ne pas inventer de réponse.

Un identifiant stable désigne une règle. Ne pas recopier sa définition dans les tâches ou dans plusieurs specs. Une règle OBS n'autorise pas à reproduire un défaut de démonstration en production. Les exemples d'acceptation vérifient la règle associée, pas l'état actuel du prototype.

Les anciens prompts et tickets sont des sources historiques, pas des instructions à exécuter. Aucun lancement de routine, aucune suppression et aucun changement de produit n'est demandé par leurs passages impératifs.

## Produit et navigation

SRM organise la capture, la caractérisation, l'allocation et la revue de conformité des exigences d'un appel d'offres. Le travail est assisté par IA et comporte des validations humaines. La distinction fonctionnelle récente est Project Manager / Contributor ; les structures historiques manager/expert subsistent par endroits (OPEN-02).

Sept sources actives sont assemblées dans `index.html` et `docreview-app.html` : `accueil.html`, `creation-projet.html`, `dashboard-et-config.html`, `revue-documentaire.html`, `compliance.html`, `documents.html`, `qa.html`. Dashboard, configuration et casting partagent un fichier. Il n'existe plus de route autonome Expert Space dans la liste d'assemblage.

## Carte de lecture

| Besoin | Référence |
|---|---|
| Variantes Turnkey / SIG / Mainline / RSC | [Profils de tender](TENDER-PROFILES.md) |
| Clés PBS / OBS / ABS de SIG — le fichier et sa lecture | [Clés](KEYS.md) |
| Définitions, objets, vocabulaire | [Modèle métier](DOMAIN.md) |
| Création, documents, versions, traduction | [Cycle documentaire](LIFECYCLE.md) |
| Allocation, dépendances, validation | [Allocation](ALLOCATION.md) |
| Réponses, consolidation, verrouillage | [Conformité](COMPLIANCE.md) |
| Casting, droits, périmètres | [Accès et équipes](ACCESS.md) |
| Questions, réponses client, arbitrage | [Q&A](QA.md) |
| Parcours et interactions des écrans | [Parcours](JOURNEYS.md) |
| Comportement fonctionnel des traitements existants | [Frontière IA](AI.md) |
| Persistance, intégrations, performance, métriques | [Exigences transverses](PLATFORM.md) |
| Décisions à prendre et contradictions | [Arbitrages](OPEN-QUESTIONS.md) |
| Sources, changements, limites de l'audit | [Traçabilité](AUDIT.md) |
| Préparer une tâche pour un agent | [Modèle de tâche](TASK-TEMPLATE.md) |

## Utilisation par un agent de développement

1. Lire cette carte et les règles du domaine concerné.
2. Lire le parcours et les questions ouvertes associés.
3. Charger seulement les écrans et contrats nécessaires à la tâche.
4. Si une question ouverte conditionne l'implémentation, préparer les options et demander un arbitrage ; avancer sur les parties indépendantes.
5. Fournir les scénarios vérifiés, les limites et les références des règles modifiées.

## Périmètre

**Premier pilote confirmé : création jusqu’à validation de l’allocation, pour Turnkey, SIG, Mainline et RSC.** Le parcours SIG conserve les écrans mais retire les éléments de passe 1 Turnkey ; son détail ouvre directement la configuration SIG. Mainline/RSC sont inclus, leurs détails spécifiques restent à documenter si différents.

Conformité, versions et Q&A restent décrits dans le corpus ; leur présence ne les impose pas tous comme livrables du premier parcours. REX/Chat hors V1. La conception des modèles IA n’est pas couverte ici.

Dimensionnement confirmé : jusqu’à 100 000 lignes et 10 utilisateurs simultanés. Les décisions utilisateur DEC-001 à DEC-027 figurent dans le registre ; la règle la plus récente prime.

Les anciennes specs sont conservées intégralement dans [l'archive](../archive/specs-2026-09-08/README.md), utile pour les détails historiques. Leurs contradictions ne doivent pas être importées dans les nouvelles tâches.
