class Token(object):
    def __init__(self, orth, lemma, tag):
        self.orth = orth
        self.lemma = lemma
        self.tag = tag
        self.after_space = True

    def to_structure(self):
        return {
            'orth': self.orth,
            'lemma': self.lemma,
            'tag': self.tag,
            'after_space': self.after_space
        }


def token_from_line(line):
    line = line.strip()
    orth, lemma, tag = line.split('\t')
    return Token(orth, lemma, tag)


def get_wordclass(tag):
    return tag.split(':')[0]


class Sentence(object):
    def __init__(self):
        self.tokens = []

    def is_empty(self):
        return not self.tokens

    def append_token(self, tok):
        self.tokens.append(tok)

    def orths(self):
        return [tok.orth for tok in self.tokens]

    def lemmas(self):
        return [tok.lemma for tok in self.tokens]

    def tags(self):
        return [tok.tag for tok in self.tokens]

    def wordclasses(self):
        return [get_wordclass(tag) for tag in self.tags]
