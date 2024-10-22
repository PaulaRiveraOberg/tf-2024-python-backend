# si rut es menos de 10 millones, agregar uno o dos ceros al comienzo del string
# el verificador en lambda retorna 0, o K, o el número calculado dependiendo de las condiciones
# establecidas por el algoritmo del verificador.

verificador = \
    lambda rut: 0 if (11-((int(rut[-1])*2+int(rut[-2])*3+int(rut[-3])*4+int(rut[-4])*5+int(rut[-5])*6+int(rut[-6])*7+int(rut[-7])*2+int(rut[-8])*3)%11)==11) \
    else ("K" if (11-((int(rut[-1])*2+int(rut[-2])*3+int(rut[-3])*4+int(rut[-4])*5+int(rut[-5])*6+int(rut[-6])*7+int(rut[-7])*2+int(rut[-8])*3)%11)==10) \
                else (11-((int(rut[-1])*2+int(rut[-2])*3+int(rut[-3])*4+int(rut[-4])*5+int(rut[-5])*6+int(rut[-6])*7+int(rut[-7])*2+int(rut[-8])*3)%11)))

print(verificador("10111000"))
