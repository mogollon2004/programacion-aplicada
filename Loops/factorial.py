#El programa permite entrar un numero, evaluar si es positivo o negativo a travez de un ciclo si, entonces y a partir de alli calcular su factorial con un ciclo for.
while True:

    value = int(input("Enter a positive integer value: "))
    print("Value: ", value)
    a = isinstance(value, int)
    if a == True and value > 0:
        fact = 1
        for i in range (1, value + 1):
            fact = fact*i            
        print(f'The factorial of {value} is: ', fact)
    else:
        print("Please, enter a positive integer number")
