# Projets, documents, versions et traduction

## Création et traitement

- LIFE-001 — Maquette : identité, documents, traitement, équipe de gestion ; nom et BO-ID obligatoires. Types : Turnkey, SIG, Mainline, RSC (DEC-004).
- LIFE-002 — Le type choisit la configuration applicable (DEC-007). Les réglages de traitement et changement de type après démarrage ne sont pas implicitement autorisés par cette décision (OPEN-05).
- LIFE-003 — Casting hors assistant ; autres PM optionnels à la création. Les étapes IA activées s'enchaînent automatiquement, sans pause de validation intermédiaire (DEC-018). La validation humaine finale de l'allocation reste requise.
- LIFE-004 — Ajouter et réordonner des documents après création ; exporter par document ; garder le même ordre en lecture/export. Gestion globale réservée à l'équipe projet.
- LIFE-005 — Identifiant stable lors d'une correction du type titre/information/exigence ; conserver original et passage source.

## Versions et décisions

- LIFE-006 — **Exigences supprimées par une nouvelle version : visibles uniquement dans la comparaison**, absentes de la vue documentaire courante (DEC-017). Cela ne signifie pas effacer l'historique. Suppression manuelle/restauration documentaire non confirmée par cette réponse.
- LIFE-007 — Nouvelle version modifiant l'exigence : **déverrouiller automatiquement le verdict et le remettre en pending** (DEC-016). L'ancien verrou ne doit pas continuer à alimenter le résultat courant. Les exigences inchangées ne sont pas réinitialisées du seul fait de l'upload.
- LIFE-008 — **Toute correction du texte ou de la traduction repasse l’exigence en revue** (DEC-026). Aucun seuil « majeur/mineur », aucune approbation préalable de traduction. Le retour en revue ne signifie pas effacement systématique de toutes les anciennes décisions : la remise à zéro est explicitement prévue pour fusion/scission (LIFE-009), et unlock + pending pour nouvelle version affectée (LIFE-007).
- LIFE-009 — Fusion/scission : ajouter les exigences résultantes au document courant, remettre leurs décisions à zéro et permettre une relance automatique des modèles pour elles (DEC-017). Une ancienne décision ne se transfère pas automatiquement à la nouvelle exigence.
- LIFE-010 — Les autres modifications passent par leur fonction dédiée, notamment la réallocation ; ne pas appliquer une réinitialisation globale à toute édition.

`documents.html:uploadVersion` reste une simulation de comparaison ; les règles ci-dessus définissent désormais la cible métier approuvée. Préserver la trace des anciennes décisions est un besoin d'audit historique conservé, pas un maintien de leur validité.

## Formats et images

DEC-018 : formats évoqués PDF texte/scanné, Word, Excel et échanges DOORS concernés. Une image est **capturée et affichée, mais son contenu n'est pas lu ni caractérisé automatiquement**. Ne pas confondre capture d'un conteneur image et extraction d'exigences depuis son contenu. La manière de traiter un PDF constitué uniquement d'images est une limite d'ingestion à expliciter avec l'équipe technique ; ne pas inventer une caractérisation visuelle. Les autres éléments textuels du document continuent d'être traités.

## Langue

- LANG-001 — DEC-019 : anglais de travail, original conservé, traduction anglaise séparée et corrigeable.
- LANG-002 — Capture → traduction automatique si nécessaire → caractérisation → allocation, sans revue humaine préalable de traduction.
- LANG-003 — Export : texte d'exigence original, contributions en anglais. Pas de retraduction implicite des contributions.
- LANG-004 — Correction possible après traitement ; tout changement soumis à LIFE-008. L'ancienne règle « jamais de stale après traduction » est remplacée.
- LANG-005 — Aucune nouvelle décision sur les dossiers multilingues : besoin non bloquant à préciser lorsque rencontré.

## Acceptation

LIFE-T01 : nom/BO-ID manquant empêche création. LIFE-T02 : casting incomplet n'arrête pas capture. LIFE-T03 : ordre conservé dans export. LIFE-T04 : changement Type conserve ID. LIFE-T05 : nouvelle version modifiant une exigence verrouillée la déverrouille et remet le verdict pending. LIFE-T06 : suppression visible en comparaison seulement. LIFE-T07 : fusion/scission crée les éléments courants sans décisions héritées, relance possible pour ces éléments. LIFE-T08 : image affichée sans caractérisation de son contenu. LANG-T01 : traduction automatique sans arrêt ; correction reste possible. LANG-T02 : original non écrasé. LANG-T03 : toute modification, même mineure, du texte/traduction fait revenir en revue ; sans modification, l’état reste inchangé. Le verdict courant n’est pas présenté comme nouvellement revalidé sans action humaine.
