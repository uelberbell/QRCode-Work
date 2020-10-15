import pyqrcode
import qrcode
from pyqrcode import QRCode
import array as arr
import png
import sys


print('            ||||||||CONVERTER CÓDIGO DE BARRAS PARA QRCODE||||||||')
print('            _____________________________________________________\n')



#Aqui nós pediremos ao usuário a quantidade de produtos que ele irá vender 
n = int (input('Digite a quantidade de produtos que serão lidos: '))

      
      
#Condição para para solicitar quantas vezes o programa vai solicitar dados
for i in range(0, n):
    print("Digite o código de barras" , i + 1, ":")
    item = input()
    arquivo = open('codigos.txt' , 'a')
    arquivo.write(item + "\nEnter\n")
    print("Nome do arquivo de texto: " , arquivo.name)
    arquivo.close()
        


arquivo = open('codigos.txt' , 'r')
for linha in arquivo:           
    linha = linha.rstrip()
    print(linha)
arquivo.close()   


#Ainda preciso achar uma forma de ler cada linha do arquivo .txt e criar o qrcode com a formatação contida dentro do arquivo.
url = pyqrcode.create("ainda precisamos saber o que entrar aqui para ler todo arquivo txt com os códigos de barras")
n = input('\nDigite o nome do cliente: ')  
url.svg(n +".svg" , scale = 8)
url.png(n + ".png" , scale = 6)
print('\n>>>>QRCODE SALVO NA PASTA DO PROGRAMA<<<<')






