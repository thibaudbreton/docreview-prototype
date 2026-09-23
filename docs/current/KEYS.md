# Clés PBS / OBS / ABS — le fichier de référence et sa lecture

Source : classeur **« PBSOBSABS Keys v260720.xlsx »**, fourni le 21 septembre 2026 pour le produit **Mainline Wayside** de SIG. Il n'est pas versionné dans ce dépôt ; ce qu'il contient l'est, sous forme générée : `build_keys.py` le lit et écrit `keys.js`, que `build_merge.py` inline dans le prototype. Remplacer le classeur, relancer le script, rebâtir — rien n'est retapé à la main.

## Comment le fichier est construit

**Trois feuilles, trois clés, une par axe.** Chacune est une **liste de référence partagée, filtrée par produit** : les colonnes `URBAN` / `Mainline Wayside` / `Mainline Onboard` portent une croix là où l'entrée s'applique. C'est DEC-047 rendu concret — *le produit sélectionne le modèle* — et le « modèle » est un sous-ensemble d'un vocabulaire commun aux trois produits.

| Feuille | Ce que c'est | Structure | Volume |
|---|---|---|---|
| **PBS** | Product Breakdown Structure — les éléments du produit | Arbre à trois niveaux : famille (`2` Signalling, `3` Infrastructure, `4` Telecoms, `5` M&E, `6` Services, `7` Transverse, `8` Civil Works, `12` Digital) → sous-système (`2.1` IXL, `2.2` ATC Mainline Wayside…) → élément (`2.1.2` Point Machine…) | 223 éléments ; 48 cochés Mainline Wayside, 34 Urban, 40 Onboard |
| **ABS** | Activity Breakdown Structure — les catégories d'activité | Liste plate | 16 catégories, toutes cochées Mainline Wayside |
| **OBS** | Organisation Breakdown Structure — les **postes** | Liste **regroupée sous les catégories ABS** ; chaque poste porte ses codes Skills / SoA / Job code | 66 postes ; 45 cochés Mainline Wayside, 2 Onboard, 0 Urban |

**Ce que la structure encode.** La chaîne ABS → OBS est dans le fichier lui-même : les postes sont rangés *sous* leur catégorie ABS. Choisir un ABS restreint les OBS candidats. Le PBS est un axe indépendant, relié aux deux autres par un seul renvoi explicite — la catégorie ABS *Installation* porte la note « Trackside and Trainborne (Use PBS Key) ».

**Ce que le fichier corrige dans le modèle du prototype** (DEC-062) :

- **L'OBS est un poste**, pas une équipe. « IXL Application Design Eng. », pas « Signalling Design — FR ». Un poste n'est pas une personne — l'esprit de DEC-054 tient — mais la maille n'est pas celle qu'on avait supposée. Établi pour le modèle Mainline ; non énoncé pour Urban, qui garde son vocabulaire antérieur.
- **Le PBS est un élément produit**, pas une nature d'exigence. La colonne que le prototype appelait PBS affichait Functional / Performance / Security / Interface / Regulatory. C'est la **nature**, utile, mais autre chose ; elle a désormais son propre champ et sa propre colonne. *Précisé par DEC-074 : ces cinq valeurs ne sont pas non plus la « nature », qui désigne Information / Heading / Requirement ; elles ont quitté Allocation.*
- **Mainline se divise en Wayside et Onboard**, avec des clés différentes. Ce sont deux produits SIG distincts (DEC-061), non un sous-produit.

## Ce qui est ignoré, délibérément

Pour ce prototype (DEC-061) : les deux listes annexes de la feuille ABS (colonnes F et I : « Risk Management, Time Management… » et « ILL, ILS, Basic Design… ») ; les anomalies du fichier — lignes sans identifiant (rattachées au niveau 3 de leur famille, sauf quand elles sont insérées dans la fratrie d'un sous-système), *Cybersecurity Manager* en double, cinq *Subsystem Manager* qui partagent le code PB-PM-05, `x` / `X` mélangés. Elles sont chargées telles quelles : la correction appartient au fichier.

## Ce que le prototype en fait

- Le tender de démonstration `RFP-2026-114` est passé sur le produit **Mainline Wayside** (« Line 4 Resignalling — ETCS L2 ») ; ses douze exigences portent des dérivations prises dans les clés.
- La chaîne ABS → PBS → OBS propose des **sélecteurs** sur les listes cochées pour le produit du tender : les 16 ABS ; les éléments PBS groupés par famille ; les postes, ceux rangés sous l'ABS choisi d'abord, les autres ensuite.
- La relance (ALLOC-014) sur un modèle à clés dérive l'OBS **sous l'ABS dérivé**. Emprunter le modèle Onboard peut produire un élément PBS hors de la liste Wayside : il reste affiché, marqué « from another product's model ».
- Le modèle Urban n'est pas branché sur les clés : DEC-062 n'a rien dit de lui.

## Critères d'acceptation

- KEY-T01 : `build_keys.py` sur le classeur reproduit `keys.js` à l'identique ; aucune valeur des clés n'est saisie ailleurs que dans le classeur.
- KEY-T02 : sur un tender Mainline Wayside, ABS, PBS et OBS se choisissent dans des listes ; aucun champ libre n'accepte une valeur hors clé.
- KEY-T03 : changer l'ABS efface le PBS et l'OBS ; l'ajout d'un rôle propose d'abord ceux rangés sous l'ABS de l'exigence.
- KEY-T04 : la colonne PBS montre un élément produit, jamais une catégorie d'exigence (Functional, Performance…) — ces catégories ont quitté Allocation (DEC-074).
- KEY-T05 : un tender Turnkey ou Urban n'expose aucun sélecteur de clé et n'a pas changé de comportement.
