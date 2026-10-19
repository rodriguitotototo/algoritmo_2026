
from tree import BinaryTree
import os

os.system('cls' if os.name == 'nt' else 'clear')

arbol_criaturas = BinaryTree()

# b. Se debe permitir cargar una breve descripción sobre cada criatura (y el campo "capturada" del punto g)
arbol_criaturas.insert_node("Ceto", {'derrotado_por': "-", 'descripcion': "Monstruo marino", 'capturada': ""})
arbol_criaturas.insert_node("Tifón", {'derrotado_por': "Zeus", 'descripcion': "Dios de las tormentas", 'capturada': ""})
arbol_criaturas.insert_node("Medusa", {'derrotado_por': "Perseo", 'descripcion': "Gorgona", 'capturada': ""})
arbol_criaturas.insert_node("Ladón", {'derrotado_por': "Heracles", 'descripcion': "Dragón de cien cabezas", 'capturada': ""})
arbol_criaturas.insert_node("Hidra de Lerna", {'derrotado_por': "Heracles", 'descripcion': "Monstruo acuático", 'capturada': ""})
arbol_criaturas.insert_node("León de Nemea", {'derrotado_por': "Heracles", 'descripcion': "León invulnerable", 'capturada': ""})
arbol_criaturas.insert_node("Cerbero", {'derrotado_por': "-", 'descripcion': "Perro de tres cabezas", 'capturada': ""})
arbol_criaturas.insert_node("Toro de Creta", {'derrotado_por': "Teseo", 'descripcion': "Toro blanco", 'capturada': ""})
arbol_criaturas.insert_node("Minotauro de Creta", {'derrotado_por': "Teseo", 'descripcion': "Mitad hombre, mitad toro", 'capturada': ""})
arbol_criaturas.insert_node("Talos", {'derrotado_por': "Medea", 'descripcion': "Gigante de bronce", 'capturada': ""})
arbol_criaturas.insert_node("Sirenas", {'derrotado_por': "-", 'descripcion': "Mujeres pájaro", 'capturada': ""})
arbol_criaturas.insert_node("Basilisco", {'derrotado_por': "-", 'descripcion': "Rey de las serpientes", 'capturada': ""})
arbol_criaturas.insert_node("Cierva Cerinea", {'derrotado_por': "-", 'descripcion': "Cierva veloz", 'capturada': ""})
arbol_criaturas.insert_node("Jabalí de Erimanto", {'derrotado_por': "-", 'descripcion': "Gran jabalí", 'capturada': ""})
arbol_criaturas.insert_node("Aves del Estínfalo", {'derrotado_por': "-", 'descripcion': "Aves de bronce", 'capturada': ""})
arbol_criaturas.insert_node("Ortro", {'derrotado_por': "Heracles", 'descripcion': "Perro de dos cabezas", 'capturada': ""})

# a. Listado inorden de las criaturas y quienes la derrotaron
print("--- A. Criaturas y quienes las derrotaron ---")
def inorden_derrotados(raiz):
    if raiz is not None:
        inorden_derrotados(raiz.left)
        print(f"{raiz.value} - Derrotado por: {raiz.other_values['derrotado_por']}")
        inorden_derrotados(raiz.right)

inorden_derrotados(arbol_criaturas.root)

# c. Mostrar toda la información de la criatura Talos
print("\n--- C. Información de Talos ---")
nodo_talos = arbol_criaturas.search("Talos")
if nodo_talos is not None:
    print(f"Nombre: {nodo_talos.value}")
    print(f"Derrotado por: {nodo_talos.other_values['derrotado_por']}")
    print(f"Descripción: {nodo_talos.other_values['descripcion']}")

# d. Determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas
print("\n--- D. Top 3 héroes que más derrotaron ---")
conteo_heroes = {}
def contar_derrotas(raiz):
    if raiz is not None:
        heroe = raiz.other_values['derrotado_por']
        if heroe != "-":
            if heroe in conteo_heroes:
                conteo_heroes[heroe] += 1
            else:
                conteo_heroes[heroe] = 1
        contar_derrotas(raiz.left)
        contar_derrotas(raiz.right)

contar_derrotas(arbol_criaturas.root)

def ordenar_diccionario(diccionario):
    lista_ordenada = []
    for clave, valor in diccionario.items():
        lista_ordenada.append((clave, valor))
    lista_ordenada.sort(key=lambda x: x[1], reverse=True)
    return lista_ordenada

top_heroes = ordenar_diccionario(conteo_heroes)
for i in range(min(3, len(top_heroes))):
    print(f"{i+1}. {top_heroes[i][0]} con {top_heroes[i][1]} derrotas")

# e. Listar las criaturas derrotadas por Heracles
print("\n--- E. Criaturas derrotadas por Heracles ---")
def derrotadas_por(raiz, heroe):
    if raiz is not None:
        derrotadas_por(raiz.left, heroe)
        if raiz.other_values['derrotado_por'] == heroe:
            print(raiz.value)
        derrotadas_por(raiz.right, heroe)

derrotadas_por(arbol_criaturas.root, "Heracles")

# f. Listar las criaturas que no han sido derrotadas
print("\n--- F. Criaturas no derrotadas ---")
derrotadas_por(arbol_criaturas.root, "-")

# g. Además cada nodo debe tener un campo "capturada" (Implementado en el inciso B)

# h. Modifique los nodos indicando que Heracles las atrapó
nodos_a_modificar = ["Cerbero", "Toro de Creta", "Cierva Cerinea", "Jabalí de Erimanto"]
for nombre in nodos_a_modificar:
    nodo = arbol_criaturas.search(nombre)
    if nodo is not None:
        nodo.other_values['capturada'] = "Heracles"

# i. Se debe permitir búsquedas por coincidencia
print("\n--- I. Búsqueda por coincidencia ('Cer') ---")
arbol_criaturas.proxy_search("Cer")

# j. Eliminar al Basilisco y a las Sirenas
arbol_criaturas.delete_node("Basilisco")
arbol_criaturas.delete_node("Sirenas")
print("\n--- J. Basilisco y Sirenas eliminados ---")

# k. Modificar el nodo que contiene a las Aves del Estínfalo agregando que Heracles derroto a varias
nodo_aves = arbol_criaturas.search("Aves del Estínfalo")
if nodo_aves is not None:
    nodo_aves.other_values['derrotado_por'] = "Heracles derroto a varias"
print("--- K. Aves del Estínfalo modificado ---")

# l. Modifique el nombre de la criatura Ladón por Dragón Ladón
nodo_ladon = arbol_criaturas.search("Ladón")
if nodo_ladon is not None:
    datos = nodo_ladon.other_values
    arbol_criaturas.delete_node("Ladón")
    arbol_criaturas.insert_node("Dragón Ladón", datos)
print("--- L. Ladón renombrado a Dragón Ladón ---")

# m. Realizar un listado por nivel del árbol
print("\n--- M. Listado por niveles ---")
arbol_criaturas.by_level()

# n. Muestre las criaturas capturadas por Heracles
print("\n--- N. Criaturas capturadas por Heracles ---")
def capturadas_por(raiz, heroe):
    if raiz is not None:
        capturadas_por(raiz.left, heroe)
        if raiz.other_values['capturada'] == heroe:
            print(raiz.value)
        capturadas_por(raiz.right, heroe)

capturadas_por(arbol_criaturas.root, "Heracles")