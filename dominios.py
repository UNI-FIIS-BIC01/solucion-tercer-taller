def obtener_dominio(dominio_por_pais, pais):
    if pais in dominio_por_pais.keys():
        return dominio_por_pais[pais]
    return None


def formatear_cadena(cadena, longitud):
    return (cadena + " " * longitud)[:longitud]


def mostrar_valores(diccionario):
    longitud_columna = 10

    if not diccionario.keys():
        print("No hay valores que mostrar.")

    for clave in diccionario.keys():
        dominio = diccionario[clave]
        print(formatear_cadena(clave + ":", longitud_columna) + formatear_cadena(dominio, longitud_columna))


def registrar_dominio(dominio_por_pais, pais, dominio):
    if obtener_dominio(dominio_por_pais, pais) is None:
        dominio_por_pais[pais] = dominio
    else:
        print(f"El pais {pais} ya se encuentra registrado con el dominio {dominio_por_pais[pais]}.")


def actualizar_dominio(dominio_por_pais, pais, nuevo_dominio):
    if obtener_dominio(dominio_por_pais, pais) is not None:
        dominio_por_pais[pais] = nuevo_dominio
    else:
        print(f"El pais {pais} no esta registrado.")


def generar_pais_por_dominio(diccionario_dominios):
    pais_por_dominio = {}
    for pais in diccionario_dominios.keys():
        dominio = diccionario_dominios[pais]
        pais_por_dominio[dominio.upper()] = pais.upper()

    return pais_por_dominio


if __name__ == "__main__":
    dominios = {"Peru": "per",
                "Brasil": "br",
                "Chile": "cl"}
    print(generar_pais_por_dominio(dominios))
