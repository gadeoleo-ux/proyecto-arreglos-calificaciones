# Sistema de calificaciones con vectores (listas) en Python
# Estudiante: Gabriel De Oleo - A00190321

NOTA_APROBADO = 70

estudiantes = ["Ana", "Luis", "Carlos", "María", "Pedro"]
calificaciones = [85, 67, 92, 74, 58]

def mostrar_calificaciones():
    print("\nCalificaciones actuales:")
    for i in range(len(calificaciones)):
        print(f"  [{i}] {estudiantes[i]}: {calificaciones[i]}")

def consultar_por_indice():
    i = int(input("Posición del estudiante (0 a " + str(len(calificaciones) - 1) + "): "))
    if 0 <= i < len(calificaciones):
        print(f"{estudiantes[i]} tiene {calificaciones[i]}")
    else:
        print("Esa posición no existe en el vector.")

def mostrar_promedio():
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"\nPromedio del grupo: {promedio:.1f}")

def mostrar_mayor_y_menor():
    mayor = calificaciones[0]
    menor = calificaciones[0]
    pos_mayor = 0
    pos_menor = 0
    for i in range(1, len(calificaciones)):
        if calificaciones[i] > mayor:
            mayor = calificaciones[i]
            pos_mayor = i
        if calificaciones[i] < menor:
            menor = calificaciones[i]
            pos_menor = i
    print(f"\nNota más alta: {mayor} ({estudiantes[pos_mayor]})")
    print(f"Nota más baja: {menor} ({estudiantes[pos_menor]})")

def contar_aprobados_y_reprobados():
    aprobados = 0
    reprobados = 0
    for nota in calificaciones:
        if nota >= NOTA_APROBADO:
            aprobados += 1
        else:
            reprobados += 1
    print(f"\nAprobados: {aprobados}")
    print(f"Reprobados: {reprobados}")

def modificar_calificacion():
    i = int(input("Posición del estudiante a modificar: "))
    if 0 <= i < len(calificaciones):
        calificaciones[i] = int(input(f"Nueva nota para {estudiantes[i]} (actual {calificaciones[i]}): "))
        print("Calificación actualizada.")
        mostrar_calificaciones()
    else:
        print("Esa posición no existe en el vector.")

def menu():
    print("\n=== SISTEMA DE CALIFICACIONES ===")
    print("1. Mostrar calificaciones")
    print("2. Consultar por posición")
    print("3. Calcular promedio")
    print("4. Nota más alta y más baja")
    print("5. Aprobados y reprobados")
    print("6. Modificar una calificación")
    print("7. Salir")

opcion = ""
while opcion != "7":
    menu()
    opcion = input("Elija una opción: ")
    if opcion == "1":
        mostrar_calificaciones()
    elif opcion == "2":
        consultar_por_indice()
    elif opcion == "3":
        mostrar_promedio()
    elif opcion == "4":
        mostrar_mayor_y_menor()
    elif opcion == "5":
        contar_aprobados_y_reprobados()
    elif opcion == "6":
        modificar_calificacion()
    elif opcion == "7":
        print("Programa finalizado.")
    else:
        print("Opción no válida.")
