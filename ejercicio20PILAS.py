# Realizar un algoritmo que registre los movimientos de un robot, los datos que se guardan son
# cantidad de pasos y dirección –suponga que el robot solo puede moverse en ocho direcciones:
# norte, sur, este, oeste, noreste, noroeste, sureste y suroeste–. Luego desarrolle otro algoritmo
# que genere la secuencia de movimientos necesarios para hacer volver al robot a su lugar de
# partida, retornando por el mismo camino que fue.


def registrar_movimiento(pila, pasos, direccion):
    movimiento = [pasos, direccion]
    pila.append(movimiento)


def volver_al_origen(pila):
    if len(pila) == 0:
        return
    
    ultimo_movimiento = pila.pop()
    pasos = ultimo_movimiento[0]
    direccion = ultimo_movimiento[1]
    
    if direccion == "norte":
        vuelta = "sur"
    elif direccion == "sur":
        vuelta = "norte"
    elif direccion == "este":
        vuelta = "oeste"
    elif direccion == "oeste":
        vuelta = "este"
    elif direccion == "noreste":
        vuelta = "suroeste"
    elif direccion == "suroeste":
        vuelta = "noreste"
    elif direccion == "noroeste":
        vuelta = "sureste"
    elif direccion == "sureste":
        vuelta = "noroeste"
        
    print("El robot hace", pasos, "pasos hacia el", vuelta)
    
    volver_al_origen(pila)


# - Zona de prueba -
historial_robot = []

registrar_movimiento(historial_robot, 10, "norte")
registrar_movimiento(historial_robot, 5, "este")
registrar_movimiento(historial_robot, 3, "noreste")

print("Secuencia de regreso:")
volver_al_origen(historial_robot)
