# Variantes par type de tender

## Décisions de référence

DEC-004 : les types à couvrir sont **Turnkey, SIG, Mainline, RSC** (réponse utilisateur 1).
DEC-005 : le modèle et les actions de SIG sont les mêmes en tender SIG autonome et dans le système SIG d'un Turnkey. Dans le second cas, les contributeurs SIG ne gèrent pas le projet global : documents, équipes au niveau projet et relation client (réponse 2). Cela n'enlève pas leur droit de gérer les rattachements de leur propre système (DEC-003).
DEC-006 : SIG conserve tous les écrans ; retirer de l'interface tout ce qui concerne la passe 1 Turnkey, dont ses ABS/PBS/OBS spécifiques. Le panneau de détail s'ouvre directement dans la configuration SIG (réponses 3–4).
DEC-007 : le type sélectionne automatiquement la configuration/référentiels et modèles applicables. La réponse « oui » ne précise pas si le type reste modifiable après traitement : OPEN-05 reste limité à ce changement (réponse 5).

## Matrice d'applicabilité

| Fonction | Tender Turnkey | SIG au sein d'un Turnkey | Tender SIG autonome | Mainline / RSC autonomes |
|---|---|---|---|---|
| Passe de distribution Turnkey | Oui, au niveau global | Déjà issue de cette distribution | Non | Non, intention existante pour types non-Turnkey |
| Allocation de système | Modèle propre au système | Modèle SIG | Même modèle SIG | Configuration propre, pas de paramètres SIG copiés implicitement |
| Écrans | Référence du prototype | Mêmes actions métier SIG ; gestion globale réservée à l'équipe projet | Tous conservés, adaptés à SIG | Parcours jusqu'à allocation inclus ; détails propres non documentés par le prototype |
| Champs ABS/PBS/OBS Turnkey | Visibles dans la passe 1 | Ne pas les confondre avec ceux de SIG | Absents, pas simplement vides | Absents dans la variante non-Turnkey ; valider détails particuliers |
| Détail d'allocation | Distribution puis détail de système | Configuration SIG pour le travail SIG | Directement configuration SIG | Configuration du type correspondant |
| Casting | Équipe projet + rattachements par système | Gestion de ses rattachements, pas du casting global | PM + contributeurs SIG ; pas de hiérarchie interne | Même principe de droits ; vocabulaire propre à confirmer si différent |
| Conformité | Équipes → systèmes → exigence | Réponses SIG alimentent le projet global | Équipes → exigence | Règles communes, pas de distribution Turnkey |
| Documents / relation client | Équipe de gestion globale | Pas de gestion globale par simple rattachement SIG | Équipe projet SIG | Équipe du projet correspondant |

Les variantes Mainline/RSC font partie du périmètre, mais leurs particularités non fournies restent OPEN-15. L'absence de description ne signifie ni exclusion du pilote ni équivalence automatique avec SIG.

**Orthographe : RSC, et seulement RSC (DEC-059).** Le nom du système est **RSC**, tel que DEC-004 l'écrit — c'est la seule autorité disponible, et « RCS » que proposaient le wizard de création et les paramètres en est une inversion, alignée depuis. **RST reste distinct** : c'est un code de la capture Turnkey, donc un sous-système, et rien de fourni ne dit qu'il est le pendant de RSC. Les deux ne sont pas traités comme synonymes ; le prototype marque RST comme porteur d'un modèle pour rendre le routage démontrable, et ce point-là reste une hypothèse explicite, pas un fait. « Rolling Stock » n'est validé ni comme système ni comme code.

## Systèmes, produits et modèles

DEC-045 à DEC-049. Ce que les décisions antérieures appelaient « activité » s'appelle **système**. Le mot « activité » revient à l'**ABS — Activity Breakdown Structure**, qui désigne les activités *au sein* des systèmes ; c'est le doublon entre les deux qui a motivé le renommage, pas un changement de modèle.

**Les quatre niveaux.**

| Niveau | Ce que c'est | Exemples | Qui le fixe |
|---|---|---|---|
| Système | Ce sur quoi le tender est émis. **Un seul par tender** | Turnkey, SIG, RSC | La création du tender |
| Sous-système | Ce vers quoi l'allocation d'un Turnkey répartit, à l'intérieur de son système | SIG, RST, OCS, TRK… | L'allocation |
| Produit | La déclinaison d'un système, qui **sélectionne le modèle** | SIG : Urban, **Mainline Wayside**, **Mainline Onboard** (DEC-061) · RSC : TGV, métro… | La création, **non modifiable ensuite** |
| Modèle | Ce que le produit applique pour dériver ABS → PBS → OBS | — | Le produit par défaut, **réglable dans les paramètres** |

**Le partage système / sous-système se lit sur la provenance, pas code par code (DEC-058).** La liste de référence des 16 codes (DEC-032) est la colonne *Responsible Entity* d'une capture **Turnkey** — Riyadh L7. Ce vers quoi une distribution Turnkey répartit est, par la définition du tableau ci-dessus, du **sous-système**. La liste entière est donc au niveau sous-système ; il n'y a rien à trancher entrée par entrée, et c'est la provenance qui le dit, pas une appréciation sur chaque code.

Les **systèmes** sont les types de tender de DEC-004 : Turnkey, SIG, RSC — « Mainline » étant un produit SIG et non un système, par DEC-047. Deux codes existent donc **aux deux niveaux** : SIG est un sous-système d'un Turnkey *et* un système quand il porte son propre tender ; RSC de même, sous réserve de son orthographe et de son rapport à RST (ci-dessous). Ce n'est pas une anomalie de modélisation — ce sont exactement les deux colonnes SIG de la matrice d'applicabilité.

Ce double statut explique aussi pourquoi ces deux codes-là sont les seuls à porter un modèle d'allocation (`ACTIVITY_MODEL`) : un code a un modèle **parce qu'**il tient debout comme tender autonome, et le Turnkey réutilise ce modèle quand il route vers lui. Le champ unique qui les mélange aujourd'hui n'a donc pas à être scindé en deux listes ; ce qui doit être marqué, c'est ce petit ensemble de codes qui vaut aussi comme système.

**Turnkey est le cas particulier.** Il n'a pas de produit propre : il porte une **combinaison** de produits de plusieurs systèmes, désignée d'un nom d'usage — TGV, Métro… Les produits y sont corrélés : un produit Urban (métro, tramway) ne se combine pas avec des trains à grande vitesse. **La matrice qui dit ce que contient chaque combinaison est à fournir.** D'ici là, la traiter en placeholder explicite à l'écran, comme la liste de catégories de non-conformité (DEC-038) — pas en la remplissant de valeurs plausibles.

**Le renommage est fait.** Le vocabulaire « système » est appliqué à l'ensemble des specs vivantes (`docs/current`) et aux commentaires du prototype. Deux réserves : les **identifiants de code** (`CAST_ACTIVITIES`, `activityId`, `deriveActivityCompliance`…) gardent leur nom — un refactor purement cosmétique sur six fichiers, sans bénéfice pour l'utilisateur — et les **documents d'archive, tickets et comptes rendus de test** ne sont pas réécrits : ce sont des traces de ce qui a été dit à une date, pas des specs. Là où le mot « activité » subsiste dans `docs/current`, il désigne l'**ABS** et garde son sens propre.

**Un modèle, concrètement, c'est un sous-ensemble de clés.** Pour SIG, le classeur PBS / OBS / ABS ([KEYS](KEYS.md)) porte les trois axes avec une croix par produit ; le modèle Mainline Wayside est ce qui est coché Mainline Wayside. Le prototype le charge tel quel pour les deux produits Mainline.

**Produit figé, modèle réglable.** Le produit décrit ce que le tender *est* : il se choisit à la création et ne se corrige pas ensuite (une erreur se règle en recréant le tender, cohérent avec OPEN-05). Le modèle qu'il applique, lui, se change dans les paramètres du projet — et ce changement déclenche la relance globale décrite en ALLOC-015.

**Fait au 21 septembre 2026.** Le champ « System » du wizard de création portait une seconde liste de systèmes (Mainline, Urban / Metro, Tramway…) sous la ligne produit — le même niveau dit deux fois. Il est devenu ce niveau-ci : **Produit** pour un tender spécialisé, **Combinaison** pour un Turnkey. Seuls les produits de SIG sont connus (Urban, Mainline Wayside, Mainline Onboard, depuis les clés) ; pour tout le reste le champ affiche un placeholder explicite au lieu d'une liste plausible — combinaison Turnkey comprise, dont la matrice reste due (DEC-048). Le produit choisi est désormais **transporté jusqu'au projet créé**, ce qui n'était pas le cas : le wizard le collectait et `addProject` le jetait, si bien qu'un tender créé dans l'application ne pouvait jamais avoir de produit ni, donc, de clés.

## Tender SIG de démonstration — RFP-2026-114

Depuis le 21 septembre 2026 : **« Line 4 Resignalling — ETCS L2 », produit Mainline Wayside**, pour porter les clés réelles (DEC-061). Le contenu urbain / CBTC décrit ci-dessous a été réécrit en conséquence — interlockings, RBC, passages à niveau — sur les trois écrans qui le portent. Le nom « Urban Line 4 » dans ce qui suit est historique.

DEC-044 : le prototype doit porter un tender **SIG autonome réellement construit**, à côté du Turnkey STB-2026. Jusqu'ici la colonne « Tender SIG autonome » de la matrice ci-dessus n'était vérifiable sur aucun projet : `RFP-2026-114 · Urban Line 4 Signalling Upgrade` existe dans la liste des tenders avec `line:"SIG"`, mais sans contenu propre — l'ouvrir affichait le chrome mono-passe par-dessus les exigences et les données en forme Turnkey de STB-2026.

Le projet est construit **avec son propre contenu** de signalisation. Réutiliser le texte d'Energy Monitoring System a été écarté : un tender de signalisation qui parle de consommation énergétique invalide la démonstration qu'il est censé porter.

**Ce que le profil implique, au-delà de la matrice.**

- **Une seule passe d'IA.** Pas de distribution entre sous-systèmes : le tender est déjà SIG. La dérivation est directe, **ABS → PBS → OBS → personne** (ALLOC-003, DEC-008).
- **La dimension système disparaît de l'allocation.** Pas de colonne Système, pas de branches multiples : une exigence donne une dérivation et une équipe. Ce n'est pas un affichage allégé d'un modèle Turnkey, c'est un modèle plus court — conformément à « Absents, pas simplement vides » de la matrice.
- **Conformité équipes → exigence.** Compliance perd son niveau intermédiaire « assignation par système » : la consolidation se fait des équipes vers l'exigence directement. La règle du plus restrictif (DEC-037) s'applique inchangée, sur un niveau de moins.
- **Casting.** PM et contributeurs SIG, sans hiérarchie interne. Les périmètres restent la liste partagée de DEC-036.

**État du code à la date de cette spec.** La plomberie mono-passe existe déjà : `runsPassOne()` vaut faux dès que la ligne du tender n'est pas Turnkey, et l'interface de passe 1 disparaît alors. Ce qui manque est le contenu du projet, son marquage comme projet construit, et la suppression effective du niveau système côté Compliance. Deux défauts connus se referment avec ce travail : le dashboard qui affichait « SIG » sur un tender traité partout ailleurs comme Turnkey, et l'ordre de dérivation du code, resté `PBS → ABS → OBS` contre ALLOC-003 et ALLOC-T02.

## Critères d'acceptation

- TYPE-T01 : créer SIG conserve les écrans du produit et n'affiche aucun champ, filtre, étape ou action réservés à la distribution Turnkey.
- TYPE-T02 : le panneau de détail SIG ouvre directement sa configuration, sans passage par un panneau Turnkey vide.
- TYPE-T03 : un même cas SIG reçoit les mêmes règles d'allocation dans le projet autonome et dans la branche SIG Turnkey ; les pouvoirs de gestion globale diffèrent selon le rattachement.
- TYPE-T04 : créer Turnkey conserve les deux passes et la consolidation multi-système.
- TYPE-T05 : Mainline et RSC chargent leur configuration ; aucune substitution silencieuse par SIG ou Turnkey si elle manque.
- TYPE-T06 : tous les parcours et tests annoncent leur type de tender ; un test Turnkey ne vaut pas recette SIG/Mainline/RSC.
- TYPE-T07 : ouvrir RFP-2026-114 affiche ses propres exigences de signalisation, jamais celles d'Energy Monitoring System, et aucun bandeau de contenu réutilisé.
- TYPE-T08 : sur ce tender, aucune exigence ne porte plus d'un système, et l'axe système est absent de la table, du panneau de détail, des filtres et de Compliance.
- TYPE-T09 : la chaîne de dérivation y est lue ABS puis PBS puis OBS, dans cet ordre, sur tous les écrans qui l'affichent.
- TYPE-T11 : sur RFP-2026-114, ABS, PBS et OBS proviennent des clés cochées Mainline Wayside ; aucune valeur inventée ne subsiste dans ses dérivations.
- TYPE-T10 : la ligne produit annoncée par le dashboard est celle du projet ouvert ; basculer de STB-2026 à RFP-2026-114 change l'affichage et le comportement ensemble, jamais l'un sans l'autre.

## Périmètre de livraison

DEC-022 : premier parcours livré de la création jusqu'à la **validation de l'allocation**, pour les quatre types. Conformité, Q&A et export client restent spécifiés pour la suite du produit, sans être des conditions d'acceptation de ce premier parcours. REX/Chat sont hors V1 (DEC-021).
