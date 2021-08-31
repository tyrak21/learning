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


# vowels = ['a', 'e', 'i', 'o', 'u']
# word = input("Provide a word to search for vowels: ")
# found = {}
# for letter in word:
#     if letter in vowels:
#         found.setdefault(letter, 0)
#         found[letter] += 1
# for k, v in sorted(found.items()):
#     print(k, 'was found', v, 'item(s).')


##### sets and tuples (Множества и кортежи)#####


# vowels = {'a', 'e', 'e', 'i', 'o', 'u', 'u'}
# vowels2 = set('aeeiouu')
# print(vowels, vowels2)

# vowels = set('aeiou')
# word = 'hello'
# u = vowels.union(set(word)) # объединяет строку и множество.
# u_list = sorted(list(u)) # отсортированный список из множетсва.
# d = vowels.difference(set(word)) # сравнивает множество vowels и множество word и взвращает множества которые содержатся в vowels и которых нет в word.
# i = vowels.intersection(set(word)) # метод возвращает те множества которые есть в множестве word и которые присутствуют в множестве vowel.
#
# print(u)
# print(vowels)
# print(u_list)
# print(d)
# print(i)


# # vowels = {'a', 'e', 'i', 'o', 'u'} #or
# vowels = set('aeiou')
# word = input("Provide a word to search for vowels: ")
# found = vowels.intersection(set(word))
# for vowel in found:
#     print(vowel)


# vowels = ['a', 'e', 'i', 'o', 'u'] #list
# vowels2 = ('a', 'e', 'i', 'o', 'u') #tuple
# print(vowels)
# print(vowels2)
# print(type(vowels2))


# import pprint
# people = {}
# people['Ford'] = {'Name': 'Ford Prefect',
#                   'Gender': 'Male',
#                   'Occupation': 'Researcher',
#                   'Home planet': 'Betelgeuse Seven'}
# people['Arthur'] = {'Name': 'Arthur Dent',
#                   'Gender': 'Male',
#                   'Occupation': 'Sandwich-maker',
#                   'Home planet': 'Earth'}
# people['Trillian'] = {'Name': 'Tricia McMillan',
#                   'Gender': 'Female',
#                   'Occupation': 'Mathematician',
#                   'Home planet': 'Earth'}
# people['Robot'] = {'Name': 'Marvin',
#                   'Gender': 'Unknown',
#                   'Occupation': 'Paranoid Android',
#                   'Home planet': 'Unknown'}
# pprint.pprint(people)
# print(people['Trillian']['Occupation'])