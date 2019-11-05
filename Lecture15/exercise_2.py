#!/user/bin/python3

import re 
dna_seq = open('long_dna.txt').read()
BpsmI = r'A[ATCG]TAAT'
BpsmII = r'GC[AG][AT]TG'

last_cut = 0
for matching in re.finditer(BpsmI, dna_seq): 
    cut_position = matching.start() + 3
    fragment_size = cut_position - last_cut
    print('Fragment size is ' + str(fragment_size))
    last_cut = cut_position
fragment_size = len(dna) - last_cut
print('Fragment size is ' + str(fragment_size))


all_cuts = []
for match in re.finditer(BpsmI, dna): 
    all_cuts.append(match.start() + 3)

for match in re.finditer(BpsmII, dna): 
    all_cuts.append(match.start() + 4)

print(all_cuts)

all_cuts.sort()
all_cuts

last_cut = 0
counter = 0
for cut_position in all_cuts:
    counter +=1
    fragment_size = cut_position - last_cut
    print('Fragment '+str(counter)+' size is ' + \
       str(fragment_size) +': '+ str(last_cut)+ ' to ' +str(cut_position) )
    last_cut = cut_position

fragment_size = len(dna) - last_cut
counter +=1
print('Fragment '+str(counter)+' size is ' + \
  str(fragment_size) +': '+ str(last_cut)+ ' to ' +str(len(dna)) )
  
