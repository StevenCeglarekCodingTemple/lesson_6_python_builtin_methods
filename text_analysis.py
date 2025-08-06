# Sample text for analysis
text = """
Python is a powerful programming language.

It is easy to learn and easy to use.

Python is great for beginners and experts alike.
"""

# Basic text analysis
lines = text.strip().split('\n')
print(f"Number of lines: {len(lines)}")

# Removes empty lines
non_empty_lines = [line for line in lines if line.strip()]
print(f"Non-empty lines: {len(non_empty_lines)}")

# Word frequency analysis
all_words = []
for line in non_empty_lines:
    words = line.lower().split()
    # Clean each word
    clean_words = []
    for word in words:
        clean_word = word.strip('.,!?').lower()
        if clean_word:
            clean_words.append(clean_word)
    all_words.extend(clean_words)
    
print(f"Total words: {len(all_words)}")

# Count word frequencies
word_count = {}
for word in all_words:
    word_count[word] = word_count.get(word, 0) + 1
    
print(word_count)

    