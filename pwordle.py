#!/usr/bin/python3

import english_words as ew
import random
import sys
import math

class PyWordle():
    def __init__(self):
        # remaining choices
        self.remaining_choices = list()
        # storage for english word set
        self.word_english_word_set = list()
        # storage for letter frequency details
        self.letter_freq = dict()
        # list of incorrect guesses made
        self.incorrect_choices = list()
        # frequency of letters guessed in their correct sequence
        self.correct_guess_letter_freq = dict()

        # length of words to filter for game (Update to increase or decrease challenge)
        self.word_guess_length = 5
        # total number of plays (Update to increase the challenge)
        self.totalPlays = self.word_guess_length + 1

        # populate the word setlist with words that match the size of the guess length
        for e in ew.english_words_set:
            if len(e) == self.word_guess_length:
                self.word_english_word_set.append(e.upper())

        # choose a random word
        self.worldle_word = random.choice(self.word_english_word_set)

        # capture the frequency of characters in the word
        for f in range(65, 91):
            self.remaining_choices.append(chr(f))

        for f in self.worldle_word:
            self.letter_freq[f] = 0

        for f in self.worldle_word:
            self.letter_freq[f] = self.letter_freq[f] + 1

        for f in self.worldle_word:
            self.correct_guess_letter_freq[f] = 0

        self.printGameLegend()


    def playGame(self):
        """Manages game play"""

        numPlays = 0

        while True:
            if numPlays <= self.totalPlays and self.playTurn():
                print("\nCongratulations You Win!")
                return True
            elif numPlays == self.totalPlays:
                print("\nSorry! You Lost! The word is: {}".format(self.worldle_word))
                return False

            numPlays = numPlays + 1
            print("\nIncorrect choices:{}".format(self.incorrect_choices))
            print("\nRemaining choices:{}".format(self.remaining_choices))
            print("")
            print("\nNum guesses remaining: {}".format(self.totalPlays - numPlays))
            

    def playTurn(self):
        val = input("\nEnter your guess: ", )
        return self.printWord(val.upper())


    def printGameLegend(self):
        """Game legend"""

        width = 48
        title = "Legend"
        padding = math.ceil(width/2 - len(title))

        print("-"*width)
        print(" " * padding + title + " " * padding)
        print("-"*width)
        print("* = Correct letter guessed in correct position")
        print("? = Correct letter but not in correct position")
        print("x = Incorrect letter")
        print("-"*width)


    def printWord(self, guess):
        """Print word sequences"""

        print("")
        sys.stdout.write("|")
        index = 0
        numCorrect = 0
        
        for i in guess:
            if i in self.worldle_word and self.worldle_word[index] == i:
                sys.stdout.write("*|")
                self.correct_guess_letter_freq[i] = self.correct_guess_letter_freq[i] + 1
                numCorrect = numCorrect + 1
            elif i in self.worldle_word and self.letter_freq[i] != self.correct_guess_letter_freq[i]:
                sys.stdout.write("?|")
            else:
                if i not in self.incorrect_choices:
                    # append item to incorrect choices list
                    self.incorrect_choices.append(i)
                    # remove item from remaining choices list
                    self.remaining_choices.remove(i)
                sys.stdout.write("x|")

            index = index + 1

            # prevent processing of characters > the actual guess word length
            if index >= len(self.worldle_word):
                break

        index = 0

        print("")
        sys.stdout.write("|")
        for i in guess:
            sys.stdout.write(i + "|")
            index = index + 1

            # prevent processing of characters > the actual guess word length
            if index >= len(self.worldle_word):
                break

        print("")

        if numCorrect == self.word_guess_length:
            return True

        return False

if __name__ == '__main__':
    try:
        wordle = PyWordle()
        wordle.playGame()
    except KeyboardInterrupt:
        print("\n\nLeaving so soon???\n")
        print("Goodbye!")