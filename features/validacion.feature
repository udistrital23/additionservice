
================================  SUMA  ================================
# language: es
Característica: Suma de números enteros no negativos en base 10

  Escenario: Suma exitosa de dos enteros positivos
    Dado los numeros enteros 15 y 25
    Cuando realizo la suma
    Entonces el resultado debe ser 40

 Escenario: Intento de suma con un numero negativo
    Dado los numeros enteros -5 y 10
    Cuando intento realizar la suma
    Entonces se lanza una excepcion de "Ambos numeros deben ser enteros no negativos"


================================  DIVISION  ================================
 # language: es
Característica: Division de dos numeros no negativos en base 10
  
  Escenario: Division exitosa de dos numeros positivos
    Dado los numeros 10 y 5
    Cuando realizo la division
    Entonces el resultado debe ser 2

  Escenario: Intento de division por cero
    Dado los numeros 10 y 0
    Cuando intento realizar la division
    Entonces se lanza una excepcion de "No se puede dividir por cero"

  Escenario: Intento de division con dividendo negativo
    Dado los numeros -10 y 5
    Cuando intento realizar la division
    Entonces se lanza una excepcion de "Los numeros deben ser positivos"

  Escenario: Intento de division con divisor negativo
    Dado los numeros 10 y -5
    Cuando intento realizar la division
    Entonces se lanza una excepcion de "Los numeros deben ser positivos"


================================  MULTIPLICACION  ================================
# language: es
Característica: Multiplicacion de dos numeros enteros no negativos en base 10
 
  Escenario: Multiplicacion exitosa de dos enteros positivos
    Dado los numeros enteros 7 y 8
    Cuando realizo la multiplicacion
    Entonces el resultado debe ser 56

  Escenario: Intento de multiplicacion con un numero negativo
    Dado los numeros enteros -5 y 10
    Cuando intento realizar la multiplicacion
    Entonces se lanza una excepcion de "Ambos numeros deben ser enteros positivos"

================================  RESTA  ================================
# language: es
Característica: Resta de dos numeros enteros no negativos en base 10
  
  Escenario: Resta exitosa con resultado positivo
    Dado los numeros enteros 20 y 5
    Cuando realizo la resta
    Entonces el resultado debe ser 15

  Escenario: Intento de resta que produce un resultado negativo
    Dado los numeros enteros 5 y 20
    Cuando intento realizar la resta
    Entonces se lanza una excepcion de "El resultado de la resta no puede ser negativo"

  Escenario: Intento de resta con un numero negativo en la entrada
    Dado los numeros enteros 10 y -2
    Cuando intento realizar la resta
    Entonces se lanza una excepcion de "Ambos numeros deben ser enteros no negativos"


================================  BASECONVERTER  ================================
# language: es
Característica: Conversion de numero entero de Base B a Base 10
  
  Escenario: Conversion exitosa de un numero octal (Base 8)
    Dado el numero "37" en base 8
    Cuando realizo la conversion a base 10
    Entonces el resultado debe ser 31

  Escenario: Conversion exitosa de un numero decimal (Base 10)
    Dado el numero "123" en base 10
    Cuando realizo la conversion a base 10
    Entonces el resultado debe ser 123

  Escenario: Intento de conversion con numero negativo
    Dado el numero "-101" en base 2
    Cuando intento realizar la conversion a base 10
    Entonces se lanza una excepcion de "El numero debe ser un entero no negativo"

  Escenario: Intento de conversion con numero flotante
    Dado el numero 410.1" en base 5
    Cuando intento realizar la conversion a base 10
    Entonces se lanza una excepcion de "El numero debe ser un entero no negativo"

  Escenario: Intento de conversion con base menor a 2
    Dado el numero "101" en base 1
    Cuando intento realizar la conversion a base 10
    Entonces se lanza una excepcion de "La base debe ser un entero entre 2 y 10"

  Escenario: Intento de conversion con base mayor a 10
    Dado el numero "101" en base 11
    Cuando intento realizar la conversion a base 10
    Entonces se lanza una excepcion de "La base debe ser un entero entre 2 y 10"

  Escenario: Intento de conversion con digito invalido para la base
    Dado el numero "201" en base 2
    Cuando intento realizar la conversion a base 10
    Entonces se lanza una excepcion de "El numero contiene digitos invalidos para la base 2"


================================  FORMATTER  ================================
# language: es
Característica: Conversion de numero entero de Base 10 a Base B
  
  Escenario: Conversion exitosa de decimal a binario (Base 2)
    Dado el numero en base 10 es 13
    Cuando realizo la conversion a la base 2
    Entonces el resultado debe ser "1101"

  Escenario: Conversion exitosa de decimal a octal (Base 8)
    Dado el numero en base 10 es 31
    Cuando realizo la conversion a la base 8
    Entonces el resultado debe ser "37"

  Escenario: Conversion exitosa de decimal a decimal (Base 10)
    Dado el numero en base 10 es 99
    Cuando realizo la conversion a la base 10
    Entonces el resultado debe ser "99"

  Escenario: Conversion exitosa del numero cero a cualquier base
    Dado el numero en base 10 es 0
    Cuando realizo la conversion a la base 5
    Entonces el resultado debe ser "0"

 Escenario: Intento de conversion con numero flotante
    Dado el numero en base 10 es 15.5
    Cuando intento realizar la conversion a la base 2
    Entonces se lanza una excepcion de "El numero debe ser un entero no negativo"

  Escenario: Intento de conversion con base de destino menor a 2
    Dado el numero en base 10 es 10
    Cuando intento realizar la conversion a la base 1
    Entonces se lanza una excepcion de "La base de destino debe ser un entero entre 2 y 10"

  Escenario: Intento de conversion con base de destino mayor a 10
    Dado el numero en base 10 es 9
    Cuando intento realizar la conversion a la base 11
    Entonces se lanza una excepcion de "La base de destino debe ser un entero entre 2 y 10"
