#ecret = 'pantofel'
#haslo = 'tralala'

#print "Secret -> "+ secret
#print "haslo -> "+ haslo

#for i in range (1, len(haslo) -1):
print('podaj haslo: ')
haslo = input()

gwiazdki = (len(haslo) - 2) * "*"



if len(haslo) == 0:
    print ('nie podano hasla')
elif len(haslo) < 3:
    print ('za krotkie haslo')
else:
    secret = haslo [0] + gwiazdki + haslo[-1]
    print(secret)


z = ''
for i in range(0, len(haslo)):
    if i in (1, len(haslo)-2):
        z = z + "*"
    else:
        z = z + haslo[i]
print [z]
