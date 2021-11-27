from os import close, read

def login():
    #login function
    loginto = input("Welcome press 1 to login or press any key to Exit: ")
    if loginto == "1":
        email = input("enter your email ")
        password = input("enter your password here ")

        txt_file = open("data.txt",'r')
        for line in txt_file:
            data = line.split(',')
            if(email == data[6] and password == data[7]):
                print("hello : " + data[1])
                break
        else:
            print("password not write enter your data again or exit")
            login()
    else :
        print("GoodBye Sir")
login()
