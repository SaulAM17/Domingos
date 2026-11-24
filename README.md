# Contando domingos (Project Euler #19)

## Problema
¿Cuántos domingos cayeron en primer día de mes durante el siglo XX
(1 de enero de 1901 al 31 de diciembre de 2000)?

## Datos
- 1 de enero de 1900: lunes.
- Septiembre, abril, junio y noviembre: 30 días; febrero: 28 (29 en bisiestos); los demás: 31.
- Año bisiesto: divisible por 4, salvo siglos no divisibles por 400.

## Solución
Se simula el calendario mes a mes llevando el día de la semana del día 1
de cada mes y se cuentan los domingos.

## Resultado
**171**

## Ejecución
    python solucion.py