primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print('primeiro_valor =', primeiro_valor, 'é maior do que segundo_valor =', segundo_valor)

elif primeiro_valor < segundo_valor:
    print('segundo_valor =', segundo_valor, 'é maior do que primeiro_valor =', primeiro_valor)
    
else:
    print('Os valores são iguais')