
# match = "gjghdfgfrd".lower()
# output = []
# for i in str(match):
#     removed = match.replace(i,"", 1)
#     if i in removed:
#         output.append('(')
#     else:
#         output.append(')')
# full = ''.join(output)
# print(full)


# s = "4епыапфц4ей3рпйшоизщи!2342#%!#%1353%!#%3%"
# string = ([s[i:i + 2] for i in range(0, len(s), 2)])
#
# def zadachka(string):
#     listof = []
#     for i in string:
#         if str(len(i)) == '2':
#             listof.append(i)
#         else:
#             listof.append(i + '_')
#     print(listof)
# zadachka(string)

# def multiply(a, b):
#     result = a * b
#     return result
# print(multiply(4, 5))


# def string_to_array(s):
#     array = s.split(' ')
#     return array
# print(string_to_array(""))


def rps(p1, p2):
     if p1 == p2:
         win = 0
     if p1 == 'scissors' and p2 == 'rock':
         win = 2
     if p1 == 'paper' and p2 == 'rock':
         win = 1
     if p1 == 'rock' and p2 == 'paper':
         win = 2
     if p1 == 'scissors' and p2 == 'paper':
         win = 1
     if p1 == 'paper' and p2 == 'scissor':
         win = 2
     if p1 == 'rock' and p2 == 'scissors':
         win = 2
     if win == 0:
         return "Draw!"
     if win == 1:
         return "Player 1 won!"
     if win == 2:
         return "Player 2 won!"
print(rps('rock', 'scissor'))

