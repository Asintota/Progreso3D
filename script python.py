import os

# Ruta de la carpeta que contiene las carpetas de archivos HTML a editar
ruta_carpeta_principal = "C:/Users/pablo/Documents/GitHub/Progreso"

# Iterar sobre las carpetas en la ruta principal
for nombre_carpeta in os.listdir(ruta_carpeta_principal):
    if nombre_carpeta.isdigit(): # Solo procesar carpetas con nombres numéricos
        ruta_carpeta = os.path.join(ruta_carpeta_principal, nombre_carpeta)
        # Buscar archivos HTML en la carpeta
        for nombre_archivo in os.listdir(ruta_carpeta):
            if nombre_archivo.endswith(".html"):
                nombre_archivo_sin_extension = os.path.splitext(nombre_archivo)[0]
                ruta_archivo = os.path.join(ruta_carpeta, nombre_archivo)
                # Editar número en las líneas del archivo HTML
                with open(ruta_archivo, "r") as archivo:
                    lineas = archivo.readlines()
                # Cambiar el número en las líneas que deseas
                linea_a_editar1 = 36
                linea_a_editar2 = 37
                linea_a_editar3 = 38
                linea_a_editar4 = 39
                nuevo_valor1 = "val1["+ nombre_archivo_sin_extension +"]"
                nuevo_valor2 = "val2["+ nombre_archivo_sin_extension +"]"
                nuevo_valor3 = "val3["+ nombre_archivo_sin_extension +"]"
                nuevo_valor4 = "val4["+ nombre_archivo_sin_extension +"]"
                lineas[linea_a_editar1-1] = lineas[linea_a_editar1-1].replace("val1[0]", nuevo_valor1)
                lineas[linea_a_editar2-1] = lineas[linea_a_editar2-1].replace("val2[0]", nuevo_valor2)
                lineas[linea_a_editar3-1] = lineas[linea_a_editar3-1].replace("val3[0]", nuevo_valor3)
                lineas[linea_a_editar4-1] = lineas[linea_a_editar4-1].replace("val4[0]", nuevo_valor4)
                with open(ruta_archivo, "w") as archivo:
                    archivo.writelines(lineas)
