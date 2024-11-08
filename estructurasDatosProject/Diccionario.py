#Ejemplos con diccionarios
diccionario = {}
puertos = {
    22:"SSH",
    23:"Telnet",
    80: "HTTP",
    3306: "MySQl",
    1526: "Oracle"
}
print(puertos)
puertos1 = {
    22: "SSH",
    80: "HTTP"
}
puertos2 = {
    53: "DNS",
    443: "HTTPS"
}
print(puertos1)
puertos1.update(puertos2)
print(puertos1)

# ELiminar un elemento del diccionario
calificaciones = {
    "Alumno1": 5,
    "Alumno2": 4,
    "Alumno3": 3,
    "Alumno4": 2,
}
print(calificaciones)
del calificaciones["Alumno3"] #Eliminar una pareja del diccionario
print(calificaciones)

# Iterar un diccionario
dicPuertos= {
    22:"SSH",
    23:"Telnet",
    80: "HTTP",
    3306: "MySQl",
    1526: "Oracle"
}
for x,y in dicPuertos.items():
    print(x,"--->",y)