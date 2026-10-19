
from tree import BinaryTree
import os

# Esto limpia la terminal porque me aparecia una ruta rara arriba 
os.system('cls' if os.name == 'nt' else 'clear')

arbol_mcu = BinaryTree()

# a. Almacenar superhéroes y villanos con su campo booleano
arbol_mcu.insert_node("Iron Man", {'is_villain': False})
arbol_mcu.insert_node("Thanos", {'is_villain': True})
arbol_mcu.insert_node("Capitan America", {'is_villain': False})
arbol_mcu.insert_node("Red Skull", {'is_villain': True})
arbol_mcu.insert_node("Hulk", {'is_villain': False})
arbol_mcu.insert_node("Black Widow", {'is_villain': False})
arbol_mcu.insert_node("Loki", {'is_villain': True})
arbol_mcu.insert_node("Doctor Strang", {'is_villain': False}) 
arbol_mcu.insert_node("Captain Marvel", {'is_villain': False})

# b. Listar los villanos ordenados alfabéticamente
# Hacemos nuestra propia función inorden (Izquierda -> Raíz -> Derecha)
print("B)--- Villanooos ---")
def listar_villanos(raiz):
    if raiz is not None:
        listar_villanos(raiz.left)
        if raiz.other_values['is_villain'] == True:
            print(raiz.value)
        listar_villanos(raiz.right)

listar_villanos(arbol_mcu.root)

# c. Mostrar todos los superhéroes que empiezan con C
print("\nC)--- Héroes con C ---")
def listar_heroes_C(raiz):
    if raiz is not None:
        listar_heroes_C(raiz.left)
        if raiz.value.startswith('C') and raiz.other_values['is_villain'] == False:
            print(raiz.value)
        listar_heroes_C(raiz.right)

listar_heroes_C(arbol_mcu.root)

# d. Determinar cuántos superhéroes hay en el árbol
def contar_heroes(raiz):
    if raiz is None:
        return 0
    cantidad = 1 if raiz.other_values['is_villain'] == False else 0
    return cantidad + contar_heroes(raiz.left) + contar_heroes(raiz.right)

print(f"\nD)----Cantidad de héroes: {contar_heroes(arbol_mcu.root)}")

# e. Buscar a Doctor Strange por proximidad y modificar su nombre
print("\nE)--- Buscando Doctor Strange ---")
arbol_mcu.proxy_search('doctor')

arbol_mcu.delete_node('Doctor Strang')
arbol_mcu.insert_node('Doctor Strange', {'is_villain': False})
print("Nombre corregido a Doctor Strange.")

# f. Listar los superhéroes ordenados de manera descendente
# Inorden inverso: Derecha -> Raíz -> Izquierda
print("\nF)--- Héroes descendente ---")
def listar_heroes_desc(raiz):
    if raiz is not None:
        listar_heroes_desc(raiz.right)
        if raiz.other_values['is_villain'] == False:
            print(raiz.value)
        listar_heroes_desc(raiz.left)

listar_heroes_desc(arbol_mcu.root)

# g. Generar un bosque (un árbol de héroes y otro de villanos)
arbol_heroes = BinaryTree()
arbol_villanos = BinaryTree()

def separar_bosque(raiz):
    if raiz is not None:
        if raiz.other_values['is_villain'] == True:
            arbol_villanos.insert_node(raiz.value, raiz.other_values)
        else:
            arbol_heroes.insert_node(raiz.value, raiz.other_values)
        separar_bosque(raiz.left)
        separar_bosque(raiz.right)

separar_bosque(arbol_mcu.root)

# I. Determinar cuántos nodos tiene cada árbol
def contar_nodos(raiz):
    if raiz is None:
        return 0
    return 1 + contar_nodos(raiz.left) + contar_nodos(raiz.right)

print("\nG1)--- Nodos por árbol ---")
print(f"Héroes: {contar_nodos(arbol_heroes.root)}")
print(f"Villanos: {contar_nodos(arbol_villanos.root)}")

# II. Realizar un barrido ordenado alfabéticamente de cada árbol
print("\nG2)---")
print("\n--- Bosque Héroes ---")
arbol_heroes.inorden()

print("\n--- Bosque Villanos ---")
arbol_villanos.inorden()