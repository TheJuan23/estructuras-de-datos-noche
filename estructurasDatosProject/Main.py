#Ejemplo con Tuplas
tupla1 = ()#Tupla vacia
print(tupla1)
tupla2 = ("apple", 2018, "samsung", 4.9, "t", True)
print(tupla2)
print(tupla2[1])
print(tupla2[3])

#Operaciones con Tuplas
tupla3 = ("A", "B", "C", "D")
tupla4 = (1, 2, 3, 4)
#concardenar
tupla5 = tupla3 + tupla4
print(tupla5)
tupla6 = tupla4 * 3
print(tupla6)
#comparar
tupla7 = ("Rojas")
tupla8 = (1,2,3)
tupla9 = ("Rosas")
tupla10 = ("rosas")
print((tupla7, tupla8)<(tupla9, tupla10))
print((tupla7, tupla8)==(tupla9, tupla10))
#Tupla enlazada
tupla11 = (0,1,2,3)
tupla12 = ("A","B","C")
tupla13 = (tupla11,tupla12)
print(tupla13[1][1])
