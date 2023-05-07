from Discardpile import Discardpile
from Drawpile import Drawpile
from Player import Player
from Playercardpile import Playercardpile


class Game:
    def __init__(self) -> None:
        """The game class. Here every other class will be made and the game itself will be written


        Member variables:
            self.Player1 (Player): player1
            self.Player2 (Player): player2
            self.MAXROUNDS (int): 3 max rounds in game
            self.current_round (int): current round variable


        """

        self.MAXROUNDS = 3
        self.current_round = 1
        self.Player1 = Player(1)
        self.Player2 = Player(2)

        self.setupforround()

        print(len(self.Player1.cardarray))
        print(len(self.Player2.cardarray))
        print(len(self.drawpile.cardarray))
        print(self.drawpile.is_cardpile_empty())

    def setupforround(self) -> None:
        """
        this function creates a new instance of every single class for every turn,except the player classes, which there the only modification needed is to clear their cardarrays, and fill them up again with 8 random cards, so there is no code duplication

        Member variables:
            self.player1_piles list[Wagercard,ExpeditionCard] : player1's playerpiles
            self.player2_piles list[Wagercard,ExpeditionCard] : player2's playerpiles
            self.current_player Union[self.Player1,self.Player2] : current player
            self.current_player_piles Union[self.player1_piles,self.player2_piles] : current player's playerpiles
            self.drawpile : drawpile class instance
            self.discardpiles : 5 of different discardpile class instancs

        """
        colors = ["green", "white", "blue", "red", "yellow"]
        self.player1_piles = [Playercardpile(colors[i]) for i in range(5)]
        self.player2_piles = [Playercardpile(colors[i]) for i in range(5)]
        self.current_player = (
            self.Player1 if self.Player1.age > self.Player2.age else self.Player2
        )
        self.current_player_piles = (
            self.player1_piles
            if self.current_player == self.Player1
            else self.player2_piles
        )
        self.drawpile = Drawpile()

        self.discardpiles = [Discardpile(colors[i]) for i in range(5)]

        if len(self.Player1.cardarray) != 0 and len(self.Player2.cardarray) != 0:
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
            card = other[-1]
            player.cardarray.append(card)
            other.remove(card)

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
            card = other[-1]
            player.cardarray.append(card)
            other.remove(card)

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
            while len(self.drawpile.cardarray) != 0:
                # playing or discarding segment
                self.handle_turn()
                # this is the end of 1 turn, now we change it.
                self.change_turn()

            if not self.is_game_over():
                self.end_turn()
                self.setupforround()
                self.current_round += 1
            else:
                self.end_game()
