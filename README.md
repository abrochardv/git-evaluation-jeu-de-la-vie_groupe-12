# Jeu de la vie groupe 12
Ce projet est une simulation du [jeu de la vie de Conway](https://fr.wikipedia.org/wiki/Jeu_de_la_vie) écrite en Python. Le programme permet de générer une grille aléatoire ou de lire une grille sur l'entrée standard, puis de calculer son évolution avec des conditions aux limites fixes ou périodiques.

- [Jeu de la vie groupe 12](#jeu-de-la-vie-groupe-12)
  - [Installation](#installation)
    - [Prérequis](#prérequis)
    - [Clonage du dépôt](#clonage-du-dépôt)
  - [Exécution](#exécution)
  - [Arguments](#arguments)
  - [Vidéos](#vidéos)
  - [Auteurs](#auteurs)
  - [Liens utiles](#liens-utiles)


## Installation
### Prérequis
Ce projet nécessite: 
- Une version de [Python](https://www.python.org/downloads/) et ses librairies par défaut afin d'exécuter le programme
- `sh` et des des commandes Unix par défaut (Utiliser [WSL](https://learn.microsoft.com/fr-fr/windows/wsl/install) si sous Windows)
- `ffmpeg` et `gource` pour la génération de vidéos
  Sur Ubuntu ou Debian
  ```bash
  sudo apt update
  sudo apt install python3 git gource ffmpeg
  ```
  Sur MacOs
  ```bash
  brew install gource ffmpeg
  ```
### Clonage du dépôt
CLoner le dépôt à l'aide de 
```bash
git clone https://github.com/abrochardv/git-evaluation-jeu-de-la-vie_groupe-12.git
```
Ou
```bash
git clone git@github.com:abrochardv/git-evaluation-jeu-de-la-vie_groupe-12.git
```
## Exécution
Le programme s'execute principalement à l'aide du script `main.py`
Sans option, le programme utilise les [valeurs par défaut](##Arguments) et crée **21 images dans `outputs`**, de `grid_0000.png` à `grid_0020.png` :

```bash
$ python3 main.py
Generation of 21 images in directory outputs
$ echo $?
0
$ ls -p1 outputs | wc -l
     21
```

À partir de la grille présentée dans un format similaire à `tests/matrix3/input.txt, `-m 1` demande une seule évolution, avec les conditions aux limites fixes utilisées par défaut :

```bash
$ cat tests/matrix3/input.txt | python3 main.py -m 1 -t text
iteration: 1
0 1 0
0 0 1
0 1 0
$ echo $?
0
```

L'ajout de `-p` active les conditions aux limites périodiques et donne un résultat différent pour la même grille :

```bash
$ cat tests/matrix3/input.txt | python3 main.py -m 1 -p -t text
iteration: 1
0 0 0
0 0 0
0 0 0
```
## Arguments
| Option courte | Option longue | Description | Valeur par défaut |
|---|---|---|---|
| `-n N` | `--nb_cells N` | nombre de cellules par côté pour une grille aléatoire | `10` |
| `-m N` | `--max_iterations N` | numéro de la dernière itération à calculer | `20` |
| `-s N` | `--seed N` | graine du générateur de nombres aléatoires | `42` |
| `-o DOSSIER` | `--output_directory DOSSIER` | dossier dans lequel écrire les images | `outputs` |
| `-t TYPE` | `--output_type TYPE` | type de sortie : `image` ou `text` | `image` |
| `-p` | `--periodic` | active les conditions aux limites périodiques | désactivée |
| `-h` | `--help` | affiche l'aide du programme | — |

## Vidéos

[Lien vers la video Jeu de la vie grille 50×50 graine 4200, groupe 12 (scénario 5)](https://youtu.be/PlvEZ6jWCYM?si=mSSTn8cSqx__0X4P)

[Lien vers Jeu de la vie historique du dépôt (Gource), groupe 12](https://youtu.be/3N7GbPkDdW8?si=4W269rF5URIvQFhc)

## Auteurs
| Nom | N° étudiant |
|---|---|
| BROCHARD Antoine | 42008983 |
| ABDALLAH Johan | 46008158 |
| ZEGHOUDI Mohamed |46007455 |

## Liens utiles

 - [Règles du jeu de la vie de Conway](https://fr.wikipedia.org/wiki/Jeu_de_la_vie)
 - [Syntaxe de rédaction Markdown](https://docs.github.com/fr/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
 - [Documentation argparse](https://docs.python.org/fr/3/library/argparse.html)
 - [Documentation ffmpeg](https://ffmpeg.org/ffmpeg.html)
 - [Documentation gource](https://github.com/acaudwell/Gource/wiki)
