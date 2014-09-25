total = 0
num = 0
count = 0
continuar = True
print("Teclee numeros y si desea terminar teclee 0")
while continuar:
    num = int(input("Teclea el numero {}: ".format(count+1)))
    total += num
    count += 1
    continuar = num != 0
    
print("El promedio de los {0} numeros es: {1}".format(
    count-1,
    int(total/(count-1))))
