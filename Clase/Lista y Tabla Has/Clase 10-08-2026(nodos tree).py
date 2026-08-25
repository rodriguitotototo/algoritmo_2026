# Estructura de un árbol
#
# Un árbol es una estructura jerárquica formada por nodos conectados entre sí.
# Cada nodo puede contener información y puede estar relacionado con otros nodos
# mediante conexiones llamadas ramas.
#
# Elementos principales:
# - Raíz: es el nodo inicial del árbol. Es el único nodo que no tiene padre.
# - Hijo: es un nodo que está directamente debajo de otro nodo.
# - Hermano: son los nodos que tienen el mismo padre y se encuentran en el mismo nivel.
# - Descendientes: son todos los nodos que se encuentran por debajo de un nodo.
# - Ancestros: son los nodos que están por encima de un nodo, hasta llegar a la raíz.
# - Hoja: es un nodo que no tiene hijos.
# - Grado de un nodo: es la cantidad de subárboles o hijos que tiene ese nodo.
#   El grado máximo del árbol es la mayor cantidad de hijos que tiene cualquier nodo.
# - Rama: es la línea o enlace que une dos nodos.
# - Camino: es la secuencia de nodos que permite ir de un nodo a otro.
#   En un árbol, el camino entre dos nodos es único porque cada nodo tiene un solo padre.
#
# Importante:
# - Un nodo no puede tener dos padres.
# - Por eso, existe una única forma de llegar a cada nodo desde la raíz.
# - Cada nodo puede tener varios hijos, pero solo un padre.
#
# ¿Dónde se usan los árboles?
# Los árboles se utilizan en muchas áreas de la informática, por ejemplo:
# - En los sistemas operativos, para organizar directorios y archivos.
# - En estructuras de datos para búsquedas y ordenamiento.
# - En índices, donde ayudan a localizar información rápidamente.
#
# En los sistemas operativos, los árboles no se usan principalmente para almacenar
# datos directamente, sino como una forma de organizar y acceder a ellos de manera
# eficiente. Su función principal es actuar como un índice o una estructura de
# navegación, por ejemplo, para ubicar archivos dentro de carpetas.
#
# En resumen, un árbol permite representar relaciones jerárquicas de forma clara,
# ordenada y eficiente, y es una de las estructuras más útiles en programación.
#
# Árboles binarios y ABB
#
# Un árbol binario es un caso particular de árbol en el que cada nodo puede tener
# como máximo dos hijos: un hijo izquierdo y un hijo derecho. Por eso, el grado
# máximo del árbol es 2.
#
# En un árbol binario de búsqueda (ABB), la regla de orden es la siguiente:
# - todo nodo del subárbol izquierdo es menor que el nodo padre;
# - todo nodo del subárbol derecho es mayor que el nodo padre.
#
# Esto significa que cada nodo tiene una posición lógica dentro del árbol y que la
# estructura conserva un orden fijo sin necesidad de reordenar los elementos cada vez
# que se realiza una búsqueda o un recorrido.
#
# Los recorridos más comunes son:
# - Preorden: raíz, izquierdo, derecho.
# - Inorden: izquierdo, raíz, derecho.
# - Postorden: izquierdo, derecho, raíz.
#
# Cuando se hace un barrido del árbol, se recorren todos los nodos siguiendo una
# regla de visita. En un ABB, el recorrido permite listar o procesar los datos de
# forma ordenada, especialmente cuando se usa el recorrido inorden.
#
# El árbol no necesita "ordenar" los elementos Manualmente, porque la propia
# estructura del ABB ya impone el orden por la relación entre padre e hijos.
#
# Propiedades principales de un árbol binario:
# - cada nodo puede tener hasta dos hijos;
# - existe un único camino desde la raíz hasta cualquier nodo;
# - el subárbol izquierdo contiene valores menores y el derecho valores mayores;
# - permite representar información jerárquica y lógica de manera eficiente.
#
# En la práctica, los árboles binarios son muy útiles para:
# - búsqueda de datos;
# - inserción y eliminación de elementos;
# - ordenamiento y recorrido de información;
# - resolución de problemas matemáticos y algorítmicos.
#
# También se puede observar que un árbol binario tiene propiedades matemáticas:
# - el número máximo de nodos en el nivel i es 2^(i-1);
# - el número máximo de nodos en un árbol binario de altura h es 2^h - 1;
# - un árbol binario está lleno si tiene 2^h - 1 nodos;
# - un árbol binario está completo si los niveles están ocupados de izquierda a
#   derecha, salvo quizás el último.
#
# Sin embargo, si se cargan los datos en un orden que favorece una sola rama, el
# árbol puede quedar desbalanceado. Esto afecta la eficiencia, porque la búsqueda
# puede tardar más en algunos subárboles que en otros.
#
# El peor caso ocurre cuando el árbol se vuelve degenerado, por ejemplo si se
# insertan valores ordenados en forma creciente o decreciente. En ese caso, el
# árbol se comporta casi como una lista y la complejidad de búsqueda se vuelve O(n).
#
# Por eso, se busca mantener el árbol equilibrado para conservar la eficiencia de
# búsqueda, inserción y eliminación en todos los subárboles. Más adelante se
# estudian técnicas de equilibrio para evitar este problema.


# -----------------------------------------------------------------------------
# TDA árbol binario de búsqueda (ABB) en Python
# -----------------------------------------------------------------------------
# En esta estructura cada nodo tiene: informacion, izquierdo y derecho.
# La raíz es el único puntero que necesitamos para acceder al árbol completo.

class NodoArbol:
    def __init__(self, info, izquierdo=None, derecho=None):
        self.info = info
        self.izquierdo = izquierdo
        self.derecho = derecho


def arbol_vacio(raiz):
    """Devuelve True si el árbol no tiene elementos."""
    return raiz is None


def insertar_nodo(raiz, elemento):
    """Inserta un elemento en el ABB. Devuelve la nueva raíz."""
    if raiz is None:
        return NodoArbol(elemento)

    if elemento < raiz.info:
        raiz.izquierdo = insertar_nodo(raiz.izquierdo, elemento)
    elif elemento > raiz.info:
        raiz.derecho = insertar_nodo(raiz.derecho, elemento)
    else:
        # Si el valor ya existe, no se duplica.
        return raiz

    return raiz


def buscar(raiz, clave):
    """Busca la primera coincidencia de la clave y devuelve el nodo encontrado."""
    if raiz is None or raiz.info == clave:
        return raiz

    if clave < raiz.info:
        return buscar(raiz.izquierdo, clave)
    return buscar(raiz.derecho, clave)


def reemplazar(raiz):
    """Función interna. Busca el nodo más a la derecha del subárbol izquierdo."""
    if raiz.derecho is None:
        return raiz, raiz.izquierdo

    nodo, hijo = reemplazar(raiz.derecho)
    raiz.derecho = hijo
    return nodo, raiz


def eliminar_nodo(raiz, clave):
    """Elimina la clave indicada y devuelve la nueva raíz del árbol."""
    if raiz is None:
        return None

    if clave < raiz.info:
        raiz.izquierdo = eliminar_nodo(raiz.izquierdo, clave)
        return raiz

    if clave > raiz.info:
        raiz.derecho = eliminar_nodo(raiz.derecho, clave)
        return raiz

    # Caso 1: nodo hoja
    if raiz.izquierdo is None and raiz.derecho is None:
        return None

    # Caso 2: solo un hijo
    if raiz.izquierdo is None:
        return raiz.derecho
    if raiz.derecho is None:
        return raiz.izquierdo

    # Caso 3: dos hijos. Se reemplaza por el mayor del subárbol izquierdo.
    nodo_reemplazo, raiz.izquierdo = reemplazar(raiz.izquierdo)
    raiz.info = nodo_reemplazo.info
    return raiz


def preorden(raiz):
    """Recorrido preorden: raíz, izquierdo, derecho."""
    if raiz is not None:
        print(raiz.info, end=' ')
        preorden(raiz.izquierdo)
        preorden(raiz.derecho)


def inorden(raiz):
    """Recorrido inorden: izquierdo, raíz, derecho."""
    if raiz is not None:
        inorden(raiz.izquierdo)
        print(raiz.info, end=' ')
        inorden(raiz.derecho)


def postorden(raiz):
    """Recorrido postorden: izquierdo, derecho, raíz."""
    if raiz is not None:
        postorden(raiz.izquierdo)
        postorden(raiz.derecho)
        print(raiz.info, end=' ')


def por_nivel(raiz):
    """Recorrido por niveles usando cola."""
    if raiz is None:
        print('Árbol vacío')
        return

    cola = [raiz]
    while cola:
        nodo = cola.pop(0)
        print(nodo.info, end=' ')
        if nodo.izquierdo is not None:
            cola.append(nodo.izquierdo)
        if nodo.derecho is not None:
            cola.append(nodo.derecho)


# Ejemplo de uso:
# raiz = None
# raiz = insertar_nodo(raiz, 50)
# raiz = insertar_nodo(raiz, 30)
# raiz = insertar_nodo(raiz, 70)
# raiz = insertar_nodo(raiz, 20)
# raiz = insertar_nodo(raiz, 40)
# raiz = insertar_nodo(raiz, 60)
# raiz = insertar_nodo(raiz, 80)
#
# print('Preorden:')
# preorden(raiz)
# print('\nInorden:')
# inorden(raiz)
# print('\nPostorden:')
# postorden(raiz)
# print('\nPor nivel:')
# por_nivel(raiz)
# print('\nBuscar 40 ->', buscar(raiz, 40))
# raiz = eliminar_nodo(raiz, 30)
# print('\nDespués de eliminar 30:')
# inorden(raiz)


# -----------------------------------------------------------------------------
# Resumen conceptual del TDA ABB
# -----------------------------------------------------------------------------
# El árbol binario de búsqueda es una estructura jerárquica donde cada nodo
# almacena una clave y dos enlaces a subárboles: izquierdo y derecho.
#
# Reglas fundamentales:
# - Todo valor del subárbol izquierdo es menor que la raíz.
# - Todo valor del subárbol derecho es mayor que la raíz.
# - Cada nodo tiene un único padre y hay un único camino desde la raíz hasta él.
#
# Operaciones principales:
# - insertar_nodo(raiz, elemento): agrega un elemento respetando la regla de orden.
# - eliminar_nodo(raiz, clave): elimina un valor, reorganizando el árbol.
# - buscar(raiz, clave): localiza un elemento del árbol.
# - preorden, inorden, postorden, por_nivel: recorren el árbol según distintas
#   reglas de visita.
#
# La ventaja de un ABB es que permite buscar, insertar y eliminar en forma
# eficiente, siempre que el árbol permanezca razonablemente balanceado.
# -----------------------------------------------------------------------------
