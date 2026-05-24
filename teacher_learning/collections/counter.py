# from collections import Counter

# signals = ['BUY', 'SELL', 'HOLD', 'BUY', 'SELL', 'BUY']
# # Using Counter to count the occurrences of each signal
# signals_count = Counter(signals)

# print(signals_count)


##############################################################################

# from collections import Counter

# marks = [80, 90, 80, 70, 90, 80, 60, 70, 90]

# marks_count = Counter(marks)

# print(marks_count)
# print(marks_count[80])
# print(marks_count[60])
# print(marks_count[100])

##################################################################################

# from collections import Counter

# marks = [80, 90, 80, 70, 90, 80, 60, 70, 90]

# marks_count = Counter(marks)

# print(marks_count.most_common()) # Give me all items sorted by count, highest first.
# print(marks_count.most_common(2))
# print(marks_count.most_common(1))



#########################################################################################



# from collections import Counter

# signals = ["BUY", "SELL", "BUY", "HOLD", "BUY", "SELL", "HOLD"]

# signal_count = Counter(signals)

# print(signal_count)
# print(signal_count.most_common())
# print(signal_count.most_common(2))

# print(type(signal_count))
# print(type(signal_count.most_common()))
# print(type(signal_count.most_common()[0]))

##############################################################################


# from collections import Counter

# symbols = ["NIFTY", "BANKNIFTY", "NIFTY", "RELIANCE", "NIFTY", "RELIANCE"]

# symbol_count = Counter(symbols)

# top_symbol, top_frequency = symbol_count.most_common(1)[0]

# print(symbol_count)
# print(top_symbol)
# print(top_frequency)

##############################################################


# from collections import Counter

# symbols = ["NIFTY", "BANKNIFTY", "NIFTY", "RELIANCE", "NIFTY", "RELIANCE"]

# symbol_count = Counter(symbols)

# top_symbol, top_frequency = symbol_count.most_common(1)[0]

# print(symbol_count)
# print(top_symbol)
# print(top_frequency)


###############################################################################

# from collections import Counter

# daily_signal_count = Counter()

# morning_signals = ["BUY", "BUY", "SELL"]
# afternoon_signals = ["HOLD", "BUY", "SELL"]
# evening_signals = ["SELL", "SELL", "BUY"]

# daily_signal_count.update(morning_signals)
# daily_signal_count.update(afternoon_signals)
# daily_signal_count.update(evening_signals)

# print(daily_signal_count)
# print(daily_signal_count.most_common(1))



##############################################################################

# from collections import Counter

# marks_count = Counter([80, 90, 80])

# marks_count.update([90, 90, 70])

# print(marks_count)
# print(marks_count.most_common())


###########################################################################
# Counter.subtract()

# subtract() is the opposite of update().
########################################################################


# from collections import Counter

# stock = Counter(["saree", "saree", "kurti", "dupatta"])

# stock.subtract(["saree", "kurti"])

# print(stock)


# stock.subtract(["saree", "kurti"]) -> makes kurticount negative 

'''
Mental model :
     
update()   -> add counts
subtract() -> reduce counts

'''

#################################################################

# from collections import Counter

# inventory = Counter(["pen", "pen", "book", "copy", "copy", "copy"])

# inventory.subtract(["copy", "pen", "bag"])

# print(inventory)

#################################################################

'''
elements()

elements() rebuilds items from their counts.

'''

# from collections import Counter

# c = Counter({"pen": 2, "book": 1, "bag": -1})

# print(list(c.elements()))

#############################################################################

# from collections import Counter

# stock = Counter({
#     "saree": 3,
#     "kurti": 2,
#     "dupatta": 0,
#     "blouse": -1
# })

# print(list(stock.elements()))

'''
So elements() means:

“Give me the original-style repeated items back, but only for positive counts.”
'''

##################################################################################


# Mini project: Counter in trading signals

# from collections import Counter

# morning = ["BUY", "SELL", "BUY", "HOLD"]
# afternoon = ["SELL", "BUY", "SELL"]
# evening = ["HOLD", "BUY", "EXIT"]

# signal_count = Counter()

# # update signal_count using morning, afternoon, evening
# signal_count.update(morning)
# signal_count.update(afternoon)
# signal_count.update(evening)

# # print full counter
# print(signal_count)

# # print most common signal
# print(signal_count.most_common(1)[0])

# # print all signals using a loop:
# for sig, count in signal_count.most_common():
#     print(f'{sig} appeared {count} times')
    

###################################################################################

































































































































































