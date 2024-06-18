n= [8,9,3,1,2,0,5,0]

for item in n:
    
    print (item*2)

    # zero's and numbers in different list
    
zero=[]
numbers=[]
for item in n:
        if item == 0:
           zero.append(item)
        else: 
           numbers.append(item)

    
print("Zero's in the list:", zero)      
print("Numbers in the list:", numbers)  
  

