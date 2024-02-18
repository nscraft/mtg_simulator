import Project.MTG_elements.game_improved


def run_game(deck_df):
    instance = Project.MTG_elements.game_improved.GameComponents(deck_df)
    instance.set_commander_to_command_zone()
    instance.set_deck_to_library()
    instance.shuffle()
    instance.table.loc[:, 'game'] += 1
    turn = 0
    instance.draw_cards(7)
    while turn < 10:
        turn += 1
        instance.table.loc[:, 'turn'] += 1
        instance.draw_cards(1)
        instance.play_land()
        instance.cast_spells()
        instance.draw_cards(instance.bonus_draw)
