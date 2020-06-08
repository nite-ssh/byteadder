'''
Created on Apr 27, 2020

@author: Nitesh Poudel
'''
print("-----------------------|Welcome|-----------------\n")
#created a function that converts decimal into binary 
def conversion(dec):
    
    initial = []
    inversedInitial = []
    counter = 0 
    #this loop converts decimal to binary and appends it into a list 
    while counter != 8:
        rem = dec % 2
        initial.append(rem)
        dec = dec // 2 
        counter = counter + 1 
    #since the appended value is 
    for i in range(len(initial) -1,-1,-1):
        inversedInitial.append(initial[i])
    
    return inversedInitial 
