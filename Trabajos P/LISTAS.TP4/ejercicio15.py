
from list_ import List

class Pokemon:
    def __init__(self, nombre: str, nivel: int, tipo: str, subtipo: str):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return f"Pokemon: {self.nombre} | Nivel: {self.nivel} | Tipo: {self.tipo}/{self.subtipo}"

def by_pokemon_name(item): 
    return item.nombre

class Entrenador:
    def __init__(self, nombre: str, torneos_ganados: int, batallas_perdidas: int, batallas_ganadas: int):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_perdidas = batallas_perdidas
        self.batallas_ganadas = batallas_ganadas
        self.pokemons = List()
        # Se agrega el criterio automaticamente al crear el entrenador
        self.pokemons.add_criterion('nombre', by_pokemon_name)

    def __str__(self):
        return f"Entrenador: {self.nombre} | Torneos: {self.torneos_ganados} | PG: {self.batallas_ganadas} | PP: {self.batallas_perdidas}"

def by_trainer_name(item): 
    return item.nombre

# Lista principal de entrenadores
lista_entrenadores = List()
lista_entrenadores.add_criterion('nombre', by_trainer_name)

# Carga de datos de prueba
e1 = Entrenador("Ash", 5, 20, 80)
e1.pokemons.append(Pokemon("Pikachu", 50, "Electrico", "Ninguno"))
e1.pokemons.append(Pokemon("Charizard", 70, "Fuego", "Volador"))
e1.pokemons.append(Pokemon("Pikachu", 20, "Electrico", "Ninguno")) # Repetido

e2 = Entrenador("Misty", 2, 10, 15)
e2.pokemons.append(Pokemon("Psyduck", 30, "Agua", "Ninguno"))
e2.pokemons.append(Pokemon("Gyarados", 60, "Agua", "Volador"))

e3 = Entrenador("Brock", 4, 5, 45)
e3.pokemons.append(Pokemon("Onix", 40, "Roca", "Tierra"))
e3.pokemons.append(Pokemon("Tyrantrum", 55, "Roca", "Dragon"))
e3.pokemons.append(Pokemon("Scovillain", 45, "Fuego", "Planta"))

lista_entrenadores.append(e1)
lista_entrenadores.append(e2)
lista_entrenadores.append(e3)

print("--- RESOLUCION EJERCICIO 15 ---")

# a. Cantidad de Pokemons de un entrenador
print("\na. Cantidad de Pokemons de Ash:")
pos = lista_entrenadores.search("Ash", "nombre")
if pos is not None:
    ent = lista_entrenadores[pos]
    print(f"Ash tiene {len(ent.pokemons)} pokemons.")

# b. Entrenadores con mas de 3 torneos ganados
print("\nb. Entrenadores con mas de 3 torneos:")
for e in lista_entrenadores:
    if e.torneos_ganados > 3:
        print(e.nombre)

# c. Pokemon de mayor nivel del entrenador con mas torneos
print("\nc. Pokemon de mayor nivel del entrenador con mas torneos:")
mas_torneos = lista_entrenadores[0]
for e in lista_entrenadores:
    if e.torneos_ganados > mas_torneos.torneos_ganados:
        mas_torneos = e

pok_mayor = mas_torneos.pokemons[0]
for p in mas_torneos.pokemons:
    if p.nivel > pok_mayor.nivel:
        pok_mayor = p

print(f"Entrenador con mas torneos: {mas_torneos.nombre}")
print(f"Su pokemon de mayor nivel es: {pok_mayor.nombre} (Nivel {pok_mayor.nivel})")

# d. Datos de un entrenador y sus pokemons
print("\nd. Datos de Misty y sus pokemons:")
pos = lista_entrenadores.search("Misty", "nombre")
if pos is not None:
    e = lista_entrenadores[pos]
    print(e)
    for p in e.pokemons:
        print(f"  - {p}")

# e. Porcentaje de batallas ganadas mayor al 79%
print("\ne. Entrenadores con mas del 79% de victorias:")
for e in lista_entrenadores:
    total = e.batallas_ganadas + e.batallas_perdidas
    porcentaje = (e.batallas_ganadas / total) * 100
    if porcentaje > 79:
        print(f"{e.nombre} ({round(porcentaje, 1)}%)")

# f. Pokemons Fuego/Planta o Agua/Volador
print("\nf. Entrenadores con pokemons Fuego/Planta o Agua/Volador:")
for e in lista_entrenadores:
    tiene = False
    for p in e.pokemons:
        if (p.tipo == "Fuego" and p.subtipo == "Planta") or (p.tipo == "Agua" and p.subtipo == "Volador"):
            tiene = True
    if tiene:
        print(e.nombre)

# g. Promedio de nivel de pokemons de un entrenador
print("\ng. Promedio de nivel de Ash:")
pos = lista_entrenadores.search("Ash", "nombre")
if pos is not None:
    e = lista_entrenadores[pos]
    suma = 0
    for p in e.pokemons:
        suma += p.nivel
    promedio = suma / len(e.pokemons)
    print(f"Promedio de nivel de {e.nombre}: {round(promedio, 2)}")

# h. Cuantos entrenadores tienen a un determinado pokemon
print("\nh. Entrenadores que tienen a Pikachu:")
buscado = "Pikachu"
cant = 0
for e in lista_entrenadores:
    if e.pokemons.search(buscado, "nombre") is not None:
        cant += 1
print(f"Cantidad de entrenadores con {buscado}: {cant}")

# i. Entrenadores con pokemons repetidos
print("\ni. Entrenadores con pokemons repetidos:")
for e in lista_entrenadores:
    vistos = []
    repetido = False
    for p in e.pokemons:
        if p.nombre in vistos:
            repetido = True
        else:
            vistos.append(p.nombre)
    if repetido:
        print(e.nombre)

# j. Entrenadores con Tyrantrum, Terrakion o Wingull
print("\nj. Entrenadores con Tyrantrum, Terrakion o Wingull:")
for e in lista_entrenadores:
    if (e.pokemons.search("Tyrantrum", "nombre") is not None or
        e.pokemons.search("Terrakion", "nombre") is not None or
        e.pokemons.search("Wingull", "nombre") is not None):
        print(e.nombre)

# k. Buscar Entrenador X y Pokemon Y
print("\nk. Busqueda interactiva:")
entrenador_x = input("Ingrese nombre de entrenador: ")
pokemon_y = input("Ingrese nombre de pokemon: ")

pos_e = lista_entrenadores.search(entrenador_x, "nombre")
if pos_e is not None:
    ent = lista_entrenadores[pos_e]
    pos_p = ent.pokemons.search(pokemon_y, "nombre")
    if pos_p is not None:
        pok = ent.pokemons[pos_p]
        print("\n--- DATOS ENCONTRADOS ---")
        print(ent)
        print(pok)
    else:
        print(f"{entrenador_x} no tiene a {pokemon_y}")
else:
    print(f"No se encontro al entrenador {entrenador_x}")