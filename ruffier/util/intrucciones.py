#PANTALLA 1 - PANTALLA PRINCIPAL
titulo = "Bienvenido Al Programa de Control de Salud"

explicacion_pantalla_inicial = """
El Test de Ruffier es una prueba sencilla que permite valorar la capacidad de recuperación del corazón.

Procedimiento:
- Permanecer en reposo durante 5 minutos.
- Medir el pulso en reposo durante 15 segundos (P0).
- Realizar 30 sentadillas en 45 segundos.
- Medir el pulso inmediatamente después del esfuerzo (P1).
- Un minuto después, medir nuevamente el pulso (P2).

Con estas mediciones se calcula el Índice de Ruffier, que indica la condición física:
- Índice bajo → buena condición física.
- Índice alto → fatiga rápida y baja tolerancia al esfuerzo.
"""

#PANTALLA 2 - PULSO DE REPOSO
instruccion_pantalla_pulso_reposo = "Mide tu pulso durante 15 segundos"

#PANTALLA 3 - SENTADILLAS
instruccion_pantalla_sentadillas = "Ahora realiza 30 sentadillas en 45 segundos"

#PANTALLA 4 - PULSO ESFUERZO
instruccion_pantalla_esfuerzo = """
Ahora vas a realizar dos tomas de pulso:

1- Tomate el pulso ahora mismo durante 15 segundos y escribe el resultado en P1
2- Espera 45 segundos, y vuelve a tomar el pulso. Esta vez escribe el resultado en P2
"""

#PANTALLA 5 - RESULTADO

def texto_resumen(nombre, edad, p0, p1, p2, indice):
    texto = (
        f"Nombre: {nombre}\n"
        f"Edad: {edad}\n"
        f"Pulso en estado de reposo P0: {p0}\n"
        f"Pulso luego del esfuerzo P1: {p1}\n"
        f"Pulso luego de la recuperación P2: {p2}\n\n"
        f"INDICE DE RUFFIER: {indice}"
    )
    return texto
