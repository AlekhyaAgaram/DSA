class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        # Lengths must match first
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for c, w in zip(pattern, words):
            # Check char -> word mapping
            if c in char_to_word and char_to_word[c] != w:
                return False

            # Check word -> char mapping
            if w in word_to_char and word_to_char[w] != c:
                return False

            # Establish mapping
            char_to_word[c] = w
            word_to_char[w] = c

        return True