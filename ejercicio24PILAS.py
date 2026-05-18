# Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
# su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
# necesarias para resolver las siguientes actividades:

# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posi-
# ción uno la cima de la pila;

# b. determinar los personajes que participaron en más de 5 películas de la saga, además indi-
# car la cantidad de películas en la que aparece;

# c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.


def buscar_posiciones(pila, pos=1):
    if len(pila) == 0:
        return
    
    personaje = pila.pop()
    nombre = personaje[0]
    
    if nombre == "Rocket Raccoon":
        print("Rocket Raccoon está en la posición:", pos)
    if nombre == "Groot":
        print("Groot está en la posición:", pos)
        
    buscar_posiciones(pila, pos + 1)
    pila.append(personaje)


def mas_de_5_peliculas(pila):
    if len(pila) == 0:
        return
    
    personaje = pila.pop()
    nombre = personaje[0]
    peliculas = personaje[1]
    
    mas_de_5_peliculas(pila)
    
    if peliculas > 5:
        print("Personaje:", nombre, "- Películas:", peliculas)
        
    pila.append(personaje)


def buscar_peliculas_vengadora(pila):
    if len(pila) == 0:
        return 0
    
    personaje = pila.pop()
    nombre = personaje[0]
    peliculas = personaje[1]
    
    resultado_resto = buscar_peliculas_vengadora(pila)
    
    pila.append(personaje)
    
    if nombre == "Black Widow":
        return peliculas
    else:
        return resultado_resto


def empezar_con_letras(pila):
    if len(pila) == 0:
        return
    
    personaje = pila.pop()
    nombre = personaje[0]
    
    empezar_con_letras(pila)
    
    if nombre[0] in ["C", "D", "G"]:
        print("Empieza con C, D o G:", nombre)
        
    pila.append(personaje)


pila_mcu = [
    ["Captain America", 11],
    ["Groot", 6],
    ["Black Widow", 9],
    ["Doctor Strange", 6],
    ["Iron Man", 10],
    ["Rocket Raccoon", 7]
]

print("--- Punto A ---")
buscar_posiciones(pila_mcu)

print("\n--- Punto B ---")
mas_de_5_peliculas(pila_mcu)

print("\n--- Punto C ---")
cant_peliculas = buscar_peliculas_vengadora(pila_mcu)
print("Black Widow participó en:", cant_peliculas, "películas.")

print("\n--- Punto D ---")
empezar_con_letras(pila_mcu)
