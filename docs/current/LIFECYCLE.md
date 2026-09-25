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
- LIFE-011 — **Après comparaison avec une nouvelle version, relancer automatiquement les modèles nécessaires sur les exigences modifiées** (DEC-027). Appliquer les traitements nécessaires au changement et au type de tender ; ne pas retraiter les exigences inchangées. Les nouvelles propositions restent à revoir/valider par un humain ; la relance ne rétablit pas automatiquement les anciennes validations ou le verdict de conformité. La sélection technique des modèles relève du chantier IA.
- LIFE-012 — **Une version est celle d'un document** (DEC-069). Chaque document avance à son rythme ; un écart se lit toujours entre deux versions d'un même document. Aucune version n'est attachée au tender entier.
- LIFE-013 — **Compare, un document à la fois** (DEC-070) : le document, puis une version antérieure comparée à celle en vigueur. Les modifications s'y lisent mot à mot ; les exigences supprimées n'y apparaissent qu'à cet endroit (LIFE-006).
- LIFE-014 — **Onglet Versions** sur une exigence changée dans la version en vigueur de son document (DEC-071) : ce qui a changé, depuis quelle version, le texte précédent. Absent sinon.
- LIFE-015 — **Une exigence ajoutée ou modifiée repasse To review** (DEC-072), sans état de traitement propre au changement ; la valider est le traitement. Si un autre statut plus restrictif s'applique (allocation incomplète), c'est lui qui s'affiche — la règle du plus restrictif ne change pas.
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

LIFE-T10 : la barre supérieure n'affiche aucune version de projet ; chaque document de Compare porte ses propres versions. LIFE-T11 : comparer un document à une seule version l'annonce, sans afficher de comparaison vide. LIFE-T12 : une exigence modifiée dans la version en vigueur est « To review », a un onglet Versions montrant le diff mot à mot ; une exigence inchangée n'a pas d'onglet. LIFE-T13 : valider une exigence modifiée suffit à traiter le changement.

LIFE-T09 : une nouvelle version modifie 3 exigences parmi 100 ; les modèles nécessaires sont relancés pour ces 3 exigences, pas pour les 97 inchangées. Les résultats correspondent à la nouvelle version et restent soumis à revue/validation ; les verdicts des exigences affectées restent pending selon LIFE-007. LIFE-T10 : un retraitement SIG ne lance pas la passe 1 Turnkey. Les images restent soumises à LIFE-T08.
