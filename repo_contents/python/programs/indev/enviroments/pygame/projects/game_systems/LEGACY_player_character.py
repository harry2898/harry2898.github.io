class create_player_character:
    def __init__(self, name, race, sex, classRole):
        self.name = name
        self.race = race
        self.sex = sex
        self.classRole = classRole
        
        self._save_player_character()
        self._update_list_of_player_characters()
    
    def _save_player_character(self):
        saveFileName = self.name + "_player_character_data.py"
        with open(saveFileName, "w") as saveFile:
            saveFile.write("class player_character_data:\n")
            saveFile.write("\tdef __init__(self):\n")
            saveFile.write("\t\tself.name = '" + self.name + "'\n")
            saveFile.write("\t\tself.race = '" + self.race + "'\n")
            saveFile.write("\t\tself.sex = '" + self.sex + "'\n")
            saveFile.write("\t\tself.classRole = '" + self.classRole + "'\n")
        
    def _update_list_of_player_characters(self):
        moduleNameOfSaveFile = self.name + "_player_character_data"
        with open("list_of_player_characters.py", "a") as playerCharacterList:
            #module.write("\n")
            playerCharacterList.write("\tif name == '" + self.name + "':\n")
            playerCharacterList.write("\t\tfrom " + moduleNameOfSaveFile + " import player_character_data\n")
            playerCharacterList.write("\t\treturn player_character_data()\n")



class get_player_character:
    def __init__(self, name):
        self._get_player_character_data(name)
        self._set_player_character_data()
        
    
    def _get_player_character_data(self, name):
        from list_of_player_characters import get_player_character_data
        self._playerCharacterData = get_player_character_data(name)
    
    def _set_player_character_data(self):
        #self.name = str(self._playerCharacterData.name)
        #self.race = str(self._playerCharacterData.race)
        #self.sex = str(self._playerCharacterData.sex)
        #self.classRole = str(self._playerCharacterData.classRole)
        
        self.name = str(self._playerCharacterData.name)
        self.race = str(self._playerCharacterData.race)
        self.sex = str(self._playerCharacterData.sex)
        self.classRole = str(self._playerCharacterData.classRole)        