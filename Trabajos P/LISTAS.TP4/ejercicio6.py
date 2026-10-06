
from typing import Any, Optional
from list_ import List 

class Superheroe:
    def __init__(self, name: str, year: int, house: str, bio: str):
        self.name = name
        self.year = year
        self.house = house
        self.bio = bio

    def __str__(self):
        return f"{self.name} ({self.year}) - {self.house} | Bio: {self.bio}"

# Funciones de criterio escritas de forma comun
def by_name(item): 
    return item.name

def by_year(item): 
    return item.year

def by_house(item): 
    return item.house

# Instanciamos la lista
lista_heroes = List()
lista_heroes.add_criterion('name', by_name)
lista_heroes.add_criterion('year', by_year)
lista_heroes.add_criterion('house', by_house)

# Carga de datos
lista_heroes.append(Superheroe("Linterna Verde", 1940, "DC", "Usa un anillo de poder extraterrestre"))
lista_heroes.append(Superheroe("Wolverine", 1974, "Marvel", "Mutante con esqueleto de adamantium y garras"))
lista_heroes.append(Superheroe("Dr. Strange", 1963, "DC", "Hechicero supremo")) 
lista_heroes.append(Superheroe("Iron Man", 1963, "Marvel", "Multimillonario que construyo una armadura de alta tecnologia"))
lista_heroes.append(Superheroe("Batman", 1939, "DC", "Multimillonario con un traje oscuro y gadgets"))
lista_heroes.append(Superheroe("Capitana Marvel", 1967, "Marvel", "Poderes cosmicos y fuerza sobrehumana"))
lista_heroes.append(Superheroe("Mujer Maravilla", 1941, "DC", "Princesa amazona con lazo de la verdad"))
lista_heroes.append(Superheroe("Flash", 1940, "DC", "Velocista escarlata, conectado a la fuerza de la velocidad"))
lista_heroes.append(Superheroe("Star-Lord", 1976, "Marvel", "Lider de los guardianes de la galaxia"))
lista_heroes.append(Superheroe("Spider-Man", 1962, "Marvel", "Usa un traje rojo y azul, lanza telaranas"))
lista_heroes.append(Superheroe("Superman", 1938, "DC", "Extraterrestre de Krypton con superfuerza"))

print("--- RESOLUCION DEL TP ---")

# a. Eliminar a Linterna Verde
print("\na. Eliminando a Linterna Verde...")
lista_heroes.delete_value("Linterna Verde", criterion="name")

# b. Anio de aparicion de Wolverine
print("\nb. Anio de aparicion de Wolverine:")
pos = lista_heroes.search("Wolverine", "name")
if pos is not None:
    print(lista_heroes[pos].year)

# c. Cambiar casa de Dr. Strange a Marvel
print("\nc. Cambiando casa de Dr. Strange...")
pos = lista_heroes.search("Dr. Strange", "name")
if pos is not None:
    lista_heroes[pos].house = "Marvel"
    print(f"Actualizado: {lista_heroes[pos].name} ahora es de {lista_heroes[pos].house}")

# d. Buscar 'traje' o 'armadura' en biografia
print("\nd. Superheroes con 'traje' o 'armadura' en su biografia:")
lista_heroes.filter_contain_on_bio(["traje", "armadura"])

# e. Superheroes anteriores a 1963
print("\ne. Superheroes anteriores a 1963:")
for heroe in lista_heroes:
    if heroe.year < 1963:
        print(f"{heroe.name} - {heroe.house}")

# f. Casa de Capitana Marvel y Mujer Maravilla
print("\nf. Casa de Capitana Marvel y Mujer Maravilla:")
pos_cap = lista_heroes.search("Capitana Marvel", "name")
pos_mar = lista_heroes.search("Mujer Maravilla", "name")

if pos_cap is not None:
    print(f"Capitana Marvel: {lista_heroes[pos_cap].house}")
if pos_mar is not None:
    print(f"Mujer Maravilla: {lista_heroes[pos_mar].house}")

# g. Informacion de Flash y Star-Lord
print("\ng. Informacion de Flash y Star-Lord:")
pos_flash = lista_heroes.search("Flash", "name")
pos_star = lista_heroes.search("Star-Lord", "name")

if pos_flash is not None:
    print(lista_heroes[pos_flash])
if pos_star is not None:
    print(lista_heroes[pos_star])

# h. Superheroes que comienzan con B, M y S
print("\nh. Superheroes que comienzan con B, M y S:")
lista_heroes.filter_start_with(("B", "M", "S"))

# i. Cantidad por casa de comic
print("\ni. Cantidad de superheroes por casa de comic:")
cant_marvel = 0
cant_dc = 0

for heroe in lista_heroes:
    if heroe.house == "Marvel":
        cant_marvel += 1
    elif heroe.house == "DC":
        cant_dc += 1

print(f"Marvel: {cant_marvel} | DC: {cant_dc}")