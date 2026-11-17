# Plan de notification — dans l'application et par e-mail

**Validé le 17 novembre 2026 (DEC-127 à DEC-136).** Ce plan fait référence pour les notifications de Smart Req. Il remplace la ligne PLAT-005 (« déclencheurs, destinataires, regroupement et relances non finalisés ») et la part notifications d'OPEN-11.

- Maquette de la cloche, de l'accueil et des réglages : [`proposals/notifications/index.html`](../../proposals/notifications/index.html). Les réglages sont aussi dans le prototype : fenêtre Settings de l'accueil (DEC-138).
- Les huit e-mails, en HTML pour messagerie, avec leur version texte et un `.eml` à ouvrir dans Outlook : [`proposals/notifications/emails/`](../../proposals/notifications/emails/index.html).
- Les user stories : US-X-10, US-X-15 à US-X-18, US-HOME-07, US-DASH-15, US-CMP-24, US-CMP-26 et US-CFG-05 ([backlog](../stories/README.md)).

Dans ce plan, **relance** veut dire le rappel qu'un tender manager adresse à une personne (DEC-125, US-CMP-24), jamais la relance d'un modèle d'IA (US-ALM-21).

## En bref

- On ne prévient que **la personne dont c'est le tour d'agir**, jamais l'auteur de l'action, et seulement pour le travail de son sous-système.
- **Tout arrive dans l'application**, sous une cloche personnelle, la même sur tous les écrans. Son point signale du nouveau, pas du travail en attente.
- **L'e-mail ne rattrape que ce qui n'a pas été vu** dans Smart Req. Il est recalculé au moment de partir.
- **Au plus un e-mail par jour** : un résumé à 8:00, les jours ouvrés, tous tenders confondus, et rien si rien n'est nouveau. Quatre cas partent dans l'heure : une relance, une mention, l'ajout à un tender et, pour le tender manager qui l'a lancé, la fin ou l'échec d'un traitement.
- **Aucun e-mail automatique** pour un retard ou une échéance : la relance reste un geste humain, plafonné.
- **Aucune mesure individuelle** : pas de suivi d'ouverture ni de clic ; l'état « vu » reste privé.

## 1. Ce qui a changé, ce qui attend

| | Ce qui a changé | Ce qui attend |
|---|---|---|
| Exemple | « Thibaud Breton sent you a reminder about 4 assignments » | « 16 assignments to answer · 2 waiting more than 5 days » |
| Nature | Un événement daté, adressé à une personne | Un état calculé, toujours à jour |
| Vie | Nouveau → vu → lu ; reste 30 jours dans la cloche | Disparaît quand le travail est fait |
| Où | La cloche (New, Earlier), le résumé e-mail, les e-mails immédiats | Les compteurs des écrans, « What needs you now », le pied de la cloche |

**Seule la première colonne est une notification.** Les cloches du prototype mélangent les deux : une par écran, chacune calcule ce qui attend sur son propre écran. Sur un vrai tender, quelque chose attend toujours : le point resterait allumé en permanence, et l'accueil n'a pas de cloche. La règle de PLATFORM reste valable pour ce qui attend : calculer, résumer par nature avec un compte, nommer l'exigence quand elle est seule, dire quand rien n'attend. Elle s'applique désormais au pied de la cloche (NOTIF-012).

## 2. Qui est prévenu

- **NOTIF-001 — DEC-127 : la personne dont c'est le tour.**
  - Pour une affectation : la personne en charge (PIC) de l'organisation (DEC-087).
  - Pour une décision du tender manager : tous les tender managers du tender. Le premier qui tranche efface la notification pour les autres.
  - Pour une réponse à une demande ou à une question : son auteur.
- **NOTIF-002 — DEC-127 : jamais l'auteur de l'action**, même quand il agit pour un autre : un tender manager qui répond à la place d'un contributeur n'est pas prévenu de sa propre réponse. Aucune notification ne propose à une personne une action qui lui est adressée (US-X-10, critère 4).
- **NOTIF-003 — DEC-127 : son sous-système seulement.** Un contributeur lit tout le tender (DEC-012), mais n'est prévenu que du travail de son sous-système (US-X-10, critère 3). Une mention fait exception : elle s'adresse à une personne nommée.
- **NOTIF-004 — DEC-127 : jamais hors de l'outil.**
  - Rien n'est envoyé au client (QA-003, US-X-10 critère 5) ni aux partenaires externes, qui n'ont pas accès à Smart Req (DEC-082).
  - Pas d'escalade vers un supérieur hiérarchique : la hiérarchie est hors de Smart Req (ACC-010).
- **NOTIF-024 — DEC-130 : les exigences à allouer d'un sous-système.** Un sous-système n'a pas forcément de manager (DEC-124). Quand des exigences y arrivent, tous ses contributeurs le voient dans la cloche. Ceux qui y sont staffés sans périmètre le reçoivent aussi dans leur résumé e-mail ; ceux qui ont un périmètre, dans la cloche seulement.
- **Affectation sans personne (DEC-025) :** personne n'est prévenu à titre personnel. Le manque reste visible dans Users et dans les compteurs (staffing incomplet, PLAT-008).

## 3. Trois niveaux

| Niveau | Dans l'application | Par e-mail | Pour quoi |
|---|---|---|---|
| **A — Immédiat** | Tout de suite | Si la notification n'est toujours pas vue 10 minutes plus tard, regroupée par tender | Une personne s'adresse à vous (relance, mention), ou vous attendez l'événement (ajout à un tender, fin ou échec d'un traitement que vous avez lancé) |
| **B — Résumé** | Tout de suite | Dans le résumé quotidien, si elle n'est toujours pas vue à l'heure du résumé | Ce qui vous demande d'agir |
| **C — Information** | Tout de suite | Jamais | Ce qui vous concerne sans rien vous demander |

- **NOTIF-005 — DEC-127 : recalcul à l'envoi.** Un e-mail se construit au moment de partir, depuis l'état courant.
  - Ce qui a été vu, fait ou annulé entre-temps disparaît : Undo, réaffectation corrigée, demande déjà tranchée par un autre tender manager.
  - S'il ne reste rien, rien ne part.
  - Les rafales se règlent ainsi : valider 300 exigences d'un coup donne la ligne « 300 new assignments », pas 300 e-mails.
- **NOTIF-006 — DEC-127 : plafonds.**
  - Au plus un résumé par jour et par personne, tous tenders confondus.
  - Au plus trois e-mails immédiats par jour et par personne ; les suivants attendent le résumé.
  - Au plus une relance par personne et par tender dans la fenêtre réglée par le tender (NOTIF-020).
- **NOTIF-007 — DEC-131 : l'heure du résumé.** 8:00 dans le fuseau de la personne, lu dans son profil d'entreprise, les jours ouvrés. La personne peut choisir tous les jours (utile les dernières semaines avant une soumission) ou aucun résumé.
- **NOTIF-008 — DEC-127, DEC-129 : ce qui attend n'est pas une nouvelle.** Ces trois états ne créent pas de notification :
  - le dépassement du seuil de retard ;
  - l'échéance de soumission à 7 jours ou moins ;
  - la clôture des questions client à 3 jours ou moins.

  Ils ajoutent une ligne grise « Still waiting » à un résumé qui part de toute façon, jamais un e-mail à eux seuls. En faire un e-mail automatique reviendrait à une relance que personne n'a décidée (DEC-125).
- **NOTIF-009 — DEC-127 : jamais de notification pour :**
  - ses propres actions ;
  - les propositions et la confiance de l'IA, les OBS faibles, les découpes incertaines : c'est du travail dans les tables, pas des nouvelles ;
  - les statistiques ;
  - le travail des autres sous-systèmes.

## 4. Le catalogue

La colonne « Dans la cloche » donne le texte de l'interface. La colonne Pilote dit ce qui sert dès le premier pilote (création jusqu'à validation de l'allocation, DEC-022, DEC-135) et ce qui vient avec Compliance et Q&A.

### Contributeur

| Événement | Source | Destinataire | Niveau | Dans la cloche | Pilote |
|---|---|---|---|---|---|
| Ajouté à un tender (staffé sur un sous-système, ou dans l'équipe du tender) | US-TEAM-05, US-NEW-07 | La personne ajoutée | A — l'e-mail part même si la personne a coupé les e-mails : c'est le premier contact | Thibaud Breton added you to STB-2026 · SIG | Oui |
| Des exigences arrivent à allouer dans son sous-système (passe 1 Turnkey, nouvelle version qui en renvoie en revue) | US-ALM-07, US-CHG-01 | Les contributeurs du sous-système (NOTIF-024) | B sans périmètre, C avec | 23 requirements to allocate in SIG | Oui |
| Sa demande de réallocation est refusée : l'exigence lui revient | US-ALM-30 | L'auteur de la demande | B | Your reallocation request for SRM-00042 was declined | Oui |
| Sa demande de réallocation est approuvée | US-ALM-30 | L'auteur de la demande | C | Your reallocation request for SRM-00042 was approved | Oui |
| Mention « @ » dans un commentaire | US-X-02 | La personne mentionnée | A | Claire Moreau mentioned you on SRM-00057 | Oui, avec les commentaires (DEC-132) |
| Relance d'un tender manager | US-CMP-24, DEC-125 | La PIC de chaque affectation relancée | A — un e-mail par relance (NOTIF-020) | Thibaud Breton sent you a reminder about 4 assignments | Après |
| Nouvelles affectations (allocation validée, réaffectation à soi, renvoi approuvé en sa faveur) | US-CMP-01, US-CMP-23 | La PIC (DEC-087) | B — une ligne par tender | 12 new assignments in SIG | Après |
| Réponse rouverte par une nouvelle version | LIFE-007, US-CMP-27 | La PIC dont le verdict revient à « Awaiting answer » | B | 3 of your answers were reopened by v2.2 | Après |
| Le client a répondu à sa question (réponse confirmée) | US-QA-08, US-QA-09 | L'auteur de la question et la PIC de l'affectation | B | The client answered your question on SRM-00031 | Après |
| Un tender manager modifie son verdict | US-CMP-25 | La PIC qui l'avait donné | C (DEC-133) | Thibaud Breton changed your verdict on SRM-00004 | Après |
| Commentaire sur une de ses affectations | US-X-02 | La PIC | C — groupé | 3 new comments on your assignments | Après |
| Sa question est marquée envoyée au client | US-QA-06 | L'auteur de la question | C | Your question on SRM-00031 was sent to the client | Après |

### Tender manager

| Événement | Source | Destinataire | Niveau | Dans la cloche | Pilote |
|---|---|---|---|---|---|
| Traitement terminé ou échoué (capture à la création, document ajouté, nouvelle version) | US-CAP-01, US-CAP-11, US-DOC-04 | Le tender manager qui l'a lancé ; les autres en C | A | Functional Specification v2.1 is processed · 7 requirements changed | Oui |
| Demande de réallocation ; sous-système manquant proposé | US-ALM-29, US-ALM-10 | Tous les tender managers du tender | B | 5 reallocation requests to decide | Oui |
| Allocation complète (carte Allocation à Done, DEC-098) | US-DASH-02 | Tous les tender managers | B, une fois | Allocation is complete on RFP-2026-114 | Oui |
| Un autre tender manager téléverse une version, importe les réponses du client ou change l'échéance | US-DOC-04, US-QA-07, US-CFG-03 | Les autres tender managers | C | Marc Dubois uploaded Functional Specification v2.1 | Oui |
| Renvoi depuis Compliance (« Not mine — return it ») | US-CMP-19 | Tous les tender managers | B | 2 assignments returned as “Not mine” | Après |
| Toutes les exigences consolidées | US-CMP-20 | Tous les tender managers | B, une fois | All 104 requirements are consolidated | Après |
| Affectations au-delà du seuil de retard | US-DASH-10 | Tous les tender managers | Aucune notification : une ligne « Still waiting » du résumé, comptée par sous-système (DEC-118). Les noms restent dans Compliance, à côté du bouton de relance | — | Après |
| Questions encore à envoyer, clôture client à 3 jours ou moins | US-QA-04 | Tous les tender managers | Aucune notification : une ligne « Still waiting » du résumé | — | Après |

Le rapport hebdomadaire (proposition `proposals/stats`) n'est pas une notification : le tender manager l'envoie lui-même, de sa boîte, à qui il veut.

## 5. Dans l'application

- **NOTIF-010 — DEC-128 : une cloche par personne, la même partout.** Même icône, même place et même contenu sur l'accueil, le tableau de bord, Allocation, Compliance, Documents & versions, Q&A et Risks. L'assistant de création n'en a pas : c'est un parcours fermé. Le contenu dépend de la personne, jamais de l'écran.
- **NOTIF-011 — DEC-128 : le point ne signale que du nouveau.** Il s'allume quand une notification n'a pas été vue et s'éteint à l'ouverture de la cloche. Cliquer une ligne la marque lue ; « Mark all as read » les marque toutes. Pas de compteur sur l'icône : le compte est dans le panneau (« STB-2026 · 3 new »).
- **NOTIF-012 — DEC-128 : le panneau.**
  - Une section **New** (non lues), puis **Earlier** (lues, 30 jours).
  - La portée « this tender » dans un tender, « all my tenders » à l'accueil ; un bouton passe de l'une à l'autre.
  - Chaque ligne résume une nature avec son compte, nomme l'exigence quand elle est seule et garde son état réel (« 9 answered since »). Une ligne entièrement traitée passe en gris.
  - Un clic mène à l'endroit exact : l'écran filtré, ou l'exigence quand elle est seule.
  - Au pied, une ligne « Waiting on you » résume ce qui attend (la règle PLATFORM) et mène à la file ou au tableau de bord ; puis le lien vers les réglages.
- **NOTIF-013 — DEC-128 : regroupement.** Une ligne non lue réunit les notifications d'un même tender, d'une même nature et d'une même cause (la même version, la même relance, la même journée de validation) ; son compte monte. Une fois lue, la notification suivante ouvre une nouvelle ligne.
- **NOTIF-014 — DEC-127 : pas de toast pour l'action d'un autre.** Le toast reste le retour de sa propre action. On n'interrompt personne au milieu d'une saisie : le point de la cloche suffit.
- **NOTIF-015 — DEC-128 : « Since your last visit » à l'accueil.** S'il y a du nouveau, la carte « Pick up where you left off » liste les tenders où quelque chose a bougé pour la personne, une ligne par tender avec un bouton Open, et finit par « Nothing new on your N other tenders ». C'est le jumeau du résumé quotidien. Sans nouveau, la carte garde sa forme actuelle. La carte de chaque tender porte une pastille « N new ».
- **NOTIF-016 — DEC-127 : rétention.** 30 jours dans la cloche. L'historique durable est le journal de l'exigence (US-X-01).
- **Accessibilité.**
  - Le bouton annonce « Notifications, 3 new ».
  - Le panneau est une boîte de dialogue que l'on parcourt au clavier et que l'on ferme avec Échap ; le focus revient au bouton.
  - Un changement de compte s'annonce poliment, sans répétition et sans déplacer le focus (WCAG 2.2, critère 4.1.3).

## 6. Par e-mail

### Les huit e-mails

Les modèles sont dans [`proposals/notifications/emails/`](../../proposals/notifications/emails/index.html) : pour chacun, le HTML (`.html`), la version texte (`.txt`) et l'e-mail complet avec ses en-têtes (`.eml`, il s'ouvre dans Outlook ou Apple Mail). `build_emails.py` les régénère depuis `content.py`, en Python standard, sans dépendance. La page `index.html` les montre en clair, en sombre, sur téléphone et en texte brut. Données fictives.

| E-mail | Niveau | Quand il part | Objet (exemple) | Pilote | Modèle |
|---|---|---|---|---|---|
| Ajout à un tender | A | 10 minutes après l'ajout s'il n'est pas vu, même si la personne a coupé les e-mails | STB-2026 — You've been added as a contributor for SIG | Oui | [added-to-tender](../../proposals/notifications/emails/added-to-tender.html) |
| Traitement terminé | A | Au tender manager qui l'a lancé, si le résultat n'est pas vu 10 minutes après | STB-2026 — Functional Specification v2.1 is processed: 7 requirements changed | Oui | [processing-finished](../../proposals/notifications/emails/processing-finished.html) |
| Traitement échoué | A | Même règle | STB-2026 — Interface Control Document couldn't be processed | Oui | [processing-failed](../../proposals/notifications/emails/processing-failed.html) |
| Mention | A | Si la mention n'est pas vue en 10 minutes | STB-2026 — Claire Moreau mentioned you on SRM-00057 | Oui, avec les commentaires | [mention](../../proposals/notifications/emails/mention.html) |
| Résumé quotidien, contributeur | B | 8:00 locale, jours ouvrés, si quelque chose de nouveau n'a pas été vu | STB-2026 — 23 requirements to allocate in SIG and 1 more update | Oui | [daily-summary-contributor](../../proposals/notifications/emails/daily-summary-contributor.html) |
| Résumé quotidien, tender manager | B | Même règle | STB-2026 — 5 reallocation requests to decide and 2 more updates | Oui | [daily-summary-tender-manager](../../proposals/notifications/emails/daily-summary-tender-manager.html) |
| Relance | A | Si la relance n'est pas vue en 10 minutes ; un e-mail par relance | STB-2026 — Reminder: 4 assignments waiting on your answer | Après | [reminder](../../proposals/notifications/emails/reminder.html) |
| Résumé quotidien avec Compliance | B | Même règle, avec les lignes « Still waiting » | STB-2026 — 4 new assignments and 2 more updates | Après | [daily-summary-compliance](../../proposals/notifications/emails/daily-summary-compliance.html) |

### Règles

- **NOTIF-017 — DEC-127 : la forme.**
  - **Objet** : le tender, puis la chose la plus importante avec son compte, puis « and N more updates ».
  - **Ligne d'aperçu** : pour un résumé, la période et les tenders ; pour un e-mail immédiat, la phrase utile (le mot du tender manager, le début du commentaire).
  - **Corps**, toujours dans le même ordre : « Smart Req », une ligne de contexte (le tender, ou « Daily summary » et la date), une phrase-titre, le contenu, au plus un bouton, puis le pied.
  - **Résumé** : groupé par tender puis par nature. Chaque ligne a son lien vers l'endroit exact. Les lignes « Still waiting » sont en gris, en bas de leur tender.
  - **Texte d'abord** : aucune image, aucun graphique, aucun pixel ni lien de suivi. La version texte se suffit à elle-même, car Outlook classique peut forcer l'affichage en texte brut.
  - **Aucun lien n'agit à l'ouverture**, car Safe Links peut ouvrir un lien avant la personne. Un lien mène à un écran, derrière la connexion SSO ; l'action se fait là.
  - **Dates absolues** (« Fri 20 Nov ») : un e-mail se lit plus tard. En anglais, comme l'interface.
- **NOTIF-018 — DEC-127 : le pied.**
  - Il dit pourquoi la personne reçoit cet e-mail. Pour un résumé, il ajoute que ce qui a déjà été vu n'y figure pas.
  - Il donne le lien vers les réglages : fréquence, ou couper les e-mails d'un tender.
  - Il dit que la boîte d'envoi n'est pas lue. Seule exception, la relance : y répondre écrit au tender manager.
  - Pas de désabonnement en un clic (RFC 8058) : il n'est exigé que des envois de masse vers des boîtes grand public, et il supposerait un lien qui agit sans connexion.
- **NOTIF-019 — DEC-136 : l'expéditeur.** Une boîte d'envoi interne au tenant Microsoft 365 de l'entreprise, nommée « Smart Req » et sans réponse, à demander à l'IT. Pour une relance, l'expéditeur affiché est « <tender manager> via Smart Req », et la réponse va directement au tender manager (Reply-To).
- **NOTIF-020 — DEC-129 : la relance.**
  - Un geste de relance (bouton, touche R ou action groupée, DEC-125) donne **un e-mail par personne**. Il liste toutes ses affectations relancées par ce geste, avec leur âge.
  - Le tender manager peut ajouter un mot facultatif, repris en tête et dans la ligne d'aperçu.
  - **Rien n'est relancé automatiquement.** « Maximum reminder cadence » (US-CFG-05) devient un plafond par personne et par tender ; l'option « Manual only » disparaît.
  - Avant la fin du plafond, le bouton dit quand la prochaine relance sera possible. Le tender manager peut toujours appeler la personne.
- **NOTIF-025 — PROP : le code des e-mails.** Le code de production reprend les règles de HTML pour messagerie appliquées par les modèles :
  - **Mise en page** : en tableaux (`role="presentation"`), avec tous les styles en ligne. Le bloc `<style>` n'apporte que des améliorations : mode sombre, téléphone.
  - **Largeur** : une colonne de 600 px. Un tableau conditionnel réservé à Outlook la tient là où `max-width` est ignoré, car Outlook pour Windows affiche le HTML avec le moteur de Word.
  - **Polices et images** : aucune image et aucune police web, seulement les polices du système (Segoe UI, San Francisco, Roboto, Arial). Rien ne casse quand les images sont bloquées.
  - **Bouton** : un rectangle VML pour Outlook pour Windows, un lien rembourré ailleurs.
  - **Mode sombre** : `color-scheme` et `prefers-color-scheme` (Apple Mail, Outlook pour Mac), sélecteurs `[data-ogsc]` et `[data-ogsb]` (Outlook.com). Outlook pour Windows et les applications Gmail recolorent eux-mêmes ; les couleurs sont choisies pour survivre à l'inversion (ni blanc pur sur noir pur, ni texte dans une image).
  - **Couleurs** : celles des tokens des thèmes clair et sombre du prototype, en hexadécimal, car les variables CSS ne passent ni dans Outlook ni dans Gmail. Seule la couleur des liens (#2456C5) est propre à l'e-mail : le navy de `--accent` est trop proche du texte. Contraste d'au moins 4,5:1 dans les deux thèmes.
  - **Ligne d'aperçu** : cachée, suivie de caractères de remplissage pour que le début du corps ne s'y affiche pas.
  - **Accessibilité** : `lang="en"`, `role="article"` avec l'objet comme `aria-label`, un seul `h1`, des liens au libellé explicite.
  - **Structure** : multipart/alternative, la version texte puis le HTML, avec le même contenu et les mêmes liens. Moins de 15 Ko par e-mail ; Gmail coupe un message au-delà de 102 Ko.

## 7. Réglages

- **NOTIF-021 — DEC-127 : des réglages personnels, pas par tender.** Ils s'ouvrent depuis le menu de l'avatar et valent pour tous les tenders de la personne. Le seuil de retard et le plafond de relance restent dans la Configuration du tender (US-CFG-05) : ils engagent toute l'équipe. Dans le prototype, ces réglages forment la rubrique Notifications de la fenêtre **Settings**, ouverte depuis l'accueil (bouton « Settings » ou avatar), avec le thème et la langue de l'interface (DEC-138, US-X-18).
- **NOTIF-022 — DEC-127, DEC-131 : peu de réglages, des défauts sobres.**
  - Résumé quotidien : jours ouvrés à 8:00 (par défaut), tous les jours à 8:00, ou aucun.
  - E-mail pour une relance : oui par défaut.
  - E-mail pour une mention : oui par défaut.
  - E-mail pour la fin ou l'échec d'un traitement qu'on a lancé : oui par défaut.
  - Ajout à un tender : toujours envoyé.
  - Par tender : couper les e-mails ; la cloche reste.
  - Rien ne se coupe dans l'application : c'est la référence.

## 8. Données personnelles et représentants du personnel

- **NOTIF-023 — DEC-127 : l'état « vu » est privé.** Il sert seulement à ne pas envoyer un e-mail en double. Il n'est montré à personne d'autre et n'entre dans aucune statistique, comme les brouillons (DEC-090) et sans mesure individuelle (DEC-118). Aucun suivi d'ouverture ou de clic par personne.
- Les relances datées et l'âge des affectations restent des données sur le travail d'une personne. Avec le reste du suivi (DEC-118 cite déjà CSE, Betriebsrat et RGPD), le dispositif est à présenter aux représentants du personnel avant le déploiement.
- **Écart du prototype à corriger** : « What needs you now » écrit « SRM-00001 unopened for 9 days ». Ce texte suppose qu'on suit l'ouverture d'une exigence par une personne. Le remplacer par « no answer for 9 days ».

## 9. Le pilote, puis la suite

| Phase | Dans l'application | Par e-mail |
|---|---|---|
| **Pilote** — création jusqu'à validation de l'allocation (DEC-135) | Cloche personnelle sur tous les écrans, « Since your last visit », réglages | Ajout à un tender ; traitement terminé ou échoué ; mention, avec les commentaires ; résumé quotidien avec les exigences à allouer, les demandes refusées, les demandes de réallocation, les sous-systèmes manquants proposés et l'allocation complète |
| **Avec Compliance et Q&A** | Les événements « Après » du catalogue | Relance ; un résumé plus riche : nouvelles affectations, réponses rouvertes, réponses du client, lignes « Still waiting » |
| **Plus tard, si le besoin apparaît** | Une page Inbox complète, avec « Done » ; la mise en attente jusqu'à une date ; « Out of office until 24 Nov » à côté du bouton de relance, lu dans la réponse automatique Outlook de la personne (Microsoft Graph, permission MailboxSettings.Read), à voir avec l'IT et les représentants du personnel | Le flux d'activité Teams à la place de l'e-mail immédiat (DEC-134). Il suppose que l'application Teams de Smart Req soit installée pour chaque destinataire |

## 10. Mise en œuvre — PROP, non normatif

- **Chaîne.**
  - Un événement métier est écrit dans la même transaction que le changement (outbox).
  - Un service de notifications applique la table du catalogue : nature, destinataires, niveau. Il écrit une ligne par destinataire avec sa clé de regroupement (tender, nature, cause).
  - Il planifie l'e-mail : 10 minutes pour le niveau A, le résumé à 8:00 locale pour le niveau B.
  - À l'heure dite, il recalcule depuis l'état courant (NOTIF-005), compose les versions HTML et texte, envoie et trace l'envoi, sans suivi d'ouverture.
- **Envoi.** Depuis le tenant Microsoft 365 de l'entreprise (DEC-136), par l'un des deux moyens :
  - Microsoft Graph (OAuth) au nom d'une boîte partagée ;
  - High Volume Email, réservé aux destinataires internes.

  Pas d'authentification SMTP basique : Exchange Online la coupera par défaut à partir de décembre 2026 (calendrier rapporté, à confirmer). Le choix se fait avec l'IT.
- **En-têtes.**
  - Un Message-ID unique par e-mail, sans fil forcé : chaque résumé se lit seul.
  - `X-SmartReq-Reason` (summary, reminder, mention, added, processing) et `X-SmartReq-Tender` : chacun peut classer ses e-mails par une règle Outlook, comme le permet GitLab avec `X-GitLab-NotificationReason`.
  - `Auto-Submitted: auto-generated` (RFC 3834) et `X-Auto-Response-Suppress: All` (Exchange) : pas de réponse automatique d'absence vers la boîte d'envoi. Selon le mode d'envoi retenu, vérifier que ces en-têtes passent : certains n'acceptent que les en-têtes `X-`.
  - `Reply-To` : le tender manager, pour une relance seulement.
- **Temps réel.** Le point de la cloche suit les nouvelles notifications par une connexion temps réel ou par un rafraîchissement chaque minute. Les deux suffisent à cette échelle (10 utilisateurs simultanés, PLAT-006).
- **Liens.** Chaque lien porte le tender, l'écran et le filtre ou l'exigence, et doit survivre au passage par la connexion SSO.
- **Fiabilité.** Une clé d'idempotence par notification : une reprise n'envoie jamais deux fois le même e-mail.
- **Une seule source de texte.** Une ligne de la cloche et la ligne correspondante du résumé disent la même chose : les composer à partir des mêmes données, avec les modèles de `proposals/notifications/emails/` comme référence de contenu et de HTML.
- **À vérifier en recette.**
  - Une validation en masse donne une ligne et au plus un e-mail par personne.
  - Une action annulée avant l'envoi ne part pas.
  - Une notification vue dans l'application ne figure dans aucun e-mail.
  - Un contributeur n'est jamais prévenu du travail d'un autre sous-système.
  - Un tender manager qui tranche efface la demande pour ses collègues.
  - Le résumé respecte le fuseau de la personne.
  - Chaque e-mail se lit en texte brut, dans Outlook pour Windows, dans Outlook sur le web et sur téléphone.

## 11. Mesurer le bruit

- Mesures agrégées par tender et par sous-système, jamais par personne (DEC-118) :
  - e-mails reçus par personne et par semaine, en médiane ;
  - part des notifications vues dans l'application avant l'e-mail, donc jamais envoyées ;
  - part des personnes qui coupent le résumé ou un tender, par nature de notification ;
  - délai entre une notification et l'action, par sous-système.
- Ni taux d'ouverture ni taux de clic : ils ne valent rien ici (images bloquées, Safe Links qui ouvre les liens), et ils mesureraient des personnes.
- **Cible : au plus 5 e-mails par semaine pour un contributeur.** Une hausse des coupures dit que le résumé est trop bavard : on retire une nature, pas un garde-fou.

## 12. Décisions du 17 novembre 2026

| Décision | Question | Ce qui est décidé |
|---|---|---|
| DEC-127 | Le plan dans son ensemble | Ce document fait référence : destinataires, niveaux, plafonds, catalogue, forme des e-mails, réglages, confidentialité |
| DEC-128 (D1) | Que montre la cloche ? | Ce qui a changé pour la personne, la même cloche sur tous les écrans ; ce qui attend en une ligne au pied ; « Since your last visit » à l'accueil |
| DEC-129 (D2) | Relances automatiques ? | Non. La relance reste humaine ; la cadence devient un plafond ; « Manual only » disparaît de US-CFG-05 |
| DEC-130 (D3) | Qui prévenir qu'un sous-système a des exigences à allouer ? | Tous ses contributeurs, dans la cloche ; le résumé e-mail pour ceux qui y sont staffés sans périmètre |
| DEC-131 (D4) | Heure et jours du résumé | 8:00 locale, jours ouvrés ; au choix tous les jours ou aucun |
| DEC-132 (D5) | Construire les mentions « @ » ? | Oui, avec les commentaires, en niveau A |
| DEC-133 (D6) | Prévenir la PIC quand un tender manager modifie son verdict ? | Oui, dans la cloche seulement |
| DEC-134 (D7) | Teams ? | Plus tard, pas dans le pilote |
| DEC-135 (D8) | Périmètre du pilote | Ajout à un tender, traitement terminé ou échoué, demandes de réallocation, exigences à allouer, allocation complète ; cloche et accueil complets |
| DEC-136 (D9) | Boîte d'envoi | Une boîte interne du tenant Microsoft 365, à demander à l'IT |

**Alignés le 17 novembre 2026.**

- PLATFORM : PLAT-005 et la règle de la cloche renvoient à ce plan.
- Les user stories :
  - US-X-10 (destinataires et catalogue) et les nouvelles US-X-15 (cloche), US-X-16 (résumé quotidien), US-X-17 (e-mails immédiats) et US-X-18 (réglages) ;
  - US-HOME-07 (« Since your last visit »), US-DASH-15 (pied de la cloche), US-CMP-24 (relance), US-CMP-26 (événements de Compliance) et US-CFG-05 (plafond des relances) ;
  - leurs voisines : US-X-02 (mentions), US-HOME-02, US-CMP-17, US-CMP-27, US-QA-02, US-QA-06, US-QA-08, US-QA-09, US-DASH-08 et US-DASH-10.

**Encore à aligner : le prototype.** En attendant, la décision la plus récente prime.

- L'App Header des huit sources.
- Dans `COMPONENTS.md`, les entrées Notifications Dropdown, Notification Item, Notification Dot et Icon Button.
- Le texte « unopened for 9 days » du tableau de bord.

**Reste ouvert.**

- Le mode d'envoi (Microsoft Graph ou High Volume Email) et la boîte : avec l'IT.
- La présentation aux représentants du personnel avant le déploiement.

## Annexe — ce que font les autres

Recherche du 16 novembre 2026. Chaque affirmation renvoie à la documentation du produit ou au guide cité ; ⚠ signale une source datée ou vérifiée en partie. Les chiffres des éditeurs d'outils de notification (Courier, SuprSend, Knock) ne sont pas étayés : ils ne sont pas repris comme références.

**Trier avant d'envoyer.**

- Tous trient d'abord par la relation de la personne à l'objet. [GitHub](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/configuring-notifications) sépare *participating* (mentionné, assigné, a commenté) de *watching*. [GitLab](https://docs.gitlab.com/user/profile/notifications/) et [Jira](https://support.atlassian.com/jira-software-cloud/docs/manage-your-jira-personal-settings/) font de même, par niveau ou par rôle.
- Ses propres actions sont exclues par défaut chez GitLab.
- L'application est le relevé complet, l'e-mail un sous-ensemble. Chez [Linear](https://linear.app/docs/notifications), tout arrive dans l'Inbox ; chez [Figma](https://help.figma.com/hc/en-us/articles/360039813234), on ne peut pas couper l'in-app.
- Ce qui attend a sa propre liste, à part des nouvelles. La [To-Do List de GitLab](https://docs.gitlab.com/user/todos/) marque une tâche faite quand on agit sur l'objet. L'[Inbox prioritaire de Linear](https://linear.app/changelog/2026-09-03-priority-inbox) (septembre 2026) sépare « ce qui demande votre attention » de « ce qui peut attendre ».

**L'e-mail ne rattrape que le non-vu.**

| Produit | Quand part l'e-mail | Si c'est déjà vu dans l'outil |
|---|---|---|
| [Notion](https://www.notion.com/help/notification-settings) | Si l'application n'est pas ouverte, ou si la notification n'est pas vue en 5 minutes | Rien ne part |
| [Linear](https://linear.app/docs/notifications) | Résumé des seules notifications non lues ; délai selon l'urgence, publié en 2019 : 30 s, 5 min, 1 h ⚠ | Rien ne part |
| [Slack](https://slack.com/help/articles/360025446073) | Mentions et messages directs, seulement si l'on est inactif, groupés toutes les 15 minutes ou toutes les heures | Rien ne part |
| [Microsoft Teams](https://support.microsoft.com/en-us/office/change-how-often-you-receive-missed-activity-emails-f10949b2-f51e-40d0-8b6e-2d7c84c2c60f) | E-mail « missed activity », toutes les heures par défaut | Implicite, règle exacte non publiée ⚠ |
| [Jira Cloud](https://support.atlassian.com/jira/kb/batching-notifications-in-jira-cloud/) | Mentions et assignations tout de suite ; le reste regroupé par ticket, 3 minutes sans changement, 10 minutes au plus. Environ 30 % d'e-mails en moins | Envoyé quand même |
| [Figma](https://help.figma.com/hc/en-us/articles/360039813234) | Commentaires groupés toutes les 30 minutes | Non documenté |

Smart Req va plus loin, avec un résumé par jour : le rythme d'un tender se compte en jours (seuil de retard à 5 jours), et la plupart des contributeurs ne vivent pas dans l'outil. Les cas immédiats couvrent l'urgent. À revoir si les tests montrent qu'un résumé du matin arrive trop tard en fin de tender (DEC-131).

**Relances.** Les produits qui en envoient restent sobres. GitLab envoie un seul e-mail la veille de l'échéance ; [Planner](https://support.microsoft.com/en-us/planner/stay-updated-with-notifications-in-planner) offre un seul interrupteur (en retard, dû aujourd'hui, dû sous 7 jours). Apple ([Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/notifications)) : « avoid sending multiple notifications for the same thing, even if someone hasn't responded ». Aucune règle chiffrée faisant autorité n'a été trouvée.

**Le panneau.**

- **Badge.** [SAP Fiori](https://www.sap.com/design-system/fiori-design-web/v1-148/ui-elements/notification-center/usage) compte le nouveau depuis la dernière ouverture et remet le compte à zéro à l'ouverture. Slack réserve le chiffre à ce qui vous est adressé et met un point pour le reste. Un point seul, notre choix, est le plus discret.
- **États.** GitHub ([inbox](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/viewing-and-triaging-notifications/managing-notifications-from-your-inbox)) sépare « lu » et « Done », gardé 3 mois. Notre ligne grisée quand le travail est fait joue le rôle du « Done », sans geste de plus.
- **Regroupement.** [Fluent](https://fluent2.microsoft.design/components/web/react/core/toast/usage) fusionne des événements semblables (« Uploading 6 files ») ; SAP les range en groupes repliables.
- **Rétention.** 3 mois chez GitHub ; 30 jours chez [Confluence](https://confluence.atlassian.com/confcloud/workbox-notifications-724765365.html) ; 4 semaines dans le flux d'activité [Teams](https://learn.microsoft.com/en-us/microsoftteams/platform/concepts/design/activity-feed-notifications).
- **Toasts.** Ils disparaissent en 5 à 8 secondes ([Atlassian](https://atlassian.design/components/flag/usage), [GitLab Pajamas](https://design.gitlab.com/components/toast), Fluent). On ne s'en sert jamais pour une erreur ([NN/g](https://www.nngroup.com/articles/indicators-validations-notifications/)), ni pour une information qu'on ne retrouve nulle part ailleurs.
- **Accessibilité.** Le critère [WCAG 2.2 4.1.3](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html) exige d'annoncer les messages d'état sans déplacer le focus. Une région « status » polie existe dans la page avant que le contenu arrive ; on ne déplace jamais le focus vers une notification ([Inclusive Components](https://inclusive-components.design/notifications/)).
- **Plus tard si le besoin apparaît.** Une page Inbox complète, avec tri et « Done » (GitHub, Linear). La mise en attente jusqu'à une date (GitLab : 1 h, plus tard aujourd'hui, demain 8:00 heure locale).

**Réglages.**

- Peu de cases, ou des préréglages plutôt qu'une longue liste ([Smashing Magazine, 2025](https://www.smashingmagazine.com/2025/07/design-guidelines-better-notifications-ux/)).
- Les heures de travail suivent le fuseau de la personne ([Slack](https://slack.com/help/articles/214908388-Pause-your-Slack-notifications) ; [Basecamp](https://signalvnoise.com/svn3/basecamp-3-work-can-wait), 8:00–18:00 du lundi au vendredi ⚠ 2015). Le contre-exemple est GitLab, qui envoie ses rappels à 00:50, heure du serveur.

**L'e-mail dans Microsoft 365.**

- Outlook classique peut forcer l'affichage en [texte brut](https://support.microsoft.com/en-US/Outlook/read-email-messages-in-plain-text-in-classic-outlook), et le benchmark CIS de niveau 2 le recommande : la version texte doit se suffire à elle-même.
- Outlook pour Windows inverse les couleurs en mode sombre ([Litmus, 2025](https://www.litmus.com/blog/the-ultimate-guide-to-dark-mode-for-email-marketers)).
- [Safe Links](https://learn.microsoft.com/en-us/defender-office-365/safe-links-about) analyse les liens avant la personne et ouvre dans un bac à sable ceux dont il ne connaît pas la réputation, courrier interne compris si l'option est active. D'où aucun lien qui agit à l'ouverture, et des clics comptés qui incluent des robots.
- Le désabonnement en un clic ([RFC 8058](https://www.rfc-editor.org/rfc/rfc8058)) vise les envois commerciaux et de masse ([Google](https://support.google.com/a/answer/14229414), [Outlook.com](https://techcommunity.microsoft.com/blog/outlook/strengthening-email-ecosystem-outlook%E2%80%99s-new-requirements-for-high%E2%80%90volume-senders/4399730)) ; le courrier transactionnel interne en est exclu.
- Envoi depuis Microsoft 365 : [options documentées](https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/how-to-set-up-a-multifunction-device-or-application-to-send-email-using-microsoft-365-or-office-365) (septembre 2026). High Volume Email ([disponible et facturé depuis juin 2026](https://mc.merill.net/message/MC1243552)) ne sert que des destinataires internes. L'authentification SMTP basique [sera coupée par défaut à partir de décembre 2026](https://techcommunity.microsoft.com/blog/exchange/updated-exchange-online-smtp-auth-basic-authentication-deprecation-timeline/4489835) ⚠.

**Volume.**

- Trop de notifications est la plainte la plus fréquente en test utilisateur (Smashing).
- Meta a réduit les notifications d'un groupe pendant un an : les visites ont d'abord baissé, puis l'usage et la satisfaction ont dépassé ceux du groupe témoin ([repris ici](https://exde601e.blogspot.com/2023/01/notifications-why-less-is-more.html), original inaccessible ⚠).
