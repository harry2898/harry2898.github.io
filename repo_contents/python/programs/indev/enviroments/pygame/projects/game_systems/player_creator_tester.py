from player_character import create_player_character

manuallyCreateCharacter = False

if manuallyCreateCharacter is True:
    print("Character Creator")
    name = input("Name: ")
    race = input("Race: ")
    sex = input("Sex: ")
    classRole = input("Class: ")
else:
    name = "Tom"
    race = "Human"
    sex = "Male"
    classRole = "Priest"

create_player_character(name, race, sex, classRole)



from player_character import get_player_character

player_character = get_player_character(name)

print("")
print("Character Info:")
print("Name:", player_character.name)
print("Race:", player_character.race)
print("Sex:", player_character.sex)
print("Class:", player_character.classRole)