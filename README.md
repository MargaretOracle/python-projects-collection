# Word Scramble Game

A simple and interactive Python word scramble game. The player is shown a scrambled word and must guess the correct original word within 3 attempts. Each correct answer earns points, and the game continues until the player chooses to stop.

---

## Project Files

- `Pythonprojects.py` → main Python script  
- `words.txt` → word list used by the game
- `highscore.txt` → Saves the highest score across sessions   
- `.gitignore` → ignores unnecessary files like virtual environments and compiled Python files  

---

## How to Play

1. Run `Pythonprojects.py`
2. Choose your difficulty level:
   - **Easy** → 3–4 letter words  
   - **Medium** → 5–7 letter words  
   - **Hard** → 8+ letter words  
3. A scrambled word will appear.  
4. You have **3 attempts**, each with a **30-second timer**.  
5. A **hint** is shown (first letter of the word).  
6. Guess correctly to earn **+5 points**.  
7. After each round, choose to continue or quit.  
8. At the end, your **final score** and the **high score** are displayed.

---

## How to Run the Game

1. Navigate to the project folder:

   ```bash
   cd word-scramble-game
   ```


2. Run the python script
    ```bash
   python Pythonprojects.py
   ```
    
--- 

## Features
-  Difficulty levels (Easy, Medium, Hard)
-  Timer for each attempt (30 seconds)
-  Hint system (first letter revealed)
-  High score tracking across game sessions
-  Score system: +5 points per correct answer
-  Unlimited rounds until user chooses to stop
-  Clean, modular code structure

---

## Requirements

- Python 3.6 or higher
- Terminal/command prompt
- Ensure words.txt is in the same folder as the script

---

## Ideas for Future Improvements

- More advanced hint system
- Progressive difficulty
- GUI version using Tkinter or PyQt

---

## Changelog

 **v1.0 — Initial Version (2025-11-10)**  
  - Basic word scramble game implemented  
  - Added score system (+5 points for correct answers)  
  - Added 3-attempt rule  
  - Added word loading from `words.txt`  
  - Added continuous play option  
  - Added difficulty levels

**v2.0 — Improved Version (2025-11-11)**  
  - Added 30-second timer per attempt
  - Added hint system
  - Added high score tracking with highscore.txt
  - Improved code structure and readability
  - Transitioned to dynamic file paths for GitHub compatibility



   
   



