print("Enter the Number : ")
number=int(input())
count=2
print()
print("The prime factors of given number are : ")
while(count<=number):
    if(number%count==0):
        flag="true"
        second_count=2
        while(second_count<count):
            if(count%second_count==0):
                 flag="false"
            second_count=second_count+1
        if(flag=="true"):
            print(count)
    count=count+1