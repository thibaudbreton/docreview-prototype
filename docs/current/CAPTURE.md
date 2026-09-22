# Capture — conversion du document source

Fait fourni le 22 septembre 2026 : les paramètres du projet portent des **réglages avancés de configuration de la capture**, distincts de la segmentation. Ils gouvernent la **conversion** — ce qui sort du fichier source — et s'appliquent donc *avant* le découpage en blocs.

## Les réglages connus

| Réglage | Valeurs | Ce qu'il décide |
|---|---|---|
| **Conversion range** | Toutes les pages · Pages spécifiques | Quelles pages du document source sont capturées. Ce qui est hors plage **n'existe pas** dans le projet : ce n'est pas un filtre sur la table de revue, c'est une absence d'exigences |
| **Default table conversion format** | Image · Dataframe | Un tableau est capturé comme une image de lui-même, ou comme des données structurées |
| **Sentences in paragraphs** | Comme le fichier source · Découpé | Un paragraphe reste un bloc, ou devient un bloc par phrase |
| **Format of equations** | Images · Formules | Une équation est capturée comme image ou comme formule |

**La liste n'est pas forcément complète.** La capture de référence est coupée sous le quatrième réglage, et un séparateur y laisse deviner une suite. Ne pas traiter ces quatre-là comme l'ensemble.

## Ce que ces réglages impliquent, et qui reste ouvert

**Le format de tableau commande la granularité.** « Default table granularity » (une exigence par ligne / tableau entier) existait déjà dans les paramètres : elle n'a de sens que si le tableau a été converti en **dataframe** — une image n'a pas de lignes à mapper. Les deux réglages sont désormais voisins à l'écran, et la dépendance est écrite. **À confirmer** : la granularité doit-elle être désactivée quand le format est « Image », ou reste-t-elle réglable pour les tableaux convertis à la main ?

**Découper les phrases change les comptes.** Passer un paragraphe en une exigence par phrase augmente mécaniquement le nombre d'exigences, et peut séparer une phrase de celle qui la qualifie. Le défaut retenu est « comme le fichier source ».

**Quand ces réglages peuvent-ils changer ?** Non répondu. Modifier une conversion après la capture ne peut pas se faire sans recapturer — c'est le même genre de rupture que le changement de modèle d'allocation (DEC-050), qui écrase tout et le dit avant. **À trancher** : réglages figés à la création comme le produit (DEC-049), ou modifiables avec un avertissement chiffré du même ordre ?

**Où ils vivent.** Dans la section de configuration désormais nommée **Capture & segmentation** : la conversion et le découpage sont deux moments de la même phase, et les séparer aurait éloigné le format de tableau de sa granularité. Les quatre réglages de conversion sont en tête de section, avant ceux de segmentation.

## Critères d'acceptation

- CAPT-T01 : choisir « Pages spécifiques » ouvre un champ où dire lesquelles ; l'option n'existe pas sans lui.
- CAPT-T02 : l'écran énonce qu'une page hors plage ne produit aucune exigence, et ne la présente jamais comme un filtre d'affichage.
- CAPT-T03 : le format de tableau et la granularité de tableau se lisent ensemble, dans cet ordre.
- CAPT-T04 : aucun de ces réglages n'est présenté comme agissant sur le prototype — la section porte son avertissement « demo only » comme le reste (TE2).
