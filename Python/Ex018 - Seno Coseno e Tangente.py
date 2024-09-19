from math import sin,cos,tan, radians

a= float(input('Digite um ângulo: '))

cos=float(cos(radians(a)))
sen=float(sin(radians(a)))
tang=float(tan(radians(a)))


print ('O seno do ângulo digitado é {:.2f}'.format(sen))
print ('O cosseno do ângulo digitado é {:.2f} '.format (cos))
print ('A tangente do ângulo digitado é {:.2f}'.format (tang))
