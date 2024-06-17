n = [1,2,3,4,5,6,7,8]
for item in n:
    if item %2==0:
       print(item, "this are EVEN numbers")
    else: 
        print(item, "this are ODD numbers")

n[0] = 100
print(n)       
