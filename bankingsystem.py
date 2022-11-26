User_name = ['Jomhel Dulla', 'Benny Sal', 'KateX']
AccountNumbers = ['2019 1856 103', '2019 8632 405','2019 1516 049']
Pass_word = ['JomD123','BenSal4567','kate123']
NamesOFClients= ['Jomhel Dulla','Benny Salde','Kate Xiao']
ClientPins = ['0001', '0002', '0003']
ClientBalances = [10000, 20000, 30000]
ClientDeposition = 0
ClientWithdrawal = 0
ClientBalance = 0
storage1 = 1
storage2 = 3
u = 0
while True:
    print("************************************************************")
    print("========== WELCOME TO COC-PHINMA BANKING SYSTEM ==========")
    print("************************************************************")
    print("========== (a). Open New Client Account     ============")
    print("========== (b). Transfer / Send Money       ============")
    print("========== (c). Deposit  Money              ============")
    print("========== (d). Check Clients & Balance     ============")
    print("========== (e). Quit                        ============")
    print("************************************************************")
   
    EnterLetter = input("Select your Transaction Above the Box menu : ")
    print ("")
    
    if EnterLetter == "a":
        print("***Open New Client Account***")
        print ("")
        NumberOfClient = eval(input("Number of account that you want to opent : "))
        u = u + NumberOfClient


        if u > 7:
            print("\n")
            print("Client registration exceed reached or Client registration too low")
            u = u - NumberOfClient
            
        else:
            while storage1 <= u:
                name = input("Type your Full Name :")
                NamesOFClients.append(name)
                user_name = input("Create Your Username : ")
                User_name.append(user_name)
                print("\n")
                print("Note! Password should not contain special characters and should only minimum of 7 characters only ")
                pass_word = input("Create your Password :")
                Pass_word.append(pass_word)
                print("\n")
                print("Note! You can find your 11 Digit Account number at the back of your Card.")
                acc_num = str(input("Please Type your 11 Digit Account number : "))
                AccountNumbers.append(acc_num)
                pin = str(input("Please Type your 4 Digit Pin Code to Secure your Account : "))
                ClientPins.append(pin)
                ClientBalance = 0
                ClientDeposition = eval(input("Please Deposit atleast PHP1,500 Amount to Start an Account : "))
                ClientBalance = ClientBalance + ClientDeposition
                ClientBalances.append(ClientBalance)
                print("\n")
                print("***--------------------------------------------------------***")
                print("")
                print("Transaction Details")
                print("FullName:", end=" ")
                print(NamesOFClients[disk2])
                print("User_name:", end=" ")
                print(User_name[disk2])
                print("\nPass_word:", end=" ")
                print(Pass_word[disk2])
                print("Pin:", end=" ")
                print(ClientPins[disk2])
                print("\nBalance:", "P", end=" ")
                print(ClientBalances[disk2], end=" ")
                disk1 = disk1 + 1
                disk2 = disk2 + 1
                print("\nYour name is added to Client Table")
                print("Your pin is added to Client Table")
                print("Your balance is added to Client Table")
                print("\n")
                print("----New Client account created Successfully !!!----")
                print("\n")
                print("Your Name is Available on the Client list now : ")
                print(NamesOFClients)
                print("\n")
                print("Note! Please remember the Username and Password for Online Transaction")
                print("========================================")

        mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
        
    elif EnterLetter == "b":
        v = 0
        print("***Transfer Money***")
        while v < 1:
            w = -1
            user_name = input("Username : ")
            pass_word = input("Password : ")
            while w < len(User_name) - 1:
                w = w + 1
                if user_name == User_name[w]:
                    if pass_word == Pass_word[w]:
                        v = v + 1
                        print("Your Current Balance:", "P", end=" ")
                        print(ClientBalances[w], end=" ")
                        print("\n")
                        ClientBalance = (ClientBalances[w])
                        ClientWithdrawal = eval(input("Insert value to Withdraw : "))
                        if ClientWithdrawal > ClientBalance:
                            deposition = eval(input(
                                "Please Deposit a higher Value because your Balance mentioned above is not enough : "))
                            ClientBalance = ClientBalance + deposition
                            print("Your Current Balance:", "P", end=" ")
                            print(ClientBalance, end=" ")
                            ClientBalance = ClientBalance - ClientWithdrawal
                            print("-\n")
                            print("----Withdraw Successfully!----")
                            ClientBalances[w] = ClientBalance
                            print("Your New Balance: ", "P", ClientBalance, end=" ")
                            print("\n\n")
                        else:
                            ClientBalance = ClientBalance - ClientWithdrawal
                            print("\n")
                            print("----Withdraw Successfully!----")
                            ClientBalances[w] = ClientBalance
                            print("Your New Balance: ", "P", ClientBalance, end=" ")
                            print("\n")
            if v < 1:
                print("Your Username or Password does not match!\n")
                break

        mainMenu = input("Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
    elif EnterLetter == "c":
        print("**------Deposit  Money-------**")
        x = 0
        while x < 1:
            w = -1
            user_name = input("Username : ")
            pass_word = input("Password : ")
            while w < len(User_name) - 1:
                w = w + 1
                if user_name == User_name[w]:
                    if pass_word == Pass_word[w]:
                        x = x + 1
                        print("Your Current Balance: ", "P", end=" ")
                        print(ClientBalances[w], end=" ")
                        ClientBalance = (ClientBalances[w])
                        print("\n")
                        ClientDeposition = eval(input("Enter the value you want to deposit : "))
                        ClientBalance = ClientBalance + ClientDeposition
                        ClientBalances[w] = ClientBalance
                        print("\n")
                        print("----Deposition successful!----")
                        print("Your New Balance: ", "P", ClientBalance, end=" ")
                        print("\n")
            if x < 1:
                print("Your name and pin does not match!\n")
                break
        mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
    elif EnterLetter == "d":
        print("***----Check Clients & Balance***----")
        w = 0
        print("Client name list and balances mentioned below : ")
        print("\n")
        while w <= len(NamesOFClients) - 1:
            print("->.Customer =", NamesOFClients[w])
            print("->.Balance =", "P", ClientBalances[w], end=" ")

            print("\n")
            w = w + 1
        mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_ ")

    elif EnterLetter == "e":
        print("Thank you for using COC-PHINMA BANK!!!")
        print("\n")
        print("May we continue to serve you better in the future!!!")
        print("Thank you and Have a Great Day!!!")
        print("God Bless")
        break
    else:
        print ("Attention!!! Case-Sensitive!!!")
        print("")
        print("Invalid option")
        print("Please Try again!")

        mainMenu = input("Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")