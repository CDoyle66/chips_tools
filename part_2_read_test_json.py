import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    ### Begin Add Code Here ###
    games = json_data["games"]
    for game in games:
        new_platform = test_data.Platform(game["platform"]["name"], game["platform"]["launch_year"])
        new_game = test_data.Game(game["title"], new_platform, game["year"])
        game_library.add_game( new_game )
    #Loop through the json_data
        #Create a new Game object from the json_data by reading
        #  title
        #  year
        #  platform (which requires reading name and launch_year)
        #Add that Game object to the game_library
    ### End Add Code Here ###
    return game_library


#Part 2
input_json_file = "data/test_data.json"

### Begin Add Code Here ###
with open(input_json_file,"r") as reader:
#Open the file specified by input_json_file
    json_input= json.load(reader)
#Use the json module to load the data from the file
    make_game_library_from_json(json_input)
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
    print(make_game_library_from_json(json_input))
#Print out the resulting GameLibrary data using print()
### End Add Code Here ###