import Project.Data.game_records
import Project.Data.game_records
from Project.Events.game import GameComponents


def run_game(deck_df, game_num):
    instance = GameComponents(deck_df=deck_df)
    game_num = game_num
    turn = 1
    while turn <= 10:
        if turn == 1:
            instance.shuffle()
            instance.draw_cards(7)
        else:
            instance.draw_cards(1)
        instance.play_land()
        instance.cast_spells()
        instance.draw_cards(instance.spell_draw)
        Project.Data.game_records.update_records(
            game_library=instance.library,
            game_hand=instance.hand,
            game_battlefield=instance.battlefield,
            game_turn=turn,
            game_num=game_num
        )
        turn += 1


def run_game_multiple(deck_df, game_num):
    Project.Data.game_records.destroy_files()
    Project.Data.game_records.reset_records_inMemory()
    games = 1
    while games <= game_num:
        run_game(deck_df, game_num=games)
        games += 1
    Project.Data.game_records.finalize_records()
