from unicodedata import decimal


num = int(input("Enter Binar Number : "))

sum = 0
i = 0
while num!=0:
    rem = num%10
    sum = sum + rem * pow(2,i)
    num = int(num/10)
    i = i+1
print()
print(" Decimal Number is : ",sum)