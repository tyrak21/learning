s = "4епыапфц4ей3рпйшоизщи!2342#%!#%1353%!#%3%"
string = ([s[i:i + 2] for i in range(0, len(s), 2)])

def zadachka(string):
    listof = []
    for i in string:
        if str(len(i)) == '2':
            listof.append(i)
        else:
            listof.append(i + '_')
    print(listof)
zadachka(string)


