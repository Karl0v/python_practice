class Word:

    DELIM = """,.()[]{}-_=+<>"—'/?\\|*&^'%$#@!“;:"""

    def __init__(self, raw):
        self.raw = raw
        self.clean = self.perform_cleaning()
        self.len = len(self.clean)

    def __str__(self):
        return self.clean

    def __repr__(self):
        return f'{self.clean} : {self.len}'

    def perform_cleaning(self):
        return self.raw.strip(Word.DELIM).lower()



if __name__ == "__main__":
    text = """До шкільного подвір’я в’їхала вантажівка. У кузові лежали саджанці фруктових дерев.
Веселою юрбою учні кинулися до машини і розвантажили її. Всі саджанці вони перенесли до садка.
Там уже були викопані глибокі ями. Школярі посадили в них саджанці. Минуть роки і сад заквітне."""
    text_dict = dict()

    for i in text.split():
        w = Word(i)
        text_dict[w.clean] = w
        words = list(text_dict.values())

    longest_top5 = sorted(words, key=lambda x: x.len, reverse=True)[:4]
    shortest_top5 = sorted(words, key=lambda x: x.len, reverse=False)[:4]
    print(longest_top5)
    print(shortest_top5)


