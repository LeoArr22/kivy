def validar_datos(nombre, edad, p0, p1, p2):
    """
    Valida los datos ingresados. 
    Lanza ValueError si algo es inválido.
    """

    if not nombre.strip():
        raise ValueError("El nombre no puede estar vacío.")

    try:
        edad = int(edad)
    except ValueError:
        raise ValueError("La edad debe ser un número entero.")

    if edad <= 0:
        raise ValueError("La edad debe ser mayor que cero.")

    try:
        p0, p1, p2 = int(p0), int(p1), int(p2)
    except ValueError:
        raise ValueError("Los valores de pulso deben ser números enteros.")

    if any(v <= 0 for v in (p0, p1, p2)):
        raise ValueError("Los pulsos deben ser mayores que cero.")

    return nombre, edad, p0, p1, p2
