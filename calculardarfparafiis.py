from datetime import datetime

proximoMes = (datetime.now().month + 1)

def pegar_mes(mes):
    if mes == 1:
        return 'janeiro'
    elif mes == 2:
        return 'fevereiro'
    elif mes == 3:
        return 'março'
    elif mes == 4:
        return 'abril'
    elif mes == 5:
        return 'maio'
    elif mes == 6:
        return 'junho'
    elif mes == 7:
        return 'julho'
    elif mes == 8:
        return 'agosto'
    elif mes == 9:
        return 'setembro'
    elif mes == 10:
        return 'outubro'
    elif mes == 11:
        return 'novembro'
    elif mes == 12:
        return 'dezembro'

print('-=-' * 20)
print('Realizando lucro/prejuízo com a venda de FIIs')
print('-=-' * 20)

precoMedio = float(input('Qual seu Preço Médio do FII? ').replace(',', '.'))
quantidadeDeCotas = int(input('Quantas cotas você vendeu? '))
valorDeVenda = float(input('Qual valor da cota no momento da venda? ').replace(',', '.'))
imposto = (valorDeVenda - precoMedio) * 0.2
darf = imposto * quantidadeDeCotas 
lucro = ((valorDeVenda - precoMedio) * quantidadeDeCotas) - darf
prejuizo = ((valorDeVenda - precoMedio) * quantidadeDeCotas)

if lucro > 0:
    if darf >= 10:
        print('Seu lucro líquido na operação foi de R${:.2f} e você precisará emitir um DARF no valor de R${:.2f} até o último dia útil de {}.'.format(lucro, darf, pegar_mes(proximoMes)))
    else:
        print('Seu lucro líquido na operação foi de R${:.2f} e você por enquanto não precisa emitir um DARF no valor de R${:.2f}, mas precisa contabilizar esse valor com outras vendas futuras.'.format(lucro, darf))
else:
    print('Seu prejuízo na operação foi de R${:.2f} e você poderá contabilizar esse prejuízo com outras vendas futuras para compensação.'.format(abs(prejuizo)))

# desenvolvido por carlos felipe araújo @carlosxfelipe
