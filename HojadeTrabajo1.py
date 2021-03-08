altura = int(input("Introduzca la altura del triangulo: "))
for i in range(altura):
   print("*"*(i+1))


numero = int(input("Introduzca el número deseado: "))
for i in range (numero, -1, -1):
   print(i, end=", ")  


num = int(input("Introduzca el número(mayor a 2): "))
for i in range(2, num):
   if num % i == 0:
      break
if(i + 1) == num:
   print(str(num) + " es primo.")
else:
   print(str(num) + " es par.")

