# Organizador-de-archivos
Script en Python para organizar archivos por tipo, con modo simulación y validación interactiva.
Este script en Python te ayuda a organizar automáticamente los archivos de una carpeta según su tipo (imágenes, documentos, ejecutables, etc.). Incluye un modo simulación para revisar los cambios antes de ejecutarlos, lo que lo hace seguro y fácil de usar.

Características: 

- 	Clasifica archivos por extensión en carpetas como imágenes, documentos, presentaciones, etc. 
- 	Modo simulación: muestra lo que se movería sin hacer cambios reales.
-  	Validación interactiva de rutas y respuestas del usuario.
-  	Resumen final con conteo de archivos movidos por categoría.
-  	Opción para organizar múltiples carpetas en una sola sesión.

¿Por qué usarlo?

Ideal para profesionales, estudiantes o cualquier persona que tenga carpetas desordenadas (como descargas) y quiera mantenerlas organizadas sin esfuerzo. El modo simulación permite revisar sin riesgo antes de ejecutar.

Requisitos

-  	Python 3.6 o superior
- 	No requiere librerías externas (usa solo "os" y  "shutil")

Cómo usarlo
1. 	Clona el repositorio:
git clone https://github.com/tu_usuario/organizador-de-archivos.git
cd organizador-de-archivos

2. 	Ejecuta el script:
python organizador.py

3. 	Sigue las instrucciones en pantalla:

-  	Ingresa la ruta de la carpeta a organizar.
-  	Elige si deseas activar el modo simulación.
- 	Revisa el resumen final

Ejemplo de organización:

Descargas/
├── Imágenes/
│   └── foto1.jpg
├── Documentos/
│   └── informe.pdf
├── Ejecutables/
│   └── setup.exe
├── Otros/
│   └── script.py
