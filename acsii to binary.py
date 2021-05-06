n = 1 #setting to 1 

while n == 1:  #creating a loop whilst n = 1

    char = input("Please enter text: ") #asking user for text to be converted
    for letter in char:   # creating a loop for every charater(s)
        deciminal = ord(letter) #getting decimal value
        binary = bin(deciminal) #getting binary value but has b in it
        a = bin(deciminal)      
        b = bin(deciminal)[2:]   #found this to remove b dont know how it works
        c = b.zfill(8)
        print()


        print(
            letter,
            "=",
            "Deciminal:",   # printing results in easy to read format
            deciminal,
            "Binary:",
            c
            )


        print()

else:
    print("error")
