def reset_list_of_player_characters():
    with open("list_of_player_characters.py", "w") as f:
        f.write("def get_player_character_data(name):\n")
        
reset_list_of_player_characters()