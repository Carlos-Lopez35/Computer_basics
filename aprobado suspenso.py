nota=int(input("Pon tu nota de entre 0 a 100"))
asistencia= int(input("Pon el número de clases a las que has asistido"))
if nota>=70 and asistencia>=32:
    print("Has aprobado")
else:
    print("Has suspendido")