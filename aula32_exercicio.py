""" Calculadora com while"""

while True:
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    
    numeros_validos = None
    numero_1 = 0
    numero_2 = 0

    try:
    
        numero_1 = float(num1)
        numero_2 = float(num2)
        numeros_validos = True
        
    except:
        
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue
    
    print("Operadores:")
    print("Soma (+)")
    print("Subtração (-)")
    print("Multiplicação (*)")
    print("Divisão (/)")
    
    operador = input('Digite o operador: ')
    
    operadores_permitidos = ('+','-','/','*')
            
    if operador.count(operador[0]) > 1:
        print('Digite apenas um operador.')
        continue
    
    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue
        
    print('Realizando sua conta. Confira o resultado abaixo:')
        
    if operador == '+':
        print(f'{numero_1}+{numero_2} =', numero_1 + numero_2)
    elif operador == '-':
        print(f'{numero_1} - {numero_2} =', numero_1 - numero_2)
    elif operador == '*':
        print(f'{numero_1} * {numero_2} =', numero_1 * numero_2)
    elif operador == '/':
        print(f'{numero_1} / {numero_2} =', numero_1 / numero_2)
    else:
        print('Nunca deveria chegar aqui.')
    
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break