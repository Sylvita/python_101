#Calculadora IVA

print("CALCULADORA IVA")
print("***************")
usuario = input("Usuario: ")
print("\n")
print("SUMA IVA")
precio = float(input("Precio sin IVA €: "))
print("---------------")
por_iva = float(input("Porcentaje de IVA %: "))
print("---------------")
print("RESULTADO:")
print(f"Precio sin IVA: {precio} €")
iva = (precio * por_iva)/100
print(f"IVA: {iva:.2f} €")
precio_iva = precio + iva
print(f"Precio con IVA: {precio_iva:.2f} €")

historicos = [usuario, precio, por_iva]
print("Historicos: Usuario - Precio - Porcentaje IVA")
print(historicos)