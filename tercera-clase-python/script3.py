lista_edades = [15, 22, 17, 30, 65, 45, 70, 19]
for i in lista_edades:
    if i < 18:
        continue
    elif i >= 65:
        break
    print(i)

contador = 0
while contador < 5:
    try:
        float(input('Escribe un numero: '))
        break
    except:
        print('Numero no valido, intentalo de nuevo')
        contador += 1