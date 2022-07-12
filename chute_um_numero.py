from random import random
from PySimpleGUI import PySimpleGUI as sg
# Layout e funções
def mostrarTelaInicial():
  sg.theme('Reddit')
  tela1=[
    [sg.Text('Este programa é um jogo para você advinhar um número aleatório.')],
    [sg.Text('Ele sorteia um número de 0 até um número máximo de sua escolha.')],
    [sg.Text('Depois te guia até acertar o número.')],
    [sg.Text('Digite um número máximo para ele sortear um número para você chutar depois.')],
    [sg.Text('Número Máximo:'),sg.Input(key='numero')],
    [sg.Button('Sortear')]
  ]
  return sg.Window("Tela Inicial",tela1, finalize=True)

def mostrarTelaPrimeiroChute(numeroMaximo):
  sg.theme('Reddit')
  tela2=[
    [sg.Text('Chute um numero entre 0 e ' + str(numeroMaximo))],
    [sg.Text('Chute:'),sg.Input(key='numero')],
    [sg.Button('Chutar Número')]
  ]
  return sg.Window("Guia",tela2, finalize=True)

def mostrarTelaChuteFoiMenor(numeroMaximo):
  sg.theme('Reddit')
  tela3=[
    [sg.Text('O seu chute foi menor que o número sortido')],
    [sg.Text('Chute um numero entre 0 e ' + str(numeroMaximo))],
    [sg.Text('Chute:'),sg.Input(key='numero')],
    [sg.Button('Chutar Número')]
  ]
  return sg.Window("Guia",tela3, finalize=True)

def mostrarTelaChuteFoiMaior(numeroMaximo):
  sg.theme('Reddit')
  tela4=[
    [sg.Text('O seu chute foi maior que o número sortido')],
    [sg.Text('Chute um numero entre 0 e ' + str(numeroMaximo))],
    [sg.Text('Chute:'),sg.Input(key='numero')],
    [sg.Button('Chutar Número')]
  ]
  return sg.Window("Guia",tela4, finalize=True)

def mostrarTelaDeSucesso(numeroSortido):
  sg.theme('Reddit')
  tela5=[
    [sg.Text('Você descobriu o número sortido.')],
    [sg.Text('O número sortido foi o ' + str(numeroSortido))],
    [sg.Button('Advinhar Outro Número'),sg.Button('Fechar')]
  ]
  return sg.Window("Guia",tela5, finalize=True)

def pulaLinhaNoConsole():
  print("\r\n")

def pegaNumeroMaximo():
  numeroMaximo = int(input("Este programa é um jogo para você acertar um número. Ele sorteia um número de 0 até um número máximo de sua escolha e depois te guia até acertar o número. Digite um número máximo para ele sortear um número para você chutar depois:\r\n"))
  return numeroMaximo

def pegaChuteInicial(numeroMaximo):
  chute = int(input("Chute um numero entre 0 e " + str(numeroMaximo) + ":\r\n"))
  return chute

def pegaNumeroSortido(numeroMaximo):
  numeroMaximo= numeroMaximo + 1
  numeroAleatorio = int(random()*numeroMaximo)
  return numeroAleatorio

def mostraAcertoDoChute(chute,numeroSortido):
  if chute == numeroSortido :
    pulaLinhaNoConsole()
    print("Você descobriu o número sortido. O número sortido foi o " + str(numeroSortido))

def pedeChuteNovamente():
  chute = int(input("Por favor, chute novamente um número. Digite seu chute:"))
  return chute

def continuaTentandoChutar(chute,numeroSortido):
  while chute != numeroSortido:
    if chute > numeroSortido:
      pulaLinhaNoConsole()
      print("O seu chute foi maior que o número sortido")
      chute = pedeChuteNovamente()
    if chute < numeroSortido:
      pulaLinhaNoConsole()
      print("O seu chute foi menor que o número sortido")
      chute = pedeChuteNovamente()
    mostraAcertoDoChute(chute,numeroSortido)

# Telas 
janela1 = mostrarTelaInicial()
janela2 = None
janela3 = None
janela4 = None
janela5 = None
numeroMaximo = 0
numeroSortido = 0
chute = 0
# Loop
while True:
  window, events, values = sg.read_all_windows()
  if (window == janela1 or window == janela2 or window == janela3 or window == janela4 or window == janela5 ) and (events == sg.WIN_CLOSED or events == "Fechar"):
    break
  elif window == janela1 and events == "Sortear":
    numeroMaximo = int(values['numero'])
    numeroSortido = pegaNumeroSortido(numeroMaximo)
    janela1.hide()
    janela2 = mostrarTelaPrimeiroChute(numeroMaximo)
  elif window == janela2 and events == "Chutar Número":
    chute = int(values['numero'])
    if chute == numeroSortido:
      janela2.hide()
      janela5 = mostrarTelaDeSucesso(numeroSortido)
    elif chute < numeroSortido:
      janela2.hide()
      janela3 = mostrarTelaChuteFoiMenor(numeroMaximo)
    elif chute > numeroSortido:
      janela2.hide()
      janela4 = mostrarTelaChuteFoiMaior(numeroMaximo)
  elif window == janela3 and events == "Chutar Número":
    chute = int(values['numero'])
    if chute == numeroSortido:
      janela3.hide()
      janela5 = mostrarTelaDeSucesso(numeroSortido)
    elif chute < numeroSortido:
      janela3 = mostrarTelaChuteFoiMenor(numeroMaximo)
    elif chute > numeroSortido:
      janela3.hide()
      janela4 = mostrarTelaChuteFoiMaior(numeroMaximo)
  elif window == janela4 and events == "Chutar Número":
    chute = int(values['numero'])
    if chute == numeroSortido:
      janela4.hide()
      janela5 = mostrarTelaDeSucesso(numeroSortido)
    elif chute < numeroSortido:
      janela4.hide()
      janela3 = mostrarTelaChuteFoiMenor(numeroMaximo)
    elif chute > numeroSortido:
      janela4 = mostrarTelaChuteFoiMaior(numeroMaximo)
  elif window == janela5 and events == "Advinhar Outro Número":
    janela5.hide()
    janela1 = mostrarTelaInicial()