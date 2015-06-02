#!/usr/bin/python

# run as "python analyze_responses.py [filename]"
# assumes tab-separated file, .tsv

import sys
import matplotlib.pyplot as plt

fname = sys.argv[1]

file = open(fname, 'r')

data = [line.split("\t") for line in file]

tot_responses = len(data)


# each entry in data is a response
# remove question headings
data.pop(0)


where_sex = [response[7].split(",") for response in data]
nw_where_sex = [[item.rstrip().lstrip() for item in response] for response in where_sex]
flat_where_sex = [item for sublist in nw_where_sex for item in sublist]

drugs = [response[13].split(",") for response in data]
nw_drugs = [[item.rstrip().lstrip() for item in response] for response in drugs]
flat_drugs = [item for sublist in nw_drugs for item in sublist]

fb_friends = [response[26+17] for response in data]


# increment counter in dictionary keyed by target1 if both target1 and target2 are
# present
def count_if(data1, data2):

    flat_data1 = [item for sublist in data1 for item in sublist]
    flat_data2 = [item for sublist in data2 for item in sublist]
    
    freq_matrix = {target:{target1:0 for target1 in flat_data2} for target in flat_data1}

    norm_mat = {target:0 for target in flat_data1}

    for response in range(len(data1)):
        for option in data1[response]:
            for corr_option in data2[response]:
                freq_matrix[option][corr_option] += 1
                norm_mat[option] += 1
    return freq_matrix, norm_mat


freqs, norm = count_if(nw_drugs, nw_where_sex)
print(norm)

hist = {}

for drug in freqs.keys():
    drug_on_campus = 0
    drug_on_campus += freqs[drug]['The steam tunnels'] + freqs[drug]['Catwalks'] + freqs[drug]['Totally banged in Pi Phi'] + freqs[drug]['The steam tunnels'] + freqs[drug]['dorm room floor']  + freqs[drug]['The Library'] + freqs[drug]['Field Session'] + freqs[drug]['kafadar'] + freqs[drug]['and Brown Building West bathroom'] + freqs[drug]['Music Practice Room in Maple'] + freqs[drug]['my office on campus'] + freqs[drug]['Kaf'] + freqs[drug]['The Ace-Hi Tavern'] + freqs[drug]['A fraternity house'] + freqs[drug]['every social lounge in maple'] + freqs[drug]['In Edgar Mine'] + freqs[drug]['Kafadar'] + freqs[drug]['A fraternity house'] + freqs[drug]['A campus building'] + freqs[drug]['A sorority house'] 

    if drug_on_campus > 8:
        hist[drug] = drug_on_campus


plt.bar(range(len(hist)), hist.values(), align='center')
plt.xticks(range(len(hist)), list(hist.keys()), rotation='vertical')

plt.show()
#n, bins, patches = plt.hist(        


