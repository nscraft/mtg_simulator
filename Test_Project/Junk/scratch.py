import Project.Data.deck_gen
import Project.Events.game_handler_improved
import Project.Analytics.game_reporter_improved
from Events.game_improved import GameComponents

test_deck = Project.Data.deck_gen.gen_rand_deck()

# result = Project.Events.game_handler_improved.run_game(test_deck, game_num=10)

#report = Project.Analytics.game_reporter_improved.game_report_multi()
