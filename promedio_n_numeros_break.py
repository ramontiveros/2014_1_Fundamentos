total = 0
num = 0
count = 0
print("Teclee numeros y si desea terminar teclee 0")
while True:
    num = int(input("Teclea el numero {}: ".format(count+1)))
    if num == 0:
        break
    total += num
    count += 1
    
print("El promedio de los {0} numeros es: {1}".format(
    count,
    int(total/count)))
