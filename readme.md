# Game-AIs in python 🦾
- Requirements : pygame

This is my pursiut to research advanced algorithms :)

These projects were developed during taking Harward's [CS50AI](https://pll.harvard.edu/course/cs50s-introduction-artificial-intelligence-python) course.

## Tic-tac-toe ❌⭕

### Launch
    $ cd tictactoe
    $ python3 runner.py

### Description
This is an unbeatable AI player which calculates moves through Minimax Algorythm.
However the game might be tied, since tictactoe is always a tie when played optimally by both sides.

First move made by AI (when it plays as X) may be a little long to calculate, since it must check all the possible outcomes, which count up to more than 255k ;)

### Demo

Here you can watch me be defeated by my own creation. Isn't life a cruel place?

<p align="center">
<img src="https://github.com/RomanchenkoAS/ai_models/assets/119735427/0c0a40d0-9bdb-49fc-86ef-7a6b8c92e469" alt="alt-text">
</p>

## Minesweeper 💣💥

### Launch
    $ cd minesweeper
    $ python3 runner.py

### Desription
This AI uses set of knowledge and logical inferences to find positions of mines and safe cells. If you want to check it out, just hold button "AI MOVE" and it will do the rest.

### Notes
- Naturally, AI has no information about mine positions, it would be pointless otherwise
- AI does sometimes make mistakes, this may occur when there is just not enough information to make a decision. In this case, AI picks move at random, just like a human player would. And it also blows up sometimes, just like a human player would ;) This mostly happens at the beginning of the game, especially on the first move, when there is no information whatsoever.  

### Demo

Short demo 8x8 field | 8 mines
<p align="center">
<img src="https://github.com/RomanchenkoAS/ai_models/assets/119735427/75a8e069-faf1-42b5-ba0a-7f8a14b91b97" alt="alt-text">
</p>

Oddly satisfying demo 20x20 field | 40 mines 🥴
<p align="center">
<img src="https://github.com/RomanchenkoAS/ai_models/assets/119735427/26af7b90-5f4b-4469-8750-fea1171d55ff" alt="alt-text">
</p>


## Crossword 💬

### Launch
    $ cd crossword
    $ python3 generate.py structure words [output]
    
- Structure - path to a structure .txt where █ (full block symbols) stand for walls and _ (underscore symbols) stand for letters
- Words - path to the dictionary .txt 
- Output - (optional) path where script will generate an image with crossword solution

### Description
This is a crossword puzzles generator. Script generate.py uses backtracking search and constraint propagation algorithms, such as node consistency and arc consistency, to find a valid assignment of words to the puzzle grid. It represents the crossword structure, words, variables, and their overlaps. The solve() function enforces consistency and backtracks to find a complete assignment. The print() and save() functions visualize and save the solved puzzle, respectively.

### Example results    
<p align="center">
<img src="https://github.com/RomanchenkoAS/ai_models/assets/119735427/1201e84c-4b9e-4347-9811-03586d709831" alt="alt-text">
</p>


## Nim Game AI 🎲🤖
### Launch
To run the game, first make sure you are in the correct directory.

#### For player vs. AI mode:

```bash
$ cd nim
$ python3 play.py
```

#### For training the AI:

```bash
$ cd nim
$ python3 train.py
```

### Description
This implementation simulates the Nim game with an intelligent AI opponent trained through Q-learning. The game has multiple piles, and players can pick any number of objects from a single pile. The one who picks the last object loses.

The AI learns from playing against itself. It uses a Q-learning dictionary to store (state, action) pairs with their corresponding rewards. Over time, the AI becomes proficient at identifying optimal moves to secure a win or to avoid a loss.

### AI Methodology
#### Q-learning
Q-learning is employed to equip the AI with the capability of learning optimal actions for different states over time. It uses the following formula to update Q-values:
Q(s,a)←old value estimate+α×(new value estimate−old value estimate)

where:
s: State
a: Action
α: Learning rate

The AI explores actions either randomly (with probability epsilon) or by exploiting the best-known action for the state.

#### Training
The training is conducted over n games, where the AI plays against itself. It continually updates its Q-values based on the rewards received and the state-action pairs experienced.

#### Notes
The AI is trained with an epsilon value to allow for some randomness in its actions during training, thus enabling it to explore various strategies.
The AI can be deterministic during actual gameplay, where it picks the move with the highest Q-value.

### Demo
[demo will be here]

Enjoy the game! Feel free to challenge the AI and test your strategic thinking! 🎲🤖