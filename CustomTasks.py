
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


# def rps(p1, p2):
#      if p1 == p2:
#          win = 0
#      if p1 == 'scissors' and p2 == 'rock':
#          win = 2
#      if p1 == 'paper' and p2 == 'rock':
#          win = 1
#      if p1 == 'rock' and p2 == 'paper':
#          win = 2
#      if p1 == 'scissors' and p2 == 'paper':
#          win = 1
#      if p1 == 'paper' and p2 == 'scissor':
#          win = 2
#      if p1 == 'rock' and p2 == 'scissors':
#          win = 2
#      if win == 0:
#          return "Draw!"
#      if win == 1:
#          return "Player 1 won!"
#      if win == 2:
#          return "Player 2 won!"
# print(rps('rock', 'scissor'))

# def get_planet_name(id):
#     switch = {
#         1: "Mercury",
#         2: "Venus",
#         3: "Earth",
#         4: "Mars",
#         5: "Jupiter",
#         6: "Saturn",
#         7: "Uranus",
#         8: "Neptune",
#         }
#     return switch.get(id, "Planet index" )


# # return reverse string
# def solution(string):
#     return string[::-1]
#     pass


# def solution(s):
#     s = ([s[i:i + 2] for i in range(0, len(s), 2)])
#     listof = []
#     for i in s:
#         if str(len(i)) == '2':
#             listof.append(i)
#         else:
#             listof.append(i + '_')
#     return listof
#     pass


# def longest(a1, a2):
#     a3 = a1 + a2
#     a3.split()
#     n = []
#     for i in a3:
#         if i not in n:
#             n.append(i)
#     d = sorted(n)
#     s = ''.join(d)
#     print(s)
#
# longest('aretheyhere', 'yestheyarehere')   #aehrsty


# def make_readable(seconds):
#
#     sec = int(seconds)
#     hour = ( sec // 3600 )
#     if hour < 10:
#         #global h
#         h = '0' + str(hour)
#     elif hour > 10:
#         return hour
#     pre_minute = ( sec - hour * 3600)
#     minute = pre_minute // 60
#     if minute < 10:
#         #global m
#         m = '0' + str(minute)
#     elif minute > 10:
#         return minute
#     secunds = pre_minute - minute * 60
#     if secunds < 10:
#         #global s
#         s = '0' + str(secunds)
#     elif secunds > 10:
#         return secunds
#     #result = (h + ":" + m + ":" + s)
#     result = (str(h) + ":" + str(m) + ":" + str(s))
#     print(str(result))
#
#
# make_readable( '600' )


# def string_to_array(str):
#
#     return(str.split(sep = ' '))
#
# str = "I love arrays they are my favorite"
#
# string_to_array(str)


