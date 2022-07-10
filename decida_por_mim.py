from random import random

respostas = ["sim","não","talvez", "claro que sim", "claro que não","espere por 1 dia para decidir","espere por 3 dias para decidir", "espere por 1 semana para decidir", "espere por 1 mês para decidir", "decida por você, mas pense bem antes de fazer sua escolha", "melhor tentar do que não tentar" ]
numeroMaximo= len(respostas) + 1
numeroAleatorio = int(random()*numeroMaximo)
input("Esse programa te auxilia em sua decisão de forma aleatória. Por favor, faça uma pergunta que exija uma resposta afirmativa ou negativa.\r\n")
print(respostas[numeroAleatorio])