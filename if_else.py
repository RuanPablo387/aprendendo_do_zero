# Um lutador precisa bater o peso para sua luta, em sua categoria o peso maximo é 62.6kgs
peso_maximo = 62.6
peso_lutador=float(input('Qual o seu peso?'))
if peso_lutador > peso_maximo:
 print ('Infelizmente, você não bateu o peso. Está desclassificado.')
else:
 print('Parabens, voce bateu o peso, boa sorte na sua luta.')

# Mesma coisa mas agora ultilzando o elif
peso_boxeador=float(input('Qual o seu preso?'))
abaixo_do_peso=60
acima_do_peso=62.6
if peso_boxeador < abaixo_do_peso:
 print('Voce esta abaixo do peso')
elif peso_boxeador <= acima_do_peso:
 print('Boa, bateu o peso')
else:
 print('voce esta acima do peso')


# Mais um pra praticar
velocidade_maxima=70
velocidade_carro=float(input('Qual velocidade seu carro estava quando passou pelo radar?'))
if velocidade_carro >= 100:
 print('Voce ultrapassou por muito o limite de velocidade permitido pela via, portanto vai receber uma multa GRAVE')
elif velocidade_carro > velocidade_maxima:
 print('Infelizmente seu carro ultrapassou o limite de velocidade nessa via e voce foi multado')
else:
 print('voce nao ultrapassou o limite permitido pela via, pode seguir viagem')
