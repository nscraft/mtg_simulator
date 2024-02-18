import Project.Events.game_improved
import Project.Data.game_records_improved


def run_game(deck_df, game_num):
    Project.Data.game_records_improved.destroy_files()
    Project.Data.game_records_improved.reset_gamestate_inMemory()
    game_loop = 0
    instance = Project.Events.game_improved.GameComponents(deck_df)
    while game_loop < game_num:
        game_loop += 1
        instance.table.loc[:, 'game'] += 1
        turn_loop = 0
        instance.table.loc[:, 'turn'] = 0
        instance.set_commander_to_command_zone()
        instance.set_deck_to_library()
        instance.shuffle()
        instance.draw_cards(7)
        while turn_loop < 10:
            turn_loop += 1
            instance.table.loc[:, 'turn'] += 1
            instance.draw_cards(1)
            instance.play_land()
            instance.cast_spells()
            instance.draw_cards(instance.bonus_draw)
            Project.Data.game_records_improved.update_gamestate_records(
                instance.table
            )
    Project.Data.game_records_improved.save_records()
