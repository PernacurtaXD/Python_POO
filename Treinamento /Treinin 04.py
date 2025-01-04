from unittest.mock import patch

# Usando o mock para simular a entrada
with patch('builtins.input', side_effect=['5', '10', '+']):
    num1 = int(input("Digite um número:"))  # O input simulado vai retornar '5'
    num2 = int(input("Digite mais um número:"))  # O input simulado vai retornar '10'
    operador = input("Agora digite um operador(+,-,/,*):")  # O input simulado vai retornar '+'
    
    def basic_op(operator, value1, value2):
        if operator == '+':
            resultado = value1 + value2
        elif operator == '-':
            resultado = value1 - value2
        elif operator == '*':
            resultado = value1 * value2
        elif operator == '/':
            resultado = value1 / value2
        return resultado 

    calculo = basic_op(operador, num1, num2)
    print("Resultado: {}".format(calculo))
