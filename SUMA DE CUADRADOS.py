n1= int (input ("ingresa el valor hasta el que deseas llegar"))
a=1
sum=0

while a<=n1:
    sum +=a**(a+1)
    a+=1

    res=sum/n1
print(f"El resultado es:{res}")
    


