# BrainFuck Script Collection

This repository contains a collection of scripts related to the BrainFuck language. It was created as a personal challenge to better understand BrainFuck and its workings.

## Features
The repository includes the following tools:
- A **BrainFuck interpreter**
- A **converter from a human-readable BrainFuck-like language (referred to as Basic) to BrainFuck**
- A **converter from BrainFuck to Basic**

### Basic Language
Basic is a more readable version of BrainFuck, using English words to represent BrainFuck commands.

## Scripts
### `entry.py` - Entry Point
This script serves as the main entry point for the program.

#### Usage
```sh
entry.py [-h] [--overwrite] mode input [output]
```
##### Positional Arguments:
- `mode` - The mode to run the program in. Options:
  - `interpret` - Run the BrainFuck interpreter.
  - `convert-bf-to-bfb` - Convert BrainFuck to Basic.
  - `convert-bfb-to-bf` - Convert Basic to BrainFuck.
  - `select` - Enter an interactive menu to choose the mode.
- `input` - The input file to read from.
- `output` - (Optional) The output file to write to.

##### Optional Arguments:
- `-h, --help` - Show this help message and exit.
- `--overwrite` - Overwrite the output file if it already exists.

### Additional Scripts
these contain the respective functionalities of the program as classes and can not be run directly.
- `BrainFuck.py` - BrainFuck interpreter.
- `BasicToBrainFuck.py` - Converts Basic to BrainFuck.
- `BrainFuckToBasic.py` - Converts BrainFuck to Basic.

## Basic Language Syntax

### Commands
#### `move`
- **Format:** `move <direction> [number]`
- **Direction:** `left`, `right`, or `to` (required)
  - `to`: Moves to the specified cell number.
  - `left`/`right`: Moves by the specified number of cells (default is `1` if omitted).
- **BrainFuck Equivalent:** `< * number`, `> * number`

#### `increase`
- **Format:** `increase [number]`
- **Number:** Optional integer (defaults to `1` if omitted).
- **BrainFuck Equivalent:** `+ * number`
- **Description:** Increases the value of the current cell by the specified number.

#### `decrease`
- **Format:** `decrease [number]`
- **Number:** Optional integer (defaults to `1` if omitted).
- **BrainFuck Equivalent:** `- * number`
- **Description:** Decreases the value of the current cell by the specified number.

#### `output`
- **Format:** `output`
- **BrainFuck Equivalent:** `.`
- **Description:** Outputs the value of the current cell as a character.

#### `input`
- **Format:** `input`
- **BrainFuck Equivalent:** `,`
- **Description:** Sets the value of the current cell to the ASCII value of the input character.

#### `loop`
- **Format:** `loop`
- **BrainFuck Equivalent:** `[`
- **Description:** Starts a loop that runs until the current cell is `0`.

#### `endloop`
- **Format:** `endloop`
- **BrainFuck Equivalent:** `]`
- **Description:** Ends the current loop.

#### Comments
- **Format:** `///`
- **BrainFuck Equivalent:** `///`
- **Description:** Comments out the rest of the line.


