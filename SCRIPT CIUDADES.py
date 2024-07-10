def calcular_distancia(ciudad_origen, ciudad_destino):
    # Distancias inventadas entre Santiago y Buenos Aires
    if ciudad_origen.lower() == "santiago" and ciudad_destino.lower() == "buenos aires":
        distancia_km = 1400  # Aproximadamente 1400 km
        distancia_millas = 870  # Aproximadamente 870 millas
        return distancia_km, distancia_millas
    else:
        return None, None

def obtener_duracion_viaje(distancia_km, medio_transporte):
    if medio_transporte == "auto":
        velocidad_kmh = 80  # velocidad promedio en km/h
    elif medio_transporte == "avion":
        velocidad_kmh = 800  # velocidad promedio en km/h
    elif medio_transporte == "tren":
        velocidad_kmh = 100  # velocidad promedio en km/h
    else:
        return None
    
    duracion_horas = distancia_km / velocidad_kmh
    return duracion_horas

def main():
    while True:
        ciudad_origen = input("Ingrese la Ciudad de Origen (o 's' para salir): ")
        if ciudad_origen.lower() == 's':
            break

        ciudad_destino = input("Ingrese la Ciudad de Destino: ")
        if ciudad_destino.lower() == 's':
            break

        medio_transporte = input("Ingrese el medio de transporte (auto, avion, tren): ").lower()
        if medio_transporte == 's':
            break

        distancia_km, distancia_millas = calcular_distancia(ciudad_origen, ciudad_destino)
        
        if distancia_km and distancia_millas:
            duracion_viaje = obtener_duracion_viaje(distancia_km, medio_transporte)
            if duracion_viaje is not None:
                narrativa = f"El viaje desde {ciudad_origen} hasta {ciudad_destino} cubre una distancia de {distancia_km} km (o {distancia_millas} millas) y toma aproximadamente {duracion_viaje:.2f} horas en {medio_transporte}."
                
                print(f"""
                Descripción                 Valor
                ----------------------------------
                Ciudad de Origen            {ciudad_origen}
                Ciudad de Destino           {ciudad_destino}
                Distancia (km)              {distancia_km}
                Distancia (millas)          {distancia_millas}
                Duración del viaje (horas)  {duracion_viaje:.2f}
                """)
                print(narrativa)
            else:
                print("Medio de transporte no válido.")
        else:
            print("No se pudieron calcular las distancias para las ciudades ingresadas. Intente con 'Santiago' y 'Buenos Aires'.")

if __name__ == "__main__":
    main()
