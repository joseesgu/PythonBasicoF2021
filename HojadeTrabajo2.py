contraseña = input("Introduzca una contraseña: ")
contraseña2 = input("Introduzca nuevamente la contraseña: ")
if contraseña == contraseña2:
    print("Bienvenido al sistema")
else:
    print("La contraseña no coincide con la contraseña en el sistema. Intente nuevamente.")


nombre = input("Ingrese su nombre: ")
sexo = input("ingrese su sexo (H o M): ")

if sexo == "M":
    if nombre.lower() < "m":
        grupo = "A"
    else:
        grupo = "B"
else:
    if nombre.lower() > "n":
        grupo = "A"
    else:
        grupo = "B"
    print("Estás en el grupo " + grupo)
