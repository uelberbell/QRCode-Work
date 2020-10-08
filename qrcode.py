import pyqrcode
from pyqrcode import QRCode
import array as arr
import png
import sys


cdBarras = []

print('            ||||||||CONVERTER CÓDIGO DE BARRAS PARA QRCODE||||||||')
print('            _____________________________________________________\n')

#Aqui nós pediremos ao usuário a quantidade de produtos que ele irá inserir 
n = int (input('Digite a quantidade de produtos que serão lidos: '))

#Condição para para solicitar quantas vezes o programa vai solicitar dados
for i in range(0, n):
    print("Digite o código de barras" , i + 1, ":")
    item = input()  
    arquivo = open('codigos.txt' , 'a')
    arquivo.write(item + "\nEnter\n")
    print("Nome do arquivo de texto: " , arquivo.name)
    arquivo.close()
    #cdBarras.append(item)
    #print(cdBarras)
    
arquivo = open('codigos.txt' , 'r')
for linha in arquivo:
    linha = linha.rstrip()
    print(linha)
arquivo.close()   


url = pyqrcode.create('codigos.txt')
n = input('\nDigite o nome do cliente: ')    
url.svg(n +".svg" , scale = 8)
url.png(n + ".png" , scale = 6)
print('\n>>>>QRCODE SALVO NA PASTA DO PROGRAMA<<<<')






