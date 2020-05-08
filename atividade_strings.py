#IMPORTES DE BIBLIOTECAS
#importa o módulo utilizado na 4ª questão da bibloteca padrão do Python datetime
from datetime import datetime


#DEFINÇÃO DE FUNÇÕES
#Define a função que imprime os quatro primeiros caracteres da palavra digitada
def fistFour(word):
    if len(word) >= 4:
        print("""As quatro primeiras letras da palavra {} são:""".format(word))
        for letter in range(4):
            print(letter+1 ,"-", word[letter])

    else:
        print("""A palavra {} tem menos de 4 letras.
As {} letras da palavra {} são:""".format(word, str(len(word)), word))
        for letter in range(len(word)):
            print(letter+1 ,"-", word[letter])


#Define a função que imprime a quantidade escolhida de caracteres da palavra digitada
def numberOfLetters(wordinput, numberofletters):
    if len(wordinput) >= numberofletters:
        print("""As {} primeiras letras da palavra {} são:""".format(numberofletters, wordinput, numberofletters))
        for letter in range(numberofletters):
            print(letter+1 ,"-", wordinput[letter])

    else:
        print("""Você digitou um número maior do que
a quantidade de letras da palavra {}.
As {} letras de {} são:""".format(wordinput, str(len(wordinput)), wordinput))
        for letter in range(len(wordinput)):
            print(letter+1 ,"-", wordinput[letter])
        

#Define a função que verifica se a primeira letra de uma palavra é vogal
def isVowel(wordvowel):
    vowels = ["A", "Á", "À","Â", "Ã", "E","É","Ê", "I", "Í", "O", "Ó","Ô","Õ", "U", "Ú"]
    if wordvowel[0].upper() in vowels:
        print("A palavra {} inicia com uma vogal - {}.".format(wordvowel, wordvowel[0]))

    else:
        print("""A palavra {} não inicia com uma vogal, pois, letra {} é uma consoante.
""".format(wordvowel, wordvowel[0]))


#Define a função que obtêm uma data específica
def dateInput(dateinput):
    try:
        date = datetime.strptime(dateinput, '%d/%m/%Y').date()
        print("""Dia: {}
Mês: {}
Ano: {}
""".format(date.day, date.month, date.year))

    except:
        print("""Parece que há  algo de errado com a sua entrada!
Por favor, verifique se o valor está no formato dd/mm/aaaa
ou se o valor {} é uma data válida.""".format(dateinput))
        dateInput(input("Digite uma data específica: "))
    

#CHAMAMENTO DAS FUNÇÕES DO PROGRAMA

print("""IFS - Instituto Federal de Sergipe - CAMPUS PROPRIÁ

ALUNO: Ginaldo Laranjeiras Júnior       Data: 06/05/2020
Profa.: Danielle Amaral Menéndez        Disciplina: Fundamentos de Programação

Respondendo à Atividade -  Manipulação de Strings

OBS.: Todas as perguntas foram respondidas em um único arquivo.
Usei o exercício para praticar também funções em Python
""")

print("Questão 1: ")
#Chama a função que imprime os quatro primeiros caracteres da palavra digitada passando como parâmetro uma palavra
fistFour((input("Digite uma palavra: ")))

print("Questão 2: ")
#Chama a função que imprime a quantidade escolhida de caracteres da palavra digitada passando como parâmetro uma palavra e um número
numberOfLetters(
    (input("Digite uma palavra: ")),
    int(input("Digite a quantidade de letras que deseja imprimir: "))
)

print("Questão 3: ")
#Chama a função que verifica se a primeira letra de uma palavra é vogal passando como parâmetro uma palavra
isVowel(input("Digite uma palavra para verificar se ela inicia com uma vogal: "))

print("Questão 4: ")
#Chama função que obtêm uma data específica passando como parâmetro uma entrada
dateInput(input("Digite uma data específica: "))

