print("\nCiclo while: escribe calificaciones  (negtivo para salir)")
calificacion = 1
contador = 0
suma = 0
while calificacion > 0:
    
    calificacion = int(input("Ingresa la calificacion: "))
    if calificacion > 0:
        suma = suma + calificacion
        print("suma:",suma)
    contador = contador + 1
promedio = suma/ (contador-1)
print("calificaciones ingresadas",contador-1)
print("el promedio es:",promedio)
print("Terminaste el ciclo.")