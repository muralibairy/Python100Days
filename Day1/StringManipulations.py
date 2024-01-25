# # using string translate - remove punctuations
# import string
# test_str = 'Gfg, is best: for ! Geeks ;'
# test_str = test_str.translate(str.maketrans('', '', string.punctuation))
# print(test_str)
#
# import string
# task_string = 'testing - is fun! unless you know coding!! :)'
# task_string.translate(str.maketrans('', '', string.punctuation))
# print(task_string)

# import string
# string_1 = 'practice - makes - man - perfect - yessssss!!!!'
# string_1 = string_1.translate(str.maketrans('', '', string.punctuation))
# print(string_1.strip())

# import string
# test_string = 'hey, this is awesome!!'
# test_string = test_string.translate(str.maketrans('', '', string.punctuation))
# print(test_string)

#remove punctuation marks using python loop
# test_string = 'yes, yes keep, doing!!!!'
# punc = "`~'[][*&())&$!@#_+)=]()/?.>^_-/%=+!,"
#
# for ele in test_string:
#     if ele in punc:
#         test_string = test_string.replace(ele, '')
#
# print(test_string)

#attempt2

# test_str = 'hey this is good, keep going bro!!'
# punc = ".,/<>?~`!@#$%^&*()_+-={}[]"
# for ele in test_str:
#     if ele in punc:
#         test_str = test_str.replace(ele, '')
# print(test_str)

#attempt3
# test_str = 'hey, awesome, need to need more buddy!!!!'
# punc = ",./<>?~`!@#$%^&*()_+-={}[]\|"
# for ele in test_str:
#     if ele in punc:
#         test_str = test_str.replace(ele, '')
# print(test_str)

# #attempt with translate
# import string
# test_str = "I'm removing all puncs, yes!!!!!"
# test_str = test_str.translate(str.maketrans('', '', string.punctuation))
# print(test_str)

# #using python loop
# test_str = 'yes, I like the way it is going!!!!'
# result = ""
# for char in test_str:
#     if char != "," and char != "!" and char != ".":
#         result += char
# print(result)


