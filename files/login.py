from os import close, read


def login():
    #login function
    loginto = int(input("Welcome press 1 to login or press any key to Exit: "))
    if loginto == 1:
        email = input("enter your email ")
        password = input("enter your password here ")
        #read file
        file = open('data.txt', 'r')
        list_of_data = []
        #for loop
        for line in file:
            #splite to arrays
            #var x include splited array
            stripped_data = line.strip()
            line_list = stripped_data.split(',')
            list_of_data.append(line_list)
        file.close()
        print(list_of_data)

        #check mail and password
        if email == list_of_data[6] in list_of_data:
            print("welcome mr")


        #if x indexes right login
        #if not enter your data again nady 3la el login or exit
    else :
        print("GoodBye Sir")
login()
