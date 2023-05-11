# Game-AIs in python 🦾
- Requirements : pygame

## Tic-tac-toe

#### Launch
    $ cd tictactoe
    $ python3 runner.py

#### Description
This is an unbeatable AI player which calculates moves through Minimax Algorythm.
Though the game might be tied, since tictactoe is always a tie when played optimally by both sides.

First move made by AI (when it plays as X) may be a little long to calculate, have patience ;)

## Minesweeper

#### Launch
    $ cd minesweeper
    $ python3 runner.py

#### Desription
This AI uses set of knowledge and logical inferences to find positions of mines and safe cells. If you want to check it out, just hold button "AI MOVE" and it will do the rest.

#### Notes
- Naturally, AI has no information about mine positions, it would be pointless otherwise
- AI does sometimes make mistakes, this may occur when there is just not enough information to make a decision. In this case, AI picks move at random, just like a human player would. And it also blows up sometimes, just like a human player would ;) This mostly happens at the beginning of the game, especially on the first move, when there is no information whatsoever.  

#### Demo

Short demo 8x8 field | 8 mines
<p align="center">
<img src="https://github.com/RomanchenkoAS/ai_models/assets/119735427/75a8e069-faf1-42b5-ba0a-7f8a14b91b97" alt="alt-text">
</p>

Oddly satisfying demo 20x20 field | 40 mines 🥴
<p align="center">
<img src="https://github.com/RomanchenkoAS/ai_models/assets/119735427/26af7b90-5f4b-4469-8750-fea1171d55ff" alt="alt-text">
</p>
