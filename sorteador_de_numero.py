from random import random

n = int(input("Este programa sorteia números. Ele sorteia um número de 0 até um número máximo de sua escolha. Digite um número máximo para ele sortear um número."))
n= n+1
for i in range(0,6):
  x = int(random()*n)
  print(str(x))