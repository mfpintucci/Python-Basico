num = int(input('Digite um número : '))
u= num // 1 % 10
d= num // 10 % 10
c= num // 100 % 10
m= num // 1000 % 10

print (' A unidade desse número é {} '.format(u))
print (' A dezena desse número é {} '.format(d))
print (' A centena desse número é {} '.format(c))
print (' O milhar desse número é {} '.format(m))
