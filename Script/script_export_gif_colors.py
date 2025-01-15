import os
from PIL import Image, ImageSequence
import re

# Configurations globales
base_input_folder = r"C:\Users\Usernmae\Downloads\script_pillow\GIFs_initiaux"  # Dossier des GIFs originaux
base_output_folder = r"C:\Users\Username\Downloads\script_pillow\GIFs_modifiés"  # Dossier des GIFs modifiés
themes = {
    "THEME_A": [
        "#123456",  # Couleur principale
        "#654321", "#112233", "#334455", "#556677",  # Monochromatiques
        "#778899", "#99AABB", "#AABBCC"  # Complémentaires
    ],
    "THEME_B": [
        "#FF0000",  # Couleur principale
        "#AA0000", "#BB1111", "#CC2222", "#DD3333",  # Monochromatiques
        "#0033FF", "#3366FF", "#6699FF"  # Complémentaires
    ],
    "THEME_C": [
        "#00FF00",  # Couleur principale
        "#00AA00", "#11BB11", "#22CC22", "#33DD33",  # Monochromatiques
        "#FF6600", "#FF9900", "#FFCC00"  # Complémentaires
    ]
}

# Fonction pour mesurer la luminance d'une couleur
def is_close_to_white(pixel, threshold=200):
    """Vérifie si un pixel est proche du blanc (luminance élevée)."""
    r, g, b, a = pixel
    luminance = 0.299 * r + 0.587 * g + 0.114 * b  # Formule de luminance
    return luminance > threshold and a > 0  # Vérifie aussi que le pixel est visible

# Fonction pour renommer correctement un fichier en fonction de la couleur appliquée
def rename_file(filename, color_hex):
    """Renomme un fichier pour inclure ou remplacer une couleur par son code hexadécimal."""
    # Recherche de noms de couleurs courants dans le fichier
    pattern = re.compile(r"(blanc|rouge|bleu|vert|jaune|orange|rose|noir|gris|violet)", re.IGNORECASE)
    new_name = pattern.sub(color_hex.lstrip("#"), filename)  # Remplace le nom de couleur par le code hex

    # Si aucun nom de couleur trouvé, ajoute le code hex à la fin
    if new_name == filename:
        name, ext = os.path.splitext(filename)
        new_name = f"{name}-{color_hex.lstrip('#')}{ext}"

    return new_name

# Fonction pour appliquer le remplissage tout en conservant les couleurs proches du blanc
def apply_fill_preserve_white(input_path, output_path, fill_color):
    img = Image.open(input_path)
    fill_color_rgba = tuple(int(fill_color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)) + (255,)
    
    frames = []
    duration = img.info.get('duration', 100)  # Durée de chaque frame
    loop = img.info.get('loop', 0)  # Nombre de répétitions (0 = boucle infinie)

    # Parcourir chaque frame
    for frame in ImageSequence.Iterator(img):
        frame = frame.convert("RGBA")  # Convertir la frame en mode RGBA
        
        # Modifier les données des pixels
        new_data = [
            pixel if is_close_to_white(pixel) else fill_color_rgba if pixel[3] > 0 else pixel
            for pixel in frame.getdata()
        ]
        frame.putdata(new_data)
        frames.append(frame)

    # Sauvegarder le GIF avec les frames traitées
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=duration,
        loop=loop,
        disposal=2
    )
    print(f"GIF corrigé et sauvegardé : {output_path}")

# Traitement par thématique et couleur
for theme, colors in themes.items():
    print(f"Traitement de la thématique : {theme}")
    
    theme_output_folder = os.path.join(base_output_folder, theme)
    os.makedirs(theme_output_folder, exist_ok=True)

    for color in colors:
        color_folder = os.path.join(theme_output_folder, color.lstrip("#"))
        os.makedirs(color_folder, exist_ok=True)

        for filename in os.listdir(base_input_folder):
            if filename.endswith(".gif"):
                input_path = os.path.join(base_input_folder, filename)
                
                # Renommer le fichier en fonction de la couleur
                renamed_file = rename_file(filename, color)
                output_path = os.path.join(color_folder, renamed_file)
                
                apply_fill_preserve_white(input_path, output_path, color)

print(f"Terminé ! Les icônes modifiées sont dans {base_output_folder}.")
