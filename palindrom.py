
word = "towarowy" #wpisujemy słowo do sprawdzenia

def check_palindrom(word): # definiujemy funkcję, która obraca kolejnośc liter w słowie 
   return  word == word[::-1]  # i zwraca po teście True lub False

test = check_palindrom(word)

if test == True :  # mając True lub False możemy wydrukowac informacje czy słowo jest polindromem
    print("Słowo :" + word + " to polindrom")
else :
    print ("Słowo : " + word + " to nie polindrom")

# dodaję do gut hub