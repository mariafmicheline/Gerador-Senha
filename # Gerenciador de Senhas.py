# Gerenciador de Senhas
from random import choice
import string
opcao = 0
i = 0

print('Bem vindo ao gerador de senha!')
print('Deseja continuar?')
while opcao != 2:
    print(''' [1] Sim
              [2] Não
              [3] Sair
        '''
)
    opcao = int(input('Insira a opção escolhida: '))
    if opcao == 1:
        tamanho = int(input('Quantos dígitos terá a sua senha?'))
        caracteres = string.digits + string.ascii_letters
        senha_segura = ''

        for i in range (tamanho):

            senha_segura += choice(caracteres)
            print('A senha segura gerada é: {}'.format(senha_segura))
        

    else:
        break



    
