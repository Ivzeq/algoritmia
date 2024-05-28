'''
Extraer un dígito de un número. La función recibe como parámetros dos números enteros, uno será del que se extraiga el dígito y el otro indica qué cifra se desea
obtener. La cifra de la derecha se considera la número 0. Retornar el valor -1 si no existe el dígito solicitado. Tener en cuenta que el número puede ser positivo o
negativo. Ejemplo: extraerdigito(12345, 1) devuelve 4, y extraerdigito(12345, 8) devuelve -1.
'''

def extraer_digito (nInput, extract_number):
    string_number = str(nInput)
    digit_list = []
    position = -1

    for letter in string_number:
        digit_list.append(letter)

    for digit in range (len(string_number)):
        if(digit_list[digit]==str(extract_number)):
            position = digit

    return position

numero_evaluado = int(input('Ingrese un numero a recorrer:'))
numero_a_extraer = int(input('Ingrese un numero a extraer:'))

print(extraer_digito(numero_evaluado, numero_a_extraer))