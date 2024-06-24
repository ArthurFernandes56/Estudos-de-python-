# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto 

preco= float(input('Informe o valor do produto: '))
nPreco= preco*0.75
print('Aplicando o desconto de 5% o produto passa a valer: R$ {:.2f}'.format(nPreco))