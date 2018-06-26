# -*- coding: utf-8 -*-
print("""\n\n\n\nThis is ATM machine's working Algo\n@author: Vishvajeet Singh\n\n""")


# Custiomized Class
class Error(Exception):
    """Base class for exception"""
    pass


class low_bal(Error):
    """Raised error low balance"""
    pass


# Taking intial amount from user
while (True):
    try:
        amt = int(input("Enter Initial Amount->\n"))
        break
    except ValueError:
        print("Please enter valid number")

# option list
while (True):
    try:
        print("""1:Balance\n2:Credit \n3:Withdraw \n4:Exit->""")
        j = int(input())

        if (j == 1):
            print("Available Balance:", amt)
        elif (j == 2):
            print("Enter Amount:")
            bal = int(input())
            amt += bal
            print("Account Balance Updated successfully ->", amt)
        elif (j == 3):
            print("Enter Amount:")
            bal = int(input())
            if (amt < bal):
                raise low_bal
            else:
                amt -= bal
                print("Account Balance Updated successfully ->", amt)
        elif (j == 4):
            break
        else:
            print("Enter Valid Option")
            continue


    except low_bal:
        print("\nSorry could not perform transection low balance")
        while (True):
            decision = input("Want to continue!(Y/N):\n")
            if (decision == 'Y' or decision == 'y'):
                break

            elif (decision == 'n' or decision == 'N'):
                break
            else:
                print("Invalid option")
        if (decision == 'Y' or decision == 'y'):
            continue
        else:
            break




    except ValueError:
        print("Please enter valid number")

print("\n### For further Updates check my GITHUB profile ###")
print("#################### THANKS FOR YOUR VISIT ######################")






