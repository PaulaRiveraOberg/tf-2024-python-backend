FIN = False
registro_llamado = {"frecuencia": None, "motivo": None, "fecha": None}
listado_llamados = []
while not FIN:
    frecuencia = input("Ingrese frecuencia: ")
    if frecuencia == "FIN":
        FIN = True
    else:
        motivo = input("Ingrese motivo: ")
        fecha = input("Ingrese fecha: ")
        registro_llamado["frecuencia"] = frecuencia
        registro_llamado["motivo"] = motivo
        registro_llamado["fecha"] = fecha
        # el error inicial radica en la copia por referencia del diccionario
        listado_llamados.append(registro_llamado.copy())
print(listado_llamados)