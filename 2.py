s = input()
letters_count_sheriff = {"s": 0, "h": 0, "e": 0, "r": 0, "i": 0, "f": 0}
letters_count_s = {}

for letter in "sheriff":
    letters_count_sheriff[letter] += 1

for letter in s:
    if letter in letters_count_s:
        letters_count_s[letter] += 1
    else:
        letters_count_s[letter] = 1

max_words = float('inf')

for letter, count in letters_count_sheriff.items():
    if letter in letters_count_s:
        max_words = min(max_words, letters_count_s[letter] // count)
    else:
        max_words = 0

print(max_words)
