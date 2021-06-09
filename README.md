# BIC01: Tercer Taller

Implemente un programe que almacene los [dominios de nivel superior
geográfico](https://es.wikipedia.org/wiki/Dominio_de_nivel_superior_geogr%C3%A1fico) 
en un diccionario, donde las claves sean los paises y los valores los 
dominios respectivos.
Dicho programa debe contar con las siguientes funciones:

1. La función `obtener_dominio(dominio_por_pais, pais)` recibe como parámetros un diccionario
de paises (claves) y dominios (valores) y una cadena de caracteres con el pais a consultar.
   Si `pais` se encuentra en el diccionario `dominio_por_pais`, la función retorna el dominio asociado.
   Caso contrario, retorna `None`:
   
    ```python
    dominios = {"Peru": "pe",
                "Brasil": "br",
                "Chile": "cl"}
    print(obtener_dominio(dominios, "Peru"))  # En consola: pe
    print(obtener_dominio(dominios, "Bolivia")) # En consola: None
    ```

2. La función `mostrar_valores(diccionario)` recibe como parámetro un diccionario donde 
    claves y valores son cadenas de caracteres. Si `diccionario` tiene valores, la función 
    muestra en consola las claves y valores en columnas de **10 caracteres** de longitud.
    En caso el diccionario este vacío, se muestra un mensaje de error.
   
    ```python
    dominios = {"Peru": "pe",
                "Brasil": "br",
                "Chile": "cl"}
    mostrar_valores(dominios) # En consola:
    #Peru:     pe        
    #Brasil:   br        
    #Chile:    cl         
    mostrar_valores({}) # En consola: No hay valores que mostrar.
    ```

3. La función `registrar_dominio(dominio_por_pais, pais, dominio)` recibe como parámetros un diccionario (donde 
   claves y valores son cadenas de caracteres), un pais a registrar y su dominio (ambos cadenas de caracteres).
   La función agrega al diccionario `dominio_por_pais` una entrada de clave `pais` y valor `dominio` **en caso
   el pais no este registrado**. En caso ya este presente, se muestra un mensaje de error.
   
    ```python
    dominios = {"Peru": "pe",
                "Brasil": "br",
                "Chile": "cl"}
    registrar_dominio(dominios, "Colombia", "col")
    mostrar_valores(dominios) # En consola:
    #Peru:     pe        
    #Brasil:   br        
    #Chile:    cl        
    #Colombia: col       
    registrar_dominio(dominios, "Colombia", "col") # En consola: El pais Colombia ya se encuentra registrado con el dominio col.
    ```

4. La función `actualizar_dominio(dominio_por_pais, pais, nuevo_dominio)` recibe como parámetros un diccionario (donde 
   claves y valores son cadenas de caracteres), un pais y su nuevo dominio (ambos cadenas de caracteres).
   La función cambia el valor de la clave `pais`, en el diccionario `dominio_por_pais`, asignándole el valor de
   `nuevo_dominio` **en caso la clave este presente en el diccionario**. Si el pais no esta presente, se 
   muestra un mensaje de error:
   
    ```python
    dominios = {"Peru": "per",
                "Brasil": "br",
                "Chile": "cl"}
    actualizar_dominio(dominios, "Peeru", "pe") # En consola: El pais Peeru no esta registrado.
    actualizar_dominio(dominios, "Peru", "pe")
    mostrar_valores(dominios)  # En consola:
    #Peru:     pe        
    #Brasil:   br        
    #Chile:    cl        
   ```
5. La función `generar_pais_por_dominio(diccionario_dominios)` recibe como parámetro un diccionario (donde 
   claves y valores son cadenas de caracteres). La función retorna un nuevo diccionario, donde las claves son 
   los dominios (en mayúsculas) y los valores los paises (en mayúsculas) de `diccionario_dominios`.
   
    ```python
   dominios = {"Peru": "per",
               "Brasil": "br",
               "Chile": "cl"}
    print(generar_pais_por_dominio(dominios)) # En consola: {'PER': 'PERU', 'BR': 'BRASIL', 'CL': 'CHILE'}
    ```
   
Complete las funciones definidas en `dominios.py` de acuerdo a lo especificado en este documento.