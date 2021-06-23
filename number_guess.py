import random
def number_guesing():
    truth_number = random.randint(1, 20)
    user_name = input("hello, what is your name")
    print(f"welcome {user_name} Am guesing of a number between 1 and 20")
    guess_taken = 0
    
    
    while guess_taken < 10:
        print("type in your guess")
        guess = int(input())
        
        guess_taken = guess_taken + 1
        if guess == truth_number:
            print(f"congratulations you got is {truth_number}")
            break
        
        if guess < truth_number:
            print(" that is wrong, guess higher")
            
        if guess > truth_number:
            print("that is wrong, guess lower")
    if guess != truth_number:
        print(f"thank you for trying, my guess number was {truth_number}")
        
number_guesing()
        