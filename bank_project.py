from function import ramdom_no
from main_menu import menu1
from exit_menu import exit1


n = 1
l = []
print("\nWelcome to the Bank Management System. Namaste \U0001F64F \U0001F64F !!")

while True:
    menu1()
    try:
        x = int(input("enter the no. what you want:"))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if x == 1:
        z = []
        print("Your Account number is:", n)
        name = input("Enter your name:")
        a = ramdom_no("cust_id")
        print("Your Customer ID:",a)
        c = input("Enter branch name:")
        d = input("Enter your address:")
        e = ramdom_no("ifse_no")
        print("Your IFSE Number:",e)
        f = input("Enter Account type:")
        g = 0

        z.append(name)
        z.append(a)
        z.append(c)
        z.append(d)
        z.append(e)
        z.append(f)
        z.append(g)
        l.append(z)
        n = n + 1

        print("\nAccount Created Successfully \U0001F44D \U0001F44D \U0001F44D")

    elif x == 2:
        no = int(input("Enter your Account number:"))
        if no < 1 or no > len(l):
            print("\nInvalid Account number.")
            continue

        print("What you want to update")
        print("1.Your name.\n2.Your address.\n3.Account type.")
        y = int(input("Enter the no."))
        xy = l[no - 1]

        if y == 1:
            print("Your Old Name is", xy[0])
            name = input("\nEnter your new name:")
            xy[0] = name
            print("\nYour Name is Successfully Updated \U0001F44D \U0001F44D \U0001F44D ")
        elif y == 2:
            print("Your Old Adress is", xy[3])
            adress = input("\nEnter your new Adress:")
            xy[3] = adress
            print("\nYour Adress is Successfully Updated \U0001F44D \U0001F44D \U0001F44D ")
        elif y == 3:
            print("Your Old Account type is", xy[-2])
            acc_type = input("\nEnter your new Account type:")
            xy[-2] = acc_type
            print("\nYour Account type is Successfully Updated \U0001F44D \U0001F44D \U0001F44D ")
        else:
            print("\nInvalid choice.")

    elif x == 3:
        no = int(input("\nEnter your Account number:"))
        if no < 1 or no > len(l):
            print("\nInvalid Account number.")
            continue
        deposit = int(input("\nEnter the Amount:"))
        ab = l[no - 1]
        ab[-1] = ab[-1] + deposit
        print("\nYour Account Balance is:", ab[-1])

    elif x == 4:
        no = int(input("Enter your Account number:"))
        if no < 1 or no > len(l):
            print("\nInvalid Account number.")
            continue
        withdraw = int(input("\nEnter the Amount:"))
        ab = l[no - 1]
        if withdraw > ab[-1]:
            print("\nInsufficient balance. Withdrawal denied.")
        else:
            ab[-1] = ab[-1] - withdraw
            print("\nYour Account Balance is:", ab[-1])

    elif x == 5:
        no = int(input("\nEnter your Account number:"))
        if no < 1 or no > len(l):
            print("\nInvalid Account number.")
            continue
        ab = l[no - 1]
        print("\nYour Account Balance is:", ab[-1])

    elif x == 6:
        no = int(input("\nEnter your Account number:"))
        if no < 1 or no > len(l):
            print("\nInvalid Account number.")
            continue
        ab = l[no - 1]
        print("\nYour Account Details is:", ab)

    elif x == 7:
        password = input("\nEnter password to access Manager folder:")
        if password == "abc123":
            print("1.Show total account.\n2.Check the customer names who have transaction more than 10 Thousand per month."
                  "\n3.Check the customer names who have transaction less than 500 per month.")
            choice = int(input("enter the no."))
            if choice == 1:
                print(l)
            elif choice == 2:
                for i in l:
                    if i[-1] >= 10000:
                        print(i)
            elif choice == 3:
                for i in l:
                    if i[-1] <= 500:
                        print(i)
            else:
                print("\nInvalid choice.")
        else:
            print("*Wrong Password*\nYou can not access Manager folder.")

    elif x >= 8:
        exit1()
        break