from Project.Data import deck_gen

deck_instance = deck_gen.gen_rand_deck()


def write_deck_toexcel(deck_name, deck_df):
    file_name = f"{deck_name}.xlsx"
    return deck_df.to_excel(file_name)


write_deck_toexcel("rand_deck", deck_instance)
