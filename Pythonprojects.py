import os
import random

print(f"file exists: {os.path.exists("C:\\Users\\maggy\\OneDrive\\Desktop\\MyPythonProjects\\words.txt")}")
def load_words():
    with open("words.txt", "r") as file:
        word = file.read()
    return word.splitlines()
loaded_words = load_words()

def set_up_game():
    random_word = random.choice(loaded_words)
    listed= list(random_word)
    random.shuffle(listed)
    shuffled_word = "".join(listed)
    print(f"Unscramble this word to form a valid word: {shuffled_word}")
    return random_word
    
def player_input():
    score = 0

    while True:
        correct_word = set_up_game()
        attempts = 0
        while attempts < 3:
            guess = input("Your guess: ").strip().lower()
            if not guess:
                print("Please give your attempt!")
                continue
            if guess == correct_word:
                print("Correct! Well done! +5points")
                score += 5
                break
            else:
                attempts += 1
                if attempts < 3:
                    print(f"Wrong! You have {3 - attempts} attempt(s) left")
                else:
                    print(f"Wrong! The correct answer was: {correct_word}")
        print(f"\nCurrent Score: {score}")
        play_again = input("Do you want to continue to next word? (yes or no): ").lower().strip()
        if play_again != "yes":
            break
player_input()
    
            
            
            
        
            
        
        
        
        


    
    
    