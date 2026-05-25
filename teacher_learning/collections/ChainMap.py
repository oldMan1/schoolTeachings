#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 22:49:50 2026

@author: chalu

ChainMap

Combines multiple dictionaries into one lookup view.







A. Beginner explanation

ChainMap lets you treat multiple dictionaries like one dictionary.

Instead of merging dictionaries permanently, it keeps them separate but searches them one by one.

from collections import ChainMap

user_settings = {"theme": "dark"}
default_settings = {"theme": "light", "language": "English"}

settings = ChainMap(user_settings, default_settings)

print(settings["theme"])
print(settings["language"])

Output:

dark
English

Why?

Python first checks:

user_settings

Then if key is not found, it checks:

default_settings

So:

theme

comes from user_settings.

But:

language

is not present in user_settings, so it comes from default_settings.













B. Mental model

Think of ChainMap like stacked transparent sheets.

Top layer:     user_settings
Second layer:  default_settings

When you ask for a key, Python looks from top to bottom.

settings["theme"]

1. Is "theme" in user_settings? Yes → use it.
2. Stop searching.

For another key:

settings["language"]

1. Is "language" in user_settings? No.
2. Is "language" in default_settings? Yes → use it.

Important: ChainMap does not copy dictionaries.

It only links them.

"""

# from collections import ChainMap

# user_settings = {"theme": "dark"}
# default_settings = {"theme": "light", "language": "English"}

# settings = ChainMap(user_settings, default_settings)

# print(settings["theme"])
# print(settings["language"])





# default_config = {
#     "symbol": "NIFTY",
#     "timeframe": "5min",
#     "capital": 100000,
#     "mode": "paper"
# }

# user_config = {
#     "capital": 50000,
#     "mode": "live"
# }



# from collections import ChainMap

# config = ChainMap(user_config, default_config)

# print(config["symbol"])
# print(config["capital"])
# print(config["mode"])



'''
H. Useful methods
1. .maps

Shows the list of dictionaries inside the ChainMap.

print(config.maps)

2. .new_child()

Adds a new dictionary layer on top.

from collections import ChainMap

base = {"mode": "paper", "capital": 100000}

config = ChainMap(base)

session_config = config.new_child({"mode": "live"})

print(session_config["mode"])
print(session_config["capital"])

Output:

live
100000

Mental model:

session override
↓
base config

3. .parents

Returns everything except the first dictionary.

print(session_config.parents)

Useful when you want to remove the top override layer.

'''

# Practice task

# Do this yourself.

# Create these three dictionaries:


defaults = {
    "symbol": "NIFTY",
    "timeframe": "5min",
    "capital": 100000,
    "mode": "paper"
}

config_file = {
    "capital": 200000,
    "broker": "zerodha"
}

runtime = {
    "timeframe": "1min"
}


# Now create a ChainMap where priority is:

# runtime
# config_file
# defaults

# Then print:

# symbol
# timeframe
# capital
# mode
# broker

from collections import ChainMap

mychainmap = ChainMap(runtime,config_file, defaults)


print(mychainmap['symbol'])
print(mychainmap['timeframe'])
print(mychainmap['capital'])
print(mychainmap['mode'])
print(mychainmap['broker'])




'''
It reads from the first dictionary where it finds the key, but writes only 
to the first dictionary of the ChainMap, whether the key exists there or not.


ChainMap reads from the first dictionary where the key is found, but writes 
only to the first dictionary.


READ   → searches all dictionaries from left to right
WRITE  → first dictionary only
DELETE → first dictionary only
'''



'''
Just remember:

normal = dict(hashmap_object)

creates a separate normal dictionary copy of the currently visible values.
'''


















