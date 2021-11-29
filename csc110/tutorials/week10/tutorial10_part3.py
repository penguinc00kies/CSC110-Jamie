"""CSC110 Tutorial 10: Abstract Data Types and Inheritance

Module Description
==================
This module contains the implementation of a simple number game.
The key class design feature here is *inheritance*, which is used to enable
different types of players, both human and computer, for the game.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 David Liu, Mario Badr, and Tom Fairgrieve.
"""
from __future__ import annotations  # This is a technical import that you may ignore

import random


class NumberGame:
    """A number game for two players.

    A count starts at 0. On a player's turn, they add to the count an amount
    between a set minimum and a set maximum. The player who brings the count
    to a set goal amount is the winner.


    The game can have multiple rounds.

    Instance Attributes:
     -  goal: The amount to reach in order to win the game.
     -  min_step: The minimum legal move.
     -  max_step: The maximum legal move.
     -  current: The current value of the game count.
     -  players: The two players.
     -  turn: The turn the game is on, beginning with turn 0.
              If turn is even number, it is players[0]'s turn.
              If turn is any odd number, it is player[1]'s turn.

    Representation Invariants:
        - self.turn >= 0
        - 0 <= self.current
        - 0 < self.min_step <= self.max_step <= self.goal
    """
    goal: int
    min_step: int
    max_step: int
    current: int
    players: tuple[Player, Player]
    turn: int

    def __init__(self, goal: int, min_step: int, max_step: int,
                 player0: Player, player1: Player) -> None:
        """Initialize this NumberGame.

        Preconditions:
            - 0 < min_step <= max_step <= goal
        """
        self.goal = goal
        self.min_step = min_step
        self.max_step = max_step
        self.current = 0
        self.players = (player0, player1)
        self.turn = 0

    def play(self) -> None:
        """Play this NumberGame.

        Print out the moves of the game, as well as who won at the end.
        """
        print('Player 0 | Player 1 | count')
        print('-------- | -------- | -----')
        print('         |          | 0    ')

        while self.current < self.goal:
            self.play_one_turn()

        # When the loop ends, the player who went one turn before is the winner.
        print(f'\nAnd Player {(self.turn - 1) % 2} is the winner!!!')

    def play_one_turn(self) -> None:
        """Play a single turn in this NumberGame.

        Determine whose move it is, get their move, and update the current
        total as well as the number of the turn we are on.
        Print the move and the new total.
        """
        next_player = self.turn % 2
        amount = self.players[next_player].move(
            self.current,
            self.min_step,
            self.max_step,
            self.goal
        )
        self.current += amount
        self.turn += 1

        # We use some string formatting to display the game moves.
        # Don't worry about the exact formatting here.
        if next_player == 0:
            print(f'{amount: <8} |          | {self.current: <5}')
        else:
            print(f'         | {amount: <8} | {self.current: <5}')


# TODO: Write classes Player (parent), RandomPlayer, and UserPlayer.

class Player:
    """Players, are you ready?"""

    def move(self, current: int, min_step: int, max_step: int, goal: int) -> int:
        """Sam says, hands on your head"""
        raise NotImplementedError

class RandomPlayer(Player):
    """Players, yes, or no?"""

    def move(self, current: int, min_step: int, max_step: int, goal: int) -> int:
        """How do you feel about, this logo?'"""
        minimum = min((goal - current, min_step))
        maximum = min((goal - current, max_step))
        if minimum == maximum:
            return minimum
        return random.randint(min_step, min(goal-current, maximum))

class UserPlayer(Player):
    """We're in the data collection portion of the game"""

    def move(self, current: int, min_step: int, max_step: int, goal: int) -> int:
        """How do you feel about, this logo?'"""
        play = int(input('Enter the amount to move: '))
        return int(play)

def run_example_game() -> None:
    """Run an example game."""
    player1 = RandomPlayer()
    player2 = UserPlayer()
    game = NumberGame(21, 1, 3, player1, player2)
    game.play()


if __name__ == '__main__':
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()
