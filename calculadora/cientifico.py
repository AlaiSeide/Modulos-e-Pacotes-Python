"""
Potência (base, expoente):
O que é?
Potência é como fazer uma multiplicação repetida.
A base é o número que você vai multiplicar, e o expoente diz quantas vezes você vai multiplicar esse número por ele mesmo.

Exemplo:
Se a base é 2 e o expoente é 3, isso quer dizer que você vai multiplicar o número 2 por ele mesmo 3 vezes:
2 * 2 * 2 = 8

Então, 2 elevado a 3 (2³) é igual a 8.

Potência: É quando você multiplica o mesmo número várias vezes.
Exemplo: 2³ significa 2 * 2 * 2, que dá 8.
"""
def potencia(base, expoente):
    return base ** expoente

"""
Raiz quadrada (número):
O que é?
A raiz quadrada é o oposto da potência.
Ela responde à pergunta: "Qual número multiplicado por ele mesmo dá o número que estou pensando?"

Exemplo:
A raiz quadrada de 9 é 3, porque:
3 * 3 = 9

Raiz quadrada: É descobrir qual número multiplicado por ele mesmo dá o número que você tem.
Exemplo: A raiz quadrada de 9 é 3, porque 3 * 3 = 9.

"""
def raiz_quadrada(numero):
    return numero ** 0.5 # A raiz quadrada é o mesmo que elevar o número a 0.5