

def search4vowels(word):
    """This is a comment in a functions"""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)

search4vowels()