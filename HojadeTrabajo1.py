peso_persona = float(input("Introduzca su peso en kilogramos: "))
altura_persona = float(input("Introduzca su altura en metros: "))
IMC = float(str(round(peso_persona/(altura_persona + altura_persona), 2)))
print("Tu índice de masa corporal es:", IMC)

