import csv
import json

with open("./data/race_modifiers.csv", "r") as fp:
    reader = csv.reader(fp, delimiter=",", quotechar='"')
    lines = []
    for row in reader:
        lines.append(row)


race_modifier_json = {}
stat_lines = lines[1:]
for i in stat_lines:
    stat_json = {
        "strength": i[1],
        "dexterity": i[2],
        "constitution": i[3],
        "intelligence": i[4],
        "wisdom": i[5],
        "charisma": i[6]
    }
    for key in stat_json:
        if len(stat_json[key]) == 0:
            stat_json[key] = 0
        elif stat_json[key] == "#ERROR!":
            stat_json[key] = 0
        else:
            stat_json[key] = int(stat_json[key])
    race_modifier_json[i[0]] = stat_json

print(race_modifier_json)
with open("./data/races.json", "w") as fp:
    json.dump(race_modifier_json, fp, indent=4)
