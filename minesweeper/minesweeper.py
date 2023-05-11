import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        if len(self.cells) == self.count:
            return self.cells

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        if self.count == 0:
            return self.cells

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """

        # If cell is in that sentence
        if cell in self.cells:

            # Remove that cell from a sentence
            self.cells.remove(cell)

            # Decrease mines count
            self.count -= 1

        # If not - do nothing
        else:
            pass

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """

        # Remove that cell from a sentence if it is there
        self.cells.discard(cell)


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=3, width=3):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()
        
        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """

        # Note that this move was made
        self.moves_made.add(cell)

        # Note that this cell is safe
        self.mark_safe(cell)

        # Create a new sentence based on cell count
        # Take all the cells around | except those which are mines or safe | say that {count} of them are mines

        i, j = cell  # Current cell's position
        cells_around = set()

        iterable = [-1, 0, 1]
        for x in iterable:
            for y in iterable:
                # If it is not the same cell
                if x != 0 or y != 0:
                    # If it is inside the boundaries: more than 0 and less then dimension
                    if (i + x) >= 0 and (j + y) >= 0 and (i + x) < self.height and (j + y) < self.width:
                        cells_around.add((i + x, j + y))

        # Remove already made moves
        cells_around = [c for c in cells_around if c not in self.moves_made]

        # Remove all the cells that are known to be safe
        cells_around = [c for c in cells_around if c not in self.safes]

        # Remove all the cells that are mines with reducing count
        for c in cells_around:
            if c in self.mines:
                cells_around.remove(c)
                count -= 1

        # Now, when the cells around list is prepared, we make a statement
        # Statement: these cells contain {count} mines
        new_sentence = Sentence(cells_around, count)
        self.knowledge.append(new_sentence)
        
        # Remove those from memory
        del cells_around, new_sentence

        # Declare a constant empty sentence to compare sentences inside knowledge with it
        EMPTY_SENTENCE = Sentence(set(), 0)

        def update_knowledge_base():
            modified = False
        
            # Infer any new known mines and safes out of knowledge
            for sentence in self.knowledge:

                new_safes = sentence.known_safes()
                new_mines = sentence.known_mines()

                # If new safe cells were found
                if new_safes:
                    for cell in list(new_safes):
                        # Mark them as safe
                        self.mark_safe(cell)
                        
                        # If there are only mines left in that sentence 
                        if len(sentence.cells) == sentence.count:
                            
                            # Mark all the rest as mines
                            for remaining_cell in sentence.cells:
                                self.mark_mine(remaining_cell)
                        
                        # And point out that some changes were made during execution of that function 
                        modified = True

                # Same for mines
                if new_mines:
                    for cell in list(new_mines):
                        self.mark_mine(cell)
                        if sentence.count == 0:
                            for remaining_cell in sentence.cells:
                                self.mark_safe(remaining_cell)
                        modified = True
                        
            # Remove any empty sentences that may have been created
            while EMPTY_SENTENCE in self.knowledge:
                self.knowledge.remove(EMPTY_SENTENCE)
                        
            # Combine each two sentences together
            combinations = itertools.product(self.knowledge, repeat=2)
            
            # For every combination check, if one is a subset of other
            for comb in combinations:
                a, b = comb
                if a.cells.issubset(b.cells):
                    # And if so - deduce a new sentence
                    new_sentence = Sentence(
                        (b.cells - a.cells), (b.count - a.count))
                    if new_sentence != EMPTY_SENTENCE and new_sentence not in self.knowledge:
                        self.knowledge.append(new_sentence)
                        modified = True
            
            # Additional check for each sentence in case we missed some already known cell
            for sentence in self.knowledge:
                to_remove = []
                for cell in sentence.cells:
                    # Remove cells from sentences if they are safe or mines for sure
                    if cell in self.mines:
                        to_remove.append(cell)
                        sentence.count -= 1
                        modified = True
                    if cell in self.safes:
                        to_remove.append(cell)
                        modified = True
                for cell in to_remove:
                    sentence.cells.remove(cell)
            
            # Return notion that knowledge has been changed
            return modified
            
            
        # Actual function call
        modified = True
        while modified:
            # Run UPDATE while it does any changes
            modified = False
            modified = update_knowledge_base()


    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        # Safe moves are moves in 'safes' set with the exception of those who are made and mines
        safe_moves = self.safes.difference(self.moves_made, self.mines)

        if self.safes and safe_moves:
            move = list(safe_moves)[0]
            return move
        else:
            return None

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        random.seed()

        i_axis = range(self.height)
        j_axis = range(self.width)

        # Any move within the board
        possible = set(itertools.product(i_axis, j_axis, repeat=1))

        # Except already made moves and already known mines
        possible = possible.difference(self.moves_made, self.mines)

        # Return any one of those
        if len(possible) > 0:
            move = list(possible)[random.randint(0, len(possible) - 1)]
            return move
        else:
            return None


def main():
    pass
if __name__ == "__main__":
    main()
