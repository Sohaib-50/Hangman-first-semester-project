from hangman_helper_functions import *


#initialising variables
warnings = 3
guesses = 6
WORD = get_word() #get a random word. This is the word we'll work on.
out_word = ["_" for c in WORD] #make a list of n underscores where n is the number of characters in the word.
available_letters = [chr(i) for i in range(97, 123)] #make a list of all alphabets from a-z inclusive, for user to choose from.
guessed_before_lst = [] #list to keep record of all characters that the user has guessed.
word_complete = False #this boolean variable will be used to control execution of the while loop.


#displaying starting messages and instructions
print_initial_messages(WORD) 
print()
input("Press enter when ready to begin...")
display_countdown(3) #displays countdown from 3 to 1

print("\n" + "-" * 60 + "\n" *2) #seperator line


#starting the iterative process of taking user input and then doing appropriate task(s) related to the input.
while guesses > 0 and not word_complete: #do the following repeatedly while guesses remain and word isn't completely guessed
    print(" " * 15 + f"MY WORD: {' '.join(out_word)}") #printing out_word list as string in a pretty manner (with indentation)
    print()
    print(f"Letters available: {', '.join(available_letters)}") #printing the available_letters list as string\
                                                                #with each alphabet seperated by commas.
    user_guess = input("Enter your guess(choose from the above list of characters): ").lower() #get user's guess and convert it to lowercase.
    print()

    if user_guess in list(WORD) and user_guess not in guessed_before_lst: #if user guesses a character
                                                                          #that's in the word and hasn't been
                                                                          #guessed before, do the following
                                                                          #(We check if user's guess is in list(WORD)
                                                                          #so that we can check the WORD character by character.)
        
        print("Good guess!")
        guessed_before_lst.append(user_guess) #add the guessed letter to the list "guessed_before_lst" .
        available_letters.remove(user_guess) #remove the letter from the list of available letters.
        out_word = adjust_out_word(user_guess, out_word, WORD) #replace underscores in the out_word list by
                                                               #the alphabet guessed wherever appropriate.'''


    elif user_guess in guessed_before_lst: #if user inputs something that they already inputted earlier
        print("Oops, you've already guessed that before! Please choose a letter from the available letters shown.")
        guesses, warnings = give_warning(guesses, warnings) #call the function that gives a warning, decreases
                                                            #warnings or guesses and recieve altered versions of guesses
                                                            #and warnings.'''


    elif user_guess not in list(WORD): #if user inputs something that isn't guessed before but is not in the word either.

        if (not user_guess.isalpha()) or (len(user_guess) != 1) or ("π" in user_guess): #if user enters something that's
                                                                                        #not alphabetical (i.e special char/number)
                                                                                        #or enters a string of more than 1 character.
                                                                                        #Also checking against "π" because python
                                                                                        #considers "π" as alphabet.
            print("Invalid input. You're supposed to enter alphabetical characters only!")
            guesses, warnings = give_warning(guesses, warnings) #call the function that gives a warning and and decreases
                                                                #warnings or guesses.

        else: #else, user must have guessed a single length alphabetical character that isn't in the word.
            guessed_before_lst.append(user_guess)
            available_letters.remove(user_guess)
            print("Wrong guess; that alphabet is not in my word.")
            if is_vowel(user_guess): #if that alphabet is a vowel
                print("You've lost 2 guesses for guessing a wrong vowel.")
                guesses -= 2
            else: #else, it must be a consonant
                print("You've lost a guess.")
                guesses -= 1


    print("\n" * 2 + "-" * 60 + "\n")

    #checking if the word is completely guessed              
    if "_" not in out_word: #all underscores in the list out_word have been replaced by alphabets
        print(" " * 15 + f"MY WORD: {' '.join(out_word)}") #print completed word.
        word_complete = True #change word_complete to True, which will make sure that the while loop
                             #isn't executed again after this iteration.
        
    elif guesses > 0: #guesses remain and word not guessed completely yet (loop will re-execute after this iteration)
         print(f"You now have {guesses} guess(es) and {warnings} warning(s) remaining.\n")   


#outside while
print("\n" * 2)
if word_complete: #if word was fully guessed, i.e loop was broken by word being completed, do the following:
    print("Congrats, you win!!")
    print(f"Your score is: {guesses * count_unique_chars(WORD)}")

else: #word wasnt guessed completely.
    print("You ran out of guesses!")
    print(f"My word was {WORD}.")
