# lolStats

This program allows you to see the stats for all league of legends champions.
You can use it to see the stats of a specific champion on a specific level too.

By default it will try to get the data from the most recent patch but that can be changed.

![Example of how it looks](https://i.imgur.com/V9QNcO1.png "UI")

**Requires requests module for python:**
>pip install requests

**How to use:**
By default the program gets Kayn's data and displays it in the console.

If you're using something like IDLE, you can then call functions like:
get_every_champion() - gets every champion, their tags and all stats.
def get_champion_data(name):
get_champions_stat_on_specific_level(name, level)