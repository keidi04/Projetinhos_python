from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import calendar

def QuantosDiasFaltam(mes, dia):
    hoje = date.today()
    ano = hoje.year
    dataProcurada = date(ano, mes, dia)

    qtosDias = dataProcurada - hoje
    qtosDiasInt = int(str(qtosDias).replace("days, 0:00:00", "")) 
    if qtosDiasInt < 0:
      ano = ano +1
      dataProcurada = date(ano,mes,dia)
      qtosDias = dataProcurada - hoje
    mensagemRetorno = "Faltam " + str(qtosDias).replace("days, 0:00:00", "") + " dias para o seu próximo aniversário " + dataProcurada.strftime("%d/%m/%y")
    print(mensagemRetorno)
    return ano

def CalendarioTexto(ano,mes):
    calendarioTexto = calendar.TextCalendar(calendar.SUNDAY)
    txtCalendario = calendarioTexto.formatmonth(ano, mes)
    print (txtCalendario)

def CalendarioHTML(ano,mes):
    calendarioHTML = calendar.HTMLCalendar(calendar.SUNDAY)
    htmlCalendario = calendarioHTML.formatmonth(ano,mes)
    return htmlCalendario

def apresentaPrograma():
    input("Este programa calcula quantos dias faltam para você completar mais um ano e quantos anos você tem. Aperte enter para continuar!")

def calculaIdade(dia,mes,ano):
    hoje = date.today()
    dataDeNascimento = date(ano, mes, dia)

    qtosDias = hoje - dataDeNascimento
    days = qtosDias.days
    years, days = days // 365, days % 365
    months, days = days // 30, days % 30

    # seconds = qtosDias.seconds
    # hours, seconds = seconds // 3600, seconds % 3600
    # minutes, seconds = seconds // 60, seconds % 60

    print("Você tem {} anos, {} meses e {} dias".format(years, months, days))
    return years

def personalizaCalendario(calendario,diaAniversario):
    if diaAniversario == 1:
        calendario = calendario.replace('>1<', ' style="font-weight: bolder">1<')
    elif diaAniversario == 2:
        calendario = calendario.replace('>2<', ' style="font-weight: bolder">2<')
    elif diaAniversario == 3:
        calendario = calendario.replace('>3<', ' style="font-weight: bolder">3<')
    else:
        calendario = calendario.replace('>' + str(diaAniversario), ' style="font-weight: bolder">' + str(diaAniversario))
    return calendario

def criaArquivoCalendario(texto):
  arquivo = open("calendario.html","w+")
  arquivo.write(texto + "\r\n")
  arquivo.close

apresentaPrograma()
diaAniversario = int(input("Em que dia do mês você nasceu?"))
mesAniversario = int(input("Em que mês você nasceu?"))
anoNascimento = int(input("Em que ano você nasceu?"))

anoAniversario = QuantosDiasFaltam(mesAniversario, diaAniversario)

calculaIdade(diaAniversario,mesAniversario,anoNascimento)
#CalendarioTexto(anoAniversario,mesAniversario)
calendario1 = CalendarioHTML(anoAniversario,mesAniversario)
calendario1 = personalizaCalendario(calendario1,diaAniversario)
calendario2 = CalendarioHTML(anoNascimento,mesAniversario)
calendario2 = personalizaCalendario(calendario2,diaAniversario)

criaArquivoCalendario(calendario1 + calendario2)


