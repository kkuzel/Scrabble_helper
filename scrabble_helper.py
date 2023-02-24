# Scrabble helper

# This program allows you to see all the possible words that you can create from given letters (max length - 8) 
# with points for each word, according to official Scrabble letter values.

# Type all lowercase letters. 
# Start your input with uppercase letter to find only words, that start with this letter.
# Put last input letter in uppercase to find only words, that ends with this letter.

# For now this program only works with polish language, so it includes all polish letters, and does not include V, X and Q.

# creating dictionary with value for each letter

# file1 = open('punktacja.txt', 'r', encoding='utf-8')
# ptable = dict()
# ptable['*'] = 0
# for line in file1:
#     line = line.lower()
#     value = line[0]
#     after = line.find(': ')
#     clearline = line[(after+1):].split()
#     for letter in clearline:
#         ptable[letter] = int(value)


# dictionary with value for each letter and empty strings and lists for output
ptable = {'*': 0, 'a': 1, 'e': 1, 'i': 1, 'n': 1, 'o': 1, 'r': 1, 
's': 1, 'w': 1, 'z': 1, 'c': 2, 'd': 2, 'k': 2, 'l': 2, 'm': 2, 
'p': 2, 't': 2, 'y': 2, 'b': 3, 'g': 3, 'h': 3, 'j': 3, 'ł': 3, 
'u': 3, 'ą': 5, 'ę': 5, 'f': 5, 'ó': 5, 'ś': 5, 'ż': 5, 'ć': 6, 
'ń': 7, 'ź': 9}
all = ['', '', '', '', '', '', '', '']
dwuliterowe = '\nDWULITEROWE: \n'
trzyliterowe = '\nTRZYLITEROWE: \n'
czteroliterowe = '\nCZTEROLITEROWE: \n'
pięcioliterowe = '\nPIĘCIOLITEROWE: \n'
sześcioliterowe = '\nSZEŚCIOLITEROWE: \n'
siedmioliterowe = '\nSIEDMIOLITEROWE: \n'
ośmioliterowe = '\nOŚMIOLITEROWE: \n'
allprint = [ośmioliterowe, siedmioliterowe, sześcioliterowe, 
pięcioliterowe, czteroliterowe, trzyliterowe, dwuliterowe]


# function to sort by points
def sortuj(e):
    nawias1 = e.find('(')
    nawias2 = e.find(')')
    f = int(e[(nawias1+1):nawias2])
    return (f)

# opening file, input - insert up to 7 letters
file2 = open('slowniczek.txt', 'r', encoding='utf-8')
entry = input("\nPodaj litery: ")
hand = []
for en in entry:
    hand.append(en)

# matching words to input
for stripword in file2:
    
    # formatting input to list, creating variables
    rword = stripword.rstrip()
    word = []
    for rw in rword:
        word.append(rw)
    rhand = []
    rhand = rhand + hand
    x = 0
    found = ''
    points = 0
    used = ''
    lhand = []

    # first letter uppercase (if word have to start with particular letter)
    if rhand[0].isupper() == True:
        lhand = lhand + rhand
        lhand[0] = rhand[0].lower()
        if lhand[0] == word[0]:

            # matching processed word to input
            for letter1 in word:
                for letter2 in lhand:
                    if (letter1 == letter2) or (letter2 == '*'):
                        x = x + 1
                        used = used + letter2
                        lhand.remove(letter2)
                        break

            # if word is matched, count points and add to list
            if x == len(word):
                for y in used:
                    for x in ptable:
                        if y == x:
                            points = points + ptable[x]
                for y in word:
                    found = found + y
                length = len(word)-2
                all[length] = all[length] + found + ' (' + str(points) + '), '


    # last letter uppercase (if word have to end with particular letter)
    elif rhand[len(rhand)-1].isupper() == True:
        lhand = lhand + rhand
        lhand[len(rhand)-1] = rhand[len(rhand)-1].lower()
        if lhand[len(rhand)-1] == word[len(word)-1]:

            # matching processed word to input
            for letter1 in word:
                for letter2 in lhand:
                    if (letter1 == letter2) or (letter2 == '*'):
                        x = x + 1
                        used = used + letter2
                        lhand.remove(letter2)
                        break

            # if word is matched, count points and add to list
            if x == len(word):
                for y in used:
                    for x in ptable:
                        if y == x:
                            points = points + ptable[x]
                for y in word:
                    found = found + y
                length = len(word)-2
                all[length] = all[length] + found + ' (' + str(points) + '), '

        
    else:
        # matching processed word to all lowercase input
        for letter1 in word:
            for letter2 in rhand:
                if (letter1 == letter2) or (letter2 == '*'):
                    x = x + 1
                    used = used + letter2
                    rhand.remove(letter2)
                    break

        # if word is matched, count points and add to list
        if x == len(word):
            for y in used:
                for x in ptable:
                    if y == x:
                        points = points + ptable[x]
            for y in word:
                found = found + y
            length = len(word)-2
            all[length] = all[length] + found + ' (' + str(points) + '), '

# sorting word values and creating output
for z in all:
    if len(z) > 0:
        z = z[:-2]
        zsplit = z.split(', ')
        zsplit.sort(reverse = True, key=sortuj)
        spacja = zsplit[0].find(' ')
        licznik = zsplit[0]
        dlugosc = len(licznik[:spacja])
        strsplit = ''
        for a in zsplit:
            strsplit = strsplit + a + ', '
        allprint[abs(dlugosc-8)] = allprint[abs(dlugosc-8)] + strsplit
for b in allprint:
    if len(b) > 20:
        b = b[:-2]
        print(b)
