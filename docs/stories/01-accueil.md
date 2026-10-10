<!-- Généré depuis le backlog du 10 octobre 2026 ; voir README.md pour les conventions. -->
# Accueil — My tenders (US-HOME)

L'accueil est la porte d'entrée de SRM pour tout utilisateur, chef de projet ou contributeur. Il ouvre le parcours JRN-001 : retrouver ses tenders, voir où chacun en est, en reprendre un ou en créer un nouveau (voir US-NEW).
Termes : **ligne produit** = le type de tender fixé à la création (Turnkey, SIG, RSC) ; **ligne du tender** = les quatre stations Capture → Allocation → Compliance → Submission, dessinées en miniature sur chaque carte ; **rôle** = « Project manager » ou « Contributor », un seul par personne et par tender (DEC-030).
La page actuelle (bandeau, carte « Pick up where you left off », bloc « How a tender travels through SRM », cartes de tender) n'a aucune spec écrite : les stories qui en viennent le disent par un point ouvert.

### US-HOME-01 — Être accueilli et orienté dès l'arrivée
**Carte :** En tant que chef de projet ou contributeur, je veux voir dès l'arrivée à quoi sert SRM et quelle place j'occupe sur mes tenders, afin de savoir tout de suite par où commencer.
**Conversation :** Le bandeau salue la personne par son prénom, dit en une phrase ce que fait SRM et résume ses rôles : combien de tenders elle dirige comme chef de projet, à combien elle contribue. Il porte les deux entrées principales : créer un tender et comprendre le parcours. Une personne qui n'a encore aucun tender doit savoir quoi faire au lieu de tomber sur une page vide. L'identité vient de l'annuaire (SSO), jamais d'une saisie.
**Maquette :** Accueil — `accueil.html` (route `#home`), Home Hero.
**Règles :** JRN-001, DEC-030, PLAT-002  ·  **Périmètre :** Pilote 1 (à confirmer)  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Le bandeau affiche une salutation suivie du prénom de la personne connectée, tiré de son identité SSO.
2. Une ligne dit « You lead N tenders as project manager and contribute to M. », comptée sur les seuls tenders dont la personne est membre ; la fin « and contribute to M » disparaît quand M vaut 0.
3. Sans aucun tender, cette ligne dit « No tender yet — create the first one, or ask a project manager to add you to theirs. »
4. « ＋ New tender », dans le bandeau comme dans l'en-tête, ouvre l'assistant de création (voir US-NEW).
5. « How SRM works » réaffiche le bloc « How a tender travels through SRM » s'il était masqué et y amène la page (voir [US-HOME-03](#us-home-03--comprendre-comment-un-tender-traverse-srm)).
Point ouvert : pas de règle écrite, comportement tiré de la maquette.
Point ouvert : qui a le droit de créer un tender n'est pas fixé (JRN-001, « politique globale à préciser ») ; l'affichage de « ＋ New tender » à tous ne doit pas être lu comme une décision.

### US-HOME-02 — Reprendre le tender en cours
**Carte :** En tant que chef de projet ou contributeur, je veux retrouver en un clic le tender sur lequel je travaillais et ce qu'il reste à y faire, afin de reprendre sans chercher.
**Conversation :** Une carte « Pick up where you left off », dans le bandeau, met en avant un tender ouvert avec sa ligne en miniature et l'étape suivante chiffrée. Elle ne propose jamais un tender encore en traitement ni un tender soumis. Toute la carte ouvre le tender.
**Maquette :** Accueil — `accueil.html` (route `#home`), Continue Card dans le Home Hero.
**Règles :** JRN-001, PLAT-001  ·  **Périmètre :** Pilote 1 (à confirmer)  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. La carte montre le nom du tender, sa référence (BO-ID), sa date de dernière mise à jour et sa ligne en miniature (voir [US-HOME-05](#us-home-05--lire-lavancement-dun-tender-sur-sa-ligne)).
2. Tant qu'il reste des exigences à allouer, l'étape suivante dit « N requirements still to allocate ».
3. Quand toutes les exigences sont allouées, elle dit « N requirements still to answer in Compliance ».
4. Un tender en traitement ou soumis n'est jamais proposé ; sans tender éligible, la carte n'apparaît pas.
5. Un clic n'importe où sur la carte, ou sur « Continue → », ouvre le tableau de bord de ce tender.
Écart maquette : le tender proposé est choisi par un marquage de démonstration, pas d'après l'usage de la personne.
Point ouvert : pas de règle écrite, comportement tiré de la maquette ; la règle de choix du tender à reprendre (le dernier ouvert par la personne ?) n'est pas décidée. Le compte « still to answer in Compliance » relève de l'après-pilote (DEC-022).

### US-HOME-03 — Comprendre comment un tender traverse SRM
**Carte :** En tant que chef de projet ou contributeur qui découvre SRM, je veux voir d'un coup d'œil les étapes d'un tender et qui fait quoi, afin de comprendre où mon travail s'insère.
**Conversation :** Le bloc « How a tender travels through SRM » présente les quatre stations, une phrase sur chacune et qui la porte, puis les écrans toujours ouverts à côté. Il s'adresse à qui découvre l'outil : une fois lu, on le masque, et on peut le rouvrir. Ses textes suivent le vocabulaire décidé (Allocation et Compliance, contributeur, système, organisation (OBS), stratégie d'écart, risque).
**Maquette :** Accueil — `accueil.html` (route `#home`), Onboarding Line, Home Section Head.
**Règles :** JRN-001, DEC-029, DEC-030  ·  **Périmètre :** Pilote 1 (à confirmer)  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Le bloc affiche, dans l'ordre, Capture, Allocation, Compliance et Submission, chacune avec une phrase et le rôle qui la porte (« Project manager », « Project manager, then each system », « Contributors », « Project manager »).
2. Sous les stations, une ligne cite les écrans toujours ouverts : « Documents & versions · Q&A with the client · Risks · Team casting ».
3. « Got it — hide » masque le bloc ; il reste masqué pour cette personne lors de ses visites suivantes, sur tout poste.
4. « How SRM works » le réaffiche et fait défiler la page jusqu'à lui.
5. Masquer le bloc chez une personne ne le masque pas chez les autres.
Écart maquette : l'état masqué n'est gardé qu'en mémoire et revient à chaque réinitialisation.
Point ouvert : pas de règle écrite, comportement tiré de la maquette ; la conservation de l'état masqué comme préférence personnelle est une déduction.

### US-HOME-04 — Voir la liste de mes tenders
**Carte :** En tant que chef de projet ou contributeur, je veux voir tous les tenders dont je suis membre avec leur type, mon rôle et leur état, afin de choisir celui qui a besoin de moi.
**Conversation :** « My tenders » liste les tenders dont la personne est membre — équipe de gestion du projet ou contributeur d'un système —, jamais les autres (ACC-007). Chaque carte porte le badge de ligne produit, la référence, le rôle de la personne, le nom et la ligne du tender ; le type est ainsi annoncé partout où l'on choisit un tender (TYPE-T06). Des onglets trient par état.
**Maquette :** Accueil — `accueil.html` (route `#home`), Home Section Head, Tab Bar, Tender Card, Product Line Badge, Role Chip.
**Règles :** JRN-001, ACC-007, ACC-T09, PLAT-001, PLAT-002, DEC-030, TYPE-T06  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. La liste ne contient que les tenders dont la personne est membre ; un autre tender n'apparaît ni dans la liste ni dans les comptes, et le serveur ne le renvoie pas (ACC-T09).
2. Chaque carte montre le badge de ligne produit (Turnkey, SIG, RSC…), la référence, la puce « Project manager » ou « Contributor », le nom et la ligne du tender.
3. Une personne n'a qu'un rôle par tender : chef de projet si elle est dans l'équipe de gestion, sinon contributeur.
4. Les onglets « All », « Processing », « In progress » et « Submitted » filtrent la liste et affichent chacun leur compte ; le titre « My tenders » est suivi du nombre total ; un onglet vide dit « No tender in this view. »
5. Après déconnexion puis reconnexion, la personne retrouve les mêmes tenders dans le même état (PLAT-001).
Écart maquette : la liste montre des tenders de démonstration non ouvrables (« Demo project — list & status only ») et déduit le rôle d'un texte libre ; rien de cela n'existe dans le produit.
Point ouvert : pas de règle écrite pour la carte, comportement tiré de la maquette ; ce qui fait passer un tender à « Submitted » n'est décrit nulle part.

### US-HOME-05 — Lire l'avancement d'un tender sur sa ligne
**Carte :** En tant que chef de projet, je veux voir sur chaque carte où en est le tender, en une ligne, afin de repérer ceux qui avancent et ceux qui attendent.
**Conversation :** La ligne a quatre stations ; seule la station courante porte un compteur : le pourcentage de traitement pendant la capture, puis les exigences allouées sur le total, puis les conformités internes renseignées sur le total, puis une coche quand la réponse est soumise. Le passage d'Allocation à Compliance se fait seul, à 100 % d'exigences allouées, jamais par un clic. La carte n'affiche plus ni santé du tender ni compte à rebours.
**Maquette :** Accueil — `accueil.html` (route `#home`), Tender Line (variante mini) dans la Tender Card et la Continue Card.
**Règles :** JRN-001, DEC-098, PLAT-008  ·  **Périmètre :** Pilote 1 (à confirmer)  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Pendant le traitement IA, la station courante est Capture avec le pourcentage d'avancement ; l'étape en cours se lit au survol.
2. Tant que toutes les exigences ne sont pas allouées, la station courante est Allocation avec « alloués / total ».
3. Dès que toutes les exigences sont allouées, la station courante devient Compliance avec « conformités internes renseignées / total », sans action de personne.
4. Si une exigence cesse d'être allouée (nouvelle version, réouverture), la ligne revient à Allocation, comme la carte Allocation du tableau de bord (DEC-098).
5. Un tender soumis montre les quatre stations franchies et une coche sur Submission.
6. Aucune carte n'affiche d'indicateur de santé composite ni de jours restants.
Écart maquette : les compteurs de démonstration ne concordent pas avec ceux du tableau de bord ; dans le produit, ce sont les mêmes données.
Point ouvert : pas de règle écrite, comportement tiré de la maquette ; le passage à Submission n'est pas spécifié ; le compteur Compliance relève de l'après-pilote (DEC-022).

### US-HOME-06 — Ouvrir un tender depuis l'accueil
**Carte :** En tant que chef de projet ou contributeur, je veux ouvrir un tender depuis sa carte, afin d'arriver sur son tableau de bord et d'y travailler.
**Conversation :** Un clic sur une carte ouvre le tableau de bord du tender, qui devient le tender courant de tous les écrans. Le cas d'un tender encore en traitement n'est pas tranché : la maquette refuse de l'ouvrir depuis l'accueil, alors que la création ouvre son tableau de bord pendant le traitement (voir [US-NEW-08](02-creation.md#us-new-08--vérifier-le-récapitulatif-et-créer-le-tender)).
**Maquette :** Accueil — `accueil.html` (route `#home`), Tender Card ; puis Tableau de bord — `dashboard-et-config.html` (route `#dashboard`).
**Règles :** JRN-001, ACC-007, PLAT-002  ·  **Périmètre :** Pilote 1  ·  **Variantes :** Toutes
**Critères d'acceptation :**
1. Un clic sur une carte ouvrable, ou sur « Open → », ouvre le tableau de bord de ce tender (voir US-DASH).
2. Les écrans ouverts ensuite nomment ce tender (référence · nom) dans leur fil d'Ariane et ne montrent que ses données.
3. Le pied d'une carte ouvrable dit « Updated <date> » ; celui d'une carte en traitement dit que le traitement est en cours, avec son avancement sur la ligne.
4. Une adresse de tender dont la personne n'est pas membre n'ouvre rien : le serveur refuse et aucune donnée du tender n'est affichée.
Écart maquette : l'ouverture des tenders de démonstration non construits est bloquée par un message ; sans objet dans le produit.
Point ouvert : ouverture d'un tender en traitement depuis l'accueil (« Still processing — it will open when the models finish » dans la maquette) — reprise non décidée (JRN-001 → OPEN-05).

## Couverture
- Règles couvertes : JRN-001 → [US-HOME-01](#us-home-01--être-accueilli-et-orienté-dès-larrivée), [US-HOME-02](#us-home-02--reprendre-le-tender-en-cours), [US-HOME-03](#us-home-03--comprendre-comment-un-tender-traverse-srm), [US-HOME-04](#us-home-04--voir-la-liste-de-mes-tenders), [US-HOME-05](#us-home-05--lire-lavancement-dun-tender-sur-sa-ligne), [US-HOME-06](#us-home-06--ouvrir-un-tender-depuis-laccueil) (la partie « création en quatre étapes » : US-NEW) ; TYPE-T06 → [US-HOME-04](#us-home-04--voir-la-liste-de-mes-tenders) (le type de chaque tender est affiché ; la règle de recette elle-même s'applique par le champ « Variantes » de chaque story).
- Non couvertes, avec la raison : reprise d'un tender en traitement depuis l'accueil — point ouvert (JRN-001 → OPEN-05) ; DEC-115 (police de la marque) — pas de story, charte graphique (US-X).
