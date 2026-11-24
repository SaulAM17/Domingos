def bisiesto(a):
    return a % 4 == 0 and (a % 100 != 0 or a % 400 == 0)

dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dia = 1

dia = (dia + 365) % 7

contador = 0
for año in range(1901, 2001):
    for mes in range(12):
        if dia == 0:
            contador += 1
        d = dias_mes[mes] + (1 if mes == 1 and bisiesto(año) else 0)
        dia = (dia + d) % 7

print(contador)