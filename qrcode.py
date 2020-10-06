import pyqrcode
from pyqrcode import QRCode
import array as arr
import png
import sys


cdBarras = []
#print('DIGITE "0" A QUALQUER MOMENTO PARA ENCERRAR O PROGRAMA!')

#while(cdBarras != 0):
 #   cdBarras = str (input('Digite o código de barras: '))
  #  #s += "\nEnter" comando para gerar a tecla enter após captar o código de barras.
   # if(cdBarras == '0'):
    #    print('SISTEMA ENCERRADO')
     #   break
print('            ||||||||CONVERTER CÓDIGO DE BARRAS PARA QRCODE||||||||')
print('            _____________________________________________________\n')



#Aqui nós pediremos ao usuário a quantidade de produtos que ele irá inserir 
n = int (input('Digite a quantidade de produtos que serão lidos: '))

#Condição para para solicitar quantas vezes o programa vai solicitar dados
for i in range(0, n):
    print("Digite o código de barras" , i + 1, ":")
    item = input()  
    cdBarras.append(item)
    print(item)

#Exibindo lista de códigos capturados    
print("\n Dados do QRCODE: ", cdBarras)

#Pegando dados capturados e jogando numa unica variável para criar o Qrcode
lista = str (cdBarras)
#Convertendo para String

#Tentativa de formatação de lista
 
lista = str(cdBarras).strip("[],''")


url = pyqrcode.create(lista)
n = input('\nDigite o nome do cliente: ')    
url.svg(n +".svg" , scale = 8)
url.png(n + ".png" , scale = 6)
print('\n>>>>QRCODE SALVO NA PASTA DO PROGRAMA<<<<')
print("\n Dados do QRCODE: ", dados)






