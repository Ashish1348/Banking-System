import random as r

print("\n\tWelcome to The Bank\n")
name = input("Enter your Name : ")
print("welcome",name)
Id1 = r.randint(1,100)
Id2 = r.randint(1,100)
Id3 = r.randint(1,100)
Id4 = r.randint(1,100)
Customar_id = ("UD"+str(Id1)+str(Id2)*2+str(Id3)+str(Id4)+str(Id2)+str(Id4)+str(Id1))
print("your Customar ID - ",Customar_id)
while True:
    chak = input("\nYou can chak your account ? \nEnter 'yes' or 'no' : ")

    if chak == "yes":
        print("\nLet's chak your account")
    elif chak == "no":
        break
    else:
        print("Worng input !\nPlease try agin")
        continue
    ID = input("\nEnter Customar ID : ")

    if ID == Customar_id :
        print("Acces Grented")
    else:
        print("\nWrong Customar ID")
        break

    class Bank():
        def __init__(self):
            self.Name = name
            self.Bankblance = 100000
        def show(self):
            print("\n\t\t  ////////Account Details////////\n")
            print("Name :",self.Name,"\tBank Blance :",self.Bankblance,"\tCustomar ID :",Customar_id)
        def action(self) :
            while True :
                print("\nWhat you do\n(1)Deposit\n(2) withdraw")
                choice = input("Enter Option : ")

                if choice == "1":
                    print("\nLet's start")
                    amout = int(input("\nHow much amout you want to deposite : "))
                    if amout <= 0 :
                        print("Invalide amount! Please try agin")
                        continue
                    self.Bankblance +=amout
                    break
                elif choice == "2":
                    while True:
                        print("\nLet's start")
                        
                        amout = int(input("\nHow much amout you want to withdraw : "))
                        if amout > self.Bankblance:
                            print("\nNo more bank blance as withdraw amout ! Plaease withdraw right amount")
                            print("Your bank Blance :",self.Bankblance)
                            continue
                        else:
                            self.Bankblance -= amout
                            break
                    break   

                else :
                    print("\nInvalid input!\nPlease try agin")
                    continue
                    

    bank = Bank()
    bank.show()
    bank.action()
    bank.show()