# CALCULADORA IVA

## 1. Breve descripción para el cliente (manual de uso)
#### 1.1 Nombre: 
- Programa para calcular IVA
#### 1.2 Objetos: 
- usuario, el precio sin IVA y porcentaje IVA
#### 1.3 Paso:
Paso | Instrución
---  | ---------------------------- 
1    | Introducir usuario 
2    | Introducir el precio sin IVA
3    | Introducir porcentaje IVA
4    | Enter
 
#### 1.4 Descripción
- Programa va a calcular IVA y precio con IVA automaticamente con su historico.
#### 1.5 Resultado:

- CALCULADORA IVA
***************
Usuario: Ana
____________

- SUMA IVA
____________
Precio sin IVA €: 36
____________
Porcentaje de IVA %: 12
____________

- RESULTADO:
____________
Precio sin IVA: 36.0 €
____________
IVA: 4.32 €
____________
Precio con IVA: 40.32 €
____________

- Historicos: Usuario - Precio - Porcentaje IVA
____________
['Ana', 36.0, 12.0]

## 2. Mis pruebas
prueba | usuario | precio | porcentaje IVA | IVA  | precio con IVA | Espero | Actual | Exito
-------| ------- | ------ | ---------------|------| ---------------| ------ | ------ | -----  
1      |   -     |    34  |       12       | 4.08 |       38.08    | 38.08  | 38.08  | IVA correcto pero falta la historia de usuario
2      |   Ana   |    45  |       21       | 9.45 |       54.45    | 54.45  | 54.45  | Sucess 
3      |   Ana   |    34  |       21       | 7.14 |       41.14    | 41.14  | 41.14  | Sucess  

## 3. Método
* COMO un cliente de una empresa de asesoramiento
* QUIERO hacer una calculadora IVA para ese cliente
* PARA calcular el precio con IVA y enseñar a cliente el resultado como una tabla con IVA y precio con IVA, utilizando Python.