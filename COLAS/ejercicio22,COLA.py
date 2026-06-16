
class Nodo:
    def __init__(self, info):
        self.info = info
        self.sig = None

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamanio = 0

    def arribo(self, dato):
        nuevo = Nodo(dato)
        if self.final is not None:
            self.final.sig = nuevo
        self.final = nuevo
        if self.frente is None:
            self.frente = nuevo
        self.tamanio += 1

    def atencion(self):
        if self.frente is None:
            return None
        dato = self.frente.info
        self.frente = self.frente.sig
        if self.frente is None:
            self.final = None
        self.tamanio -= 1
        return dato

    def esta_vacia(self):
        return self.frente is None

    def en_frente(self):
        if self.frente is not None:
            return self.frente.info
        return None

def mostrar_cola(cola):
    cola_aux = Cola()
    while not cola.esta_vacia():
        personaje, superheroe, genero = cola.atencion()
        print(f"Personaje: {personaje} | Superheroe: {superheroe} | Genero: {genero}")
        cola_aux.arribo((personaje, superheroe, genero))
    while not cola_aux.esta_vacia():
        cola.arribo(cola_aux.atencion())

def cargar_personajes():
    cola = Cola()
    personajes = [
        ("Tony Stark",        "Iron Man",             "M"),
        ("Steve Rogers",      "Capitan America",      "M"),
        ("Natasha Romanoff",  "Black Widow",          "F"),
        ("Bruce Banner",      "Hulk",                 "M"),
        ("Thor Odinson",      "Thor",                 "M"),
        ("Clint Barton",      "Hawkeye",              "M"),
        ("Carol Danvers",     "Capitana Marvel",      "F"),
        ("Scott Lang",        "Ant-Man",              "M"),
        ("Peter Parker",      "Spider-Man",           "M"),
        ("Stephen Strange",   "Doctor Strange",       "M"),
        ("Wanda Maximoff",    "Scarlet Witch",        "F"),
        ("Sam Wilson",        "Falcon",               "M"),
        ("T'Challa",          "Black Panther",        "M"),
        ("Shuri",             "Shuri",                "F"),
        ("Hope Van Dyne",     "The Wasp",             "F"),
    ]
    for p in personajes:
        cola.arribo(p)
    return cola

# Punto A
def buscar_personaje_por_superheroe(cola, nombre_superheroe):
    cola_aux = Cola()
    resultado = None
    while not cola.esta_vacia():
        personaje, superheroe, genero = cola.atencion()
        if superheroe.lower() == nombre_superheroe.lower():
            resultado = personaje
        cola_aux.arribo((personaje, superheroe, genero))
    while not cola_aux.esta_vacia():
        cola.arribo(cola_aux.atencion())
    return resultado

# Punto B
def mostrar_superheroes_femeninos(cola):
    cola_aux = Cola()
    contador = 0
    print("\nSuperheroes femeninos:")
    while not cola.esta_vacia():
        personaje, superheroe, genero = cola.atencion()
        if genero == "F":
            contador += 1
            print(f"{contador}. {superheroe}")
        cola_aux.arribo((personaje, superheroe, genero))
    while not cola_aux.esta_vacia():
        cola.arribo(cola_aux.atencion())
    return contador

# Punto C
def mostrar_personajes_masculinos(cola):
    cola_aux = Cola()
    contador = 0
    print("\nPersonajes masculinos:")
    while not cola.esta_vacia():
        personaje, superheroe, genero = cola.atencion()
        if genero == "M":
            contador += 1
            print(f"{contador}. {personaje}")
        cola_aux.arribo((personaje, superheroe, genero))
    while not cola_aux.esta_vacia():
        cola.arribo(cola_aux.atencion())
    return contador

# Punto D
def buscar_superheroe_por_personaje(cola, nombre_personaje):
    cola_aux = Cola()
    resultado = None
    while not cola.esta_vacia():
        personaje, superheroe, genero = cola.atencion()
        if personaje.lower() == nombre_personaje.lower():
            resultado = superheroe
        cola_aux.arribo((personaje, superheroe, genero))
    while not cola_aux.esta_vacia():
        cola.arribo(cola_aux.atencion())
    return resultado

# Punto E
def mostrar_nombres_con_letra(cola, letra):
    cola_aux = Cola()
    print(f"\nPersonajes/Superheroes que empiezan con {letra}:")
    while not cola.esta_vacia():
        personaje, superheroe, genero = cola.atencion()
        if personaje[0].upper() == letra.upper() or superheroe[0].upper() == letra.upper():
            print(f"Nombre: {personaje} | Superheroe: {superheroe} | Genero: {genero}")
        cola_aux.arribo((personaje, superheroe, genero))
    while not cola_aux.esta_vacia():
        cola.arribo(cola_aux.atencion())

# Punto F
def buscar_personaje(cola, nombre_buscado):
    cola_aux = Cola()
    encontrado = False
    superheroe = None
    while not cola.esta_vacia():
        personaje, superheroe_actual, genero = cola.atencion()
        if personaje.lower() == nombre_buscado.lower():
            encontrado = True
            superheroe = superheroe_actual
        cola_aux.arribo((personaje, superheroe_actual, genero))
    while not cola_aux.esta_vacia():
        cola.arribo(cola_aux.atencion())
    return encontrado, superheroe

# Main
if __name__ == "__main__":
    cola_personajes = cargar_personajes()
    
    print("--- COLA COMPLETA ---")
    mostrar_cola(cola_personajes)

    print("\n--- PUNTO A ---")
    personaje_cm = buscar_personaje_por_superheroe(cola_personajes, "Capitana Marvel")
    print(f"El personaje de Capitana Marvel es: {personaje_cm}")

    print("\n--- PUNTO B ---")
    mostrar_superheroes_femeninos(cola_personajes)

    print("\n--- PUNTO C ---")
    mostrar_personajes_masculinos(cola_personajes)

    print("\n--- PUNTO D ---")
    superheroe_sl = buscar_superheroe_por_personaje(cola_personajes, "Scott Lang")
    print(f"El superheroe de Scott Lang es: {superheroe_sl}")

    print("\n--- PUNTO E ---")
    mostrar_nombres_con_letra(cola_personajes, "S")

    print("\n--- PUNTO F ---")
    encontrada, superheroe_cd = buscar_personaje(cola_personajes, "Carol Danvers")
    if encontrada:
        print(f"Carol Danvers SI esta en la cola. Superheroe: {superheroe_cd}")
    else:
        print("Carol Danvers NO esta en la cola.")