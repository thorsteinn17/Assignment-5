
n = int(input("Enter the length of the sequence: ")) # Do not change this line

number_1 = 1 
number_2 = 2
number_3 = 3 
next_number = 0
n=n-2
print(number_1)
print(number_2)
print(number_3)
for i in range(1,n):
    
    next_number = number_1+number_2+number_3
    print (next_number)
    number_1 = number_2
    number_2 = number_3
    number_3 = next_number
    
   
        