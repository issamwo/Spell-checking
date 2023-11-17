# from spellchecker import SpellChecker


# def spell_checker(inputs: str):
#     """Check if spelling is known

#     Args:
#         inputs (str): text

#     Returns:
#         _type_: input corrected
#     """

#     spell = SpellChecker()
#     print("***************")

#     # Split the text into words
#     words = inputs.split()

#     # Find and correct misspelled words
#     corrected_text = []
#     for word in words:
#         # Check if the word is misspelled
#         if spell.unknown([word]):
#             print("**************")
#             print("unknown word = ", word)
#             # Get the most likely correction for the misspelled word
#             corrected_word = spell.correction(word)
#             if corrected_word==None:
#                 corrected_word= word
#             #print("correcte word = ", corrected_word)
#             corrected_text.append(corrected_word)
#         else:
#             corrected_text.append(word)
    
#     # Reconstruct the corrected text
#     corrected_text = " ".join(corrected_text)
#     return corrected_text

# print(spell_checker('zarlka'))

# # add txt file to 
# # if I just want to make sure some words are not flagged as misspelled
# # spell.word_frequency.load_words(['microsoft', 'apple', 'google'])
# import re
# from collections import Counter

# from utils.config import PATH_KNOWLEDGE

# def text_to_words(text : str)-> list: 
#     return re.findall(r'\w+', text.lower())

# KNOWLEDGE = (text_to_words(open(PATH_KNOWLEDGE).read()))

# print(len(list(KNOWLEDGE)))
