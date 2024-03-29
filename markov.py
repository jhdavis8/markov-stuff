'''
markov.py: takes in an order (int), length of sample (int), and 
           source file (string) and prints a sample of random
           markov-generated text based on the source

Josh Davis July 2019
Credit to this article for the approach:
https://realpython.com/lyricize-a-flask-app-to-create-lyrics-using-markov-chains/
'''

from random import choice
import sys

def generateModel(text, order):
    model = {}
    for i in range(0, len(text) - order):
        fragment = text[i:i+order]
        next_letter = text[i+order]
        if fragment not in model:
            model[fragment] = {}
        if next_letter not in model[fragment]:
            model[fragment][next_letter] = 1
        else:
            model[fragment][next_letter] += 1
    return model


def getNextCharacter(model, fragment):
    letters = []
    for letter in model[fragment].keys():
        for times in range(0, model[fragment][letter]):
            letters.append(letter)
    return choice(letters)


def generateText(text, order, length):
    model = generateModel(text, order)

    currentFragment = text[0:order]
    output = ''
    for i in range(0, length-order):
        newCharacter = getNextCharacter(model, currentFragment)
        output += newCharacter
        currentFragment = currentFragment[1:] + newCharacter
    print(output)

def runMarkov(order, length, filename):
    f = open(filename, "r")
    if f.mode == 'r':
        text = f.read()
    generateText(text, order, length)

if __name__ == "__main__":
    runMarkov(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3])
