import Project.Events.game_improved
import Project.Data.game_records_improved


def run_game(deck_df, game_num):
    Project.Data.game_records_improved.destroy_files()
    Project.Data.game_records_improved.reset_gamestate_inMemory()
    game = 1
    instance = Project.Events.game_improved.GameComponents(deck_df)
    instance.set_commander_to_command_zone()
    instance.set_deck_to_library()
    while game <= game_num:
        game += 1
        instance.table.loc[:, 'game'] += 1
        instance.shuffle()
        turn = 0
        instance.table.loc[:, 'turn'] = 0
        instance.draw_cards(7)
        while turn < 10:
            turn += 1
            instance.table.loc[:, 'turn'] += 1
            instance.draw_cards(1)
            instance.play_land()
            instance.cast_spells()
            instance.draw_cards(instance.bonus_draw)
            Project.Data.game_records_improved.update_gamestate_records(
                instance.table
            )
    Project.Data.game_records_improved.save_records()
