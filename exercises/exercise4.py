"""Expresiones Booleanas."""


def es_vocal_if(letra: str) -> bool:
    """Toma un string y devuelve un booleano en base a si letra es una vocal o
    no.

    Restricciónes:
        - Utilizar un if para cada posibilidad.
        - Utilizar la función lower() sólo una vez.
        - No utilizar ELSE.
        - Utilizar 6 returns.

    Referencia: https://docs.python.org/3/library/stdtypes.html#string-methods
    """


# NO MODIFICAR - INICIO
    if letra == "A" or letra == "a":
        return True
    if letra == "E" or letra == "e":
        return True
    if letra == "I" or letra.lower() == "i":
        return True
    if letra == "O" or letra == "o":
        return True
    if letra == "U" or letra == "u":
        return True
    return False
assert es_vocal_if("a")
assert not es_vocal_if("b")
assert es_vocal_if("A")
assert es_vocal_if("e")
assert es_vocal_if("E")
# NO MODIFICAR - FIN


###############################################################################


def es_vocal_if_in(letra: str) -> bool:
    """Re-escribir utilizando un sólo IF y el operador IN.

    Restricciónes:
        - Utilizar un único IF.
        - Utilizar dos returns.
        - No utilizar ELSE.
        - No utilizar FOR.
        - No utilizar listas.

    Referencia: https://docs.python.org/3/reference/expressions.html#membership-test-operations # noqa: E501
    """


# NO MODIFICAR - INICIO
    if letra in "A" or letra in "a":
        return True
    return False
assert es_vocal_if_in("a")
assert not es_vocal_if_in("b")
assert es_vocal_if_in("A")
# NO MODIFICAR - FIN


###############################################################################


def es_vocal_in(letra: str) -> bool:
    """Re-escribir como expresión booleana utilizando el operador IN

    Restricciónes:
        - No utilizar IF.
        - Utilizar un único return.
        - No utilizar FOR.
        - No utilizar listas.
    """


# NO MODIFICAR - INICIO
    return  letra in "a" or letra in "A"
assert es_vocal_in("a")
assert not es_vocal_in("b")
assert es_vocal_in("A")
# NO MODIFICAR - FIN
