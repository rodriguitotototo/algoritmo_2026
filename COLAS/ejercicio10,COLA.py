
class Nodo:
    def __init__(self, info):
        self.info = info
        self.sig = None

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None

    def arribo(self, dato):
        nuevo = Nodo(dato)
        if self.frente is None:
            self.frente = nuevo
            self.final = nuevo
        else:
            self.final.sig = nuevo
            self.final = nuevo

    def atencion(self):
        if self.frente is None:
            return None
        dato = self.frente.info
        self.frente = self.frente.sig
        if self.frente is None:
            self.final = None
        return dato

    def esta_vacia(self):
        return self.frente is None

class Pila:
    def __init__(self):
        self.cima = None

    def apilar(self, dato):
        nuevo = Nodo(dato)
        nuevo.sig = self.cima
        self.cima = nuevo

    def desapilar(self):
        if self.cima is None:
            return None
        dato = self.cima.info
        self.cima = self.cima.sig
        return dato

    def esta_vacia(self):
        return self.cima is None


# Funciones del Ejercicio

def mostrar_cola(cola):
    cola_aux = Cola()
    while not cola.esta_vacia():
        notif = cola.atencion()
        print(f"Hora: {notif[0]} | App: {notif[1]} | Mensaje: {notif[2]}")
        cola_aux.arribo(notif)
    
    while not cola_aux.esta_vacia():
        cola.arribo(cola_aux.atencion())


# a)
def eliminar_facebook(cola):
    cola_aux = Cola()
    while not cola.esta_vacia():
        notif = cola.atencion()
        if notif[1] != "Facebook":
            cola_aux.arribo(notif)
    while not cola_aux.esta_vacia():
        cola.arribo(cola_aux.atencion())


# b) 
def mostrar_twitter_python(cola):
    cola_aux = Cola()
    while not cola.esta_vacia():
        notif = cola.atencion()
        
        
        if notif[1] == "Twitter" and "Python" in notif[2]:
            print(f"-> [{notif[0]}] {notif[2]}")
            
        cola_aux.arribo(notif) 
        
    while not cola_aux.esta_vacia():
        cola.arribo(cola_aux.atencion())


# c) 
def notificaciones_en_rango(cola):
    pila_temporal = Pila()
    cola_aux = Cola()
    contador = 0
    
    while not cola.esta_vacia():
        notif = cola.atencion()
        if "11:43" <= notif[0] <= "15:57":
            pila_temporal.apilar(notif)
            contador += 1
        cola_aux.arribo(notif)
        
    while not cola_aux.esta_vacia():
        cola.arribo(cola_aux.atencion())
        
    print(f"Cantidad de notificaciones en el rango: {contador}")
    print("Mostrando contenido de la Pila (Orden LIFO):")
    while not pila_temporal.esta_vacia():
        n_pila = pila_temporal.desapilar()
        print(f"   [{n_pila[0]}] {n_pila[1]}: {n_pila[2]}")


# Carga de datos 

cola_notificaciones = Cola()
datos = [
    ("08:15", "Facebook",  "Juan comentó tu foto"),
    ("09:00", "Twitter",   "Nuevo tweet sobre Python y datos"),
    ("10:20", "Facebook",  "Tienes 3 solicitudes de amistad"),
    ("12:00", "Twitter",   "Curso gratuito de Python disponible"),
    ("13:45", "Twitter",   "Python es genial"),
    ("14:15", "Instagram", "A Pedro le gustó tu historia"),
    ("15:00", "Facebook",  "Cumpleaños de Ana mañana"),
    ("16:00", "Twitter",   "Workshop de programación")
]

for d in datos:
    cola_notificaciones.arribo(d)

print("--- COLA ORIGINAL ---")
mostrar_cola(cola_notificaciones)

print("\n--- PUNTO B (Twitter con Python) ---")
mostrar_twitter_python(cola_notificaciones)

print("\n--- PUNTO C (Pila en rango horario) ---")
notificaciones_en_rango(cola_notificaciones)

print("\n--- PUNTO A (Eliminar Facebook) ---")
eliminar_facebook(cola_notificaciones)
print("Cola final resultante:")
mostrar_cola(cola_notificaciones)