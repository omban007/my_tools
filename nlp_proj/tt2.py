import re


def pos_tagging(sentence):
    # Define POS tags
    pos_tags = {
        'NN': 'Noun',
        'NNS': 'Noun',
        'NNP': 'Proper Noun',
        'NNPS': 'Proper Noun',
        'VB': 'Verb',
        'VBD': 'Verb',
        'VBG': 'Verb',
        'VBN': 'Verb',
        'VBP': 'Verb',
        'VBZ': 'Verb',
        'JJ': 'Adjective',
        'JJR': 'Adjective',
        'JJS': 'Adjective',
        'RB': 'Adverb',
        'RBR': 'Adverb',
        'RBS': 'Adverb',
        'PRP': 'Pronoun',
        'PRP$': 'Pronoun',
        'WP': 'Pronoun',
        'WP$': 'Pronoun',
        'DT': 'Determiner',
        'IN': 'Preposition',
        'CC': 'Conjunction',
        'CD': 'Cardinal Number',
        'MD': 'Modal',
        'TO': 'To',
        'EX': 'Existential There',
        'FW': 'Foreign Word',
        'UH': 'Interjection',
        'RP': 'Particle',
        'SYM': 'Symbol',
        'WDT': 'Wh-Determiner',
        'WRB': 'Wh-Adverb',
        'LS': 'List Item Marker',
        'PDT': 'Predeterminer',
        'POS': 'Possessive Ending'
    }

    # Regular expressions for matching patterns
    patterns = [
        (r'\b[A-Z][a-z]+\b', 'NNP'),  # Proper nouns
        (r'\b[a-z]+\b', 'NN'),  # Nouns
        (r'\b[A-Z]+\b', 'NNP'),  # Acronyms
        (r'\b[0-9]+\b', 'CD'),  # Cardinal numbers
        (r'\b[a-z]+ly\b', 'RB'),  # Adverbs ending in 'ly'
        (r'\b[a-z]+ing\b', 'VBG'),  # Gerunds/Verbs ending in 'ing'
        (r'\b[a-z]+ed\b', 'VBD'),  # Past tense verbs ending in 'ed'
        (r'\b[A-Z][a-z]+ed\b', 'VBD'),  # Past tense proper nouns ending in 'ed'
        (r'\b[A-Z][a-z]+\b', 'NNP'),  # Proper nouns (fallback)
        (r'\b[a-z]+\b', 'NN')  # Nouns (fallback)
    ]

    # Tokenize the sentence into words
    words = re.findall(r'\b\w+\b', sentence)

    # Perform POS tagging
    tagged_words = []
    for word in words:
        for pattern, tag in patterns:
            if re.match(pattern, word):
                tagged_words.append((word, pos_tags.get(tag, 'Unknown')))
                break
        else:
            tagged_words.append((word, 'Unknown'))

    return tagged_words


# Example usage
sentence = "I love coding in Python."
tagged_words = pos_tagging(sentence)
print(tagged_words)
