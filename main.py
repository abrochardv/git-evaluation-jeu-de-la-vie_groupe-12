import random
import argparse
import os
import random
import sys

from lib import write_grid

Grid = list[list[int]]

"Valeurs par défault des paramètres du programme"

nb_cells = 10
max_iter = 20
seed = 42
output_directory = "outputs"
type_sortie = "image"
periodic = False




# --- A ---
def count_neighbors(grid: Grid, row: int, col: int, periodic: bool) -> int:
    """Nombre de voisines vivantes de la cellule (row, col)."""

    n = len(grid)
    count = 0

    for i in range(-1, 2):
        for j in range(-1, 2):

            if i == 0 and j == 0:
                continue

            r = row + i
            c = col + j

            if periodic:
                r = r % n
                c = c % n

                count += grid[r][c]

            elif 0 <= r < n and 0 <= c < n:
                count += grid[r][c]

    return count
    
def next_generation(grid: Grid, periodic: bool) -> Grid:
    """Renvoie la génération suivante, sans modifier la grille reçue."""

    n = len(grid)
    new_grid = []

    for i in range(n):
        row = []

        for j in range(n):
            neighbors = count_neighbors(grid, i, j, periodic)

            if grid[i][j] == 1:
                if neighbors == 2 or neighbors == 3:
                    row.append(1)
                else:
                    row.append(0)

            else:
                if neighbors == 3:
                    row.append(1)
                else:
                    row.append(0)

        new_grid.append(row)

    return new_grid

# --- B ---
def create_grid() -> Grid:
    """Si une grille est fournie en entrée lit et valide la grille sur STDIN.
    Sinon grille générée aléatoirement"""
    entree = sys.stdin.read().splitlines()
    global nb_cells
    if entree:
        while entree and not entree[-1].strip():
            entree.pop()
        try:
            cells = int(entree[0])
        except ValueError :
            raise ValueError(f"{entree[0]} n'est pas un entier")
        if cells <= 0:
            raise ValueError(f"La taille doit être strictement positive")
        if len(entree) != cells+1:
            raise ValueError("Nombre de lignes incorrectes")

        nb_cells = cells
        grid = []

        for i, entree in enumerate(entree[1:], start=2):
            ligne = entree.split()
            if len(ligne) != cells:
                raise ValueError(f"Ligne {i} : {cells} valeurs attendues, {len(ligne)} reçues")
            for c in ligne:
                if c not in ("0", "1"):
                    raise ValueError(f"Ligne {i} : valeur '{c}' invalide (0 ou 1 attendu)")
            grid.append([int(c) for c in ligne])

        return grid

    else:
        rng = random.Random(seed)
        return [[rng.choice([0, 1]) for _ in range(nb_cells)]for _ in range(nb_cells)]


def format_grid_text(grid: Grid, iteration: int) -> str:
    """Renvoie 'iteration: N' suivi des lignes de la grille."""

def write_images(grids: list[Grid], output_directory: str) -> None:
    """Écrit grid_0000.png, grid_0001.png... avec write_grid de lib.py."""

# --- C ---
def positive_int(value: str) -> int:
    """Convertit en entier strictement positif (pour argparse -n)."""
    try:
        number = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"'{value}' n'est pas un entier")
    if number <= 0:
        raise argparse.ArgumentTypeError(f"{number} doit être strictement positif")
    return number

def non_negative_int(value: str) -> int:
    """Convertit en entier positif ou nul (pour argparse -m)."""
    try:
        number = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"'{value}' n'est pas un entier")
    if number < 0:
        raise argparse.ArgumentTypeError(f"{number} doit être positif ou nul")
    return number

def parse_args() -> argparse.Namespace:
    """Lit et vérifie les options -n -m -s -o -t -p."""
    parser = argparse.ArgumentParser(description="Jeu de la vie de Conway")
    parser.add_argument("-n", "--nb_cells", type=positive_int, default=10,
                        help="nombre de cellules par côté (défaut : 10)")
    parser.add_argument("-m", "--max_iterations", type=non_negative_int, default=20,
                        help="numéro de la dernière itération (défaut : 20)")
    parser.add_argument("-s", "--seed", type=int, default=42,
                        help="graine aléatoire (défaut : 42)")
    parser.add_argument("-o", "--output_directory", default="outputs",
                        help="dossier des images (défaut : outputs)")
    parser.add_argument("-t", "--output_type", choices=["image", "text"],
                        default="image", help="type de sortie (défaut : image)")
    parser.add_argument("-p", "--periodic", action="store_true",
                        help="active les conditions aux limites périodiques")
    return parser.parse_args()

def random_grid(nb_cells: int, seed: int) -> Grid:
    """Grille aléatoire reproductible avec random.Random(seed)."""

def fail(message: str) -> None:
    """Écrit le message sur STDERR et quitte avec le code 1."""

def main():
    try:
        grid = create_grid()
    except ValueError as erreur:
        print('Erreur :',erreur,file=sys.stderr)
        sys.exit(1)
    iter = 0
    filename = f"outputs/grid_{iter:04d}.png"
    write_grid(matrix=grid, filename=filename)

if __name__ == "__main__":
    main()
