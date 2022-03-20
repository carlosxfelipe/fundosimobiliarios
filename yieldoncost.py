print('-=-' * 20)
print('Calculando Yield on Cost (YOC) de FIIs')
print('-=-' * 20)

preco_aquisicao = float(input('Qual seu custo médio de aquisição? ').replace(',', '.'))
preco_aquisicao * 100
rendimento = float(input('Quanto rendeu no último mês? ').replace(',', '.'))
rendimento * 12
yield_on_cost = rendimento / preco_aquisicao * 100

print('Seu yield on cost foi de {:.3f}% nesse mês.'.format(yield_on_cost))
print('A rentabilidade anualizada seria {:.3f}%.'.format(yield_on_cost * 12))
