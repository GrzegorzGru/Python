# For the sentence "Lorem ipsum...":
#
# 1. Write it alternating lowercase and uppercase letters: "lOrEm iPsUm..."
# 2. Write it alternating words with lowercase and uppercase letters: "LOREM ipsum EST..."
# 3. Write it in uppercase, except for words that start with a letter that appears only once.
# 4. Write it by removing all vowels.

# 1.
sign_count = 0
sentence = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
new_sentence = ''
letter = ''
for sign in sentence:
    sign_count += 1
sign_range = range(0, sign_count)
for i in sign_range:
    if i % 2 == 0:
        letter = sentence[i].lower()
    else:
        letter = sentence[i].upper()
    new_sentence += letter
print(new_sentence)

# 2.
sentence_list = sentence.split(' ')
new_sentence = ''
word = ''
sentence_count = len(sentence_list)
for j in range(0, sentence_count):
    if j % 2 ==0:
        word = (sentence_list[j]).upper()
        new_sentence += word + ' '
    else:
        word = sentence_list[j].lower()
        new_sentence += word + ' '
print(new_sentence)

# 3.
first_letters = []
new_sentence = ''
word = ''
letter = ''
sentence_list = sentence.lower().split(' ')
lower_word_list = []
# List of first letters.
for word in sentence_list:
    first_letters += word[0]
# Count how many times given letter is as first in every word and create list
for letter in first_letters:
    counter = first_letters.count(letter)
    if counter == 1:
        lower_word_list += letter
# Create new sentence
for word in sentence_list:
    if word[0] in lower_word_list:
        word = word.lower()
        new_sentence += word + ' '
    else:
        word = word.upper()
        new_sentence += word + ' '
print(new_sentence)

# 4.
new_sentence = ''
vowels = ['a', 'i', 'o', 'u', 'y', 'e']
for vowel in vowels:
    sentence = sentence.replace(vowel, '')
print(sentence)