from Project.MTG_elements.goldfish import GoldfishGame
from Project.Data.deck_loader import write_deck

game_instance = GoldfishGame(deck_df=write_deck())


class Handler:

    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, request):
        if not self._successor:
            raise NotImplementedError('Must define handle method or set a successor')
        self._successor.handle(request)


class DrawCardHandler(Handler):

    def handle(self, request):
        if request == 'draw_cards':
            try:
                draw_str = int(input("How many more cards would you like to draw?"))
            except ValueError:
                print("Please enter a valid integer.")
                return
            GoldfishGame.draw_cards(game_instance, draw_str)
            print("Cards in Library:", len(game_instance.library))
            print("Cards in Hand:", game_instance.hand)
            print("Cards in Graveyard:", game_instance.graveyard)
        else:
            super().handle(request)


class DiscardCardHandler(Handler):

    def handle(self, request):
        if request == 'discard_cards':
            discard_input = input("What card(s) would you like to discard?")
            try:
                discard_list = [int(card_str) for card_str in discard_input.split()]
                cards_to_discard = set(discard_list)
                GoldfishGame.discard_cards(game_instance, cards_to_discard)
            except ValueError:
                print("Please enter a valid integer.")
                return

            print("Cards in Library:", len(game_instance.library))
            print("Cards in Hand:", game_instance.hand)
            print("Cards in Graveyard:", game_instance.graveyard)
        else:
            super().handle(request)


chain_root = DrawCardHandler(DiscardCardHandler())
chain_root.handle('draw_cards')
chain_root.handle('discard_cards')
