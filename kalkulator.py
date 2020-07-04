import logging

def add (num1, num2):
    return num1 + num2   
def substr (num1, num2):
    return num1 - num2
def multip (num1,num2):
    return num1 * num2
def divid (num1, num2):
    return num1/num2 


print ("Podaj działanie, posługując się odpowiednią liczbą:")
print ("1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
operation = input ("Podaj numer działania (1,2,3 lub 4)  :  ")

if __name__ == "__main__":
    if operation in  ('1', '2', '3', '4' ): #if operation in range (1:4)
        print ("podaj liczby na których dokonamy działania")
        num1 = float(input ("podaj liczbę nr 1 : "))
        num2 = float (input ("podaj liczbę nr 2 : "))
        if operation == '1':
            logging.info(f"Dodaję liczby {num1} i {num2}")
            print(num1, "+", num2, "=", add(num1, num2))
        elif operation == '2':
            logging.info(f"Odejmuję liczby {num1} i {num2}")
            print(num1, "-", num2, "=", substr(num1, num2))
        elif operation == '3':
            logging.info(f"Mnożę liczby {num1} i {num2}")
            print(num1, "*", num2, "=", multip(num1, num2))
        elif operation == '4':
            logging.info(f"Dzielę liczby {num1} i {num2}")
            roundup = int(input("Ile zer po przecinku ? : "))
            print(num1, "/", num2, "=", round(divid(num1, num2),roundup) )
    else : print ("Nieprawidłowy numer działania")




