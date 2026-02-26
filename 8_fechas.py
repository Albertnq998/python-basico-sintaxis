#ALBERT FRAND NINA QUISPE
#Fechas en python

from datetime import date, time, datetime

# fecha actual
hoy = date.today()
print(hoy)
#Formatear fecha
formateado =  hoy.strftime("%d/%m/%Y")
print(formateado)


#hora actual
fecha_actual = datetime.now()
print(fecha_actual)

#capturar el año
anio = fecha_actual.year
print(anio)

mes = fecha_actual.month
print(mes)

dia = fecha_actual.day
print(dia)

hora = fecha_actual.strftime("%H:%M:%S")
print(hora)

#Formato AM PM
hora_am_pm = fecha_actual.strftime("%I:%M:%S %p")
print(hora_am_pm)