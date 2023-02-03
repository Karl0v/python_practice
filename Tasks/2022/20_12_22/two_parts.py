d1 = {'unicorn': 'blue', 'bear': 'brown', 'dear': 1}
d2 = {'dear': 'beige', 'unicorn': 'pink'}
d2['woolf'] = 'gray'
d_dict = {**d2,**d1}

print(d_dict)

for key in d1:
    if key in d2:
        d_dict[key + '_copy'] = d2[key]
print(d_dict)

print(set(d1.keys()).intersection(set(d2.keys())))

