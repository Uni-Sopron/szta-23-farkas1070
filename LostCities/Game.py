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
            self.drawpile (Drawpile): the drawpile of the game
            self.discardpile1 (Discardpile) = the first discardpile
            self.discardpile2 (Discardpile) = the second discardpile
            self.discardpile3 (Discardpile) = the third discardpile
            self.discardpile4 (Discardpile) = the fourth discardpile
            self.discardpile5 (Discardpile) = the fifth discardpile
            self.player1_piles (array) = player1-s playercardpiles
            self.player2_piles (array) = player2-s playercardpiles
            self.current_round (int): which round are we currently in.
            self.MAXROUNDS (int): 3 max rounds in game
            self.current_player (Player): the current player


        """

        self.MAXROUNDS = 3
        self.current_round = 1

        self.Player1 = Player(1)
        self.Player2 = Player(2)

        self.setupforround()

        print(self.current_player_piles)

        print(len(self.Player1.cardarray))

        print(len(self.Player2.cardarray))
        print(len(self.drawpile.cardarray))
        print(self.drawpile.is_cardpile_empty())

    def setupforround(self) -> None:
        """
        this function creates a new instance of every single class for every turn,except the player classes, which there the only modification needed is to clear their cardarrays, and fill them up again with 8 random cards, so there is no code duplication
        """

        self.player1_piles = [Playercardpile(1) for _ in range(5)]
        self.player2_piles = [Playercardpile(2) for _ in range(5)]
        self.current_player = (
            self.Player1 if self.Player1.age > self.Player2.age else self.Player2
        )
        self.current_player_piles = (
            self.player1_piles
            if self.current_player == self.Player1
            else self.player2_piles
        )
        self.drawpile = Drawpile()
        colors = ["green", "white", "blue", "red", "yellow"]
        self.discardpiles = [Discardpile(colors[i]) for i in range(5)]

        if len(self.Player1.cardarray) != 0 and len(self.Player2.cardarray) != 0:
            self.Player1.cardarray.clear()
            self.Player2.cardarray.clear()

        for _ in range(8):
            self.draw_card_from_drawpile(self.drawpile.cardarray, self.Player1)
            self.draw_card_from_drawpile(self.drawpile.cardarray, self.Player2)

    def draw_card_from_drawpile(self, other: Drawpile, player: Player) -> None:
        """
        Draw random card from drawpile class instance

        Args:
            other (Drawpile): “Card deck to draw cards from”
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
        Daw from one of the discardpiles. you can only draw the top card.

        Args:
            other (Discardpile): “Card deck to draw cards from”
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
        choice_str = input(
            "here are your cards, choose which one you want to discard: "
        )
        choice = int(choice_str)
        for i in range(len(player.cardarray)):
            print(f"{i +1}. card: {player.cardarray[i]}")
        if choice <= 0 or choice > len(player.cardarray):
            print("bad choice, choose again")
            choice_str = input()
            choice = int(choice_str)
        else:
            other.cardarray.append((player.cardarray[choice - 1]))
            player.cardarray.pop(choice - 1)

    def play_card(self, other: Playercardpile, player: Player) -> None:
        """
        The function used if the player wants to play their card

        Args:
            other (Playercardpile): the playercardpile which the player want to put their card on
            player (Player): the current player
        """
        print("your cards: ")
        for i in range(len(player.cardarray)):
            print(f"{i +1}. card: {player.cardarray[i]}")

        choice_str = input("choose which one you want to play ")
        choice = int(choice_str)

        if choice <= 0 or choice > len(player.cardarray):
            print("bad choice, choose again")
            choice_str = input()
            choice = int(choice_str)
        else:
            other.cardarray.append((player.cardarray[choice - 1]))
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
        """
        pass

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

        """
        pass

    def game(self) -> None:
        """
        the main function of the Game class. this will not only start the game, but ultimately this function will handle the entire game.

        """

        while self.current_round != self.MAXROUNDS + 1:
            while len(self.drawpile.cardarray) != 40:
                # playing or discarding segment

                str_choice = input(
                    f"It's your turn {self.current_player.name} what would you like to do? \n 1: Play Card \n 2: discard card "
                )
                choice = int(str_choice)

                # playing

                if choice == 1:
                    print("here are the player columns:")
                    for i, player_pile in enumerate(self.current_player_piles):
                        if len(player_pile.cardarray) == 0:
                            print(f"Pile {i+1} üres")
                        else:
                            print(player_pile.cardarray)

                    which_playercolumn = input(
                        "Which one would you like to place your card onto? choose between 1-5"
                    )

                    self.play_card(
                        self.current_player_piles[int(which_playercolumn) - 1],
                        self.current_player,
                    )

                # discarding

                elif choice == 2:
                    print("here are the discard piles:")
                    for i, discard_pile in enumerate(self.discardpiles):
                        if len(discard_pile.cardarray) == 0:
                            print(f"Pile {i+1} üres")
                        else:
                            for card in discard_pile.cardarray:
                                print(f"{card} card is: {discard_pile.cardarray[card]}")

                    which_discardcolumn = input(
                        "Which one would you like to discard your card onto? choose between 1-5"
                    )

                    self.discard_card(
                        self.discardpiles[int(which_discardcolumn)], self.current_player
                    )

                # bad choice

                else:
                    str_choice = input(
                        "bad choice, you only have 2 options, choose again, remember: \n 1:Play Card \n 2: discard card "
                    )
                    choice = int(str_choice)

                # drawing a card segment

                print("Here are the top cards from the discard piles:")
                for i, discard_pile in enumerate(self.discardpiles):
                    if len(discard_pile.cardarray) == 0:
                        print(f"Pile {i+1} üres, erről nem tudsz húzni")
                    else:
                        print(f"{i +1} oszlopról ezt tudod húzni: {discard_pile[-1]}")

                str_choice = input(
                    "Now you need to draw a card, where do you want to draw your card from? \n 1: One of the discard piles \n 2: draw pile."
                )

                if int(str_choice) == 1:
                    print("here are the discardpiles again:")
                    for i, discard_pile in enumerate(self.discardpiles):
                        if len(discard_pile.cardarray) == 0:
                            print(f"Pile {i+1} üres, erről nem tudsz húzni")
                        else:
                            print(
                                f"{i + 1} oszlopról ezt tudod húzni: {discard_pile[-1]}"
                            )

                    discardpile_choice = input("which discard pile card you want?")

                    self.draw_card_from_discardpile(
                        self.discardpiles[int(discardpile_choice)].cardarray,
                        self.current_player,
                    )

                elif int(str_choice) == 2:
                    self.draw_card_from_drawpile(
                        self.drawpile.cardarray, self.current_player
                    )
                else:
                    str_choice = input(
                        "bad choice, you only have 2 options, choose again, remember: \n 1: One of the discard piles \n 2: draw pile. "
                    )
                    choice = int(str_choice)

                # this is the end of 1 turn, now we change it.
                self.change_turn()

            if not self.is_game_over():
                self.end_turn()
                self.setupforround()
                self.current_round += 1
            else:
                self.end_game()
