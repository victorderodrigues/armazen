print ('Ei, bora lá!')
print ('Deixa eu te conhecer melhor, beleza?\n')

nome = input('Me conta, não é fofoca, mas diz teu nome ai\n')

idade = int(input('\nFiquei sabendo que estas perto do inss já, né? Diz tua idade\n'))

mensagem = (f'\nOlha {nome}, chega junto, vi que já se passaram {idade} primaveras')

print (mensagem)

print ('Como te falei, não é fofoca!\n')
print ('Mas boatos que você precisa de ajuda para comprar tinta rsrs, deixa eu ajudar!\n')
print ('Vê só, tu sabes o tamanho em metros quadrados?')
print ('Sim? ')
print ('Não? ')
opcao = input('Opção: ')

if opcao == 'não':
    
    print ('\nEntão bora lá, me ajude para eu te ajudar.')
    comprimento = float(input('Me diz o comprimento em metros: '))
    largura = float(input('Agora manda a largura em metros: '))
    
    cm_lg = comprimento*largura
    
    qnt_litros_1 = (cm_lg / 6)           
    qnt_latas_1 = qnt_litros_1 / 4  
    
    qnt_total_1 = int(qnt_latas_1)
    if qnt_latas_1 > int(qnt_latas_1):
        qnt_total_1 += 1  
    valor_unitario_1 = 80.0      
    
    valor_total_1 = qnt_total_1 * valor_unitario_1
    print (f'Você precisa de {qnt_total_1} latas de tinta e o valor que você pagará sera R$ {valor_total_1}')

elif opcao == 'sim':
    print ('Ai que bom, facilitou as coisas')    
    metros = float(input('Informe aqui quantos metros quadrados: '))

    qnt_litros_2 = (metros / 6)           
    qnt_latas_2 = qnt_litros_2 / 4  
    
    qnt_total_2 = int(qnt_latas_2)
    if qnt_latas_2 > int(qnt_latas_2):
        qnt_total_2 += 1   
        
    valor_unitario_2 = 80.0              
    valor_total_2 = qnt_total_2 * valor_unitario_2

    print (f'Você precisa de {qnt_total_2} latas de tinta e o valor que você pagará sera R$ {valor_total_2}\n')
    
print ('\nE ai? Tas ruim de calculo né?')
print ('Deixa eu te ajudar nisso também')

numero_1 = int(input ('Diga ai o primeiro número, sem ponto visse!\n'))
numero_2 = int(input ('Manda o segundo número, também sem ponto\n'))
numero_3 = float(input ('O ultimo é com ponto, e bora calcular, digita ai:\n'))

calculo_1 = (numero_1*2)+(numero_2/2)
calculo_2 = (numero_1*3)+(numero_3)
calculo_3 = numero_3**3

print ('Então vou te mostrar aos resultado, fechou??')
print (f'O dobro do primeiro número somado a metade do segundo é: {calculo_1}')
print (f'A soma do triplo do primeiro com o terceiro é: {calculo_2}')
print (f'O terceiro número elevado ao cubo é: {calculo_3}')

print ('Satisfeito? Sim ou Claro?')