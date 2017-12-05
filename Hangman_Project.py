
import time

name = raw_input("What's Your Name?")
print "Hello, " + name, "Lets Play Hangman!"

print ""

time.sleep(1)
print "Start Guessing..."
time.sleep(0.5)

word = "secret"
guesses = ''
turns = 10

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print char,
        else:
            print "_",
            failed += 1
        if failed == 0:
            print "You Win!"
            break
        print
        guess = raw_input("Guess a Letter!")
        guesses += guess
        if guess not in word:
            turns -= 1
            print "Wrong Guess"

            print "You have ", + turns, "more guesses"

            if turns == 0:
                print "You Lose! :D"
                

