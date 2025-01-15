# Script de gestion des GIFs : /!\ script en développement /!\

Ce script permet de modifier et d'organiser vos fichiers GIF en les classant par thèmes dans des dossiers spécifiques. Il exporte chaque GIF avec plusieurs palettes de couleurs, simplifiant ainsi considérablement la tâche par rapport à un changement manuel des couleurs sous Adobe Animate. La qualité des GIFs exportés reste inchangée et identique à celle des GIFs d'origine.

---

## Fonctionnalités principales
- **Modification automatisée des couleurs** : Les fichiers GIF sont modifiés avec des palettes de couleurs prédéfinies.
- **Organisation par thèmes et couleurs** : Les fichiers exportés sont triés dans des dossiers structurés.
- **Flexibilité évolutive** : Possibilité d'ajouter facilement de nouvelles palettes de couleurs au script.
- **Gain de temps considérable** : Un export manuel sous Adobe Animate peut prendre plus d'une heure pour chaque thème, tandis que ce script réalise la tâche en environ quatre minutes (peut varier selon le nombre de GIFs traités).

## Comparaison Adobe Animate VS Script Pillow

| Critère               | Adobe Animate               | Pillow (Python)         |
|-----------------------|-----------------------------|-------------------------|
| **Configuration initiale** | Négligeable                  | ~5 à 10 minutes         |
| **Temps par GIF**        | ~45 sec à 1m30              | ~1 à 5 secondes         |
| **Automatisation**       | Non                         | Oui                     |
| **Risque d'erreurs**     | Élevé (manuel)              | Faible (automatique)    |
| **Adaptabilité**         | Limitée aux outils d'Animate | Très flexible (script Python) |
| **Pour 10 GIFs × 5 couleurs** | ~75 minutes (1h15)          | ~5 minutes (peut varier selon le volume) |

**Résumé** : Le traitement avec Pillow est nettement plus rapide et flexible, particulièrement adapté aux grands volumes de fichiers GIF, tandis qu'Adobe Animate convient davantage pour des ajustements précis mais demande beaucoup de temps.

---

## Prérequis

### 1. Installer Python
1. **Télécharger Python** :
   - Rendez-vous sur [python.org/downloads](https://www.python.org/downloads/) et téléchargez la version correspondant à votre système (Windows, macOS, Linux).

2. **Installer Python** :
   - Lors de l'installation :
     - Cochez l'option **"Add Python to PATH"** pour que Python soit accessible depuis n'importe où.
     - Suivez les étapes de l'installateur.

3. **Vérifier l'installation** :
   - Ouvrez une invite de commande (Windows) ou un terminal (macOS/Linux).
   - Tapez :
     ```
     python --version
     ```
     ou :
     ```
     python3 --version
     ```
     Vous devriez voir la version de Python installée (ex. : Python 3.11.2).

### 2. Installer Pillow
- **Documentation officielle :** [Pillow](https://pillow.readthedocs.io/en/stable/)

#### a. Installer pip (si nécessaire) :
   - pip est normalement inclus avec Python.
   - Vérifiez avec :
     ```
     python -m pip --version
     ```
   - Si pip n'est pas installé :
     ```
     python -m ensurepip --upgrade
     ```

#### b. Installer Pillow :
   - Exécutez la commande suivante :
     ```
     pip install pillow
     ```
   - Attendez que l'installation soit terminée.

#### c. Vérifier l'installation de Pillow :
   - Lancez Python dans votre terminal :
     ```
     python
     ```
   - Importez Pillow :
     ```
     from PIL import Image
     ```
   - Si aucune erreur ne s'affiche, Pillow est installé correctement.

---

## Instructions d'utilisation

### Étape 1 : Configurer les chemins des dossiers
1. **Préparer les dossiers** :
   - Placez vos GIFs originaux dans le dossier spécifié par `base_input_folder` (par exemple : `C:\Users\Lucas\Downloads\LUCAS25_copy\icones`).
   - Assurez-vous que le dossier de sortie spécifié dans `base_output_folder` existe ou sera créé automatiquement.

2. **Modifier les variables dans le script** :
   - Dossier source (`base_input_folder`) : Chemin vers le dossier contenant les GIFs d'origine.
   - Dossier d'export (`base_output_folder`) : Chemin vers le dossier d'exportation des GIFs modifiés.

### Étape 2 : Exécuter le script
1. Ouvrez le script dans votre éditeur de code préféré (ex. : Visual Studio Code).
2. Naviguez jusqu'au dossier contenant le script :
   ```
   cd chemin\vers\le\dossier\du\script
   ```
3. Exécutez le script :
   ```
   python script_export_gif_colors.py
   ```
4. Les résultats seront disponibles dans le dossier d'export.

---

## Organisation des fichiers exportés

Les GIFs modifiés seront automatiquement triés par thèmes et couleurs dans des sous-dossiers structurés. Voici un exemple de structure :

```
/icones_modifiés/
├── THEME_A/
│   ├── 0011FF/
│   │   ├── egal-0011FF.gif
│   │   ├── addition-0011FF.gif
│   │   └── multiplication-0011FF.gif
│   ├── 113377/
│   │   ├── egal-113377.gif
│   │   ├── addition-113377.gif
│   │   └── multiplication-113377.gif
│   └── FFAA00/
│       ├── egal-FFAA00.gif
│       ├── addition-FFAA00.gif
│       └── multiplication-FFAA00.gif
├── THEME_B/
│   ├── 330011/
│   │   ├── egal-330011.gif
│   │   ├── addition-330011.gif
│   │   └── multiplication-330011.gif
│   ├── 770055/
│   │   ├── egal-770055.gif
│   │   ├── addition-770055.gif
│   │   └── multiplication-770055.gif
│   └── DDAAEE/
│       ├── egal-DDAAEE.gif
│       ├── addition-DDAAEE.gif
│       └── multiplication-DDAAEE.gif
└── THEME_C/
    ├── FF2233/
    │   ├── egal-FF2233.gif
    │   ├── addition-FF2233.gif
    │   └── multiplication-FF2233.gif
    └── 1199EE/
        ├── egal-1199EE.gif
        ├── addition-1199EE.gif
        └── multiplication-1199EE.gif
```

---

## Notes importantes

- **Format des chemins :**
  - Sous Windows, utilisez le préfixe `r` pour les chemins ou doublez les barres (échappement) :
    ```
    base_input_folder = r"C:\MonDossier\GIFs"
    ```

- **Structure des dossiers :**
  - Assurez-vous que le dossier source contient uniquement des fichiers GIF valides.
  - Le dossier d'export sera créé automatiquement s'il n'existe pas.

- **Permissions :**
  - Vérifiez que les permissions d'écriture sont correctes sur le dossier d'export pour éviter les erreurs.

- **Dépendances :**
  - Ce script nécessite Python et la bibliothèque Pillow. Assurez-vous que tout est correctement installé avant de l'exécuter.

---

## Conclusion
Ce script est un outil puissant pour gérer et modifier des GIFs en masse, offrant une solution rapide et efficace par rapport aux méthodes manuelles. Si vous avez des questions ou des suggestions d'amélioration, n'hésitez pas à me contacter !
