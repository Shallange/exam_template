# Examination

Individuell examinationsuppgift i kursen Programmering med Python.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Game Overview](#game-overview)
3. [Controls](#controls)
4. [Special Commands](#special-commands)
5. [Game Rules](#game-rules)
6. [Scoring](#scoring)
7. [High Scores](#high-scores)
8. [Emoji Guide](#emoji-guide)

## Getting Started

To start the game, ensure you have Python installed on your system. Clone the repository, navigate to the game directory, and run the following command:

```commandline
python -m src.games
```

 <img src="/images/game_grid.png"/>
 
 # Emoji Guide

Below is a guide to the emojis used in the game:
<table>
<tr><th>Food </th><th>Other Items</th></tr>
<tr><td>

| Emoji | Description |
|-------|-------------|
| 🍓 | Strawberry |
| 🍉 | Watermelon |
| 🥒 | Cucumber |
| 🍖 | Meat |
| 🍎 | Apple |
| 🥕 | Carrot |

</td><td>

| Emoji | Description |
|-------|-------------|
| 🔑 | Key |
| 💣 | Bomb |
| 🧰 | Chest |
| 🪤 | Trap |
| 🥄 | Shovel | 
| 🔥 | Fire |

</td></tr> </table>

Game Overview
-------------

In the game, you control a character on a grid filled with various objects including food, keys, bombs, and traps. Your goal is to collect items, avoid or disarm traps, and exit the grid with the highest score possible.

### Controls

-   `W`: Move up
-   `A`: Move left
-   `S`: Move down
-   `D`: Move right
-   `Q` or `X`: Quit the game

### Special Commands

-   `I`: Show inventory
-   `B`: Place a bomb at your current location
-   `T`: Attempt to disarm a nearby trap

### Game Rules

-   Navigate the grid to collect items that increase your score.
-   Avoid or disarm traps that can decrease your score.
-   Use keys to unlock chests for bonus points.
-   Placing a bomb will countdown and explode, clearing nearby cells.
-   Exiting the game saves your score along with the number of moves taken to achieve it.

### Scoring

-   Each food item collected increases your score by its value.
-   Unlocking a chest gives a large point boost.
-   Disarming traps prevents point loss.
-   Every move deducts 1 point unless protected by a grace period after picking up an item.

High Scores
-----------

At the end of each game session, your score and number of moves are logged to `game_results.txt` with the format:

`HH:MM:SS - player_name - Number of moves: XX - Total highscore: YY`

