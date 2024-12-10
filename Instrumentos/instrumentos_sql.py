import sqlite3

class INSTRUMENTOS:
    def __init__(self, ID, Name, Caracteristicas, Precio):
        self.ID = ID
        self.Name = Name
        self.Caracteristicas = Caracteristicas
        self.Precio = Precio

connection = sqlite3.connect("instrumentos.db")
#instrumentos = connection.getInstrumentos()

cursor = connection.cursor()
sql = "SELECT * FROM INSTRUMENTOS"
cursor.execute(sql)

filas = cursor.fetchall()
instrumentos = [INSTRUMENTOS(*f) for f in filas] # unpacking

#Mostrar con los objetos:
for inst in instrumentos:
    print(inst.ID)
    print(inst.Name)
    print(inst.Caracteristicas)
    print(inst.Precio)
connection.commit()

connection.close()