import Project.Data.deck_gen
import Project.Events.game_handler_improved
import Project.Analytics.game_reporter_improved

test_deck = Project.Data.deck_gen.gen_rand_deck()

result = Project.Events.game_handler_improved.run_game(test_deck, game_num=2)

report = Project.Analytics.game_reporter_improved.game_report_multi()
