class Word_qty:

    DELIM = """,.()[]{}-_=+<>"—'/? \\|*&^'%$#@!“;:"""

    def __init__(self, raw):
        self.raw = raw
        self.clean = self.perform_cleaning()

    def __str__(self):
        return self.clean

    def __repr__(self):
        return self.clean

    def perform_cleaning(self):
        return self.raw.strip(Word_qty.DELIM).lower()


if __name__ == "__main__":
    text = """At least 28 people at have died in western New York State, most of them in Buffalo, as a monster winter storm continues to batter North America.

A state official said some people had been trapped in cars for more than two days during what was "probably" the worst storm of their lifetime.

Up to nine more inches (23cm) of snow are expected in parts of the state through Tuesday, meteorologists warn.

The storm stretching from Canada to the Mexican border has killed 56 people.

US President Joe Biden approved an emergency declaration allowing federal support for New York State. "My heart is with those who lost loved ones this holiday weekend," he tweeted.

The owner of a small family-run shop in East Buffalo, who didn't want to be named, said looters broke into his general store on Christmas Day.

"They took everything. People took toys, electronics and speakers," he said.

He estimated up to $50,000 (£41,000) worth of equipment was stolen. He said he called the police, "but they told me they were too busy rescuing the elderly"."""
    text_count = dict()
    for count in text.split():
        w = Word_qty(count)
        x = str(w)
        if x in text_count:
            text_count[x] += 1
        else:
            text_count[x] = 1

    print(text_count)
    sorted_text = list(text_count.items())
    print(sorted_text)
    sorted_text.sort(key=lambda x: x[1])
    print(sorted_text[:5])
    sorted_text.sort(key=lambda x: x[1], reverse=True)
    print(sorted_text[:5])
    """for i in text_count_lst:
        for k in text_count.keys():
            if text_count[k] == i
                sorted_text[k] = text_count[k]
                break"""


