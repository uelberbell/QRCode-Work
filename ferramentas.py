author = 'uelber'
import os, sys


#ORGANIZANDO TOPO DA TELA
print('     -------------------------------------------------')
print ('         ||||||||FERRAMENTAS PARA TESTES|||||||||')
print('______________________________________________________________')


#DECLARANDO ALGUMAS VARIÁVEIS 
site = ''
ip = 00000000000000
ping = 'ping'
opcao = '1'
ipconfig = 'ipconfig'
getmac = 'getmac'
netstat = 'netstat -a -o'
winver = 'winver'


#CAPTURANDO OPÇÃO ESCOLHIDA PELO USUÁRIO E CONDIÇÃO PARA DECISÃO
while (opcao != '0'):
    print('\n       ________[ESCOLHA UMA DAS OPÇÕES ABAIXO!]________')
    opcao = input("\n[2] Testar PING \n[3] Testar INTERNET \n[4] Quais são os meus IPs? \n[5] Quais são meus MACs? \n[6] Scan de portas do seu PC com NETSTAT" +
    "\n[7] Qual a versão do meu Windows \n[8] Reiniciar fila de impressão \n[0] Sair\n\n")
    if (opcao == '2'):
        ip = input("Digite o endereço IP: ")
        os.system(ping + " " + ip)
    elif (opcao == '3'):
        site = input("Digite uma URL para testar a conexão: ")
        os.system(ping + " " + site)
    elif (opcao == '4'):
        os.system(ipconfig)
    elif (opcao == '5'):
          os.system(getmac) 
    elif (opcao == '6'):
       os.system(netstat) 
    elif (opcao == '7'):
        os.system(winver) 
    elif (opcao == '8'):
        print("Esta função está indisponível no momento. Escolha outra")
    elif (opcao == '0'):
        print("Programa encerrado")








