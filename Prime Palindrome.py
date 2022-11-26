my_number=int(input("Enter the number: "))


lower = 0
upper = 100000
my_list = []

for num in range(lower,upper+1):
    reverse = int(str(num)[::-1])
    if num == reverse:
        if num>1:
            for i in range (2,num):
                if (num%i)==0:
                    break
            else:
                my_list.append(num)

print(my_list[my_number],"is the Palindromic Prime Number")
