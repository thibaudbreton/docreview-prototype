# Décisions et points restant à préciser

## Autorité

Les réponses utilisateur de cette session priment sur le code et les anciennes specs. Une précision ultérieure remplace la réponse antérieure sur le même sujet : DEC-026 remplace notamment la limite aux « changements majeurs » de DEC-015. Le prototype n'est pas modifié dans cette tâche.

## Décisions consolidées

| ID | Décision | Source dans la conversation |
|---|---|---|
| DEC-001 | Trois verdicts internes ; deux à l'export client | Premier arbitrage |
| DEC-002 | Tous les contributeurs d'une activité peuvent répondre ; responsable affecté chargé du suivi | Premier arbitrage |
| DEC-003 | PM et tous les contributeurs d'une activité peuvent gérer ses rattachements | Premier arbitrage |
| DEC-004 | Types : Turnkey, SIG, Mainline, RSC | Réponse 1 |
| DEC-005 | Même modèle/actions SIG autonome et SIG dans Turnkey ; aucune gestion globale par simple rattachement SIG | Réponse 2 |
| DEC-006 | SIG conserve les écrans ; retire tout ce qui relève de passe 1 Turnkey ; détail directement SIG | Réponses 3–4 |
| DEC-007 | Type sélectionne automatiquement configuration et modèles | Réponse 5 ; changement ultérieur non précisé |
| DEC-008 | SIG : ABS → PBS → OBS → personne, sans distinction technique/non technique | Réponse 6 |
| DEC-009 | Validation par l'équipe de gestion projet, composée de bid managers et requirement managers SIG | Réponse 7 |
| DEC-010 | Un responsable de suivi par exigence, pas par branche | Réponse 8 ; absence autorisée DEC-025 |
| DEC-011 | Réallocation : se référer à la maquette | Réponse 11 ; fonctions inspectées et décrites dans ALLOCATION |
| DEC-012 | Lecture de toutes les activités du projet, modification limitée à ses activités ; pas de hiérarchie interne d'activité | Réponses 12–13 |
| DEC-013 | PM peut répondre/modifier ; export conversion automatique avec warning interne ; champs de conformité de la maquette | Réponses 14–16 ; destination précisée DEC-024 |
| DEC-014 | Consolidation confirmée ; toutes réponses reçues = complet, PM peut encore modifier | Réponses 17–18 |
| DEC-015 | Historique : seuls changements importants de texte/traduction invalidaient | Réponse 19, **remplacée par DEC-026** |
| DEC-016 | Version modifiant une exigence : déverrouillage automatique et retour pending | Réponse 20 |
| DEC-017 | Exigences supprimées visibles uniquement en comparaison ; fusion/scission ajoutées au document, décisions remises à zéro, modèles relançables automatiquement | Réponse 21 |
| DEC-018 | Formats évoqués pris en charge ; images capturées/affichées sans lecture/caractérisation ; étapes enchaînées | Réponses 22–23 |
| DEC-019 | Traduction automatique de confiance, sans validation préalable, corrigeable ; original et politique d'export conservés | Réponse 24 |
| DEC-020 | IA disponibles ou en cours ; fonctionnement/maintenance des modèles hors specs fonctionnelles | Réponses 10 et 25 |
| DEC-021 | Même Q&A entre types ; aucune action supplémentaire lors d'exclusion ; REX/Chat hors V1 | Réponses 26–28 |
| DEC-022 | Pilote complet jusqu'à validation de l'allocation, pour les quatre types | Réponse 29 |
| DEC-023 | Jusqu'à 100 000 lignes et 10 utilisateurs simultanés ; rapidité et sécurité requises | Réponse 30 |
| DEC-024 | **R&D Needed → Compliant** automatiquement à l'export client ; warning interne uniquement | Précision complémentaire |
| DEC-025 | **Validation d'allocation autorisée sans responsable** ; ne pas bloquer le travail | Précision complémentaire |
| DEC-026 | **Toute modification du texte ou de la traduction repasse en review**, sans seuil de gravité | Précision complémentaire, remplace DEC-015 |

## Suivi des anciens arbitrages

| ID | État actuel |
|---|---|
| OPEN-01 | Résolu : DEC-001/024, échelle et conversion client |
| OPEN-02 | Résolu pour droits métier : DEC-003/012/013. Admin/VIP hors détail du pilote ; à préciser si ajoutés |
| OPEN-03 | Résolu : responsable unique par exigence, absence autorisée ; ne bloque pas validation (DEC-010/025) |
| OPEN-04 | Champs et validations de maquette retenus. Liste Category encore explicitement placeholder dans le code ; vocabulaire réel à fournir avant production Compliance |
| OPEN-05 | Choix automatique par type résolu. Modification ultérieure du type/mode non répondue explicitement ; ne pas déduire une autorisation du « oui » à la sélection automatique |
| OPEN-06 | Lecture projet et exclusion sans action résolues. Cycles multiples/plusieurs questions bloquantes non précisés ; conserver le périmètre maquette décrit, à compléter pour la phase Q&A |
| OPEN-07 | Texte/traduction : review pour tout changement ; nouvelle version affectée : unlock + pending ; fusion/scission : zéro décision. Suppression manuelle/restauration reste un détail distinct non confirmé |
| OPEN-08 | Volumes résolus DEC-023. Budgets chronométrés, portée exacte du jeu 100k et protocole de mesure restent à définir avec le développement |
| OPEN-09 | Séquencement traduction résolu DEC-019/026. Dossiers multilingues non précisés |
| OPEN-10 | Pas de chantier de conception des IA dans ces specs. Formats techniques/contrats et PDF entièrement image à préciser à l'intégration, sans caractérisation visuelle implicite |
| OPEN-11 | Sécurité requise ; standards/rétention et notifications détaillées à fournir par les interlocuteurs concernés |
| OPEN-12 | Pilote résolu DEC-022 ; REX/Chat hors V1. Connecteur DOORS direct et date de pilote non confirmés |
| OPEN-13 | Labels exacts des états et composition des filtres restent alignés sur la maquette ; détails multi-pages à préciser pour 100k lignes |
| OPEN-14 | PM peut saisir/modifier même après complétude. Les interfaces de réédition doivent refléter cette décision |
| OPEN-15 | Mainline/RSC : inclus au pilote, pas de passe Turnkey selon le modèle non-Turnkey ; particularités de configuration/UI non fournies, ne pas les inventer depuis SIG |

## Ne pas redemander

Ne pas rouvrir l'échelle des verdicts, le droit de lecture des autres activités, la permission de casting, le responsable unique ou la validation sans responsable. La réallocation et les champs existants sont à documenter depuis la maquette. Les questions purement internes aux modèles sont à traiter dans le chantier IA.
