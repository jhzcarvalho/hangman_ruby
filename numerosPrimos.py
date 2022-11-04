import time
import math

if __name__ == '__main__':
    num = int(input('Insira até qual numero será testado\n'))

    start_time = time.time()
    listaPrimos = []

    '''
    A lista de primos começará com os numeros 2 adicionado
     - 2 é o unico numero primo que é par
     - outros numeros pares não precisam ser testados 
    '''
    listaPrimos.append(2)
    print(2)
    listaPrimos.append(3)
    print(3)

    for i in range(5, num+1, 2):

        if (i % 1_000_000 == 0):
            print(f'Tempo até aqui {time.time() - start_time}')

        ehPrimo = True
        raiz = math.sqrt(i)

        for j in listaPrimos:
            #print(f'Testando {i} / {j}')

            if j > raiz:
                #print(f'{j} já é maior que a raiz quadrada de {i}')
                break
            elif (i % j) == 0:
                #print(f'{i}/{j} = {i / j}')
                ehPrimo = False
                break

        if ehPrimo:
            print(f'O numero {i} é primo')
            listaPrimos.append(i)

    print(listaPrimos)
    print(f'{time.time() - start_time} segundos')
