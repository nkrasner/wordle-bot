from copy import deepcopy
import sys

def no_repeats(word):
    return len(set(word)) == len(word)
if len(sys.argv) < 2:
    print("Usage: wordlebot.py <dictionary file>")
# Get all 5 letter wordswhich only contain letters
with open(sys.argv[1], "rt") as file:
    lines = file.readlines()
words = [line.strip().lower() for line in lines]
words = [word for word in words if len(word) == 5 and word.isalpha()]

letter_counts = ({},{},{},{},{})
for word in words:
    for position, letter in enumerate(word):
        if letter not in letter_counts[position]:
            letter_counts[position][letter] = 0
        letter_counts[position][letter] += 1

def score(word):
    return sum([letter_counts[position][letter] for position, letter in enumerate(word)])

word_ranks = {word:score(word) for word in sorted(words, key=lambda word: score(word), reverse=True)}

best_word = max([word for word in words if no_repeats(word)], key=lambda word: score(word))

optimal = [max(letter_counts[position], key=lambda letter:letter_counts[position][letter]) for position in range(5)]


def correct_input(text):
    if len(text) != 5:
        return False
    for letter in text:
        if letter not in ['c','p','a']:
            return False
    return True

current_word = best_word
options = deepcopy(word_ranks)

print(f"Start with the word {current_word}.")
status = input("How were those letters? ([c]orrect, [p]resent, [a]bsent)\n")
while not correct_input(status):
    status = input("Please respond inline. (e.g. 'cpaac')\n")

attempt = 1

correct_letters = {}
while status != 'ccccc' or attempt >= 6:
    for position, condition in enumerate(status):
        if condition == 'c':
            options = {word:options[word] for word in options if current_word[position] == word[position]}
            if current_word[position] not in correct_letters:
                correct_letters[current_word[position]] = []
            correct_letters[current_word[position]].append(position)
        elif condition == 'p':
            options = {word:options[word] for word in options if current_word[position] in word and current_word[position] != word[position]}
        elif condition == 'a':
            if current_word[position] in correct_letters:
                incorrect_positions = [index for index in list(range(5)) if index not in correct_letters[current_word[position]]]
                for index in incorrect_positions:
                    options = {word:options[word] for word in options if current_word[position] != word[index]}
            else:
                options = {word:options[word] for word in options if current_word[position] not in word}

    if len(options) == 0:
        print("That word does not exist.")
        break
    current_word = max(options, key=lambda word: score(word))

    print(f"Play the word {current_word}.")
    status = input("How were those letters? ([c]orrect, [p]resent, [a]bsent)\n")
    while not correct_input(status):
        status = input("Please respond inline. (e.g. 'cpaac')\n")

print("Game over, goodbye!")