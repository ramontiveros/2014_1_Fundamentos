num = 0
count = 0
while count < 10:
    num += int(input("Teclea el numero {}: ".format(count+1)))
    count += 1
    
print("El promedio de los numeros es: {}".format(num/10))
