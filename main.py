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
def read_grid_from_stdin() -> Grid:
    """Lit et valide la grille sur STDIN. Quitte avec une erreur si invalide."""

def format_grid_text(grid: Grid, iteration: int) -> str:
    """Renvoie 'iteration: N' suivi des lignes de la grille."""

def write_images(grids: list[Grid], output_directory: str) -> None:
    """Écrit grid_0000.png, grid_0001.png... avec write_grid de lib.py."""

# --- C ---
def parse_args() -> argparse.Namespace:
    """Lit et vérifie les options -n -m -s -o -t -p."""

def random_grid(nb_cells: int, seed: int) -> Grid:
    """Grille aléatoire reproductible avec random.Random(seed)."""

def fail(message: str) -> None:
    """Écrit le message sur STDERR et quitte avec le code 1."""

def main():
    nb_cells = 50

    rng = random.Random(4200)

    matrix = [
        [rng.choice([0, 1]) for _ in range(nb_cells)]
        for _ in range(nb_cells)
    ]

    iter = 0
    filename = f"outputs/grid_{iter:04d}.png"
    write_grid(matrix=matrix, filename=filename)

if __name__ == "__main__":
    main()
