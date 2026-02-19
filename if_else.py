#Um lutador precisa bater o peso para sua luta, em sua categoria o peso maximo é 62.6kgs
peso_maximo = 62.6
peso_lutador=float(input('Qual o seu peso?'))
if peso_lutador > peso_maximo:
 print ('Infelizmente, você não bateu o peso. Está desclassificado.')
else:
 print('Parabens, voce bateu o peso, boa sorte na sua luta.')



peso_boxeador=float(input('Qual o seu preso?'))
abaixo_do_peso=59.9
acima_do_peso=62.7
peso_ideal=62.6
if peso_boxeador > abaixo_do_peso:
 print('Boa, bateu o peso')
elif peso_boxeador < acima_do_peso:
 print('Boa, bateu o peso')
else:
 print('infelizmente voce nao bateu o peso')

