#build a program that contain:
    #1. if else
    #2. for
    #3. while
    #4. input
    #5. function
    
import random

# Create User Interface
print ("          ~~ HANGMAN ~~ ")
print (" ---------------------------------- ")
print ()
usern = input("Please, Enter Your Name : ")
print (" Welcome ", usern)
print ("-------------")
print ("Guess the word in less than 10 attempts")
print ("")

def hangman():
    # Creating Words List: The Lord of The Rings Characters
    word = random.choice(["aragorn" , "galadriel" , "gandalf" , "elrond" , "frodo" , "gollum" , "legolas" , "sauron", "gimli", "saruman"])
    ## Rules And Regulations
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    attempts = 10
    guessmade = ''

    while len(word) > 0 :
        main = ""
        ## Main Logic
        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print ("Guess the word: " + main)
            print ("Congratulations \nYou win!")
            break
        print ("Guess the word:" , main)
        guess = input()

        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            print ("Enter a valid character")
            guess = input()
        
        # Stickman's Slowly Drawn
        if guess not in word:
            attempts = attempts - 1
            if attempts == 9:
                print ("9 turns left")
                print ("  --------  ")
            if attempts == 8:
                print ("8 turns left")
                print ("  --------  ")
                print ("     O      ")
                print ()
            if attempts == 7:
                print ("7 turns left")
                print ("  --------  ")
                print ("     O      ")
                print ("     |      ")
                print ()
            if attempts == 6:
                print ("6 turns left")
                print ("  --------  ")
                print ("     O      ")
                print ("     |      ")
                print ("    /       ")
                print ()
            if attempts == 5:
                print ("5 turns left")
                print ("  --------  ")
                print ("     O      ")
                print ("     |      ")
                print ("    / \     ")
                print ()
            if attempts == 4:
                print ("4 turns left")
                print ("  --------  ")
                print ("   \ O      ")
                print ("     |      ")
                print ("    / \     ")
                print ()
            if attempts == 3:
                print ("3 turns left")
                print ("  --------  ")
                print ("   \ O /    ")
                print ("     |      ")
                print ("    / \     ")
                print ()
            if attempts == 2:
                print ("2 turns left")
                print ("  --------  ")
                print ("   \ O /|   ")
                print ("     |      ")
                print ("    / \     ")
                print ()
            if attempts == 1:
                print ("1 turn left")
                print ("Watch your letter buddy, your people is about to die!")
                print ("  --------  ")
                print ("   \ O_|/   ")
                print ("     |      ")
                print ("    / \     ")
                print ()
            if attempts == 0:
                print ("You lose")
                print ("You let a kind human die")
                print ("  --------  ")
                print ("     O_|    ")
                print ("    /|\      ")
                print ("    / \     ")
                print ()
                print ("THE ANSWER IS: ", word)
                
                break
                
# Function execution
hangman()