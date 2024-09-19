d = float(input('Quantos dias o carro ficou alugado? '))
k = float(input('Quantos kilometros foram rodados neste período? '))

v = (d * 60) + (k * 0.15)

print('O valor a pagar pelo veículo é R$ {:.2f} .' .format (v))
