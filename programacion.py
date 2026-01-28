entrada:
    - datos por teclado:
        1- Alquilar:
            datos por teclado:
                - DNI
                - numero que identifica bicicleta
                - numero que identifica casco
                
        2- Devolver:
            datos por teclado:
                - nro bicicleta
                - nro casco
                
        3- Cierre del día

proceso:
# dependiendo de la opcion que se elija:
    1- Alquilar:
        - pedir datos por teclado
        - controlar que los elementos no se encuentren ya alquilados
        - si es asi, se agrega el alquiler al archivo csv con todos los
        datos ingresados (dni;nro_bici;nro_casco)
        
    2- Devolver:
        - pedir datos por teclado
        - validar que ambos elementos hayan sido alquilados previamente
        - liberar bicicleta y casco ingresados
        
    3- Cierre del día:
        - en el archivo de alquileres, contar cuantos alquileres tuvo cada
        elemento
        - ordenar este listado de mayor a menor por cant alquileres
        - buscar articulos sin devolver, identificando dni de quien los tiene
        en su poder
        
salida:
    - impresion de ambos listados hechos en opcion 3
    - archivo con todos los alquileres
    
        
    
