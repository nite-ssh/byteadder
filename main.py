#importing modules
import conversionFunction as cf
#created a function that converts list into string 
def listToString(a):
    jrey = ""
    for value in a:
        jrey = jrey + str(value) 
    return jrey 
#created a function that displays the dum of two binary number from list to string
def displayTheSum(a,b,list):
    print(f"The sum of {a} and {b} is: ",end = "")

    for value in list:
        print(value,end = "")
    print("\n")
#bounds the input number 
def numberRange(number):
    if number < 0 or number > 255:
        return True
    else:
        return False 
#converts decimal input into binary
def bintodec(l):
    init = 0
    dec = 0
    for i in range(len(l) - 1, -1, -1):
        dec = dec + l[i]*(2**init)
        init = init+1
    return dec 
#adds two 8 bit binary numbers
def addition(a,b):
    carr = [0,0,0,0,0,0,0,0]
    #add = []
    finalSum = []
    fullandfinal = []
    x = len(a)-1
    

    for i in range (x+1):
        #using XOR addition to add binary numbers and storing it in sum
        sum = a[x-i] ^ b[x-i] ^ carr[x-i]
        #carry out is stored in 6th index as the 7th carry out remains 0
        carr[(x-i)-1] = (carr[x-i] and (a[x-i] ^ b[x-i])) or (a[x-i] and b[x-i])       
        finalSum.append(sum)
    #using while loop to reverse the value
    counter = 7
    while counter>-1:
        varStore = finalSum[counter]
        fullandfinal.append(varStore)
        counter = counter -1 
    return fullandfinal

invalidValue = False 
continuation = True 
operation = False 
while continuation == True:
    try: #using try and ecept to catch an exception
        firstInput = int(input("Enter first decimal number:\n"))
        invalidValue = numberRange(firstInput) 
        while invalidValue == True:
            firstInput = int(input("Number out of range enter input between 0 and 255:\n")) 
            invalidValue = numberRange(firstInput) 
        g = cf.conversion(firstInput) 
        h = listToString(g)
        print("The binary equivalent of",firstInput,"is",h)
        print("--------------------------------------------------")

        if invalidValue == False:
            reversedec = cf.conversion(firstInput) 

        secondInput = int(input("Enter another decimal number:\n"))
        invalidValue = numberRange(secondInput)
        while invalidValue == True:
            secondInput = int(input("Number out of range enter input between 0 and 255:\n")) 
            invalidValue = numberRange(secondInput)    
        g = cf.conversion(secondInput)
        h = listToString(g)
        print("The binary equivalent of",secondInput,"is",h)
        print("--------------------------------------------------")
        if (firstInput+secondInput > 255):
            #checks if the addition of two numbers is greater than 255 to make the binary addition 8 bit
            print("This number exceeds the bound of 8 bit addition operation")
            print("--------------------------------------------------")
        else:
            if invalidValue == False:
                reversedec_2 = cf.conversion(secondInput) 

            if invalidValue == False:
                operation = True 
            if operation == True:
                xyza = addition(reversedec, reversedec_2) #intakes two values for addition
                print("--------------------------------------------------")
                b1 = listToString(reversedec)
                b2 = listToString(reversedec_2)
                ltstring = displayTheSum(b1, b2, xyza)
                print("The decimal value of sum is: ",bintodec(xyza))
                print("--------------------------------------------------")
            else:
                print("Input values are out of bound. Please enter input below 255")

        ask = input("Do you want to continue? (y/n)\n")
        ask = ask.upper() #asks if user wants to continue
        if ask == "N":
            continuation = False #after n is pressed continuation sets to false and the code ends. 
            break 
    except:     
        print("The program only accepts integer data type")
        break

print("----------------|The Program has Ended|----------- \n")
print("---------------------|Thank you!|-----------------")
