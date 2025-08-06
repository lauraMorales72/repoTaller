edad = int(input("Ingresa tu edad: "))

if edad >=0 and edad<4:
    print("gratis")
elif edad >=4 and edad<=12:
    print("pagar 40")
elif edad >=13 and edad<=59:
    print("pagar 70")
elif edad >=60:
    print("pagar 35")
else:
    print("Edad no válida.")