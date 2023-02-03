text = """До шкільного подвір’я в’їхала вантажівка. У кузові лежали саджанці фруктових дерев.
Веселою юрбою учні кинулися до машини і розвантажили її. Всі саджанці вони перенесли до садка.
Там уже були викопані глибокі ями. Школярі посадили в них саджанці. Минуть роки і сад заквітне."""
delim = """,.()[]{}-_=+<>"—'/?\|*&^'%$#@!“;:"""
text_dict = {}


for i in text.split():
    i_clean = i.strip(delim).lower()
    text_dict[i_clean] = len(i_clean)



text_dict_lst = list(text_dict.items())
longest_top5 = sorted(text_dict_lst, key=lambda x: x[1], reverse=True)[:4]
shortest_top5 = sorted(text_dict_lst, key=lambda x: x[1], reverse=False)[:4]
print(longest_top5)
print(shortest_top5)



