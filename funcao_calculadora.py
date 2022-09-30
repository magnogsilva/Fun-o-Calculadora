def calculadora():
    while True:
        print('OPERAÇÕES')
        print('1: Soma')
        print('2: Subtração')
        print('3: Multiplicação')
        print('4: Divisão')
        print('0: Sair')
        op = int(input('Digite o Número para a operação correspondente: '))
        if op!=1 and op!= 2 and op!=3 and op!=4 and op!=0:
            print('Essa opção não existe!')
        elif op==0:
            break            
        else:
            n1 = int(input('Digite o primeiro número: '))
            n2 = int(input('Digite o segundo número: ')) 
            if op==1:
                res = n1+n2
                print('A opção escolhida foi a SOMA.')
                print('E o resultado é {}'.format(res))
            elif op==2:
                res = n1-n2
                print('A opção escolhida foi a SUBTRAÇÃO.')
                print('E o resultado é {}'.format(res))
            elif op==3:
                res = n1*n2
                print('A opção escolhida foi a MULTIPLICAÇÃO.')
                print('E o resultado é {}'.format(res))
            elif op==4:
                res = n1/n2
                print('A opção escolhida foi a DIVISÃO.')
                print('E o resultado é {}'.format(res))


calculadora()
