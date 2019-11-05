#!/user/bin/python3

import re

acc_num = ['xkn59438','yhdck2','eihd39d9','chdsye847','hedle3455','xjhd53e','45da','de37dp']

#contain number 5
for acc in acc_num:
    if re.search(r'5',acc):
        print(acc)
    else:
        print('Not Found')

#contain letter d or e
for acc in acc_num:
    if re.search(r'[de]',acc):
        print(acc)
    else:
        print('Not Found')

#contain letter d and e 
for acc in acc_num:
    if re.search(r'de',acc):
        print(acc)
    else:
        print('Not Found')
        
#contain the letters d and e in that order with a single letter between them
for acc in acc_num:
    if re.search(r'd.e',acc):
        print(acc)
    else:
        print('Not Found')

#contain both the letters d and e in any order
for acc in acc_num:
    if re.search(r'd', acc) and re.search(r'e', acc) :
        print(acc)
    else:
        print('Not Found')

#start with x or y
for acc in acc_num:
    if re.search(r'(^x|^y)',acc):
        print(acc)
    else:
        print('Not Found')
        
#start with x or y and end with e
for acc in acc_num:
    if re.search(r'(^x|^y)',acc) and re.search(r'e$',acc):
        print(acc)
    else:
        print('Not Found')

#contain three or more numbers in a row
for acc in acc_num:
    if re.search(r'[0123456789]{3,}', acc):
        print(acc)
    else:
        print('Not Found')

#end with d followed by either a, r or p
for acc in acc_num:
    if re.search(r'[arp]$',acc):
        print(acc)
    else:
        print('Not Found')


