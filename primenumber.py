Lower=int(input("Enter lower range:"))
Upper=int(input("Enter upper range:"))

for num in range(Lower,Upper+1):
        for i in range(2,num):
            if(num%i==0):
                break
        else:
            print(num)