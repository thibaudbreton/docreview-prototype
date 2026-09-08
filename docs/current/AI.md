# Traitements IA — frontière fonctionnelle

## Périmètre

DEC-020 : les IA existent déjà ou sont en cours de création. La conception et l'entretien de leurs modèles/référentiels relèvent du chantier IA, **pas de ces specs fonctionnelles**. Les propositions précédentes sur leur développement et leurs évaluations ne sont pas des prérequis fonctionnels à faire arbitrer à l'utilisateur ici.

Ces specs définissent seulement le comportement du produit lorsqu'il reçoit ou attend leurs résultats. Formats API, disponibilité des endpoints et contrats d'intégration sont à traiter avec les responsables techniques/IA.

## Règles conservées

- AI-001 — Le résultat reste rattaché au bon projet, document, version et élément. Les propositions et corrections ne doivent pas être confondues.
- AI-002 — Capture : éléments textuels et images affichables ; **pas de lecture ni caractérisation du contenu des images** (DEC-018).
- AI-003 — Traduction automatique en anglais, sans validation intermédiaire, correction possible (LANG-001 à LANG-004).
- AI-004 — Caractérisation selon la configuration applicable ; aucune transposition implicite des règles Turnkey à SIG.
- AI-005 — Allocation selon le type ; SIG suit ABS → PBS → OBS → personne (ALLOC-003). Pas de passe 1 Turnkey en standalone SIG.
- AI-006 — Comparaison : effets fonctionnels LIFE-006 à LIFE-009. Fusion/scission : décisions remises à zéro, relance automatique possible sur les éléments concernés.
- AI-007 — Q&A : même parcours selon le type, décrit pour la suite du produit ; hors borne du pilote allocation.
- AI-008 — REX/Chat hors V1 (DEC-021), même si la maquette les représente.
- AI-009 — Enchaînement automatique des étapes activées ; la validation humaine de l'allocation reste la borne finale du pilote.
- AI-010 — Absence de modèle applicable : état explicite et traitement manuel lorsqu'il est prévu ; ne pas utiliser silencieusement le modèle d'un autre type.
- AI-011 — Relance : remise à zéro explicitement prévue pour fusion/scission ; ne pas écraser les autres décisions humaines par défaut.
- AI-012 — PROP d'intégration : échec/traitement en cours/résultat disponible distincts ; pouvoir reprendre après incident sans doublons.
- AI-013 — Conformité consolidée et permissions calculées par les règles métier, pas déterminées par un LLM.

Les scores générés par `seed_demo_confidence` restent une illustration d'affichage. Leur calibration relève du chantier IA ; ils ne constituent pas une mesure du système réel.
