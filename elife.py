peso_boxeador=float(input('Qual o seu preso?'))
abaixo_do_peso=60
acima_do_peso=62.6
if peso_boxeador < abaixo_do_peso:
 print('Voce esta baixo do peso')
elif peso_boxeador <= acima_do_peso:
 print('Boa, bateu o peso')
else:
 print('voce esta acima do peso')
