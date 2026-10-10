<!-- Généré depuis le backlog du 10 octobre 2026 ; voir README.md pour les conventions. -->
# Stratégies d'écart, conformité externe et risques (US-RSK)
Après un Not compliant, le responsable de l'affectation (un contributeur de son système) choisit une stratégie d'écart et lie un risque ; tout le reste en découle (DEC-105, SPEC-risks, parcours JRN-003). Le chef de projet écrit les stratégies du tender, corrige au besoin ce que reçoit le client et saisit le verdict des partenaires. Quelques termes, une ligne chacun :
- **stratégie d'écart** : ce que le tender fait d'un écart (nom + résultat externe), propre au tender, écrite dans Settings → Compliance.
- **conformité externe** : ce que le client reçoit, dérivée du verdict et de la stratégie, corrigeable par le chef de projet avec un motif (DEC-106).
- **risque** : une justification en trois phrases, identifiée `RSK-`, qui appartient au tender et se réutilise d'une exigence à l'autre (DEC-113, DEC-114).
- **partenaire** : entreprise ajoutée à un tender Turnkey, sans accès à l'outil, dont le chef de projet saisit le verdict (DEC-082).
Écrans : `compliance.html`, `risks.html`, `dashboard-et-config.html` (paramètres). Tout ce périmètre vient après le premier pilote (DEC-022).

### US-RSK-01 — Écrire les stratégies d'écart du tender
**Carte :** En tant que chef de projet, je veux écrire la liste des stratégies d'écart du tender avec ce que chacune déclare au client, afin que chaque Not compliant soit traité selon les options réelles de ce tender.
**Conversation :** Chaque tender a ses propres stratégies : la liste est vide à la création et le chef de projet l'écrit dans les paramètres (DEC-110). Une stratégie, c'est un nom et un résultat externe — Compliant, Not compliant ou Pending (SPEC-risks §2.1). Tant qu'il n'y en a aucune, un Not compliant reste signalé « Strategy missing » et sa conformité externe reste Pending. L'écran des paramètres lui-même est décrit dans US-CFG.
**Maquette :** Configuration — `dashboard-et-config.html` (route `#config`), section « Compliance », Gap Strategy Editor.
**Règles :** DEC-110, DEC-105, CONF-029  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Un tender nouvellement créé n'a aucune stratégie ; la section dit « No strategy yet. Until there is one, a Not compliant is flagged Strategy missing and its external compliance stays Pending. »
2. Le chef de projet ajoute une stratégie avec « Strategy name », un résultat (« Compliant », « Not compliant » ou « Pending », Pending par défaut) et « ＋ Add » ; un message confirme « <nom> added — declares <résultat> ».
3. Un nom vide est refusé (« Name the strategy »), un nom déjà présent sur le tender aussi (« That strategy already exists »).
4. Une stratégie ajoutée est aussitôt proposée dans Compliance pour tout Not compliant de ce tender, et seulement de ce tender.
5. Seul le chef de projet ajoute une stratégie ; le serveur refuse cette action à un contributeur.
Écart maquette : les tenders de démonstration arrivent avec quatre stratégies déjà écrites.

### US-RSK-02 — Renommer ou supprimer une stratégie d'écart
**Carte :** En tant que chef de projet, je veux renommer une stratégie ou supprimer celle qui ne sert pas, afin de garder une liste claire sans casser les exigences qui l'utilisent.
**Conversation :** Une stratégie utilisée ne se supprime pas, elle se renomme (DEC-110) : aucune exigence ne perd sa stratégie en silence. L'usage se compte en exigences dont un Not compliant utilise la stratégie.
**Maquette :** Configuration — `dashboard-et-config.html` (route `#config`), section « Compliance », Gap Strategy Editor.
**Règles :** DEC-110, CONF-029  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Chaque stratégie affiche son usage : « used N× » ou « unused ».
2. Modifier le nom puis valider (Entrée ou sortie du champ) renomme la stratégie (« Renamed to “…” ») ; Échap rend l'ancien nom ; un nom vide ou déjà pris est refusé (« A strategy needs a name », « Another strategy already has that name »).
3. Le nouveau nom apparaît partout où la stratégie sert : cellules « Gap strategy », panneaux, exports et statistiques ; les affectations la gardent.
4. Une stratégie inutilisée se supprime (« <nom> deleted ») ; sur une stratégie utilisée, le bouton de suppression est inactif, avec « In use — rename it instead ».
5. Le serveur refuse la suppression d'une stratégie utilisée, quelle que soit la voie.

### US-RSK-03 — Changer le résultat d'une stratégie déjà utilisée
**Carte :** En tant que chef de projet, je veux changer ce qu'une stratégie déclare au client en sachant combien d'exigences vont changer, afin de corriger une politique d'écart sans surprise.
**Conversation :** Changer le résultat externe d'une stratégie utilisée recalcule toutes les exigences qui l'utilisent, après une confirmation qui annonce combien changent ; les corrections du chef de projet sont conservées (DEC-111, SPEC-risks §12.4). Une stratégie inutilisée change sans confirmation.
**Maquette :** Configuration — `dashboard-et-config.html` (route `#config`), section « Compliance », Gap Strategy Editor (confirmation sous la ligne).
**Règles :** DEC-111, DEC-106, CONF-029, PLAT-003  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Changer le résultat d'une stratégie utilisée ouvre, sous sa ligne, « N requirements will change external compliance from <avant> to <après> », suivi s'il y a lieu de « · K corrected by the PM keep their value », avec « Cancel » et « Change and recompute ».
2. « Cancel » laisse le résultat et les exigences inchangés.
3. « Change and recompute » change le résultat : la conformité externe de chaque affectation qui utilise la stratégie, hors corrections, prend la nouvelle valeur, et les exigences concernées se reconsolident (« … now declares <résultat> — N requirements recomputed »).
4. Une affectation corrigée par le chef de projet garde sa valeur corrigée.
5. Changer le résultat d'une stratégie inutilisée se fait sans confirmation.
6. Chaque exigence dont ce que reçoit le client change en garde la trace dans son journal.

### US-RSK-04 — Choisir une stratégie d'écart après un Not compliant
**Carte :** En tant que contributeur, je veux choisir, après un Not compliant, ce que le tender fera de l'écart et voir aussitôt ce qui sera déclaré au client, afin de décider en connaissance de cause.
**Conversation :** C'est le geste central du module (SPEC-risks §1) : le contributeur donne la vérité technique, et la stratégie qu'il choisit décide de ce que reçoit le client (DEC-106). Le responsable de l'affectation — tout contributeur de son système — la choisit dans le panneau de décision, ou après coup sur un Not compliant déjà donné ; le chef de projet le fait pour un partenaire ([US-RSK-13](#us-rsk-13--saisir-le-verdict-dun-partenaire-et-documenter-son-écart)). Un Compliant ne porte ni stratégie ni risque (SPEC-risks §8).
**Maquette :** Compliance — `compliance.html` (route `#compliance`), Decision Panel, Gap Editor (Strategy + Risk).
**Règles :** DEC-105, DEC-106, DEC-108, CONF-029  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Choisir « ✕ Not compliant » ouvre d'abord « Gap strategy », la liste des stratégies du tender, sur « — Pick a strategy — ».
2. Une stratégie choisie fait apparaître la ligne « Declared to the client: <résultat> » ; un message confirme « <ID> · <SYS> — <stratégie>: the client is told <résultat> » et le journal de l'exigence le note.
3. Sans aucune stratégie sur le tender, le champ dit « No strategy is defined for this tender yet — the project manager writes them in Settings → Compliance. Until then the client is told Pending. »
4. Sur un Not compliant déjà donné, un contributeur du système choisit ou change la stratégie depuis le panneau ; pour tout autre lecteur le champ est en lecture seule et montre « Strategy missing » s'il est vide.
5. Confirmer un Compliant n'enregistre ni stratégie ni risque sur l'affectation.
Point ouvert : quand un Not compliant redevient Compliant, ce que deviennent sa stratégie, ses liens de risque et une éventuelle correction du chef de projet n'est pas décidé — la maquette efface stratégie et risques et garde la correction (docs/gap SPECS, « Statuts d'une affectation », Toujours ouvert).

### US-RSK-05 — Lier un risque existant à un Not compliant
**Carte :** En tant que contributeur, je veux lier à mon Not compliant un risque déjà écrit sur le tender, afin de réutiliser les risques plutôt que d'en créer un par exigence.
**Conversation :** Les risques se réutilisent : quelques centaines de Not compliant pointent vers environ moitié moins de risques (SPEC-risks §1). On choisit donc d'abord un risque existant (DEC-113). Les suggestions sont classées « déjà liés sous le même chapitre », puis le reste du tender, jamais par système : un risque appartient au tender (DEC-114). La stratégie n'est pas portée par le risque : deux exigences peuvent partager un risque avec des stratégies différentes.
**Maquette :** Compliance — `compliance.html` (route `#compliance`), Gap Editor (Strategy + Risk), Risk Chip.
**Règles :** DEC-105, DEC-113, DEC-114, CONF-029  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Sous la stratégie, « Risk » propose la recherche « Search the tender's risks — ID or words », sur l'ID et le texte des risques du tender ; sans aucun risque sur le tender, elle est inactive et dit « No risk on this tender yet ».
2. Les suggestions montrent d'abord les risques déjà liés dans la même section, marqués « same heading », puis le reste du tender ; chacune donne son ID, sa première phrase et « N req. » ; six au plus, puis « N more — refine the search ».
3. Un clic lie le risque (« <RSK> linked to <ID> ») ; il s'affiche en puce avec sa première phrase et « N req. », et le lien s'inscrit au journal.
4. Une affectation peut porter plusieurs risques ; « ✕ » délie un risque (« <RSK> unlinked from <ID> »), et le geste s'annule.
5. Le même risque se lie à plusieurs exigences avec des stratégies différentes ; lier ne change ni le risque ni la conformité externe des autres exigences.
6. Une recherche sans résultat dit « No risk matches “<texte>”. »

### US-RSK-06 — Créer un risque quand aucun ne convient
**Carte :** En tant que contributeur, je veux créer un risque en répondant à trois questions quand aucun risque existant ne convient, afin que mon Not compliant soit justifié.
**Conversation :** On ne crée un risque que si aucun ne convient (DEC-113). Un risque n'est que sa justification — les trois réponses du modèle — et ses liens : pas de poids, pas de statut, pas de commentaires, pas de système (DEC-113, DEC-114). Il est aussitôt lié et disponible pour tout le tender ; le travail de fond sur les risques se fait hors de l'outil.
**Maquette :** Compliance — `compliance.html` (route `#compliance`), Gap Editor (Strategy + Risk), formulaire « New risk ».
**Règles :** DEC-113, DEC-114, DEC-105, CONF-029, PLAT-003  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. « ＋ New risk », sous les suggestions, ouvre « New risk · only if none of the existing ones fits » avec trois champs : « There is a risk that… », « The risk is caused by… », « The direct impact of the risk will be… ».
2. Les trois champs sont requis : « Save and link » avec un champ vide est refusé (« Answer the three questions — “<question>” is empty ») ; « Cancel » ferme sans rien créer.
3. Enregistrer crée un risque d'identifiant `RSK-` suivi d'un numéro séquentiel propre au tender (RSK-00001, RSK-00002…), avec son créateur et sa date, et le lie aussitôt (« <RSK> created and linked to <ID> »).
4. Le nouveau risque est immédiatement proposé à tous les Not compliant du tender et visible dans la page Risks.
5. Le formulaire ne demande ni poids, ni statut, ni système, ni commentaire.

### US-RSK-07 — Enregistrer un Not compliant sans stratégie ni risque, en le signalant
**Carte :** En tant que contributeur, je veux pouvoir confirmer un Not compliant avant d'avoir choisi sa stratégie ou son risque, afin de ne jamais retenir un verdict honnête pour un manque de documentation.
**Conversation :** Rien ne bloque (DEC-108) : le Not compliant s'enregistre, et ce qui manque est signalé, filtrable et compté. Un risque est attendu sur tout Not compliant, SIG compris : pas de réglage par système en v1 (DEC-109). Sans stratégie, la conformité externe reste Pending. La part des Not compliant documentés (« % NC logged ») est une statistique : voir US-STAT.
**Maquette :** Compliance — `compliance.html` (route `#compliance`), Gap Editor (Strategy + Risk), Risk Chip (marques « Strategy missing » / « Risk missing »), Requirement Table (Review Grid).
**Règles :** DEC-108, DEC-109, DEC-105, DEC-085, CONF-029  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. « Confirm — Not compliant » enregistre le verdict même sans stratégie et sans risque.
2. Sans stratégie, la cellule « Gap strategy » et le panneau montrent « Strategy missing » ; sans risque, la cellule « Risk » et le panneau montrent « Risk missing ».
3. Le filtre avancé isole les affectations sans stratégie et celles sans risque (mécanique du filtre : US-TAB).
4. La touche N d'un contributeur du système mène à ses Not compliant non documentés ; son panneau dit « Not compliant — document the gap. » avec ce qui manque, et « Until a strategy is picked, the client is told Pending. » tant que la stratégie manque.
5. Sur un tender SIG, Mainline ou RSC, un risque manquant est signalé exactement comme sur Turnkey.

### US-RSK-08 — Dériver la conformité externe d'une affectation
**Carte :** En tant que chef de projet, je veux que ce que le client reçoit pour chaque affectation se déduise du verdict et de la stratégie choisie, afin que personne n'ait à le saisir et que cela reste cohérent.
**Conversation :** La conformité externe est dérivée (DEC-106) : interne Compliant → externe Compliant ; interne Not compliant → le résultat de la stratégie choisie ; sans stratégie → Pending. Personne ne la saisit ; seul le chef de projet peut la corriger ([US-RSK-10](#us-rsk-10--corriger-la-conformité-externe-dune-affectation)). Elle remplace la déclaration externe du chef de projet et le texte « Risk accepted » (DEC-028, caduque).
**Maquette :** Compliance — `compliance.html` (route `#compliance`), External Compliance Field (with PM correction), Verdict Pill.
**Règles :** DEC-106, DEC-108, DEC-105, CONF-029  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Une affectation Compliant a une conformité externe Compliant, sans stratégie ni risque.
2. Une affectation Not compliant prend le résultat de sa stratégie (Compliant, Not compliant ou Pending) ; sans stratégie, Pending.
3. Une affectation sans verdict n'a pas de conformité externe.
4. Le panneau d'une affectation répondue montre « External compliance · what the client is told » (« … for this system » quand l'exigence a plusieurs affectations) et sa valeur ; aucun écran ne permet de la saisir directement.
5. Changer la stratégie, son résultat ou le verdict met la valeur à jour aussitôt.
Point ouvert : DEC-106 et CONF-029 disent « par système » alors que le verdict se donne par organisation (DEC-087, DEC-055) ; le grain de la stratégie et de la conformité externe (organisation ou système) est à confirmer — la maquette porte tout au système.

### US-RSK-09 — Consolider la conformité externe d'une exigence
**Carte :** En tant que chef de projet, je veux voir pour chaque exigence ce que le client recevra, calculé depuis ses affectations, afin de connaître la réponse du tender exigence par exigence.
**Conversation :** Au niveau de l'exigence, la conformité externe se consolide comme l'interne, mais sur trois valeurs : Not compliant l'emporte, puis Pending, sinon Compliant (SPEC-risks §8). Elle ne s'affiche qu'une fois l'interne consolidé : tant qu'une affectation n'a pas de verdict, il n'y a rien à déclarer. Une réouverture par une nouvelle version ([US-CMP-27](09-compliance.md#us-cmp-27--rouvrir-les-verdicts-dune-exigence-modifiée-par-une-nouvelle-version)) la remet donc à vide.
**Maquette :** Compliance — `compliance.html` (route `#compliance`), colonne « External compliance », Verdict Pill, Activity Timeline.
**Règles :** DEC-106, DEC-122, CONF-029  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Tant que l'exigence n'est pas consolidée, la colonne « External compliance » montre « — ».
2. Une fois l'exigence consolidée : Not compliant si une affectation l'est en externe, sinon Pending si une l'est, sinon Compliant.
3. La pastille porte « ✎ » quand au moins une affectation est corrigée par le chef de projet ; son infobulle dit si la valeur est dérivée ou corrigée.
4. Quand la valeur se fixe à Compliant ou Not compliant, le journal marque le jalon « Declared to the client: <valeur> » ; tout changement ultérieur s'y inscrit (« What the client is told changed »).
5. Une réouverture par une version vide la conformité externe de l'exigence jusqu'aux nouveaux verdicts.
Point ouvert : ce que deviennent la stratégie, les risques liés et la correction du chef de projet d'une affectation rouverte par une version n'est pas décidé ; la maquette les garde, et la page Risks compte encore l'exigence comme liée (docs/gap SPECS, « Stratégies d'écart », Toujours ouvert).

### US-RSK-10 — Corriger la conformité externe d'une affectation
**Carte :** En tant que chef de projet, je veux corriger ce que le client reçoit pour une affectation, avec un motif visible de tous, afin d'aligner la réponse sur une décision prise hors de la stratégie.
**Conversation :** Seul le chef de projet corrige, avec un motif obligatoire et visible de tous ; la valeur s'affiche corrigée, la valeur dérivée à côté, et peut revenir à la valeur dérivée (DEC-106). Il ne verrouille plus rien (ACC-011). Une correction survit à un changement du résultat de la stratégie (DEC-111).
**Maquette :** Compliance — `compliance.html` (route `#compliance`), External Compliance Field (with PM correction), Inline Form Shell.
**Règles :** DEC-106, DEC-111, DEC-085, ACC-011, CONF-029, PLAT-003  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Sur une affectation répondue, le chef de projet voit « Correct » sous la conformité externe ; il ouvre « Correct what the client is told » : « Compliant », « Not compliant », « Pending » et « Reason · required, shown to everyone ».
2. « Save correction » sans motif est refusé (« Give the reason — a correction is on the record ») ; avec motif, tous les lecteurs voient la valeur corrigée avec « ✎ », « derived: <valeur dérivée> » et « Corrected by <nom> · <date> — “<motif>” ».
3. « Change the correction » modifie la correction ; « Revert to derived » rend la valeur dérivée ; chaque geste s'annule (« Undo » ou ⌘/Ctrl + Z).
4. Correction et retour à la valeur dérivée s'inscrivent au journal avec l'avant → après et le motif.
5. Un contributeur ne voit ni « Correct » ni « Revert to derived », et le serveur refuse sa correction.

### US-RSK-11 — Consulter la liste des risques du tender
**Carte :** En tant que chef de projet, je veux lire tous les risques du tender avec leur justification et les exigences qui s'y rattachent, afin de poursuivre ce travail hors de l'outil sur une base complète.
**Conversation :** La page Risks est un écran de support du tender, comme Q&A ou Documents : la liste des risques avec leur justification (DEC-113). Elle ne crée, ne modifie, ne délie et ne supprime rien : tout se fait depuis Compliance. Ni poids, ni statut, ni matrice, ni système (DEC-113, DEC-114). On y arrive par l'icône Risks de Compliance et par la carte Risks du tableau de bord (US-DASH).
**Maquette :** Risks — `risks.html` (route `#risks`), Risk List.
**Règles :** DEC-113, DEC-114, DEC-105, DEC-012, CONF-029  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. La page « Risks » montre une ligne par risque : ID, « There is a risk that… », « The risk is caused by… », « The direct impact of the risk will be… », « Requirements » et « Created by » avec la date.
2. La recherche « Search a risk — ID or words » porte sur l'ID et les trois réponses ; le compte dit « N risks » ou « n of N » ; sans résultat, « No risk matches. »
3. Rien sur cette page ne crée, modifie, délie ou supprime un risque, et il n'y a ni colonne ni filtre par système.
4. Sans risque sur le tender, la page dit « No risk on this tender yet. », explique que les risques naissent dans Compliance et propose « Open Compliance → ».
5. « Export » produit la liste affichée ; chef de projet et contributeurs lisent la page.
Écart maquette : l'export n'est qu'un message, sans options.
Point ouvert : modifier la justification d'un risque, ou supprimer un risque devenu inutile, n'est pas spécifié depuis DEC-113 ; filtres avancés et export filtré « comme sur toute table » non plus (SPEC-risks §5, §6.2 ; docs/gap SPECS, « Page Risks », Toujours ouvert).

### US-RSK-12 — Passer d'un risque à ses exigences, et inversement
**Carte :** En tant que chef de projet, je veux aller d'une puce de risque à sa fiche et d'un risque à ses exigences, afin de voir en un geste ce que couvre un risque partagé.
**Conversation :** Compliance et Risks se renvoient l'un à l'autre : une puce `RSK-` ouvre le risque dans la page Risks ; depuis la page, une exigence ouvre Compliance sur elle, et « all → » ouvre Compliance filtrée sur toutes les exigences du risque. Les liens se déduisent de la documentation d'écart ; personne ne les saisit sur le risque.
**Maquette :** Compliance — `compliance.html` (route `#compliance`), Risk Chip, bandeau de filtre par risque ; Risks — `risks.html` (route `#risks`), Risk List.
**Règles :** DEC-113, DEC-105, CONF-029  ·  **Périmètre :** Après pilote  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Une puce `RSK-` (colonne « Risk » ou panneau) ouvre la page Risks, la ligne de ce risque mise en évidence et amenée à l'écran.
2. Dans la page Risks, chaque exigence liée est un bouton qui ouvre Compliance sur cette exigence ; un risque sans lien affiche « none ».
3. Quand un risque a plusieurs exigences, « all → » ouvre Compliance filtrée sur elles, avec un bandeau qui nomme le risque et un « ✕ » pour tout réafficher.
4. La colonne « Requirements » liste exactement les exigences dont une affectation lie ce risque ; lier ou délier dans Compliance la met à jour.

### US-RSK-13 — Saisir le verdict d'un partenaire et documenter son écart
**Carte :** En tant que chef de projet d'un tender Turnkey, je veux saisir le verdict qu'un partenaire externe m'a renvoyé, avec sa stratégie et son risque s'il n'est pas conforme, afin que sa part consolide comme celle de tout autre système.
**Conversation :** Un partenaire est une entreprise ajoutée à la liste OBS du Turnkey (voir US-ALM) : ni modèle, ni organisation, ni personne, ni accès à l'outil (DEC-082). Le chef de projet saisit son verdict au niveau du système, d'après ce que le partenaire a renvoyé (e-mail, Excel, appel) ; ce verdict consolide sans exemption ni statut propre. La provenance se lit au système, sans champ dédié. L'envoi au partenaire passe par l'export filtré ([US-CMP-28](09-compliance.md#us-cmp-28--exporter-le-registre-de-conformité-avec-options)).
**Maquette :** Compliance — `compliance.html` (route `#compliance`), Partner Verdict Entry, Gap Editor (Strategy + Risk).
**Règles :** DEC-082, DEC-105, DEC-107, DEC-108, DEC-125, DEC-085, CONF-026, CONF-029  ·  **Périmètre :** Après pilote  ·  **Variantes :** Turnkey
**Critères d'acceptation :**
1. L'affectation d'un partenaire affiche « PM · for partner » dans « Assigned to » ; son panneau explique qu'il s'agit d'une entreprise ajoutée pour ce tender, hors du modèle et sans accès, dont le chef de projet saisit le verdict.
2. Le chef de projet choisit « ✓ Compliant » ou « ✕ Not compliant », saisit « Their answer, as received » et confirme par « Record <partenaire>'s verdict — <verdict> » ; « Undo » ou ⌘/Ctrl + Z l'annule.
3. Sur un Not compliant, il choisit la stratégie et lie ou crée un risque comme un contributeur ([US-RSK-04](#us-rsk-04--choisir-une-stratégie-décart-après-un-not-compliant) à -06), sans que cela bloque, et saisit Category + Topic (Topic requis).
4. La réponse enregistrée dit « entered by the project manager from <partenaire>'s reply » et consolide avec les autres systèmes comme n'importe quel verdict.
5. Aucun contributeur ne peut saisir ce verdict, et aucune relance n'est possible vers un partenaire (« <partenaire> works outside the tool — follow up with them directly »).
6. La touche N du chef de projet mène aux partenaires dont le verdict ou la documentation d'écart reste à saisir.

## Couverture
- Règles couvertes :
  - CONF-029 (« Category + Topic sur Turnkey seulement » : voir [US-CMP-12](09-compliance.md#us-cmp-12--qualifier-un-not-compliant-par-category-et-topic-sur-un-tender-turnkey) ; « par système » : voir le point ouvert de [US-RSK-08](#us-rsk-08--dériver-la-conformité-externe-dune-affectation)) → [US-RSK-01](#us-rsk-01--écrire-les-stratégies-décart-du-tender), [US-RSK-02](#us-rsk-02--renommer-ou-supprimer-une-stratégie-décart), [US-RSK-03](#us-rsk-03--changer-le-résultat-dune-stratégie-déjà-utilisée), [US-RSK-04](#us-rsk-04--choisir-une-stratégie-décart-après-un-not-compliant), [US-RSK-05](#us-rsk-05--lier-un-risque-existant-à-un-not-compliant), [US-RSK-06](#us-rsk-06--créer-un-risque-quand-aucun-ne-convient), [US-RSK-07](#us-rsk-07--enregistrer-un-not-compliant-sans-stratégie-ni-risque-en-le-signalant), [US-RSK-08](#us-rsk-08--dériver-la-conformité-externe-dune-affectation), [US-RSK-09](#us-rsk-09--consolider-la-conformité-externe-dune-exigence), [US-RSK-10](#us-rsk-10--corriger-la-conformité-externe-dune-affectation), [US-RSK-11](#us-rsk-11--consulter-la-liste-des-risques-du-tender), [US-RSK-12](#us-rsk-12--passer-dun-risque-à-ses-exigences-et-inversement)
  - CONF-026 (saisie du verdict partenaire au niveau système ; l'export qui dit le filtre → [US-CMP-28](09-compliance.md#us-cmp-28--exporter-le-registre-de-conformité-avec-options)) → [US-RSK-13](#us-rsk-13--saisir-le-verdict-dun-partenaire-et-documenter-son-écart)
  - JRN-003 (partie stratégie d'écart, risque et conformité externe) → [US-RSK-04](#us-rsk-04--choisir-une-stratégie-décart-après-un-not-compliant) à [US-RSK-10](#us-rsk-10--corriger-la-conformité-externe-dune-affectation)
- Non couvertes, avec la raison :
  - Les autres règles de la famille (CONF-001 à CONF-028, CONF-T01 à CONF-T18, DOM-008 à DOM-010, LIFE-007) sont placées ou déclarées caduques dans la Couverture de US-CMP.md, qui couvre la famille entière.
