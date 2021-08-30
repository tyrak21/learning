##### LISTS #####

# vowels = ['a', 'e', 'i', 'o', 'u']
# word = "Milliways"
# for letter in word:
#     if letter in vowels:
#         print(letter)


# found = []
# found.append('a')
# found.append('e')
# found.append('tra-ta-ta')
# if 'u' not in found:
#     found.append('u')
#     print(found)
#     print(len(found))


# vowels = ['a', 'e', 'i', 'o', 'u']
# word = input("Provide a word to search for wovels: ")
# found = []
# for letter in word:
#     if letter in vowels:
#         if letter not in found:
#             found.append(letter)
# for vowel in found:
#     print(vowel)


# phrase = "Don't panic!"
# plist = list(phrase)
#
# print(phrase)
# print(plist)
#
# for each in plist:
#     if each not in "on tap":
#         plist.remove(each)
# plist.pop(7)
# plist.pop(6)
# ext = (plist.pop(3))
# plist.insert(2, ext )
# for letter in plist:
#     if letter == "a":
#         need = plist.pop()
#         plist.insert(4, need )
#
# new_phrase = ''.join(plist)
# print(plist)
# print(new_phrase)

first = [1, 2, 3, 4, 5]
second = first
second.append(6)
third = second.copy()
third.append(12)
print(first)
print(second)
print(third)

