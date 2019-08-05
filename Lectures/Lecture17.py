#Objects and Classes
import bankaccount

def main():

    aheesh = bankaccount.BankAccount(1000000)
    print(aheesh.get_balance())
    print(aheesh.get_name())
    print(aheesh.get_age())
    aheesh.set_name('Aheesh Mantha')
    aheesh.set_age(12)
    print(aheesh.get_name())
    print(aheesh.get_age())    


main()

