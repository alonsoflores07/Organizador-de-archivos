import os
import shutil

def organizar():

# Explicación para el usuario
    print("Introduce la ruta completa de la carpeta que quieres organizar.")
    print("Ejemplo: C:/Users/tu_usuario/Downloads")
    print("Evita usar comillas, espacios al final, o barras invertidas simples (usa / o doble \\)\n")

#Pide al usuario la ruta de carpeta que quiere organizar, si la introduce marca error y pide que la vuelva a ingresar
while True:
    carpeta_origen = input("Ruta de la carpeta (o escribe 'salir' para terminar):\n").strip()
    if carpeta_origen.lower() == "salir":
        print("Organización cancelada por el usuario.")
        exit()
    elif os.path.exists(carpeta_origen):
        break
    else:
        print(f"\n La ruta '{carpeta_origen}' no existe. Intenta de nuevo o escribe 'salir' para terminar.\n")


# Preguntar si quiere activar modo simulación
while True:
    respuesta_simulacion = input("¿Quieres activar el modo simulación? (si/no):\n").strip().lower()
    if respuesta_simulacion.startswith("s"):
        simulacion = True
        break
    elif respuesta_simulacion.startswith("n"):
        simulacion = False
        break
    else:
        print("Respuesta no válida. Por favor escribe 'sí' o 'no'.")

# Diccionario de tipos de archivo
tipos = {
    "Imágenes": [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".doc", ".docx", ".txt", ".pdf"],
    "Presentaciones": [".ppt", ".pptx"],
    "Hojas de cálculo": [".xls", ".xlsx", ".csv"],
    "Ejecutables": [".exe", ".msi"],
    "Comprimidos": [".zip", ".rar", ".7z"],
    "Otros": [".py",]
}
# Inicializar contador por categoría
contador = {categoria: 0 for categoria in tipos}

# Crear carpetas si no existen
for categoria in tipos:
    ruta_destino = os.path.join(carpeta_origen, categoria)
    if not os.path.exists(ruta_destino):
        os.makedirs(ruta_destino)

# Obtener lista de archivos ordenada alfabéticamente
archivos = sorted(os.listdir(carpeta_origen))


# Organizar archivos
for archivo in archivos:
    ruta_archivo = os.path.join(carpeta_origen, archivo)
    if os.path.isfile(ruta_archivo):
        extension = os.path.splitext(archivo)[1].lower()
        movido = False
        for categoria, extensiones in tipos.items():
            if extension in extensiones:
                destino = os.path.join(carpeta_origen, categoria, archivo)
                if simulacion:
                    print(f"[SIMULACIÓN] Mover '{archivo}' a '{categoria}'")
                else:
                     shutil.move(ruta_archivo, destino)
                contador[categoria] += 1
                movido = True
                break
        if not movido:
            destino = os.path.join(carpeta_origen, "Otros", archivo)
            if simulacion:
                print(f"[SIMULACIÓN] Mover '{archivo}' a 'Otros'")
            else:
                 shutil.move(ruta_archivo, destino)
            contador["Otros"] += 1

#Mostrar resumen final
print("\nOrganización completada. Resumen:")
for categoria, cantidad in contador.items():
    print(f"{categoria}: {cantidad} archivo(s) movido(s)")

if simulacion:
    print("\n[SIMULACIÓN] No se movió ningún archivo realmente.")

# Preguntar si quiere organizar otra carpeta
respuesta_repetir = input("\n¿Quieres organizar otra carpeta? (si/no):\n").strip().lower()
if respuesta_repetir.startswith("s"):
    print("\n Reiniciando el organizador...\n")
    os.system("python " + __file__)  # Vuelve a ejecutar el script
else:
    print("\n Organización finalizada. ¡Buen trabajo!")

