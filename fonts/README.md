# Polices de marque

- **Alstom** — la police de la marque, pour tout le texte de l'interface (DEC-115). Sous licence (© Alstom, tous droits réservés) : ni les fichiers ni rien qui en dérive ne sont versionnés.
  - Fabriquer les copies web à partir des TTF fournis par la marque :

    ```bash
    python3 build_fonts.py "/chemin/vers/Alstom Font"
    ```

    Elles arrivent ici : `Alstom-Regular.woff`, `Alstom-Medium.woff`, `Alstom-Bold.woff` (WOFF, deux fois plus légers, sans les bitmaps des TTF de bureau).
  - `build_merge.py` les embarque dans `local/index.html` (non versionné), qui s'ouvre aussi par double-clic, et dans les captures du deck.
  - `index.html` et `docreview-app.html` (dépôt public, GitHub Pages) ne les embarquent pas tant que `PUBLISH_BRAND_FONT = False` : la page publiée donnerait le fichier de la police à qui l'ouvre. Ils s'affichent en Noto Sans, sur les mêmes métriques, donc avec la même mise en page.
  - Jamais `local()` : les TTF installés contiennent des bitmaps 1 bit que Chrome sous Windows dessine à la place des contours entre 9 et 18 px.
- **Noto Sans** — chargée depuis Google Fonts par chaque écran ; la police de repli, sur laquelle la police Alstom est calée (hauteur d'x, ascendante, descendante).
- **Antarctica** — police de titre demandée en DEC-063, sous licence, absente des CDN publics. Déposer ici `Antarctica-Regular.woff2` et `Antarctica-Bold.woff2`. Tant qu'ils manquent, les titres sont en Alstom (en Noto Sans là où Alstom n'est pas embarquée).
- **Georgia** — reste la police du document source (vue Document) : le papier se distingue de l'interface.
