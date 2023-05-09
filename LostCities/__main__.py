from Discardpile import Discardpile
from Drawpile import Drawpile
from Game import Game
from Player import Player
from Playercardpile import Playercardpile

if __name__ == "__main__":

    def startgame() -> None:
        colors = ["green", "white", "blue", "red", "yellow"]
        Player1 = Player(1)
        Player2 = Player(2)
        player1_piles = [Playercardpile(colors[i]) for i in range(5)]
        player2_piles = [Playercardpile(colors[i]) for i in range(5)]
        current_player = Player1 if Player1.age > Player2.age else Player2
        current_player_piles = (
            player1_piles if current_player == Player1 else player2_piles
        )
        drawpile = Drawpile()
        discardpiles = [Discardpile(colors[i]) for i in range(5)]

        game = Game(
            colors,
            3,
            1,
            Player1,
            Player2,
            player1_piles,
            player2_piles,
            current_player,
            current_player_piles,
            drawpile,
            discardpiles,
        )
        game.game()

    startgame()
