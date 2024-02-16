import Project.Data.game_records
import Project.Data.game_records_batch
from Project.MTG_elements.game import GameComponents


def run_game(deck_df, game_num):
    instance = GameComponents(deck_df=deck_df)
    game_num = game_num
    turn = 1
    if game_num == 1:
        Project.Data.game_records_batch.reset_save()
    else:
        pass
    while turn <= 10:
        if turn == 1:
            instance.shuffle()
            instance.draw_cards(7)
        else:
            instance.draw_cards(1)
        instance.play_land()
        instance.cast_spells()
        instance.draw_cards(instance.spell_draw)
        Project.Data.game_records_batch.update_records(
            game_library=instance.library,
            game_hand=instance.hand,
            game_battlefield=instance.battlefield,
            game_turn=turn,
            game_num=game_num
        )

        turn += 1


def run_game_multiple(deck_df, game_num):
    games = game_num
    while games < 100:
        games += 1
        run_game(deck_df, game_num=games)
    Project.Data.game_records_batch.finalize_records()