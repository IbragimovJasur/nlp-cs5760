
# 1. Tokenize a paragraph
paragraph = "Kecha u maktabga bormadi, chunki sog'lig'i yomonlashgan edi. O'qituvchisi: 'Tezroq sog'ayib ket!' deb aytdi. Bu Toshkentdagi eng yaxshi shifoxonadir."

# Do naïve space-based tokenization
space_based = [
    'Kecha', 'u', 'maktabga', 'bormadi,', 'chunki', "sog'lig'i", 'yomonlashgan', 'edi.', 
    "O'qituvchisi:", 'Tezroq', "sog'ayib", 'ket!', 'deb', 'aytdi.', 'Bu', 'Toshkentdagi', 'eng', 'yaxshi', 'shifoxonadir.'
]

# Manually corrected the tokens by handling punctuation, suffixes, and clitics
manually_corrected = [
    'Kecha', 'u', 'maktab', 'ga', 'borma', 'di', ',', 'chunki', "sog'lig'i", 'yomonlash', 'gan', 'edi', '.', 
    "O'qituv", 'chi', 'si', ':', 'Tezroq', "sog'ayib", 'ket', '!', 'deb', 'ayt', 'di', '.', 'Bu', 'Toshkent', 'dagi', 
    'eng', 'yaxshi', 'shifoxona', 'dir', '.'
]



# 2. Compare with a Tool
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt_tab')
nltk_tokens = word_tokenize(paragraph)
ouput = [
    'Kecha', 'u', 'maktabga', 'bormadi', ',', 'chunki', "sog'lig", "'", 'i', 'yomonlashgan', 'edi', '.', 
    "O'qituvchisi", ':', "'Tezroq", "sog'ayib", 'ket', '!', "'", 'deb', 'aytdi', '.', 'Bu', 'Toshkentdagi', 
    'eng', 'yaxshi', 'shifoxonadir', '.'
]

# Almost every complex word in the paragraph differs. Specifically:
    # Apostrophe-heavy words: 
        # sog'lig'i vs. sog'lig, ', i
    # Agglutinative forms: 
        # maktabga, bormadi, yomonlashgan, Toshkentdagi, shifoxonadir
    # Punctuation/Quotes: 
        # 'Tezroq (NLTK kept the quote attached)

# The reason why tokens differ is I guess because:
    # NLTK's word_tokenize is optimized for English. That's why it cannot detect commmon suffixes ('ga', 'gi', 'gan')
    # Also, it sees apostrophe and assumes it is a possessive contraction (like user's), breaking the word incorrectly.



# 3. Multiword Expressions (MWEs)
# Sog'ayib ketmoq (To get well / recover)
# Why: If split, the word "ketmoq" (to go) loses its grammatical function as an auxiliary verb indicating the completion or transition of an action. It is a compound verb where the two words represent a single semantic concept.

# Qo'shma Shtatlar (United States)
# Why: This is a proper noun referring to a specific sovereign entity. Treating "Qo'shma" (Joined/United) and "Shtatlar" (States) as separate tokens would lose the specific geopolitical identity, which is essential for accurate entity recognition and translation.

# O'rta Osiyo (Central Asia)
# Why: As a specific geographical proper name, it represents a single entity. In an NLP pipeline, identifying this as a single token prevents the model from interpreting "O'rta" (Middle) as a general adjective rather than part of a fixed location name.



# 4. Reflection
# The hardest part: Dealing with the apostrophe and suffixes.
# In Uzbek, the apostrophe is actually a letter (like in o' or g'), not just a punctuation mark. 
# If you split it, you aren't just separating words; you are breaking a single letter in half.

# Comparison with English: 
# In English, splitting a word like don't into do and n't makes sense because they are two separate ideas combined. 
# In Uzbek, splitting sog'lig'i is like breaking the word apple into ap and ple. It destroys the base word and makes it meaningless.

# Difficulty: Punctuation and morphology make Uzbek much harder because a single "word" can be a whole sentence. 
# While English is mostly about finding spaces, Uzbek requires you to "peel" off layers like -ga (to) or -dir (is).
# MWEs like O'rta Osiyo (Central Asia) add more trouble because they look like two words but represent one single place.
