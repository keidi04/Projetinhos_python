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

def pegaNumeroSortido(numeroMaximo):
  numeroMaximo= numeroMaximo + 1
  numeroAleatorio = int(random()*numeroMaximo)
  return numeroAleatorio

def func0(chute,numeroSortido):
  if chute == numeroSortido:
    return mostrarTelaDeSucesso(numeroSortido)

def func1(chute,numeroSortido,numeroMaximo):
  if chute < numeroSortido:
    return mostrarTelaChuteFoiMenor(numeroMaximo)

def func2(chute,numeroSortido,numeroMaximo):
  if chute > numeroSortido:
    return mostrarTelaChuteFoiMaior(numeroMaximo)

def casoPararPrograma(window,janela1,janela2,janela3,janela4,janela5,events):
  return (window == janela1 or window == janela2 or window == janela3 or window == janela4 or window == janela5 ) and (events == sg.WIN_CLOSED or events == "Fechar")
    
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
  if casoPararPrograma(window,janela1,janela2,janela3,janela4,janela5,events):
    break
  elif window == janela1 and events == "Sortear":
    numeroMaximo = int(values['numero'])
    numeroSortido = pegaNumeroSortido(numeroMaximo)
    janela1.hide()
    janela2 = mostrarTelaPrimeiroChute(numeroMaximo)
  elif window == janela2 and events == "Chutar Número":
    chute = int(values['numero'])
    janela2.hide()
    janela5 = func0(chute,numeroSortido)
    janela3 = func1(chute,numeroSortido,numeroMaximo)
    janela4 = func2(chute,numeroSortido,numeroMaximo)
  elif window == janela3 and events == "Chutar Número":
    chute = int(values['numero'])
    janela3.hide()
    janela5 = func0(chute,numeroSortido)
    janela3 = func1(chute,numeroSortido,numeroMaximo)
    janela4 = func2(chute,numeroSortido,numeroMaximo)
  elif window == janela4 and events == "Chutar Número":
    chute = int(values['numero'])
    janela4.hide()
    janela5 = func0(chute,numeroSortido)
    janela3 = func1(chute,numeroSortido,numeroMaximo)
    janela4 = func2(chute,numeroSortido,numeroMaximo)
  elif  window == janela5 and events == "Advinhar Outro Número":
    janela5.hide()
    janela1 = mostrarTelaInicial()