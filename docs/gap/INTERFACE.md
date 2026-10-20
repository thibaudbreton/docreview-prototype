# Écart d'interface — du 8 septembre au 10 octobre 2026

**Pour qui.** Le développeur qui refait le front du produit à partir de la maquette du 8 septembre 2026 (14 h 14). Ce document ne parle que de l'interface : ce qu'on voit à l'écran, et ce qui s'y passe quand on agit.

**Départ.** `5e7ae6b`, l'état de `main` le 8 septembre 2026 à 14 h 14.

**Arrivée.** `main` au 10 octobre 2026 (`f2568cb`). C'est tout ce que décrit [CODE.md](CODE.md), plus deux changements faits ensuite :
- l'alignement sur DEC-025 et DEC-012 (`3d779af`) ;
- le retour de la règle « au moins une organisation » (`0776cb0`).

> **Nom de l'outil.** Depuis le 19 octobre 2026, l'outil s'appelle « Smart Req ». Ce document décrit l'état au 10 octobre : partout où il cite « SRM » ou « Smart Requirement Manager » comme nom de l'outil (en-tête, titres de page, « How SRM works »…), lire « Smart Req ». Les identifiants d'exigence (SRM-00001…) ne changent pas.

> **Vocabulaire pas encore figé.** Les termes métier (système, sous-système, organisation (OBS), allocation, affectation…) sont en cours de validation. Les libellés cités ici sont ceux de la maquette au 10 octobre et peuvent encore changer : ne pas les graver en dur.

**Ce qui est dedans.** Quatre couches, pour chaque écran :
- les écrans et composants : ce qui apparaît, disparaît ou change de forme ;
- les textes et libellés, cités exactement, en anglais comme à l'écran ;
- les comportements visibles : ce qui se passe quand on agit, ce qui est actif, grisé ou en lecture seule, qui peut modifier quoi ;
- le style visuel : logo, couleurs, polices, icônes, jetons de design.

**Ce qui n'y est pas.** Le « back » du prototype : magasin de données du shell, build, persistance, contenu des données de démo, noms de fonctions, code retiré sans effet visible. Pour ces sujets :
- le code : [CODE.md](CODE.md) ;
- les règles métier : [SPECS.md](SPECS.md) ;
- le pourquoi de chaque décision : [DECISIONS.md](DECISIONS.md).

**Comment lire.**
- **Ordre.** Un chapitre par écran, dans l'ordre du parcours. Le socle commun (en-tête, charte, tableaux) vient d'abord, une fois pour tous les écrans.
- **Sections.** Chaque chapitre ouvre sur un « En bref », puis donne :
  - **Ajouté** ;
  - **Modifié** (avant → maintenant) ;
  - **Retiré** ;
  - **Libellés** ;
  - **Style visuel** ;
  - **Points incertains**.
- **Références.** La colonne **Réf.** donne la décision qui motive le changement (DEC-xxx), quand elle est connue ; « — » sinon.
- **Notations.** Dans les libellés, `{…}` marque une valeur variable (`{ID}`, `{nom}`, `{date}`), et N, M, K un nombre. Les noms entre parenthèses (Toast, Status Pill…) renvoient aux composants de [COMPONENTS.md](../../COMPONENTS.md).
- **Style.** Le style commun (logo, police, couleurs, trait rouge, icônes) est décrit une fois, dans le Socle commun. La section Style visuel d'un écran ne donne que ce qui lui est propre.
- **Démo.** Les contrôles de démo sont regroupés dans le dernier chapitre. Ils ne sont pas à reproduire.

**Méthode.** Les deux versions du code ont été comparées écran par écran. Seul ce qui se voit à l'écran a été retenu. Chaque point vient de la lecture du code des deux versions, et « (à vérifier) » signale ce qui n'a pas pu être confirmé entièrement. Les captures, prises sur les deux versions, montrent les principaux changements. Le reste n'a pas été revérifié à l'écran ligne par ligne.

## Sommaire

- [L'essentiel](#lessentiel)
- [Vue d'ensemble par écran](#vue-densemble-par-écran)
- [Captures avant / après](#captures-avant--après)
- [Socle commun — en-tête, charte, tableaux](#socle-commun--en-tête-charte-tableaux)
- [Accueil](#accueil)
- [Création d'un tender](#création-dun-tender)
- [Tableau de bord](#tableau-de-bord)
- [Statistiques](#statistiques)
- [Documents & versions](#documents--versions)
- [Allocation — page, tableau, vue Document, versions](#allocation--page-tableau-vue-document-versions)
- [Allocation — panneau de détail et modèle d'allocation](#allocation--panneau-de-détail-et-modèle-dallocation)
- [Compliance](#compliance)
- [Q&A](#qa)
- [Risks — nouvel écran](#risks--nouvel-écran)
- [Configuration](#configuration)
- [Team casting](#team-casting)
- [Contrôles de démo — à ne pas reproduire](#contrôles-de-démo--à-ne-pas-reproduire)

## L'essentiel

Les changements qui comptent le plus pour le front, tous écrans confondus. Le détail est dans les chapitres.

**Partout**
- **Marque.**
  - L'en-tête de chaque écran affiche le logo de l'entreprise puis « SRM » en texte ; la marque SRM ne sert plus que de favicon.
  - Accent marine, police de la marque, trait rouge devant les titres.
  - Icônes au trait à la place des emoji.
- **Vocabulaire.**
  - « activity » devient « system », et « expert » devient « contributor ».
  - « Requirements review » et « Follow-up » deviennent « Allocation » et « Compliance ».
  - Ces termes sont encore provisoires (voir l'encadré plus haut).
- **Cloche et fil d'Ariane.** La cloche ouvre une vraie liste sur le tableau de bord, Compliance, Documents et Q&A. Le fil d'Ariane nomme le tender ouvert.
- **Rôles.** Un contributeur lit tout le tender et ne modifie que son système : il n'y a plus de vue restreinte ni de passages caviardés. La nature et la classe d'une exigence sont réservées au chef de projet.

**Accueil et tableau de bord**
- **Accueil refondu.**
  - Ajoutés : un bandeau de bienvenue, la carte « Pick up where you left off », le bloc « How a tender travels through SRM ».
  - Les cartes de tender montrent une mini-ligne à quatre stations.
  - Retirés : l'indicateur de santé et le compte à rebours.
- **Plus de finalisation.** « Finalize allocation » disparaît. Une exigence part vers Compliance dès qu'on la valide, et la carte Allocation du tableau de bord passe à Done toute seule.
- **Statistiques refaites.** Trois onglets : « Project », « Allocation », « Compliance ». Chaque bloc s'ouvre sur une phrase calculée, et aucun chiffre n'est donné par personne.

**Allocation**
- **Une allocation = une organisation (OBS) + sa personne.**
  - Les champs « Manager » et « Expert » disparaissent.
  - Chaque organisation a un seul champ « Assigned to », limité aux membres du système.
  - Une personne manquante n'empêche plus de valider.
- **Chaîne ABS → PBS → OBS.**
  - L'OBS devient une liste d'organisations : on en ajoute par recherche, on en retire jusqu'à zéro.
  - Le PBS devient un élément produit.
  - « ↻ Re-run » rejoue un modèle d'allocation.
- **Une seule validation,** « Validate & send to Compliance ».
  - Elle est toujours affichée, et grisée avec sa raison quand elle ne peut pas servir.
  - Sur Turnkey, le chef de projet valide l'aiguillage, puis chaque système se valide dans son propre détail.
- **Versions par document.** Le mode « Compare » disparaît. À la place :
  - une colonne Changes, avec les différences mot à mot ;
  - un onglet Changes dans la vue Document ;
  - un onglet Versions dans le panneau.
- **Tableau.**
  - Colonnes personnalisées, partagées avec Compliance ; largeurs réglables.
  - TK OBS est fondu dans System. OBS et Compliance passent en lecture seule.
  - Nouveaux raccourcis : X, N, C, ⌘/Ctrl+Z…

**Compliance**
- **Panneau de décision du contributeur.** On y trouve sa file et le texte complet. Il choisit puis confirme son verdict, et dispose de « Ask the client » et de « Not mine — return it ».
- **Deux verdicts, plus de verrou.**
  - Après un Not compliant, on choisit une stratégie d'écart et un risque.
  - La conformité externe est calculée ; seul le chef de projet la corrige, avec un motif.
- **Même mécanique de tableau qu'Allocation :** ordre du document, tri par en-tête, filtres, colonnes, clavier, annulation. Disparaissent les retards, « outdated », « Needs my action » et la vue « By expert ».

**Q&A, Risks, Documents, réglages**
- **Q&A simplifié.**
  - Une liste à deux vues : « Our questions » et « Other bidders ».
  - Les statuts To send, Sent et Answered se marquent à la main.
  - « Answer to confirm » remplace l'arbitrage.
  - Retirés : l'export du lot, les doublons, l'exclusion.
- **Risks, nouvel écran,** en lecture seule. Les risques se créent dans Compliance.
- **Documents.** Une nouvelle version rouvre réellement les réponses des exigences qu'elle modifie (« answers reopened »).
- **Configuration.**
  - Nouvelles sections « Allocation model » et « Compliance » (stratégies d'écart).
  - La ligne produit, le produit et la langue passent en lecture seule.
  - « Restricted view » et le verrou de validation sont retirés.
- **Création et équipe.**
  - Création : quatre lignes produit (« RCS » devient « RSC » ; INFRA et Rolling Stock disparaissent). « Product » ou « Combination » remplace « System ».
  - Team casting : codes système, périmètres en liste fermée, manager facultatif, une personne = un système.

## Vue d'ensemble par écran

Nombre de lignes de chaque tableau du chapitre (un changement par ligne). Le style, les points incertains et les contrôles de démo ne sont pas comptés.

| Écran | Ajouté | Modifié | Retiré | Libellés |
|---|---|---|---|---|
| [Socle commun — en-tête, charte, tableaux](#socle-commun--en-tête-charte-tableaux) | 6 | 5 | 1 | 3 |
| [Accueil](#accueil) | 13 | 5 | 4 | 1 |
| [Création d'un tender](#création-dun-tender) | 4 | 7 | 1 | 9 |
| [Tableau de bord](#tableau-de-bord) | 10 | 19 | 6 | 2 |
| [Statistiques](#statistiques) | 19 | 3 | 7 | 0 |
| [Documents & versions](#documents--versions) | 3 | 1 | 0 | 7 |
| [Allocation — page, tableau, vue Document, versions](#allocation--page-tableau-vue-document-versions) | 43 | 41 | 14 | 13 |
| [Allocation — panneau de détail et modèle d'allocation](#allocation--panneau-de-détail-et-modèle-dallocation) | 26 | 40 | 12 | 15 |
| [Compliance](#compliance) | 62 | 37 | 12 | 12 |
| [Q&A](#qa) | 13 | 9 | 10 | 2 |
| [Risks — nouvel écran](#risks--nouvel-écran) | 22 | 0 | 0 | 0 |
| [Configuration](#configuration) | 20 | 6 | 7 | 17 |
| [Team casting](#team-casting) | 3 | 12 | 3 | 6 |

## Captures avant / après

Huit écrans, pris le 12 octobre 2026 sur les deux versions, sur le tender de démo STB-2026, côté chef de projet. Risks n'existe que dans la nouvelle version.

**Fichiers locaux, non versionnés.**
- `docs/gap/captures/` est dans `.gitignore` : les liens ne marchent que sur une copie locale, transmise à part.
- Sur les écrans d'Allocation, le texte réel des exigences, des documents et des sections est masqué par des barres grises. Les autres écrans montrent des données de démo.
- Pour les refaire : outillage local `deck/ui-gap/` (non versionné), avec le prototype servi sur le port 8934.

| Écran | Avant (8 sept.) | Maintenant (10 oct.) |
|---|---|---|
| Accueil | [01-accueil-avant.png](captures/01-accueil-avant.png) | [01-accueil-apres.png](captures/01-accueil-apres.png) |
| Tableau de bord | [02-tableau-de-bord-avant.png](captures/02-tableau-de-bord-avant.png) | [02-tableau-de-bord-apres.png](captures/02-tableau-de-bord-apres.png) |
| Allocation — tableau | [03-allocation-tableau-avant.png](captures/03-allocation-tableau-avant.png) | [03-allocation-tableau-apres.png](captures/03-allocation-tableau-apres.png) |
| Allocation — panneau ouvert sur une exigence à deux systèmes | [04-allocation-panneau-avant.png](captures/04-allocation-panneau-avant.png) | [04-allocation-panneau-apres.png](captures/04-allocation-panneau-apres.png) |
| Compliance — panneau ouvert sur une affectation | [05-compliance-avant.png](captures/05-compliance-avant.png) | [05-compliance-apres.png](captures/05-compliance-apres.png) |
| Q&A | [06-qa-avant.png](captures/06-qa-avant.png) | [06-qa-apres.png](captures/06-qa-apres.png) |
| Team casting | [07-equipe-avant.png](captures/07-equipe-avant.png) | [07-equipe-apres.png](captures/07-equipe-apres.png) |
| Configuration | [08-configuration-avant.png](captures/08-configuration-avant.png) | [08-configuration-apres.png](captures/08-configuration-apres.png) |
| Risks (nouvel écran) | — | [09-risks-apres.png](captures/09-risks-apres.png) |

## Socle commun — en-tête, charte, tableaux

Tous les écrans : en-tête, favicon, jetons de couleur, polices, icônes ; `build_merge.py`, `table-engine.js`, `components.css`.

**En bref.** Le shell n'affiche toujours rien par lui-même en dehors de l'onglet du navigateur : ni barre commune, ni sélecteur de tender, ni menu utilisateur (l'avatar reste de simples initiales) ; chaque écran dessine son propre en-tête. Partout, cet en-tête s'ouvre désormais sur le logo de l'entreprise suivi de « SRM » en texte, et la marque SRM, redessinée, ne sert plus que de favicon. La charte change d'un bout à l'autre : accent marine en thème clair, surfaces marine en thème sombre, police de la marque calée sur Noto Sans, petite barre rouge décorative devant les titres, icônes au trait à la place des emoji. La cloche s'ouvre sur quatre écrans de plus, le fil d'Ariane nomme le tender réellement ouvert, et un 8ᵉ écran, Risks, entre dans la navigation. Dans les tableaux d'Allocation et de Compliance, les colonnes se redimensionnent et le filtre avancé gère les colonnes à choix multiple ; le chat du tender existe dans le code mais reste désactivé.

### Ajouté

| Zone › élément | Ce qu'on voit, ce qui se passe | Réf. |
|---|---|---|
| En-tête de tous les écrans › logo de l'entreprise (Brand Logo) | Premier élément à gauche : le logo de l'entreprise, en couleur sur thème clair, en blanc sur thème sombre (15 px de haut), puis un filet vertical fin et « SRM » en texte gras. Infobulle « Alstom ». Le logo n'est pas cliquable ; « SRM » garde le lien qu'avait l'ancienne marque (vers l'accueil depuis le tableau de bord, vers le tableau de bord depuis les autres écrans d'un tender). | — |
| En-tête › liste de la cloche, sur Dashboard, Compliance, Documents et Q&A (Notifications Dropdown) | La cloche, inerte sur ces quatre écrans, ouvre une liste sous l'icône : titre « Notifications · N », une ligne par élément (pastille de couleur, texte, heure) qui mène à l'endroit concerné, ou « Nothing waiting on you here. » quand rien n'attend. Le contenu dépend de l'écran (voir chaque chapitre) ; un clic ailleurs referme la liste. Allocation garde sa liste propre, inchangée. | — |
| Navigation › écran Risks (route `#risks`) | Nouvel écran, le registre des risques du tender. On y arrive par la carte « Risks » du tableau de bord, par l'icône « Risks — the tender's risk register » de l'en-tête de Compliance et par les puces de risque de Compliance ; son en-tête renvoie à Compliance et aux paramètres, sans cloche. Contenu : chapitre Risks. | DEC-113 |
| Tableaux d'Allocation et de Compliance › poignée de redimensionnement (Column Resize Handle) | Sur le bord droit de chaque en-tête de colonne, sauf la case de sélection : invisible au repos, trait fin au survol de l'en-tête, trait couleur accent pendant le glissement. Glisser redimensionne, double-cliquer rend la largeur par défaut, ←/→ au clavier agit par pas de 16 px ; infobulle « Drag to resize · double-click to reset ». Largeurs gardées par tender et par tableau ; le bouton « Reset column widths » apparaît dans le panneau des colonnes dès qu'une largeur a été changée. | — |
| Filtre avancé d'Allocation et de Compliance › colonnes à choix multiple (Advanced Filter Builder) | Pour une colonne personnalisée à choix multiple, les opérateurs proposés sont « is any of », « is none of », « is empty » et « is not empty ». « is any of » retient une ligne qui porte au moins une des valeurs choisies. | DEC-066 |
| Toasts d'Allocation et de Compliance › annulation (Toast) | Le bouton « Undo » d'un toast porte l'infobulle « Undo (Ctrl/⌘ Z) » ; Compliance, qui n'en avait pas, gagne ce bouton. ⌘/Ctrl+Z (hors champ de saisie) annule la dernière action annulable même après la disparition du toast, avec le toast « Undone — {action} », ou « Nothing to undo » s'il n'y a plus rien. Détail : chapitres Allocation et Compliance. | DEC-085 |

### Modifié

| Zone › élément | Avant (8 sept.) | Maintenant | Réf. |
|---|---|---|---|
| Onglet du navigateur › favicon | Deux icônes selon le thème du système : la marque SRM à trois lobes translucides et point blanc, encre sombre ou blanche. | Une seule icône pour les deux thèmes, la marque SRM « Fan Ribbons » : tuile marine très sombre aux coins arrondis, rubans gris-bleu en éventail, un ruban corail. Le titre de l'onglet ne change pas (« Smart Requirement Manager — STB-2026 · Full app »). | — |
| En-tête › fil d'Ariane, nom du tender (Breadcrumb) | Seul le tableau de bord nommait le tender ouvert ; Allocation, Compliance, Documents et Q&A affichaient toujours « STB-2026 · … », même sur un autre tender. | Tous les écrans d'un tender affichent « {référence} · {nom} » du tender ouvert. | — |
| En-tête › point rouge de la cloche (Notification Dot) | Point rouge (`--warn`) toujours affiché sur Dashboard et Compliance, absent sur Documents et Q&A. | Présent sur les quatre écrans et masqué quand rien n'attend. Sur Compliance et Q&A il suit chaque mise à jour ; sur Dashboard et Documents il n'est recalculé qu'à l'ouverture de la cloche (à vérifier). | — |
| Tableaux d'Allocation et de Compliance › édition d'une cellule au clavier | Échap pouvait ne rien rétablir quand la fenêtre n'avait pas le focus système. | Échap rétablit toujours la valeur d'origine d'un champ texte de cellule ouvert au clavier. | — |
| Toasts de Documents et de Q&A (Toast) | Les messages de ces deux écrans n'apparaissaient pas (aucun style pour leur zone de toasts). | Même toast que sur les autres écrans, centré en bas de l'écran. | — |

### Retiré

| Zone › élément | Ce qui disparaît, et ce qui le remplace s'il y a lieu | Réf. |
|---|---|---|
| En-tête de tous les écrans › marque SRM (App Header) | Le dessin SRM à trois lobes (variantes claire et sombre) quitte tous les en-têtes. Il est remplacé par le logo de l'entreprise suivi de « SRM » en texte ; la marque SRM ne subsiste que comme favicon, redessinée. | — |

### Libellés

| Où | Avant | Maintenant |
|---|---|---|
| Tous les écrans, axe d'allocation (DEC-045) — occurrences dans chaque chapitre | « activity » / « Activity » | « system » / « System » (les « Activity » restants désignent le journal d'activité) |
| Tous les écrans, personne qui répond (DEC-030) | « expert » / « Expert » | « contributor » / « Contributor » |
| Tous les écrans, noms d'étapes (DEC-029) | « Requirements review », « Expert review », « Follow-up » | disparaissent au profit de « Allocation » et « Compliance » |

### Style visuel

- **Thème clair, thème par défaut du prototype** : `--accent` #0050E3 → #0B294A (marine de la marque), `--accent-soft` #E9EFFD → #E6EBF2 (DEC-063). Boutons principaux, onglets actifs, sélections, bordures au focus et liens passent du bleu vif au marine ; le survol (`--accent-hover`, hors échelle, toujours dérivé de `--accent`) devient un marine éclairci. Les liens texte ont presque la couleur du texte courant (#1E3246) et ne se distinguent plus que par leur place et le survol.
- **Thème sombre** : les surfaces passent sur la famille marine — `--bg` #141F2B → #071A30, `--panel` #1E3246 → #0B294A, `--line` #2C3E52 → #1F3E5F, `--accent-soft` #1E3A63 → #1B3F6B ; hors échelle suivie : `--panel-2` #26374C → #143556, `--panel-3` #2F4257 → #1D4062, `--line-2` #3A4E66 → #2E4E70. `--accent` reste #4C82FF. Textes et couleurs d'état (`--ok`, `--warn`, `--ia`, `--human`) ne changent dans aucun thème.
- **Nouveaux jetons de l'échelle suivie** : `--font-heading` et `--brand-red` (#E4002B, valeur provisoire, définie une seule fois et donc identique dans les deux thèmes).
- **Nouveaux jetons hors échelle** : `--brand-blue` (#5B8CF5 sombre / #2F6BD8 clair), `--brand-blue-soft` (#1A3560 / #E3ECFA) et `--brand-slate` (#5F7A99 / #4F6A88), sur l'accueil et le tableau de bord seulement ; `--partner` #1b9aaa et `--partner-soft` (sarcelle des partenaires externes) sur Allocation, Compliance et le tableau de bord, sans valeur propre au thème clair.
- **Police de l'interface** : `--font-ui` passe de « Inter », que les écrans ne chargeaient pas (police du système si Inter n'est pas installée), à « Alstom UI », la police de la marque, avec Noto Sans en repli chargée depuis Google Fonts (graisses 400 à 700). Les deux sont calées sur les mêmes métriques : mise en page identique (DEC-115). La version publiée du prototype affiche Noto Sans (licence non réglée) ; seule la version locale montre la police de la marque. Le demi-gras (600) est dessiné avec le Medium, l'extra-gras (800) avec le Bold.
- **Identifiants et codes** : `--font-mono` commence par « Alstom UI » (chiffres de même largeur), puis la pile monospace du système : police de la marque en local, monospace système dans la version publiée, comme avant. Le texte du document source reste en Georgia (`--font-doc`).
- **Titres** : h1, h2, h3 et quelques titres de section (panneaux de configuration, menus) prennent `--font-heading` (Antarctica, puis Alstom UI, puis Noto Sans). Antarctica n'est pas fourni : les titres s'affichent aujourd'hui dans la police de l'interface (DEC-063).
- **Marque rouge** : chaque h1 et h2 est précédé d'une barre verticale rouge de 5 px (`--brand-red`, hauteur 0,85 em), purement décorative. Le rouge n'est jamais posé sur un élément cliquable ou porteur d'état (DEC-063) (Page Title).
- **Icônes** : un seul jeu d'icônes au trait (grille 24 px, trait 2 px, couleur et taille du texte, 33 icônes) remplace dans les 8 écrans les emoji (📄 🔒 🔔 📷 🗑 🎭 🕐 💬 🌐 📎 ⏳) et les symboles absents de la police (⇗ ⎘ ⌕ ⑂ ◷ ⇲ ⏷ ▤ ▸ ▶ ⤵ ⬆ ⬇). Les flèches simples et ✓ ✕ ⚠ ✎ ↻ ↺ ▾ restent du texte (Icon).
- **Pastilles de statut** d'Allocation, de Compliance et de Documents : plus de point coloré devant le libellé, la couleur de la pastille suffit.
- **Composants partagés** : le fichier des composants communs (listes, listes déroulantes, champs texte) est désormais chargé aussi par Compliance ; ses nouvelles listes déroulantes et ses champs texte ont exactement le dessin de ceux d'Allocation. Aucun composant commun n'a changé d'aspect.
- **En-tête** : hauteur (52 px), fond (`--panel`) et avatar (initiales sur dégradé orange, sans menu) inchangés.

### Points incertains

- Point rouge de la cloche sur Dashboard et Documents : d'après le code, il reste visible au chargement tant que la cloche n'a pas été ouverte, même si rien n'attend ; non vérifié à l'exécution.
- Valeurs de charte encore provisoires : rouge exact de la marque, fichiers Antarctica, licence de diffusion de la police de la marque (DEC-063, DEC-115).
- Liens texte en thème clair : presque de la couleur du texte depuis le passage de l'accent au marine ; un second accent réservé aux liens a été évoqué par l'auteur, sans décision.

## Accueil

`accueil.html` · route `#home` · captures : [avant](captures/01-accueil-avant.png), [maintenant](captures/01-accueil-apres.png)

**En bref.** L'accueil n'est plus une simple grille : il s'ouvre sur un bandeau de bienvenue (salutation, rôles de l'utilisateur, « ＋ New tender », « How SRM works » et une carte « Pick up where you left off » pour reprendre le tender en cours), puis un bloc masquable qui explique les quatre étapes d'un tender, puis la liste « My tenders ». Chaque carte de tender est refaite : badge de ligne produit, référence, puce de rôle à deux valeurs (« Project manager » / « Contributor »), nom, puis une mini-ligne à quatre stations (Capture, Allocation, Compliance, Submission) qui remplace la pastille d'étape et les barres de progression. Disparaissent : l'indicateur de santé (« On track »…), le compte à rebours (« N days left ») et le sous-titre « you lead as Bid Director ». Les onglets et l'ouverture d'un tender au clic ne changent pas ; l'en-tête ne change que par son logo (voir Socle commun).

### Ajouté

| Zone › élément | Ce qu'on voit, ce qui se passe | Réf. |
|---|---|---|
| Bandeau d'accueil › cadre (Home Hero) | Bloc encadré aux coins arrondis en tête de page, fond en dégradé du panneau vers un bleu pâle (bleu sombre en thème sombre) ; texte à gauche, carte de reprise à droite. Un dessin de lignes de métro (une ligne couleur d'accent, une bleue, une rouge, une correspondance) occupe le coin bas droit, purement décoratif. | — |
| Bandeau › surtitre et salutation (Page Title) | Surtitre en capitales, en bleu, « Smart Requirement Manager », puis le titre de la page : « Good morning, {prénom} », « Good afternoon, {prénom} » ou « Good evening, {prénom} » selon l'heure locale (avant midi, avant 18 h, ensuite), le prénom en bleu. « Welcome » s'affiche le temps du calcul. | — |
| Bandeau › phrase d'objet | « Every requirement of a tender — captured from its documents, routed to the team that answers it, and declared to the client — in one place. » | — |
| Bandeau › ligne des rôles | « You lead N tender(s) as project manager and contribute to M. », comptée sur le rôle de l'utilisateur dans chaque tender ; la fin « and contribute to M » disparaît si M = 0. Sans aucun tender : « No tender yet — create the first one, or ask a project manager to add you to theirs. » | — |
| Bandeau › bouton « How SRM works » | Bouton secondaire juste après « ＋ New tender ». Il réaffiche le bloc « How a tender travels through SRM » s'il avait été masqué et fait défiler la page jusqu'à lui. | — |
| Bandeau › carte « Pick up where you left off » (Continue Card) | Carte à droite, liseré dégradé accent → bleu en haut : surtitre « Pick up where you left off », nom du tender, « {référence} · updated {quand} », sa mini-ligne, l'étape suivante (« N requirement(s) still to allocate », puis, une fois tout alloué, « N requirement(s) still to answer in Compliance ») et le bouton « Continue → ». Toute la carte est cliquable (infobulle « Open {nom} ») et ouvre le tender comme une carte de la liste. Absente s'il n'y a aucun tender ouvert (ni en traitement, ni soumis). | — |
| Bloc « How a tender travels through SRM » › en-tête (Onboarding Line, Home Section Head) | Sous le bandeau, sans cadre : titre « How a tender travels through SRM » avec une marque rouge, indice « four stations, the same for every tender » et, à droite, « Got it — hide ». Ce bouton masque le bloc, qui reste masqué en naviguant pendant la session ; « How SRM works » le fait revenir. | — |
| Bloc › station 1 « Capture » | Première station numérotée sur une ligne horizontale : « The AI reads the tender's documents and captures every requirement, table row and figure. You check what it found. » ; étiquette de rôle « Project manager ». | — |
| Bloc › station 2 « Allocation » | « Each requirement gets its nature, class and systems, then the organisation (OBS) and the person who will answer it. » ; étiquette « Project manager, then each system ». | — |
| Bloc › station 3 « Compliance » | « Each contributor gives a verdict. A Not compliant gets a gap strategy and a risk; the verdicts consolidate per requirement. » ; étiquette « Contributors », en bleu (les autres étiquettes sont dans la couleur d'accent). | — |
| Bloc › station 4 « Submission » | « Export to DOORS or Excel, and hand the client the compliance matrix. » ; étiquette « Project manager ». | — |
| Bloc › pied | « Always open alongside: Documents & versions · Q&A with the client · Risks · Team casting ». Simple texte : aucun de ces noms n'est un lien. | — |
| Carte de tender › mini-ligne (Tender Line, variante mini) | Sous le nom : quatre stations « Capture », « Allocation », « Compliance », « Submission » reliées par un trait qui se remplit avec l'avancement ; stations passées pleines, station en cours cerclée et nommée en gras avec son compte (« Capture N% » en traitement, « Allocation {alloués}/{total} », « Compliance {remplis}/{total} » dès que tout est alloué, « Submission ✓ » une fois soumis). Infobulle : l'étape de traitement en cours, ou « Response submitted · N requirements ». | — |

### Modifié

| Zone › élément | Avant (8 sept.) | Maintenant | Réf. |
|---|---|---|---|
| Bandeau › bouton « ＋ New tender » | À droite du titre « My tenders ». | Dans le bandeau, sous la ligne des rôles, suivi de « How SRM works ». Le bouton identique de l'en-tête ne bouge pas. | — |
| Page › titre « My tenders » (Home Section Head) | Titre de page « My tenders » tout en haut, sous-titre « N tenders · you lead as Bid Director », bouton « ＋ New tender » à droite. | Titre de section « My tenders » placé sous le bloc d'explication, précédé de la marque rouge, avec l'indice « N tenders » ; le titre de la page est désormais la salutation. | — |
| Carte de tender › ligne produit (Product Line Badge) | Texte gras dans la ligne d'informations sous le nom (« Turnkey », « SIG »…). | Badge en capitales en haut à gauche, avant la référence : couleur d'accent pour Turnkey (marine en thème clair), bleu pour SIG, ardoise pour les autres lignes ; infobulle « Product line ». | — |
| Carte de tender › rôle (Role Chip) | Pastille neutre reprenant le rôle tel qu'enregistré (« Project manager », « Signalling manager », « Expert »…), dans la ligne d'informations. | Puce en haut à droite, deux valeurs seulement : « Project manager » (icône drapeau, couleur d'accent avec contour) ou « Contributor » (icône personnes, bleu) pour tout autre rôle. Infobulle inchangée « Your role on this tender ». | DEC-030 |
| Carte de tender › pied d'un tender en traitement | « Opens when processing completes », en gris. | Point bleu clignotant puis « Processing — opens when it completes », en bleu et en gras. | — |

### Retiré

| Zone › élément | Ce qui disparaît, et ce qui le remplace s'il y a lieu | Réf. |
|---|---|---|
| Carte de tender › pastille d'étape (Status Badge / Chip) | La pastille colorée en haut à droite (« Processing » clignotante, « Allocation », « Expert review », « Q&A & Versioning », « Submitted ») disparaît ; l'étape se lit sur la mini-ligne. | — |
| Carte de tender › indicateur de santé (Status Dot) | La ligne « On track », « At risk » ou « Behind » suivie d'un commentaire, avec son point vert, orange ou rouge, disparaît sans remplacement. | — |
| Carte de tender › échéance (Deadline Chip) | « N days left » (orange à 25 jours ou moins, rouge à 10 ou moins) ou « overdue » disparaît : l'accueil n'affiche plus ni date ni compte à rebours. | — |
| Carte de tender › barres de progression (Progress Bar) | La ligne « N/T validated », « N/T answered » ou « N/T resolved » avec sa barre verte, la barre de traitement avec son libellé et « N% », et la ligne « Response submitted · N requirements » disparaissent. La mini-ligne les remplace ; l'étape de traitement et « Response submitted… » passent en infobulle. | — |

### Libellés

| Où | Avant | Maintenant |
|---|---|---|
| Carte d'un tender en traitement › libellé de la dernière étape de traitement (avant dans la carte, maintenant en infobulle de la mini-ligne) — DEC-030 | « Allocating to experts… » | « Allocating to contributors… » |

### Style visuel

- En-tête : logo de l'entreprise, filet, puis « SRM » (voir Socle commun) ; « ↺ Reset demo », « ＋ New tender » et l'avatar ne changent pas.
- Largeur maximale du contenu : 1 120 → 1 180 px.
- Salutation (titre de page) à 32 px, au-dessus de l'échelle typographique (l'ancien titre était à `--text-xl`, 21 px), précédée de la barre rouge de 5 px ; titres de section à `--text-lg` précédés d'une barre rouge de 4 px. Ces marques sont décoratives (DEC-063).
- Couleurs propres à l'accueil, hors échelle suivie : `--brand-blue` (surtitre, prénom, puce « Contributor », badge SIG, pied « Processing… », début de la ligne d'explication), `--brand-blue-soft` (fond des puces contributeur, fin du dégradé du bandeau), `--brand-slate` (badge des lignes autres que Turnkey et SIG).
- Code couleur des rôles commun aux puces des cartes et aux étiquettes du bloc d'explication : chef de projet dans la couleur d'accent (`--accent`, marine en thème clair), contributeur en bleu (`--brand-blue`).
- Bloc d'explication : ligne horizontale en dégradé bleu → accent, stations numérotées de 30 px dont la couleur glisse du bleu vers l'accent.
- Carte de reprise : ombre portée légère, bordure accent et léger soulèvement au survol, comme les cartes de tender.
- Nom du tender dans la police des titres et en gras (avant : police de l'interface, demi-gras).
- Fenêtre de moins de 1 220 px de large : la carte de reprise passe sous la salutation (460 px au plus) et le dessin de métro rétrécit (440 px) dans le coin libre.

### Points incertains

- Règle de choix du tender de la carte de reprise dans le produit (dernier ouvert ? dernier modifié ?) : non définie ; la maquette s'appuie sur un marqueur de démo.
- Rôle affiché sur la carte et compté dans la ligne des rôles : déduit d'un texte libre (tout rôle qui ne contient pas « project manager » devient « Contributor ») ; dans le produit, il devrait venir de l'équipe du tender (à vérifier).
- Carte de reprise : ni la carte ni son bouton « Continue → » ne prennent le focus clavier (à vérifier si c'est voulu).
- Bloc d'explication masqué : mémorisé pour la session seulement dans la maquette ; persistance par utilisateur dans le produit à décider (à vérifier).

## Création d'un tender

`creation-projet.html` · route `#new` (assistant en quatre étapes)

**En bref.** L'assistant garde ses quatre étapes (identité, documents, mode de traitement, équipe de direction), son récapitulatif et sa fin de parcours. L'étape 1 change le plus : quatre lignes produit au lieu de six (« RCS » devient « RSC », « INFRA » et « Rolling Stock » disparaissent), et le champ « System » laisse place à « Product » — une vraie liste pour SIG (Urban, Mainline Wayside, Mainline Onboard), un champ désactivé avec une note « Placeholder » pour RSC et Services — ou à « Combination », désactivé, sur un Turnkey. Le produit choisi est désormais conservé sur le tender créé. L'étape 3 annonce que le mode de traitement est figé à la création ; les cartes de document affichent la langue source choisie ; la recherche d'un chef de projet s'ouvre enfin en vraie liste déroulante ; tous les textes passent au vocabulaire « system » et aux noms d'écrans actuels.

### Ajouté

| Zone › élément | Ce qu'on voit, ce qui se passe | Réf. |
|---|---|---|
| Étape 1 › champ « Product », ligne SIG (Form Field Row) | Sous « Product line », une liste active « Urban », « Mainline Wayside », « Mainline Onboard », « Urban » présélectionné. Aide : « Selects the allocation model. Fixed at creation — it describes what the tender is. » (« is » en italique). | DEC-047, DEC-049, DEC-061 |
| Étape 1 › note sous « Product », ligne SIG | Mainline Wayside ou Onboard : « Derives ABS, PBS and OBS from the {produit} keys. Changeable later as a model setting, never as the tender's product. » Urban : « Selects the Urban allocation model. Not on the PBS/OBS/ABS keys — those cover the two Mainline products so far. » La note suit le produit choisi. | DEC-061, DEC-062 |
| Étape 1 › champ « Combination », ligne Turnkey | Le même champ s'intitule « Combination », aide « A Turnkey has no product of its own — it carries a combination of several systems' products. » La liste est désactivée et n'affiche que « — Not available — », avec la note « Placeholder. The matrix saying what each combination contains has not been supplied (DEC-048), so there is nothing truthful to offer here yet. » | DEC-048, DEC-049 |
| Étape 1 › champ « Product », lignes RSC et Services | Champ « Product » désactivé, avec la même aide que pour SIG, n'affichant que « — Not available — », et la note « Placeholder. {ligne}'s products have not been supplied. Only SIG's are known, from the PBS/OBS/ABS keys. » | DEC-047 |

### Modifié

| Zone › élément | Avant (8 sept.) | Maintenant | Réf. |
|---|---|---|---|
| Étape 1 › sélecteur « Product line » | Six choix : « Turnkey », « RCS », « SIG », « INFRA », « Rolling Stock », « Services ». | Quatre choix : « Turnkey », « RSC », « SIG », « Services » ; Turnkey reste présélectionné. | DEC-004, DEC-059 |
| Étape 1 › note sous « Product line » | Turnkey : « Allocation resolves to an activity, split further by technical/non-technical classification. » Toute autre ligne : « Allocation resolves to a person. » | Turnkey : « Routes to systems; each derives its ABS / PBS / OBS and person. » SIG : « Derives ABS, PBS and OBS, then the person for each OBS. » RSC et Services : « No model supplied yet — allocated by hand. » | DEC-044, DEC-045 |
| Étape 2 › cartes de document (Document / File Card) | Chaque document ajouté indiquait « … pages · … MB · English », quelle que soit la langue source. | La carte indique la langue source choisie à l'étape 1 (« French », « German »…), mise à jour si l'on revient la changer. | DEC-096 |
| Étape 3 › sous-titre de « Processing mode » | « How much of the initial work the AI does. Nothing here is irreversible: the AI never overwrites a manual correction, and you can re-run any step later. » | « How much of the initial work the AI does. This mode is fixed once the tender is created. The AI never overwrites a manual correction. » | DEC-095 |
| Étape 4 › recherche d'un chef de projet (Search-to-Add Combobox) | Les résultats de « Search a person via SSO to add another project manager… » s'affichaient dans le flux de la page, sans cadre, et restaient affichés après un clic ailleurs. | Liste déroulante flottante sous le champ (cadre, ombre, défilement au-delà de 260 px), cachée tant que le champ est vide, refermée au clic ailleurs ou après un ajout ; « No match in the directory. » si rien ne correspond. | — |
| Étape 4 › « Summary », ligne « System » (Key-Value Summary Row) | « System » avec la valeur choisie à l'étape 1 (« Mainline » par défaut). | « Combination » sur un Turnkey, « Product » sinon ; valeur = produit choisi, ou « Not set » (toujours le cas sur Turnkey, RSC et Services). | DEC-049 |
| Fin de l'assistant › tender créé | Le produit saisi n'était pas transmis au tender. | Le tender créé garde son produit : pour un tender SIG Mainline Wayside ou Mainline Onboard, Allocation propose ensuite les listes ABS, PBS et OBS de ce produit (voir chapitres Allocation). Destinations inchangées : Allocation en mode manuel, sinon la fenêtre « Project created » puis le tableau de bord. | DEC-049 |

### Retiré

| Zone › élément | Ce qui disparaît, et ce qui le remplace s'il y a lieu | Réf. |
|---|---|---|
| Étape 1 › champ « System » (Form Field Row) | La liste « Mainline », « Urban / Metro », « Tramway », « Monorail », « Multiple systems » et son aide « The system concerned by the tender. » disparaissent ; remplacées par « Product » ou « Combination » selon la ligne produit. | DEC-049 |

### Libellés

| Où | Avant | Maintenant |
|---|---|---|
| Étape 1 › sous-titre | « Basic identity of the tender. The deadline drives the countdown and the overdue thresholds later on. » | « Basic identity of the tender. The deadline drives the countdown to submission. » |
| Étape 2 › sous-titre, dernière phrase | « Later versions are added from the Versions screen. » | « Later versions of each document are added in Documents & versions. » |
| Étape 2 › encadré d'avertissement | « You can create the project without documents and add them later, but the review screen stays empty until at least one source document is attached. » | « You can create the project without documents and add them later, but Allocation stays empty until at least one source document is attached. » |
| Étape 3 › « Characterisation », description quand l'étape est active (DEC-120) | « Proposes a type and domain for each block, and whether it is a requirement. » | « Proposes each block's nature and a requirement's class (technical / non-technical), with a Low / Medium / High confidence. » |
| Étape 3 › « Allocation », description quand l'étape est active | « Proposes which activity each requirement needs, based on its characterization. » | « On a Turnkey tender, routes each requirement to its system(s); on a single-system tender, derives its ABS, PBS and OBS. » |
| Étape 3 › « Allocation », description quand l'étape est désactivée | « Off — you assign the activity yourself, for every requirement. » | « Off — you assign the system yourself, for every requirement. » |
| Étape 3 › encadré « Manual mode. » | « The review screen opens with the document but no blocks. Use Edit segmentation… » | « Allocation opens with the document but no blocks. Use Edit segmentation… » |
| Étape 4 › sous-titre | « You're the first member automatically — whole-project scope, no activity restriction. Add others now if you already know who they are, or leave it and do it later from the Casting screen. » | « You're the first member automatically — whole-project scope, no system restriction. Add others now if you already know who they are, or leave it and do it later from Team casting. » |
| Étape 4 › « Summary », valeur de « Processing mode » en mode personnalisé | « Custom — {codes} », par exemple « Custom — seg, char » (codes internes des étapes activées) | « Custom — {étapes} », par exemple « Custom — Capture, Characterisation » |

### Style visuel

- En-tête : logo de l'entreprise, filet, puis « SRM » (voir Socle commun) ; « / New project » et « Cancel » ne changent pas.
- Titre du panneau des étapes « Create a tender project » : police des titres et barre rouge de 5 px ; les titres d'étape (« Project identity », « Source documents »…) ne changent pas.
- Icônes : la flèche ⬆ des zones de dépôt (« Drop tender documents here », « Drop another document here ») et le ◷ de l'estimation de traitement deviennent les icônes au trait « upload » et « clock ».
- Thème clair : ligne produit sélectionnée, carte de mode choisie, interrupteurs et bouton « Continue → » passent du bleu vif au marine (`--accent`), comme partout.
- Champ « Product » ou « Combination » désactivé : aspect désactivé par défaut du navigateur, sans style dédié.

### Points incertains

- Turnkey : « Combination » reste vide et le récapitulatif affiche « Not set » sans bloquer la création, en attendant la matrice des combinaisons (DEC-048) ; le comportement une fois la matrice fournie reste à définir.
- « Services » est toujours proposé alors que DEC-004 ne retient que Turnkey, SIG, Mainline et RSC (écart relevé dans DECISIONS.md, non tranché).
- Les notes « Placeholder » montrent une référence de décision (« (DEC-048) ») dans le texte lu par l'utilisateur : sans doute à ne pas reprendre telle quelle (à vérifier).
- SIG : « Urban » est présélectionné sans choix explicite de l'utilisateur (à vérifier si le produit doit être choisi activement).

## Tableau de bord

`dashboard-et-config.html` · route `#dashboard` · captures : [avant](captures/02-tableau-de-bord-avant.png), [maintenant](captures/02-tableau-de-bord-apres.png)

**En bref.** Le tableau de bord suit maintenant le tender réellement ouvert (titre, ligne, produit, volume, jours restants) et ne dépend plus d'aucune « finalisation » : la carte Allocation passe seule à Done quand tout est alloué, et tout ce qui touche Compliance est visible dès le premier jour. La cloche fonctionne enfin, le rail « Always open » gagne une carte Risks, et une carte des demandes de réaffectation en attente apparaît quand il y en a. La colonne de droite est refaite : « Recent comments » et « Answers by system » remplacent l'état de santé du projet, la barre de conformité et la liste nominative des experts. L'en-tête (logo de l'entreprise, puis « SRM » en texte) est décrit dans le Socle commun.

### Ajouté

| Zone › élément | Ce qu'on voit, ce qui se passe | Réf. |
|---|---|---|
| En-tête › cloche « Notifications » › menu déroulant (Notifications Dropdown, Notification Item) | Un clic sur la cloche ouvre un menu « Notifications · N », recalculé à chaque ouverture. Chaque ligne (point de couleur, texte, nom de l'écran en gris) ferme le menu et ouvre cet écran ; un clic ailleurs ferme le menu. Sans rien à signaler : « Nothing waiting on you here. » | — |
| En-tête › cloche › lignes possibles | « N requirements waiting to be reviewed in Allocation » et « N weak OBS derivations to check » (→ Allocation), « N assignments past the overdue threshold » (→ Compliance), « {document} {version} arrived — gap analysis ready » (→ Documents & versions, seulement après le dépôt d'une nouvelle version sur ce tender). Singulier quand N = 1. | — |
| Bandeau du tender › « N requirements » | Nouvel élément de la ligne d'identité, avant « Bid Director: … » : le nombre total d'exigences du tender. | — |
| Process › carte Allocation › description (Phase Card) | Ligne grise sous le titre : « Route each requirement to the system and team responsible for answering it. » Le code la signale comme texte provisoire. | — |
| Process › carte Compliance › description (Phase Card) | « Record whether each requirement is met, and declare the result to the client. » (provisoire aussi). | — |
| Always open › carte « Risks » (Phase Card, variante support) | Troisième carte du rail, icône « ! », chiffre « N in the list » (nombre de risques du tender). Clic → page Risks. Infobulle : « Risks — the tender's risk register, fed from Compliance. » | DEC-113 |
| Always open › infobulles des cartes | Chaque carte porte sa description en infobulle : « Team casting — staff each system, with or without a manager. », « Documents & versions — upload tender documents and track what changed between versions. », « Q&A — ask the issuer questions and track their answers. » | — |
| Carte « Pending reassignment requests » (sous le rail Always open) | N'apparaît que s'il existe des demandes de réaffectation en attente ; compteur rouge dans le titre. Jusqu'à 5 lignes « {id} — reassignment requested », sous-ligne « {nom}: "{note}" » (90 caractères). « Review → » au survol, clic → Allocation. | — |
| Colonne de droite › « Recent comments » (Activity Feed Item) | Les 6 éléments les plus récents : demandes de réaffectation de la session (« {nom} requested a reassignment on {id} — "{note}" », datées « Today », point ambre), puis commentaires, questions au client et liens de risque. Vide : « No comments yet. » | — |
| Colonne de droite › « Answers by system » (Experts Summary Panel, Compact Expert Line) | Les trois systèmes qui ont le plus d'affectations : code dans une pastille, barre verte (ambre en cas de retard), « répondues/confiées » ou « N late » en rouge. Sur un tender SIG : « Answers by sub-system », une ligne par sous-système. | DEC-118 |

### Modifié

| Zone › élément | Avant (8 sept.) | Maintenant | Réf. |
|---|---|---|---|
| En-tête › cloche (Notification Dot) | Bouton sans effet ; point rouge toujours affiché. | Ouvre le menu décrit dans Ajouté ; le point rouge, plus petit, n'apparaît que s'il y a au moins une ligne. | — |
| Bandeau du tender › identité | Sur STB-2026 (seul tender construit), titre, BO-ID et ligne écrits en dur (la ligne affichait « SIG » sur un tender Turnkey). Recalculés seulement pour les tenders non construits, dont ceux créés dans l'assistant. | Toujours lus sur le tender ouvert : titre, BO-ID, ligne. | — |
| Bandeau › ligne et produit | Une sous-ligne grise (« Multi-site EMS » en dur sur STB-2026, sinon le système ou à défaut la ligne du tender), puis la ligne en gras. | La ligne en gras d'abord, puis le produit du tender (ex. « Mainline Wayside »), masqué s'il n'y en a pas ou s'il égale la ligne. | — |
| Bandeau › « days to submission » | « 23 » fixe. | Les jours restants du tender ouvert. | — |
| Process › carte Allocation › chiffre | « N / 14 requirements validated », compté sur la copie locale des données du tableau de bord. | « N / M requirements allocated », lu sur la progression que publie l'écran Allocation dès qu'il a été ouvert (copie locale sinon). | DEC-098 |
| Process › carte Allocation › état Done | Seulement après « Finalize allocation » : badge « Done », « 14 / 14 validated · finalized », barre verte. | Automatique quand toutes les exigences sont allouées : badge « Done », « N / N allocated · done », barre verte. Sinon « Current ». | DEC-098, DEC-084 |
| Process › étape mise en avant | Allocation jusqu'à la finalisation, Compliance ensuite. | Allocation tant qu'une exigence n'est pas allouée, Compliance ensuite. | DEC-098 |
| Always open › disposition (Support Rail) | 3 cartes sur 3 colonnes (2 sous 1000 px) ; nom, chiffre et, pour Team casting, une barre. | 4 cartes (Team casting, Documents & versions, Risks, Q&A) sur 4 colonnes, 2 sous 1000 px, 1 sous 620 px. Nom puis chiffre sur deux lignes tronquées, sans barre. | — |
| Always open › carte Team casting (Phase Card) | « N / 7 activities fully staffed » (tous les périmètres pourvus ; une activité sans manager ne comptait jamais), barre verte, badge « K pending » ou « Complete ». | « N / M staffed » : systèmes où au moins une personne est staffée, avec ou sans manager. Badge « K pending » ou « Complete » (bordure verte), sans barre. | DEC-124 |
| Always open › carte Team casting › mise à jour | Calculée au chargement seulement. | Recalculée au retour de Team casting, comme « The team » et « By system, with who is on it » des statistiques. | DEC-124 |
| Always open › cartes Documents & versions et Q&A | Badge « Open » sur chacune. | Plus de badge, seulement la flèche. | — |
| What needs you now › élément Allocation (Attention List Item) | « Allocation not finalized » / « N requirements still to validate » / « Finalize allocation → ». | « Requirements still to validate » / « N requirements still to validate » / « Open Allocation → ». Masqué quand tout est alloué. | DEC-084, DEC-098 |
| What needs you now › éléments liés à Compliance | Retard de réponse, questions et non-conformité masqués tant qu'Allocation n'était pas finalisée. | Visibles dès le départ, chacun selon sa propre condition (masqué s'il n'y a rien). | DEC-035 |
| What needs you now › nouvelle version | « New version v2.2 ready for review » / « Arrived during allocation · +2 ~1 −0 · SRM-00009 response now on an outdated version », après la simulation v2.2. | « {document} {version} ready for review » / « +a ~m −r · N answers reopened in Compliance » (ou « no answer reopened »), après le dépôt d'une nouvelle version dans Documents & versions sur ce tender. | DEC-122 |
| What needs you now › questions au client | « 2 questions awaiting internal review » / « A possible duplicate was detected ({sujet}) — merge before sending », vers Compliance. | « 2 questions to send » / « Mark them as sent once they're out », vers l'écran Q&A. Chiffre figé dans le prototype. | DEC-116 |
| What needs you now › non-conformité | « 1 non-compliant requirement » / « SRM-00007 — {sujet} (Infrastructure) », écrits en dur. | « N Not compliant verdicts » / « K not linked to a risk yet · J without a gap strategy » (ou « All documented — strategy and risk on each »), d'après les totaux de Compliance ; masqué à zéro. Sans totaux : « N non-compliant requirements » / « {id} — internal verdict Not compliant ». | — |
| Recent activity › entrées de version (Activity Feed Panel) | « Version v2.2 uploaded and processed — gap analysis ready (+2 ~1 −0) » et « SRM-00009 flagged as answered on outdated version after v2.2 », « Today, 10:46 AM », après la simulation v2.2. | « {document} {version} uploaded — gap analysis ready (+a ~m −r) » et « N answers reopened by the new version — {ids} » (retirée si rien n'est rouvert), datées « Today », après un dépôt réel sur ce tender. | DEC-122 |
| Recent activity › dernière réponse | « {nom} responded on SRM-00013 — verdict Needs clarification ». | « {id} answered — internal verdict Compliant » (ou « Not compliant »), généré. | — |
| Recent activity › envoi au client | « Q&A batch — 1 question sent to the issuer ({sujet}) ». | « QA-01 marked as sent ». | DEC-116 |

### Retiré

| Zone › élément | Ce qui disparaît, et ce qui le remplace s'il y a lieu | Réf. |
|---|---|---|
| Colonne de droite › « Project health » (Project Health Panel) | Quatre chiffres : « Requirements », « Managers assigned » (100 %), « Validated » N/14 avant finalisation, « Response rate » après. Le volume passe dans le bandeau ; « Recent comments » prend la place. | — |
| Colonne de droite › « Compliance » (Compliance Summary Panel) | Barre « Compliant » / « Partial » / « Non-compliant » / « Awaiting » et sa légende, affichée après finalisation. Pas de remplacement dans la colonne : voir Statistics › Compliance. | — |
| Colonne de droite › « Experts » | Trois personnes (avatar, nom, équipe, barre, « 3/4 » ou « 2 late »), affichées après finalisation. Remplacée par « Answers by system ». | DEC-118 |
| Colonne de droite › note de verrouillage | « Compliance, experts and response tracking appear here once allocation is finalized. » Plus rien n'attend la finalisation. | DEC-035 |
| Recent activity › jalon | « Allocation milestone reached — register exported, 3 experts notified ». Il n'y a plus de jalon d'allocation. | DEC-084 |
| Recent activity › lien « View all » | Lien inactif dans le titre de la carte, sans remplacement. | — |

### Libellés

| Où | Avant | Maintenant |
|---|---|---|
| What needs you now › élément « 2 uncertain segmentations » | « Fix in review → » | « Fix in Allocation → » |
| Always open › carte Documents & versions | « documents · 1 processing » | « docs · 1 processing » |

### Style visuel

- Icônes au trait à la place des emoji et symboles : cloche de l'élément de retard, flèche de l'élément questions, icône de colonnes sur la carte Documents & versions.
- Cartes Always open plus basses (marges `--space-2`/`--space-3`), chiffre en `--text-sm` ; au survol, fond `--panel-3` sans soulèvement (les cartes Process se soulèvent toujours).
- Menu de la cloche : 330 px de large, fond `--panel-2`, bordure `--line-2`, rayon `--radius-lg`, ombre portée.
- « Answers by system » : pastille de code (fond `--panel-2`, police mono sauf pour un sous-système) à la place de l'avatar.

### Points incertains

- Le compteur de « What needs you now » compte aussi les lignes de la carte « Pending reassignment requests » quand elle est affichée (lu dans le code, à vérifier à l'écran).
- La carte Allocation lit la progression publiée par Allocation, alors que « N requirements » du bandeau et les statistiques comptent la copie locale du tableau de bord : une fois Allocation ouvert, les chiffres peuvent diverger (à vérifier).
- « Recent activity » : la ligne de réponse reprend la première exigence répondue de la copie locale, pas la plus récente.
- Retards : « What needs you now » (« N contributor responses overdue »), la cloche (« N assignments past the overdue threshold ») et les statistiques (« N late ») parlent encore de retard, alors que DEC-078 a retiré le statut « overdue » de Compliance ; seul le réglage « Overdue threshold » subsiste. À arbitrer.

## Statistiques

`dashboard-et-config.html` · panneau « Statistics » sous le tableau de bord

**En bref.** Le panneau est entièrement refait (DEC-117) : trois onglets « Project », « Allocation » et « Compliance » remplacent « For you » et « For stakeholders ». Chaque bloc s'ouvre sur une phrase calculée, celle qu'un chef de projet dirait à voix haute, puis la figure ; la plupart des lignes ouvrent l'écran derrière le chiffre. Plus rien ne mesure l'IA, et aucun chiffre ne mesure une personne : activité et réponses sont comptées par système et sous-système (DEC-118). Les personnes n'apparaissent que là où il faut relancer, décider ou montrer qui est staffé. Sur un tender SIG (un seul système), les blocs passent aux sous-systèmes.

### Ajouté

| Zone › élément | Ce qu'on voit, ce qui se passe | Réf. |
|---|---|---|
| Project › « Timeline » › dates clés (Key Dates List) | Bloc pleine largeur. À gauche, liste datée : « Tender received » (« requirements captured »), « Q&A cut-off » (« passed » ou « in N days · last day to ask the client »), « Client answers expected » (« passed » ou « in N days »), « Today », « Submission ». Point plein si passé, bleu cerclé pour aujourd'hui, creux à venir, anneau pour la soumission. | DEC-117 |
| Project › « Timeline » › courbe (Progress Trend Chart) | % d'exigences allouées (accent) et répondues (vert) de la réception à la soumission, repères « Today » et « Submission {date} », prolongement en pointillé au rythme de la semaine. Légende « Allocated », « Answered », « at this week's pace » ; infobulle du dernier point « Today · N% allocated » (ou « answered »). | DEC-117 |
| Project › « Timeline » › phrase | « At this week's pace, allocation is done by {date}, N days to spare. The answers would only be all in by {date}, N days after submission. » Date en vert (plus de 2 jours de marge), ambre (2 jours ou moins), rouge (après la soumission) ; variantes « … is complete » et « … has not moved this week ». | DEC-117 |
| Project › « Most active this week » (Leaderboard Row) | Période « last 7 days · {date} – {date} » ; phrase « N actions on the tender this week — +X% on the week before. {SYS} leads, with {sous-système} and {sous-système}. » ; légende « Allocation » / « Answers » / « Comments & questions ». | DEC-117, DEC-118 |
| Project › « Most active this week » › lignes | Jusqu'à 7 systèmes classés : rang (le 1er sur fond bleu), code, sous-ligne de ses sous-systèmes avec leur total (ou « not split into sub-systems »), barre empilée, total. Les validations et verdicts de la session s'ajoutent en direct (« not split N »). Pied : « Counted for the system the work was done on, whoever did it — nobody's own activity is shown. » | DEC-118 |
| Project › « Most active this week » › tender SIG | Les sous-systèmes sont classés à la place des systèmes, sous-ligne « N validated · N answers · N comments » ; phrase « {sous-système} leads SIG's sub-systems. » | DEC-118 |
| Project › « The team » (Team Role Row, Avatar Stack) | Lien « Team casting → » ; phrase « N people on this tender, across M systems — work moved on K of them this week. » (sur un tender SIG : « … on this tender and its M sub-systems — … »). Trois lignes avec piles d'avatars : « Project management » (noms), « N system managers » (« no manager on {codes} — contributors only » ou « one on every system »), « N contributors » (« across N systems »). | DEC-117, DEC-124 |
| Project › « The team » › manques et activité | En rouge « no contributor on {codes} yet » quand un système n'a personne ; la ligne ouvre alors Team casting. Barre « Systems active this week K / M » (« Sub-systems … » sur un tender SIG). | DEC-118, DEC-124 |
| Allocation › « Where the requirements are » (Stacked Bar) | Pleine largeur. Phrase « N of M requirements allocated. Of the rest, N are ready to validate, N to review and N still incomplete. » ; barre en quatre segments « Incomplete », « To review », « To validate », « Allocated », légende avec nombre et %. Clic → Allocation. | DEC-117 |
| Allocation › « By system, with who is on it » (System Manager Row) | Phrase « {SYS} has the most left to allocate — N of M, with {manager ou N contributors}. » (+ en rouge « {SYS} has nobody staffed yet. »). Une ligne par système, de celui qui a le plus à allouer à celui qui en a le moins : code, avatar, manager ou « N contributors · no manager » ou « Nobody staffed yet » (rouge), barre alloué (vert) / à valider (accent), « fait/total ». | DEC-117, DEC-124 |
| Allocation › « By system… » › navigation et cas SIG | Clic → Allocation, ou Team casting pour un système sans personne ; pied « N requirements not routed to a system yet. » Bloc masqué sur un tender SIG : « Sent back for reallocation » prend alors toute la largeur. | DEC-044 |
| Allocation › « Sent back for reallocation » (Reallocation Breakdown) | Phrase « N requirements sent back by a system so far — N reallocated, N kept where it was, N waiting for your decision. » ; trois chiffres « reallocated », « kept as allocated », « to decide » (encadré ambre et cliquable vers Allocation s'il est non nul). | DEC-117 |
| Allocation › « Sent back for reallocation » › détail | « Why » : une barre par motif (« Right system, wrong person », « Wrong system », « This system doesn't apply here ») ; « Latest » : 3 lignes (avatar de qui a renvoyé, « {id} · {SYS} · {nom} · {date} », pastille « Reallocated », « Kept » ou « To decide ») vers Allocation. Vide : « Nothing sent back so far — every system kept what it was given. » | DEC-117 |
| Compliance › « Progress to the client » (Progress Sequence) | Pleine largeur. Phrase « So far the client will be told Compliant on N requirements and Not compliant on M — K of T are not settled yet. » ; quatre étapes fléchées avec %, barre et sous-ligne : « Assigned » (« N of M assignments »), « Internal compliance » (« N answered · M Not compliant »), « Not compliant logged » (« N of M linked to a risk », en rouge s'il en manque), « External compliance » (« N of M requirements settled · K pending »). « Assigned » ouvre Allocation, les trois autres Compliance. | DEC-117 |
| Compliance › « Answers by system » (System Answers Row) | Phrase « N of M answers in — K answers overdue, in {SYS} and {SYS}. » (ou « — none overdue. »). Une ligne par système, retards d'abord : barre verte, « répondues/confiées », repère « N late · Nd » (rouge), « ✓ all in » (vert) ou « N open » ; clic → Compliance. « Answers by sub-system » sur un tender SIG. | DEC-118 |
| Compliance › « What the open requirements are waiting on » (Waiting Queue Row) | Phrase « N requirements still open. » suivie de l'état des contributeurs (« The N with contributors are on time », « K of the N with contributors are overdue »…) et de « N more wait on the client » ; barre fine ; chaque exigence dans une seule file. Vide : « Every requirement has its answer. » | DEC-117 |
| Compliance › « What the open requirements are waiting on » › files | « On a contributor » (« K overdue · the oldest for N days, with {nom} » ou « none overdue ») → Compliance ; « On the client » (« questions asked, the oldest N days ago · answers expected {date} ») → Q&A ; « On your decision » (« {id} · {SYS}, sent back by {nom} ») → Allocation ; « Not assigned yet » (« {ids} — no one to answer yet ») → Compliance. | DEC-117 |
| Compliance › « Not compliant by gap strategy » (Stacked Bar) | Phrase « N Not compliant answers — K still without a strategy. » (ou « … each with its strategy. ») ; barre par stratégie du tender plus « Strategy missing » ; clic → Compliance. Vide : « No Not compliant verdict yet. » | DEC-117 |
| Compliance › « Risks » (Risk Summary Row) | Phrase « N risks in the list, linked N times to Not compliant answers — K shared by several requirements. » (ou « none shared yet »). Les 4 risques les plus liés (ID, intitulé, avatar de l'auteur, « ×N ») ouvrent la page Risks ; « + N more in the list. » Vide : « No risk on this tender yet — they are created in Compliance, on each Not compliant. » | DEC-113 |

### Modifié

| Zone › élément | Avant (8 sept.) | Maintenant | Réf. |
|---|---|---|---|
| Statistics › onglets (Tab Bar) | « For you » (par défaut) / « For stakeholders » : un onglet par public. | « Project » (par défaut) / « Allocation » / « Compliance » : le projet, puis une étape chacun, comme les deux cartes Process. | DEC-117 |
| Statistics › tête des blocs (Stat Block) | Titre et sous-titre gris explicatif. | Titre (avec période ou lien à droite), puis une phrase calculée : chiffres en gras, retard en rouge, limite en ambre, bon en vert. Plus de sous-titre. | DEC-117 |
| Allocation › « Work invalidated by a new version » | Onglet « For you » ; « ⇄ N expert answers now on an outdated version — {ids} », après la simulation v2.2 (une exigence fixe). | Onglet Allocation, pleine largeur ; « ⇄ N contributor answers reopened by new versions — {ids} », somme des réponses rouvertes par les versions déposées sur ce tender. Masqué à zéro ; clic → Documents & versions. | DEC-122 |

### Retiré

| Zone › élément | Ce qui disparaît, et ce qui le remplace s'il y a lieu | Réf. |
|---|---|---|
| For you › « Bottlenecks by perimeter » (Bottleneck Row) | Périmètres classés par âge de la plus ancienne attente (« N awaiting », « Nd oldest », en rouge à partir de 10 jours). Remplacé par « What the open requirements are waiting on » et les retards de « Answers by system ». | DEC-117 |
| For you et For stakeholders › « Compliance profile » (Compliance Bar) | La même barre deux fois : « Compliant » / « R&D needed » / « Not compliant » / « Pending ». Remplacée par la phrase de « Progress to the client » ; plus de segment R&D. | DEC-117, DEC-031 |
| For you › « Blocked on the client » (Q&A Blocked Row) | « N questions raised, oldest N days ago » et une ligne par question. Remplacé par la file « On the client ». | DEC-117 |
| For you › « Casting gaps » | « ✓ Every perimeter has a manager cast » ou « ⚠ N perimeters unstaffed — {noms} » (activités sans manager). Remplacé par « Nobody staffed yet » (By system…) et « no contributor on … yet » (The team) : un manager n'est plus requis. | DEC-117, DEC-124 |
| For you › « Trajectory to deadline » | Courbe des exigences restantes avec repère « Deadline {date} ». Remplacée par « Timeline ». | DEC-117 |
| For stakeholders › « Progress against deadline » | « N requirements remaining, down from M at the start — on pace for the {date} deadline. » Remplacé par la phrase de « Timeline ». | DEC-117 |
| For stakeholders › « AI reliability — correction rate by field » (AI Reliability Row) | Taux de correction par champ (« Type », « Class », « Activity », « Allocation »). Aucun remplacement sur le tableau de bord ; l'IA reste dans Configuration › AI feedback. | DEC-117 |

### Style visuel

- Trois couleurs hors de l'échelle suivie, reprises de l'accueil : `--brand-blue`, `--brand-blue-soft`, `--brand-slate` (repère « Today », 1er rang, barres d'activité et de motifs, files « On a contributor » et « On the client », lien « Team casting → »).
- Barres empilées de 26 px (10 px en version fine) ; segments neutre (`--line-2`), `--ia`, `--accent`, `--ok`, `--warn`, `--human`.
- Avatars ronds de 24 px (initiales sur la couleur de la personne), piles de six puis « +N ».
- Grille à deux colonnes (une seule sous 760 px), blocs à la hauteur de leur contenu ; Timeline, Where the requirements are, Progress to the client et Work invalidated en pleine largeur.
- Codes de système et ID de risque en `--font-mono` ; intertitres « Why » et « Latest » en petites capitales grises.

### Points incertains

- Historique de la courbe, activité de la semaine, réallocations déjà décidées et chiffres de « Answers by system » sont écrits à la main ; seules les données de la session (journal d'activité, demandes de réaffectation, totaux de Compliance, risques, versions) sont réelles. Le calcul attendu dans le produit n'est pas montré.
- Le point « Today » de la courbe et « Where the requirements are » comptent la copie locale du tableau de bord, pas la progression publiée par Allocation qui alimente la carte Allocation.
- Les retards sont une liste fixe, sans lien avec « Overdue threshold » de la configuration.
- Les demandes de réaffectation ne sont pas rangées par tender dans le prototype (tri par préfixe d'identifiant).

## Documents & versions

`documents.html` · route `#documents`

**En bref.** L'écran garde la structure du 8 septembre : bandeau de quatre chiffres, recherche et filtre, liste des documents dans l'ordre du tender (↑ / ↓), historique des versions dépliable par document, ajout d'un document avec progression, suppression confirmée qui annonce les pertes, export d'un document. Les versions étaient déjà rattachées à leur document sur cet écran (DEC-069). Ce qui change, c'est l'effet d'une nouvelle version : elle rouvre réellement, dans Compliance, les réponses des exigences qu'elle modifie. L'écran affiche ce nombre de réponses rouvertes, qui peut être 0, au lieu d'un compte de « stale verdicts » qui n'était jamais nul ; ce vocabulaire est remplacé partout par « answers reopened ». La cloche ouvre maintenant une liste, le fil d'Ariane nomme le tender ouvert, les toasts s'affichent enfin, et l'écran prend la charte (police, logo, icônes, couleurs).

### Ajouté

| Zone › élément | Ce qu'on voit, ce qui se passe | Réf. |
|---|---|---|
| En-tête › cloche › menu « Notifications » (Icon Button) | La cloche ne faisait rien au 8 sept. Elle ouvre maintenant un menu titré « Notifications · N ». Chaque document dont la version en vigueur a rouvert des réponses y a une ligne « **N answer(s)** reopened by vX.Y of {nom court du document} » (point rouge, date de la version). Chaque document sans exigence a une ligne « **{nom court}** has no requirements yet — not processed » (point ambre, date d'ajout). Le nom court est la partie avant le tiret. Sans élément : « Nothing waiting on you here. » | — |
| En-tête › cloche › clic sur une ligne du menu | Le menu se ferme, l'historique des versions du document s'ouvre et, pour une réponse rouverte, la liste défile jusqu'au document. Un clic hors du menu le ferme. | — |
| En-tête › cloche › pastille (Notification Dot) | Petit point rouge sur la cloche, masqué quand le menu est vide (voir Points incertains). | — |

### Modifié

| Zone › élément | Avant (8 sept.) | Maintenant | Réf. |
|---|---|---|---|
| Liste › action « Upload a new version — runs gap analysis » › nombre annoncé | Le nombre annoncé était celui des exigences modifiées (2 ou 3). Chaque téléversement affichait donc la note ⚠ dans l'historique, la mention ⚠ sous l'état et un toast d'alerte, sans effet sur les autres écrans. | Le nombre annoncé est celui des réponses rouvertes (affectations déjà répondues) sur les exigences du document que la version modifie. Dans Compliance, ces affectations repassent en attente de réponse, verdict effacé, et le tableau de bord annonce la version. À 0, pas de note ⚠ ni de mention sous l'état, et le toast de succès omet le compte. | DEC-016, DEC-122 |

### Libellés

| Où | Avant | Maintenant |
|---|---|---|
| Bandeau de synthèse › 4ᵉ tuile (Stat Tile / Card) | « Verdicts made stale by a new version » | « Answers reopened by a new version » |
| Barre de filtres › liste déroulante, 4ᵉ option | « Has stale verdicts » | « Has reopened answers » |
| Liste › ligne › mention sous la pastille d'état | « ⚠ N stale verdict(s) » | « ⚠ N answer(s) reopened » |
| Liste › document en traitement › libellé de progression (DEC-045) | « Characterisation — class, activity and type… » | « Characterisation — class, system and type… » |
| Historique des versions › note d'avertissement (Warning / Notice Box) (DEC-119 pour le renvoi) | « **N verdict(s) made stale by this version** — given before the change, on requirements the change affected. They need confirming or redoing in Compliance. » | « **N answer(s) reopened by this version** — the requirements changed, so their verdicts went back to pending. See Allocation › Document view › Changes. » Au singulier : « … — the requirement changed, so its verdict went back to pending. … ». Le lien « Open Compliance → » ne change pas. |
| Toast après téléversement d'une version | « vX.Y uploaded — gap analysis: +a ~m −r, N verdict(s) now stale » | « vX.Y uploaded — gap analysis: +a ~m −r, N answer(s) reopened » (sans la fin quand le compte est 0) |
| Modale « Export one document » › case du bloc « Include » (DEC-045) | « Characterisation — class, activity, type and status » | « Characterisation — class, system, type and status » |

### Style visuel

- Icônes SVG au trait (Icon) à la place des glyphes. « ⬇ » d'« Export one document » devient l'icône de téléchargement. « ⬆ » de la zone d'ajout et de l'action de ligne devient l'icône de téléversement. Le caret « ▶ » de la ligne devient un chevron, un peu plus grand (11 px au lieu de 9 px), qui pivote toujours à l'ouverture.
- Toast : fond `--panel-3`, bordure, ombre, coins `--radius-lg`. Menu des notifications : 330 px de large, fond `--panel-2`, point coloré par type de ligne (`--warn`, `--ia`).

### Points incertains

- La note renvoie à « Allocation › Document view › Changes », mais dans le prototype une version téléversée ici n'apparaît pas dans Allocation : ni dans la colonne ni dans l'onglet Changes. Le lien attendu entre les deux écrans reste à confirmer (DEC-119) (à vérifier).
- La pastille rouge de la cloche est affichée dès l'ouverture de l'écran et ne se met à jour qu'à l'ouverture du menu. Sur Q&A, elle suit l'état en continu. Le comportement sur Documents n'est probablement pas voulu.
- Aucune différence de rôle à l'écran : réordonner, téléverser, supprimer et exporter restent ouverts à tous (comme au 8 sept.). À vérifier contre la spécification.
- Le document de démo « Q&A response dossier — round 1 » a été renommé « Addendum n°3 — technical clarifications ». Cela suggère que le dossier de réponses du client n'est plus un document du tender et passe par l'import de Q&A (déduit, à vérifier).

## Allocation — page, tableau, vue Document, versions

`revue-documentaire.html` · route `#review` — tout l'écran sauf le panneau de détail · captures : [avant](captures/03-allocation-tableau-avant.png), [maintenant](captures/03-allocation-tableau-apres.png)

**En bref.** L'écran s'appelle « Allocation » : le titre ouvre la barre de statut, qui gagne une jauge « % allocated ». « Finalize allocation », la pastille « v2.1 active » et le mode « Compare » disparaissent.
Le tableau gagne une colonne Changes (le texte avec ses différences face à une version antérieure du document), des colonnes personnalisées et des largeurs réglables. TK OBS se fond dans System et PBS devient l'élément produit. OBS et Compliance passent en lecture seule, et « Manager » devient « Assigned to », lu sur les organisations (OBS).
Les versions se comparent document par document : dans l'onglet Changes du navigateur de la vue Document, et dans un onglet Versions du détail. Une exigence changée repasse To review.
Le clavier gagne la sélection, N, C et ⌘/Ctrl+Z. Un contributeur voit désormais tout le tender et ne modifie que son système.

### Ajouté

| Zone › élément | Ce qu'on voit, ce qui se passe | Réf. |
|---|---|---|
| En-tête › menu « Export ▾ » › note des colonnes personnalisées (Export Panel) | Quand le tender a des colonnes personnalisées : « N custom columns included — internal exports only. Never sent in the client compliance matrix. » Le toast de fin ajoute « · N custom columns ». | DEC-068 |
| En-tête › menu des notifications › lien vers une exigence absente (Notifications Dropdown) | Si l'exigence d'une notification n'existe pas dans le tender ouvert, le clic affiche le toast « This requirement isn't in this tender ». Avant, le détail ne pouvait pas s'ouvrir. | — |
| Barre de statut › jauge « % allocated » (Triage Bar, Progress Bar) | Après « N requirements » : une mini-barre verte et « N% allocated ». Infobulle « Share of requirements fully allocated — characterisation and every system validated ». Le pourcentage suit le compteur « allocated » (voir Points incertains). | — |
| Barre d'outils › bouton « ＋ Column » (Custom Column Editor) | Entre « Filter ▾ » et « View ▾ », avec l'infobulle « Add a column of your own to this tender's Allocation table ». Il ouvre la fenêtre de création ; il est masqué pour un contributeur. | DEC-064 |
| Barre d'outils › menu « View ▾ » › « Reset column widths » (Columns Panel) | Apparaît sous la liste des colonnes dès qu'une largeur a été changée. Il remet toutes les largeurs par défaut (toast « Column widths back to default »). | — |
| Barre d'outils › icône clavier, tout à droite (Shortcut Help) | La liste des raccourcis s'ouvre au survol ou au focus clavier, en quatre groupes : « Move », « Edit », « Select », « Act » (détail aux lignes Clavier). Elle remplace la bande d'aide de la barre de statut. | — |
| Tableau › colonne « Changes » (Changes Cell) | Nouvelle colonne entre Requirement et Class, avec l'infobulle « The requirement with what changed since an earlier version of its document — removed words struck, added ones highlighted ». Elle est affichée par défaut seulement si un document du tender a plusieurs versions ; sinon on l'active dans View ou avec C. | DEC-119 |
| Tableau › en-tête Changes › « vs previous ▾ » / « vs first ▾ » (Version Picker Button, Version Picker Popover) | Fixe la comparaison de toutes les lignes : « The previous version » (« of its document — what the version in force changed ») ou « The first version » (« of its document — everything since the tender was issued »). Si des lignes ont leur propre choix, le menu prévient « N requirements have a version of their own — choosing here resets them. », puis les remet à zéro. | DEC-119 |
| Tableau › entonnoir de la colonne Changes (Column Filter Section) | Valeurs « Modified », « Added », « No change », calculées par rapport à la version que compare chaque ligne. | DEC-119 |
| Tableau › poignée de redimensionnement des en-têtes (Column Resize Handle) | Une poignée au bord droit de chaque en-tête sauf la case de sélection, visible au survol, avec l'infobulle « Drag to resize · double-click to reset ». On la glisse pour redimensionner ; un double-clic revient au défaut ; une fois la poignée sélectionnée, ←/→ agissent par pas de 16 px. Les largeurs sont gardées par tender quand on revient sur l'écran. | — |
| Tableau › en-têtes des colonnes personnalisées (Custom Column Header Cell) | Ajoutées à la fin du tableau, qui défile jusqu'à la nouvelle. L'en-tête porte le nom (un clic trie), un entonnoir pour une liste, et « ✎ » (« Edit or delete this column », masqué pour un contributeur). Infobulle « {nom} — a column of this tender's own. Entered by people, never by the AI. » | DEC-064 |
| Tableau › colonnes personnalisées dans View, le tri et les filtres (Custom Column Tag) | Elles sont listées dans View avec l'étiquette « custom » (masquables, déplaçables) et triables ; une liste a son entonnoir (ses options + « — empty — »). Le filtre avancé gagne un groupe « Custom columns » ; une liste multiple y offre « is any of », « is none of », « is empty », « is not empty ». | DEC-066 |
| Tableau › colonnes personnalisées partagées avec Compliance | Mêmes colonnes et mêmes valeurs que dans Compliance. Une colonne est visible sur l'écran où elle a été créée, et masquée sur l'autre jusqu'à ce qu'on l'active dans View (choix gardé). La supprimer la retire des deux écrans. | DEC-097 |
| Tableau › cellule Changes d'une exigence changée (Changes Cell, Word Diff) | Une étiquette de version (« v2.1 », ou « v2.0 · v2.1 »), masquée quand on compare à la version précédente, puis le texte : mots retirés barrés sur fond rouge pâle, mots ajoutés sur fond vert pâle, le début et les longs passages inchangés repliés en « … ». Une exigence nouvelle affiche « New » (ou « New in vX ») et tout son texte surligné. L'infobulle du texte donne la description du changement. | DEC-119 |
| Tableau › cellule Changes sans changement (Changes Cell) | « No change », ou « Single version » quand le document n'a qu'une version (infobulle « {document} has a single version »). En « Wrap text », la cellule montre le texte entier sous une ligne qui porte l'étiquette et le sélecteur. Cellule vide sur les lignes d'information et les sous-lignes. | DEC-119 |
| Tableau › cellule Changes › bouton « vs vX ▾ » (Version Picker Button, Version Picker Popover) | Choisit la version de comparaison de cette ligne : le menu « {ID} — compare vN, in force, with » liste les versions antérieures (« date · note », avec « — no change since » si rien n'a changé depuis), et « Same as the column » revient au choix commun. Le bouton passe en couleur d'accent quand la ligne a son propre choix. Infobulle « Compared with vX · date · note — chosen for this requirement. Click to compare with another version. » | DEC-119 |
| Tableau › cellule System, confiance de l'aiguillage (Turnkey) | Sur un tender Turnkey, « N% » s'affiche à droite de l'étiquette du système, en gris, ou en orange gras sous 75 %. Infobulle « Turnkey routing — N% confidence (below the 75% threshold — which system this belongs to is uncertain) ». Visible sur une exigence à un seul système et sur chaque sous-ligne système. | DEC-077 |
| Tableau › cellule System, « +N » (Activity / Requirement Tag) | La cellule tient sur une ligne : autant d'étiquettes que la largeur le permet, puis « +N » en pointillés (infobulle « Also: {systèmes} ») ; en « Wrap text », toutes s'affichent. Infobulle de la cellule : « {systèmes} — click to edit », ou « No system yet — click to edit ». | — |
| Tableau › système partenaire (Turnkey) (Activity / Requirement Tag) | Un partenaire ajouté au tender apparaît comme un système, étiquette turquoise, infobulle « {nom} — added for this tender, not part of the Turnkey model. The AI never predicts it; the partner works outside the tool. ». Sa sous-ligne a l'OBS « — » (« A partner system has no teams ») et l'Assigned to « PM · for partner », que propose aussi le filtre Assigned to. Voir le panneau de détail. | DEC-082 |
| Tableau › statut « Reassignment requested » (Turnkey) (Status Pill) | Sur Turnkey, la pastille d'une exigence devient « Reassignment requested » (violet) quand un système demande une réassignation ; un contributeur qui a son système sur l'exigence voit, lui, le statut de ce système. Infobulle « A system asked for this requirement to be reassigned — approve or reject it — Nothing to validate yet ». La valeur s'ajoute aux filtres Status ; voir le panneau de détail. | DEC-104 |
| Tableau › exigence changée dans la version en vigueur (Status Pill) | Une exigence ajoutée ou modifiée dans la version en vigueur de son document passe To review. Motif dans l'infobulle de la pastille : « Added in vX of its document — see the Versions tab » (ou « Modified in … »). La valider vaut traitement du changement. | DEC-072 |
| Tableau › cellules des colonnes personnalisées (Custom Column Cell) | Texte libre : un champ éditable. Liste simple : une liste déroulante avec « — ». Liste multiple : un bouton qui affiche les valeurs et ouvre des cases à cocher (↑/↓, Espace, Entrée confirme et descend, Échap rétablit) ; cellule vide sur les sous-lignes, « — » sur les lignes d'information. | DEC-066 |
| Tableau › sous-lignes système et organisation, ABS / PBS et OBS faible (Branch / Allocated-Activity Sub-row) | La sous-ligne système affiche maintenant l'ABS et le PBS du système, en lecture. Un OBS proposé sous 75 % porte « N% » en orange gras dans la cellule OBS, avec l'infobulle « OBS proposed with N% confidence — below the 75% threshold, to review ». | — |
| Tableau › tender SIG autonome (RFP-2026-114) | L'écran sert aussi un tender SIG. La colonne System est masquée et absente de View ; il n'y a ni regroupement par système, ni confiance d'aiguillage, ni statut de niveau Turnkey. | DEC-044 |
| Tableau › tender à référentiel (produit Mainline) | Les cellules ABS et PBS deviennent des listes déroulantes du référentiel du produit (PBS groupé par famille, groupe « From another product's model » pour un élément hors liste). L'en-tête OBS devient « OBS · role » et View affiche « OBS (role) ». | DEC-061, DEC-062 |
| Barre d'actions groupées › menu « Re-run ▾ » (Bulk Selection Action Bar) | Entre « Assign » et « Classify », avec l'infobulle « Replay an allocation model on the selection. Derivation only — who answers is not touched. ». Le menu liste « SIG Urban », « SIG Mainline Wayside », « SIG Mainline Onboard », « RST Metro », « RST High speed ». | DEC-052 |
| Barre d'actions groupées › résultat de « Re-run » | Seules les exigences à un seul système sont relancées. Toast récapitulatif : « N re-derived with {modèle} · N left alone — already answered · N span several systems — re-run those from the panel · N not requirements — nothing to derive ». Une exigence dont le résultat ne change pas n'est pas comptée. | DEC-091 |
| Clavier (vue Review) › sélection (Shortcut Help) | « X » coche la ligne active depuis n'importe quelle colonne ; « Shift+↑/↓ » (ou Shift+J/K) étend la sélection. « ⌘/Ctrl+A » sélectionne tout ce que montrent les filtres (toast « N selected — everything in view ») ; « Esc » vide la sélection. | DEC-085 |
| Clavier (vue Review) › N, C, Entrée/F2 (Shortcut Help) | « N » va à la prochaine exigence To review ou To validate (sinon toast « Nothing left to review or validate in this view »). « C » montre ou masque la colonne Changes (toasts « Changes column shown — C to hide it », « Changes column hidden — C to show it », « Every document has a single version — no change to show »). « Enter » ou « F2 » commence l'édition de la cellule active. | DEC-085, DEC-119 |
| Clavier › « ⌘/Ctrl+Z » | Annule la dernière action annulable, même après la disparition du toast (30 au plus) : la personne choisie dans la cellule Assigned to d'une ligne, une validation unitaire (pastille, V, bouton du détail) ou groupée. Toast « Undone — {message} » ou « Nothing to undo ». Le bouton « Undo » des toasts a l'infobulle « Undo (Ctrl/⌘ Z) ». | DEC-085 |
| Vue Document › onglets du navigateur « Outline » / « Changes » (Changes Navigator) | En haut du navigateur de gauche, seulement en vue Document et si un document du tender a plusieurs versions. « Changes » porte le nombre de changements (badge ambre) et l'infobulle « What changed between two versions of a document ». Il remplace l'arbre et la recherche par la liste des changements. | DEC-119 |
| Vue Document › onglet Changes, en-tête (Changes Navigator, Compare Summary Chip) | Choix du document (« Doc i — {nom} », grisé avec « · one version »), puis de la version de départ (« vX — {date} ») « → vN · in force ». Les pastilles « +N added », « ~N modified », « −N removed » et l'alerte « ↺ N changes reopen answers already given » filtrent la liste (« Show only these » / « Show every change »). Navigation « Change i of n » avec « ‹ » / « › » (« Previous change — [ », « Next change — ] »), et « · show all N » sous un filtre. | DEC-070, DEC-119 |
| Vue Document › onglet Changes, cartes (Change List Card, Change Type Tag) | Une carte par changement : type (« Added » vert, « Modified » ambre, « Removed » rouge), ID, « § n° », description sur deux lignes, et l'effet sur le travail fait. Effets : « New — needs allocation », « New — allocated since », « ↺ Was answered — back to To review » (orange), « Awaiting its answer — the contributor answers the new text », « Back to To review », « Removed — its work stays archived with vX ». Un clic sélectionne l'exigence et fait défiler le document jusqu'à elle. | DEC-119 |
| Vue Document › onglet Changes, états vides | « Only one version of this document — nothing to compare yet. » ou « No change between vX and vY in this document. » | DEC-119 |
| Vue Document › rail « Changes » du navigateur replié | Quand le navigateur est replié en vue Document : un rail vertical « N Changes ». Un clic ouvre l'onglet Changes et déplie le navigateur. | DEC-119 |
| Vue Document › reclasser un bloc en « Requirement » sur un tender SIG (Nature Picker) | Le bloc reçoit d'office le système SIG, et apparaît avec lui dans le tableau. Ailleurs, il reste sans système, comme avant. | — |
| Panneau › onglet « Versions » (Versions Tab) | Il n'apparaît que si l'exigence a changé dans la version en vigueur de son document. Il montre « Added in vX » / « Modified in vX » (date · note), « {document} — compared with vY », la description, « What changed » (différences mot à mot) et « Full text in vY » repliable — ou, pour une nouvelle, « New in this version — there is no earlier text to compare with. ». En bas : « Earlier versions ». | DEC-071 |
| Panneau › onglet Versions, suite à donner (Versions Tab) | Un encadré dit « Set back to To review by this change. Validate the requirement once the change has been checked. » (plus « Its status shows {statut} first — that is more restrictive and wins. » si besoin), ou, une fois traité, « Checked since the change — the requirement has moved on from To review. ». Le bouton « Show in the document → » (« Opens the Document view on its Changes, at this requirement ») ouvre l'onglet Changes sur l'exigence. | DEC-072 |
| Panneau › exigence supprimée (Removed Requirement Panel) | S'ouvre au clic sur un bloc supprimé de l'onglet Changes : « Removed » + « Removed in vX », le texte d'avant, « {document} — present in vY, gone from vX », la description et « Text in vY ». La note dit « No longer part of the tender. It shows only under Changes, in the Document view — never in the table or the outline. » ; rien n'est modifiable. | DEC-017, DEC-119 |
| Panneau › champs des colonnes personnalisées (Custom Fields Panel Section) | Chaque colonne personnalisée est aussi éditable dans le détail, avec la note « Custom columns — entered by people. The AI never fills them, and they never put a requirement into review. ». Mise en page : voir le panneau de détail. | DEC-067 |
| Fenêtre « New column » / « Edit column » (Custom Column Editor) | Champs « Name » (« e.g. Commercial risk ») et « Type » (« Free text » / « List ») ; pour une liste, « Options » (« Add an option… » + « Add », « used by N ») et la case « Allow several values per requirement ». Un encadré rappelle la portée : ce tender seulement, partagée avec Compliance, interne, jamais remplie par l'IA. Boutons « Cancel », « Create column » / « Save », et « Delete column… » en édition. | DEC-064, DEC-068 |
| Fenêtre de colonne › garde-fous (Custom Column Editor) | Le type se verrouille dès qu'une valeur existe (« The type can't change — N requirements hold a value, and converting would lose data. Renaming is fine. »), et on ne revient pas à une valeur unique si une exigence en a plusieurs. Une option utilisée ne se retire pas (« “X” is used by N requirements — clear those values before removing it »). La suppression se confirme avec le nombre de valeurs perdues (« Delete “X”? », « Keep it » / « Delete column and N values »). | DEC-065, DEC-068 |
| Fenêtre de colonne › contrôles à l'enregistrement (Custom Column Editor) | Toasts « Give the column a name », « A column called “X” already exists » (colonnes natives comprises), « A list needs at least one option », « “X” is already an option ». Fin : « “X” added — at the end of the table », « “X” updated », « “X” deleted — N values removed ». Un contributeur qui atteint l'éditeur reçoit « Only project managers create or change columns ». | DEC-064 |

### Modifié

| Zone › élément | Avant (8 sept.) | Maintenant | Réf. |
|---|---|---|---|
| En-tête › sélecteur d'affichage | « Review », « Document », « Compare ». | « Review », « Document ». La comparaison est l'onglet Changes de la vue Document ; pendant ce temps, « Document » reste actif et cliquer dessus ne change rien. | DEC-119 |
| En-tête › menu « Export ▾ » (Export Panel) | Pour un contributeur (View as), l'export ne prenait que ses exigences. | Tout le tender pour tous, réduit seulement par les filtres de colonnes et le filtre avancé. | DEC-012 |
| Barre de statut › titre de page (Triage Bar, Page Title) | Une ligne à part au-dessus de la table : « Requirements review » + « N shown of M — verify class, activity, managers, experts and statuses ». | « Allocation » ouvre la barre de statut (police de titre, marque rouge, séparateur), avec l'infobulle « Verify class, system, assignments and statuses ». La table gagne une ligne de hauteur. | DEC-029 |
| Barre de statut › pastille des changements | « N changes v2.0 → v2.1 » : compte augmenté de 1 et incluant les exigences supprimées. | « N changed in latest version » : les exigences ajoutées ou modifiées dans la version en vigueur de leur document, que le filtre affiche. | DEC-069 |
| Barre de statut › compteurs (Triage Bar) | Comptés sur tout le tender, alors qu'en View as un contributeur ne voyait ensuite que ses lignes. | Tout le tender pour tous. Sur Turnkey, les exigences du système d'un contributeur comptent avec le statut de ce système. | DEC-012, DEC-104 |
| Barre de statut › pastille « pending reassignment » | Ne comptait que les demandes de réassignation. | Compte aussi les propositions « + Missing system » qui attendent le chef de projet. | — |
| Barre d'outils › nombre de lignes affichées | Dans le sous-titre, toujours visible. | « N of M shown » juste après la recherche, seulement quand un filtre réduit la liste. | — |
| Barre d'outils › puce du filtre actif | À gauche de la recherche, phrase tronquée (complète au survol). | Après la recherche, jamais tronquée : si la place manque, elle passe sur sa propre ligne. | — |
| Barre d'outils › menu « Filter ▾ » (Advanced Filter Builder) | Groupe Allocation : PBS (5 types), ABS, OBS (équipes), Manager, Allocation level, « Awaiting manual allocation ». Champs « Doubt — which pass » et « Changed since version ». | Groupe Allocation : ABS, PBS et OBS (texte), Assigned to, Allocation level. « Doubt — where » (« Which system », « Within the system », « No doubt ») et « Changed in latest version » ; Compliance sans « R&D Needed », Status avec « Reassignment requested », groupe « Custom columns ». | DEC-074, DEC-103, DEC-123 |
| Barre d'outils › menu « Filter ▾ », compteur en direct | Pour un contributeur, il comptait ses seules exigences. | Il compte sur tout le tender, comme le tableau. | DEC-012 |
| Barre d'outils › menu « View ▾ » (Columns Panel) | « Group by » « None / Activity ». Colonnes : « Class », « Activity », « ABS », « PBS », « TK OBS (activity) », « OBS (team) », « Manager », « Status », « Compliance ». | « None / System » (sans « System » sur SIG). Colonnes : « Changes », « Class », « System », « ABS », « PBS », « OBS (team) » ou « OBS (role) », « Assigned to », « Status », « Compliance », puis les colonnes personnalisées (étiquette « custom »). | DEC-045, DEC-044 |
| Tableau › colonnes (Requirement Table (Review Grid)) | ID, Requirement, Class, Activity, ABS, PBS, TK OBS, OBS · team, Manager, Status, Compliance. | ID, Requirement, Changes, Class, System, ABS, PBS, OBS · team, Assigned to, Status, Compliance, puis les colonnes personnalisées. | DEC-077, DEC-119, DEC-064 |
| Tableau › colonnes visibles par défaut | Toutes. Sur Turnkey, la vue du chef de projet masquait ABS, PBS, OBS et Manager et montrait TK OBS. | Même réglage Turnkey, sans TK OBS. Sur un tender SIG, System est masquée ; Changes est masquée si aucun document n'a plusieurs versions. | DEC-044, DEC-119 |
| Tableau › colonne « Activity » → « System » | « Activity », sans infobulle ; les étiquettes passaient à la ligne et étaient coupées dès la troisième. | « System », avec l'infobulle « The system(s) the requirement is routed to — on Turnkey, with the routing model's confidence. ». Une seule ligne, avec « +N ». | DEC-045 |
| Tableau › colonne PBS | Une liste déroulante de cinq types (« Functional », « Performance », « Security », « Interface », « Regulatory »), avec un entonnoir. | L'élément produit : texte en lecture seule, ou liste déroulante du référentiel (modifiable) sur un tender à référentiel ; plus d'entonnoir. Infobulle « Product Breakdown Structure — the product element the requirement bears on ». | DEC-062, DEC-074 |
| Tableau › colonne « OBS · team » | Une liste déroulante des équipes avec leur expert : la choisir assignait (toast « {ID} assigned to {équipe} » avec Undo). Un entonnoir ; infobulle « Pass 2 — the team or service within the activity. This is what casting staffs. » | La valeur de l'organisation, en lecture seule, sans entonnoir ; « Multiple (N) » sur plusieurs systèmes. Infobulle « The team or service within the system — informational, not a separate person to assign. » | DEC-054, DEC-087 |
| Tableau › colonne « Manager » → « Assigned to » | Le responsable de l'exigence, choisi parmi tous les managers (prénoms) ; « Multiple (N) » sur plusieurs systèmes. | La personne de chaque organisation (OBS). Avec une seule organisation : une liste limitée aux membres du système (toast « {ID} assigned to {nom} » / « {ID} unassigned », avec Undo). Sinon un résumé (prénoms, « n/m assigned », « Unassigned » ou « PM · for partner ») avec le détail par système en infobulle. | DEC-087, DEC-102, DEC-123 |
| Tableau › personne manquante | Une organisation sans personne laissait la ligne Incomplete. | La ligne peut être To validate ou Allocated sans personne ; le manque reste visible (« Unassigned », « n/m assigned »). Voir le panneau de détail. | DEC-025 |
| Tableau › cellule Class | Infobulle « AI-detected, unconfirmed — Click to switch classification ». | Tant que la classe est celle de l'IA, infobulle « Characterisation model: {niveau} confidence — Click to switch classification » (« {niveau} » = low, medium ou high ; « , not confirmed yet » s'ajoute en Low). Désactivée pour un contributeur (« … — Set by the project manager ») ; le toast « Nature and class are set by the project manager » répond si l'action est tentée autrement. | DEC-120, DEC-086 |
| Tableau › clic sur la pastille Status (Status Pill) | Sur une exigence à un seul système, un premier clic validait la caractérisation (« {ID} characterisation validated »), un second l'allocation (« {ID} allocated — sent to Expert Review »). | Un seul clic valide les deux (« {ID} allocated — sent to Compliance »). Si l'allocation est encore Incomplete, rien n'est validé : toast « Nothing to validate yet — fill this in first ». | DEC-099 |
| Tableau › pastille Status sur Turnkey (Status Pill) | Même logique que sur les autres tenders. | Chef de projet : le niveau Turnkey (nature, classe, aiguillage), et un clic valide l'aiguillage (« {ID} routing validated — sent to its systems »). Contributeur : le statut de son système, et un clic valide ce système. Voir le panneau de détail. | DEC-104 |
| Tableau › colonne Compliance (Compliance Pill) | Sur une exigence à plusieurs systèmes, la pastille pouvait porter « 🔒 » (« Locked by {nom} — no longer follows the activities below ») ; quatre verdicts, dont « R&D Needed ». | Pastille sans verrou, verdicts « Compliant », « Not Compliant », « Pending ». Toujours en lecture seule : le verdict se saisit dans Compliance. | DEC-039, DEC-028, DEC-031 |
| Tableau › cellule Requirement (Block Badge, Disclosure / Expand Chevron) | Chevron de dépliage dans la cellule ID ; « ⚠ Blocked » seulement d'après un texte saisi à la main ; badge « Δ v2.1 » écrit en dur. | Chevron avant le texte. « ⚠ Blocked » sur toute ligne dont un système attend une réassignation (infobulle « {système} — reassignment needed »). « Δ vX » donne la vraie version (« Added/Modified in vX of its document ») et n'apparaît que si la colonne Changes est masquée. | DEC-119 |
| Tableau › lignes d'information et titres | Pastille « To review » quand l'IA doutait de leur nature. | Aucun statut (« — ») ; le doute se voit sur la puce de nature, en vue Document. Un clic sur un titre ouvre toujours le détail. | DEC-073 |
| Tableau › sous-ligne système (Branch / Allocated-Activity Sub-row) | Listes « expert » (OBS), manager et verdict, éditables ; ABS et PBS vides ; colonne TK OBS en %. | ABS, PBS et OBS en lecture ; une liste « Assigned to » limitée aux membres du système (toast « {système}: assigned to {nom} » / « {système}: unassigned ») ; verdict en lecture (« Set on Compliance — read-only here. ») ; confiance d'aiguillage à côté de l'étiquette (Turnkey). | DEC-087, DEC-039 |
| Tableau › statut des sous-lignes sur Turnkey | Affiché pour tous. | Masqué pour le chef de projet, sur les sous-lignes système comme organisation : il valide un système depuis le détail. Le contributeur voit le sien. | DEC-104 |
| Tableau › sous-ligne organisation (Branch / Allocated-Activity Sub-row) | Listes expert, manager et verdict ; nom de l'équipe. | OBS en lecture (avec « N% » s'il est faible), « Assigned to » limité aux membres du système, verdict en lecture. Une organisation sans nom s'affiche « Organisation N » (« Role N » sur un tender à référentiel). | DEC-087, DEC-039 |
| Tableau › tri par colonne | PBS triait par type, OBS par équipe-expert, Manager par nom. | PBS par élément produit, OBS par organisation, Assigned to par noms des personnes (lignes sans personne d'abord). Les colonnes personnalisées sont triables ; Changes ne l'est pas. | DEC-123 |
| Tableau › entonnoirs de colonne (Column Filter Section) | Class, Activity, PBS (5 types), OBS (équipes), Manager, Status. | Changes, Class, System, Assigned to, Status, et les colonnes personnalisées de type liste. Assigned to a une valeur par organisation, « Unassigned » si l'une n'a personne, et « PM · for partner » si le tender a des partenaires ; Status gagne « Reassignment requested ». | DEC-123, DEC-119 |
| Tableau › ce que voit un contributeur (Requirement Row (Review Table Row)) | En View as, seules les exigences dont il était manager s'affichaient, toutes modifiables. | Tout le tender. Sur les lignes hors de son système, les contrôles sont désactivés (infobulle « Not assigned to you — read only »), la case de sélection et le chevron restent. « ＋ Column » et « ✎ » sont masqués, et « N » ne mène qu'à son travail (« Nothing of yours left to review or validate in this view »). | DEC-012, DEC-100 |
| Barre d'actions groupées › « Assign ▾ » (Bulk Selection Action Bar) | Quatre champs : « Manager », « OBS », « Activity », « PBS » (5 types). | Deux champs, « Assigned to » et « System ». La personne va sur les organisations de son propre système : remplace celle d'un système à une seule organisation, sinon remplit seulement les vides (toast « N requirements → {nom} · N left as is (…) », ou « Nothing assigned — … »). Ajouter un système crée aussi sa sous-ligne. | DEC-087, DEC-102, DEC-123 |
| Barre d'actions groupées › « Validate » | Validait l'étape suivante de chaque ligne (caractérisation, puis allocation), sans Undo. | Une validation complète par ligne ; toast « N of M validated — K were not ready » avec Undo. | DEC-099, DEC-085 |
| Barre d'actions groupées › contributeur | Il ne voyait que ses lignes, et pouvait toutes les modifier. | Il peut cocher n'importe quelle ligne, mais Assign, Re-run, Mark to review et Validate n'agissent que sur les siennes (toast « N selected requirements are not on your system — left as is »). « Classify » est masqué. | DEC-100, DEC-086 |
| Clavier (vue Review) › touches existantes | Flèches et J/K, Espace sur la case, V valide l'exigence active, A met le focus sur la première liste déroulante de la ligne. | V valide la sélection s'il y en a une, sinon l'exigence active ; A va à la cellule Assigned to. ←/→ suivent l'ordre affiché, colonnes déplacées et personnalisées comprises. Mettre le focus dans un champ d'une cellule (clic ou Tab) en fait aussi la cellule active. | DEC-085 |
| Vue Document › titre et pied de page (Document Reading View) | « Technical Requirements Specification » et « … — Ref. STB-2026 — Version 2.1 » sur tout tender ; pied « Doc i / n — STB-2026 v2.1 — Restricted distribution ». | Le nom et la référence du tender ouvert ; pied « Doc i / n — {version en vigueur du document} — Restricted distribution ». | DEC-069 |
| Vue Document › navigateur, points des exigences (Nav Tree Item) | « To review — AI confidence is low » ; point « Unassigned » si aucun expert. | « To review » ; point non assigné avec l'infobulle « Unassigned » ou « n/m assigned ». | DEC-087 |
| Vue Document › puce d'une exigence (Type Chip) | « {type} · {statut} », par exemple « Functional · To review ». | « Requirement · {statut} » (voir Points incertains pour les lignes de tableau). | DEC-074 |
| Vue Document › badge non assigné (Document Block) | « Unassigned » quand aucun expert OBS n'était choisi. | « Unassigned » si aucune organisation n'a de personne, « n/m assigned » si certaines n'en ont pas. | DEC-087 |
| Vue Document › sélecteur de nature (Nature Picker) | « {Nature} ▾ » au survol, infobulle « Reclassify this block ». | Bordure pointillée orange si la nature vient de l'IA sans confirmation (« Nature proposed by the AI with {niveau} confidence, not confirmed yet — pick it to confirm, or change it ») ; re-choisir la même nature la confirme (« {ID} — nature confirmed: {nature} »). Inerte pour un contributeur (« Set by the project manager »). | DEC-073, DEC-120, DEC-086 |
| Vue Document › comparaison des versions (Document Reading View) | Mode « Compare » : tous les documents, différences inscrites dans les données, étiquettes fixes « Added in v2.1 » / « Modified ». | Onglet Changes : un document à la fois, en-tête « vA → vB · {note} » (ou « vX — only version »), différences mot à mot calculées, étiquettes « Added in vX » / « Modified in vX ». Une exigence supprimée s'affiche « Removed in vX — {ancien texte} », seulement dans la plage comparée ; chaque section porte « +a · ~m · -r changes in this section ». | DEC-070, DEC-119 |
| Panneau pendant la comparaison | En mode Compare, une exigence changée ouvrait une fiche de changement (voir Retiré). | Le détail reste celui de l'exigence ; il s'ouvre une fois sur l'onglet Versions quand on arrive depuis l'onglet Changes. | DEC-119, DEC-072 |

### Retiré

| Zone › élément | Ce qui disparaît, et ce qui le remplace s'il y a lieu | Réf. |
|---|---|---|
| En-tête › pastille « v2.1 active » (Version Pill) | Le bouton de version du tender (infobulle « Switch version »). Les versions sont maintenant par document : colonne Changes, onglet Changes, onglet Versions. | DEC-069 |
| En-tête › « Modified 12 min ago » | La mention fixe de dernière modification et son infobulle nominative. Rien ne la remplace. | — |
| En-tête › bouton « Finalize allocation » et sa fenêtre (Finalize / Export Modal) | Le bouton vert, la fenêtre « Finalize allocation » (« Export requirements register (.xlsx) », « Send to assigned experts », « ✓ Finalize allocation »), le refus « Review milestone not reached — … » et les toasts de clôture. Chaque exigence part vers Compliance quand on la valide ; le registre s'exporte par « Export ▾ ». | DEC-084 |
| En-tête › mode « Compare » et sa barre (Compare Bar) | Le bouton « Compare » et la barre « Compare [vA] → [vB] », avec des listes inertes et « +1 added · ~2 modified · −1 removed » et « Change 1/3 ‹ › » écrits en dur. Remplacés par l'onglet Changes de la vue Document. | DEC-119 |
| Barre de statut › pastille « awaiting manual allocation » (Turnkey) | Un système sans modèle est simplement Incomplete et compte comme tel. Le champ du même nom quitte aussi le filtre avancé. | DEC-103 |
| Barre de statut › bande « J/K navigate · V validate · A assign » | L'aide clavier permanente, à droite de la barre en vue Review. Remplacée par l'icône clavier de la barre d'outils. | — |
| Tableau › colonne « TK OBS » | La colonne de l'aiguillage Turnkey : système visé et %, ou « — » hors Turnkey, avec des infobulles « Pass 1 — … ». Remplacée par la confiance affichée dans System. | DEC-077 |
| Tableau › bouton « ▾ » de reclassement (Row Reclassify Button) | Le petit « ▾ » affiché au survol de la cellule Requirement (lignes d'exigence et d'information). La nature se corrige dans le détail ou en vue Document. | DEC-074 |
| Tableau › saisie du verdict | Les listes de verdict des sous-lignes système et organisation, leurs toasts (« {système}: compliance set to … », « … final verdict stays locked at … ») et le verrou « 🔒 » du verdict de l'exigence. | DEC-039, DEC-028 |
| Tableau › choix de l'expert (OBS) | Les listes « expert » des sous-lignes et les toasts « {système}: expert — … » / « {système}: manager — … ». Il reste une seule personne par organisation, dans Assigned to. | DEC-087, DEC-054 |
| Carte flottante « AI got this wrong with high confidence » (AI Feedback Panel (Why Box)) | Elle s'ouvrait en bas à droite quand on remplaçait une équipe OBS proposée par l'IA à 85 % ou plus, et demandait une raison (puces, « Other reason (optional)… », « Send »). La correction reste enregistrée, sans question. | DEC-054 |
| Vue Document › passages masqués pour un contributeur | Les passages hors de son périmètre ne sont plus remplacés par une bande hachurée « Restricted », ni retirés : tout le texte se lit. | DEC-012 |
| Vue Document › compteurs de changements du navigateur | Les compteurs « +1 ~2 -1 » à côté des sections (affichés en permanence) et le point « Changed in v2.1 » des exigences (en mode Compare). Les changements se lisent dans l'onglet Changes. | DEC-119 |
| Panneau en mode Compare › fiche de changement (Change Card) | La pastille « Change v2.0 → v2.1 », les boutons « New » / « Reviewed, no impact » / « Action required », « Affected passage » et « ＋ Create action / reminder ». Remplacée par l'onglet Versions et le panneau d'exigence supprimée : un changement n'a plus d'état « traité » propre. | DEC-072 |

### Libellés

| Où | Avant | Maintenant |
|---|---|---|
| Tableau › infobulle de la pastille Status | « Allocated — sent to Expert Review » ; « … — Click to validate — sends to Expert Review » | « Allocated — sent to Compliance » ; « … — Click to validate — sends to Compliance » |
| Tableau › sous-ligne, infobulle de l'état d'avancement | « In Expert Review » | « In Compliance » |
| Tableau › sous-ligne d'un système sans modèle | « manual » ; « This activity has no allocation model — … » | « no model » ; « This system has no allocation model — … » |
| Tableau › sous-ligne, organisations | « N teams allocated within this activity » ; « N teams within this activity — expand to see each » | « N teams allocated within this system » ; « N teams within this system — expand to see each » |
| Tableau › ligne à plusieurs systèmes, OBS | « This requirement has N parallel allocations — expand to see experts per branch » | « This requirement has N parallel allocations — expand to see the team per branch » |
| Tableau › étiquette de système proposé | « Proposed change — pending project-manager review » | « {système} — proposed change, pending project-manager review » |
| Tableau › regroupement par système (Grid Section / Group Header) | « NO TYPOLOGY » ; « Activity not set » ; « {système} perimeter » | « NO SYSTEM » ; « System not set » ; « {système} » |
| Tableau › motifs To review (infobulle de la pastille ; voir le panneau de détail) | « Type is AI-detected, unconfirmed » ; « Class is AI-detected, unconfirmed » ; « Activity is AI-detected, unconfirmed » | « Nature proposed by the AI with low confidence » ; « Class proposed by the AI with low confidence » ; « System is AI-detected, unconfirmed » |
| Filtres › « Review field » | « Type », « Activity » | « Nature », « System » |
| Filtres › « Allocation level » | « Branches — multiple activities » | « Branches — multiple systems » |
| Barre d'actions groupées › infobulle de « Move to Information » | « Reclassify the selected rows as Information — they disappear from this table, which lists requirements only » | « Reclassify the selected rows as Information — they leave allocation (no status, no system) and stay as information rows » |
| Menu « Export ▾ » › étapes | « Characterization » — « Class, typology, type and status » ; « Allocation » — « Managers and expert assignments » | « Characterisation » — « Nature, class, system and status » ; « Allocation » — « ABS / PBS / OBS and who is assigned to each » |
| Vue Document › confirmation du passage en Information | « {ID} already has an expert's answer recorded. Switching it to Information permanently deletes that work — … » | « {ID} already has a contributor's answer recorded. Switching it to Information permanently deletes that work — … » |

### Style visuel

- **Icônes.** Un jeu d'icônes SVG au trait, qui prend la couleur du texte, remplace les emoji et les glyphes : « ⬇ » Export, « ⏷ » Filter et entonnoirs, « ▤ » View, « ⬆ » Add a document, « 📄 » documents, « 💬 » commentaires, « 📷 » image source, « 🔒 » image verrouillée, « ⎘ » Duplicate, « 🗑 » Delete, « ⑂ » nombre de systèmes, « ▸ » chevrons, « 🌐 » note de langue de l'export, « ⤵ » note du filtre avancé. Nouvelles icônes : clavier, et œil du bandeau.
- **Pastilles de statut** sans point coloré initial. « Reassignment requested » prend le même violet (`--human`) que « To validate ».
- **Couleur partenaire** turquoise #1b9aaa (`--partner`, hors échelle de jetons suivie).
- **Colonne Changes.** Mots retirés barrés sur `--warn-soft`, ajoutés sur `--ok-soft`. Étiquettes de version ambre (`--ia`), « New » vert ; le badge de l'onglet Changes et le rail sont ambre.
- **Largeurs par défaut.** System passe de 112 à 136 px, PBS de 100 à 150 px ; Changes fait au moins 280 px et une colonne personnalisée 150 px. Les poignées de redimensionnement restent invisibles jusqu'au survol de l'en-tête et passent en accent pendant le glissement.
- **Jauge « % allocated ».** 64 × 6 px, remplissage `--ok` sur `--panel-3`.
- **Filtre avancé.** Les boutons « Apply » (vert plein) et « Cancel » (contour) sont enfin mis en forme, et les lignes d'aide passent en petit gris : ils s'affichaient sans style.
- **Détails.** Les cellules texte (ABS, colonnes personnalisées) se terminent par « … » ; les numéros de section du navigateur ne chevauchent plus les titres.

### Points incertains

- La jauge « % allocated » promet en infobulle « characterisation and every system validated », mais elle compte les pastilles « Allocated ». Pour le chef de projet sur Turnkey, c'est l'aiguillage validé ; sur une exigence à plusieurs systèmes hors Turnkey, la seule caractérisation suffit (à vérifier).
- Un contributeur peut encore changer les systèmes d'une de ses exigences, par la cellule System ou « Assign › System », alors que nature et classe lui sont fermées (DEC-086). La règle produit pour le système est à confirmer (à vérifier).
- Sur Turnkey, la validation groupée (bouton « Validate », ou V avec une sélection) lancée par un contributeur semble valider l'aiguillage de niveau Turnkey plutôt que son système (lu dans le code, à vérifier dans le navigateur).
- Sur un tender à référentiel, l'en-tête OBS dit « OBS · role » mais son infobulle parle encore de « team or service ».
- Vue Document : les exigences capturées depuis une ligne de tableau gardent l'ancien type dans leur puce (« Interface · To review »), contrairement aux paragraphes (« Requirement · … »).
- La recherche trouve encore l'ancien type (« Functional », « Performance »…), qui ne s'affiche plus nulle part.
- Trié par Status, « Reassignment requested » passe après « Allocated ».
- Le point « To review » du navigateur suit le statut de caractérisation, pas celui de la pastille (Turnkey, systèmes).
- Le rail « Changes » du navigateur replié n'apparaît qu'en vue Document, pas en vue Review.

## Allocation — panneau de détail et modèle d'allocation

`revue-documentaire.html` · route `#review` — le panneau ouvert sur une exigence, et les statuts · captures : [avant](captures/04-allocation-panneau-avant.png), [maintenant](captures/04-allocation-panneau-apres.png)

**En bref.** Le panneau ne parle plus de « Manager » ni d'« Expert » : une allocation, c'est une organisation (OBS) et sa personne, montrées en cartes « Allocations » avec un seul champ « Assigned to ». S'il manque la personne, on peut quand même valider.
La chaîne se lit désormais ABS → PBS → OBS. L'OBS devient une liste d'organisations (ajout par recherche, ✕ jusqu'à zéro), le PBS un élément produit (listes du classeur de clés sur les produits SIG Mainline), et un bouton « ↻ Re-run » rejoue un modèle d'allocation.
Il n'y a plus qu'une validation, toujours affichée, grisée avec sa raison, accrochée en bas du panneau, et elle envoie à Compliance. Sur Turnkey, le chef de projet valide l'aiguillage vers les systèmes, puis chaque système se valide dans son propre détail, devenu un panneau complet ; sur un tender SIG, le champ System disparaît.
Le contributeur voit tout le tender mais ne modifie que son système (lecture seule ailleurs). Nature et classe sont réservées au chef de projet et affichent le niveau de l'IA (Low / Medium / High).
Disparaissent : le verrou « Final verdict », la carte de suggestion de l'IA, la fenêtre « Why » et la fiche de changement. Le journal d'activité devient un vrai historique, filtrable et partagé avec Compliance.

### Ajouté

| Zone › élément | Ce qu'on voit, ce qui se passe | Réf. |
|---|---|---|
| Panneau › Vue lecture seule du contributeur (Detail / Assignment Panel) | Un contributeur peut ouvrir n'importe quelle exigence. Si aucun de ses systèmes n'y figure, il voit la note « Not assigned to you — read only. » (icône cadenas), Nature et Class en lecture, puis un encadré par système (code) avec ABS, PBS et chaque OBS suivie de sa personne (« · — nobody yet — » si personne). Un partenaire affiche « Partner company — answered outside the tool. », une exigence sans système « No system yet. » ; aucune action dans l'onglet Details (ni validation, ni proposition, ni colonnes personnalisées), mais l'onglet Activity reste ouvert aux commentaires. | DEC-012, DEC-100 |
| Panneau › Ouverture d'un ID absent du tender | Demander l'ouverture d'une exigence qui n'existe pas dans le tender ouvert (par exemple depuis une notification) affiche le toast « This requirement isn't in this tender » au lieu d'un panneau vide. | — |
| En-tête › Lien de paragraphe (Paragraph Reference) | Sous l'ID : « § 2.2.1 » (gras, police mono) puis le titre du paragraphe le plus proche ; infobulle « {chemin} — view in document ». Un clic ouvre la vue Document sur le bloc. | — |
| En-tête › Ligne « ⚠ … » › bouton de nature (Nature Picker) | Dans la ligne de motif d'une nature douteuse, choisir à nouveau la même nature dans « Requirement ▾ » la confirme, avec le toast « {ID} — nature confirmed: Requirement » (avant, ce choix ne faisait rien). Pour un contributeur, le bouton est inactif, infobulle « Set by the project manager ». | DEC-086, DEC-099 |
| En-tête › Onglet « Versions » (Versions Tab) | N'apparaît que si l'exigence a été ajoutée ou modifiée dans la version en vigueur de son document. On y voit « Added in vX » / « Modified in vX », un diff mot à mot (« What changed »), le texte précédent repliable, une phrase d'état et le bouton « Show in the document → » ; le détail relève de l'analyse Versions. | DEC-071, DEC-072 |
| Statuts › « Reassignment requested » (Status Pill (Requirement Workflow State)) | Nouveau statut d'exigence, pastille violette (`--human` sur `--human-soft`), seulement sur Turnkey et côté chef de projet : un système a demandé une réaffectation ou proposé un système manquant. Tant qu'il dure, le bouton d'aiguillage est grisé avec « A system asked for a reassignment — approve or reject it first. » | DEC-104 |
| Nature / Class › Niveau de l'IA (Confidence Level Badge) | Petite pastille « High », « Medium » ou « Low » à côté du libellé Nature et du libellé Class, tant que la valeur affichée est celle de l'IA. Elle passe en ambre gras quand l'appel n'est pas confirmé (Low, cause du To review), infobulle « Proposed by the characterisation model — low confidence, not confirmed yet: to review. This model gives a level, not a percentage. » ; elle disparaît dès qu'une personne change la valeur. | DEC-120 |
| Turnkey (chef de projet) › Liste « System » › ✕ | Chaque système porte un ✕ « Remove this system », le dernier compris. Sans système, la liste affiche « No system yet » et l'allocation repasse Incomplete. Toast « {CODE} removed » ou « {CODE} removed — no system left », avec confirmation si le système a déjà une réponse. | DEC-076 |
| Turnkey (chef de projet) › Partenaires | Les entreprises partenaires du tender s'ajoutent comme des systèmes à part : étiquette sarcelle, infobulle « {Nom} — added for this tender, not part of the Turnkey model. The AI never predicts it; the partner works outside the tool. », et dans la recherche « + Add system » elles sont listées en dernier sous « Added for this tender — not in the model ». | DEC-082 |
| Turnkey (chef de projet) › Carte et détail d'un partenaire | La carte n'a pas de statut et dit « {Nom} · outside the tool — the project manager enters its verdict in Compliance ». « Open system detail → » ouvre un encadré « A partner company, added for this tender. » (pas d'ABS / PBS / OBS ni de personne ; filtrer la table sur le code, exporter, saisir le verdict dans Compliance), suivi de « Propose a change ». | DEC-082 |
| Modèle › « ↻ Re-run ▾ » (Re-run Control) | Le bouton se trouve dans l'en-tête du bloc du modèle, dès qu'un seul système est en jeu. Son menu montre « This system's models », puis « Borrow another system's model » (« SIG Urban », « SIG Mainline Wayside », « SIG Mainline Onboard », « RST Metro », « RST High speed »). Il rejoue ABS, PBS et toutes les OBS, jamais les personnes ; toast « {ID} — re-derived with {produit} », aucun toast si le résultat est identique. | DEC-040 à DEC-043, DEC-056, DEC-091 |
| Modèle › Re-run bloqué | Le bouton reste visible mais grisé, sans menu : « ↻ Re-run », infobulle « Cannot re-run — an answer has been recorded. » ou « Cannot re-run — a verdict has been recorded. » Une question en cours avec le client ne bloque pas. | DEC-041, DEC-089 |
| Modèle › Proposition de relance (Re-run Prompt) | Après un changement de nature ou de classe, une barre pleine couleur s'affiche au-dessus d'ABS : « ↻ Re-run the model » et, à droite, « class changed » ou « nature changed » (l'infobulle rappelle l'état au moment du calcul et nomme le produit relancé). Variantes sans bouton : « Class changed · re-run blocked » et « Class changed · check ABS / PBS / OBS by hand » (système sans modèle), ou « Nature changed · … ». Rien n'est relancé automatiquement. | DEC-075 |
| OBS › Ajout d'une organisation par recherche (OBS List) | « + Add organisation » ouvre un champ « Name the organisation… » avec, dessous, les organisations déjà utilisées sur le tender (« Used on this tender ») ; dès qu'on tape un nom nouveau, « Add “{texte}” » (« New organisation ») passe en tête. ↑/↓, Entrée, Échap ou ✕ « Cancel (Esc) » ; toast « {organisation} added ». | DEC-055 |
| OBS › ✕ sur chaque organisation (OBS List) | Chaque ligne a son ✕ « Remove this organisation », la dernière comprise : la liste affiche alors « No organisation yet » et le système repasse Incomplete (toast « {organisation} removed — no organisation left »). L'organisation part avec sa personne. | DEC-076 |
| Clés (tender SIG de produit Mainline Wayside / Onboard) › ABS et PBS | ABS devient une liste déroulante des 16 catégories du classeur, avec « — Not derived yet — » en tête. PBS devient une liste groupée par famille (groupes « From another product's model » et « Other » au besoin), avec l'icône « i » « The product element the requirement bears on — from the PBS key, grouped by family. » | DEC-061, DEC-062 |
| Clés (tender Mainline) › OBS en rôles | Le libellé devient « OBS · role », le bouton « + Add role », et la recherche « Search a role, or a code (e.g. TIS03)… » range les rôles sous « Under {ABS} » puis « Other roles on this product », chacun avec ses codes en police mono. Aide : « The role(s) — job positions from the OBS key, listed under the ABS chosen above. A position, not a person: who fills it is assigned below. » ; liste vide : « No role matches — the list is the product's OBS key. » | DEC-062 |
| Validation › Note « personne manquante » (Validate Zone) | Sous un bouton de validation actif s'affiche « No one assigned yet — you can still validate; the system's contributors can answer. » ou « {k} of {m} organisations with no one assigned — you can still validate; … » (sur une ligne de « Validate per system », la note s'arrête à « … you can still validate. »). Le texte est gris et informatif ; il ne grise jamais le bouton. | DEC-025 |
| Validation › Raison sous le bouton grisé (Validate Zone) | Un bouton qui ne peut pas servir reste affiché, grisé, avec sa raison dessous et en infobulle : « Characterisation incomplete — set its nature and class first. », « Allocation incomplete — complete ABS / PBS / OBS first. » ou « A system asked for a reassignment — approve or reject it first. » | DEC-084 |
| Validation › « Validate per system » (Validate Zone) | Exigence à plusieurs systèmes hors Turnkey : un encadré « Validate per system » avec une ligne par système (étiquette, petit bouton « ✓ Validate & send » ou « ✓ Allocated — sent » en vert, raison ou note de personne manquante sur la même ligne). Valider un système valide aussi la caractérisation. | DEC-099 |
| Validation › Zone accrochée en bas (Validate Zone) | La zone suit directement les données qu'elle confirme. Si cet endroit est sous le bas de l'écran, elle reste collée en bas du panneau (fond et filet supérieur) ; une fois validée, elle redevient une simple ligne d'état. | — |
| Colonnes personnalisées › Champs du panneau (Custom Fields Panel Section) | Dans la vue « SIG » du chef de projet et dans la vue contributeur, un champ par colonne personnalisée (texte, liste ou puces à choix multiple), sous un séparateur. Mention : « Custom columns — entered by people. The AI never fills them, and they never put a requirement into review. » | DEC-064, DEC-067 |
| Confirmations › Retrait d'un système déjà répondu | Confirmation du navigateur : « {CODE} already has a recorded answer. Removing the system permanently deletes that work — this can't be undone. Continue? » (✕ Turnkey ou dernier système décoché). En décochant un système qui n'est pas le dernier : « {Système} already has a contributor's answer recorded on this requirement. Removing it permanently deletes that work — this can't be undone. Continue? » | DEC-076 |
| Confirmations › Retrait d'une organisation déjà répondue | « This organisation already has a recorded answer. Removing it permanently deletes that work — this can't be undone. Continue? » (« role » sur un tender à clés). | DEC-076 |
| Activity › Filtre par catégorie (Activity Timeline) | Des puces au-dessus du journal : « All », « Status N », « Allocation N », « Compliance N », « Comments N ». La puce active est pleine ; si la catégorie est vide : « Nothing in this category yet. » | — |
| Activity › Jalons | Quatre moments sont marqués comme des stations sur la ligne : « Captured », « Allocated », « Answered », « Declared to the client » (nom en police de titre au-dessus de l'entrée). | — |

### Modifié

| Zone › élément | Avant (8 sept.) | Maintenant | Réf. |
|---|---|---|---|
| Panneau › Choix de la vue (Detail / Assignment Panel) | Deux cas : la vue Turnkey du chef de projet, sinon un panneau commun au chef de projet et au contributeur, avec des champs conditionnels. Un contributeur ne voyait que ses exigences. | Quatre vues : chef de projet sur Turnkey (aperçu, puis détail d'un système), vue « SIG » du chef de projet sur les autres tenders, vue du contributeur sur son système, lecture seule partout ailleurs. | DEC-100, DEC-101 |
| Panneau › Vue « SIG » du chef de projet (hors Turnkey) | Carte de suggestion IA, « Classification », « Activity », « Final verdict », bloc « Pass 2 » (PBS, ABS, sans OBS), « Allocations » par système, « Source section », validation. | Nature, Class, « System » (seulement hors SIG), bloc « {Ligne}'s model » avec « ↻ Re-run ▾ », ABS, PBS, liste OBS, « Allocations (N) » par organisation, « Assigned to » si aucun système, validation, colonnes personnalisées, « Source section » si besoin. | DEC-060, DEC-074 |
| Panneau › Vue contributeur sur son système | Mêmes champs que le chef de projet, presque tous modifiables (« Classification », « Activity · your allocated activity », chaîne, « OBS · team », bloc « Manager »), puis « Propose a change » et validation. | Ordre fixe : Nature et Class en lecture (« Set by the project manager »), « {Système}'s model » + « ↻ Re-run ▾ », ABS, PBS, liste OBS, « Allocations (N) », demande de réaffectation à traiter, validation de son système, colonnes personnalisées, « Propose a change », « Source section ». Il modifie ABS, PBS, organisations et personnes de son système, relance le modèle et valide son système, mais ne change ni nature, ni classe, ni liste des systèmes. « Son système » = celui dont il est membre, qu'il y soit assigné ou non. | DEC-086, DEC-102, DEC-104 |
| Panneau › Turnkey (chef de projet) › Aperçu | Nature, « Type », PBS ou ABS de passe 1, liste « Activity », « Activities (N) », « Source section », puis « ✓ Validate characterisation ». | Nature, Class (avec niveau IA), PBS ou ABS de passe 1, liste « System », validation de l'aiguillage, « Systems (N) ». Plus de « Source section » ; les colonnes personnalisées n'y figurent pas non plus. | DEC-104 |
| Panneau › État vide | « N/M requirements allocated · K to assign. » : K comptait les exigences sans affectation OBS. | Même texte ; K compte les exigences dont au moins une organisation n'a pas de personne (ou sans système ni personne). | DEC-123 |
| En-tête › Pastille de statut (Status Pill (Requirement Workflow State)) | Statut de l'exigence pour tout le monde ; un titre ou une information pouvait afficher « To review ». | Contributeur : statut de son système, infobulle « Your status on this system ». Chef de projet Turnkey : statut du niveau Turnkey. Titre ou information : aucune pastille. Toujours non cliquable. | DEC-073, DEC-104 |
| En-tête › Ligne « ⚠ … » (motif To review) | Aussi pour un titre ou une information (« Type is AI-detected, unconfirmed — reclassify to resolve: … »). | Exigences seulement. Pour un contributeur, c'est le motif de son système (ex. « Weak OBS derivation (61%) — the proposed assignment may be wrong »). | DEC-073 |
| En-tête › Onglet « Translation » | Toujours présent, même sur un tender en anglais (« This tender's source language is English — there is no translation to correct. »). | Masqué quand la langue source est l'anglais. Dans « Read in », la langue originale (« {Langue} — original ») vient en premier et est donc présélectionnée, avant « English — working text ». | — |
| Statuts › Exigence : quand chaque statut apparaît | Incomplete (rouge `--warn`) : classe ou système (« Activity ») manquant, ou OBS non choisie. To review (ambre `--ia`) : type, classe ou système non confirmés, dérivation faible, marquage en masse. To validate (violet `--human`). Allocated (vert `--ok`) : validé, « sent to Expert Review ». | Mêmes quatre, plus « Reassignment requested » (violet, Turnkey). To review : nature ou classe proposées en Low, système non confirmé, ABS/PBS/OBS sous 75 %, exigence changée dans la version en vigueur, marquage en masse. Allocated : validé et envoyé à Compliance ; pour le chef de projet Turnkey, aiguillage validé. | DEC-073, DEC-104, DEC-120 |
| Statuts › Exigence à plusieurs systèmes (hors Turnkey) | Statut de caractérisation, puis « Allocated » une fois la caractérisation validée (premier clic). | Même règle, mais la caractérisation est validée avec le premier système : la pastille passe à « Allocated » dès qu'un système est validé, les autres se lisant dans « Validate per system ». | DEC-099 |
| Statuts › Conditions d'Incomplete | Incomplete tant que « OBS · team » (ou l'« Expert » du système) restait sur « — Unassigned — », ou si PBS, ABS et OBS étaient vides. | Caractérisation : classe ou système manquant. Allocation : aucune organisation (OBS) renseignée, ou ABS, PBS et OBS tous vides — retrait de la dernière organisation ou du dernier système, système Turnkey sans modèle (il part vide), information reclassée en exigence. Une organisation sans personne ne rend plus rien Incomplete : « Unassigned » / « n/m assigned » et la note sous le bouton le signalent. | DEC-025, DEC-076, DEC-103 |
| Statuts › Statut d'un système (Turnkey System Card) | Pastille à trois états calculée sur les équipes : « Not started » (gris), « In progress » (ambre), « Allocated » (vert). | Statut d'allocation du système, avec les quatre libellés et couleurs de l'exigence (Incomplete / To review / To validate / Allocated), dans le coin droit de la carte, non cliquable, infobulle « This system's allocation status » ; aucun statut pour un partenaire. To review vient ici d'une dérivation ABS/PBS/OBS sous 75 %. | DEC-103 |
| Statuts › Avancement par organisation (cartes Allocations) | Une pastille par système : « Proposed », « Assigned », « Awaiting answer » (gris), « Awaiting Q&A » (accent), « Reassignment needed » (rouge), « Answered » (vert). | Mêmes libellés et couleurs, mais une pastille par organisation. | DEC-060 |
| Statuts › Conformité en lecture (Compliance Pill) | Quatre valeurs (« Compliant », « R&D Needed » en ambre, « Not Compliant », « Pending »), variante verrouillée 🔒, verdict de l'exigence en tête des Allocations. | Trois valeurs : « Compliant » (vert), « Not Compliant » (rouge), « Pending » (pointillés, gris italique). Dans le panneau, ne subsistent que la ligne « Compliance » des cartes systèmes Turnkey (infobulle « Derived from this system's teams — most restrictive wins ») et l'avancement de chaque organisation. | DEC-031, DEC-039 |
| Champs › Nature (Nature and Class Fields) | Champ « Nature » seulement dans la vue Turnkey du chef de projet ; ailleurs, un titre ou une information avait un champ « Type » (même liste) et une exigence aucun. | Champ « Nature » (Heading / Information / Requirement) dans toutes les vues, avec le niveau de l'IA. Liste déroulante pour le chef de projet ; pour un contributeur, texte en lecture et « Set by the project manager ». Plus de bouton « Confirm » : c'est la validation de l'exigence qui confirme. | DEC-074, DEC-086, DEC-099 |
| Champs › Class (Nature and Class Fields) | « Classification » (Technical / Non-technical), modifiable par tous, suivie de « Technical requirement — routed through the PBS allocated activity. » ou « Non-technical requirement — routed through the ABS allocated activity. ». Dans la vue Turnkey : « Type · AI, unconfirmed ». | « Class » partout, avec une option grisée « — Not set — » tant qu'aucune classe n'est choisie. Lecture seule pour un contributeur ; la ligne d'aide disparaît. | DEC-074, DEC-086 |
| Champs › Système (tenders ni Turnkey ni SIG) (Multiselect Dropdown) | « Activity · AI-detected, unconfirmed », liste à cocher « Select activities… », visible du chef de projet hors Turnkey (SIG compris) et de tout contributeur sans système à lui sur l'exigence. | « System · AI-detected, unconfirmed », « Select systems… », pour le chef de projet seulement et masqué sur un tender SIG. Décocher un système retire aussi son allocation (confirmation s'il y a une réponse) ; le dernier peut partir (Incomplete). | DEC-044, DEC-076 |
| Turnkey (chef de projet) › Liste « System » (UI List) | Liste « Activity » : code, nom, %, puis « has a model » ou « manual », où « manual » voulait dire « pas de modèle ». | « has a model » seulement si le système a un modèle. Ensuite, soit le % du modèle Turnkey (ambre sous 75 %, infobulle « Proposed by the Turnkey model — N% confidence that this is the right system »), soit « manual » : ajouté à la main (« Added by hand — not proposed by the Turnkey model »). | — |
| Turnkey (chef de projet) › « + Add system » | « + Add activity » ouvrait le formulaire de proposition, absent de cette vue : le clic ne faisait rien. | Ajout direct : champ « Search a system… » (code et nom), ↑/↓, Entrée, Échap ; « No system matches. » ou « Every system is already on this requirement. » Toast « {CODE} added » ; le système arrive sans dérivation, donc Incomplete. | DEC-076 |
| Turnkey (chef de projet) › Champ de passe 1 (PBS si la classe est technique) | Liste à 5 valeurs (Functional, Performance, Security, Interface, Regulatory). | Texte libre « Product element ». Le % n'apparaît que s'il y a une valeur. | DEC-062, DEC-074 |
| Turnkey (chef de projet) › Validation de l'aiguillage (Validate Zone) | En fin de panneau, « ✓ Validate characterisation », puis « Characterisation allocated — each allocated activity below validates its own allocation individually. » | Juste sous la liste des systèmes : « ✓ Validate & send to the systems », puis « ✓ Routing validated — sent to the systems » (grisé). Toast « {ID} routing validated — sent to its systems ». | DEC-104 |
| Turnkey (chef de projet) › Cartes systèmes (Turnkey System Card) | « Activities (N) » : lignes « OBS · team » (liste), « Manager / expert » (noms joints par « · »), « Compliance », bouton « Open activity detail → ». | « Systems (N) » : statut du système en coin, puis une ligne par organisation (organisation à gauche, personne à droite ; « No organisation yet » et « Unassigned » en gris italique ; % ambre si l'OBS est faible), ligne « Compliance », bouton pleine largeur « Open system detail → ». | DEC-060, DEC-103 |
| Turnkey (chef de projet) › Détail d'un système | « ← All activities », résumé en lecture (« Pass 2 — {système}'s own model » : Type, Specialty, PBS, ABS, OBS · team ; « Assigned to » avec « · manager … »), bloc « Raise a problem ». | Même panneau que sur un tender SIG, appliqué au système ouvert : « ← All systems », Nature, Class, bloc « {Système} » + « ↻ Re-run ▾ », ABS, PBS, liste OBS, « Allocations (N) », « ✓ Validate & send to Compliance », « Propose a change ». | DEC-101 |
| Modèle › Bloc de dérivation (Derivation Chain) | Pastille « Pass 2 » + « {x}'s model », ordre PBS → ABS → OBS. Sur Turnkey, le contributeur avait au-dessus un bloc « Pass 1 — Distribution across activities » et une flèche « routes into ». | En-tête « {Ligne}'s model » (vue SIG), « {Système} » (détail Turnkey) ou « {Système}'s model » (contributeur), avec la relance. L'ordre devient ABS → PBS → OBS ; plus de bloc de passe 1 hors de l'aperçu du chef de projet. | DEC-008 |
| Modèle › ABS | Deuxième champ, texte libre, aide « Derived from the PBS above — correcting the PBS clears this and the OBS. ». Le modifier effaçait l'OBS. | Premier champ : texte libre (« Fill in by hand » quand c'est la chaîne d'un système) ou liste sur un tender à clés. Le modifier efface PBS et OBS, toast « ABS changed — PBS and OBS cleared, they were derived from it ». | DEC-008 |
| Modèle › PBS | Premier champ, liste « Functional / Performance / Security / Interface / Regulatory ». Le modifier effaçait ABS et OBS. | Deuxième champ, élément produit : texte libre « Product element » ou liste par famille sur un tender à clés. Le modifier efface l'OBS (« PBS changed — OBS cleared, they were derived from it »), sinon « PBS updated ». | DEC-062, DEC-074 |
| Modèle › OBS (OBS List) | Une liste déroulante « OBS · team » d'équipes avec leur personne (« — Unassigned — » en tête), suffixe « · your allocated activity » pour le contributeur. Cachée au chef de projet dès qu'il y avait un système. | Une liste d'organisations, sans personnes, chacune avec son % (ambre sous 75 %) et son ✕, plus « + Add organisation ». Visible aussi du chef de projet quand un seul système est en jeu. Aide : « The organisation(s) — the team or service within the system. This is what casting staffs, not a person to pick here. » | DEC-054, DEC-055 |
| Allocations › Cartes (Allocated-Activity Detail Card) | Chef de projet : « Allocations (N) », une carte par système (étiquette + statut), champs « Manager » (tous les managers) et « Expert » (équipes-personnes). | Une carte par organisation : son nom en tête, son avancement, un champ « Assigned to » limité aux membres du système (« {Nom} — {rôle} », plus la personne en place). Étiquette système seulement s'il y a plusieurs systèmes ; N = nombre d'organisations, avec « · each organisation answers for itself, and the verdicts consolidate — most restrictive wins, pending until all have answered » si N > 1. Même bloc dans la vue contributeur et dans le détail Turnkey. | DEC-060, DEC-087, DEC-102 |
| Personne › Exigence sans système (Manager Assignment Card) | Bloc « Manager · handles this requirement » (ou « · handles your allocated activity ») : carte avatar et rôle avec « Change » au survol, ou « No manager assigned » / « Nobody handles this requirement yet » + « Assign » ; édition par liste + « Done ». | Bloc « Assigned to · responsible for its compliance », seulement quand l'exigence n'a aucun système (chef de projet, hors Turnkey) : nom ou « — Unassigned — », bouton « Assign » / « Change », puis recherche « Search a person… » dans l'annuaire (« No match in the directory. »). Toast « Assigned to {Nom} ». | DEC-087 |
| Réaffectation › Formulaire de demande (Propose / Reassign Form) | Remplaçant choisi dans une liste fixe de couples équipe-personne ; la demande visait le système du lecteur, ou le premier. | Remplaçant choisi par son nom parmi tous les contributeurs. Dans un détail Turnkey, la demande vise le système ouvert ; « ↩ Request reassignment » est grisé (« Already flagged for reassignment ») dès qu'une demande existe. | DEC-087 |
| Réaffectation › Carte à approuver | « ↩ Reassignment requested by {nom} (expert) » sur la carte du système ; approuver « wrong person » changeait l'expert. | « … (contributor) », sur la première carte d'organisation du système. Approuver « Right system, wrong person » met le remplaçant sur les organisations que tenait le demandeur. Comme avant, aucune carte à approuver dans les vues Turnkey du chef de projet. | DEC-087 |
| « Propose a change » (Propose / Reassign Form) | Petits boutons « ↩ Request reassignment » / « + Missing activity » ; le détail d'un système Turnkey avait sa propre copie « Raise a problem ». | Gros boutons sur fond accent pâle, « ↩ Request reassignment » / « + Missing system », un seul bloc partout, y compris dans le détail d'un système Turnkey, où il agit sur ce système. | DEC-045 |
| Validation › Exigence à un système (Validate Zone) | Deux clics : « ✓ Validate characterisation V » puis « ✓ Validate & send to Expert Review V ». Le bouton restait actif ; sur Incomplete, le clic donnait le toast « Nothing to validate yet — fill this in first ». | Un seul « ✓ Validate & send to Compliance », qui confirme aussi ce que l'IA a détecté ; grisé avec sa raison si l'exigence est incomplète. Ensuite « ✓ Allocated — sent to Compliance » (grisé). Toast « {ID} allocated — sent to Compliance » (avant : « … sent to Expert Review »), avec « Undo ». | DEC-084, DEC-099 |
| Validation › Contributeur | Validait l'exigence (caractérisation puis allocation). | Valide son système : « ✓ Validate & send to Compliance » selon le statut de son système. Sur une exigence d'un autre système, la validation est refusée (« Not your system — read only »). | DEC-100, DEC-104 |
| « Source section » | Toujours en bas : « {n}. {titre} · View in document → ». | Affiché seulement quand l'en-tête n'a pas de lien de paragraphe. | — |
| Activity › Récapitulatif des rôles (Role Recap Card) | Trois lignes fixes : « Admin », « Manager », « Expert » (« To assign » si vide). | « Admin », puis une ligne « Assigned to » par personne présente sur les organisations, et « To assign — {k} of {m} organisations » (ou « To assign ») s'il en manque. | DEC-087, DEC-123 |
| Activity › Journal (Activity Timeline Entry) | Quelques entrées fixes de démonstration et les traces locales de l'écran, sur un fin trait gris. | Historique de l'exigence partagé avec Compliance : chaque changement de nature, de classe, de statut, d'ABS/PBS/OBS ou de personne, système par système, avec auteur, « avant → après » (ancien barré en rouge, nouveau en vert), heure « Today, HH:MM » et catégorie. S'y ajoutent la capture (« Captured from {document} and typed {Nature} ») et les versions du document (« New document version »). | — |
| Activity › Commentaire (Comment Composer) | « Comment… @ to mention » incrémentait le compteur de l'onglet sans rien ajouter au fil. | Le commentaire apparaît dans le journal, entre guillemets, catégorie Comments. | — |
| Exigence supprimée (Removed Requirement Panel) | Fiche de changement : « EXG-00X », « Change v2.0 → v2.1 », boutons « New / Reviewed, no impact / Action required », « Affected passage », « ＋ Create action / reminder ». | « Removed » + pastille « Removed in vX », texte précédent en titre, « {document} — present in vA, gone from vB », « Text in vA », note « No longer part of the tender… ». Lecture seule (détail : analyse Versions). | DEC-072, DEC-119 |
| Exigence changée ouverte depuis les changements | Ouvrait la fiche de changement à la place du panneau. | Ouvre le panneau normal, directement sur l'onglet « Versions » (une fois par sélection). | DEC-119 |

### Retiré

| Zone › élément | Ce qui disparaît, et ce qui le remplace s'il y a lieu | Réf. |
|---|---|---|
| En-tête › Badge « 🔀 N assignments » | Badge du chef de projet sur une exigence à plusieurs systèmes ; le nombre se lit dans « Allocations (N) ». | — |
| Détails › Carte « ✦ AI Suggestion — needs confirmation » (AI Suggestion Card) | « Proposed assignment: … » avec « Accept assignment » / « Reject » (toasts « AI assignment accepted », « Suggestion rejected — manual assignment required ») : l'IA ne propose plus de personne. Seule reste la carte « ⚠ Uncertain segmentation ». | DEC-054 |
| Fenêtre « Why » (AI Feedback Panel (Why Box)) | Carte flottante en bas à droite après le remplacement d'une OBS proposée avec forte confiance (depuis le panneau ou la cellule OBS du tableau) : « AI got this wrong with high confidence », raisons en puces, « Other reason (optional)… », « Send », « Feeds future model training only — nothing changes in this session. ». Rien ne la remplace. | DEC-054 |
| Détails › Bloc « Final verdict » | Verdict consolidé avec « Lock » / « Unlock » (chef de projet), mention « tree now says … », note « Locked — contact the project management team to change it » côté contributeur, toasts de verrouillage. Le verdict ne se gère plus que dans Compliance. | DEC-028 |
| Détails › Champ « Activity · your allocated activity » | Code et nom du système du contributeur, en lecture ; remplacé par l'en-tête « {Système}'s model ». | — |
| Détails › « ✓ Confirm AI activity » et note Turnkey | Bouton vert sous la liste des systèmes, et encadré « Turnkey. Supervises the whole scope — needs a coordinating owner plus one specialist per perimeter. ». Valider l'exigence confirme ce que l'IA a détecté. | DEC-099 |
| Chaîne › Bloc « Pass 1 — Distribution across activities » | Vu du contributeur sur Turnkey : dimension lue (« … a single dimension is read, the PBS »), systèmes avec « → has a model » / « → allocate manually », flèche « routes into ». Le contributeur ne voit plus que la chaîne de son système. | — |
| Chaîne › Pastilles « Pass 1 » / « Pass 2 » et flèche « ↓ » avant l'OBS | Repères de passe supprimés ; l'ordre des champs suffit. | — |
| Personne › Bloc « Manager » et champ « Expert » | Plus de manager ni d'expert : une personne par organisation, « Assigned to ». | DEC-087 |
| Turnkey › Ancien détail d'un système, en lecture | Champs « Specialty », « Type » et bloc « Raise a problem » ; remplacés par le détail complet du système. | DEC-101 |
| Fiche de changement (Change Card) | Boutons « New », « Reviewed, no impact », « Action required » et « ＋ Create action / reminder » (toast de rappel factice). Un changement remet l'exigence en To review et la valider le traite. Il ne reste aucune action de relance (rappel au contributeur) dans le panneau Allocation. | DEC-072 |
| Validation › Touche « V » dans le bouton | Le raccourci n'est plus imprimé dans le bouton ; il figure dans l'aide clavier de la barre d'outils. | — |

### Libellés

| Où | Avant | Maintenant |
|---|---|---|
| Turnkey › détail d'un système disparu | « That activity is gone. » | « That system is gone. » |
| Turnkey › liste vide | « No activity yet » | « No system yet » |
| Turnkey › infobulle « has a model » | « Routed into this activity's own allocation model. » | « Routed into this system's own allocation model. » |
| Turnkey › infobulle Compliance de la carte | « Derived from this activity's teams — most restrictive wins » | « Derived from this system's teams — most restrictive wins » |
| En-tête › motifs To review | « Type is AI-detected, unconfirmed » ; « Class is AI-detected, unconfirmed » ; « Activity is AI-detected, unconfirmed » | « Nature proposed by the AI with low confidence » ; « Class proposed by the AI with low confidence » ; « System is AI-detected, unconfirmed » ; nouveau : « Added in vX of its document — see the Versions tab » / « Modified in vX of its document — see the Versions tab » |
| Réaffectation › raisons | « Right typology, wrong person » ; « Wrong typology » ; « This activity doesn't apply here » | « Right system, wrong person » ; « Wrong system » ; « This system doesn't apply here » |
| « Propose a change » › demandes en attente | « ✦ New activity requested — … » | « ✦ New system requested — … » |
| « Propose a change » › infobulle | « Ask the project manager to add an activity you think was missed » | « Ask the project manager to add a system you think was missed » |
| Formulaire « Missing system » | « Why do you think this typology is missing? » ; « No activity left to propose » | « Why do you think this system is missing? » ; « No system left to propose » |
| Formulaire « Missing system » › toasts | « Pick a typology first » ; « New typology proposed — sent to the project manager » | « Pick a system first » ; « New system proposed — sent to the project manager » |
| Allocations › carte de proposition | « ✦ Proposed — new activity by … » | « ✦ Proposed — new system by … » |
| Allocations › toast du choix de personne | « {système}: manager — {Nom} » / « {système}: expert — {équipe} » / « … unassigned » | « {organisation}: assigned to {Nom} » / « {organisation}: unassigned » |
| Nature › confirmation de reclassement en Information | « {ID} already has an expert's answer recorded. Switching it to Information permanently deletes that work — this can't be undone. Continue? » | « {ID} already has a contributor's answer recorded. … Continue? » |
| Journal › entrées de proposition et de réaffectation | « Proposed adding {X} as a missing typology — "…" » ; « Approved — {X} added as a new activity. » ; « Rejected — proposed {X} activity removed, reverted to its prior state. » ; « … (activity didn't apply / wrong typology) » | « … as a missing system — "…" » ; « … added as a new system. » ; « … proposed {X} system removed, … » ; « … (system didn't apply / wrong system) » |
| Journal › validation | « Requirement allocated — characterisation and assignment confirmed, sent to Expert Review. » | « Allocated — sent to Compliance » (jalon « Allocated ») |

### Style visuel

- Pastilles de statut sans le point coloré initial ; « Reassignment requested » reprend `--human` sur `--human-soft`, comme To validate.
- En-tête : titre de l'exigence dans la police de titre (`--font-heading`) ; ligne de l'ID décalée de 18 px pour ne plus passer sous le bouton de repli du panneau ; onglets qui défilent horizontalement au lieu de se tasser.
- Icônes au trait à la place des emoji : appareil photo, copie et corbeille sur la ligne « Captured from … » (« Duplicate », « Delete ») ; cadenas dans la note de lecture seule (petite boîte `--panel-2`, filet `--line`, texte `--text-3`).
- Zone de validation collée en bas : fond `--panel`, filet `--line` en haut, toute la largeur du panneau ; l'état « fait » perd fond et filet.
- « Propose a change » : boutons pleine largeur à fond `--accent-soft`, bordure et texte `--accent`, pleins au survol. « ↻ Re-run the model » : barre `--accent` pleine, texte blanc, une ligne ; variante muette `--ia-soft` / `--ia`.
- Listes de systèmes et d'organisations au format liste compacte, avec des ✕ ronds de 20 px (fond rouge pâle au survol). Sélecteurs de recherche : champ + liste aux en-têtes de groupe en capitales, collés en haut, codes en police mono.
- Couleur partenaire `--partner` (#1b9aaa) / `--partner-soft`, hors de l'échelle de jetons suivie.
- Badge de niveau de l'IA : même pastille que les pourcentages (fond `--panel-3`), ambre gras (`--ia` sur `--ia-soft`) quand non confirmé.
- Cartes Allocations : le nom de l'organisation fait la tête (`--text`, vide en `--text-3`). Cartes systèmes Turnkey : statut en coin, organisation à gauche, personne à droite, manquants en gris italique, ligne Compliance séparée par un filet.
- Journal : « ligne de rail » verticale de 4 px en `--accent`, arrêts de 10 px colorés selon le type d'événement, stations de jalon de 16 px (anneau `--accent`) avec leur nom en police de titre ; puces de filtre en pilule, l'active pleine en `--accent`.

### Points incertains

- Turnkey : le statut « Reassignment requested » grise le bouton d'aiguillage (« approve or reject it first »), mais les vues Turnkey du chef de projet n'ont aucune carte « ✓ Approve / ✕ Reject » ; l'approbation passerait par Compliance (à vérifier).
- Turnkey : retirer le dernier système met l'allocation en Incomplete, mais la pastille d'en-tête du chef de projet (niveau Turnkey) n'est pas recalculée et le bouton d'aiguillage peut rester actif (à vérifier).
- « Read in » : la langue originale est présélectionnée, mais le titre de l'en-tête reste en anglais tant qu'on ne change pas la liste (à vérifier).
- Vue « SIG » du chef de projet : une organisation vide s'affiche « Team not set » en tête de carte, alors que la vue contributeur et le détail Turnkey affichent « — No organisation yet — » (à vérifier).
- La liste des remplaçants du formulaire de réaffectation contient tous les contributeurs, sans filtre par système, contrairement à « Assigned to » (DEC-102) (à vérifier si c'est voulu).
- Contributeur hors Turnkey : si la caractérisation est Incomplete, son bouton « ✓ Validate & send to Compliance » reste actif, mais le clic répond « Nothing to validate yet — fill this in first », et sa pastille montre le statut de son système, pas l'Incomplete de l'exigence (à vérifier).
- Exigence à plusieurs systèmes hors Turnkey : le bloc du modèle du chef de projet n'a ni « ↻ Re-run » ni liste OBS, prévus « dans le détail de chaque système », qui n'existe que sur Turnkey ; les sous-lignes du tableau montrent l'OBS en lecture. Seul le contributeur de chaque système pourrait alors modifier ses organisations, depuis sa propre vue (à vérifier).
- Pas de colonnes personnalisées dans les vues Turnkey du chef de projet ni dans la vue lecture seule (à vérifier si c'est voulu).
- Libellés restés en décalage : « Weak … derivation (NN%) — the proposed assignment may be wrong » dit « assignment » alors que l'OBS est une organisation (DEC-054) ; « Characterisation incomplete — set its nature and class first. » s'affiche aussi quand c'est le système qui manque.
- Analyse faite à la lecture du code des deux versions, prototype non lancé : le rendu exact (couleurs, défilement, position collée) reste à confirmer à l'écran.

## Compliance

`compliance.html` · route `#compliance` · captures : [avant](captures/05-compliance-avant.png), [maintenant](captures/05-compliance-apres.png)

**En bref.** Compliance devient un écran de travail complet, au niveau d'Allocation : tableau dans l'ordre du document (lignes de titre de document et de section), tri par les en-têtes, filtres de colonne et filtre avancé, colonnes personnalisées partagées, colonnes redimensionnables, raccourcis clavier et annulation.
Le contributeur ne saisit plus son verdict dans un petit formulaire : il a un panneau de décision dédié (sa file, le texte complet, choisir puis confirmer, question au client, renvoi, ressources Q&A / Similar / REX / Chat).
Après un Not compliant, on documente l'écart (stratégie d'écart + risque RSK) ; la conformité externe, ce que le client reçoit, est calculée et seul le chef de projet peut la corriger, avec un motif.
Les retards (« overdue »), les versions obsolètes (« outdated »), le tri « action needed first », « Needs my action », la navigation « By expert » et l'onglet Document disparaissent ; une nouvelle version d'un document rouvre les verdicts concernés.
Un contributeur voit désormais tout le tender, ne modifie que son système, et peut se restreindre avec la pastille facultative « My system ».

### Ajouté

| Zone › élément | Ce qu'on voit, ce qui se passe | Réf. |
|---|---|---|
| En-tête › icône Risks (Icon Cluster) | Nouvelle icône triangle entre « Team casting » et « Q&A », infobulle « Risks — the tender's risk register » ; ouvre la page Risks. | DEC-113 |
| Barre d'état › total des affectations (Triage Bar) | Après la jauge : « N assignments », nombre total d'affectations du tender, toujours affiché. | — |
| Barre d'état › pastille « set aside » (Filter Pill) | Contributeur seulement : « N set aside » avec un drapeau, infobulle « Your set-aside assignments — only you see them ». Filtre le tableau sur ses affectations ouvertes mises de côté. | DEC-081 |
| Barre d'état › pastille « my system » (Filter Pill) | Contributeur seulement, inactive par défaut : « N my system » (toutes les affectations de son système), infobulle « Only your system's assignments — the rest of the project stays readable without it ». Se combine avec les pastilles de statut ; « ✕ Clear filter » la désactive aussi. | DEC-012 |
| Barre d'outils › compteur filtré | « N of M requirements · K assignments shown », affiché seulement quand un filtre réduit la liste. | — |
| Barre d'outils › pastille du filtre avancé | Juste après la recherche : « Showing requirements where … » (le filtre en mots) et « ✕ » (« Clear every filter »). Passe à la ligne au lieu d'être tronquée. | — |
| Barre d'outils › pastille de risque | En arrivant de la page Risks sur un risque : « Requirements linked to RSK-xxxxx » et « ✕ » (« Show every requirement again ») ; le tableau ne garde que les exigences liées à ce risque. | — |
| Barre d'outils › « ↺ Document order » | Visible seulement quand une colonne est triée ; infobulle « Clear the column sort and go back to document order ». | DEC-083 |
| Barre d'outils › « Wrap text » (Toggle Switch) | Interrupteur, infobulle « Show the full requirement text instead of a single-line excerpt » : texte, commentaire et stratégie s'affichent en entier, les lignes s'agrandissent. | DEC-078 |
| Barre d'outils › « Filter ▾ » (filtre avancé) | Bouton entonnoir, infobulle « Build a filter across several fields at once ». Panneau « Filter » : conditions et groupes (« + Add condition », « + Add group », « Match all / any of: »), compte en direct (« N of M requirements », « Nothing matches — … alone matches 0 »), filtres enregistrés (« Saved filters », « Save current as… »), « Cancel » / « Apply » (ou « Clear filter »). | — |
| Barre d'outils › champs du filtre avancé | Groupes « Progress » (Status, Internal compliance, Gap strategy, Risk, External compliance), « Assignment » (System, Contributor, Age (days)), « Content & source » (ID, Text, Section, Document), « Custom columns ». « Gap strategy » propose aussi « Strategy missing », « Risk » « Linked » / « Risk missing », « External compliance » « Nothing yet ». | DEC-108 |
| Barre d'outils › « ＋ Column » | Chef de projet seulement, infobulle « Add a column of your own — shared with Allocation, shown here by default » ; ouvre l'éditeur de colonne personnalisée. | DEC-064, DEC-097 |
| Barre d'outils › aide clavier (Shortcut Help) | Icône clavier à droite de la barre ; au survol ou au focus, liste en quatre blocs : « Move », « Select », « Act on the selected assignment », « Custom columns ». | DEC-085 |
| Tableau › tri par en-tête | Un clic sur le libellé trie (▲), un deuxième inverse (▼), un troisième revient à l'ordre du document ; infobulle « Sort by this column », libellé trié en couleur d'accent. Vaut aussi pour les colonnes personnalisées. | DEC-083 |
| Tableau › filtre d'en-tête « System » et « Assigned to » | Un entonnoir dans l'en-tête ouvre les valeurs à cocher, avec « All » / « None », « N of M shown » et « Clear » (« Assigned to » inclut « Unassigned »). Entonnoir blanc sur fond d'accent quand un filtre est actif, infobulle « Filtered — System ». | — |
| Tableau › redimensionnement (Column Resize Handle) | Poignée au bord droit de chaque en-tête, infobulle « Drag to resize · double-click to reset » : glisser, double-cliquer pour revenir, ou ←/→ par pas de 16 px. Largeurs gardées par tender. | — |
| Tableau › colonne « Compliance » (Verdict Pill) | Le verdict seul : « ✓ Compliant » (vert) ou « ✕ Not Compliant » (rouge), « — » tant que l'affectation n'a pas répondu ; sur la ligne d'exigence, le verdict consolidé. | — |
| Tableau › colonne « Gap strategy » | Pour chaque affectation Not compliant : le nom de la stratégie choisie, ou « Strategy missing » (étiquette rouge en pointillé). Vide sur les sous-lignes. | DEC-105, DEC-108 |
| Tableau › colonne « Risk » (Risk Chip) | Puces « RSK-xxxxx » des risques liés (infobulle : le texte du risque, « — open in Risks ») ; un clic ouvre la page Risks sur ce risque. « Risk missing » si un Not compliant n'en a pas. | DEC-105, DEC-108 |
| Tableau › colonne « External compliance » (Verdict Pill) | Ce que le client reçoit : « ✓ Compliant », « ✕ Not compliant », « Pending » (gris, sans icône) ou « — ». Marque « ✎ » si le chef de projet l'a corrigée ; infobulle « Corrected by the project manager on at least one assignment » ou « Derived — from the verdicts and the gap strategies picked ». | DEC-106 |
| Tableau › colonnes personnalisées (Custom Column Header Cell, Custom Column Cell) | Après les colonnes standard ; en-tête = nom + « ✎ » (chef de projet, « Edit or delete this column »). Cellule texte, liste ou liste multiple, modifiable par le chef de projet ou un contributeur ayant une affectation sur l'exigence, en lecture seule sinon. Une colonne créée dans Allocation arrive masquée (à activer dans View). | DEC-097, DEC-100 |
| Tableau › lignes de document et de section (Grid Section / Group Header) | En ordre du document seulement (aucun tri, hors « Show only selected ») : une ligne par document (icône, nom, nom du fichier à droite), puis une par section (numéro, titre, nombre d'exigences affichées). | DEC-078 |
| Tableau › flèche d'une exigence multi-système (Disclosure / Expand Chevron) | Dans la cellule Requirement, repliée par défaut ; infobulle « Expand N systems » / « Collapse systems ». Ouvre les sous-lignes système de cette exigence seulement. | — |
| Tableau › lignes d'équipe, niveau 2 (Branch / Allocated-Activity Sub-row) | Sous un système à plusieurs équipes : badge « N teams » (« N teams within this system — most restrictive wins »), puis une ligne par personne (nom ou « Unassigned ») avec statut, verdict et commentaire. Un clic ouvre le système. | — |
| Tableau › marques dans la cellule ID (contributeur) | Drapeau (« Set aside — only you see this ») et « ✎ » (« Draft verdict in progress ») sur ses propres affectations ; cellule ID teintée de violet quand elle est mise de côté. | DEC-079, DEC-081 |
| Tableau › systèmes partenaires (Turnkey) | Étiquette de système en bleu-vert, infobulle « {Partner} — added for this tender, not part of the Turnkey model. The AI never predicts it; the partner works outside the tool. » ; « Assigned to » affiche « PM · for partner ». | DEC-082 |
| Panneau › phrase d'attente (Detail / Assignment Panel) | Un encadré dit ce qui est attendu, dans chaque état : « Answered and consolidated. Nothing is waiting on you. », « This assignment is answered; N others still are not, so the requirement cannot consolidate yet. », « Waiting on {name} — sent N days ago. Nothing is due from you but a reminder. », « Not dispatched yet. It leaves Allocation before anyone can answer it. ». Grisé quand rien n'est dû. | — |
| Panneau › phrase d'attente d'un Not compliant | « Not compliant — document the gap. Pick a gap strategy and a risk below. Until a strategy is picked, the client is told Pending. » pour qui doit le faire ; pour les autres « Not compliant, gap not documented yet — {name} still has to pick … ». | DEC-108 |
| Panneau › éditeur d'écart (Gap Editor) | Sur une affectation répondue Not compliant : « Gap strategy » et « Risk ». Modifiable par le contributeur du système (et par le chef de projet sur un partenaire) ; ailleurs en lecture seule, avec « Strategy missing » / « Risk missing ». | DEC-105, DEC-108 |
| Éditeur d'écart › « Gap strategy » | Liste « — Pick a strategy — » + stratégies du tender ; dessous « Declared to the client: {pastille} » ; toast « {ID} · {SYS} — {strategy}: the client is told {X} ». Sans stratégie : « No strategy is defined for this tender yet — the project manager writes them in Settings → Compliance. Until then the client is told Pending. » | DEC-106, DEC-110 |
| Éditeur d'écart › « Risk » | Risques liés : puce RSK, première phrase « There is a risk that … », « N req. », « ✕ » pour délier (annulable). Recherche « Search the tender's risks — ID or words » (grisée « No risk on this tender yet ») ; six suggestions au plus, « same heading » d'abord, « N more — refine the search », « No risk matches “…”. » | DEC-105, DEC-114 |
| Éditeur d'écart › « ＋ New risk » | « New risk · only if none of the existing ones fits » : trois champs obligatoires « There is a risk that… », « The risk is caused by… », « The direct impact of the risk will be… », puis « Save and link » ; toast « RSK-xxxxx created and linked to {ID} ». | DEC-113 |
| Panneau › « External compliance » (External Compliance Field) | Sur une affectation répondue : « External compliance · what the client is told » (« for this system » si plusieurs), la pastille ; si corrigée, « derived: {X} » et « Corrected by {name} · {date} — “{reason}” ». | DEC-106 |
| Panneau › correction par le chef de projet | Chef de projet seulement : « Correct » ouvre « Correct what the client is told » (Compliant / Not compliant / Pending, « Reason · required, shown to everyone », « Save correction ») ; ensuite « Change the correction » et « Revert to derived ». Les deux sont annulables. | DEC-106 |
| Panneau › affectation partenaire (Partner Verdict Entry) | Encadré « {Partner} — a partner company added for this tender. … » ; le chef de projet saisit « {Partner}'s verdict » : ✓ / ✕, stratégie et risque si Not compliant, Category + Topic, « Their answer, as received », « Record {Partner}'s verdict — Compliant ». La réponse s'affiche « entered by the project manager from {Partner}'s reply ». | DEC-082 |
| Panneau › onglet Activity › événements | Chaque changement s'inscrit avec auteur et heure : verdict, statut, personne, stratégie (« … (the client is told X) »), risque lié / délié, correction externe, question, renvoi, relance, « Every system has answered — consolidated X », « No longer consolidated — a system is open again », « Declared to the client: X ». | — |
| Panneau › onglet Requirement › colonnes personnalisées | Bloc « Custom columns · entered by people, never by the AI » avec une valeur par colonne ; modifiable par le chef de projet ou un contributeur ayant une affectation sur l'exigence. | DEC-097, DEC-100 |
| Panneau de décision (Decision Panel) | Remplace le panneau à onglets quand un contributeur ouvre une affectation de son système qui attend son verdict (Proposed, Awaiting answer, Awaiting Q&A). Il n'a pas les onglets Assignment / Activity / Requirement. | DEC-079 |
| Panneau de décision › file | Mini-barre (part répondue de son système), « N left · this is k of N · M set aside », « Next › » (« Next in your queue (set-aside ones skipped) »). | DEC-079 |
| Panneau de décision › « Set aside » | Bouton drapeau (« Come back to it later — only you see this marker »), plein et violet quand actif. Toast « {ID} set aside — only you see this marker » / « {ID} back in your queue », annulable ; touche S. | DEC-079, DEC-090 |
| Panneau de décision › « ⇤ Widen panel » | Élargit le panneau (« ⇥ Narrow panel » pour revenir), infobulle « More room for long text, figures or formulas ». | DEC-079 |
| Panneau de décision › en-tête | L'ID puis un lien « § {section} » (« Open the clause in its document ») qui bascule en vue Document. | DEC-080 |
| Panneau de décision › bandeaux | « Reopened by {document} {version} — the requirement changed, so the verdict went back to pending. Give it again. » et « Question in the Q&A register: {QA-ID} {status}. They don't hold your verdict up. » (« N questions … » s'il y en a plusieurs). | DEC-092, DEC-122 |
| Panneau de décision › texte de l'exigence | Libellé « Requirement », texte complet sur un bloc teinté ; dessous « View in the document » (vue Document sur l'exigence, surlignée un instant, le panneau reste). Sur un tender non anglais, interrupteur « Original · {language} » (anglais par défaut). | DEC-080, DEC-081 |
| Panneau de décision › « Your verdict » | Phrase « Give the technical truth. … » et deux grands boutons « ✓ Compliant » / « ✕ Not compliant ». Après le choix : « Verdict: {pastille} Change », les champs du choix, commentaire facultatif, puis « Confirm — Compliant » / « Confirm — Not compliant », collé en bas du panneau. | DEC-080 |
| Panneau de décision › Not compliant | L'éditeur d'écart (stratégie + risque), puis, sur un tender Turnkey seulement, « Category » (liste provisoire, « Placeholder list — the real categories aren't defined yet. ») et « Topic » obligatoire (« Required — what specifically fails »). | DEC-105, DEC-107 |
| Panneau de décision › brouillon | Sous le bloc : « Drafts save themselves », puis « Draft saved · HH:MM » à chaque saisie ; choix, commentaire, catégorie et topic se retrouvent en revenant. | DEC-079, DEC-090 |
| Panneau de décision › « Ask the client » | Bouton secondaire (« Write a question to the client — it goes into the Q&A register »). Formulaire « Ask the client » : « Official: it goes into the Q&A register, … », question obligatoire, « Add to the Q&A register ». Toast « {ID} · {SYS} — question QA-xx added to the Q&A register (To send) », annulable ; l'onglet Q&A s'ouvre. | DEC-080, DEC-088 |
| Panneau de décision › « ↩ Not mine — return it » | Bouton secondaire (« Not yours — send it back to the project management team ») ; ouvre le formulaire de renvoi (voir Modifié). | DEC-079 |
| Panneau de décision › ressources | Onglets repliés « Q&A N », « Similar N », « REX N », « Chat » (un clic ouvre, un second referme). Q&A : « Our questions » et « Asked by other bidders », statut, « Client's answer » ou « No answer yet ». Similar : trois exigences proches au plus (« N% similar », leur verdict), cliquables. | DEC-079, DEC-080 |
| Fenêtre Export (Export Options Modal) | « Export the compliance register » : « Format » (Excel (.xlsx), CSV, PDF), « Rows » (« All requirements (N) », « What the filters show — N requirements ({filters}) », « Selected rows (N) », grisé sans sélection), « Columns » (cases, « All », « As in the table »), « Cancel » / « Export ». | DEC-081 |
| Fenêtre Export › colonnes | ID, texte, section, Compliance, commentaire, Gap strategy, Risk et External compliance cochés ; System, Assigned to, Status, Last follow-up et Age comme dans le tableau ; colonnes personnalisées décochées, étiquetées « internal », avec « Custom columns are internal: leave them unticked for the file that goes to the client. » | DEC-081, DEC-068 |
| Fenêtre colonne personnalisée (Custom Column Editor) | « New column » / « Edit column » : « Name », « Type » (« Free text » / « List »), « Options » + « Add », « Allow several values per requirement », note de portée « This tender only. … », « Create column » / « Save », « Delete column… ». | DEC-097, DEC-066 |
| Fenêtre colonne personnalisée › garde-fous | Type figé dès qu'une valeur existe (« The type can't change — … »), option utilisée non supprimable (« used by N »), suppression confirmée (« Delete “{name}”? », « Keep it » / « Delete column and N values »). | DEC-065, DEC-068 |
| Clavier › sélection | X coche la ligne active, ⇧↑/↓ étend la sélection, ⌘/Ctrl+A sélectionne ce que montrent les filtres (toast « N selected — everything in view »), Échap vide la sélection. | DEC-085 |
| Clavier › N | Va à l'exigence suivante qui attend le lecteur (contributeur : à décider ou écart à documenter ; chef de projet : renvoi à réaffecter, partenaire à saisir). Sinon toast « Nothing waiting on you in this view » (contributeur : « Nothing left waiting on you in this view »). | DEC-085 |
| Clavier › S | Met de côté / remet dans la file l'affectation ouverte (contributeur). | DEC-079 |
| Annulation (Toast) | Verdict, verdict partenaire, question au client, renvoi, réaffectation, mise de côté, risque délié et correction externe ont « Undo » dans leur toast ; ⌘/Ctrl+Z annule la dernière, même toast disparu (« Undone — … », « Nothing to undo »). | DEC-085 |
| Rôles › actions réservées au chef de projet | « ＋ Column » et le « ✎ » des colonnes, « Correct » de la conformité externe, « Send reminder » (panneau, R, barre de sélection), verdict d'un partenaire. Le panneau de décision, lui, n'apparaît qu'au contributeur. | DEC-064, DEC-106, DEC-125 |
| Versions › réouverture | Quand une nouvelle version d'un document modifie une exigence, ses affectations répondues repassent « Awaiting answer », verdict effacé, âge à zéro. « Reopened by {document} {version} » s'affiche dans le panneau de décision, la phrase d'attente, la cloche et l'historique. | DEC-122 |
| Q&A › état partagé | Les questions portent l'état du registre Q&A : « To send », « Sent », « Answer to confirm », « Answered », avec la réponse du client ; les questions d'autres soumissionnaires importées dans Q&A apparaissent dans l'onglet Q&A du panneau de décision. | DEC-116, DEC-122 |
| Tender SIG | Compliance montre les exigences du tender ouvert (avant : toujours celles du tender Turnkey de démo). Sur un tender SIG : ni colonne System (ni dans View, ni dans les filtres, ni à l'export), libellé « Assignment » sans système, ni Category / Topic. | DEC-044, DEC-107 |

### Modifié

| Zone › élément | Avant (8 sept.) | Maintenant | Réf. |
|---|---|---|---|
| En-tête › cloche (Notification Dot) | Bouton sans effet, point rouge permanent. | Ouvre « Notifications · N » : une ligne par type avec son nombre (renvois à réaffecter, questions chez le client, réponses rouvertes par une version) ou « Nothing waiting on you here. » ; point seulement si quelque chose attend. Un clic ouvre l'affectation (si une seule) ou filtre le tableau ; un contributeur ne voit que son système. | — (portée contributeur : DEC-012) |
| En-tête › bouton « Export » | Générait directement un fichier fixe (toasts « Compliance register STB-2026_qualification.xlsx generated », « Risk summary included: … »). | Ouvre la fenêtre « Export the compliance register » ; le bouton « Go to export → » du bandeau « Compliance matrix complete » aussi. | DEC-081 |
| Barre d'état › titre « Compliance » (Triage Bar) | Sur sa propre ligne au-dessus de la barre d'outils, avec « N requirements · M assignments · X/Y pending consolidation ». | Ouvre la barre d'état, marque rouge devant ; la ligne de compte disparaît (remplacée par le total et le compteur filtré). | — |
| Barre d'état › progression | Barre de 120 px + « N/M consolidated · X% · a/b assignments answered ». | Anneau de 16 px + « N/M consolidated » ; pourcentage et affectations répondues passent en infobulle. | DEC-081 |
| Navigation gauche (Left Navigator Panel) | Ouverte par défaut. | Repliée par défaut ; « › » (« Expand navigation ») la rouvre. | — |
| Barre d'outils › recherche (Search Box) | Champ étiré sur toute la barre, « Search requirement ref or text… ». | Champ fixe de 220 px avec loupe, « Search requirement, ID… » (cherche toujours dans l'ID, le texte, le système et la personne). | — |
| Barre d'outils › « View ▾ » (Column Visibility Menu) | « ▤ View ▾ » sur la ligne du titre ; Activity, Expert, Manager, Status, Compliance comment, Last follow-up, Age. | À droite de la barre d'outils ; ajoute Compliance, Gap strategy, Risk, External compliance et les colonnes personnalisées (étiquette « custom ») ; « Reset column widths » quand une largeur a changé (toast « Column widths back to default »). | — |
| Tableau › clic sur un en-tête | Masquait la colonne ; seul View la ramenait. | Trie la colonne ; on ne masque que par View. | DEC-083 |
| Tableau › ordre par défaut | « Sort: action needed first » (renvois, questions, retards d'abord). | Ordre du document (document, section, ID), avec lignes de titre ; un tri donne une liste à plat. | DEC-078, DEC-083 |
| Tableau › colonnes visibles par défaut | Expert, Status, Compliance comment, Last follow-up (Activity, Manager, Age masquées). | Assigned to, Status, Compliance, Compliance comment, Gap strategy, Risk, External compliance, Last follow-up (System et Age masquées). | — |
| Tableau › « Activity » devient « System » | En-tête « Activity » ; cinq activités inventées à libellé long ; « N activities » sur une exigence multiple. | En-tête « System » ; les 16 codes de la capture, libellé = code partout (cellule, sous-ligne, panneau, filtres) ; « N systems ». | DEC-032, DEC-045 |
| Tableau › « Expert » + « Manager » deviennent « Assigned to » | Deux colonnes (expert, et manager d'activité masqué) ; « — no expert — ». | Une personne par affectation : avatar + prénom, « — unassigned — », « Multiple (N) », « PM · for partner » ; entonnoir de filtre. | DEC-087 |
| Tableau › colonne « Status » (Progress Status Chip) | Le verdict une fois consolidé, la puce « ⛔ Reassignment needed », sinon « Pending · N allocated activities ». | L'avancement seul : « Answered » une fois consolidé, sinon le statut de l'affectation prioritaire (renvoi, puis réponse due, puis question chez le client) + « · N assignments ». Même ordre pour l'étiquette des blocs en vue Document et pour l'affectation que le panneau du chef de projet ouvre. | DEC-125 |
| Tableau › sous-lignes système | Toujours affichées sous une exigence multi-activité ; libellé long. | Cachées tant que la flèche est fermée ; libellé = code ; Gap strategy, Risk et External compliance vides sur ces lignes. | — |
| Tableau › « Compliance comment » d'un Not compliant | « {Category} — {Topic} ». | Turnkey : « {Category} — {Topic}. {comment} » ; ailleurs, le commentaire seul (peut être vide). | DEC-107 |
| Barre de sélection › « Send reminder » (Bulk Selection Action Bar) | Datait seulement les affectations en attente de réponse ; « No pending assignment to remind in this selection ». | Mêmes règles que le panneau et R ; relance aussi les « Awaiting Q&A », saute les autres (« · N skipped — answered, not dispatched, returned or unassigned ») ; inscrite dans l'historique ; masqué pour un contributeur. | DEC-125 |
| Vue Document › feuilles (Document Reading View) | Une seule feuille « Technical Requirements Specification », sous-titre « Qualification synthesis — verdicts overlaid on source · read-only ». | Une feuille par document source, titrée de son nom, sous-titre « Compliance synthesis — consolidated verdicts over the source text · read-only ». | — |
| Vue Document › légende | Cinq états : « Compliant », « Partially », « Non-compliant », « Needs clarification », « Awaiting » ; un Not compliant restait sans couleur. | Trois états : « Compliant », « Not compliant », « Pending » ; les blocs Not compliant sont rouges. | — |
| Panneau › en-tête | ID + verdict consolidé (ou « Pending consolidation ») + « Δ outdated version ». | ID + « Pending consolidation » tant que l'exigence n'est pas consolidée ; rien une fois consolidée. | — |
| Panneau › bloc Assignment | « Assignment · {activity} », expert « nom — équipe » ou « No expert assigned yet », puis « Activity manager: … ». | « Assignment · {SYS} » (« Assignment » seul sur SIG), une personne « nom — rôle » ou « Nobody assigned yet » ; pour un partenaire, l'encadré partenaire. | DEC-087 |
| Panneau › affectation répondue | « Response · date », « Compliance for this allocated activity » toujours, bouton bleu actif « ⇗ Escalate to client Q&A [Q] ». | Réponse, « This assignment's verdict · technical assessment » seulement s'il y a plusieurs affectations, phrase d'attente, éditeur d'écart (Not compliant), « External compliance », « Ask the client » grisé. | DEC-121 |
| Panneau › « Ask the client » grisé | « Escalate to client Q&A » restait actif et repassait l'affectation en Awaiting Q&A. | Bouton présent mais désactivé, infobulle « The verdict is given — nothing left to ask on this assignment » ; Q donne le même message. | DEC-121 |
| Panneau › affectation « Awaiting Q&A » | « ⇗ Blocked on the issuer », note, « Question QA-xx — see the Q&A register », « This assignment cannot be answered yet … blocks consolidation of {ID}. » | « Question to the client », une ligne par question (« QA-xx — {status} in the Q&A register », « Client's answer: … »), « It doesn't hold anything up: … Nothing is due from you but a reminder. », « Send a reminder » (chef de projet), « → Open the Q&A register ». | DEC-092, DEC-122 |
| Panneau › affectation renvoyée (chef de projet) | « ↩ Returned by the expert » ; deux listes (« — Activity manager — » tous managers, « Expert » tous experts) ; « Pick an expert before reassigning ». | « ↩ Returned by the contributor », « Reallocate it and send it back out. Internal action — nothing leaves the company here. », une liste « Reallocate to » (« — Nobody — » + personnes de ce système), « Pick someone before reassigning » ; réaffectation annulable. | DEC-102 |
| Panneau › affectation en attente (chef de projet) | « Waiting » : « No response yet — sent N days ago. Above the 5-day threshold. » ; « 🔔 Send a reminder [R] » n'affichait qu'un toast. | Phrase d'attente ; « Send a reminder » seulement si une relance est possible ; la relance date « Last follow-up » et s'inscrit dans l'historique. | DEC-125 |
| Panneau › saisie du verdict (contributeur) | Dans l'onglet Assignment : « ✓ Render a verdict » ouvrait « Render a verdict » (Compliant + commentaire ou Not compliant + Category + Topic, « Save verdict ») ; impossible sur une affectation en Awaiting Q&A. | Le panneau de décision : choisir, documenter, confirmer ; possible aussi pendant qu'une question est chez le client. | DEC-079, DEC-092 |
| Panneau › renvoi par le contributeur (Reassignment Request Form) | « ↩ Request reassignment » : motifs, « Reassign to » (tous les experts), « Correct activity », « Why », « Send request ». | « ↩ Not mine — return it » : « Return it — why isn't it yours? », motifs, « Who should take it » (personnes du même système), « Correct system », « Why », « Return it » ; toast « {ID} · {SYS} — returned to the project management team », annulable. | DEC-102 |
| Panneau › onglet Activity (Activity Timeline) | Frise reconstituée depuis le statut (« Responded — … », « Raised a question to the issuer — assignment blocked until answered. », « Overdue threshold reached … », « … (export from Allocation) »). | Historique de l'exigence partagé avec Allocation : filtres « All / Status / Allocation / Compliance / Comments » avec compteurs, jalons (« Captured », « Allocated », « Answered », « Declared to the client »), avant → après, champ « Comment on {ID}… » + « Post ». | — |
| Consolidation › question au client | Une affectation « Awaiting Q&A » était présentée comme bloquante et son contributeur ne pouvait plus répondre. | La question ne retient rien : le verdict peut être donné à tout moment. Règle inchangée : en attente tant qu'une affectation n'a pas de verdict, puis le plus restrictif l'emporte. | DEC-092 |
| Question au client › création | Q (ou le bouton) créait une question locale « QA-0N » au texte générique et passait l'affectation en « Awaiting Q&A », même répondue ; toast « … escalated — draft question QA-0N created ». | Le contributeur écrit sa question ; elle entre dans le registre Q&A en « To send » avec un identifiant du registre ; seule une affectation « Awaiting answer » passe « Awaiting Q&A » ; plusieurs questions possibles ; « Undo » la retire. | DEC-088, DEC-092 |
| Relance › touche R | Datait « Last follow-up » de toute affectation ayant un expert, même répondue ; « No expert assigned yet on this branch ». | Même règle partout : seulement si la personne doit encore répondre (Awaiting answer ou Awaiting Q&A), jamais par un contributeur ; sinon toast du motif (« Already answered — nobody owes anything on it », « Not dispatched yet — nobody owes an answer », « Returned to the project team — reallocate it instead », « Nobody assigned yet on this assignment »). | DEC-125 |
| Clavier › Q | Escaladait toujours, quel que soit l'état. | Contributeur sur son affectation ouverte : ouvre « Ask the client ». Répondue : refus (« The verdict is given — … »). Autre système : « Read only — {SYS}'s assignment ». Chef de projet : question générique déposée dans le registre. | DEC-121, DEC-012 |
| Rôles › contributeur, lecture | Tableau réduit aux affectations de son activité ; dans la navigation, les autres exigences grisées. | Tout le tender, comme le chef de projet (les compteurs de la barre d'état couvraient déjà tout le tender) ; « My system » pour se restreindre. | DEC-012 |
| Rôles › contributeur, autres systèmes | Filtrées du tableau ; le panneau n'avait aucune notion de lecture seule. | Ouvrables en lecture seule : « Read only — {SYS}'s assignment. Only {SYS}'s contributors or the project team change it. » ; pas de relance, réaffectation, question ni mise de côté ; éditeur d'écart et colonnes personnalisées en lecture. | DEC-012, DEC-100 |
| Rôles › contributeur, arrivée | Panneau vide « No assignment selected ». | S'ouvre sur la première affectation de sa file (ordre du tableau, mises de côté sautées) ; sur une exigence multi-système, son système est sélectionné d'office. | — |
| Export › langue du texte | Sur un tender non anglais, le texte partait dans la langue d'origine (toast « Requirement text in {language} (the original) · … »). | Choix « Original ({language}) » / « English translation », anglais par défaut ; « Comments and categories stay in English either way. » | DEC-081 |
| Export › toasts | « Compliance register STB-2026_qualification.xlsx generated », « Risk summary included: N non-compliant · M still pending consolidation ». | « {ref}_compliance.{format} generated — N requirements · K columns » (+ filtres), « Summary included: … », « Includes internal custom columns — not for the client as it stands » si coché ; « Tick at least one column ». | — |

### Retiré

| Zone › élément | Ce qui disparaît, et ce qui le remplace s'il y a lieu | Réf. |
|---|---|---|
| Barre d'état › retards (« overdue ») | Pastille « N overdue » et son filtre, âge en rouge au-delà de 5 jours, « Above the 5-day threshold. », « · N overdue assignments » dans le panneau vide, événement « Overdue threshold reached ». Seul l'âge reste. | DEC-078 |
| Barre d'état › « 🔔 Remind all overdue » | Bouton et toasts (« Reminders sent to … », « Nothing overdue — all good »). Remplacé par la relance unique (panneau, R, barre de sélection). | DEC-078, DEC-125 |
| Barre d'état › version obsolète (« outdated ») | Pastille « N outdated version » et son filtre, drapeau « Δ outdated » sur la ligne, « Δ outdated version » dans le panneau, encadré « Answered on outdated version. … ». Remplacé par la réouverture des verdicts. | DEC-078, DEC-122 |
| Barre d'état › « By section / By expert » | Bascule et navigation « By expert » (cartes par expert : avatar, équipe, « 🔔 Remind », « answered / pending / blocked », « N overdue · silent N d »). Seule la navigation par section reste. | DEC-081 |
| Barre d'état › aide clavier permanente | « J/K », « R remind », « Q to Q&A ». Remplacée par l'icône clavier de la barre d'outils. | DEC-081 |
| Barre d'outils › listes « All experts » et « All activities » | Remplacées par les filtres d'en-tête de colonne et le filtre avancé. | — |
| Barre d'outils › liste de tri | « Sort: action needed first », « Sort: status », « Sort: expert », « Sort: requirement ref ». Remplacée par le tri par en-tête. | DEC-083 |
| Barre d'outils › « ⚡ Needs my action » | Bouton bascule (renvois, affectations débloquées). En partie remplacé par la touche N. | DEC-078 |
| Tableau › colonne « Manager » | Plus de manager d'activité : une seule personne par affectation. | DEC-087 |
| Panneau › onglet « Document » | Extrait de la section avec l'exigence surlignée. Remplacé par « View in the document » et « § section » (panneau de décision) et par l'onglet de ressources Q&A. | DEC-078, DEC-080 |
| Panneau › relance proposée au contributeur | « 🔔 Send a reminder » sur sa propre affectation : un contributeur ne relance plus. | DEC-125 |
| Onglet Requirement › ligne « Type » | La nature (Functional, Performance…) n'apparaît plus. | DEC-074 |

### Libellés

| Où | Avant | Maintenant |
|---|---|---|
| Panneau vide | « Select a requirement or one of its assignments to see the expert response. » | « Select a requirement or one of its assignments to see the contributor's response. » |
| Barre de sélection | « ↪ Reassign expert » ; toast « Jump to the branch below to reassign its expert/manager » | « ↪ Reassign contributor » ; toast « Jump to the assignment below to reassign its contributor » |
| Panneau › renvoi, texte par défaut | « The expert judged this allocation wrong and returned it. » | « The contributor judged this allocation wrong and returned it. » |
| Panneau › question, texte par défaut | « The expert needs a precision from the tender issuer before answering. » | « The contributor asked the client for a precision — the verdict doesn't wait for it. » |
| Formulaire de renvoi › motifs | « Right activity, wrong person » / « Wrong activity » / « This activity doesn't apply here » | « Right system, wrong person » / « Wrong system » / « This system doesn't apply here » |
| Formulaire de renvoi › toast | « A reason is required to request a reassignment » | « A reason is required to return it » |
| Saisie du verdict › commentaire Compliant | « Free comment, optional. Say so here if R&D work is needed for compliance. » | « Comment — optional. Say so here if R&D work is needed. » (Not compliant : « Comment — optional ») |
| Saisie du verdict › Topic | placeholder « Free text — what specifically fails » ; toast « Describe the topic before saving » | « Required — what specifically fails » ; « Name the topic — a Not compliant verdict gets documented » |
| Saisie du verdict › toast | « {ID} · {activity} — verdict recorded » | « {ID} · {SYS} — Compliant » / « {ID} · {SYS} — Not compliant » |
| Onglet Requirement › note | « 🔒 Frozen at review export — editable only through a new document version (Versions & exchanges). » | cadenas + « The requirement text changes only through a new document version (Documents & versions). » |
| Onglet Requirement › « Consolidated » | « Pending — blocked by {activity} ({status}) » | « Pending — {SYS} not answered yet ({status}) » |
| Onglet Chat | « … separate from "Escalate to client Q&A" above, which leaves the company and blocks consolidation. … » | « … separate from "Ask the client", which files an official question in the Q&A register. This one never does either. » |

### Style visuel

- Icônes au trait (masques sur la couleur du texte) à la place des emoji et symboles : œil (démo), fichier (navigation, lignes de document), cloche, trombone (pièce jointe), cadenas, flèche (« Ask the client »), drapeaux (« Set aside »), entonnoir, colonnes, clavier, chevron.
- Pastilles d'avancement sans point devant ; « Answered » passe en violet (`--human`), « Reassignment needed » en ambre (`--ia`) ; le vert et le rouge sont réservés aux verdicts (colonnes Compliance et External compliance). Mêmes couleurs pour les points du sélecteur de systèmes du panneau.
- Pastilles de verdict avec icône ✓ / ✕ ; « Pending » externe en gris plein ; valeur corrigée entourée et marquée ✎. Un Not compliant est enfin rouge dans la navigation et la vue Document.
- Jauge de consolidation : anneau de 16 px (`--ok`) au lieu de la barre de 120 px.
- Partenaires en bleu-vert `--partner` #1b9aaa / `--partner-soft`, hors de l'échelle de jetons. Cellule ID d'une mise de côté et puces RSK sur `--human-soft` (hors échelle) ; « Strategy missing » / « Risk missing » en pointillé `--warn`.
- Lignes de structure : titre de document sur `--panel-3`, numéro de section en accent et police mono ; flèche de 20 px qui pivote d'un quart une fois ouverte ; lignes d'équipe sur `--bg`, plus indentées.
- Panneau de décision : texte de l'exigence en Georgia, `--text-lg`, sur `--accent-soft` avec un bord gauche accent (original : `--ia-soft`, bord ambre) ; boutons de verdict pleins vert / rouge ; « Confirm » collé en bas avec un halo couleur panneau ; largeur élargie min(720 px, 62 vw).
- Historique dessiné en ligne de rail : trait vertical de 4 px en accent, jalons en cercles de 16 px avec libellé en police de titre, « avant » barré rouge → « après » vert.
- Onglets du panneau : défilent à l'horizontale au lieu de passer à la ligne ; ligne d'ID décalée pour dégager le bouton de repli. Fenêtres Export et colonne sur fond flouté.

### Points incertains

- Le chef de projet n'a aucun bouton actif « Ask the client » sur une affectation ouverte (seulement le bouton grisé sur une affectation répondue, et la touche Q qui dépose une question générique) : voulu ou oubli ? (à vérifier)
- Un contributeur voit le formulaire de réaffectation (« Reallocate to ») sur une affectation renvoyée de son propre système ; aucune garde de rôle dans le code. (à vérifier)
- Sur une exigence à une seule affectation répondue, le panneau du chef de projet n'affiche plus le verdict interne (ni dans l'en-tête, ni dans l'onglet) : seulement la réponse et la conformité externe. (à vérifier si voulu)
- Majuscule incohérente à l'écran : « Not Compliant » (colonne Compliance, filtre « Internal compliance », étiquette de la vue Document) et « Not compliant » (conformité externe, boutons, légende, toasts).
- Clic sur une notification groupée : le tableau est filtré mais la pastille de statut correspondante ne s'allume pas et « ✕ Clear filter » peut ne pas apparaître (lu dans le code). (à vérifier)
- « ↪ Reassign contributor » (barre de sélection) n'est toujours qu'un saut vers la première exigence sélectionnée, sans réaffectation en masse, et reste visible pour un contributeur.
- « N my system » compte toutes les affectations de son système, répondues comprises, alors que les autres compteurs comptent des états.
- Les lignes d'équipe ne sont qu'un affichage : le verdict du système n'est pas recalculé à partir de ses équipes (constat de CODE.md, non vérifiable à l'écran sans autre jeu de données).
- La liste « Category » est toujours provisoire (« Placeholder category A… »), en attente de la liste métier.

## Q&A

`qa.html` · route `#qa` · captures : [avant](captures/06-qa-avant.png), [maintenant](captures/06-qa-apres.png)

**En bref.** Le registre des questions au client est simplifié (DEC-116). Les onglets « Questions » / « Answers » laissent place à une seule liste à deux vues : « Our questions » (nos questions, chacune avec son statut et la réponse du client dessous) et « Other bidders » (les questions-réponses des autres soumissionnaires, en lecture seule, après import). Les statuts se marquent à la main : « To send », puis « Sent » avec « Mark as sent » (une question ou une sélection), et retour possible par « Not sent ». L'import pose les réponses sur nos questions, et une réponse incertaine devient « Answer to confirm » sur la question au lieu de passer par une file d'arbitrage. Disparaissent l'export du lot qui marquait tout comme envoyé, les doublons et leur fusion, l'exclusion, les groupes, les tuiles, l'arbitrage et ses raccourcis, et la liste « Resolved & context ». Les questions posées dans Compliance arrivent ici, et aucune question n'est plus présentée comme bloquante.

### Ajouté

| Zone › élément | Ce qu'on voit, ce qui se passe | Réf. |
|---|---|---|
| En-tête › cloche › menu « Notifications » (Icon Button, Notification Dot) | La cloche ne faisait rien au 8 sept. Elle ouvre maintenant « Notifications · N », avec au plus trois lignes : « **N answer(s)** to confirm » (point violet, « from the client's dossier »), « **N question(s)** to send » (point gris, « mark them as sent once they're out ») et « **N question(s)** sent, no answer yet » (point couleur accent, « awaiting the client »). Un clic ouvre la vue « Our questions » filtrée sur ce statut. Sans élément : « Nothing waiting on you here. » La pastille rouge de la cloche n'apparaît que s'il y a au moins une ligne. | — |
| Barre d'outils › sélecteur de vue (Q&A View Switch) | Interrupteur à deux segments : « Our questions N » et « Other bidders N ». Avant tout import, le second affiche « — », avec l'info-bulle « Not imported yet ». Changer de vue vide la recherche. Il remplace les onglets (voir Retiré). | DEC-116 |
| Our questions › filtre de statut (Q&A Status Filter) | Puces avec compteur : « All N », « To send N », « Sent N », « Answer to confirm N », « Answered N ». « Answer to confirm » n'apparaît que s'il y a au moins une réponse à confirmer, encadrée en violet. Quand elle se vide, le filtre revient à « All ». | DEC-116 |
| Our questions › sélection et action groupée (Q&A Status Filter) | À droite des puces : le lien « Select the N to send » apparaît quand plus d'une question à envoyer est affichée et que rien n'est sélectionné. Dès qu'une question est cochée, une barre « **N** selected » s'affiche, avec le bouton primaire « Mark as sent » et le lien « Clear ». | DEC-116 |
| Carte › case à cocher (Q&A Card) | Seulement sur une question « To send ». Info-bulle : « Select it to mark several as sent at once ». Une carte cochée prend une bordure accent et une barre accent à gauche. | DEC-116 |
| Carte › bouton « Mark as sent » (Q&A Card) | Seulement sur une question « To send ». Info-bulle : « It has gone to the client — the tool doesn't send anything itself ». La question passe à « Sent · {date du jour} ». Toast « QA-xx marked as sent », ou « N questions marked as sent » en groupe. | DEC-116 |
| Carte › bouton « Not sent » (Q&A Card) | Bouton discret, seulement sur une question « Sent » sans réponse à confirmer. Info-bulle : « Back to the questions to send ». La question revient à « To send » et perd sa date d'envoi. Toast « QA-xx back with the questions to send ». | DEC-116 |
| Carte › question venue de Compliance (Q&A Card) | Une question posée dans Compliance (« Ask the client ») arrive ici en « To send », en tête de son groupe de statut. Sa ligne d'infos se termine par « · from Compliance ». Son statut et sa réponse, une fois marqués ici, sont repris dans Compliance. | DEC-088, DEC-122 |
| Carte › réponse à confirmer (Q&A Card, variante « answer to confirm ») | Sous la question, un encadré violet en pointillés titré « Probably the client's answer — N% sure it answers this question », suivi du texte proposé. « ✓ It's the answer » fait passer la question à « Answered · {date} » (toast « QA-xx answered — {exigence · système} »). « Not this one » retire la proposition : la question reste « Sent » (toast « QA-xx stays sent — still waiting for its answer »). | DEC-116 |
| Our questions › registre vide | Quand aucune question n'existe : « No question yet — they are raised from Compliance, on an assignment. » | DEC-088 |
| Other bidders › liste (Q&A Card, variante « other bidder ») | En tête : « N question(s) asked by other bidders, with the client's answer — published to every bidder ». Chaque carte montre la question, à droite l'étiquette de l'exigence (info-bulle « The requirement it concerns ») ou « No requirement linked » en italique gris (info-bulle « The import couldn't tell which requirement this concerns »), puis l'encadré vert « Client's answer ». Pas d'identifiant, de statut ni d'action. Les Q&A rattachées à une exigence apparaissent aussi dans l'onglet Q&A du panneau de Compliance pour cette exigence. | DEC-116 |
| Other bidders › état vide avant import | Titre « Nothing imported yet », puis « The client's Q&A dossier holds every bidder's questions with their answers. Import it: the answers to our questions go onto them, and everyone else's are listed here. », et bouton primaire « Import the client's answers ». | DEC-116 |
| Other bidders › recherche sans résultat | « No question or answer matches. » | DEC-116 |

### Modifié

| Zone › élément | Avant (8 sept.) | Maintenant | Réf. |
|---|---|---|---|
| Dates du tender (Deadline Banner) | Un bandeau coloré par onglet. Dans Questions : « Question cut-off **passed** — {date}. New questions can still be raised and merged in; it's your call whether a late one still goes out. » (ou « Question cut-off: {date}. »). Dans Answers : « Answers were expected by {date} — **overdue**. N branches are still blocked in Awaiting Q&A. » (ou « Answers expected by {date}. »). | Une seule ligne grise, discrète, au-dessus de la barre d'outils et dans les deux vues : « Question cut-off {date} — passed » et « Answers expected by {date} — overdue » (icônes sablier et horloge). « passed » et « overdue » n'apparaissent, en rouge gras, que si c'est le cas. Une date absente n'affiche toujours rien. | DEC-116, DEC-092 |
| Barre d'outils › recherche (Filter Toolbar, Text Input) | « Search question text or requirement ref… » : texte de la question ou exigence. | Sur Our questions : « Search a question or a requirement ID… », qui cherche aussi l'ID de question. Sur Other bidders : « Search their questions and answers… », sur la question, la réponse ou l'exigence. | DEC-116 |
| Barre d'outils › filtre système (Select Dropdown) | « All activities », puis cinq libellés inventés (« SIG & Urban », « Mainline Wayside », « Safety », « Telecom », « Infrastructure »). | « All systems », puis les 16 codes système de la capture, dont le libellé est le code (AFC … TRK). Le filtre n'apparaît que sur Our questions. | DEC-032, DEC-045 |
| Barre d'outils › export | Section « Export the batch » : une carte affichait un grand nombre (« N question(s) ready to go out ») et le bouton primaire « ⬇ Export batch for issuer ». Ce bouton faisait passer toutes les questions à envoyer en « Sent » et remplaçait leur date par « Today ». | Bouton secondaire « Export to Excel » (icône de téléchargement) à droite de la barre, sur Our questions seulement. Info-bulle : « An Excel file of the questions still to send, one row each with its requirement ID — sending stays yours, and so does marking them as sent ». Il ne change aucun statut. Toast « Excel with the N question(s) to send — mark them as sent once they're out », ou alerte « Nothing left to send ». | DEC-116 |
| Barre d'outils › import | Dans l'onglet Answers, la section « Import the dossier » contenait une boîte à deux modes (fichier ou texte collé), puis lançait une extraction, un rapprochement automatique et l'arbitrage. | Un bouton secondaire « Import the client's answers » (icône de téléversement), à droite de la barre, dans les deux vues. Il figure aussi dans l'état vide d'Other bidders. Pendant l'import, il est désactivé et affiche une roue et « Importing… ». | DEC-116 |
| Import › résultat | Toast « Dossier imported — N pairs extracted, N matched automatically, N need arbitration ». Nos questions rapprochées passaient en Answered, les incertaines partaient dans la file d'arbitrage, celles des concurrents dans « Resolved & context ». | Chaque question « Sent » reçoit la réponse du client et passe à « Answered · {date} ». Une réponse incertaine reste sur sa question en « Answer to confirm ». Les Q&A des autres soumissionnaires remplissent la vue Other bidders, et son compteur se met à jour. Toast « Client's answers imported — N of our questions answered, K to confirm, M from other bidders » (en alerte s'il y a des réponses à confirmer). | DEC-116 |
| Our questions › organisation de la liste | Une section « All questions » (« One question blocks exactly one assignment », « N on record »), puis des groupes titrés avec compteur : « Drafts », « Sent to the issuer », « Answered », « Excluded from export ». | Une liste unique sans intertitres, triée dans l'ordre Answer to confirm, To send, Sent, Answered. Le statut figure sur chaque carte. Plus aucune mention de blocage. | DEC-116, DEC-092 |
| Carte › statut (Q&A Card) | Le statut ne se lisait qu'au titre du groupe : Drafts, Sent to the issuer, Answered ou Excluded from export. | Une pastille à droite de la question : « To send » (gris), « Sent · {date d'envoi} » (accent), « Answered · {date} » (vert) ou « Answer to confirm » (violet). Le statut Excluded n'existe plus. | DEC-116 |
| Carte › ligne d'infos (Activity / Requirement Tag) | Étiquette de l'exigence, puis « {exigence} · {libellé long} » (un libellé de l'ancienne liste, par exemple « Mainline Wayside »), puis « raised by {nom} · {date} ». Après l'export, la date devenait « Today ». | Étiquette de l'exigence, code système (rien s'il n'y en a pas), puis « raised by {nom} · {date} » (+ « · from Compliance »). La date de dépôt est conservée et la date d'envoi s'affiche dans la pastille. | DEC-032, DEC-088, DEC-116 |

### Retiré

| Zone › élément | Ce qui disparaît, et ce qui le remplace s'il y a lieu | Réf. |
|---|---|---|
| Sous le titre › onglets « Questions » / « Answers » (Tab Bar, Count Badge) | Ils disparaissent avec le compteur rouge de l'onglet Answers (nombre d'éléments à arbitrer). Remplacés par le sélecteur de vue « Our questions » / « Other bidders ». | DEC-116 |
| Questions › section « Export the batch » (Export Readiness Summary) | Disparaissent : l'intertitre et sa mention « Once per tender · nothing leaves the tool by itself », la carte au grand nombre, les textes « From N contributor(s). Excel, one row per question with its requirement ID beside it — you forward the file to the issuer yourself. » et « Nothing waiting to be exported » / « Questions raised from Compliance land here as drafts. Everything already exported is in the register below. », le bouton « ⬇ Export batch for issuer » et le toast « N question(s) exported for the issuer — forward the file yourself ». Remplacé par « Export to Excel ». | DEC-116 |
| Questions › alerte de doublon (Duplicate Alert) | L'encadré « QA-xx and QA-yy look like the same question to the issuer. Merge before exporting so the client gets one, not two. » disparaît, avec le bouton « ⇲ Merge into QA-xx » et le toast « … merged into … — one question to the issuer, both assignments attached ». Plus de détection de doublons, rien ne les remplace. | DEC-116 |
| Questions › intertitre « All questions » | Disparaissent : l'intertitre, la mention « One question blocks exactly one assignment » et le compteur « N on record ». Le compte est maintenant dans « Our questions N » et « All N ». | DEC-116, DEC-092 |
| Questions › exclusion | Disparaissent : la mention « In the batch » et le bouton « Exclude » sur les brouillons (info-bulle « Remove from this export — the question stays on record, but {nom} isn't told it was dropped »), le groupe « Excluded from export » aux cartes estompées, « ↺ Include again », la note « Removed from export — {nom} hasn't been told; there's no notification for this yet. » et leurs toasts. Rien ne les remplace. | DEC-116 |
| Answers › boîte d'import (Q&A Dossier Import Box, Textarea) | Disparaissent : l'intertitre « Import the dossier », le texte « In whatever form the client sent it — Excel, PDF, a plain email body. … », les modes « Upload a file » / « Paste content », la zone « Paste the dossier's raw text here — any layout… », les boutons « ⬆ Choose a file (simulated) » et « Extract Q&A pairs », l'alerte « Paste the dossier's content first » et la ligne « Extracting question/answer pairs from an arbitrary layout… ». Remplacée par le bouton « Import the client's answers ». | DEC-116 |
| Answers › tuiles « Where the dossier stands » | Disparaissent l'intertitre (« N question/answer pairs extracted ») et les trois tuiles « Matched automatically », « Awaiting arbitration » et « Branches still in Awaiting Q&A ». Rien ne les remplace. | DEC-116, DEC-092 |
| Answers › file d'arbitrage (Arbitration Queue Card, Arbitration Guess Button, Kbd Key) | Disparaissent : la section « Arbitrate what the matching couldn't place », la progression « N/M arbitrated » avec sa barre et « N left », la carte « ● Our question — … » / « Competitor question — matched for context only », les propositions numérotées « NN% confidence », « No matching requirement », « Skip — come back to this », la fin « Nothing left to arbitrate — N items went through this queue. » et leurs toasts. Remplacée par la réponse à confirmer sur la carte. | DEC-116 |
| Answers › raccourcis clavier | Les touches 1–9 (choisir une exigence), N (aucune) et S (passer) disparaissent avec la file d'arbitrage. Plus aucun raccourci sur l'écran. | DEC-116 |
| Answers › liste « Resolved & context (N) » (Context Row) | La liste repliable « Our question — QA-xx · {exigence} » / « Competitor — context only · … » disparaît. Les Q&A des autres soumissionnaires vont dans la vue Other bidders. | DEC-116 |

### Libellés

| Où | Avant | Maintenant |
|---|---|---|
| Carte › encadré de la réponse du client | « Issuer answer · {date} » | « Client's answer · {date} » |
| Our questions › aucun résultat de filtre ou de recherche | « No question matches this filter. » | « No question matches. » |

### Style visuel

- Pastilles de statut : « To send » `--panel-3` / `--text-2`, « Sent » `--accent-soft` / `--accent`, « Answered » `--ok-soft` / `--ok`, « Answer to confirm » `--human-soft` / `--human` (violet).
- Réponse à confirmer : encadré violet pâle à bordure pointillée `--human`. Réponse du client : encadré vert pâle à bordure `--ok` atténuée, aligné sur le texte de la question (retrait de 25 px).
- Sélecteur de vue : segments sur fond `--panel-3`, segment actif sur `--panel` avec ombre légère. Les compteurs sont en pastille, en accent sur le segment actif.
- Ligne des dates : texte `--text-3` en `--text-sm`, dates en gras, « passed » / « overdue » en `--warn`. Les bandeaux rouges et ambre disparaissent.
- Icônes SVG au trait (Icon) : téléchargement pour « Export to Excel », téléversement pour « Import the client's answers », sablier et horloge pour les dates. Elles remplacent les glyphes « ⬇ », « ⬆ » et les emoji ⏳, 🕐, ⚠.
- Plusieurs éléments visuels disparaissent : le grand nombre de 32 px de la carte d'export, la carte d'arbitrage et ses touches carrées, les tuiles et les cartes estompées des questions exclues.

### Points incertains

- Aucun contrôle de rôle à l'écran : tout utilisateur peut cliquer « Mark as sent » ou « Not sent », confirmer une réponse ou importer, comme au 8 sept. Qui a le droit de marquer l'envoi et d'importer (le chef de projet seulement ?) reste à vérifier contre la spécification.
- Dans le prototype, « Import the client's answers » n'ouvre aucun sélecteur de fichier. Le produit devra demander le dossier, mais l'écran ne dit plus quels formats sont acceptés depuis la disparition de la boîte d'import (à vérifier).
- Une question « Answered » n'offre aucune action : une réponse confirmée par erreur ne peut pas être annulée. « Not this one » jette la proposition sans la garder nulle part (à vérifier si c'est voulu).
- « Export to Excel » exporte toutes les questions « To send », sans tenir compte des filtres système et recherche affichés (déduit du code).

## Risks — nouvel écran

`risks.html` · route `#risks` · capture : [maintenant](captures/09-risks-apres.png)

**En bref.** C'est un nouvel écran de support : la liste des risques du tender, en lecture seule. Chaque risque porte un identifiant « RSK-… », sa justification en trois réponses (« There is a risk that… », « The risk is caused by… », « The direct impact of the risk will be… »), les exigences auxquelles il est lié et son créateur. Les risques se créent et se lient dans Compliance, sur une affectation Not compliant, en réutilisant d'abord un risque existant (DEC-105). Sur cette page, on cherche, on exporte et on part vers Compliance : vers une exigence, ou vers toutes celles liées au risque. Un risque n'a ni poids, ni statut, ni commentaires, ni fusion, ni système : il appartient au tender (DEC-113, DEC-114).

### Ajouté

| Zone › élément | Ce qu'on voit, ce qui se passe | Réf. |
|---|---|---|
| En-tête (App Header, Brand Logo, Breadcrumb) | De gauche à droite : logo de l'entreprise, filet, « SRM » (vers le tableau de bord), puis le fil d'Ariane « / {référence} · {nom} » du tender ouvert (info-bulle « Back to the project dashboard »). | — |
| En-tête › bouton « Compliance » (Nav Button) | À droite, avec une icône drapeau. Info-bulle : « Compliance — where risks are linked to Not compliant requirements ». Il ouvre Compliance sans filtre. | — |
| En-tête › icône réglages (Icon Button) | Icône curseurs. Info-bulle : « Project configuration — gap strategies are under Compliance ». Elle ouvre la configuration du projet. | DEC-110 |
| En-tête › avatar (Header Avatar) | Initiales de l'utilisateur. L'écran n'a ni cloche, ni bouton Q&A, ni bouton Documents. | — |
| Titre (Page Title) | « Risks » (titre de page avec trait rouge), suivi du sous-titre « Each Not compliant should be traced to a risk; risks are reused — each justified by the three answers below ». Un risque manquant est signalé, jamais bloquant. | DEC-108, DEC-113 |
| Barre d'outils › recherche (Text Input) | Champ « Search a risk — ID or words ». Il filtre à chaque frappe, sans tenir compte de la casse, sur l'ID et les trois réponses, mais ni sur les exigences ni sur le créateur. Le curseur reste dans le champ. | DEC-113 |
| Barre d'outils › compteur | « N risks » (« 1 risk » au singulier), ou « N of M » quand la recherche réduit la liste. | — |
| Barre d'outils › « Export » (Ghost Button) | À droite, avec une icône de téléchargement. Il exporte les risques affichés, recherche appliquée, avec leur justification. Message : « Risk list exported — N risks with their justification » (voir Contrôles de démo). | DEC-113 |
| Filtres | Il n'y a aucun filtre en dehors de la recherche : ni statut, ni poids, ni système. | DEC-113, DEC-114 |
| Tableau › colonnes (Risk List) | « ID », « There is a risk that… », « The risk is caused by… », « The direct impact of the risk will be… », « Requirements », « Created by ». Une ligne par risque, dans l'ordre de création. Les textes s'affichent en entier, renvoyés à la ligne. Pas de tri, pas de sélection, et rien ne s'ouvre au clic sur une ligne. | DEC-113 |
| Tableau › « ID » | Forme « RSK-00001 » : cinq chiffres, numérotation continue par tender, en gras dans la police des codes. | DEC-105 |
| Tableau › trois colonnes de justification | Les réponses aux trois questions du gabarit de risque, saisies comme trois champs obligatoires dans le formulaire « ＋ New risk » de Compliance. Elles ne se modifient pas ici. | DEC-113 |
| Tableau › « Requirements » › puces d'exigence | Une puce par exigence liée, sans doublon, avec l'info-bulle « Open {ID} in Compliance ». Le clic ouvre Compliance avec cette exigence sélectionnée. Un risque sans lien affiche « none » en gris. | DEC-113 |
| Tableau › « Requirements » › lien « all → » | Il apparaît dès que le risque a plus d'une exigence liée, avec l'info-bulle « Compliance filtered on RSK-… ». Le clic ouvre Compliance filtré sur ces exigences, sous un bandeau « Requirements linked to RSK-… » ; sa croix (« Show every requirement again ») retire le filtre. | DEC-113 |
| Tableau › « Created by » | Le nom du créateur, et dessous la date de création, en petit et en gris ; « — » si le créateur est inconnu. Un risque créé dans Compliance porte le nom de l'utilisateur et « Today ». | DEC-113 |
| Tableau › ligne mise en évidence | Quand on arrive par une puce « RSK-… » de Compliance, la ligne de ce risque est surlignée en accent pâle et amenée au centre de l'écran. | — |
| Panneau de détail | Aucun panneau. Le tableau montre tout ce qu'un risque contient. | DEC-113 |
| Actions sur un risque | Rien ne se crée, ne se modifie, ne se supprime ni ne se fusionne ici, et il n'y a ni statut ni commentaire. La création et le lien ou la suppression de lien se font dans Compliance, sur un Not compliant (« ＋ New risk », proposé seulement si aucun risque existant ne convient). | DEC-105, DEC-113 |
| État vide › aucun risque sur le tender | Encadré en pointillés : « No risk on this tender yet. », puis « Risks are created in Compliance, when the responsible of a Not compliant requirement documents the gap — and reused from there. », puis le bouton « Open Compliance → ». La barre d'outils (recherche, compteur, export) n'est pas affichée. | DEC-105 |
| État vide › recherche sans résultat | « No risk matches. » remplace le tableau ; la barre d'outils reste affichée. | — |
| Rôles et type de tender | Même page pour le chef de projet et le contributeur, en lecture seule pour tous. Elle est identique en Turnkey et en SIG : aucune colonne système, puisqu'un risque appartient au tender. | DEC-114 |
| Accès depuis les autres écrans (hors de cette page) | Trois entrées : la carte « Risks » du rail « Always open » du tableau de bord (« N in the list », info-bulle « Risks — the tender's risk register, fed from Compliance. ») ; l'icône triangle de l'en-tête de Compliance (« Risks — the tender's risk register ») ; et, dans le panneau de Compliance, une puce « RSK-… » (« Open RSK-… in Risks ») qui ouvre la page sur ce risque. Le détail figure dans les zones Tableau de bord et Compliance. | — |

### Style visuel

- La page occupe toute la largeur, sans largeur maximale, alors que Documents et Q&A restent centrés à 1080 px.
- Le tableau est propre à l'écran (Risk List) et n'utilise pas le moteur de tableau partagé d'Allocation et Compliance. Il a un cadre `--line`, des coins `--radius-lg`, des en-têtes en `--text-xs` gris sur `--panel-2`, des cellules alignées en haut et un texte en `--text-sm`. Il dépend de `--panel-2` et `--line-2`, qui ne font pas partie de l'échelle de jetons suivie.
- L'ID et les puces d'exigence sont en police des codes (`--font-mono`, police de la marque). Les puces ont une bordure `--line-2`, des coins `--radius-xs` et passent en `--accent` au survol. « all → » est en `--accent`, « none » en `--text-3`.
- La ligne mise en évidence prend un fond `--accent-soft`. L'état vide est un encadré pointillé `--line-2`, centré.
- La charte est la même que sur les autres écrans : police de la marque, trait rouge `--brand-red` devant le titre, accent marine en thème clair, logo de l'entreprise suivi de « SRM ».

### Points incertains

- Les liens sont lus dans la documentation d'écart de Compliance. Une exigence dont le Not compliant a été rouvert par une nouvelle version reste listée comme liée au risque (déduit du code, à vérifier si c'est voulu). Repasser l'affectation en Compliant, en revanche, retire bien le lien.
- Une exigence liée au même risque sur deux systèmes n'apparaît qu'une fois dans « Requirements ». Rien n'indique à l'écran quel système porte le lien (à vérifier si c'est suffisant).
- Le texte de l'état vide dit « the responsible of a Not compliant requirement ». La formulation anglaise est à revoir, et le rôle visé (la personne de l'OBS, DEC-087) est à confirmer.
- Le contenu exact du fichier exporté (colonnes, format) n'est pas défini à l'écran (à vérifier).

## Configuration

`dashboard-et-config.html` · route `#config` · captures : [avant](captures/08-configuration-avant.png), [maintenant](captures/08-configuration-apres.png)

**En bref.** Onze sections au lieu de neuf. Les deux nouvelles portent de vrais réglages du tender : « Allocation model » (système, liste OBS Turnkey avec ajout de partenaires, produit, modèle appliqué, relance globale montrée mais non câblée) et « Compliance » (stratégies d'écart). Ce qui est fixé à la création devient visible mais non modifiable : ligne produit, produit, langue de travail. Sept réglages sans réalité disparaissent, dont « Restricted view » et le verrou de validation, et quatre réglages de conversion du document arrivent dans « Capture & segmentation ». Le vocabulaire suit les décisions : « contributors », « system », « Allocation ».

### Ajouté

| Zone › élément | Ce qu'on voit, ce qui se passe | Réf. |
|---|---|---|
| Menu de gauche › « Allocation model » et « Compliance » (Config Nav Item) | Deux nouvelles entrées, placées après « Reminders » (icônes de relance et de drapeau). | DEC-049, DEC-110 |
| Allocation model › en-tête (Config Section) | « Which model derives ABS, PBS and OBS on this tender — and what changing it costs. » | DEC-049 |
| Allocation model › « System » | Valeur en lecture seule : la ligne du tender (« Turnkey », « SIG »…). « What the tender is issued on. One per tender. » | DEC-046, DEC-049 |
| Allocation model › « Turnkey OBS list » (Turnkey OBS List Setting) | Tender Turnkey seulement : « The systems a requirement can be assigned to at pass 1. Add a partner company that takes part of the scope — it joins this list for this tender only. » Les 16 systèmes du modèle en étiquettes neutres (infobulle « From the Turnkey model »), puis les partenaires ajoutés, en couleur, « {CODE} · {nom} » avec ✕ (infobulle « {nom} — added for this tender, not part of the model »). | DEC-082 |
| Allocation model › « Turnkey OBS list » › note | « An added system is not part of the Turnkey model: the AI never predicts it, and the partner has no access to the tool. It has no model and no teams — a requirement assigned to it stops at the system — and the project manager enters its compliance verdict from the partner's answer. » | DEC-082 |
| Allocation model › « Turnkey OBS list » › ajout | Champ « Partner company name » + « ＋ Add » (ou Entrée). Le code est le premier mot du nom en majuscules (8 caractères au plus, suivi d'un chiffre s'il existe déjà) ; toast « {nom} added to the Turnkey OBS list as {CODE} ». Refus : « Type the partner's name », « That partner is already in the list ». | DEC-082 |
| Allocation model › « Turnkey OBS list » › retrait | ✕ (infobulle « Remove — only while no requirement is assigned to it ») : « {nom} removed from the Turnkey OBS list ». S'il est utilisé : « Still assigned to N requirements — reassign them to another system first ». | DEC-093 |
| Allocation model › « Product » | Lecture seule : « {ligne} {produit} » (ex. « SIG Mainline Wayside ») ; sans produit : « Not set — a Turnkey tender carries a combination of several systems' products, whose matrix is still owed (DEC-048). » Note « Not editable, by decision — not a missing control. » | DEC-049, DEC-048 |
| Allocation model › « Model applied » | « Follows the product by default. This is the part that can be changed. » Tender SIG : « SIG Urban », « SIG Mainline Wayside — on the PBS/OBS/ABS keys », « SIG Mainline Onboard — on the PBS/OBS/ABS keys », présélection = produit du tender. Ailleurs : liste grisée « Per-system models — set by the tender's combination ». | DEC-047, DEC-061 |
| Allocation model › « Re-run on all requirements » | « Changing the model makes every derivation produced by the previous one wrong, so this re-derives the whole tender. » Encadré rouge « Changing the model would re-derive N requirements and destroy M recorded answers and K internal verdicts, including those already declared to the client. » (chiffres du tender ouvert) ; bouton rouge « ↻ Change model and re-run everything », désactivé. | DEC-050 (ALLOC-015) |
| Allocation model › « Re-run on all requirements » › note | « Unlike the per-requirement re-run, this one does not spare answered requirements (DEC-050): the model that produced them has changed, so what was built on it no longer holds. The two are deliberately not the same action, and one is never offered as a fallback for the other. » | DEC-050 |
| Compliance › « Gap strategies » (Gap Strategy Editor) | « What the responsible of a requirement can do about a Not compliant — and what each choice declares to the client. Written for this tender. » Une ligne par stratégie : nom modifiable (Entrée valide, Échap annule), résultat externe « Compliant » / « Not compliant » / « Pending », usage « used N× » ou « unused », corbeille. | DEC-110 |
| Compliance › « Gap strategies » › renommer et supprimer | Renommage : « Renamed to “{nom}” » ; refus « A strategy needs a name », « Another strategy already has that name ». Corbeille grisée sur une stratégie utilisée (« In use — rename it instead ») ; sinon « {nom} deleted ». | DEC-110 |
| Compliance › « Gap strategies » › ajout et liste vide | Champ « Strategy name », liste de résultat (« Pending » par défaut), « ＋ Add » (ou Entrée) : « {nom} added — declares {résultat} » ; refus « Name the strategy », « That strategy already exists ». Nouveau tender : « No strategy yet. Until there is one, a Not compliant is flagged Strategy missing and its external compliance stays Pending. » | DEC-110, DEC-108 |
| Compliance › « Gap strategies » › changement de résultat | Stratégie utilisée : confirmation sous la ligne « N requirements will change external compliance from {X} to {Y} · K corrected by the PM keep their value. », boutons « Cancel » / « Change and recompute » (toast « {nom} now declares {Y} — N requirements recomputed »). Stratégie inutilisée : appliqué tout de suite. | DEC-111 |
| Compliance › « Gap strategies » › note | « The external compliance of a requirement is derived: Compliant when its responsible answers Compliant, otherwise the result of the strategy they pick. A strategy in use can be renamed but not deleted; changing its result recomputes every requirement that uses it, after you confirm. » | DEC-106 |
| Capture & segmentation › « Conversion range » (Segmented Control) | « Which pages of the source document are captured at all. » « All pages » / « Specific pages » ; « Specific pages » fait apparaître un champ (« e.g. 1-12, 40, 55-58 », curseur placé dedans) et la note « Anything outside these pages is not captured, so it produces no requirements at all — this is not a filter on the Allocation table. » | — |
| Capture & segmentation › « Default table conversion format » | « Whether a table is captured as a picture of itself or as structured data. » « Image » / « Dataframe », avec la note « Image: faithful to the layout, nothing inside is searchable or extractable. Dataframe: rows and columns become data — which is what lets a table row become a requirement, below. » | — |
| Capture & segmentation › « Sentences in paragraphs » | « Whether a paragraph stays one block or is cut into one block per sentence. » « As source file » / « Split », avec la note « Splitting raises the requirement count and can separate a sentence from the one that qualifies it. Kept as the source file has it by default. » | — |
| Capture & segmentation › « Format of equations » | « Whether an equation is captured as a picture or as a formula. » « As images » / « As formulas ». | — |

### Modifié

| Zone › élément | Avant (8 sept.) | Maintenant | Réf. |
|---|---|---|---|
| Menu de gauche (Config Sidebar Nav) | 9 entrées avec des glyphes (◈ ◉ ⇄ ◐ ✦ ↺ ⇗ ◷ Aa). | 11 entrées avec des icônes au trait : General, Team & contributors, Reminders, Allocation model, Compliance, Appearance, Capture & segmentation, AI feedback, Q&A & submission, Versions, Language. | — |
| General › « Product line » | Liste modifiable (Turnkey, RCS, SIG, INFRA, Rolling Stock, Services), SIG présélectionné quel que soit le tender. | La ligne du tender en texte, non modifiable. « Chosen at creation and fixed afterwards (DEC-095) — it sets how allocation works. Correcting it means recreating the tender. » + « Not editable, by decision — not a missing control. » | DEC-095 |
| General › document source | « Source document » : « Active version used for review. », fichier actif, nombre de pages, « managed in Versions ». | « Documents » : « The tender's documents and every version of each. » / « Managed in Documents & versions, not here. » | — |
| Reminders (ex-« Workflow & milestones ») | Section des règles de passage de phase, des rappels et du verrou de revue. | Seuls « Overdue threshold » et « Maximum reminder cadence » restent (voir Retiré). | DEC-084 |
| Capture & segmentation › ordre et granularité | Document rendering, Uncertainty threshold, Default table granularity, Re-segmentation, Never overwrite. | Les 4 réglages de conversion en tête ; « Default table granularity » juste après le format de tableau, avec « … Only reachable once a table is converted as a dataframe — an image has no rows to map. » | — |
| Language › langue cible | « Default translation target » : French (FR) / German (DE) / Spanish (ES), « Used by the Translate tab in the review panel. » | « Working language » : « English », non modifiable ; « What a source in another language is translated into. » + « Not editable — translation always goes into English. » | — |

### Retiré

| Zone › élément | Ce qui disparaît, et ce qui le remplace s'il y a lieu | Réf. |
|---|---|---|
| Team & contributors › « Restricted view » | Choix « Redacted » / « Hidden » de ce qu'un manager voit hors de ses affectations. Plus aucun masquage : chacun lit tout le tender et ne modifie que son système. | DEC-012 |
| Team & contributors › « Assignment criteria » › puce « Discipline » | Restent « PBS (product) », « ABS (activity) », « OBS (organization) ». | — |
| Reminders › « Review milestone gate » | Interrupteur « Enforce full validation before export ». Plus de finalisation à verrouiller. | DEC-035, DEC-084 |
| Reminders › « Outdated-response re-flag » | « Substantive changes only » / « Any change ». Plus de statut « outdated ». | DEC-078 |
| Q&A & submission › « AI duplicate detection » | « Suggest merges before submission ». Plus de détection de doublons. | DEC-116 |
| Q&A & submission › « Internal review before sending » | « Require internal review stage ». | — |
| Versions › « Expert notification on version switch » | « Immediate » / « Grouped at change-review validation ». | — |

### Libellés

| Où | Avant | Maintenant |
|---|---|---|
| Menu et titre de section | « Team & experts » | « Team & contributors » |
| Team & contributors › sous-titre | « Experts available for requirement assignment during allocation. Each can be assigned requirements and receives a qualification link. » | « Contributors available for requirement assignment during allocation. Each can be assigned requirements and receives a link to their Compliance queue. » |
| Team & contributors › bouton et toast d'ajout | « Add expert » ; « Expert added » | « Add contributor » ; « Contributor added » |
| Menu et titre de section | « Workflow & milestones » | « Reminders » |
| Reminders › sous-titre | « Rules that govern phase transitions, reminders and the review gate. » | « How late answers are flagged and how often contributors are reminded. » |
| Reminders › « Maximum reminder cadence » | « Prevents reminder spam to experts. » | « Prevents reminder spam to contributors. » |
| General › sous-titre | « … The submission deadline drives the countdown and the overdue calculations. » | « … The submission deadline drives the countdown to submission. » |
| General › « Submission deadline » | « Sets the countdown and overdue thresholds baseline. » | « Drives the countdown to submission. » |
| Menu et titre de section | « AI & segmentation » | « Capture & segmentation » |
| Capture & segmentation › sous-titre | « How the document is processed into blocks, and how the AI surfaces its uncertainty. » | « How the source document is converted, how it is cut into blocks, and how the AI surfaces its uncertainty. » |
| Capture & segmentation › « Uncertainty threshold », encadré | « ⚠ Confidence is used internally to prioritize, never shown to users as a score. » | « ⚠ Segmentation confidence is used internally to prioritise; it is not shown as a score. » |
| Q&A & submission › sous-titre | « How clarification questions are consolidated and transmitted to the tender issuer. » | « How questions to the client are exported. » |
| Q&A & submission › « Issuer channel » | « Determines whether the batch is a simple export or a formatted submission. » ; « Buyer portal: the batch is exported to … » | « Determines whether the questions go out as a plain export or a formatted submission. » ; « Buyer portal: the questions are exported to … » |
| AI feedback › carte de taux | « Activity accepted » | « System accepted » |
| AI feedback › « This session » | « live signal from the review screen » | « live signal from Allocation » |
| AI feedback › étiquette d'une correction de système | « TYPO » | « SYS » |
| AI feedback › liste vide | « … Reassign a requirement or change an activity in the review screen — it will appear here instantly, silently logged. » | « … Reassign a requirement or change a system in Allocation — it will appear here instantly, silently logged. » |

### Style visuel

- Icônes au trait dans le menu de gauche, à la place des glyphes.
- Valeurs non modifiables (ligne, système, produit, langue de travail, « Documents ») affichées en texte simple dans la colonne du champ, sans cadre ni style propre.
- Relance globale : encadré à bordure `--warn` sur fond `--warn-soft`, chiffres en gras rouge ; bouton à contour rouge, à 50 % d'opacité quand il est désactivé.
- Liste OBS Turnkey : étiquettes en `--font-mono` à bordure `--line-2` ; partenaires en turquoise `--partner` (#1b9aaa) sur `--partner-soft`, couleur hors échelle suivie.
- Stratégies d'écart : champ, liste de 132 px, usage, corbeille de 28 px ; confirmation sur fond `--warn-soft` ; liste vide en cadre pointillé.
- Thème : aperçus aux nouvelles couleurs (#071A30 / #4C82FF en sombre, #ffffff / #0B294A en clair) ; titres de section en `--font-heading`.

### Points incertains

- Sur un tender sans produit qui n'est pas Turnkey (RSC, Services), « Product » affiche quand même le texte de combinaison Turnkey : probable défaut du prototype.
- « Model applied » est une liste grisée pour toute ligne autre que SIG, RSC compris ; le comportement attendu pour RSC n'est pas montré.
- Les valeurs non modifiables n'ont aucun style dédié (texte brut) : forme cible à confirmer.
- « Source document language » et « Interface language » restent des listes modifiables non câblées, alors que la langue source est unique par tender (DEC-096) (à vérifier).

## Team casting

`dashboard-et-config.html` · route `#team` · captures : [avant](captures/07-equipe-avant.png), [maintenant](captures/07-equipe-apres.png)

**En bref.** Les systèmes suivent désormais la liste de référence à 16 codes (le libellé est le code), et les périmètres sont une liste fermée, la même pour tous les systèmes et identique à « OBS · team » d'Allocation : DBM, Risk, BTM, Wayside, Design, V&V. Un système n'a plus besoin de manager : le chef de projet le staffe directement, la ligne du manager dit « No manager — contributors only » au lieu de bloquer. Une personne = un système : dans la recherche, quelqu'un qui appartient déjà à un autre système reste listé en grisé avec ce système, et son ajout est refusé. Partout, « activity » devient « system » ; « + Add system » propose les codes restants, jamais sur un tender SIG qui n'a qu'un système.

### Ajouté

| Zone › élément | Ce qu'on voit, ce qui se passe | Réf. |
|---|---|---|
| Système › « + Add someone » › résultats de recherche (Add-Person Flow, Search-to-Add Combobox) | Une personne déjà staffée dans un autre système reste listée, grisée, avec « In {CODE} — one system per person » à droite (même infobulle). La choisir (clic ou Entrée) affiche le toast « {nom} already belongs to {CODE} — a person is staffed on one system only », sans passer à l'étape périmètre. | DEC-102, DEC-124 |
| Système › « + Add someone » › personne déjà dans ce système | Affiche « Already in {CODE} » et reste choisissable, pour la placer sur un autre périmètre du même système. | DEC-102 |
| Système › « + Add someone » › clic sur « Add » | Le même refus « une personne = un système » est vérifié à la confirmation, avant le contrôle de doublon (« {nom} is already staffed here — … », inchangé). | DEC-102 |

### Modifié

| Zone › élément | Avant (8 sept.) | Maintenant | Réf. |
|---|---|---|---|
| Liste des systèmes (Cast Activity Group, Cast Coverage Card) | 7 « activities » inventées avec libellé (SIG « Signalling & Urban », MLN « Mainline », INF, PWR, TLC, CVL, SYS). | 7 codes de la liste de référence : SIG, TRK, SEN, POS, COM, RST, RAMS. Le libellé est le code, qui apparaît donc deux fois (étiquette et titre). | DEC-032, DEC-045 |
| Tender SIG › liste des systèmes | Les mêmes 7 activités que sur STB-2026. | Un seul système « SIG » (avec manager, étiquette « model »), staffé par périmètre ; pas de « + Add system ». | DEC-044 |
| En-tête d'un système › étiquette de modèle | « model » sur SIG seulement, « manual » ailleurs. | « model » sur SIG et RST, « manual » ailleurs. | DEC-059 |
| En-tête d'un système › ligne du manager | « Unassigned » quand aucun manager n'est casté. | « No manager — contributors only », en gris neutre. | DEC-124 |
| Qui peut staffer un système | Le chef de projet seulement sur une activité qui a un manager ; un manager sur la sienne. | Le chef de projet sur tout système, manager ou non ; un manager sur le sien. Ailleurs, note « Read-only — {nom} manages this system, not you. » ou « Read-only — no manager here; the project management team staffs it. » | DEC-124, DEC-003 |
| Boutons ✕ de retrait (Cast Person Row) | Visibles et actifs même dans un groupe en lecture seule. | Seulement là où la personne qui regarde peut modifier. | DEC-124 |
| Périmètres d'un système (Cast Perimeter Group) | Liste propre à chaque activité (ex. « Interlocking », « ATP / ATC »… sur SIG), certaines sans périmètre (staffage direct seulement). | Les mêmes 6 périmètres pour tous : « DBM », « Risk », « BTM », « Wayside », « Design », « V&V », chacun marqué « ⚠ Unstaffed » tant qu'il est vide. « Staffed directly (no perimeter) » seulement si quelqu'un y est. | DEC-036 |
| Couverture (badge du système, bandeau du chef de projet) | Part des périmètres de l'activité pourvus (1 seul emplacement si staffage direct). | 6 périmètres + l'emplacement direct = 7 ; « Fully staffed » seulement si les 7 sont pourvus, sinon « N/7 staffed » ou « Nothing staffed ». | DEC-036 |
| « + Add someone » › étape 2, choix du périmètre | Champ libre avec suggestions, « Perimeter — pick existing, type a new one, or leave blank » ; Entrée validait. | Liste fermée : « — No perimeter — staffed directly — » puis les 6 périmètres ; validation par « Add » (plus de validation par Entrée dans le champ, à vérifier). | DEC-036 |
| Puce « Just added » | « ↻ Just added {nom} — staffing them on another perimeter too? Search their name again in the right spot below. » | « ↻ Just added {nom} — staffing them on another perimeter of {CODE} too? Search their name again in its add box — one system per person. » | DEC-102 |
| Bouton « + Add activity » devenu « + Add system » › liste proposée | Fenêtre « Add activity » : 4 activités inventées (« RST — Rolling Stock », « COM — Communications », « SAF — Safety & RAMS », « ARC — Architecture & Buildings »). | Fenêtre « Add system » : les 9 codes restants (AFC, CJV, CYB, DEQ, ILS, PSD, SCADA, OCS, SPM), affichés « {CODE} — {CODE} ». Chef de projet seulement, jamais sur un tender SIG. | DEC-032 |
| « + Add system » › résultat | L'activité ajoutée arrivait sans manager, donc impossible à staffer ; toast « {libellé} added — cast a manager to it to start staffing ». | Le système s'ouvre avec sa boîte « + Add someone » ; toast « {CODE} added — staff it below ». | DEC-124 |

### Retiré

| Zone › élément | Ce qui disparaît, et ce qui le remplace s'il y a lieu | Réf. |
|---|---|---|
| Système sans manager › bloc bloquant | « This activity hasn't been cast to a manager yet — nobody can staff it until it is. Assign an activity manager in the project wizard or from here once that flow is wired. », sans périmètres ni ajout. Remplacé par le staffage direct (voir Modifié). | DEC-124 |
| Badge « No manager cast » et état « No manager cast yet » du bandeau de couverture | Remplacés par la seule couverture : un système n'est « Nothing staffed » que si personne n'y est. | DEC-124 |
| Création d'un périmètre à la volée | On ne peut plus taper un nouveau périmètre : la liste est fermée et partagée. | DEC-036 |

### Libellés

| Où | Avant | Maintenant |
|---|---|---|
| Sous-titre, vue chef de projet | « Which activities and perimeters still need someone, at a glance — click a card above to jump to it. » | « Which systems and perimeters still need someone, at a glance — click a card above to jump to it. » |
| Sous-titre, vue manager | « Your own activity, expanded and ready to staff. Everything else stays visible for context, read-only. » | « Your own system, expanded and ready to staff. Everything else stays visible for context, read-only. » |
| Groupe « Project management team » | « Whole-project scope — no activity restriction » | « Whole-project scope — no system restriction » |
| Étiquette « manual », infobulle | « No allocation model — requirements routed here are allocated manually by this activity's contributors » | « … by this system's contributors » |
| « + Add someone » › aide de l'étape 2 | « Leave blank to staff {libellé} directly, with no perimeter — that's a valid, ordinary choice, not a skipped step. » | « Leave on "No perimeter" to staff {CODE} directly — that's a valid, ordinary choice, not a skipped step. » |
| Fenêtre d'ajout de système, liste épuisée | « Every activity in the reference list is already on this project. » | « Every system in the reference list is already on this project. » |

### Style visuel

- Option de recherche bloquée : texte `--text-3`, avatar à 50 % d'opacité, curseur « interdit » ; mention du système à droite en `--text-xs`.
- « No manager — contributors only » en gris neutre : plus d'état d'alerte pour un manager manquant.
- Icônes au trait : loupe de la recherche (avant « ⌕ »), cadenas de la lecture seule (avant l'emoji 🔒), œil du bouton de démo (avant l'emoji 🎭).
- Chaque système affiche désormais 6 périmètres : les vides apparaissent encadrés en rouge (« ⚠ Unstaffed », fond `--warn-soft`), d'où beaucoup plus de rouge qu'avant.
- L'étape 2 est une liste déroulante qui garde l'apparence du champ en pointillé ; titre « Team casting » précédé de la barre rouge `--brand-red`.

### Points incertains

- La couverture « N/7 » et les marques « ⚠ Unstaffed » comptent les 6 périmètres partagés plus l'emplacement direct, alors que DEC-124 dit « non staffé = personne dessus » (règle que suivent la carte Team casting du tableau de bord et les statistiques) : un système staffé seulement en direct affiche « 1/7 staffed » et six périmètres rouges. À arbitrer.
- DEC-003 et DEC-124 donnent aussi aux contributeurs d'un système la gestion de ses rattachements ; le prototype ne permet pas de simuler un contributeur, ce cas n'est donc pas visible.
- Chaque système a pour libellé son code (légende des 16 codes non fournie, DEC-032), d'où « SIG » répété dans les cartes et les en-têtes.
- L'étiquette « model » sur RST repose sur une hypothèse non confirmée (DEC-059).
- Le casting n'alimente ni Allocation ni Compliance dans le prototype (listes de managers distinctes) : le lien attendu dans le produit n'est pas montré.

## Contrôles de démo — à ne pas reproduire

Ce que le prototype montre seulement pour la démonstration, écran par écran : sélecteurs « View as », remise à zéro, données et IA simulées, routes de démo. Rien de tout cela n'est à construire tel quel ; la liste dit ce qui a changé depuis le 8 septembre pour qu'on ne le prenne pas pour une fonction.

### Socle commun — en-tête, charte, tableaux

- **Modifié** — Remise à zéro de la démo (bouton « ↺ Reset demo » de l'accueil, ou Ctrl+Maj+R avec la confirmation « Reset the demo to its initial state? », tous deux inchangés) : elle efface aussi les colonnes personnalisées et leurs largeurs, les partenaires, les stratégies d'écart, les risques, la documentation d'écart, le journal d'activité, les questions et le registre Q&A, les versions de documents déposées et la progression d'Allocation, et réaffiche le bloc « How a tender travels through SRM » de l'accueil.
- **Modifié** — « View as » d'Allocation : infobulle « Preview a manager's restricted view (demo only) » → « Preview a contributor's view (demo only) » ; le menu ne propose plus que l'administrateur et deux contributeurs ; la vue choisie ne masque ni ne caviarde plus rien, le bandeau dit « Viewing as … — contributor on …: everything is readable, only … can be changed. » au lieu de « Restricted view — … Passages outside their scope are redacted. » (DEC-012). Détail : chapitres Allocation.
- **Modifié** — sélecteur de démo de Compliance (« DEMO Project manager ▾ ») : l'emoji 🎭 devient l'icône œil ; la vue contributeur montre désormais tout le tender, en lecture seule hors de son système (DEC-012). Détail : chapitre Compliance.
- **Ajouté, désactivé** — chat du tender « Ask the tender » (Tender Chat) : panneau flottant prévu dans le shell, désactivé depuis le 1ᵉʳ octobre ; rien ne s'affiche. Ne pas le construire (REX et Chat hors V1, DEC-021).

### Accueil

- **Modifié** — « ↺ Reset demo » (en-tête, même infobulle, même confirmation « Reset the demo to its initial state? This clears all progress made during the session. ») réaffiche aussi le bloc « How a tender travels through SRM ». Portée complète de la remise à zéro : chapitre Socle commun.
- **Modifié** — Deux tenders de démo s'ouvrent désormais : RFP-2026-114 (SIG) en plus de STB-2026 (Turnkey). Le message affiché au clic sur un tender d'illustration devient « This is a demo-only project in this prototype — open … (STB-2026) or … (RFP-2026-114) for a full, navigable build » (avant : STB-2026 seul) ; le pied « Demo project — list & status only » ne change pas. Dans le produit, tout tender s'ouvre.
- **Ajouté** — La carte « Pick up where you left off » prend le tender marqué comme principal dans les données de démo, à défaut le premier tender ouvert et construit : ce n'est pas une règle produit.

### Création d'un tender

- **Modifié** — Un tender de ligne SIG créé ici s'ouvre ensuite sur le contenu de démo du tender SIG RFP-2026-114 (avant : sur celui de STB-2026, comme toute création) ; les autres lignes gardent le contenu de STB-2026. Détail : chapitres Allocation.

### Tableau de bord

- Modifié : bandeau « Prototype scope » d'un tender créé dans l'assistant. Avant : « … its Allocation and Compliance screens below reuse the (nom masqué) (STB-2026) reference content for this test phase, rather than data of its own. Team casting above is this project's own, from the creation wizard. » Maintenant : « … Allocation, Compliance, Statistics and Team casting reuse a reference tender's content for this test phase. »
- Inchangé : lien « DEMO Compliance (contributor) → » dans l'en-tête ; « Bid Director: {nom} » toujours écrit en dur dans le bandeau.
- Inchangé, chiffres figés à calculer dans le produit : « 3 docs · 1 processing », « 5 questions · 1 answered », « 2 uncertain segmentations », « 2 questions to send ». « Recent comments » et « Recent activity » sont en partie écrits à la main ; aucun des deux ne lit le journal d'activité.

### Statistiques

- Ajouté : « Counted from Compliance — open it once and these figures fill in. » dans les blocs « Progress to the client » et « Not compliant by gap strategy », tant que Compliance n'a pas publié ses totaux (tender neuf du prototype).
- Aucun autre contrôle de démo dans le panneau.

### Documents & versions

- Modifié : l'écart d'une nouvelle version reste inventé (« +a ~m −r », numéro mineur +1, date « Today », aucun fichier lu). Le choix des exigences « modifiées » est maintenant simulé lui aussi : ce sont les premières exigences du document, celles qui ont des réponses d'abord.
- Modifié : seuls deux documents de STB-2026 et un de RFP-2026-114 ont des exigences connues. Une nouvelle version de n'importe quel autre document annonce donc toujours 0 réponse rouverte.

### Allocation — page, tableau, vue Document, versions

- **Modifié — « View as » (icône œil de l'en-tête).** L'infobulle « Preview a manager's restricted view (demo only) » devient « Preview a contributor's view (demo only) ». La liste proposait l'admin + trois managers (« SIG manager », « Mainline manager », « Infrastructure manager ») ; elle propose l'admin + deux contributeurs, un SIG et un sur un système sans modèle (« SIG contributor », « SEN contributor »).
- **Modifié — bandeau de View as.** « 🔒 Restricted view — showing only requirements assigned to {nom}. Passages outside their scope are redacted. » devient, avec une icône œil, « Viewing as {nom} — contributor on {SYS}: everything is readable, only {SYS} can be changed. ». « Exit to admin view » ne change pas.
- **Modifié — toast de View as.** « Viewing as {nom} — restricted to assigned requirements » devient « Viewing as {nom} ». L'aperçu survit au passage Review / Document (il se perdait). (DEC-012)
- **Retiré —** le réglage « Restricted view (Redacted / Hidden) » de Configuration ne pilote plus cet écran.
- **Modifié —** le menu des notifications garde son contenu fixe de démo (des exigences du tender STB-2026). Sur un autre tender, le clic donne désormais le toast « This requirement isn't in this tender ».
- **Ajouté —** les largeurs de colonnes et les colonnes personnalisées sont gardées dans la mémoire du shell et effacées par « Reset demo ».
- **Ajouté —** les modèles derrière « Re-run » sont simulés (résultat fixe pour une même exigence et un même modèle).
- **Ajouté — données de démo qui rendent les nouveautés visibles.**
  - Historiques de versions écrits à la main sur la démo STB-2026 et sur RFP-2026-114 : Changes visible. La capture a une version par document : Changes masquée.
  - 12 % d'exigences To review semées sur STB-2026.
  - Un partenaire semé sur deux exigences.
  - Une figure et un tableau d'interfaces ajoutés à la capture.

### Allocation — panneau de détail et modèle d'allocation

- Modifié : « View as » ne montre plus une vue restreinte. Il prévisualise un contributeur (un de SIG et un de SEN proposés) et choisit ainsi la vue du panneau. Bannière « Viewing as {Nom} — contributor on {CODE}: everything is readable, only {CODE} can be changed. » au lieu de « Restricted view — … Passages outside their scope are redacted. »
- Ajouté : annuaire simulé (20 noms fictifs) derrière « Search a person… » ; une personne choisie y entre avec le rôle « Assigned from search ».
- Ajouté : modèles d'allocation simulés derrière « ↻ Re-run » (tirages déterministes ; vocabulaires inventés pour SIG Urban et les produits RST).
- Ajouté : historiques d'activité semés par le shell. L'auteur d'un changement détecté est la personne « vue comme » ; les heures sont au format « Today, HH:MM ».
- Retiré : entrées de journal codées en dur, carte de suggestion de l'IA de démonstration, toast de rappel factice « Reminder created for … — due Friday ».
- Inchangé, mais démo : onglet « REX » (titres seulement) ; langues de lecture simulées (German, Spanish) dans « Read in ».

### Compliance

- Modifié : bouton « DEMO » du contrôle « Viewing as » : icône œil au lieu de 🎭.
- Modifié : la liste des personnes ne propose plus que deux contributeurs (un SIG, un SEN) au lieu de trois.
- Modifié : « My team only » n'est plus actif à l'ouverture (le tableau du chef de projet montre tout) ; il se réactive quand on repasse en chef de projet ou qu'on change de personne.
- Modifié : passer en contributeur ou changer de personne vide la sélection, désactive « My system » et ouvre la première affectation de sa file.
- Modifié : route `#compliance-contributor` : arrive en contributeur SIG sur tout le tender, panneau de décision ouvert sur la première affectation de sa file (avant : tableau réduit à son activité, panneau vide).
- Ajouté : données de démo qui rendent visibles des structures nouvelles : un partenaire sur le tender Turnkey de démo, deux équipes sur une exigence, le tender SIG de démo avec ses 12 exigences, des questions publiées d'autres soumissionnaires, des stratégies et risques préremplis.
- Ajouté (substituts) : « Similar » calculé par mots communs (25 % au moins, trois au plus), REX en exemples fixes, Chat non construit (« Chat isn't built yet — … »).
- Ajouté : la touche Q du chef de projet dépose une question générique « [Draft] Clarification needed on {ID}: … ».
- Inchangé, à ne pas reproduire : l'export n'affiche que des toasts, aucun fichier ; brouillons et mises de côté ne vivent que dans la session du navigateur (DEC-090 les veut côté serveur, privés à leur auteur).

### Q&A

- Retiré : la boîte d'import simulée (« ⬆ Choose a file (simulated) », mode collage, extraction factice de 50 paires précédée de la ligne « Extracting… »).
- Modifié : l'import reste simulé. Un clic suffit, sans choix de fichier ; une roue et « Importing… » s'affichent environ 0,9 s ; les réponses sont écrites à la main. Seul le premier import produit une réponse à confirmer, avec une certitude fixe de 63 %. Les 15 Q&A d'autres soumissionnaires sont fixes, dont un quart environ sans exigence.
- Inchangé dans le principe : l'export n'écrit aucun fichier. « Export to Excel » n'affiche qu'un toast, comme l'ancien export du lot.
- Modifié : les dates de démo passent du 22 / 24 août au 17 / 24 juillet. Ce sont des textes fixes, identiques sur tous les tenders, et les drapeaux « passed » / « overdue » sont écrits en dur.

### Risks — nouvel écran

- Ajouté : l'export est simulé. Aucun fichier n'est produit, et le message se termine par « (simulated) » (« Risk list exported — N risks with their justification (simulated) »).
- Ajouté : des risques de démo sont pré-remplis, six sur STB-2026 et un sur RFP-2026-114 (DEC-112).

### Configuration

- Ajouté : bandeau « ⚠ Demo only: this screen shows the setting and what changing it would destroy. Nothing here is wired — selecting another model changes no derivation, and no re-run is performed in this build. » (Allocation model) ; infobulle « Not wired in this build » sur le bouton de relance.
- Modifié : bandeaux « ⚠ TE2 — demo only: … » de General, Reminders, Capture & segmentation, Q&A & submission et Versions réécrits (plus de « Follow-up », de « review screen » ni de bouton « Simulate upload — v2.2 » ; Versions dit désormais « … Versions are per document, in Documents & versions; uploading a new version of the main document there is what the dashboard reacts to. »).
- Modifié : note « (TE2 — demo only, doesn't change what the review table actually offers) » devenue « … what the Allocation table actually offers ».
- Modifié : toast de « Save configuration » : « Theme, partners and gap strategies apply immediately — other settings on this page aren't wired in this build » (avant : « Theme and restricted-view mode apply immediately — … »). « Discard changes » inchangé.
- Inchangé : AI feedback garde des taux et des motifs récurrents écrits à la main (3 motifs au lieu de 4) ; la liste de « Team & contributors » reste une liste de démo, indépendante du casting.

### Team casting

- Modifié : sélecteur « Viewing as » : groupe « Activity managers » renommé « System managers » ; rôles « Mainline / Infrastructure / Power Supply / Telecom / Systems Integration manager » devenus « TRK / SEN / POS / COM / RAMS manager » (« SIG manager » inchangé). On ne peut toujours simuler que le chef de projet ou un manager.
- Modifié : bouton « DEMO Simulate 200 roster » : icône œil ; infobulle « Generates ~185 additional staffed rows across every system/perimeter, … » ; il remplit aussi les systèmes sans manager et respecte « une personne = un système » ; toast « Simulated N additional staffed rows — N total, spread across every system ».
- Inchangé : annuaire « SSO » simulé ; les modifications du casting ne sont pas conservées en quittant l'écran.
