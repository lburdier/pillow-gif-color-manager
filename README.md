**English** · [Français](README.fr.md)

# GIF colour manager (Pillow)

> Work in progress.

This script recolours and organises your GIF files, sorting them by theme into dedicated folders. It exports each GIF with several colour palettes, which is far faster than changing colours by hand in Adobe Animate. Exported GIFs keep exactly the same quality as the originals.

---

## Features

- **Automatic recolouring**: GIFs are recoloured with predefined palettes.
- **Sorted by theme and colour**: exported files go into a structured folder tree.
- **Easy to extend**: add new colour palettes to the script in a few lines.
- **Big time saver**: a manual export in Adobe Animate can take over an hour per theme; the script does it in about four minutes (depending on the number of GIFs).

## Adobe Animate vs Pillow script

| Criterion                  | Adobe Animate                  | Pillow (Python)            |
|----------------------------|--------------------------------|----------------------------|
| **Initial setup**          | Negligible                     | ~5 to 10 minutes           |
| **Time per GIF**           | ~45 s to 1 min 30              | ~1 to 5 seconds            |
| **Automation**             | No                             | Yes                        |
| **Risk of mistakes**       | High (manual)                  | Low (automatic)            |
| **Flexibility**            | Limited to Animate's tools     | Very flexible (Python)     |
| **10 GIFs × 5 colours**    | ~75 minutes                    | ~5 minutes (varies with volume) |

**In short**: Pillow is much faster and more flexible, especially for large batches of GIFs. Adobe Animate is better for fine-tuning a single file, but takes a lot of time.

---

## Requirements

### 1. Install Python

1. **Download Python** from [python.org/downloads](https://www.python.org/downloads/) for your system (Windows, macOS, Linux).
2. **Install it**: tick **"Add Python to PATH"** so Python can be run from anywhere, then follow the installer.
3. **Check the installation** in a terminal:
   ```
   python --version
   ```
   or:
   ```
   python3 --version
   ```
   You should see the installed version (e.g. Python 3.11.2).

### 2. Install Pillow

Official documentation: [Pillow](https://pillow.readthedocs.io/en/stable/)

a. **Check pip** (normally bundled with Python):
   ```
   python -m pip --version
   ```
   If it is missing:
   ```
   python -m ensurepip --upgrade
   ```

b. **Install Pillow**:
   ```
   pip install pillow
   ```

c. **Check Pillow**: start `python`, then run:
   ```
   from PIL import Image
   ```
   No error means Pillow is installed correctly.

---

## Usage

### Step 1: set the folder paths

1. **Prepare the folders**:
   - Put your original GIFs in the folder set by `base_input_folder` (e.g. `C:\Users\username\GIFs_initiaux`).
   - The output folder set by `base_output_folder` is created automatically if needed.

2. **Edit the variables in the script**:
   - `base_input_folder`: folder containing the original GIFs.
   - `base_output_folder`: folder where the recoloured GIFs are exported.

### Step 2: run the script

1. Go to the script's folder:
   ```
   cd path\to\the\script
   ```
2. Run it:
   ```
   python script_export_gif_colors.py
   ```
3. The results are in the output folder.

---

## Output structure

Recoloured GIFs are sorted by theme and colour into sub-folders, for example:

```
/icones_modifiés/
├── THEME_A/
│   ├── 0011FF/
│   │   ├── egal-0011FF.gif
│   │   ├── addition-0011FF.gif
│   │   └── multiplication-0011FF.gif
│   ├── 113377/
│   │   └── ...
│   └── FFAA00/
│       └── ...
├── THEME_B/
│   ├── 330011/
│   ├── 770055/
│   └── DDAAEE/
└── THEME_C/
    ├── FF2233/
    └── 1199EE/
```

---

## Notes

- **Paths on Windows**: use the `r` prefix or double the backslashes:
  ```
  base_input_folder = r"C:\MyFolder\GIFs"
  ```
- **Input folder**: it should only contain valid GIF files.
- **Permissions**: make sure you can write to the output folder.
- **Dependencies**: Python and Pillow must be installed.

---

## Feedback

Questions or ideas for improvement? Open an issue.
