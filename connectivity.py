#!/usr/bin/python3


# TODO:
# 1) Get champion's stat on specific Level
# 2) get all champion's stat on specific Level
# 3) Get the champion's name with highest stats level 1
# 4) Get the champion's name with lowest stat level 1
# 5) Get the champion's name with highest stat level 18
# 6) Get the champion's name with lowest stat level 18
# 7) Get the respective icons somehow from the web
# 8) Make everything into a proper GUI app.
# 9) Allow people to compare this patch's data to older patches

import json # used to parse the data from json to usable data
import requests # used to get the data from the API
import tkinter # will be used to create a proper interface as times go on.

# Get the most recent version every time
def get_current_version():
    currentVersionUrl = "https://ddragon.leagueoflegends.com/api/versions.json"
    responseVersion = requests.get(currentVersionUrl)
    wholeFileJson = json.loads(responseVersion.text)
    # return the very first
    return wholeFileJson[0]

# Get the champion's stats.
def get_champion_data(name):
    for champion in championsData:
        if championsData[champion].get('id') == name:
            print(championsData[champion].get('id')
            + " (" + ','.join(championsData[champion].get('tags')) + ")")
            stats = championsData[champion].get('stats')
            print(stats)


websiteURL = "https://ddragon.leagueoflegends.com/cdn/" + get_current_version() + "/data/en_US/champion.json"

response = requests.get(websiteURL)

mainJsonFile = json.loads(response.text)

championsData = mainJsonFile.get("data")

# m=tkinter.Tk()

for champion in championsData:

    # Champion's data: name, tags(marksman, tank etc) and stats
    championStats = championsData[champion].get('stats')

    # I'm splitting every stat into a variable

    hp = championStats.get('hp')
    hp_per_lvl = championStats.get('hpperlevel')
    hp_at_max_lvl = round(( hp + ( hp_per_lvl * 18)), 2)

    hp_regen = championStats.get('hpregen')
    hp_regen_per_lvl = championStats.get('hpregenperlevel')
    hp_regen_at_max_lvl = round( (hp_regen + (hp_regen_per_lvl * 18)), 2)

    mana_pool = championStats.get('mp')
    mana_pool_per_lvl = championStats.get('mpperlevel')
    mana_pool_at_max_lvl = round( (mana_pool + (mana_pool_per_lvl * 18)), 2)

    mana_pool_regen = championStats.get('mpregen')
    mana_pool_regen_per_lvl = championStats.get('mpregenperlevel')
    mana_pool_rege_at_max_lvl = round( (mana_pool_regen + (mana_pool_regen_per_lvl * 18)), 2)

    movement_speed = championStats.get('movespeed')

    armor = championStats.get('armor')
    armor_per_lvl = championStats.get('armorperlevel')
    armor_at_max_lvl = round( (armor + (armor_per_lvl * 18)), 2)

    magic_resistance = championStats.get('spellblock')
    magic_resistance_per_lvl = championStats.get('spellblockperlevel')
    magic_resistance_at_max_lvl = round( (magic_resistance + (magic_resistance_per_lvl * 18)), 2)

    attack_range = championStats.get('attackrange')

    attack_dmg = championStats.get('attackdamage')
    attack_dmg_per_lvl = championStats.get('attackdamageperlevel')
    attack_dmg_at_max_lvl = round( (attack_dmg + (attack_dmg_per_lvl * 18)), 2)

    attack_speed = championStats.get('attackspeed')
    attack_speed_per_lvl = championStats.get('attackspeedperlevel')
    attack_speed_at_max_lvl = round( (attack_speed + (attack_speed * 18)), 2)

# m.mainloop()
