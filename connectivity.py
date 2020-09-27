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
# 10) Get number of skins per champion

import json # used to parse the data from json to usable data
import requests # used to get the data from the API

# Get the most recent version every time
def get_current_version():
    currentVersionUrl = "https://ddragon.leagueoflegends.com/api/versions.json" # get the recent version.
    responseVersion = requests.get(currentVersionUrl)
    wholeFileJson = json.loads(responseVersion.text)
    # return the very first
    return wholeFileJson[0]

def get_data(current_version):
      websiteURL = "https://ddragon.leagueoflegends.com/cdn/" + current_version + "/data/en_US/champion.json"
      response = requests.get(websiteURL)
      mainJsonFile = json.loads(response.text)
      mainJsonFile = mainJsonFile.get("data")
      return mainJsonFile

# Get the champion's stats.
def get_champion_data(name, championsData):
     for champion in championsData:
        if championsData[champion].get('id') == name:
            print(championsData[champion].get('id')
            + " (" + ','.join(championsData[champion].get('tags')) + ")")
            stats = championsData[champion].get('stats')
            return stats
     return "Champion does not exist"

def get_champions_stat_on_specific_level(name, level, championsData):
      if level <18 and level >1:
            pass
            #everything is fine.
      #else:
            #break
      for champion in championsData:
            if championsData[champion].get('id') == name:
                  print(championsData[champion].get('id')
                  + " (" + ','.join(championsData[champion].get('tags')) + ")")
                  stats = championsData[champion].get('stats')
                  print("HP: " + stats.get('hp') * level)
                  #print(stats)

#def sort_by_stat(stat):

def get_every_champion(championsData):
    for champion in championsData:
        # Champion's data: name, tags(marksman, tank etc) and stats
        championName = championsData[champion].get('id')
        championTags = championsData[champion].get('tags')
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

        # this will now all the data we have saved so far.
        # maybe later on I can save champions as name->stats dictionary?
        print(championName + " (" + ','.join(championTags) + ")")

        print("HP: " +str(hp) +"\t\tPer Level: " +str(hp_per_lvl) + "\tAt 18: "
              + str(hp_at_max_lvl))
        print("HP Regen: " + str(hp_regen) + "\tPer Level: " + str(hp_regen_per_lvl) + "\tAt 18: "
              + str(hp_regen_at_max_lvl))

        print("Mana: " + str(mana_pool) + "\tPer Level: " + str(mana_pool_per_lvl)
              + "\tAt 18: " + str(mana_pool_at_max_lvl))

        print("Mana regen: " + str(mana_pool_regen) + "\tPer Level: " + str(mana_pool_regen_per_lvl)
              + "\tAt 18: " + str(mana_pool_rege_at_max_lvl))

        print("Movement Speed: " + str(movement_speed))

        print("Armor: " + str(armor) + "\tPer Level: " + str(armor_per_lvl) +
              "\tAt 18: " + str(armor_at_max_lvl))

        print("Magic resist: " + str(magic_resistance) + "\tPer Level: " +
              str(magic_resistance_per_lvl) + "\tAt 18: " + str(magic_resistance_at_max_lvl))

        print("Attack Range: " + str(attack_range))

        print("Attack Damage: " + str(attack_dmg) + "\tPer Level: " + str(attack_dmg_per_lvl) +
              "\tAt 18: " + str(attack_dmg_at_max_lvl))

        print("Attack speed: " + str(attack_speed) + "\tPer Level: " + str(attack_speed_per_lvl) +
              "\tAt 18: " + str(attack_speed_at_max_lvl) + "\n")