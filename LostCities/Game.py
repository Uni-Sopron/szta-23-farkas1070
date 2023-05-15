import os

from Discardpile import Discardpile
from Drawpile import Drawpile
from Player import Player
from Playercardpile import Playercardpile


class Game:
    def __init__(self) -> None:
        """
        This is init function of the entire game. Here we set up the players, the COLORS, the current round and the max rounds

            Member Variables:
            - self.current_round (int): The current round of the game.
            - self.MAXROUNDS (int): The maximum number of rounds in the game.
            - self.COLORS (list[str]): The colors used in the game.
            - self.numbers (list[int]): The numbers used in the game.
            - self.Player1 (Player): The first player.
            - self.Player2 (Player): The second player.
            - self.player1_piles (list[Playercardpile]): Piles of the first player.
            - self.player2_piles (list[Playercardpile]): Piles of the second player.
            - self.current_player (Player): The current player.
            - self.current_player_piles (list[Playercardpile]): Piles of the current player.
            - self.drawpile (Drawpile): The drawpile containing cards.
            - self.discardpiles (list[Discardpile]): Discard piles of the game.

        """
        self.current_round = 1
        self.MAXROUNDS = 3
        self.COLORS = ["green", "white", "blue", "red", "yellow"]
        self.numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.Player1 = Player(1)
        self.Player2 = Player(2)
        self.player1_piles = [Playercardpile(self.COLORS[i]) for i in range(5)]
        self.player2_piles = [Playercardpile(self.COLORS[i]) for i in range(5)]
        self.current_player = (
            self.Player1 if self.Player1.age > self.Player2.age else self.Player2
        )
        self.current_player_piles = (
            self.player1_piles
            if self.current_player == self.Player1
            else self.player2_piles
        )
        self.drawpile = Drawpile(self.COLORS, self.numbers)
        self.discardpiles = [Discardpile(self.COLORS[i]) for i in range(5)]

        for _ in range(8):
            self.draw_card_from_drawpile(self.drawpile.cardarray, self.Player1)
            self.draw_card_from_drawpile(self.drawpile.cardarray, self.Player2)

    def clear_screen(self) -> None:
        """
        This function is used to clear the terminal, so the game is clearer
        """
        os.system("cls" if os.name == "nt" else "clear")

    def setupforround(self) -> None:
        """
        in this function we start a new round which means that we first clear all the cardarrays in the player piles and the discard piles, then, generate a new drawpile, take the cards from the players(clear their cardarray), and give them new cards.


        """
        # clear every playerpile and discardpile
        for i in range(5):
            self.player1_piles[i].cardarray.clear()
            self.player2_piles[i].cardarray.clear()
            self.discardpiles[i].cardarray.clear()

        # setup current player and current player piles
        self.current_player = (
            self.Player1
            if self.Player1.expeditionpoint > self.Player2.expeditionpoint
            else self.Player2
        )
        self.current_player_piles = (
            self.player1_piles
            if self.current_player == self.Player1
            else self.player2_piles
        )
        # recreate drawpile

        self.drawpile = Drawpile(self.COLORS, self.numbers)

        # clear cardarrays of players reasign cards
        self.Player1.cardarray.clear()
        self.Player2.cardarray.clear()
        for _ in range(8):
            self.draw_card_from_drawpile(self.drawpile.cardarray, self.Player1)
            self.draw_card_from_drawpile(self.drawpile.cardarray, self.Player2)

    def draw_card_from_drawpile(self, other: Drawpile, player: Player) -> None:
        """
        Drawing from drawpile function

        Args:
            other (Drawpile): Drawpile class instance that we get cards from
            player (Player): player that currently is playing

        """
        if len(other) == 0:
            print(
                "you cannot draw from this pile, because there are no cards to draw from"
            )
        else:
            card = other.pop(-1)
            player.cardarray.append(card)

    def draw_card_from_discardpile(self, other: Discardpile, player: Player) -> None:
        """
        drawing from on of the 5 discardpiles function


        Args:
            other (Discardpile): Drawpile class instance that we get cards from
            player (Player): player that currently is playing
        """
        if len(other) == 0:
            print(
                "you cannot draw from this pile, because there are no cards to draw from"
            )
        else:
            card = other.pop(-1)
            player.cardarray.append(card)

    def discard_card(self, other: Discardpile, player: Player) -> None:
        """
        The function used to discard a specific player's card

        Args:
            other (Discardpile): the chosen discardpile that the player wants to discard their card onto
            player (Player): The current player
        """
        print("here are the discard piles:")
        for i, discard_pile in enumerate(other):
            if len(discard_pile.cardarray) == 0:
                print(f"{i+1} {discard_pile.color} Pile üres")
            else:
                for i, card in enumerate(discard_pile.cardarray):
                    print(f"{i} card is: {card}")

        while True:
            which_discardcolumn = input(
                "Pick a discardpile from 1 to 5, if you see this again, it means you picked a discardpile, with a color that you don't have, pick another one"
            )
            color_to_check = other[int(which_discardcolumn) - 1].color
            has_color = any(card.color == color_to_check for card in player.cardarray)
            if has_color:
                break

        print("your cards: ")
        for i in range(len(player.cardarray)):
            print(f"{i +1}. card: {player.cardarray[i]}")

        choice_str = input("choose which one you want to discard: ")
        choice = int(choice_str)

        while (
            other[int(which_discardcolumn) - 1].color
            != player.cardarray[choice - 1].color
        ):
            choice_str = input(
                "Card's color is not equal to the chosen card's color, pick again: "
            )
            choice = int(choice_str)

        if choice <= 0 or choice > len(player.cardarray):
            print("bad choice, choose again")
            choice_str = input()
            choice = int(choice_str)
        else:
            other[int(which_discardcolumn) - 1].cardarray.append(
                (player.cardarray[choice - 1])
            )
            player.cardarray.pop(choice - 1)

    def play_card(self, other: Playercardpile, player: Player) -> None:
        """
            Plays a card from the player's card pile onto another player's card pile.

            Args:
                other (Playercardpile): The other player's card pile where the card will be played.
                player (Player): The player who will play the card.

            Returns:
        None
        """
        print("here are the player columns:")
        for i, player_pile in enumerate(other):
            if len(player_pile.cardarray) == 0:
                print(f"{i+1} {player_pile.color} Pile üres")
            else:
                print(player_pile.cardarray)

        while True:
            which_playercolumn = input(
                "Pick a playerpile from 1 to 5, if you see this again, it means you picked a playerpile, with a color that you don't have, pick another one"
            )
            color_to_check = other[int(which_playercolumn) - 1].color
            has_color = any(card.color == color_to_check for card in player.cardarray)
            if has_color:
                break

        print("your cards: ")
        for i in range(len(player.cardarray)):
            print(f"{i +1}. card: {player.cardarray[i]}")

        choice_str = input("choose which one you want to play ")
        choice = int(choice_str)

        while (
            other[int(which_playercolumn) - 1].color
            != player.cardarray[choice - 1].color
        ):
            choice_str = input(
                "Card's color is not equal to the chosen card's color, pick again: "
            )
            choice = int(choice_str)

        if choice <= 0 or choice > len(player.cardarray):
            print("bad choice, choose again")
            choice_str = input()
            choice = int(choice_str)
        else:
            other[int(which_playercolumn) - 1].cardarray.append(
                (player.cardarray[choice - 1])
            )
            player.cardarray.pop(choice - 1)

    def is_game_over(self) -> bool:
        """
        check if game is over

        Returns:
            bool: yes if game is over no if its not. game over if round 3 has been completed
        """
        return self.current_round == self.MAXROUNDS

    def change_turn(self) -> None:
        """
        changes the turn which means that the self.currentplayer variable will be changed to the other player
        """
        if self.current_player == self.Player1:
            self.current_player = self.Player2
            self.current_player_piles = self.player2_piles
        else:
            self.current_player = self.Player1
            self.current_player_piles = self.player1_piles

    def end_game(self) -> None:
        """
        here every scoring things will be calculated

            Member Variables:
                winner (Player): the winner player
        """
        winner = (
            self.Player1
            if self.Player1.expeditionpoint > self.Player2.expeditionpoint
            else self.Player2
        )
        print(
            f"The game is over. the winner is {winner.name}, with {winner.expeditionpoint} points."
        )

    def end_turn(self) -> None:
        """
        clalculate the score for 1 turn.
        """

        for player_pile in self.player1_piles:
            player_pile.calculate_result()
            print(player_pile.result)
            self.Player1.expeditionpoint += player_pile.result
            # self.Player1.expeditionpoint += player_pile.calculate_sum()
        print(
            f"{self.Player1.name} in this round you ended up with the sum of {self.Player1.expeditionpoint} points."
        )

        for player_pile in self.player2_piles:
            player_pile.calculate_result()
            print(player_pile.result)
            self.Player2.expeditionpoint += player_pile.result
            # self.Player2.expeditionpoint += player_pile.calculate_sum()
        print(
            f"{self.Player2.name} in this round you ended up with the sum of {self.Player2.expeditionpoint} points."
        )

        print(
            f"round {self.current_round} is over, the winner of this round is {self.Player1.name if self.Player1.expeditionpoint > self.Player2.expeditionpoint else self.Player2.name}"
        )

    def handle_turn(self) -> None:
        """
        This function will handle each turn for the players.

        Member Variables:
            str_choice (str) = the choice in string that the user choose to either play or discard a card
            discardpile_choice (str) = the numbr of the discardpile that the user wantr to discard their card onto
        """
        str_choice = input(
            f"It's your turn {self.current_player.name} what would you like to do? \n 1: Play Card \n 2: discard card "
        )
        # playing
        match int(str_choice):
            case 1:
                self.play_card(
                    self.current_player_piles,
                    self.current_player,
                )
            # discarding

            case 2:
                self.discard_card(self.discardpiles, self.current_player)

            # bad choice

            case _:
                str_choice = input(
                    "bad choice, you only have 2 options, choose again, remember: \n 1:Play Card \n 2: discard card "
                )

        # drawing a card segment

        print("Here are the top cards from the discard piles:")
        for i, discard_pile in enumerate(self.discardpiles):
            discard_pile.print_last_element(i)

        str_choice = input(
            "Now you need to draw a card, where do you want to draw your card from? \n 1: One of the discard piles \n 2: draw pile."
        )
        match int(str_choice):
            case 1:
                print("here are the discardpiles again:")
                for i, discard_pile in enumerate(self.discardpiles):
                    discard_pile.print_last_element(i)

                discardpile_choice = input("which discard pile card you want?")

                self.draw_card_from_discardpile(
                    self.discardpiles[int(discardpile_choice) - 1].cardarray,
                    self.current_player,
                )

            case 2:
                self.draw_card_from_drawpile(
                    self.drawpile.cardarray, self.current_player
                )
            case _:
                str_choice = input(
                    "bad choice, you only have 2 options, choose again, remember: \n 1: One of the discard piles \n 2: draw pile. "
                )

    def game(self) -> None:
        """
        the main function of the Game class. this will not only start the game, but ultimately this function will handle the entire game.

        """

        while self.current_round != self.MAXROUNDS + 1:
            # because in the first round everything is already setup
            if self.current_round != 1:
                print(f"round {self.current_round} begins")
                self.setupforround()

            while len(self.drawpile.cardarray) != 40:
                # playing or discarding segment
                self.handle_turn()
                # this is the end of 1 turn, now we change it.
                self.change_turn()

            if not self.is_game_over():
                self.end_turn()

                self.current_round += 1
            else:
                self.end_game()
                print(len(self.drawpile.cardarray))
                break
