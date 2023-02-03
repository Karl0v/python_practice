text = """До шкільного подвір’я в’їхала вантажівка. У кузові лежали саджанці фруктових дерев.
Веселою юрбою учні кинулися до машини і розвантажили її. Всі саджанці вони перенесли до садка.
Там уже були викопані глибокі ями. Школярі посадили в них саджанці. Минуть роки і сад заквітне."""

delim = ' ,.()[]{}-_=+<>/?\|*&^%$#@!;:"'
text_dict = {}

for i in text.split():
    i_clean = i.strip(delim).lower()
    if i_clean in text_dict:
        text_dict[i_clean] += 1
    else:
        text_dict[i_clean] = 1

text_dict_lst = list(text_dict.items())
text_dict_lst.sort(key=lambda x: x[1])
print(text_dict_lst[:4])
text_dict_lst.sort(key=lambda x: x[1], reverse=True)
print(text_dict_lst[:4])
print(text_dict_lst)