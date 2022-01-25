# wordle-bot
Solves wordle puzzles by eliminating the most possible words at every step.

To solve wordles:
1. Run wordlebot.py with the dictionary of choice as an argument.
    - base_dictionary.txt: The dictionary for the standard wordle game.
    - big_dictionary.txt: A very large dictionary containing 479k English words (from https://github.com/dwyl/english-words).
      - This will take more steps to find a word.
    - unlimited_dictionary.txt: The dictionary for the unlimited version of wordle at https://www.wordleunlimited.com/.
      - This is best for testing out the bot as you can play over and over again without waiting.

2. Use the words that it tells you and then type a sequence of a, p, and c to tell the bot the games response (e.g. "pcpac").
    - "a": absent - When the letter is grey.
    - "p": present - When the letter is yellow.
    - "c": correct - When the letter is green.

3. Repeat until solved.

![An image of a solved wordle board](https://i.imgur.com/xKcib9G.png)
![An image of the bot's running process](https://i.imgur.com/kodd0gV.png)

If you want to test out the scoring function, see the number of letter occurences, etc.:
1. Run wordlebot.py with the interactive flag "-i" and the desired dictionary as an argument (see above).
2. Type "ccccc". This will tell the bot that it has found a solution and it will drop you into its python session.
3. Run any python code you like using the available variables and functions.

![An image of some experimentation in the python session](https://i.imgur.com/4yCwJjM.png)
