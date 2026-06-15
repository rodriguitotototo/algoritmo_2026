

cola_notificaciones = [
    ["08:15", "Facebook",  "Juan comentó tu foto"],
    ["09:00", "Twitter",   "Nuevo tweet sobre Python y datos"],
    ["10:20", "Facebook",  "Tienes 3 solicitudes de amistad"],
    ["12:00", "Twitter",   "Curso gratuito de Python disponible"],
    ["13:45", "Twitter",   "Python supera a Java en popularidad"],
    ["14:15", "Instagram", "A Pedro le gustó tu historia"],
    ["15:00", "Facebook",  "Cumpleaños de Ana mañana"],
    ["16:00", "Twitter",   "Workshop de programación"]
]
for n in cola_notificaciones:
    print(n)
print()

# A) Eliminar todas las notificaciones de Facebook

def eliminar_facebook(cola):
    cola_auxiliar = []

    while len(cola) > 0:
        notificacion = cola.pop(0)
        app = notificacion[1]
        if app != "Facebook":
            cola_auxiliar.append(notificacion)
    while len(cola_auxiliar) > 0:
        cola.append(cola_auxiliar.pop(0))


# B) Mostrar notificaciones de Twitter con 'Python' (sin perder datos)

def mostrar_twitter_python(cola):
    cola_auxiliar = []

    while len(cola) > 0:
        notificacion = cola.pop(0)
        app = notificacion[1]
        mensaje = notificacion[2]

        if app == "Twitter" and "Python" in mensaje:
            print(f"Hora: {notificacion[0]} | Mensaje: {mensaje}")

        cola_auxiliar.append(notificacion)

    while len(cola_auxiliar) > 0:
        cola.append(cola_auxiliar.pop(0))


# C) Pila temporal para notificaciones entre las 11:43 y las 15:57

def notificaciones_en_rango(cola):
    pila_temporal = []
    cola_auxiliar = []
    
    while len(cola) > 0:
        notificacion = cola.pop(0)
        hora = notificacion[0]
        
        if "11:43" <= hora <= "15:57":
            pila_temporal.append(notificacion)
            
        cola_auxiliar.append(notificacion)
        
    while len(cola_auxiliar) > 0:
        cola.append(cola_auxiliar.pop(0))
        
    print(f"Cantidad de notificaciones en la pila: {len(pila_temporal)}")
    
    print("Mostrando contenido de la pila (desde la última que entró):")
    while len(pila_temporal) > 0:
        notif_pila = pila_temporal.pop()
        print(f"[{notif_pila[0]}] {notif_pila[1]}: {notif_pila[2]}")



print("--- PUNTO B: Twitter con 'Python' ---")
mostrar_twitter_python(cola_notificaciones)

print("\n--- PUNTO C: Pila con rango de horas ---")
notificaciones_en_rango(cola_notificaciones)

print("\n--- PUNTO A: Eliminando Facebook ---")
eliminar_facebook(cola_notificaciones)
print()
print("Cola final sin las de Facebook:")
for n in cola_notificaciones:
    print(n)
