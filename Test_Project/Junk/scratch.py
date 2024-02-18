import Project.Data.deck_gen
import Project.Events.game_handler
import Project.Analytics.game_reporter

test_deck = Project.Data.deck_gen.gen_rand_deck()

result = Project.Events.game_handler.run_game(test_deck, game_num=2)

report = Project.Analytics.game_reporter.game_report_multi()
