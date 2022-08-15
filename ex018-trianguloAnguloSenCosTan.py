#ler um angulo qualquer e mostrar seno, cosseno e tangente do triangulo
#usar biblioteca com modulo de matematica de trigonometria

import math


ang = float(input('Digite um angulo: ')) 

print('Relaçoes trigonometricas: seno= {:.2f}, cosseno= {:.2f}, tangente= {:.2f}'
.format(math.sin(math.radians(ang)),math.cos(math.radians(ang)),math.tan(math.radians(ang))))
