from Project.Data import deck_loader

deck_instance = deck_loader.gen_deck()


def write_deck_toexcel(deck_name, deck_df):
    file_name = f"{deck_name}.xlsx"
    return deck_df.to_excel(file_name)


write_deck_toexcel("rand_deck_1", deck_instance)
