def edit_distance(string1, string2):
    if len(string1) > len(string2):
        distance = len(string1) - len(string2)
        string1[:distance]
    
    elif len(string2) > len(string1):
        distance = len(string2) - len(string1)
        string2[:distance]
    
    else:
        distance = 0
    
    for i in range(len(string1)-1):
        if string1[i] != string2[i]:
            distance += 1

    return distance

print(edit_distance("treasurer","prestige"))
