from random import random

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

numeroMaximo = pegaNumeroMaximo()
chute = pegaChuteInicial(numeroMaximo)
numeroSortido = pegaNumeroSortido(numeroMaximo)

mostraAcertoDoChute(chute,numeroSortido)

continuaTentandoChutar(chute,numeroSortido)