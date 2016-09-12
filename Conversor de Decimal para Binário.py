# -*- coding: utf-8 -*-

print("+===================================+\n")
print("|Conversor de decimal para binario!!|\n")
print("+===================================+\n")

dec = int(input("Insira qualquer numero inteiro: "))
if dec < 0:
    print "\n**Numero convertido para positivo**"
    dec *= -1
lista = []
def conv_bin(dec2, lista, dec):
    while dec2 != 0:
        dec1 = dec2 % 2
        dec2 = dec2 / 2
        dec1 = "%s" % dec1
        lista.append(dec1)
    lista.reverse()
    print "\n%s em binario eh:" % dec, "".join(lista)
conv_bin(dec, lista, dec)
input("")
