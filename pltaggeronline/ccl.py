from xml.etree import ElementTree

from pltaggeronline import struct


def token_from_node(node):
    for lex in node.findall('lex'):
        orth = node.find('orth').text
        if lex.get('disamb') == '1':
            return struct.Token(orth=orth, lemma=lex.find('base').text, tag=lex.find('ctag').text)
    raise ValueError('Unexpected tok node')


def sentences_from_ccl(ccl_str):
    root_node = ElementTree.fromstring(ccl_str)
    sents = []
    for sent_node in root_node.iter('sentence'):
        sent = struct.Sentence()
        after_space = True
        for tok_node in sent_node.iter():
            if tok_node.tag == 'tok':
                tok = token_from_node(tok_node)
                tok.after_space = after_space
                sent.append_token(tok)
                after_space = True
            elif tok_node.tag == 'ns':
                after_space = False
        sents.append(sent)
    return sents


def tokens_from_ccl(ccl_str):
    toks = []
    for sent in sentences_from_ccl(ccl_str):
        for tok in sent.tokens:
            toks.append(tok)
    return toks
