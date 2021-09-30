#
# word = "fffffffoooo"
# def search4vowels(word):
#     """This is a comment in a functions"""
#     vowels = set('aeiou')
#     found = vowels.intersection(set(word))
#     for vowel in found:
#         print(vowel)
#
# search4vowels(word)



# word = 'fgha'
# def search4vowels(word):
#     """This is a comment in a functions"""
#     vowels = set('aeiou')
#     print(bool (vowels.intersection(set(word))))
#
# search4vowels(word)



# word = 'fgh'
# def search4vowels(word:str)->set:
#     """returns the vowels found in the specified word"""
#     vowels = set('aeiou')
#     print(bool (vowels.intersection(set(word))))
#
# search4vowels(word)


# phrase = 'fgh'
# def search4vowels(phrase:str)->set:
#     """returns the vowels found in the specified word"""
#     vowels = set('aeiou')
#     print(bool (vowels.intersection(set(phrase))))
#
# search4vowels(phrase)



# def search4letters(phrase:str, letters:str)->set:
#     """returns the vowels found in the specified word"""
#     return set(letters).intersection(set(phrase))
#
# print(search4letters('abcde', 'abdefg'))



def search4letters(phrase:str, letters:str='aeiou')->set:
    """returns the vowels found in the specified word"""
    return set(letters).intersection(set(phrase))

print(search4letters('abcde'))

