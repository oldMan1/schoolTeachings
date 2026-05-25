#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 22:49:25 2026

@author: chalu

OrderedDict

Dictionary that is specially designed for order operations.

Modern normal dictionaries already preserve insertion order, so OrderedDict is less 
commonly needed now.
"""


'''
Yes — for OrderedDict, the main special order operation is exactly this:

move an existing key to the end
move an existing key to the beginning
remove from the end
remove from the beginning

So the two big methods are:

od.move_to_end(key)              # move key to last/right
od.move_to_end(key, last=False)  # move key to first/left

and:

od.popitem(last=True)   # remove last/right item
od.popitem(last=False)  # remove first/left item

'''

# from collections import OrderedDict

# od = OrderedDict()

# od["A"] = 10
# od["B"] = 20
# od["C"] = 30
# od["D"] = 40

# od.move_to_end("B")

# print(list(od.keys()))


###################################################################################

'''
Now your exercise:

Write this code yourself:

Create an OrderedDict called recent.

Add:

"NIFTY": 22000
"BANKNIFTY": 48000
"RELIANCE": 2900
Move "NIFTY" to the end.
Add "TCS": 3900.
Remove the oldest item.
Print recent.

Expected final keys:

['RELIANCE', 'NIFTY', 'TCS']

'''

from collections import OrderedDict

recent = OrderedDict()

recent['NIFTY'] = 22000
recent['BANKNIFTY']= 48000
recent['RELIANCE'] = 2900

recent.move_to_end('NIFTY')

recent['TCS'] = 3900

recent.popitem(last= False)

print(recent)




































