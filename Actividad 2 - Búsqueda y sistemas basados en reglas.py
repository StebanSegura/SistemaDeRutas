# Base de conocimiento de rutas
rutas = {
    'ruta1': {'origen': 'A', 'destino': 'B', 'tiempo': 15, 'distancia': 10},
    'ruta2': {'origen': 'A', 'destino': 'C', 'tiempo': 10, 'distancia': 5},
    'ruta3': {'origen': 'C', 'destino': 'B', 'tiempo': 5, 'distancia': 3},
    'ruta4': {'origen': 'A', 'destino': 'D', 'tiempo': 20, 'distancia': 15},
    'ruta5': {'origen': 'D', 'destino': 'B', 'tiempo': 10, 'distancia': 7}
}

def mejor_ruta(origen, destino, criterio='tiempo'):
    rutas_posibles = [ruta for ruta in rutas.values() 
                      if ruta['origen'] == origen and ruta['destino'] == destino]
    
    if not rutas_posibles:
        return None
    
    mejor_opcion = min(rutas_posibles, key=lambda x: x[criterio])
    return mejor_opcion

if __name__ == "__main__":
    # Solicitar entrada del usuario
    origen = input("Introduce el punto de origen: ").strip().upper()
    destino = input("Introduce el punto de destino: ").strip().upper()
    criterio = input("¿Quieres encontrar la mejor ruta por 'tiempo' o 'distancia'? ").strip().lower()
    
    # Validar el criterio
    if criterio not in ['tiempo', 'distancia']:
        print("Criterio no válido. Por favor, elige 'tiempo' o 'distancia'.")
    else:
        resultado = mejor_ruta(origen, destino, criterio)
        
        if resultado:
            if criterio == 'tiempo':
                print(f"La mejor ruta de {origen} a {destino} es: {resultado['tiempo']} minutos, {resultado['distancia']} km.")
            else:
                print(f"La mejor ruta de {origen} a {destino} es: {resultado['distancia']} km, {resultado['tiempo']} minutos.")
        else:
            print(f"No hay ruta disponible de {origen} a {destino}.")