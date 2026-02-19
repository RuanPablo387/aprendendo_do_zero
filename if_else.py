#Um lutador precisa bater o peso para sua luta, em sua categoria o peso maximo é 62.6kgs
peso_maximo = 62.6
peso_lutador=float(input('Qual o seu peso?'))
if peso_lutador > peso_maximo:
 print ('Infelizmente, você não bateu o peso. Está desclassificado.')
else:
 print('Parabens, voce bateu o peso, boa sorte na sua luta.')