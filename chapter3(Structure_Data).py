          ##### Dictionary #####

# person3 = { 'Name': 'Ford Prefect',
#             'Gender': 'Male',
#             'Occupation': 'Researcher',
#             'Home planet': 'Betelgeuse Seven' }
# person3['Age'] = 33
# print(person3['Age'])


# found = {'a': '0', 'e': '2', 'i': '0', 'o': '0', 'u': '0' }
# for k, v in sorted(found.items()):
#     print(k, 'was found', v, 'time(s).')


# vowels = ['a', 'e', 'i', 'o', 'u']
# word = input("Provide a word to search for vowels: ")
# found = {}
# # found["a"] = 0
# # found["e"] = 0
# # found["i"] = 0
# # found["o"] = 0
# # found["u"] = 0
# for letter in word:
#     if letter in vowels:
#         found[letter] += 1
# for k, v in sorted(found.items()):
#     print(k, 'was found', v, 'item(s).')


# fruits = {}
# fruits['apples'] = 10
#
# if 'pears' not in fruits:
#     fruits['pears'] = 0
# else:
#     fruits['bansnas'] = 1
# print(fruits)


vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")
found = {}
for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1
for k, v in sorted(found.items()):
    print(k, 'was found', v, 'item(s).')


##### sets and tuples (Множества и кортежи)#####
