word_file = open('words_alpha_fr.txt', 'r')
good_word_file = open('good_words.txt', 'w+')
words_list = word_file.read().lower().split()
good_words = []

word_sum = 0
for word in words_list:
    for letter in word:
        word_sum += ord(letter)-96
    if word_sum == 100:
        good_words.append(word)
    word_sum = 0
        

for word in good_words:
    good_word_file.write(word + '\n') 

word_file.seek = 0
#-96
#code_point_A = ord('a')-96
#print(f"The Unicode code point of 'a' is: {code_point_A}")