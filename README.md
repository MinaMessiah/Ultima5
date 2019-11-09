# Ultima 5 Hacker

A Python program that hacks the legendary retro game, Ultima 5. This project was initially built for my Cybersecurity class with minimal requirements, but since I enjoyed it, I developed it to be a full-fledged Ultima 5 hacking tool.

### The program allows to view/edit the following:
1. Single character attributes
2. All characters attributes
3. Characters enabled and their names
4. Equipment
5. Items
6. Spells
7. Reagents
8. Armaments

### The program also has the following features:

**1. Input validation with customer ranges:** The program will check if a numeric value that is entered for an attribute is within the valid range.

**2. File validation:** The program will check if the `SAVED.GAM` file exists, and prompt for correct path if not found at the default path `C:\Ultima_5\SAVED.GAM`

**3. Save protection:** The program will not overwrite the actual file until a save command is issued, preventing accidental changes. Also, if the user issues an exit command while modifications have not been saved yet, the program will prevent the user and issue a warning. A second exit command will force exit.

### Notes:
- The program is compatible with **Python 3.6** or higher.
- To run the program, open a terminal and navigate to its directory, then run the following command:
  ```
  python Main.py
  ```
  or
  ```
  python3 Main.py
  ```
- The program modifies the `SAVED.GAM` file, present inside the game directory. A copy of that file is included to experiment with before modifying the actual game file.
