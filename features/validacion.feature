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
