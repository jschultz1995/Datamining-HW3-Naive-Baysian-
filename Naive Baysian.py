# -*- coding: utf-8 -*-
"""
Josh Schultz
Naive Baiysian
"""

def get_prob(val, entry, attrib_index, label_index,data_frame, num_labels):
    numer = 0.0
    denom = 0.0
    
    
    for line in data_frame:
        if(line[label_index] == val):
            denom += 1
        if(line[label_index] == val and line[attrib_index] == entry):
            numer += 1
    if(numer == 0.0):
        numer += 1
        denom += num_labels
    #print "Numer: ", numer, " Denom: ", denom , "\n"
    return (numer/denom)

def tot_prob(attrib, attrib_index, data_frame, num_labels):
    numer = 0.0
    denom = 0.0
    
    for entry in data_frame:
        if(entry[attrib_index] == attrib):
            numer += 1
    denom = len(data_frame)
    if(numer == 0.0):
        numer += 1
        denom += num_labels
    #print "Numer: ", numer, " Denom: ", denom , "Num/Den: ", numer/denom, "\n"
    return (numer/denom)

def get_label(test_tuple, attribs, data_frame, target_att):
    valFreq = {}
    label_index = attribs.index(target_att)
    attrib_index = 0
    num_labels = 0
    prob = 0.0
    value_for_prob_one = 1.0
    value_for_prob_two = 1.0
    
    for entry in data_frame:
        if(entry[label_index] in valFreq):
            valFreq[entry[label_index]] += 1.0
        else:
            valFreq[entry[label_index]] = 1.0
            
    for key in valFreq:
        num_labels += 1
    
    for val in valFreq:
        for entry in test_tuple:
            value_for_prob_one *= get_prob(val, entry, attrib_index, label_index, data_frame, num_labels)
            #print "Val2: ", value_for_prob_two, " * ", tot_prob(entry, attrib_index, data_frame, num_labels), "\n"
            value_for_prob_two *= tot_prob(entry, attrib_index, data_frame, num_labels)
            attrib_index += 1
        value_for_prob_one *= tot_prob(val, label_index, data_frame, num_labels)
        #print "Values before dividing: ", value_for_prob_one, " ", value_for_prob_two
        value_for_prob_one /=  value_for_prob_two
        #print "Val: ", val, " Prob: ", value_for_prob_one, "\n"
        if(prob < value_for_prob_one):
            prob = value_for_prob_one
            label = val
        value_for_prob_one = 1.0
        value_for_prob_two = 1.0
        attrib_index = 0
    return(label)
    
data_frame_game_full = [
        ["Is Home/Away?", "Is Opponent in AP Top 25 at Preseason?", "Media", "Win/Lose"],
        ["Home","Out","1-NBC", "Win"],
        ["Away","Out","4-ABC", "Win"],
        ["Home","In","1-NBC", "Win"],
        ["Home","Out","1-NBC", "Win"],
        ["Away","In","4-ABC", "Lose"],
        ["Home","Out","1-NBC", "Win"],
        ["Home","In","1-NBC", "Win"],
        ["Away","Out","4-ABC", "Win"],
        ["Away","Out","4-ABC", "Win"],
        ["Home","Out","1-NBC", "Win"],
        ["Away","Out","1-NBC", "Win"],
        ["Away","In","3-FOX", "Lose"],
        ["Away","Out","4-ABC", "Lose"],
        ["Home","Out","1-NBC", "Win"],
        ["Home","Out","1-NBC", "Lose"],
        ["Home","Out","1-NBC", "Lose"],
        ["Home","Out","2-ESPN", "Win"],
        ["Away","Out","4-ABC", "Lose"],
        ["Home","In","1-NBC", "Lose"],
        ["Home","Out","1-NBC", "Win"],
        ["Home","Out","5-CBS", "Lose"],
        ["Home","Out","1-NBC", "Win"],
        ["Home","In","1-NBC", "Lose"],
        ["Away","In","4-ABC", "Lose"],
        ]

data_frame_game_test = [
        ["Home","Out","1-NBC"],
        ["Home","In","1-NBC"],
        ["Away","Out","2-ESPN"],
        ["Away","Out","3-FOX"],
        ["Home","Out","1-NBC"],
        ["Away","Out","4-ABC"],
        ["Home","In","1-NBC"],
        ["Home","Out","1-NBC"],
        ["Home","Out","1-NBC"],
        ["Away","In","4-ABC"],
        ["Home","Out","1-NBC"],
        ["Away","In","4-ABC"],
        ]

print("Win/Lost Data Frame Predictions:\n")
attribs = data_frame_game_full[0]
data_frame_game_full.remove(attribs)

for entry in data_frame_game_test:
    print(get_label(entry, attribs, data_frame_game_full, "Win/Lose"))
    
#print(get_label(["Away","Out","2-ESPN"], attribs, data_frame_game_full, "Win/Lose"))