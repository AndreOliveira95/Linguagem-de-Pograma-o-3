'''
Created on 9 de mar de 2017

@author: Andre
'''
from math import log

number = int(input("Tamanho da mensagem?"))

bits = int(log(number, 2)+1)

print("Quantidade de bits = {0}" .format(bits))