num = int(input("Enter a number"))
if num < 25:
    i = num
    while i < 26:
        print ("Inside the loop, my variable is", i)
        i +=1
if num > 25:
    print ("Error")