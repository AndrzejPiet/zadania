import logging
import math

def add (numbers):
    return sum(numbers)  
def substr (num1, num2):
    return num1 - num2
def multip (numbers):
    return math.prod(numbers) 
def divid (num1, num2):
    return num1/num2 
numbers=[]

print ("Podaj działanie, posługując się odpowiednią liczbą:")
print ("1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
operation = input ("Podaj numer działania (1,2,3 lub 4)  :  ")

if __name__ == "__main__":
    if operation in  ( '2', '4' ): 
        print ("podaj liczby na których dokonamy działania")
        num1 = float(input ("podaj liczbę nr 1 : "))
        num2 = float (input ("podaj liczbę nr 2 : "))
        if operation == '2':
            logging.info(f"Odejmuję liczby {num1} i {num2}")
            print(num1, "-", num2, "=", substr(num1, num2))
        elif operation == '4':
            logging.info(f"Dzielę liczby {num1} i {num2}")
            roundup = int(input("Ile zer po przecinku ? : "))
            print(num1, "/", num2, "=", round(divid(num1, num2),roundup) )
    elif operation in ('1','3') :
        data = input("Podaj liczby (po przecinku) , na których dokonamy działania : ")
        list = data.split(',')
        numbers = [int(i) for i in list]
        logging.info(numbers)
        if operation == '1':
            logging.info(f"Dodaję liczby {numbers}")
            print(f"Suma Twoich liczb {numbers} to : ", add(numbers) )
        elif operation == '3':
            logging.info(f"Mnożę liczby {numbers}")
            print(f"Wynik po przemnożeniu Twoich liczb {numbers} to : ", multip (numbers) )

    else : print ("Nieprawidłowy numer działania")