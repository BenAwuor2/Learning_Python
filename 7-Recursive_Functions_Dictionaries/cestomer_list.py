#!/usr/bin/python3
#Create a list
customers = []
#Create a loop
while True:
    #Get i/p and make it y or n
    createEntry = input("Enter Customer (yes/no) : ")
    createEntry = createEntry[0].lower()
    #Check to leave the loop
    if createEntry == 'n':
        break
    #Get cutomers data
    else:
        fname,sname = input("Enter customer Name : ").split()
        #Add customers data in a list
        customers.append({"fname": fname, "sname": sname})
#print customers data
for cust in customers:
    print(cust["fname"],cust["sname"])

