import json
import requests
import tkinter

websiteURL = "https://ddragon.leagueoflegends.com/cdn/9.14.1/data/en_US/champion.json"

response = requests.get(websiteURL)

mainJsonFile = json.loads(response.text)

championsWithCritAtLVL1 = 0
championsWithCritAtLVL18 = 0

championsData = mainJsonFile.get("data")

m=tkinter.Tk()

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
    
    print(championName + " (" + ','.join(championTags) + ")")
    
    print("HP: " +str(hp) +"\tPer Level: " +str(hp_per_lvl) + "\tAt 18: "
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
          "\tAt 18:" + str(attack_dmg_at_max_lvl))

    print("Attack speed: " + str(attack_speed) + "\tPer Level: " + str(attack_speed_per_lvl) +
          "\tAt 18: " + str(attack_speed_at_max_lvl) + "\n")

m.mainloop()
