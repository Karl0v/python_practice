text1 = 'Ми дуже довго ходили, десь (чотири) години, тому стомилися'
text2 = 'Він дуже сміявся, хоча причинини не було, тож я здивувася'
delimetr = ',','.','(',')','[',']','{','}','-','_','=','+','<','>','/','?','|','*','&','^','%','$','#','@','!',';',':','"'
delim = (',.()[]{}-_=+<>/?\|*&^%$#@!;:"')




# 1
for i in text1:
    a = i.lower().split()
#for i in a:
    #b = i.strip(delim)
#print(b)

# 2
for i in text1:
   a = i.lower().split()
'''for i in a:
    print(i.strip(delim))'''

# 3
for i in text1:
    a = i.lower().split().sort()
#print(a)



def longest(txt):
    a = str(txt).lower().split()
    b = max(a, key=len)
    return b

#print(longest(text1))
#print(longest(text2))


def swapping(text):
    x = text.split()
    x[0], x[-1] = x[-1], x[-0]
    return x


print(swapping(text1))
print(swapping(text2))


def a_z(text):
    x = text.lower().split()
    return sorted(x)


#print(a_z(text1))
#print(a_z(text2))


def even(text):
    x = text.split()
    z = len(x)
    for i in range(0,z,2):
        print(x[i])


#even(text1)
#even(text2)


