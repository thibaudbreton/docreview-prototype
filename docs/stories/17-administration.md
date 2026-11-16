# Administration de la plateforme (US-ADM)

**Qui s'en sert.** L'admin de la plateforme. Il ne travaille dans aucun tender.

**Le parcours.** L'admin gère ce qui dépasse un tender : les personnes et leurs droits, la liste de tous les tenders, le journal d'audit, les statistiques de la plateforme et le suivi de l'IA (DEC-127).

**Termes.**
- **Admin** : voit tout et agit sur les personnes et les tenders, mais n'a aucune autorité métier (ACC-016).
- **Tender leader** : statut accordé par un admin. Lui seul crée un tender (ACC-015).
- **Ce qui ne change pas :** ce qui appartient à un tender reste dans sa Configuration.

### US-ADM-01 — Donner ou retirer le droit de créer un tender
**Carte :** En tant qu'admin, je veux faire d'une personne un Tender leader ou lui retirer ce statut, afin que seules les personnes autorisées créent des tenders.
**Conversation :**
- Le statut se donne dans la section Users.
- Le retirer n'enlève rien sur les tenders que la personne a déjà créés ou qu'elle gère.
- Plus tard, des rôles SSO (Bid Director, Bid Manager, Requirement Manager…) donneront ce statut d'eux-mêmes. Ce n'est pas actif au pilote : l'écran l'annonce comme « Later ».

**Maquette :** Administration — `admin.html` (route `#admin`), section Users.
**Règles :** DEC-127, ACC-015, ACC-018  ·  **Périmètre :** Pilote 1 (à confirmer)  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. « Make tender leader » donne le statut ; la personne voit ensuite « ＋ New tender » sur l'accueil et le tableau de bord.
2. « Withdraw leader » retire le statut ; « ＋ New tender » disparaît pour elle, et ses tenders existants restent les siens.
3. Une personne sans le statut ne peut pas créer de tender, même par l'adresse directe de l'assistant (refus côté serveur).
4. Chaque changement de statut s'inscrit au journal d'audit avec l'admin, la date et l'avant → après.
5. Une personne dont le rôle SSO serait éligible porte la mention « Eligible by SSO role, once the rule is active ».

Écart maquette : le refus côté serveur n'est pas simulé.

### US-ADM-02 — Désactiver une personne qui part
**Carte :** En tant qu'admin, je veux désactiver une personne qui quitte l'entreprise sans laisser de tender sans pilote, afin que le travail continue.
**Conversation :**
- Les personnes viennent du SSO ; on ne les crée jamais ici.
- Désactiver empêche la connexion et garde tout le travail de la personne, à son nom.
- Le cas critique : la personne est le seul tender manager actif d'un tender. Il faut alors nommer quelqu'un avant de valider.

**Maquette :** Administration — `admin.html` (route `#admin`), section Users › « Deactivate ».
**Règles :** DEC-127, ACC-017, ACC-002, ACC-006  ·  **Périmètre :** Pilote 1 (à confirmer)  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. « Deactivate » ouvre un encadré qui liste les tenders où la personne est seule tender manager active, chacun avec une liste pour choisir un remplaçant.
2. Tant qu'un remplaçant manque, la désactivation est refusée avec « Name a tender manager for N tenders first ».
3. Une fois validée, la personne apparaît « Deactivated · {date} », ne peut plus se connecter, et les remplaçants deviennent tender managers.
4. Ses réponses, verdicts et entrées de journal gardent son nom.
5. Ses affectations (PIC) apparaissent sans personne chez les tender managers concernés.
6. « Reactivate » la rétablit. La désactivation comme la réactivation s'inscrivent au journal d'audit.

### US-ADM-03 — Voir tous les tenders et en garder un pilote
**Carte :** En tant qu'admin, je veux voir tous les tenders en liste, avec leurs tender managers et leur avancement, afin de repérer un tender orphelin ou en retard.
**Conversation :**
- C'est une liste, pas les cartes de l'accueil : l'admin y voit aussi les tenders dont il n'est pas membre.
- Un tender sans tender manager actif est signalé en tête de la liste.
- Archiver plutôt que supprimer : un tender archivé quitte les listes de tout le monde, mais reste lisible.

**Maquette :** Administration — `admin.html` (route `#admin`), section Tenders.
**Règles :** DEC-127, ACC-016, ACC-002  ·  **Périmètre :** Pilote 1 (à confirmer)  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Chaque ligne montre : référence, nom, ligne, région, tender managers actifs, étape, avancement, jours avant soumission et dernière activité.
2. La recherche (référence, nom, ligne), le filtre de région et le filtre d'étape réduisent la liste. « Show archived » réaffiche les tenders archivés.
3. Un bandeau nomme les tenders sans tender manager actif. « + Tender manager » permet d'en nommer un, et le bandeau disparaît.
4. « Archive » / « Restore » change l'état du tender et s'inscrit au journal d'audit.
5. « Open » ouvre le tender tel que ses tender managers le voient. L'admin n'y valide rien et n'y donne aucun verdict (ACC-016).

Écart maquette : un tender archivé n'est pas encore retiré de l'accueil des autres personnes, et la lecture seule d'un tender archivé n'est pas simulée.

### US-ADM-04 — Consulter le journal d'audit de la plateforme
**Carte :** En tant qu'admin, je veux retrouver qui a changé quoi, quand, sur tous les tenders et dans l'administration, afin de répondre à un audit ou d'expliquer une situation.
**Conversation :**
- Le journal réunit les journaux d'exigence de tous les tenders et les actions d'administration.
- Il est en lecture seule : rien ne s'y modifie ni ne s'y supprime.

**Maquette :** Administration — `admin.html` (route `#admin`), section Audit log.
**Règles :** DEC-127, ACC-018, PLAT-003  ·  **Périmètre :** Pilote 1 (à confirmer)  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Chaque entrée montre : date et heure, auteur, tender, élément (exigence), nature du changement, description et avant → après.
2. Les entrées vont de la plus récente à la plus ancienne. Elles se filtrent par tender, par nature, par personne et par recherche libre.
3. Aucune entrée ne peut être modifiée ni supprimée depuis l'écran.
4. « Export » produit toutes les entrées filtrées, avec auteur, date, avant et après.

Point ouvert : la durée de conservation du journal (OPEN-11).

### US-ADM-05 — Suivre la plateforme dans son ensemble
**Carte :** En tant qu'admin, je veux voir combien de tenders sont en cours, où ils en sont et qui utilise l'outil, afin de piloter l'usage de la plateforme.
**Conversation :**
- Ce sont les statistiques de toute la plateforme, pas celles d'un tender : celles-ci restent sur son tableau de bord.
- Aucun classement de personnes (DEC-118).

**Maquette :** Administration — `admin.html` (route `#admin`), section Statistics.
**Règles :** DEC-127, DEC-118  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Les tuiles donnent :
   - les tenders en cours, soumis et archivés ;
   - les exigences en cours ;
   - la part allouée ;
   - la part répondue dans Compliance ;
   - les personnes actives dans la semaine.
2. Deux répartitions montrent les tenders par étape et par ligne.
3. Un tableau par région donne : tenders, en cours, exigences, part allouée, part répondue.
4. Aucun chiffre n'est donné par personne.

### US-ADM-06 — Suivre ce que fait l'IA et reprendre un traitement échoué
**Carte :** En tant qu'admin, je veux voir les traitements de l'IA par tender, ceux qui ont échoué et ce qu'ils coûtent, afin de reprendre un échec et de surveiller la qualité.
**Conversation :**
- L'IA propose, les personnes décident (AI-013).
- Un traitement échoué reprend là où il s'est arrêté, sans refaire ni doubler ce qui est fait (AI-012).
- Ce que les corrections apprennent aux modèles reste dans Configuration › AI feedback de chaque tender.

**Maquette :** Administration — `admin.html` (route `#admin`), section AI tracking.
**Règles :** DEC-127, AI-012, AI-013, AI-014, PLAT-003  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Chaque tender montre l'état de ses étapes : capture, traduction, caractérisation, allocation. Les états possibles sont terminé, en cours, échoué, en attente, ou sans objet (source en anglais).
2. Un échec montre son message et un bouton « Resume ». Après reprise, l'étape repasse en cours, et la reprise s'inscrit au journal d'audit.
3. Les colonnes donnent les exigences traitées, la part de confiance Low (DEC-120), la part de propositions corrigées par des personnes, le dernier passage et le coût.
4. Les tuiles résument les traitements en cours, ceux à reprendre, les blocs capturés, le taux de correction et le coût du mois.

Écart maquette : les chiffres et coûts sont des valeurs de démonstration.

Point ouvert : la source réelle des coûts et des compteurs (chantier IA, DEC-020).

## Couverture
- Règles couvertes :
  - DEC-127 → US-ADM-01 à 06 ;
  - ACC-015 → US-ADM-01 ;
  - ACC-016 → US-ADM-03 ;
  - ACC-017 → US-ADM-02 ;
  - ACC-018 → US-ADM-01, 02, 04 ;
  - PLAT-003 → US-ADM-04, 06 ;
  - AI-012 → US-ADM-06.
