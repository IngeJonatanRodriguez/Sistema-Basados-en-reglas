# -----------------------------
# Base de conocimiento (reglas)
# -----------------------------
# Representamos conexiones entre estaciones como reglas simples

reglas = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D", "E"],
    "D": ["F"],
    "E": ["F"],
    "F": []
}

# -----------------------------
# Motor de inferencia: búsqueda de rutas
# -----------------------------
def encontrar_ruta(inicio, destino, visitados=None):
    if visitados is None:
        visitados = []

    # agregar la estación actual al recorrido
    visitados.append(inicio)

    # si llegamos al destino, devolvemos la ruta encontrada
    if inicio == destino:
        return [visitados]

    rutas = []
    for siguiente in reglas[inicio]:
        if siguiente not in visitados:  # evitar ciclos
            nuevas_rutas = encontrar_ruta(siguiente, destino, visitados.copy())
            for ruta in nuevas_rutas:
                rutas.append(ruta)

    return rutas

# -----------------------------
# Función para elegir la mejor ruta
# -----------------------------
def mejor_ruta(inicio, destino):
    rutas = encontrar_ruta(inicio, destino)
    if not rutas:
        return None
    # La "mejor" ruta será la más corta
    return min(rutas, key=len)

# -----------------------------
# Programa principal
# -----------------------------
if __name__ == "__main__":
    punto_inicio = "A"
    punto_fin = "F"

    ruta = mejor_ruta(punto_inicio, punto_fin)
    if ruta:
        print(f"La mejor ruta desde {punto_inicio} hasta {punto_fin} es: {ruta}")
    else:
        print(f"No existe ruta desde {punto_inicio} hasta {punto_fin}.")

