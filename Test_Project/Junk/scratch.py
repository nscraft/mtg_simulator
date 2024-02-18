import Project.Data.deck_gen
import Project.MTG_elements.game_handler_improved

test_deck = Project.Data.deck_gen.gen_rand_deck()

result = Project.MTG_elements.game_handler_improved.run_game(test_deck)

print(test_deck)
print(result)
