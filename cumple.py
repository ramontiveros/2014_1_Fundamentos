import datetime

actual = datetime.date.today()

def ProximoCumple(fecha):
    cumple = datetime.date(actual.year,fecha.month,fecha.day)
    if((cumple - actual).days < 0):
        return datetime.date(actual.year + 1,fecha.month,fecha.day)
    else:
        return datetime.date(actual.year,fecha.month,fecha.day)

def DiasParaCumple(fecha):
    return (ProximoCumple(fecha) - actual).days
    

cfecha = input("Cual es tu fecha de nacimiento? (formato dd/mm/aaaa): ")
dfecha = datetime.datetime.strptime(cfecha, "%d/%m/%Y")
dias = DiasParaCumple(dfecha)
print("Felicidades, faltan {} dias para tu cumpleaños".format(dias))
