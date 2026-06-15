


cola_personajes = [
    ["Tony Stark",        "Iron Man",             "M"],
    ["Steve Rogers",      "Capitan America",      "M"],
    ["Natasha Romanoff",  "Black Widow",          "F"],
    ["Bruce Banner",      "Hulk",                 "M"],
    ["Thor Odinson",      "Thor",                 "M"],
    ["Clint Barton",      "Hawkeye",              "M"],
    ["Carol Danvers",     "Capitana Marvel",      "F"],
    ["Scott Lang",        "Ant-Man",              "M"],
    ["Peter Parker",      "Spider-Man",           "M"],
    ["Stephen Strange",   "Doctor Strange",       "M"],
    ["Wanda Maximoff",    "Scarlet Witch",        "F"],
    ["Sam Wilson",        "Falcon",               "M"],
    ["T'Challa",          "Black Panther",        "M"],
    ["Shuri",             "Shuri",                "F"],
    ["Hope Van Dyne",     "The Wasp",             "F"]
]

# Punto A
def buscar_personaje_por_superheroe(cola, nombre_superheroe):
    cola_auxiliar = []
    resultado = None
    
    while len(cola) > 0:
        item = cola.pop(0)
        if item[1].lower() == nombre_superheroe.lower():
            resultado = item[0]
        cola_auxiliar.append(item)
        
    while len(cola_auxiliar) > 0:
        cola.append(cola_auxiliar.pop(0))
        
    return resultado

# Punto B
def mostrar_superheroes_femeninos(cola):
    cola_auxiliar = []
    contador = 0
    
    while len(cola) > 0:
        item = cola.pop(0)
        if item[2] == "F":
            contador += 1
            print(f"{contador}. {item[1]}")
        cola_auxiliar.append(item)
        
    while len(cola_auxiliar) > 0:
        cola.append(cola_auxiliar.pop(0))
        
    return contador

# Punto C
def mostrar_personajes_masculinos(cola):
    cola_auxiliar = []
    contador = 0
    
    while len(cola) > 0:
        item = cola.pop(0)
        if item[2] == "M":
            contador += 1
            print(f"{contador}. {item[0]}")
        cola_auxiliar.append(item)
        
    while len(cola_auxiliar) > 0:
        cola.append(cola_auxiliar.pop(0))
        
    return contador

# Punto D
def buscar_superheroe_por_personaje(cola, nombre_personaje):
    cola_auxiliar = []
    resultado = None
    
    while len(cola) > 0:
        item = cola.pop(0)
        if item[0].lower() == nombre_personaje.lower():
            resultado = item[1]
        cola_auxiliar.append(item)
        
    while len(cola_auxiliar) > 0:
        cola.append(cola_auxiliar.pop(0))
        
    return resultado

# Punto E
def mostrar_nombres_con_letra(cola, letra):
    cola_auxiliar = []
    
    while len(cola) > 0:
        item = cola.pop(0)
        if item[0][0].upper() == letra.upper() or item[1][0].upper() == letra.upper():
            print(f"Nombre: {item[0]} | Superheroe: {item[1]} | Genero: {item[2]}")
        cola_auxiliar.append(item)
        
    while len(cola_auxiliar) > 0:
        cola.append(cola_auxiliar.pop(0))

# Punto F
def buscar_personaje(cola, nombre_buscado):
    cola_auxiliar = []
    encontrado = False
    superheroe = None
    
    while len(cola) > 0:
        item = cola.pop(0)
        if item[0].lower() == nombre_buscado.lower():
            encontrado = True
            superheroe = item[1]
        cola_auxiliar.append(item)
        
    while len(cola_auxiliar) > 0:
        cola.append(cola_auxiliar.pop(0))
        
    return encontrado, superheroe

# Pruebas en consola
print("--- PUNTO A: Personaje de Capitana Marvel ---")
personaje_cm = buscar_personaje_por_superheroe(cola_personajes, "Capitana Marvel")
print(f"El personaje es: {personaje_cm}")

print("\n--- PUNTO B: Superheroes femeninos ---")
mostrar_superheroes_femeninos(cola_personajes)

print("\n--- PUNTO C: Personajes masculinos ---")
mostrar_personajes_masculinos(cola_personajes)

print("\n--- PUNTO D: Superheroe de Scott Lang ---")
superheroe_sl = buscar_superheroe_por_personaje(cola_personajes, "Scott Lang")
print(f"El superheroe es: {superheroe_sl}")

print("\n--- PUNTO E: Nombres que empiezan con S ---")
mostrar_nombres_con_letra(cola_personajes, "S")

print("\n--- PUNTO F: Buscar a Carol Danvers ---")
encontrada, superheroe_cd = buscar_personaje(cola_personajes, "Carol Danvers")
if encontrada:
    print(f"Carol Danvers SI esta en la cola. Su superheroe es: {superheroe_cd}")
else:
    print("Carol Danvers NO esta en la cola.")