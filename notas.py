#Positivo
for ele in range(1, 10):
    print(ele)


#Negativo
for ele in range(10, 1, -1):
    print(ele)

#Variaável auxiliar

soma = 0
for ele in range(0, 10):
    numero = int(input('Digite um número: '))
    soma = numero + soma

    print(f'a soma é {soma}')