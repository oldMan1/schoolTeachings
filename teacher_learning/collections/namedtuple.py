#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 22:30:10 2026

@author: chalu


Think of namedtuple as:

a tuple with field names



Change it to make a Trade namedtuple with:

symbol
entry_price
exit_price
quantity

"""

from collections import namedtuple
# Trade = namedtuple("Trade", ['symbol', 'entry_price', 'exit_price', 'quantity'])

# T1 = Trade('TCS', 4000, 5000, 2000)

# profit = T1.quantity * (T1.exit_price - T1.entry_price)

# print('profit =',profit)

##############################################################################

# Because a namedtuple is still a tuple internally, you can unpack it.

# from collections import namedtuple

# Candle = namedtuple("Candle", ["time", "open", "high", "low", "close"])

# c1 = Candle("09:15", 100, 110, 95, 108)

# time, open_price, high, low, close = c1

# print(time)
# print(open_price)
# print(high)
# print(low)
# print(close)

# if open_price < close:
#     print('green candle')
# else:
#     print('red candle')

################################################################################
# as_dict method -> converst namedtuple to dictionary , done it may be useful 
# during dataframe formation

# candle_dict = c1._asdict()

# print(candle_dict)


###################################################################################

'''
Because namedtuple behaves like a tuple.

So instead of modifying the old object, we create a new updated copy.

For that, use:

_replace()

'''

#c2 = c1._replace(close = 0,low = 100) # replaced close with 0 and low with 100 in the new object c2


'''
Next concept: defaults in namedtuple

Mental model

Defaults apply from the right side.

Trade = namedtuple(
    "Trade",
    ["symbol", "entry_price", "exit_price", "quantity"],
    defaults=[None, 1]
)

Fields are:

symbol, entry_price, exit_price, quantity

Defaults are:

None, 1

So Python matches from the right:

exit_price → None
quantity   → 1

That means these two fields become optional:

t1 = Trade("TCS", 4000)

Python understands:

t1 = Trade("TCS", 4000, None, 1)

'''

Trade = namedtuple(
    "Trade",
    ["symbol", "entry_price", "exit_price", "quantity"],
    defaults=[None, 1]
)

t1 = Trade("TCS", 4000)
print(t1)



'''
Small challenge

Create an Order namedtuple with fields:

symbol
side
quantity
status

Set default:

status = "PENDING"

Create:

o1 = Order("RELIANCE", "BUY", 10)

Then use _replace() to create:

status = "EXECUTED"

Print both orders.
'''

Order = namedtuple('Order',
                   ['symbol','side','quantity','status'],
                   defaults=['PENDING']
)

o1 = Order("RELIANCE", "BUY", 10)
o2 = o1._replace(status = "EXECUTED")

print(o1)
print(o2)

'''
_fields

_fields tells you the field names of a namedtuple.

print(Order._fields)

Output:

('symbol', 'side', 'quantity', 'status')

Notice: no parentheses after _fields.

It is not a method. It is an attribute.

Use case:

for field in Order._fields:
    print(field)

This is useful when you want to inspect the structure of a record.
'''


print(o2._fields)


#################################################################################

'''
_make() is like saying:

“Take this sequence and fit it into the namedtuple fields in order.”
'''

from collections import namedtuple

Trade = namedtuple("Trade", ["symbol", "entry_price", "exit_price", "quantity"])

raw_trade = ["TCS", 4000, 5000, 2000]

t1 = Trade._make(raw_trade)

print(t1)
print(t1.symbol)
print(t1.exit_price)


###############################################################################################
'''
B. Mental model

Think:

rename=True means:
"If any field name is invalid, Python will replace it with a safe automatic name."

Example:

from collections import namedtuple

Trade = namedtuple(
    "Trade",
    ["symbol", "entry price", "class"],
    rename=True
)

print(Trade._fields)

Output:

('symbol', '_1', '_2')

Python kept "symbol" because it was valid.

It changed:

"entry price" → "_1"
"class"       → "_2"
'''

from collections import namedtuple

Row = namedtuple(
    "Row",
    ["name", "class", "marks"],
    rename=True
)

r1 = Row("Sahil", 10, 94)

print(r1)
print(Row._fields)

# Use rename=True mostly when you are quickly handling messy external data.












