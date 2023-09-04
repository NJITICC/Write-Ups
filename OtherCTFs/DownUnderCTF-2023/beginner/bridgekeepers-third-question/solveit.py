#Remove comment to test
#answer = input("Give me 13 characters: ")

a  = ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "b", "a", "a", "a", "a", "a", "a", "a", "a"]
b  = ["b", "b", "b", "b", "c", "b", "a", "a", "b", "b", "a", "b", "a", "b", "a", "a", "b", "a", "b", "a", "a", "b", "a", "b", "a", "b"]
c  = ["a", "d", "b", "c", "a", "a", "a", "c", "b", "b", "b", "a", "b", "c", "a", "b", "b", "a", "c", "c", "b", "a", "b", "a", "c", "c"]
d  = ["c", "d", "c", "c", "e", "d", "d", "c", "c", "c", "c", "b", "c", "c", "d", "c", "b", "d", "a", "d", "c", "c", "c", "a", "d", "c"]
e  = ["a", "e", "f", "c", "d", "e", "a", "e", "c", "d", "c", "c", "c", "d", "a", "e", "b", "b", "a", "d", "c", "e", "b", "b", "a", "a"]
f  = ["f", "d", "g", "e", "d", "e", "d", "c", "b", "f", "f", "f", "a", "f", "e", "f", "f", "d", "a", "b", "b", "b", "f", "f", "a", "f"]
g  = ["h", "a", "c", "c", "g", "c", "b", "a", "g", "e", "e", "c", "g", "e", "g", "g", "b", "d", "b", "b", "c", "c", "d", "e", "b", "f"]
h  = ["c", "d", "a", "e", "c", "b", "f", "c", "a", "e", "a", "b", "a", "g", "e", "i", "g", "e", "g", "h", "d", "b", "a", "e", "c", "b"]
i  = ["h", "a", "d", "b", "d", "c", "d", "b", "f", "a", "b", "b", "i", "d", "g", "a", "a", "a", "h", "i", "j", "c", "e", "f", "d", "d"]
j  = ["b", "f", "c", "f", "i", "c", "b", "b", "c", "j", "i", "e", "e", "j", "g", "j", "c", "k", "c", "i", "h", "g", "g", "g", "a", "d"]
k  = ["i", "k", "c", "h", "h", "j", "c", "e", "a", "f", "f", "h", "e", "g", "c", "l", "c", "a", "e", "f", "d", "c", "f", "f", "a", "h"]
l  = ["j", "k", "j", "a", "a", "i", "i", "c", "d", "c", "a", "m", "a", "g", "f", "j", "j", "k", "d", "g", "l", "f", "i", "b", "f", "l"]
m  = ["c", "c", "e", "g", "n", "a", "g", "k", "m", "a", "h", "h", "l", "d", "d", "g", "b", "h", "d", "h", "e", "l", "k", "h", "k", "f"]
n = "blue"

nav = a


allArrays = [a, b, c, d, e, f, g, h, i, j, k, l, m]

order = []

def getOrder(allArrays,order):
    highest = 0;
    word = "DUCTF{"
    for arr in allArrays:
        for c in arr:

            val = (ord(c) - 97)

            #print(f"val is {val}")
            if val > highest:
                highest = val
                position = arr.index(c)
                #print(f"New highest = {highest} at {position}")     
                order.append(position)
                realChar = chr(position+97)
                word = word + realChar
                break
    word = word + "}"
    return print(order, word)

getOrder(allArrays,order)




