import os
import random
import threading
base_dir = os.path.dirname(__file__)
words_path = os.path.join(base_dir, "words.txt")
highscore_path = os.path.join(base_dir, "highscore.txt")

def load_words():
    with open(words_path, "r") as file:
        words = [w.strip().lower() for w in file.readlines() if w.strip()]
        
    easy = [w for w in words if 3<= len(w) <= 4]
    medium = [w for w in words if 5<= len(w) <= 7]
    hard = [w for w in words if len(w) >= 8]
    
    return {"easy": easy, "medium": medium, "hard": hard}

def load_highscore():
    if not os.path.exists("highscore.txt"):
        return 0
    with open("highscore.txt", "r") as file:
        return int(file.read())
    
def save_highscore(score):
    with open("highscore.txt", "w") as file:
        file.write(str(score))

def timed_out(prompt, timeout):
    user_input = [None] #use list because it is mutable
    def get_input():
        user_input[0] = input(prompt)
    t = threading.Thread(target = get_input)
    t.start()
    t.join(timeout)
    
    if t.is_alive():
        print("Time is up!")
        return None
    return user_input[0]
   
def generate_scramble(word):
    listed = list(word)
    random.shuffle(listed)
    return "".join(listed)
def play_around(word):
    hint = word[0]
    scrambled = generate_scramble(word)
    
    print(f"Unscramble this word: {scrambled}")
    print(f"Hint: starts with '{hint}'")
    
    attempts = 0
    while  attempts < 3:
        print(f"\nAttempt {attempts + 1}/3 – You have 30 seconds")
        
        guess = timed_out("Your guess: ", 30)
        if guess is None:
            print("No answer entered in time! press enter to continue with your remaining attempts!")
            attempts += 1
            continue
        
        guess = guess.strip().lower()
        
        if guess == word:
            print("Correct! +5points")
            return 5
        else: 
            attempts += 1
            if attempts < 3:
                print("Incorrect! Try again")
            else:
                print(f"Wrong! the correct answer was {word}")
    return 0

def choose_difficulty():
    print("\nChoose difficulty:")
    print("1. Easy (3–4 letter words)")
    print("2. Medium (5–7 letters)")
    print("3. Hard (8+ letters)")
    
    while True:
        choice = input("Enter the choice 1/2/3: ")
        if choice == "1":
            return "easy"
        if choice == "2":
            return "medium"
        if choice == "3":
            return "hard"
        print("Incorrect choice! Try again")
def play_game():
    score = 0
    highscore = load_highscore()
    
    difficulty = choose_difficulty()
    words = load_words()
    pool = words[difficulty]
    
    if not pool:
        print("No words available for this level")
    
    print(f"Starting {difficulty} mode!\n")
    
    while True:
        word = random.choice(pool)
        score += play_around(word)
        
        print(f"Current score {score}")
        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            break
    
    print(f"Game Over! Final Score: {score}")
    print(f"High Score: {highscore}")
    
    if score > highscore:
        print("NEW HIGH SCORE!")
        save_highscore(score)
    else:
        print("You didn’t beat the high score this time.")

    print("Thanks for playing!")

play_game()


        
        
    
    
        
        
        

            



    
    
    
        
        
    



    
            
            
            
        
            
        
        
        
        


    
    
    