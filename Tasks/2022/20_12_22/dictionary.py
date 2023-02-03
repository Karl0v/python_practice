#text = """The Réunion swamphen (Porphyrio caerulescens) is a hypothetical extinct species of rail that was endemic to the Mascarene island of Réunion. While only known from accounts by visitors from the 17th and 18th centuries, it was scientifically named in 1848 based on a 1674 account by Sieur Dubois. The Réunion swamphen was described as entirely blue in plumage with a red beak and legs; the size of a Réunion ibis, which could mean 65 to 70 cm (26 to 28 in) in length; and possibly similar to the takahē. While easily hunted, it was a fast runner and able to fly. It may have fed on plant matter and invertebrates, and was said to nest among grasses and aquatic ferns. It was only found on the Plaine des Cafres plateau, to which it may have retreated during the latter part of its existence, whereas other swamphens inhabit lowland swamps. While the last unequivocal account is from 1730, the bird may have survived until 1763. Overhunting and the introduction of cats probably drove it to extinction."""
text = """До шкільного подвір’я в’їхала вантажівка. У кузові лежали саджанці фруктових дерев.
Веселою юрбою учні кинулися до машини і розвантажили її. Всі саджанці вони перенесли до садка.
Там уже були викопані глибокі ями. Школярі посадили в них саджанці. Минуть роки і сад заквітне."""
delim = ',.()[]{}-_=+<>/?\|*&^%$#@!;:"'
text_dict = {}

for i in text.split():
    i_clean = i.strip(delim).lower()
    if i_clean in text_dict:
        text_dict[i_clean] += 1
    else:
        text_dict[i_clean] = 1


text_dict_lst = list(text_dict.items())
print(sorted(text_dict_lst, key=lambda x: x[1], reverse=True)[:4])
print(sorted(text_dict_lst, key=lambda x: x[1])[:4])

while True:
    word = input('Interested word? -> ').lower()
    print(text_dict.get(word,0))
    if word == 'no':
        break

text_dict_lst = list(text_dict.items())
print(sorted(text_dict_lst, key=lambda x: x[1], reverse=True)[:4])
print(sorted(text_dict_lst, key=lambda x: x[1])[:4])

#print(text_dict_lst[0], type(text_dict_lst[0]))





d = {
    'hunted': 1,
    'was': 1,
    'while': 1
}

if 'to' in d:
    d['to'] += 1
else:
    d['to'] = 1
d ['was'] += 1


