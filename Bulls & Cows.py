# Bulls and Cows Game code
import random
import math

# Calculating bulls and cows
def bulls_cows(actual, guess):
    intersection = set(actual).intersection(set(guess))
    cows = len(intersection) # Calculates the number of common digits
    
    bulls = 0
    for a, g in zip(actual, guess):
        if a == g:
            bulls += 1
            cows -= 1 # Substracts 1 from the cows variable each time a bull is found to avoid multiple counting.   
    return bulls, cows # Returns the number of bulls and cows

# Calculates entropy
def entropy(possible_numbers):
    possibilities = len(possible_numbers)  
    prob = 1 / possibilities # Assuming the same probability for every number
    total_entropy = round(prob * math.log(1/prob, 2) * possibilities,3) # Calculating total entropy
    return total_entropy

# Filtering the possibile numbers space afer each guess made by the user
def filter(possible_numbers,guess,bulls, cows):
    new_list = []
    for num in possible_numbers:
        calculated_bulls, calculated_cows = bulls_cows(num, guess)
        if calculated_bulls == bulls and calculated_cows == cows: # Compares cows and bulls of the guess with each number in possible_numbers
            new_list.append(num)
    return new_list

def game():
    ans = 'Y'
    while ans.upper() == 'Y':
        attempts = 0
        n = 1
        possible_numbers=[]
        for x in range(1000,10000):
            if len(set(str(x))) == 4:
                possible_numbers.append(str(x)) # Creates the list of all possible numbers
        secret = random.choice(possible_numbers)
        
        while True:
            guess = input("Enter a four digit number: ") # Prompts the user to enter the guess
            if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4: # Checks multiple conditions for the entered number
                print("Invalid input. Please enter a 4-digit number.")
                continue
            
            attempts += 1
            
            # Calculates and prints the number of bulls and cows
            bulls, cows = bulls_cows(secret, guess)
            print("The number of bulls is: " + str(bulls) + " and the number of cows is: " + str(cows)) 
            
            # Filter the possible numbers based on the guesses
            possible_numbers = filter(possible_numbers,guess,bulls, cows)
            new_possible_numbers = len(possible_numbers)
            print(f"Possible numbers after filtering:", new_possible_numbers)
            
            # Calculate the entropy based on remaining possibile numbers
            H = entropy(possible_numbers)
            print("Current entropy: "+ str(H) + " bits")
            
            if bulls == 4: # The user have found the secret number
                print("Congratulations!! You found the secret number in " + str(attempts) + " attempts")
                break

            if attempts > 4 and attempts < 11: # Provides a hint to the user if the number of attempts is more than 4 
                hint = input("Do you want a guess(y/n):") # Asking if the user needs hints
                if hint == 'y':
                    if n == 4:
                        print('The secret number is', secret)
                        break
                    else:
                        hint = secret[:n] # Gives the first n digits of the secret
                        print("The secret starts with: ", hint)
                        n += 1

            #Condition to end the game
            if attempts == 11: # The user loses when the number of attempts is 11
                print("Sorry you have run of attempts to guess the secret")
                break
        ans = input("Another game? Enter Y or y for yes.") # Prompts the user for a rematch
    print("Thank you for playing!")
    
if __name__ == "__main__":
    print("Welcome to the Bulls and Cows game!\nFind the 4-digit number I have guessed in 10 attempts.")
    game()
