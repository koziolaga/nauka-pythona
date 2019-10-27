samochody =['syrena', 'poloneza', 'fiat', 'kia']
ilosc = [3,5,6,6]
#print samochody[-1]
#print samochody[1,-1]
#print samochody[1:]
#print samochody[10]
for idx in range( len (samochody)) :
    print("idx: " + str(idx) + " : " + samochody[idx])
    print(samochody[idx] + " ma ilosc drzwi " + str(ilosc[idx]))
