import Project.Data.game_records
from Project.MTG_elements.auto_game_components import GameComponents


def run_game(deck_df):
    instance = GameComponents(deck_df=deck_df)
    turn = 1
    Project.Data.game_records.reset_save()
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
            game_turn=turn)
        turn += 1
