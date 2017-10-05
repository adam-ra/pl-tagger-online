# closed grammatical classes, i.e. new words are unlikely to be introduced to the language
# that should be tagged with any of these
# assuming NKJP tagset
from pltaggeronline import ws, ccl, struct

closed_classes = set('ppron12 ppron3 siebie bedzie aglt winien prep conj comp qub burk interp'.split())


def word_lemmas_in_text(text, skip_classes=None):
    """Send text for tagging and read lemmas only. Return a list of lemmas."""
    result_xml = ws.process(text)
    lemmas = []
    for tok in ccl.tokens_from_ccl(result_xml):
        if not skip_classes or struct.get_wordclass(tok.tag) not in skip_classes:
            lemmas.append(tok.lemma)
    return lemmas


def token_structure(text):
    """Tag the given text and return a simple JSON-able structure."""
    result_xml = ws.process(text)
    tokens = []
    for tok in ccl.tokens_from_ccl(result_xml):
        tokens.append(tok.to_structure())
    return tokens
