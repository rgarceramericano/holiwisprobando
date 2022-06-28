#comentarios
#lineas que no se jecutan y sirven para revisar el codigo

'''hola k hace'''

#constantes: son datos FIJOS, que no deben de ser cambiados

pie=3.14

#variables: son datos que pueden o no cambiar con el tiempo

fecha=4
fecha=5

#print(): nos permite mandar informacion a la consola

print(pie)

print(fecha)

fecha=13

print(fecha)

print(7)

print('hola k hace')
print("no lo ce")

print("el valor de pi es: ", pie)
print("hoy es el dia", fecha, "de enero")

print(3+4)
print(3-9)

#operadores matematicos
# + suma -resta *multipl /div

a=2890
b=45

suma=a+b
resta=a-b
mult=a*b
div=b/a

print(suma)
print(resta)
print(mult)
print(div)

#ciclos son fragmentos de codigo que se repiten un numero de veces

#while permite reptir un codigo mientras que una condicion se confirme

# while(condicion):
#     codigo
#      codigo   


#identacion: le avisa a la estrucutra si una linea es de esa estructura

#cuando un codigo se cicla puede ser a proposito o sin querer

a=2
while (a==2):
	print('hola mundo')
	a=a-1

#operadores logicos:

#a>b a mayor que b
#a<b a menor que b
#a==b a es identico b
#a>=b a es mayor o igual que b
#a<=b a es menor que igual b
#a!=b a diferente de b

a=0
while(a<=5):
	print('salimos temprano?')
	a=a+1
print('ya pueden irse...')