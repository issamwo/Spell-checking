import re
from collections import Counter

from .config import PATH_KNOWLEDGE


def text_to_words(text : str)-> list: 
    """Convert text to list of words - with no special caracters

    Args:
        text (str): text

    Returns:
        str: list of words
    """
    return re.findall(r'\w+', text.lower())

KNOWLEDGE = Counter(text_to_words(open(PATH_KNOWLEDGE).read()))



class KnowledgeCorrection():
    """Correct spelling based on a knowledge base
    """
    def __init__(self) -> None:
        pass
    
    def P(self, word: str, N: int = sum(KNOWLEDGE.values()))-> int:
        """Get proba of occurrence of (word)

        Args:
            word (int): word
            N (int): sum of all words of the knowledge base

        Returns:
            proba (int): proba of the word in the Knowlegde-base
        """
        return KNOWLEDGE[word] / N

    def candidates(self, word): 
        "Generate possible spelling corrections for word."
        return (self.known([word]) or self.known(self.edits1(word)) or\
                 self.known(self.edits2(word)) or [word])

    def known(self, words): 
        "The subset of `words` that appear in the dictionary of WORDS."
        return set(w for w in words if w in KNOWLEDGE)

    def edits1(self, word):
        "All edits that are one edit away from `word`."
        letters    = 'abcdefghijklmnopqrstuvwxyz'
        splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
        deletes    = [L + R[1:]               for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
        replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
        inserts    = [L + c + R               for L, R in splits for c in letters]
        return set(deletes + transposes + replaces + inserts)

    def edits2(self, word): 
        "All edits that are two edits away from `word`."
        return (e2 for e1 in self.edits1(word) for e2 in self.edits1(e1))
    


spell_correct = KnowledgeCorrection()


def correct_knowledge_spell(text: str)-> str:
    """Correct spelling based 

    Args:
        text (str): _description_

    Returns:
        str: _description_
    """
    list_words = text_to_words(text)
    list_words =[max(spell_correct.candidates(word), key=spell_correct.P) for word in list_words]
    return " ".join(list_words)

