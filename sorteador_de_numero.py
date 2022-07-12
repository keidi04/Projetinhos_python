from random import random
from PySimpleGUI import PySimpleGUI as sg

# Layouts
def mostraTelaInicial():
  sg.theme('Reddit')
  tela1=[
    [sg.Text('Este programa sorteia números.')],
    [sg.Text('Ele sorteia um número de 0 até um número máximo de sua escolha.')],
    [sg.Text('Digite um número máximo para ele sortear um número.')],
    [sg.Text('Número Máximo:'),sg.Input(key='numero')],
    [sg.Button('Sortear')]
  ]
  return sg.Window("Tela Inicial",tela1, finalize=True)

def mostraTelaFinal(numero):
  sg.theme('Reddit')
  tela2=[
    [sg.Text('O número sorteado foi o número '+ str(numero))],
    [sg.Button('Sortear Número Novamente')]
  ]
  return sg.Window("Tela Final",tela2, finalize=True)

# Janelas
janela1,janela2 = mostraTelaInicial(),None

# Loop
while True:
  window, events, values = sg.read_all_windows()
  if (window == janela1 or window == janela2) and events == sg.WIN_CLOSED:
    break
  if window == janela1 and events == 'Sortear':
    numeroMaximo = int(values['numero'])
    numeroMaximo = numeroMaximo + 1
    numeroAleatorio = int(random()*numeroMaximo)
    janela1.hide()
    janela2 = mostraTelaFinal(numeroAleatorio)
  elif window == janela2 and events == 'Sortear Número Novamente':
    janela2.hide()
    janela1 = mostraTelaInicial()
