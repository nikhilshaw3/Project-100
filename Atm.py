import time
import random as ran

Name=input('Hello, what is your Name ??? - ')

print('Hello !!! . Welcome to this Atm .')

class ATM(object):
    def cardNumber():
        num=input('Enter your card number - ')
        print('Hello ' + Name + "!!!")

    def pin():
        pin=input('Enter your pin number - ')
        
    def withdraw():
        balance=100000
        howMuchMoney=input('How much money do you want to withdraw ??? - ')
        howMuchMoneyint=int(howMuchMoney)
        
        if howMuchMoneyint < balance:
            balance=int(balance)-howMuchMoneyint
            print('Your balance is now, '+str(balance))
        
        if howMuchMoneyint>balance:
            print('Not enough money')

    def deposit():
        balance=100000
        
        howMuchMoney=input('How much money do you want to deposit ??? - ')
        howMuchMoneyint=int(howMuchMoney)
       
        balance = balance+int(howMuchMoney)
        
        print('Your balance in this Atm is - '+str(balance))
    
    def enquiry():
        balance=str(100000)
        print('Your balance in this Atm is - '+balance)

    cardNumber()
    pin()
    
    print("What do you want to do ???")
    transaction=str(input('if you want to withdraw some money press 1, If you want to deposit some money press 2, If you want to know how much money you have press 3 -> '))
    
    if transaction=='1':
        withdraw()
    elif transaction=='2':
        deposit()
    elif transaction=='3':
        enquiry()
    elif transaction != ('1' or '2' or '3'):
        print('There is no transaction for the number '+ transaction)