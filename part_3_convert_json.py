import cc_dat_utils
import json
import cc_classes

# Part 3
# Load your custom JSON file
input_json_file = "data/cddoylecc1.json"
json_input = None
with open(input_json_file, "r") as reader:
    json_input = json.load(reader)


# Convert JSON data to CCLevelPack
def MakeLevelPack(json_input):
    level_pack = cc_classes.CCLevelPack()
    levels = json_input["levels"]
    for level in levels:
        game_level = cc_classes.CCLevel()
        game_level.level_number = level["level_number"]
        game_level.time = level["time"]
        game_level.num_chips = level["chip_count"]
        game_level.upper_layer = level["top_layer"]
        game_level.lower_layer = level["lower_layer"]

        # fields
        title = cc_classes.CCMapTitleField(level["title"])
        password = cc_classes.CCEncodedPasswordField(level["password"])
        hint = cc_classes.CCMapHintField(level["hint"])
        mon_list = level["monsters"]
        mon_cor_list = []
        for mon in mon_list:
            mon_cor = cc_classes.CCCoordinate(mon[0], mon[1])
            mon_cor_list.append(mon_cor)
        monsters = cc_classes.CCMonsterMovementField(mon_cor_list)

        # append fields
        game_level.add_field(title)
        game_level.add_field(password)
        game_level.add_field(hint)
        game_level.add_field(monsters)

        # put into pack
        level_pack.add_level(game_level)
    return level_pack


# Save converted data to DAT file
cc_dat_utils.write_cc_level_pack_to_dat(MakeLevelPack(json_input), "cddoyle_cc1.dat")