import matematica
from meu_pacote import matematica, saudacoes
from calculadora import somar, potencia, celsius_para_fahrenheit

#result_soma = matematica.somar(200, 555)
#result_subtracao = matematica.subtrair(543, 6)
#print('Soma: ', result_soma)
#print('Subtracao: ', result_subtracao)



# usando os modulos do meu pacote
resultado_multi =  matematica.multiplicar(33, 9)
#print('Multiplicacao: ', resultado_multi)
#saudacoes.dizer_adeus()


# usando o meu pacote calculadora.
print(somar(10, 5))
print(potencia(2, 3))
print(celsius_para_fahrenheit(100))