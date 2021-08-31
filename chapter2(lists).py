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


# first = [1, 2, 3, 4, 5]
# second = first
# second.append(6)
# third = second.copy()
# third.append(12)
# print(first)
# print(second)
# print(third)

#Диапазон [начало:конец:шаг] индексов
# saying = "Don't Panic!"
# letters = list(saying)
# print(letters[0:10:3])
# print(letters[3:])
# print(letters[::2])


book = "The Hitchhiker's Guide to the Galaxy"
booklist = list(book)
print(booklist)
print(booklist[0:3])
print(''.join(booklist[0:3]))    # покажет символы с индекса 0 по индекс 3
print(''.join(booklist[-6:]))    # покажет символы до конца наченая с символа с индексом -6
print(''.join(booklist[4:16:1])) # символы с индекса 4 по индекс 16 с шагом 1 (тоесть каждый символ диапозона, без шага получится тот-же результат)
backwards = booklist[::-1]       #
print(''.join(backwards))        # покажет все символы в обратном порядке


# phrase = "Don't panic!"
# plist = list(phrase)
# #### From My version ####
# # x =[]
# # x = (plist[1:3])
# # x.extend(plist[5])
# # x.extend(plist[4])
# # x.extend(plist[7:5:-1])
# # new_phrase = ''.join(x)
# #### end ####
#
# #### From book version ####
# new_phrase = ''.join(plist[1:3])
# new_phrase = new_phrase + ''.join([plist[5],plist[4], plist[7], plist[6]])
# #### end ####
# print(plist)
# print(new_phrase)



# paranoid_android = "Marvin"
# letters = list(paranoid_android)
# for i in letters:
#     print('\t', i)


# paranoid_android = "Marvin, the Paranoid Android"
# letters = list(paranoid_android)
# for i in letters[:6]:
#     print('\t', i)
# print()
# for i in letters[-7:]:
#     print('\t'*2, i)
# print()
# for i in letters[12:20]:
#     print('\t'*3, i)


