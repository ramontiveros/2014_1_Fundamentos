num = 0
for count in range(10):
    num += int(input("Teclea el numero {}: ".format(count+1)))
    
print("El promedio de los numeros es: {}".format(num/10))
