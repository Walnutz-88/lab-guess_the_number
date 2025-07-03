import random

def main():
    print("Hello from lab-guess-the-number!")
    
    while True:

        secret_number = random.randint(1, 100)
        attempts = 0
        pb = 0
        
        while True:
            try:
                guess = int(input("Guess the number between 1 and 100: "))
                attempts += 1
                
                if guess == secret_number:
                    print(f"Congratulations! You guessed the number in {attempts} attempts!")
                    if attempts < pb:
                        pb = attempts
                        print(f"New personal best: {pb}")
                    else:
                        print(f"You didn't beat your best of {pb} attempts.")
                    break
                elif guess < secret_number:
                    print("Too low. Try again.")
                elif guess > secret_number:
                    print("Too high. Try again.")
                else:
                    raise ValueError
            except ValueError:
                print("Please enter a valid number.")
                
        while True:
            try:
                play_again = input("Do you want to play again? (y/n): ")
                if play_again.lower() not in ["y", "n"]:
                    raise ValueError
                elif play_again.lower() == "n":
                    return
                elif play_again.lower() == "y":
                    break
            except ValueError:
                print("Please enter a valid option.")


if __name__ == "__main__":
    main()
